# GI Oncology Daily Digest — Project Instructions

## Owner
Dr. Allan Pereira — Medical Oncologist, GI Malignancies, Moffitt Cancer Center
- GitHub: allanatal
- X/Twitter: @DrAllanPereira
- Website: https://allanatal.github.io/my-website/

## Purpose
Automated daily digest system that curates GI oncology research, generates a polished website digest page, an X/Twitter thread draft, and maintains a digest archive. Goal: increase Allan's social media exposure as a GI oncology specialist.

---

## The "run" Command

When Allan says **"run"**, execute this exact workflow:

1. **Check mount path** — Run `ls /sessions/*/mnt/` to find the correct mount. It varies between sessions (`Claude_projects` or `CURSO_DE_PESQUISA--Claude_projects`).
2. **Web searches** (7-8 searches, date-filtered to last 7 days using `after:YYYY-MM-DD`)
3. **Score and rank** papers using the scoring system below
4. **Write JSON data file** to `digests/data/YYYY-MM-DD.json`
5. **Run engine**: `python3 digest_engine.py digests/data/YYYY-MM-DD.json`
6. **Verify**: Check IIFE count (`}());` = 2 in digest + index), thread-card count, link count
7. **Git commit** (never push — Allan pushes manually from Terminal)
8. **Report run stats**: searches count, total tool calls, session usage %

**Target efficiency:** 7-8 searches, ~11 total tool calls per run.

---

## Search Sources (in priority order)

1. **Journals**: NEJM, Lancet, JCO, JAMA Oncology, Annals of Oncology, Nature Medicine
2. **Conferences**: ASCO, ASCO GI, ESMO, AACR (when in season)
3. **Press releases**: GlobeNewswire, PR Newswire, BusinessWire (Phase 2/3 results)
4. **FDA**: New approvals, accelerated approvals, breakthrough therapy, fast track, priority review
5. **News**: OncoDaily, OncLive, Targeted Oncology, Cancer Network
6. **X/Twitter colleagues**: Engagement signals from GI oncology KOLs

**Date filtering**: Always add `after:YYYY-MM-DD` (7 days back) to search queries to avoid stale results consuming tokens.

**GI cancer scope**: Colorectal, pancreatic, gastric/GEJ, hepatocellular, cholangiocarcinoma, GIST, esophageal, small bowel, anal. Include general oncology if directly relevant (e.g., pan-tumor IO approvals).

---

## Scoring System (max 20)

### Base Score — Journal/Source Prestige
| Source | Score |
|--------|-------|
| NEJM | 10 |
| Lancet, Nature Medicine | 9 |
| JCO | 8 |
| Annals of Oncology, JAMA Oncology | 7 |
| FDA regulatory action | 8 |
| ASCO/ESMO plenary | 8 |
| AACR oral presentation | 7 |
| AACR poster / conference presentation | 6 |
| Press release (Phase 3) | 6 |
| NCCN guideline update | 7 |
| Other | 5 |

### Bonus — Study Type
| Type | Bonus |
|------|-------|
| Phase III RCT | +3 |
| Phase II | +2 |
| Meta-analysis | +2 |
| Retrospective / real-world | +1 |

### Bonus — Clinical Impact
| Impact | Bonus |
|--------|-------|
| New standard of care | +3 |
| Survival benefit (OS or PFS) | +2 |
| Biomarker-guided / precision | +1 |

### Bonus — Colleague Engagement
| Signal | Bonus |
|--------|-------|
| Each GI oncology KOL engagement on X | +1 |

### NEJM Safety-Net Rule
**Any NEJM paper from the last 7 days related to GI malignancies OR general oncology topics MUST appear in the digest** — either as a Top 5 paper or in the Additional Papers section. Never miss an NEJM paper.

---

## JSON Data File Schema

File location: `digests/data/YYYY-MM-DD.json`

```json
{
  "date": "2026-04-23",
  "date_display": "April 23, 2026",
  "subtitle": "Post-AACR 2026 Edition",
  "feed_desc": "Short descriptions of top 5 papers with sources in parentheses, comma-separated",
  "papers": [
    {
      "title": "Full descriptive title",
      "url": "https://source-url.com",
      "source": "Journal / Conference / Organization",
      "authors": "Author names or organization",
      "published": "Date string",
      "score": 12,
      "score_rationale": "Breakdown: base (X) + bonus (+Y) + bonus (+Z)",
      "summary": "3-5 sentence summary with key data points (ORR, PFS, OS, HR, p-values)",
      "post_angle": "Suggested social media angle with hashtags"
    }
  ],
  "additional": [
    {
      "title": "Paper title",
      "url": "https://source-url.com",
      "source_line": "Source — One-line description of key finding"
    }
  ],
  "x_thread": [
    {
      "label": "Post 1 — Hook",
      "text": "Thread text (300-800 chars, bullet-point style)",
      "url": ""
    },
    {
      "label": "Post 2 — #1 Short Name",
      "text": "Post text with bullet points",
      "url": "https://source-url.com"
    }
  ]
}
```

**Top 5 papers**: Ranked by score descending. Always exactly 5.
**Additional papers**: 5-6 papers. Avoid duplicating papers already covered in prior digests.
**feed_desc**: Always provide explicitly. Auto-generation from the engine is a fallback only.

---

## X Thread Style (7 Posts)

Allan has **X Premium** — posts can be 300-800 characters (text only; URLs don't count on X).

### Structure
- **Post 1 — Hook**: Emoji + date + subtitle + 2-3 teaser lines highlighting the most exciting findings + "A thread 🧵👇" + hashtags
- **Posts 2-6 — Top 5 papers**: Each post has:
  - Emoji header (🔥 #1, 📊 #2, 🎯 #3, 🌍 #4, 🧪 #5, etc.)
  - Trial/study name + source
  - Bullet points (•) with key data
  - 1-2 sentence commentary/opinion
  - Hashtags
  - URL (appended as clickable link in HTML, doesn't count toward char limit)
- **Post 7 — Additional Papers**: Bullet list of 4 additional papers + link to full digest

### Style Rules
- Keep bullet-point format (Allan likes it)
- Be punchy and opinionated — this is social media, not a journal
- Include trial acronyms, drug names, key endpoints
- Use hashtags: #GIOnc, #CRC, #PDAC, #HCC, #GastricCancer, #AACR2026, #PrecisionMedicine, etc.
- Every post except Post 1 and Post 7 must have a source URL

---

## Digest Engine

**Location**: `my-website/digest_engine.py`

**Usage**: `python3 digest_engine.py digests/data/YYYY-MM-DD.json`

**Outputs** (all generated automatically):
1. `digests/digest-YYYY-MM-DD.html` — Main digest page (Bootstrap 4.6.2, Font Awesome 5, Inter font, site.css, anti-flash IIFE, paper-card divs, navbar, full footer)
2. `digests/x-thread-YYYY-MM-DD.html` — Polished X thread draft (gradient header, thread-card layout, post-label badges, char-count display, clickable links, dark mode)
3. `digests/digest-feed.json` — Updated feed (single source of truth for website listing)
4. `digests/index_digest.html` — Rebuilt archive page from feed JSON

**DO NOT modify the engine** unless the website design changes. The engine contains all stable HTML templates, CSS, and generation logic. Only the JSON data file changes per run.

### Anti-Flash IIFE Pattern
The digest and index HTML files use an Immediately Invoked Function Expression for dark mode. It MUST end with `}());` (not `});`). Always verify: `grep -c '}());'` should return 2 for each file.

---

## Git Workflow

- **Repo**: https://github.com/allanatal/my-website.git
- **Branch**: main
- **User**: allanatal
- **PAT**: Embedded in remote URL (do not modify git config)
- **Push fails from sandbox** (HTTP 403 proxy) — Allan pushes manually from Terminal

### Files to commit per run
```
git add digests/digest-YYYY-MM-DD.html \
       digests/x-thread-YYYY-MM-DD.html \
       digests/data/YYYY-MM-DD.json \
       digests/digest-feed.json \
       digests/index_digest.html
```

### Commit message format
```
Add GI Oncology Digest [Date] ([Theme/Edition])

Top stories: [1-line per paper with source in parentheses]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

### Git lock files
If `fatal: cannot lock ref 'HEAD'` occurs, run:
```bash
rm -f .git/HEAD.lock .git/objects/maintenance.lock
```

---

## Website Design Reference

- **Framework**: Bootstrap 4.6.2 + Font Awesome 5 + Inter font
- **CSS**: `../site.css?v=3` (relative from digests/)
- **Dark mode**: `data-theme="dark"` attribute on `<html>`, toggled via button
- **Colors**: Navy (#003366), accent blue (#00528A), green score badge (#007A33)
- **Navbar**: Links to CV, Testimonials, Contact, GI Digest
- **Footer**: Social media links (Facebook, Twitter, LinkedIn, Instagram, YouTube), Moffitt Magnolia Campus, book appointment links

---

## Common Pitfalls to Avoid

1. **Never regenerate the engine script** — it's stable and committed. Only write JSON data files.
2. **Never use f-strings in generated HTML** — they corrupt IIFE syntax. The engine uses string concatenation (already handled).
3. **Mount path changes every session** — always check `ls /sessions/*/mnt/` first.
4. **Don't ask Allan for folder permission** — he has already authorized Cowork access to his Dropbox/Claude_projects folder.
5. **Don't push to git** — it fails from the sandbox. Tell Allan to push.
6. **Date-filter searches** — use `after:YYYY-MM-DD` to avoid old results wasting tokens.
7. **Avoid duplicate papers** — check what was covered in the most recent digest(s) via `digest-feed.json`.
8. **WebFetch is often blocked** — many oncology sites are blocked by the egress proxy. Rely on WebSearch summaries instead of trying to fetch full pages.

---

## Run Stats Tracking

Report at the end of every run:
```
Run stats — [Date]:
- Searches: X
- Total tool calls: Y
- Session usage: Z% (ask Allan if not known)
```

Baseline targets: 7-8 searches, ~11 tool calls, ~15-20% session usage per run.
