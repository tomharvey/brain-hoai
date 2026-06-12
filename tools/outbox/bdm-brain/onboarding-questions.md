# Onboarding Questions — BDM Brain Setup

This file contains the 7 onboarding questions and instructions for how to use each answer.
The onboarding skill (`skills/onboarding.md`) reads this file and steps through questions
one at a time.

Edit this file to change the questions or what gets done with answers.
Do not edit the onboarding skill itself unless you want to change the interaction pattern.

---

## Questions

### Q1 — Priority accounts

**Ask:**
> Which brokers are currently your top 3 priorities?
> For each, just give me the name — I'll look them up in HubSpot and Granola
> to get context before we go further.

**What to do with the answer:**
- For each name given: query HubSpot (company search) and Granola (recent meetings)
- Confirm you found the right record: "I found Brown & Brown — last HubSpot activity was
  [date], owner [name]. Is that the one?"
- Write broker names to My Accounts (if not already there)
- **Capture HubSpot company ID**: after the BDM confirms the correct record, extract the
  company ID from the HubSpot response. Store it in My Accounts as `HubSpot ID: [id]`
  alongside the broker name. Future lookups use this ID directly — eliminates name
  matching fragility (Brown & Brown vs B&B vs "Brown and Brown Ltd" all break name search).
- These become the pre-loaded Layer 3 context for morning briefs

---

### Q2 — Current status and next action per priority account

**Ask:**
> For each of those three — what's the current status, and what's the single
> most important next action you need to take?

**What to do with the answer:**
- Create a My Commitments entry for each next action: owner = [BDM_NAME], no due date
  unless they mention one
- Note current status against each account in My Accounts (one-line note)
- Flag if any next action is overdue relative to the HubSpot last activity date

---

### Q3 — Pre-call information need

**Ask:**
> When you're about to call a broker, what's the one piece of information
> you most want to know before you pick up the phone?

**What to do with the answer:**
- Write the answer to My Shortcuts as: "Pre-call priority: [answer]"
- Use this to lead the pre-meeting brief for this BDM
- Common answers: "what did we last promise them", "what's their current quote status",
  "who else from our team have they spoken to"

---

### Q4 — What's worked before

**Ask:**
> Is there a broker — current or past — where you figured out exactly the right
> approach and it clicked? What was the pattern?

**What to do with the answer:**
- Write to My Shortcuts as: "What's worked: [summary of pattern]"
- This becomes a coaching reference — when a new deal resembles this one,
  the Coach role can surface it
- If they name a specific broker: check if it's in HubSpot or Granola for reference

---

### Q5 — Current challenge

**Ask:**
> What's your biggest challenge right now — finding new brokers, moving deals
> forward, closing, or something else entirely?

**What to do with the answer:**
- Write to My Development Focus: "[Challenge area] — [their words]"
- This informs which brain roles to lead with for this BDM:
  - Finding new brokers → Forecaster (similar prospect detection) + Librarian
  - Moving deals forward → Secretary (commitments) + Strategy partner (pre-call brief)
  - Closing → Coach + Sparring partner
- Note in project instructions personalisation section

---

### Q6 — Morning brief preference

**Ask:**
> For your daily morning brief, do you prefer short bullet points,
> or a bit more context on each item?

**What to do with the answer:**
- Update project instructions personalisation: Morning brief style = [BULLETS / NARRATIVE]
- Bullets: 5–7 items, one line each, lead with anything urgent
- Narrative: short paragraph per theme, more context on why something matters

---

### Q7 — Delivery preference

**Ask:**
> Last one: Slack or email for daily messages?
> (Slack for quick nudges, Gmail draft for a weekly summary — or both, or just one.)

**What to do with the answer:**
- Update project instructions: Delivery preference = [SLACK / EMAIL / BOTH]
- If Slack: confirm their handle (cross-check against BDM Directory)
- If email: confirm their address (cross-check against BDM Directory)
- If both: Slack for daily (morning brief, EOD nudge), Gmail draft for weekly pulse

---

## After all questions — synthesis

Once all 7 answers are collected:

1. **Show a summary** — present all answers back in a clean format for the BDM to confirm
2. **Write Layer 2** — with approval, write to:
   - My Accounts: top 3 brokers with status notes
   - My Commitments: next actions from Q2
   - My Shortcuts: pre-call priority (Q3) + what's worked (Q4)
   - My Development Focus: challenge area (Q5)
3. **Update project instructions** — note which personalisation fields to update manually
   (morning brief style, delivery preference, Slack handle, email)
4. **Confirm completion** — "Setup complete. Your morning brief starts tomorrow.
   You can run `/granola` after any broker meeting to log it and notify the team."
