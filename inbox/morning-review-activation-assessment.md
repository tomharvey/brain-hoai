---
title: Morning Review — AI Activation Assessment
created: 2026-06-18
type: inbox
---

# Priority Review List — AI Activation Assessment

Overnight run completed. 3 verification agents ran after the assessment to check evidence, name confusion, and completeness. Here's what needs your attention, ranked by priority.

---

## Issues found (fix before presenting)

### 1. Mollie Brownlow — missing from assessment entirely
Emily's people file says she reports to "Mollie Brownlow (Head of Operations)." Mollie does not appear in:
- The org chart Mermaid diagram
- Any transcript
- The assessment (not scored, not unassessed, not out-of-scope)

**Action needed:** Check with Emily or Rakhee whether Mollie is currently employed. If yes, add her. If she departed, update Emily's people file.

### 2. Anna Spriggs "cut out unnecessary steps" quote — sourced from meeting note, not transcript
The April 2 transcript is a stub. The quote comes from the meeting note `2026-04-02-anna-ai-discovery.md`. This is weaker than a verbatim transcript quote but is still your own contemporaneous note. The Stage 3 upgrade is primarily supported by the May 13 ops sync evidence (deal creator error identification, dual-logic fix proposal), which IS confirmed in transcript.

**Action needed:** Decide if you're comfortable with meeting-note-sourced evidence for Anna. If yes, no change needed. If not, her confidence should drop to Low rather than Medium.

### 3. Geran "multiple MCPs" — slightly overstated
The evidence shows Snowflake/Glue infrastructure and Claude Desktop, but explicit enumeration of "multiple MCP servers" isn't present. Geran has MCP-adjacent infrastructure rather than classic MCP connections. The Stage 3 upgrade is primarily supported by the "breadth of context" practice and Streamlit production apps — both confirmed in transcript.

**Action needed:** Minor. Could soften the language in the assessment from "multiple MCPs integrated" to "Snowflake/Glue data infrastructure integrated with Claude." Not a stage-changing issue.

---

## Verified clean (no action needed)

These were checked and confirmed correct:

- **Name confusion:** All 5 high-risk name pairs checked (Darren x2, Sam/Sami, David x2, Matt x4, Harvey/Javier). Zero misattributions found.
- **Shreya 3→4:** All 3 tools (NOC, deal creator, workload allocation) confirmed in transcripts, correctly attributed.
- **Jacob 3→4:** "Capable juniors" quote and parallel processes confirmed in Jun 3 transcript. The "cron agents" evidence comes from the pre-existing April codifying context session (already in his people file) — not hallucinated, just from a different source.
- **David Z 3→4:** "Agents change plans from planning to building mode" confirmed verbatim in May 12 transcript.
- **Kirsty 3→4:** Pod metrics automation and team-wide deployment confirmed. "Spinning our wheels for four months" quote verified.
- **Sam 2→3:** "Senior engineer that thinks faster" confirmed as Tom's immediate recap of Sam's words. Verified this is Sam Adeniyi, not Sami.
- **Eraaz 2→3:** All evidence (3x/day co:work, multi-connector, advising colleagues) confirmed in Jun 2 workshop transcript.
- **Fred 1→2:** Daily skill use and personalised version creation confirmed in Jun 3 transcript.
- **Phoebe 2→1 downgrade:** Fully justified — transcript shows only planning and aspiration, zero demonstrated practice.

---

## Completeness gaps (low urgency)

### 4. Sami missing from org chart
Sami is correctly in the assessment (Stage 1, Low confidence) but is not in the org chart Mermaid diagram — he joined after it was last updated. Surname still unknown.

**Action needed:** Add Sami to org chart under Jordi. Check surname.

### 5. Antton Pena has more evidence than originally captured
The assessment initially said "zero data." Verification found 5+ third-party transcript mentions: he engages with AI outputs at SLT (Adam's trading pack, Christian's budget HTML), asks AI governance questions. Updated the assessment to reflect this. Still needs a direct 1:1 but he's not a blank slate.

**Action needed:** Already fixed in the assessment file. Review the updated wording.

### 6. Christian Nielsen likely Stage 3 already
Fergus (Jun 11 weekly) describes Christian setting himself "the challenge of producing [budget content] without touching a spreadsheet" — deliberate practice, not casual use. Combined with "highest token user in finance," he may be further along than anyone has formally assessed. His 1:1 should be a priority.

**Action needed:** Schedule the 1:1. You may be pleasantly surprised.

---

## Assessment quality summary

| Check | Result |
|---|---|
| Org chart completeness | 1 gap (Mollie Brownlow) |
| Name confusion | 0 errors across 5 high-risk pairs |
| Quote verification (10 key upgrades) | 8 fully confirmed, 2 minor caveats (Anna meeting note, Geran MCP wording) |
| Person file frontmatter ↔ body consistency | Fixed for all 9 upgraded files + Phoebe downgrade |
| Unassessed register honesty | Updated Antton with evidence; rest confirmed |
| People files created | 3 new (Liam Thomson, Harry Dowrick, Michael Matthews) |
| People files updated | 20 existing files (stages, confidence, body text) |

---

## Files changed (not yet committed)

**New files:**
- `reference/ai-activation-assessment-2026-06.md` — the main deliverable
- `people/liam-thomson.md`
- `people/harry-dowrick.md`
- `people/michael-matthews.md`

**Updated files:**
- `reference/ai-activation-map.md` — full matrix refresh
- 20 person files with stage/confidence changes
- `WORKING.md` — session state
