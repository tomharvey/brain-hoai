---
title: Aleksandra / Thomas — AI catchup (May 22)
created: 2026-05-22
updated: 2026-05-22
domain: engineering-workflows
type: meeting
tags: [engineering-workflows, ai-enablement, engineering-culture, admiral]
---

# Aleksandra / Thomas — AI catchup (May 22)

**Attendees:** Tom Harvey, [[aleks-yanova|Aleksandra Yaneva]]

Full transcript: [[2026-05-22-aleksandra-ai-catchup-transcript]]

---

## Key themes

### Admiral visit debrief
- Aleksandra discovered 30 minutes before the call that she had to demo to Admiral (CTO, Director of Technology, Principal Engineer)
- Attendees reduced from many to three at the last minute; no schedule, very informal engineering discussion
- Crash detection demo went well despite zero prep
- Group: very male-heavy; Mima was sick and missed it; Aleksandra noted this
- Topics: AI, claims integration with Admiral's existing API
- Deal status: nearly complete, not yet; no data access until formally complete

### Cursor leaderboard
- Aleksandra not in top 10; Rob Grice high (asking "read the whole codebase" queries)
- Tom: leaderboards send wrong message — tacky, creates wrong incentives, favours engineering unfairly
- Concern: people game the metric rather than using AI well

### "Should I understand or just trust it?" — the core tension
- Aleksandra's dilemma: when Claude suggests something in an unfamiliar domain (e.g. DLT Firehose), should she spend time understanding it or trust and move fast?
- Concern about appearing slow if she pauses to learn
- Tom's answer: **always go for understanding** — but you don't need to read the docs. Instead:
  - Train your agent to cite its sources (add another layer against hallucination)
  - Ask Claude to explain its decisions; it learns what you want explained
  - Use the AWS documentation MCP server for service-specific questions
  - Rob is using Claude to read the existing codebase and learn from priors — a valid approach
- Broader message: **faster is not the definition of better** — robust understanding of a service IS the win

### AI job anxiety — engineering
- Steve: worried he'll become an "AI babysitter" — the fun of engineering is the problem-solving struggle
- Tom: had the same feeling for two weeks; refined his joy by realising AI doesn't remove the problem-solving — it raises the abstraction level
- Reddit threads: hundreds of engineers grieving the pre-AI era
- Engineers being "protective" of what they've built with AI — not sharing techniques, competitive mindset
- Bigger concern: "two classes of employee" emerging between AI-heavy and AI-light users
- Ed has said publicly: he doesn't want a two-tier company
- Company's position: ambitious growth targets, hiring (not laying off) — very different from FAANG layoffs
- Tom's view on FAANG layoffs: AI is a convenient excuse; the real reasons are metaverse spending, slower growth, product/market shifts

### Admiral Business engineers (context)
- Tom Blomfield "company operating system" talk came up: Aleksandra doesn't recommend it beyond validating existing ideas
- Tom confirmed Aleksandra's general AI usage via multi-agent document processing sessions — running overnight

---

## Actions

- [ ] Tom: Schedule squad-by-squad conversations on job philosophy and AI identity (→ AI-073)
- [ ] Tom: Share "faster is not better" framing more broadly with engineering team
- [ ] Tom: Share "cite your sources" practice as team-wide guidance

---

## People without vault files
- Steve — engineer, worried about "AI babysitter" role; presented Databricks anomaly detection at lunch & learn
