`tech-spec.md`

```markdown
# wiki-scribe — Technical Specification (v1)

## Stack
- **Language:** TypeScript (strict mode) end-to-end — shared types across web + worker.
- **Framework:** Next.js 15 (App Router) for the editor/admin UI + API routes; **Hono** for the standalone ingestion/generation worker (lightweight, edge-portable).
- **Runtime:** Node.js 20 LTS. React 19 frontend. Tailwind + shadcn/ui for the wiki/editor surface.
- **LLM layer:** Anthropic Claude (Haiku 4.5 for bulk extraction/spoiler-classification, Sonnet 4.6 for article drafting). Prompt caching ON for the per-wiki style/canon system prompt. Strict JSON tool-use for spoiler-tagging output.
- **Background jobs:** BullMQ on Redis (generation, re-index, spoiler-recheck are async — generation can take 20–90s/article and must not block requests).
- **Vector/search:** Postgres + `pgvector` (article-chunk embeddings for dedup, "related pages," and spoiler-context retrieval). Postgres FTS (`tsvector`) for keyword search — no separate Elastic in v1.
- **Embeddings:** `text-embedding-3-small` (1536-d) or Voyage; cheap, batched.

## Hosting (free-tier-first)
- **Web + API:** Vercel Hobby (Next.js native; generous free tier, preview deploys per-PR).
- **Worker:** Railway or Fly.io (one shared-CPU instance free/near-free; needs a long-running process BullMQ can't host on Vercel).
- **Postgres + pgvector:** Neon free tier (0.5 GB, branching for previews) or Supabase free (500 MB, includes auth + storage).
- **Redis:** Upstash Redis free tier (10k cmd/day — fine for early queue volume).
- **Object storage (images/exports):** Cloudflare R2 free tier (10 GB, zero egress) or Supabase Storage.
- **Migration path:** all components are container/Postgres-standard, so escape from any single free tier is a config change, not a rewrite.

## Data model (Postgres)
| Table | Key fields |
|---|---|
| `users` | id (uuid), email, auth_provider, created_at |
| `wikis` | id, owner_id→users, slug (unique), title, canon_description (text), style_guide (jsonb), visibility (`public`/`unlisted`/`private`), spoiler_policy (jsonb), created_at |
| `wiki_members` | wiki_id, user_id, role (`owner`/`editor`/`viewer`), invited_at |
| `pages` | id, wiki_id, slug, title, status (`draft`/`published`/`archived`), current_revision_id, qc_score (numeric), created_at, updated_at |
| `revisions` | id, page_id, content_md (text), author_kind (`llm`/`human`), model, prompt_hash, created_at, parent_revision_id |
| `spoiler_spans` | id, revision_id, start_offset, end_offset, milestone_id→milestones, confidence (numeric), source (`llm`/`human`), verified (bool) |
| `milestones` | id, wiki_id, label (e.g. "Chapter 12", "Season 2"), ordinal (int), description — the spoiler timeline a reader sets their position against |
| `sources` | id, wiki_id, kind (`url`/`upload`/`text`), uri, raw_text, ingested_at |
| `page_chunks` | id, page_id, revision_id, chunk_text, embedding (vector(1536)), ord |
| `qc_findings` | id, revision_id, type (`contradiction`/`tone`/`unsourced`/`spoiler-leak`), severity, message, span, resolved (bool) |
| `gen_jobs` | id, wiki_id, page_id, type, status, model, input_tokens, output_tokens, cost_cents, error, created_at, finished_at |
| `audit_log` | id, wiki_id, actor_id, action, target, meta (jsonb), created_at |

**Spoiler model is the differentiator:** spoilers are *spans tied to milestones*, not page-level flags. A reader viewing at `milestone.ordinal = 5` gets every span with a higher-ordinal milestone redacted server-side.

## API surface
| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/wikis` | Create a wiki (canon description + style guide → seeds system prompt). |
| `POST` | `/api/wikis/:id/sources` | Ingest source material (URL/upload/paste); enqueues chunk+embed. |
| `POST` | `/api/wikis/:id/pages:generate` | Generate a new page from a title + sources; returns `gen_job` id (async). |
| `GET` | `/api/jobs/:id` | Poll generation/QC job status + cost. |
| `GET` | `/api/wikis/:id/pages/:slug?milestone=N` | Fetch a page rendered with spoilers ≥ milestone N redacted. |
| `POST` | `/api/pages/:id/revisions` | Submit a human edit → new revision → triggers QC re-run. |
| `POST` | `/api/revisions/:id/qc` | Run automated quality control (contradiction/tone/unsourced/spoiler-leak). |
| `POST` | `/api/revisions/:id/spoilers:detect` | Re-classify spoiler spans against the milestone timeline. |
| `PUT` | `/api/spoiler_spans/:id` | Human verify/override a spoiler span (corrects LLM). |
| `POST` | `/api/wikis/:id/publish/:pageId` | Promote draft revision to published. |
| `GET` | `/api/wikis/:id/search?q=&milestone=N` | FTS + vector search, spoiler-filtered to reader's milestone. |

## Security model
- **Auth:** Supabase Auth (or Auth.js) — email magic-link + GitHub OAuth (target users are solo devs). Sessions via HTTP-only, `SameSite=Lax`, `Secure` cookies; short-lived JWT + refresh.
- **Authorization:** row-level via `wiki_members.role`. Enforced in a single `assertRole(userId, wikiId, min)` guard on every mutating route. If on Supabase, mirror with Postgres RLS policies as defense-in-depth.
- **Spoiler enforcement is server-side only** — redaction happens before serialization; raw spans never reach an under-milestone reader's client.
- **Secrets:** platform env vars only (Vercel/Railway encrypted env). `ANTHROPIC_API_KEY`, DB URL, Redis URL never in repo. `.env.example` documents keys; pre-commit `gitleaks` scan.
- **LLM safety:** per-wiki spend cap (`gen_jobs.cost_cents` rollup) with hard cutoff; prompt-injection mitigation — ingested source text is delimited and treated as untrusted data, never as instructions.
- **Abuse:** rate-limit generation endpoints per-user (Upstash ratelimit), input size caps on sources.
- **IAM:** least-privilege DB role for the app (no superuser); separate read-only role for analytics; scoped R2 token (PutObject on one bucket).

## Observability
- **Logs:** structured JSON (pino) → platform log drain; every request carries a `request_id`, every gen job a `job_id`. Ship to Better Stack / Axiom free tier.
- **Metrics:** generation latency p50/p95, tokens & cost per job, QC pass rate, spoiler-leak finding rate, queue depth/age. Exposed at `/api/metrics` (Prometheus text) or pushed to Grafana Cloud free tier.
- **Traces:** OpenTelemetry SDK spanning request → enqueue → LLM call → QC; one trace per generation. OTLP export to Grafana Tempo / Honeycomb free tier.
- **Product KPIs:** % LLM articles shipped without human edit, mean human-edit time saved, spoiler false-negative rate (the trust metric).
- **Alerts:** spend-cap breach, QC pass rate < 80%, queue age > 5 min, any unverified spoiler-leak finding on a published page.

## Build / CI
- **Monorepo:** pnpm workspaces (`web`, `worker`, `shared`). Turborepo for cached task graph.
- **CI (GitHub Actions):** on PR → typecheck (`tsc --noEmit`), lint (eslint + prettier), unit tests (Vitest), `gitleaks` secret scan, build. Migrations via Drizzle ORM (`drizzle-kit`), checked in and applied on deploy.
- **Tests:** unit on spoiler-redaction logic + role guards (security-critical); contract tests on the LLM JSON tool schemas; one e2e (Playwright) on generate→QC→publish→read-as-reader.
- **Deploy:** Vercel auto-deploy on merge to `main` w/ preview per PR; worker deploys via Railway GitHub integration. DB preview branches (Neon) per PR for safe migration testing.
- **Release gate:** no deploy if migration is non-additive without a reviewed expand/contract plan.
```