---
title: "Thin Harness, Fat Skills — Garry Tan + vault analysis"
created: 2026-04-14
updated: 2026-04-14
domain: ai-enablement
type: reference
tags: [architecture, skills, harness, garry-tan, agent-design]
---

## Source

Garry Tan (YC), April 2026. Originally shared as a post — saved to inbox 2026-04-14.

## Key concepts

### 1. Skill files

Reusable markdown that teaches the model *how* to do something. Works like a method call — same procedure, different arguments, wildly different outputs. "Markdown is a more perfect encapsulation of capability than rigid source code, because it describes process, judgment, and context in the language the model already thinks in."

### 2. The harness

The program wrapping the LLM. Does four things: runs the model in a loop, reads/writes files, manages context, enforces safety. **Keep it thin.** Anti-pattern: fat harness with 40+ tool definitions eating context. Purpose-built tooling should be fast and narrow.

### 3. Resolvers

Routing table for context. When task type X appears, load document Y first. The developer doesn't need to know the eval suite exists — the resolver loads `docs/EVALS.md` automatically. Claude Code's built-in resolver: skill descriptions matched to user intent.

### 4. Latent vs deterministic

Every step is one or the other. Latent = judgment, synthesis, pattern recognition. Deterministic = same input, same output (SQL, compiled code, arithmetic). Most agent failures come from putting the wrong work on the wrong side.

### 5. Diarization

The model reads everything about a subject and writes a structured profile — judgment distilled from many documents. Not a database lookup. Not RAG. The model has to read, hold contradictions, notice changes, and synthesise.

## Architecture

Three layers:
- **Top**: Fat skills (markdown procedures encoding judgment + domain knowledge — 90% of value)
- **Middle**: Thin CLI harness (~200 lines, JSON in / text out, read-only by default)
- **Bottom**: Deterministic application (QueryDB, ReadDoc, Search, Timeline)

Principle: push intelligence up into skills, push execution down into deterministic tooling, keep the harness thin. Model improvements automatically improve every skill.

## The learning loop

1. Retrieve → read → diarize → count → synthesise
2. Survey → investigate → diarize → rewrite the skill

Skills rewrite themselves based on feedback. "12% OK ratings → 4% OK ratings. The skill file learned what OK actually meant."

Key instruction: "If I have to ask you for something twice, you failed." Every task that will recur must become a skill, optionally on a cron.

---

## How our vault maps to this

### Where we align

| Concept | Our implementation | Assessment |
|---------|-------------------|------------|
| **Fat skills** | 11 skills in `.claude/skills/`, each a directory with `SKILL.md`. `/granola` knows scoping + structuring. `/calendar` knows freebusy + buffer rules. | Strong. Skills carry the capability, CLAUDE.md points. |
| **Thin harness** | CLAUDE.md is ~200 lines of conventions and pointers. No bloated tool definitions. | Strong. Harness is thin by design. |
| **Skills as method calls** | `/granola` is the same 6-step procedure producing different output per invocation. `/issue` routes by argument (create/update/list/close). | Strong. Same pattern Tan describes. |
| **Latent/deterministic split** | Skills with `disable-model-invocation: true` are fully deterministic (`/manifest`, `/reindex`, `/calendar`, `/morning`). Others use Claude for scoping decisions only. Search uses SQLite + FTS5 + vectors — deterministic retrieval, Claude only in synthesis. | Good discipline. Clear separation. |
| **Diarization** | People files are structured profiles synthesised from multiple meetings/Slack/observations. Initiative files distil many conversations. 1:1 logs are running diarizations. | Strong. This is exactly what Tan describes. |
| **Learning loop** | Memory files persist corrections across sessions. Skills refined over time (calendar now has buffer rules, day-verification). | Partial. Manual, not automated. |

### Where we're weak

**1. Resolvers are underdeveloped.** No active context routing. When "schedule a meeting" comes in, nothing auto-loads `feedback_calendar_scheduling.md` and `feedback_meeting_buffers.md`. The memory system is a proto-resolver (passive scan of MEMORY.md index) but not a real resolver (active loading by task type). A proper resolver would say: "task involves calendar → load these 3 docs before proceeding."

**2. No crons.** `/reindex` should run after every commit. `/manifest` should too. `/morning` could generate at 8am. Infrastructure exists (Claude Code scheduled triggers) but isn't wired up. Tan's principle: "if it should run automatically, put it on a cron."

**3. Search layer underused.** Solid deterministic foundation (SQLite, FTS5, vectors, wikilink graph, action extraction) but rarely invoked in practice. Most context resolution is manual file reads. Structured queries (`open-actions`, `actions-for`, `orphans`, `unlinked-meetings`) should be embedded in skill workflows, not standalone.

**4. No skill self-improvement.** When the calendar skill fails (Saturday scheduling), a memory file gets updated but the skill itself doesn't learn. The fix should be written into the skill procedure: "Step 0: run `date -d` to verify day of week." No `/improve` pattern exists.

**5. Skills don't compose.** `/granola` could call `/issue` to auto-create issues from meeting actions. `/morning` could call `/search` to find orphaned notes. Composition would multiply capability.

### Suggested improvements

1. **Add resolver logic** — map task types to context documents (either in CLAUDE.md or a dedicated resolver file)
2. **Wire up crons** — `/reindex` and `/manifest` on post-commit hook, `/morning` on daily schedule
3. **Bake corrections into skills** — calendar day-check should be in the skill procedure, not just memory
4. **Compose skills** — `/granola` offers to create issues from actions, `/morning` calls `/search`
5. **Build `/improve`** — reviews recent memory/feedback entries and proposes skill file updates

---

## Editorial notes on the post

**What's strong:**
- "Skill as method call" is the best framing of why same prompts → wildly different results for different people
- Latent/deterministic split is genuinely useful as a design heuristic
- Chase Center example is concrete enough to be actionable
- "Markdown as programming language" is exactly right for knowledge work systems

**What's overblown:**
- "1000x vs 2005 Googlers" — inflammatory framing that invites dismissal. The real insight (architecture > model intelligence) doesn't need hyperbole
- "You failed if I ask twice" — good theatre but undersells value of doing things manually first to understand edge cases. Shreya's NOC skill works *because* she did it manually first
- Claude Code leak presented as revelation, but the principles are well-documented in Anthropic's own guides

**What's missing:**
- When skills are the wrong abstraction — some work is genuinely one-off, and codifying everything creates maintenance burden (dead skills, stale procedures)
- Skill testing — how do you know `/match-lunch` still works after the skill rewrites itself? Same governance gap [[jordi]] flagged: "who tested this?"
- Multi-user orgs — the post assumes a single user. In an org with 28 people at different AI maturity levels (our situation), the challenge isn't fat skills — it's getting people to invoke skills at all

## Links

- [[ai-capability-uplift]]
- [[skills-distribution]]
- [[claude-standardisation]]
