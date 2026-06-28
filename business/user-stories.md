Generated `user-stories.md` for **wiki-scribe** — 13 stories across 4 epics, Connextra format, each with 3–5 acceptance criteria and S/M/L complexity.

Key decisions:
- **Epic structure** mirrors the hypothesis's two halves (spoiler-free generation + automated QC) plus the two enablers they depend on (chronology-tagged ingestion, and publishing/ops).
- **The defensible wedge** is isolated and called out: the *enforceable spoiler horizon backed by chronology-tagged provenance* (US-1.1 + US-3.1 + US-3.2) — the one thing Fandom/Wiki.js and raw LLM writers structurally can't do. Acceptance criteria are written to be testable against it (e.g. ≤5% leak false-negative, additive-only horizon monotonicity, ≥80% traceability gate).
- **Cost visibility** (US-4.3) is in because the BD persona is explicitly solo/cost-sensitive — a wiki you can't afford to regenerate is dead on arrival.
- Added an **MVP critical path** and a **scope guardrail** for the downstream PRD/architect so they don't rebuild a generic wiki CMS.

Note: the file at `/tmp/user-stories.md` previously held a different product (`cloud-nexus`) — I overwrote it with the wiki-scribe deliverable.