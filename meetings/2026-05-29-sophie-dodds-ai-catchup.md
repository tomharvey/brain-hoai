---
title: Sophie / Thomas — AI catchup (May 29)
created: 2026-05-29
updated: 2026-05-29
domain: ai-enablement
type: meeting
tags: [ai-enablement, bdm, granola, skills, automation]
---

# Sophie / Thomas — AI catchup (May 29)

**Attendees:** Tom Harvey, [[sophie-dodds|Sophie Dodds]]

Full transcript: [[2026-05-29-sophie-dodds-ai-catchup-transcript]]

---

## Key themes

### Current automation setup
- Meeting notes → Slack: Claude gets Granola summaries (not full transcripts) → inconsistent quality; Sophie manually copies to team channel
- Daily brief: runs at 8am, updates a Notion page — meeting notes, live deals pipeline, open/completed actions, email summaries. Working well
- Accelerator broker tracker: company-wide sheet + Sophie's personal detailed sheet; feeds into Friday weekly reports for Anton/Adam
- DRP and Partners flagged as priority relationships for business updates

### Root-cause: summaries not transcripts
- Claude is only receiving Granola summaries, not full transcripts — the source of the inconsistency problem
- Fix: build a skill that always fetches the full transcript and summarises it in Sophie's format

### Recommended next steps
- **Custom meeting summary skill**: pulls full transcript, filters personal/social content, highlights escalations to Adam/Alex/Matt, maintains consistent format with attendees/topics/actions
- **Accelerator broker automation**: auto-update broker needs/objectives from meeting content; feed into weekly report
- **Risk update emails**: bi-weekly/monthly summaries to regional broker heads (e.g. DRP head)
- **Super Whisper**: Tom recommended for talking directly to Claude — Sophie is voice-first (prefers voice notes over typing)
- Workshop rescheduled one week later (Sophie on Centre Parcs holiday)

### AI maturity observation
- Sophie is well ahead of most of the workforce — she's already asking "is Claude reading the summary or the transcript?" and instinctively knows to just ask Claude. Tom framed this as a top-1% capability
- Blocker is not knowledge, it's time and confidence

---

## Actions

- [ ] Sophie: Build custom Granola summary skill (pull full transcript, filter personal, tag escalations)
- [ ] Sophie: Try Super Whisper for voice-first Claude interaction
- [ ] Tom: Book BDM team workshop (week after next — Sophie confirmed available after Centre Parcs)

---

## Notes

- Origin of AI-069 (custom BDM Granola summary skill)
