```markdown
# PRD: wiki-scribe
**Product Lead:** Senior Product/Engineering, Axentx
**Date:** 2026-05-23
**Repo:** arkashira/surrogate-1-harvest | Branch: wiki-scribe
**Linked Issues:** None (new initiative)

---

## Problem Statement
Solo developers and fan-wiki operators often struggle to maintain quality, consistency, and scalability in their wiki documentation. Manual content creation is time-consuming, error-prone, and difficult to standardize, leading to outdated or inconsistent information that frustrates users. Existing solutions do not provide AI-generated, spoiler-free, structured content with built-in quality control tailored for technical and fandom contexts.

---

## Target Users
1. **Solo Developers**
   - Building open-source projects with community-facing wikis
   - Need to document APIs, features, and usage without revealing future updates (spoilers)
   - Limited time for manual writing and editing

2. **Fan-Wiki Operators**
   - Managing wikis for franchises (games, anime, etc.)
   - Rely on community contributions but require consistency and editorial standards
   - Want to automate content generation while preserving lore accuracy

---

## Goals
| Goal | Success Criteria |
|------|------------------|
| **Generate quality wiki content** | >90% of generated articles rate ≥4/5 for readability and accuracy (internal QA) |
| **Spoiler-free generation** | 100% of generated content passes automated spoiler detection (custom classifier trained on franchise data) |
| **Automate quality control** | Reduce manual editing time per article by >70% via automated checks (grammar, tone, links, citations) |
| **Scalability** | Support 10,000+ articles with <2s generation latency per article (perf tested on AWS c6i.large) |
| **Portfolio synergy** | Reuse components from Axentx’s existing [iceoryx2 v0.9](https://github.com/iceoryx2) for fast IPC and data processing pipelines |

---

## Key Features (Prioritized)

### 1. Core Content Generation Engine (Must-Have)
- **Spoiler-Free LLM Pipeline**
  - Input: Git repo, issue tracker, or pre-filtered dataset (e.g., franchise lore DB)
  - Output: Wiki article drafts with spoilers masked (e.g., `{{spoiler:major_patch_v2}}`)
  - LLM Prompt Template: Structured system/user/assistant turns (reusing Axentx’s `system-user-assistant: 1.4M` pairs for instruction-following)
  - Supported formats: Markdown, HTML, MediaWiki wikitext

- **Context-Aware Drafting**
  - Integrate with repository files (README, CHANGELOG) or fan wiki dumps
  - Use Axentx’s `auto: 12.8M` open dataset pairs for technical writing patterns
  - Auto-cite sources with inline references (APA/MLA style)

### 2. Editorial Quality Control Suite (Must-Have)
- **Automated QA Checks**
  - Grammar/spelling (using `instr-resp: 6.4M` licensed Apache-2.0 models)
  - Tone consistency (e.g., neutral for technical docs, enthusiastic for fan wikis)
  - Link/anchor validation (checks for broken internal links)
  - Citation accuracy (scrape verify via web or DB queries)

- **Human-in-the-Loop Editor**
  - Web UI for reviewing/editing drafts (built with Axentx’s `messages: 4.3M` datasets for user-assistant interactions)
  - Diff viewer with side-by-side comparison (old vs. new version)
  - Approval workflow with optional Git commit hooks

### 3. Orchestration & Integration (Must-Have)
- **Pipeline Manager**
  - Input sources: GitHub/GitLab webhooks or manual uploads
  - Job queue with retries (using Axentx’s `pairs-B: 31.0M` async workflows)
  - Export options: Git commit, zip download, or direct MediaWiki API

- **Preview Server**
  - Live rendering in browser (using lightweight Markdown/HTML renderers from `instr-resp` repo)
  - Spoiler tag toggle for editors to verify masking

### 4. Advanced Features (Nice-to-Have)
- **Multi-Lingual Support**
  - Auto-translate drafts (powered by Axentx’s multilingual models from `auto: 12.8M`)
  - Language detection and style adaptation

- **Versioned Snapshots**
  - Save article revisions tied to Git commits (leveraging iceoryx2 IPC for fast blob storage)

- **Community Contribution Tools**
  - Gamified suggestions (e.g., upvote/downvote drafts)
  - Moderator dashboards for fan-wiki admins

---

## Assumptions
- Users have access to clean source data (e.g., Git repos, franchise lore DBs).
- API rate limits comply with target platforms (GitHub, MediaWiki).
- Deployment target: Single-tenant SaaS or self-hosted (Docker/K8s).

---

## Out of Scope
- **AI-generated images** (focus on text-only wiki content).
- **Real-time multiplayer editing** ( async workflows only).
- **Payment/subscription billing** (future add-on; start with free tier).
- **Spam/disinformation detection** (assume trustworthy input sources).

---

## Technical Stack
| Component | Tech | Source |
|-----------|------|--------|
| LLM Backend | vLLM (vllm-project/vllm) | Optimized inference engine |
| Structured Gen | SGLang (sgl-project/sglang) | Structured JSON outputs |
| Vector DB | pgvector | Shared BRAIN storage for context |
| IPC | iceoryx2 v0.9 | High-performance inter-process comms |
| Web UI | React + TypeScript | Leverage Axentx’s `messages` datasets |

---

## Success Metrics
| KPI | Target | Measurement |
|-----|--------|-------------|
| **Content Generation Speed** | ≤5 min/article (1000 tokens) | Internal perf suite |
| **Spoiler Detection Accuracy** | ≥99% recall | Custom classifier on test set |
| **Editorial Time Saved** | 70% reduction vs. manual wiki | Time-tracking in UI |
| **Adoption Rate** | 500+ active projects in 6 months | GitHub API + telemetry |
| **User Satisfaction** | ≥4.2/5 NPS | Post-task survey in product |

---

## Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| **Off-Topic/Inaccurate Content** | High | Fine-tune on project-specific heuristics (e.g., exclude CHANGELOG “Upcoming” lines) |
| **Spoiler Bypass** | Critical | Regular human audits + stronger prompt guardrails |
| **Performance Degradation** | High | Iceoryx2 IPC + batching via `pairs-D` async loops |

---
## Milestones & Timeline
| Phase | Goal | ETA |
|-------|------|-----|
| 1. Alpha | Core generation + QA pipeline | 2026-08-08 |
| 2. Beta | Multi-repo integration + spoiler masking | 2026-09-19 |
| 3. Launch | Public SaaS + GitHub App | 2026-10-31 |
```
