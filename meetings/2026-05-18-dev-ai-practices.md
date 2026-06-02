---
title: Dev AI Practices — Engineering Future Environment
created: 2026-05-18
updated: 2026-05-18
domain: engineering-workflows
type: meeting
tags: [engineering, ai-practices, sdlc, code-quality, harness, linear-to-pr, tech-debt, critical-thinking]
---

## Attendees

- [[tom-harvey|Tom Harvey]]
- [[ishmael|Ishmael Jebril]]
- [[jordi|Jordi Pallares]]
- [[david|David Zamora]]
- [[fergus|Fergus Doyle]]
- [[chris|Chris Fothergill]]

## Key themes

### Current AI usage patterns — a wide spectrum

Everyone is using AI but in fundamentally different ways:

- **Ishmael**: Architecture thinking with Claude before delegating implementation. Rubber duck for new domains. CLAUDE.md at the top of J agent, updated every time he does something. Recording team calls and feeding transcripts as context — getting right context is now more important than writing code.
- **Chris**: Offloading parallel/smaller tasks (API creation, test writing) while staying focused on the primary task. Front end builds while backend API changes happen in parallel. Already getting output "as I'd raise it, really."
- **David**: Multiple Cursor windows; asks one agent to generate full context to copy into another window. Focused on context-setting more than code-writing.
- **Rob**: Tendency to delegate everything to AI without first thinking critically about what he's trying to solve or why. Needs targeted support — a different approach from Chris/Ishmael.

The codebase matters: product config repo (well-structured, clear responsibility) gets 19/20 success rate. Backend services with complex architecture are harder — but pointing the agent at a well-built service (insurance service) as a gold standard dramatically improves output.

### The cognitive load shift — two fundamentally different modes

Fergus articulated the key distinction:

- **Mode 1 (most people now)**: Ask a question, frame it, wait for response, repeat. Still mentally in the loop the whole time.
- **Mode 2 (target)**: Sit outside the loop. Let the agent do the spade work. Guide and repoint when necessary — like reviewing a mid-level hire's output.

Most of the team are in Mode 1. Mode 2 is the target state. The failure mode is thinking these are the same thing, or expecting Mode 2 to emerge naturally without deliberate practice.

### Failure mode: harness engineering vs. shipping

Jordi raised it: "there's a failure mode where everyone wants to start building the harness and lose sight of impact." The CICD analogy — teams with no one who naturally invests in pipeline infrastructure will either neglect it entirely or overcorrect when attention is directed at it.

Tom's counter: the current problem is the opposite end. People aren't yet comfortable enough. "I'd rather be in a month where we're saying, everyone stop working on the harness and get back to work, than where we are now." Agreed direction: invest deliberately, treat it like the SDLC investment — it fits the priority stack the same as any other technology initiative.

### Code consistency as the primary goal

Jordi's framing of what AI can fix: unbreakable principles/rules that should govern all code but currently exist only as tribal knowledge passed through onboarding and day-to-day conversation. Front end: UI kit usage, component creation patterns. Back end: CQRS hexagonal architecture compliance. These can be encoded in markdown context files and used for:
- Agent-driven first-pass PR reviews
- Standardising repeatable processes (new query, new service, new endorsement)
- Tech debt cleanup — making old services look like gold standard is pure execution, no judgment required

Chris: "there might also be non-agent solutions to some of these things" — deterministic npm packages for front-end structural problems. The deterministic layer and the AI layer are complementary, not alternatives.

### Linear → PR as the direction of travel

Fergus described the full arc: strategy page → initiatives → projects → tasks → linear tickets → PRs, potentially with an agent at every stage. **Immediate first step (Chris's proposal)**: ticket breakdown — linear ticket → discrete subtasks. Immediate value, usable by everyone regardless of AI fluency. **Longer term**: linear → draft PR, reviewed by engineer as if reviewing a mid-level hire's output.

Tom: the end goal isn't speed. "For the first time in my career, no one's complaining about the team's shipping speed." The goal is better products and better code — and, at the highest level, "so we're all still employable in 2030."

### Tech debt as the first real candidate

The commoditised work is the right entry point: making older services look like a modern gold standard. Chris already tested this with model files in the insurance service — the agent "did a really good job." Customers and broker services are the next candidates. This work never gets done because it doesn't block anything; it's exactly the kind of task that should be handed to agents while engineers focus on critical thinking.

**Endorsements** called out as an ideal isolated workflow pilot — well-documented, straightforward end-to-end, good precedent in version history.

### Critical thinking as the preserved human skill

Jordi: Rob tends to delegate everything to AI without first thinking about what he wants to solve. This is the wrong pattern. The right pattern: critical/architectural thinking first (with Claude as a thinking partner), then delegate implementation. Fergus: "let's make sure we are indexing for those skills — differential thinking, judgment — so we can guide agents to really good results."

Jordi's framing: right talent + right context + right tools = potential 100x engineers. The job security concern is real and was named explicitly by Tom. The answer: "recognise what is being commoditised around you, so you can lean into the novel skills you always had."

### Time as the stated blocker

Chris: "biggest blocker is time." The prescription agreed: 30–60 minutes/day of deliberate AI practice. Build context gradually. Test refactoring on non-critical services. Hold the 20% buffer — it's not different from how CICD investment was treated.

## Actions

- [ ] **Tom**: Identify endorsements as first isolated end-to-end workflow pilot; scope what "done" looks like
- [ ] **Jordi / Chris**: Define engineering target state — what does good look like? Written down, shareable with the whole team, so they can chip away incrementally
- [ ] **Chris**: Start customers/broker service refactor via agent (after MTAs); 10 min/day approach
- [ ] **Tom**: Design different support approach for Rob vs Chris/Ishmael — Rob needs critical thinking scaffolding, not just access to context files
- [ ] **All**: Hold 30–60 min/day deliberate AI practice as a standing commitment

## Notes

"Adam" early in transcript = garbled "without him" (speaker asking how much they can cover before Ishmael joins).
"Jebodi" in transcript = Jordi (name-resolution.yaml updated).
"Thanks, John" at close = Tom departing, garbled.
Alex Smith (David's team) mentioned as a more deliberate AI user — no people file yet.

Full transcript: [[2026-05-18-dev-ai-practices-transcript]]
