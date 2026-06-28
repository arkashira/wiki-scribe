# breakeven.md  

**Product:** *wiki‑scribe* – AI‑augmented wiki‑building platform that auto‑generates spoiler‑free articles, runs continuous quality‑control edits, and ships a lightweight editor for solo devs & fan‑wiki operators.  

---

## 1. Cost per Active User (CPU + Storage + Bandwidth)

| Cost Component | Assumptions (per MAU) | Monthly Cost (USD) |
|----------------|----------------------|--------------------|
| **Compute (LLM inference)** | • 2 k tokens generated per user per month (average 0.5 k per article, 4 articles)  <br>• 0.0004 USD per 1 k tokens (using an 8‑B parameter hosted model)  <br>• 10 % overhead for moderation QC passes | **0.80** |
| **Background QA & Editing** | • 1 k tokens for automated edit‑suggestion per article (4 articles)  <br>• Same pricing as above | **0.40** |
| **Storage** | • Avg. 5 MB per article (text + metadata) → 20 MB/user ≈ 0.02 GB <br>• Cloud object storage $0.023/GB‑mo | **0.0005** |
| **Bandwidth (download)** | • Avg. 2 MB per article view, 30 views/mo → 60 MB = 0.06 GB <br>• Egress $0.09/GB | **0.0054** |
| **API & SaaS overhead (auth, analytics)** | Fixed per‑user slice of shared services | **0.10** |
| **Total Variable Cost / MAU** |  | **≈ $1.31** |

> **Note:** Costs are calculated using public cloud pricing (AWS S3, CloudFront, EC2 spot for inference) and assume a modest 5 % safety margin for spikes.

---

## 2. Pricing Tiers (USD / month)

| Tier | Price | Core Features | Expected Adoption % |
|------|-------|---------------|---------------------|
| **Starter** | **$5** | • 5 articles/month <br>• Basic spoiler‑filter <br>• Community‑only support <br>• 5 GB storage quota | 45 % |
| **Growth** | **$15** | • Unlimited articles <br>• Advanced spoiler‑filter (custom rules) <br>• Auto‑QC & edit suggestions <br>• API access (REST) <br>• 20 GB storage <br>• Email support | 40 % |
| **Enterprise** | **$45** | • All Growth features + <br>• Dedicated LLM instance (lower latency) <br>• Bulk import/export <br>• SLA 99.9 % <br>• 100 GB storage <br>• Priority phone support <br>• Custom branding | 15 % |

*Revenue per user (weighted avg.)*  
\(0.45×5 + 0.40×15 + 0.15×45 = 2.25 + 6.0 + 6.75 = **$15.00**\)

---

## 3. Customer‑Acquisition Cost (CAC)

| Channel | Cost per Lead | Conversion to Paid | CAC (USD) |
|---------|---------------|--------------------|-----------|
| Content‑marketing (blog, SEO) | $0.30 | 2 % | **$15** |
| Paid‑social (Twitter, Reddit) | $1.20 | 5 % | **$24** |
| Partnerships (wiki‑hosting platforms) | $0.80 | 8 % | **$10** |
| **Overall CAC range** | — | — | **$10 – $25** |

We will target an **average CAC of $15** by balancing organic and partnership channels.

---

## 4. Lifetime Value (LTV)

Assumptions:  

* **Monthly churn** = 5 % (typical for niche SaaS).  
* **Average revenue per user (ARPU)** = $15 (from tier mix).  

\[
\text{LTV} = \frac{\text{ARPU}}{\text{Churn}} = \frac{15}{0.05} = **\$300**
\]

*With a $15 CAC, LTV:CAC ≈ 20 : 1 → healthy unit economics.*

---

## 5. Break‑Even Users Count

### Fixed Monthly Overheads (est.)

| Item | Monthly Cost (USD) |
|------|--------------------|
| Engineering (2 devs) | $12,000 |
| DevSecOps / Cloud Ops | $2,500 |
| Product & Design | $4,000 |
| Marketing & Sales (budget) | $5,000 |
| General & Admin (legal, accounting) | $1,500 |
| **Total Fixed** | **$25,000** |

### Contribution Margin per MAU  

\[
\text{Revenue per MAU} - \text{Variable Cost per MAU} = 15 - 1.31 = **\$13.69**
\]

### Break‑Even MAU  

\[
\frac{\text{Fixed Monthly Cost}}{\text{Contribution Margin}} = \frac{25,000}{13.69} \approx **1,828\ \text{active users}**
\]

---

## 6. Path to $10 K MRR  

| Tier | Price | Users Needed for $10 K MRR |
|------|-------|----------------------------|
| Starter | $5 | 2,000 users |
| Growth | $15 | 667 users |
| Enterprise | $45 | 223 users |

**Strategic Mix (realistic)** – Assuming the weighted tier distribution (45 % Starter, 40 % Growth, 15 % Enterprise):

* Required total MAU = 1,828 (break‑even) → yields **≈ $27 K MRR** (since ARPU = $15).  
* To hit **$10 K MRR** we only need **≈ 667 Growth‑equivalent users**.  

A practical launch plan:

| Phase | Target MAU | Expected Tier Mix | MRR |
|-------|------------|-------------------|-----|
| **Beta (Month 1‑2)** | 200 | 70 % Starter, 30 % Growth | $1,600 |
| **Launch (Month 3‑5)** | 600 | 45 % Starter, 40 % Growth, 15 % Enterprise | $9,000 |
| **Scale (Month 6‑9)** | 2,000 | 45 %/40 %/15 % | $30,000 |

Thus, **by month 5** we cross the $10 K MRR threshold with ~600‑700 paying users (mostly Growth tier).  

---

### Quick‑look Summary

| Metric | Value |
|--------|-------|
| Variable cost / MAU | **$1.31** |
| ARPU (tier‑weighted) | **$15** |
| Contribution margin / MAU | **$13.69** |
| Fixed monthly overhead | **$25 K** |
| Break‑even MAU | **≈ 1.8 K** |
| CAC (avg) | **$15** |
| LTV | **$300** |
| Users for $10 K MRR | **≈ 667 Growth‑equivalent** |

These numbers give a clear, data‑driven runway to profitability and guide the go‑to‑market pacing for *wiki‑scribe*.  