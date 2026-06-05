---
title: BDM Brain — Meeting Prep (Adam + Ollie)
created: 2026-06-04
updated: 2026-06-04
domain: ai-enablement
type: inbox
tags: [bdm, shared-brain, meeting-prep, adam-smith, ollie-crowe]
---

# BDM Brain — Meeting Prep

Related: [[bdm-ai-multiplayer]] · [[AI-072]] · [[adam-smith]] · [[ollie-crowe]]

---

## Meeting order: Adam solo → Ollie solo → Adam + Ollie together

Three meetings, not two. The third is short — it only works because the first two did the heavy lifting.

**Why not joint from the start:** you need Adam's unfiltered read on the outcomes *before* Ollie's product framing enters the room. In a joint meeting, one of two things happens: Adam defers to Ollie's more structured thinking, or the conversation gets pulled toward delivery before the problem has been properly named. Either way, you lose the thing the Adam conversation is for.

There's also a role tension in a joint setting: Ollie is simultaneously meant to listen to the user need and challenge the design — those modes conflict. He'll either hold back or crowd Adam out.

**Adam solo (45 min):** outcomes only. Let him name the problem. Get the hypotheses from him, not at him.

**Ollie solo (60 min):** full design review. Bring what Adam said. Challenge the architecture and phase plan together.

**Joint alignment (30–45 min):** synthesis, not discovery. *"Here's what we heard, here's the shape — do you both agree before we take it to the team?"* This is the pre-workshop lock. Walk out with confirmed hypotheses, shared framing, and both names on the brief.

---

## What you need from each person

### Adam — validate the outcomes
Adam is your authority on what actually matters in the sales process. He doesn't need to understand the architecture. He needs to understand the outcome so completely that he could describe it to his team without you in the room.

Specifically:
- **Confirm or reject the conversion hypotheses** — not nod along. Push him to say "that one — that's the one that would change what I do."
- **Add hypotheses you've missed** — he knows the sales floor; there will be things not in the current list
- **Name the vocabulary** — what does "ghost" mean to his team? What does "accelerator" mean in deal terms?
- **Own the pilot** — who on his team is the obvious first user?

### Ollie — shape the delivery
Ollie is PM and conversion bets author. He can handle the full picture.

Specifically:
- **Validate the phase plan** against his bandwidth and the team's capacity
- **Challenge the tool stack** — are BDMs actually in Notion daily, or is that aspirational?
- **Confirm his PM role** through to launch — make this explicit
- **Sequence the workshop** — what goes in front of the team, in what order

---

## Questions that must be answered before the Adam call

These are blockers — you can't finalise the hypotheses without them:

1. **Which moment in the sales process does he feel most contextually blind?** Don't lead — let him name it. This is the "what decision gets made differently" question from the Anton gate.
2. **Of the candidate hypotheses, which one would he actually use?** Not "which is most interesting" — "which would change what you do tomorrow morning."
3. **Does he feel the ghost account problem?** Does he already have a name for it? If so, use his language.
4. **How does he expect to interact with it?** Does he see himself prompting it, or does he expect it to push things to him? His answer determines whether Phase 1 is sufficient or whether the proactive layer is actually what he needs first.
5. **Manager layer or peer layer?** Does he want visibility into what his BDMs are doing, or does this brain belong to the team — not a management reporting tool? This affects the ontology significantly.
6. **Who is the obvious early adopter on his team?** Who do you run the Phase 1 pilot with?

---

## Questions that must be answered before the Ollie call

1. **What does Ollie already know about the initiative?** Start from what's shared — don't re-explain what he's across.
2. **Does he have PM capacity for this?** Alongside his other conversion bets, this needs to be explicit before the workshop is booked.
3. **How clean is HubSpot data really?** Ollie is closer to this than the initiative admits. The identity/join key risk (#1 in open decisions) may already be understood — or already worse than expected.
4. **What's his read on the BDM team's actual daily workflow?** Do they live in Notion? Or is that a tool we want them to use more than they currently do?
5. **Which conversion bet does he think this most directly moves?** He authored the bets — he should be able to point at the specific one this brain is serving.

---

## What to present vs what to leave open

### Adam meeting

| Bring as strawman | Leave open — co-develop |
|-------------------|------------------------|
| The eight roles in plain language (what the brain does *for him*, no architecture) | The hypotheses — he should finish the sentences |
| The "no new tool" frame (see below) | The vocabulary — stages, statuses, what ghost and accelerator mean to his team |
| One concrete Monday morning scenario: what does starting the day with the brain look like? | Which BDMs are in the pilot and in what order |
| The Anton gate framing: this has to move conversion, not just improve context | The write workflow — what does contributing feel like day-to-day? |

### Ollie meeting

| Bring as strawman | Leave open — co-develop |
|-------------------|------------------------|
| Full three-plane architecture (he can handle it) | Phase sequencing — he should pressure-test the order |
| The roles taxonomy | Tool stack for delivery — validate what BDMs actually use |
| Adam's confirmed hypotheses (from the Adam call) | Workshop agenda — this is co-owned, not handed to him |
| The open decisions register | Identity/join key approach — he'll have a view |

---

## Opening frames

### For Adam — start with the problem, not the brain

> *"You've got four BDMs. Each of them has context the others don't. Every Monday morning, someone walks into a call not knowing a colleague spoke to that account last week. Every quarter, a deal goes cold and nobody noticed. That's not a people problem — it's a context problem.*
>
> *Before I show you what we're thinking of building, I want to know which of those scenarios actually keeps you up at night — because that's where we start."*

Then listen. The hypotheses should come from what he says next, not from the slide you prepared.

### For Ollie — start with what Adam confirmed

> *"I spoke to Adam. He said [X]. Here's how we build toward that. I want to show you the architecture and the phase plan, and I want you to challenge both — particularly on what the BDM team actually uses day-to-day versus what we think they use."*

---

## The "no new tool" frame — use in both meetings

This is the strongest clarity unlock for non-technical audiences. The brain doesn't introduce a new tool. It makes the tools they already use smarter:

- **Claude** — already using it. The brain gives Claude memory: it knows their accounts, their deals, their colleagues' conversations.
- **Notion** — already in it. The brain writes structured knowledge there. They query it through Claude.
- **HubSpot** — already the deal tracker. The brain reads it, doesn't replace it.
- **Email and Calendar** — already where work flows. The brain can surface signals there (a daily brief, a flag on a deal going cold).

**The brain is an upgrade to their existing stack, not a new tool to learn.**

This frame also answers the "is this just another system to maintain?" objection before it's raised.

---

## What not to do

- Don't open with the architecture in either meeting
- Don't use the word "ontology" with Adam
- Don't present all eight roles as a feature list — pick two or three that directly answer the problem he named, and let the others surface naturally
- Don't let Ollie turn the Adam meeting into a joint session — the two conversations need to be separate before they converge at the workshop
- Don't ask Adam to validate the technical decisions (search federation, CloudWatch, MCP hosting) — that's Ollie's territory

---

## Next actions

- [ ] Book Adam solo (45 min — outcomes conversation, not a demo)
- [ ] Book Ollie solo (60 min — full design review)
- [ ] Book Adam + Ollie joint (30–45 min — pre-workshop alignment lock)
- [ ] Prepare the Monday morning scenario (one concrete story, not a feature list) before the Adam call
- [ ] After Adam: update [[bdm-ai-multiplayer]] hypotheses with his input before the Ollie call
- [ ] After Ollie: update open decisions and phase plan before the joint call
