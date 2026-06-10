# Skill: /ghost-check

On-demand ghost account detection. Surfaces brokers that have gone quiet
before the BDM notices.

Triggered by `/ghost-check` or "which accounts have gone quiet?"

---

## Steps

### Step 1 — Load account list

Read My Accounts. Get the list of brokers [BDM_NAME] owns.

Also read the Shared Activity Log — look for any entries in the last 30 days
for each broker.

---

### Step 2 — Check each broker

For each broker in My Accounts:

1. **HubSpot**: when was the last logged activity (email, call, meeting)?
   Get: `last_activity_date` from company/deal record
2. **Granola**: when was the most recent transcript with this broker?
3. **Activity Log**: when was this broker last logged by any BDM?

Compute: days since last contact = minimum of (HubSpot, Granola, Activity Log)

---

### Step 3 — Classify

| Days since contact | Status |
|-------------------|--------|
| 0–7 | Active — skip |
| 8–14 | Cooling — note |
| 15–29 | Ghost candidate — flag |
| 30+ | Ghost — escalate |

---

### Step 4 — Report

Present results:

> Here's your account health check:
>
> **Ghosts (30+ days, no contact):**
> - [Broker] — last contact: [date] ([N] days ago)
>   Last: [what the last interaction was, from HubSpot/Granola]
>
> **Ghost candidates (15–29 days):**
> - [Broker] — last contact: [date] ([N] days ago)
>
> **Cooling (8–14 days):**
> - [Broker] — last contact: [date]
>
> **Active (≤7 days):** [count] accounts — all good.

If no ghosts: "All your accounts have had contact in the last 14 days. Nothing urgent."

---

### Step 5 — Recovery actions (optional)

For each ghost:

> [Broker] has been quiet for [N] days. Want me to:
> - Pull their HubSpot record and last Granola transcript to see what was last discussed?
> - Draft a re-engagement plan?

Handle each one the BDM wants to act on.

---

### Step 6 — Team ghosts (optional)

If [BDM_NAME] asks "what about the whole team?" or "are there unowned accounts?":

Read the Shared Activity Log for all BDMs. Find any broker that appears in
the Activity Log but is not in any BDM's My Accounts page.

> These brokers appear in the Activity Log but don't seem to have a clear owner:
> [list]
> Want me to flag this to Adam?
