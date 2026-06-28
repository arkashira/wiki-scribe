## Customer Segments
- Solo developers managing public-facing documentation or fan-wikis (e.g., indie game devs, open-source maintainers)
- Fan-wiki operators (communities maintaining continuous documentation for franchises like TV series, games, or comics)
- Small-to-medium content teams (2–20 people) needing automated spoiler-free wiki generation (e.g., anime wiki administrators)
- Educational institutions documenting curricula or project wikis with non-disclosure constraints
- Indie publishers launching interactive fiction or choose-your-own-adventure media requiring low-maintenance wiki infrastructure

## Value Propositions
- **Automated spoiler-free wiki generation**: LLM generates wiki pages from raw content (PDFs, transcripts, scripts, GitHub READMEs) with zero cross-contamination between arcs/chapters
- **Built-in spoiler detection & redaction**: Proprietary model filters and suppresses explicit/forbidden terms based on configurable rulesets (e.g., character names, cliffhangers)
- **Self-healing content**: Continuous quality control via periodic LLM-driven consistency checks; flags contradictions, dead links, or factual drift
- **One-click publishing**: Integrates with Docusaurus, MkDocs, MediaWiki; supports GitHub Pages, Netlify, Vercel deploy
- **Multilingual & font support**: Outputs spoiler-free wikis in Thai, Japanese, Arabic, and Latin scripts without needing localization teams
- **Cost redux threshold**: 60% faster wiki production vs. manual entry (benchmarked at 2 developer-days saved per 100 pages)

## Channels
- **Open-core GitHub repo**: `axentx/wiki-scribe` (core open-source; extensions/pro features closed) with 10,000+ monthly preview downloads projected by M3
- **Product Hunt launch** + curated tech newsletters (`TLDR`, `Indie Hackers`) featuring “AI-powered spoiler-safe wikis for fan communities”
- **Influencer seeding**: Provide Pro licenses (value $199/yr) to indie streamers who document games/TV—grow word-of-mouth via live citations in stream overlays
- **Sponsorships**: Partner with indie game bundles (e.g., itch.io Humble bundles) offering bundled Pro licenses as bonus
- **SEO long-tail**: Target keywords like “automated wiki spoiler filter”, “generate spoiler-free fan wiki”, “LLM wiki editor open-source”

## Customer Relationships
- **Self-serve onboarding**: 3-step guided setup (upload repo, set spoiler rules, generate HTML export) with 90-second tutorial video
- **Community Slack + Discord**: Public channel for fan-wiki admins; Axentx team hosts biweekly AMA on advanced rule templating
- **Pro ticket escalation**: 24h SLA for paid users on spoiler-exfiltration incidents (e.g., accidental leak → corrected version within 24h)
- **Automated ROI emails**: Monthly dashboard showing pages created, spoiler saves, and time-money equivalence vs. manual labor
- **Viral unlocks**: Free users can share editable link previews; Pro required for private wikis & API keys

## Revenue Streams
- **Pro tier**: $19/mo or $199/yr per wiki (≈ THB 630 / 6,600)
  - Private repo sync, API keys (5,000 requests/month), spoiler-rule templates, priority linting
- **Team tier**: $99/mo or $990/yr for 5 wikis (≈ THB 3,200 / 32,000)
  - Role-based access, audit logs, dedicated channel support, SLA 8h
- **Enterprise**: Custom pricing per 50+ wikis; includes on-prem/air-gap deploy + 20h/yr of manual spoiler-rule consultation
- **Extensions marketplace**: Sell premium rule packs (e.g., “Starfield armor spoiler rules” $49/yr) with 40% rev-share to creators
- **API credits**: $0.002 per generated wiki paragraph for high-volume users (>20k paragraphs/month)

## Key Resources
- **LLM capability stack**: Fine-tuned proprietary model for spoiler-free Thai + multilingual hallucination suppression (labelled dataset: 89k spoiler/redaction pairs)
- **GitHub Actions + Rust CLI**: 800ms avg. spoiler-lint per page; compiled into minimal WebAssembly for in-browser preview
- **Branded template gallery**: 40 prebuilt wiki themes optimized for game manuals, anime episode guides, software docs (CC-BY-SA; user remixes encouraged)
- **Community testimonials library**: Curated quotes from indie devs/fans showcasing spoiler-safe wikis (usage rights granted)
- **KPI dashboard repo**: Public repo exposing anonymized savings metrics (pages auto-corrected, spoilers caught) to verify ROI claims

## Key Activities
- **Daily model retraining**: Augment with spoiler-mitigated user edits (opt-in telemetry captured via GitHub Events)
- **Rule-engine development**: Weekly iteration on common spoiler lexicons (add 150 new terms/month from fan-forum leak feeds)
- **Compatibility maintenance**: Quarterly updates for Docusaurus v2/v3, MkDocs material 9.x, MediaWiki 1.41 parity
- **PR & benchmarking**: Publish quarterly “spoiler-leak index” ranking top wiki-tools by containment score; aim top-3 within 6 months
- **Support triage**: Triage GitHub issues + Slack within SLA; escalate popular feature requests to sprint backlog every 2 weeks

## Key Partners
- **itch.io bundle hosts**: Cross-promote wiki-scribe Pro to indie devs purchasing asset packs; reciprocate by listing bundle products in template gallery
- **Fountain pen/Indie game press**: Sponsored podcasts/interviews targeting tabletop RPGs and visual novels (<5% CAC)
- **Thai localization NGOs**: Validate Thai lexicon accuracy; co-brand “Thai-language spoiler-free wiki grants” for small Thai indie developers
- **GitHub Stars & Docs maintainers**: Recruit open-source advocates to curate template themes; share visibility in maintainer newsletters
- **SponsorAPI**: Automated integrations with Fly.io, Netlify, Vercel for zero-config deploy buttons inside repo README

## Cost Structure
- **Compute**: $8k/mo GPU cluster (A100 40GB) at run-rate of 2M wiki pages/yr; down to $3k/mo on spot-instances with 20% queue wait
- **Hosting**: $2.5k/mo Netlify + Cloudflare R2 for template thumbs & public wikis; burst to $3.8k during viral launches
- **Annotations & lexicons**: $1.2k/month crowdsourced lexicon updates from Thai/Vietnamese/Korean fan forums (Mechanical Turk–style micro-tasks via Upwork)
- **Team**: 1 PM ($120k/yr), 1 ML engineer ($140k/yr), 1 growth hacker ($95k/yr) = $35k/mo fully-loaded
- **Legal & insurance**: $8k quarterly for DMCA spoiler-rule IP indemnification (fan leaks = unpredictable)