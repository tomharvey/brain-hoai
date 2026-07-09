---
title: AI Finance workshop
created: 2026-07-08
updated: 2026-07-08
domain: ai-enablement
type: meeting
tags: [finance, workshop, moss, netsuite, mcp, claude-code, ai-activation]
---

# AI Finance workshop — 2026-07-08

**Attendees:** Tom Harvey, [[ivan-boix|Ivan Boix]], Pavel Soulimov, [[anneliese-vanwijk|Anneliese Van Wijk]], [[kirsty|Kirsty Alexandre]], [[queency-gonsalves|Queency Gonsalves]], [[matt-dipre|Matt Dipre]], Sarah Phillips, [[jade-mounir|Jade Mounir]], [[geran|Geran Butcher]]

**Transcript:** [[2026-07-08-ai-finance-workshop-transcript]]

> Name note: Granola's attendee record gives **"Pavel Soulimov"** (pavel@flockcover.com); the vault ([[../reference/org-chart|org-chart]], activation map) has "Pavel Souliman". The surname is never spoken in the transcript, so the transcript itself supports neither spelling — but the calendar/directory metadata favours **Soulimov**. Sarah Phillips is new to the vault (no people file yet): finance team member of a few weeks, never used NetSuite before, would sit on the Flock Premium side.

## Themes

### 1. NetSuite MCP — working but flaky, and governance is emerging bottom-up
- Finance created a **separate view-only NetSuite role for Claude** themselves — deliberately avoiding write access ("it could just delete everything very quickly by accident"). Governance instinct arrived without being imposed.
- Open question: does the read-only role cover Flock Premium, Flock Limited, or both? Nobody in the room knew — Geran to confirm. Segregation needed: Sarah, Jade, and probably Queency should be Flock Premium only.
- Recurring friction: users get bounced by role permissions (must close everything and reopen NetSuite in the MCP role) and the MCP **disconnects automatically** and needs manual reconnection. Local installation floated as a fix (was faster and account-bound when previously used).
- Matt's Looker MCP also drops out; his Claude-made Looker dashboards land in a generic account he can't open directly — he now mostly bypasses Looker and pulls from the data lake.

### 2. From playful to productionised — automation wins
- **Ivan**: daily report fully automated. Claude runs it from a watched folder; if the data isn't there, Ivan gets a Slack message. No manual Excel upload. "It gives me more time to think about things I can keep automating."
- **Kirsty**: POG report skill (64 metrics) with a **self-audit trick** — recompute a previously verified quarter and diff against stored values ("checking that Claude hadn't gone rogue"; it "flagged one or two places that it had gone a bit off piste"). Plus an executive summary highlighting red metrics and progressive deterioration — Paul now runs the POG meeting from that summary instead of walking 64 metrics. Safety-net pattern: writes to a new Google Sheet rather than overwriting checked work.
- **Matt Dipre**: instalment calculator demo (see below) — the centrepiece.
- **Queency**: month-end reconciliation via Claude since May, now "so accurate" — lists every discrepancy down to minute differences. Self-invented extension: Claude sends managers **direct approval links per expense** — "I do get approvals done much quicker than before."
- **Kevin** (via Anneliese/Jade): vendor-level cost analysis from Moss that NetSuite can't produce — will drive budget-vs-actuals conversations with heads of department. "Something we've been crying out for for a very long time."
- Moss expense attachments: Claude can fetch the PDF behind an expense and answer questions from it (e.g. seat count on the Anthropic invoice) — Christian's use case, shared with the room.

### 3. Matt's instalment calculator — shadow tool becomes OKR blueprint
- Built with Claude Code + co:work (exported the whole co:work conversation as one big MD prompt into Claude Code, then iterated between the two). Pulls straight from the data lake, Python calculation engine, local web UI, private GitHub repo — commit to GitHub and "it goes live".
- Chris reviewed all the code (one column fix); numbers have been correct since. Every run self-audits: unmapped policies (NetSuite/GoCardless), the haulage-rider anomaly, oddities. Filters per broker for statement checking; surfaces new business in the last 24h; produces broker-ready schedules with portal links.
- "Made something that was never possible possible" — quarterly MTAs with monthly instalments now supported, letting finance tell brokers **yes**. Added the Kirsty-inspired feature *during* an OKR session after Tom mentioned it in passing: "It's like my own personal engineer."
- Bus-factor discussed: all on Matt's Mac; plan to load it onto a second machine (Queency's) for holiday cover. Jade pushed the productionisation question; per Jade (via Jordi), engineering will use it **as the basis for the OKR build**, not just inspiration — Geran has already played with it and built a further version. Matt should take credit.
- Next step: NetSuite API key so a "push" button posts invoice/credit CSVs straight into NetSuite.
- Matt's usage was high enough last month that he was upgraded to the premium tier. Tool built with Fable 5.

### 4. Moss MCP rollout — nearly, not quite done
- Python-version install failures: Dave (David Pilley) **resolved** by Tom; **Anneliese still hit the same issue** — Tom in office today to help, also fixable remotely. Christian has no access, is on holiday, and will likely hit the same error on return — Kirsty wants the written fix so she can sit with him. Jade hasn't attempted the install yet; will try solo and reach out if stuck.
- Tom's pitch: the Moss MCP lives on GitHub like Matt's tool — record a sticky process (e.g. the month-end description captured in Granola → "go build that") and it becomes a feature. Wants the MCP into Kirsty's Claude Code so features get added as she hits them.

### 5. Sharing live dashboards
- Anneliese (dashboard question, some audio ambiguity with Jade on the call): builds Claude dashboards regularly — cash burn / runway, Looker-MCP pulls, broker commission as % of GWP — but can't share a live, auto-updating view; it's stuck on her Mac.
- Fix (proven by distribution team): point co:work at a **shared Google Drive folder** instead of the desktop — same HTML, still interactive, auto-syncs to everyone's Mac. Tom to help set up.

## Per-person signals (activation evidence)

| Person | Evidence |
|---|---|
| [[ivan-boix\|Ivan]] | Daily report fully automated with folder-watch + Slack alerting; thinking about the next automation. |
| [[kirsty\|Kirsty]] | Skill-building with self-verification and exec summaries; changed how Paul runs the POG meeting; coordinating team Moss rollout. |
| [[matt-dipre\|Matt Dipre]] | Full application built and in daily production use for ~1 month; engineering adopting it as OKR-build basis. |
| [[queency-gonsalves\|Queency]] | Habitual reconciliation use since May, now trusted; self-invented approval-links workflow; co-debugging NetSuite discrepancies with Matt. |
| [[anneliese-vanwijk\|Anneliese]] | Regular Claude dashboard builder (cash burn, Looker MCP, broker commission %GWP); raised the NetSuite access-segregation governance point; Moss install still blocked on Python version. |
| [[jade-mounir\|Jade]] | Strategic engagement (OKR/productionisation push for Matt's tool); hasn't attempted Moss install yet. |
| Pavel Soulimov | First direct evidence (attribution tentative — room mic): set up the NetSuite MCP himself, hit role bugs / auto-disconnects, reconnects it himself ("not a huge task"). Tooling installed and touched; no output or win yet. |
| Sarah Phillips | New joiner (a few weeks), never used NetSuite; learning; positive on Claude-as-interface ("if I could just ask it a question it'd be so much better"). |
| [[geran\|Geran]] | Got Matt data-lake access; built a further version of Matt's calculator; owns NetSuite role-scope question. |
| [[kevin-berg\|Kevin]] (not present) | Vendor cost analysis via Moss for dept-head budget conversations. |

## Actions

- [ ] **Geran** — confirm NetSuite MCP read-only role scope (Flock Premium vs Flock Limited vs both), then set up segregation so Sarah / Jade / Queency sit on the Premium side only.
- [ ] **Tom** — share the Google Drive shared-folder dashboard fix (distribution team's pattern) with Anneliese and help the finance team set it up.
- [ ] **Tom** — resolve Anneliese's Moss Python-version install error (in office today; remote also fine). Relates to [[../issues/AI-149-debug-anneliese-python-install|AI-149]].
- [ ] **Tom → Kirsty** — write up the Python-version fix so Kirsty can sit with Christian when he's back from holiday. Relates to [[../issues/AI-148-moss-mcp-reinstall-rollout|AI-148]].
- [ ] **Jade** — attempt Moss MCP install solo; reach out to Tom/Kirsty if stuck. Relates to [[../issues/AI-148-moss-mcp-reinstall-rollout|AI-148]].
- [ ] **Tom** — get the Moss MCP into Kirsty's Claude Code and add features iteratively as she hits them.
- [ ] **Matt Dipre** — get NetSuite API key (admin approval) for push-button invoice posting; load the calculator onto a second machine (likely Queency) for holiday cover.
