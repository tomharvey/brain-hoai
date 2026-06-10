# Skill: /onboarding

Interactive first-time setup for a new BDM. Reads `onboarding-questions.md`
and steps through each question one at a time, waiting for a response before
moving to the next.

---

## When to run

First conversation in this project. Typically triggered by Tom or the BDM
themselves typing `/onboarding`.

Do NOT run this if Layer 2 pages (My Accounts, My Shortcuts) already contain
substantive content — the BDM has already been set up. Instead, ask if they'd
like to update specific sections.

---

## How to run this skill

Read `onboarding-questions.md` before starting. That file contains:
- The exact text of each question
- What to do with each answer (HubSpot lookups, what to write where)
- The synthesis step at the end

Follow the steps below. Do not rush through questions — each one deserves a
real answer and you may need to do a lookup or ask a follow-up before moving on.

---

## Steps

### Step 0 — Opening

Say exactly this (adapt name from project context):

> Hi [BDM_NAME] — I'm going to ask you 7 questions to get your brain set up.
> This takes about 10 minutes.
>
> I'll ask one question at a time. Take your time with each one —
> the better your answers, the more useful I'll be from day one.
>
> Ready? Let's start.

Wait for any response (even just "yes" or "go") before continuing.

---

### Step 1 — Ask Q1

Read Q1 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- Do the HubSpot lookups described in the Q1 instructions
- Confirm each broker found: "Found [company] in HubSpot — last touched [date] by [owner]. That's the one?"
- If a broker isn't in HubSpot: note it, don't block — say "I don't see [name] in HubSpot yet, we can add them. Carry on."
- Once all three are confirmed, say: "Got it — [Name 1], [Name 2], [Name 3] are your top three."

Then say: "Next question." and move to Step 2.

---

### Step 2 — Ask Q2

Read Q2 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- For each broker: extract the status and the next action
- If a next action has a date mentioned, note it
- Reflect back: "So for [Broker 1]: status is [X], next action is [Y]. Is that right?"
- Confirm all three before moving on

Then say: "Good. Three more to go." and move to Step 3.

---

### Step 3 — Ask Q3

Read Q3 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- Reflect the answer back in one sentence: "So before a call you most want to know [X]."
- If the answer is vague ("everything" / "it depends"), gently probe once:
  "If you had to pick the single most useful thing — what would it be?"
- Accept the second answer even if still general

Then say: "That'll shape how I brief you before every call." and move to Step 4.

---

### Step 4 — Ask Q4

Read Q4 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- If they name a specific broker: pull Granola and HubSpot in background — note any
  available transcripts for later Coach reference
- Reflect: "So the pattern was [summary]. I'll keep that in mind when similar deals come up."
- If they say they don't have a good example: accept it — "That's fine, we'll build this
  up as we go."

Move to Step 5.

---

### Step 5 — Ask Q5

Read Q5 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- Map to a brain role internally (see Q5 instructions in onboarding-questions.md) — don't
  say the role name out loud, just note it for personalisation
- Reflect: "Got it — [challenge area] is where I'll focus first."

Move to Step 6.

---

### Step 6 — Ask Q6

Read Q6 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- Confirm: "Bullet points" or "more context" — make sure it's unambiguous
- Say: "I'll keep your morning brief [short and scannable / a bit more detailed]."

Move to Step 7.

---

### Step 7 — Ask Q7

Read Q7 from `onboarding-questions.md`. Ask it verbatim.

After the BDM answers:
- Confirm their Slack handle against BDM Directory. If it doesn't match, flag: "I have
  you as @[handle] in the team directory — is that still right?"
- Confirm email similarly
- If they want both: confirm which cadence for each (Slack = daily, Gmail = weekly)

---

### Step 8 — Synthesis and write

Read the synthesis section of `onboarding-questions.md`.

Present the full summary:

> Here's what I've captured:
>
> **Top 3 brokers:**
> 1. [Broker] — [status] — next action: [action]
> 2. [Broker] — [status] — next action: [action]
> 3. [Broker] — [status] — next action: [action]
>
> **Before a call, you most want to know:** [Q3 answer]
>
> **What's worked before:** [Q4 summary]
>
> **Current focus:** [Q5 summary]
>
> **Brief style:** [bullets / narrative]
>
> **Delivery:** [Slack @handle / email / both]
>
> Shall I write this to your Notion pages now?

Wait for confirmation before writing anything.

On confirmation:
1. Write My Accounts entries (top 3 with status notes)
2. Write My Commitments entries (next actions from Q2)
3. Write My Shortcuts (pre-call priority + what's worked)
4. Write My Development Focus (challenge area)

Show each write before executing. Write one page at a time.

---

### Step 9 — Close

Once all writes are confirmed:

> Setup complete. Here's what happens next:
>
> - Tomorrow at 8am you'll get your first morning brief [on Slack / by email]
> - Before any broker meeting, I'll send you a pre-call brief 30 minutes beforehand
> - After meetings, type `/granola` and I'll help you log it and notify the team
> - Every Monday morning you'll get a weekly team pulse
>
> Any questions before we start?

Wait for response. If none, close gracefully.
