# /decision — Create Decision Record

Create a new decision record in MADR format.

## When to use

When a decision needs to be documented — technical choices, process changes, tool selections, governance calls.

## Steps

1. Scan `decisions/` to find the highest-numbered existing decision file. The next number is that + 1, zero-padded to three digits (e.g., `001`, `002`, `013`). If no decisions exist, start at `001`.
2. Gather the following (ask the user if not provided, or infer from context):
   - **Title**: short descriptive title
   - **Domain**: one of engineering-workflows, operational-tooling, product-ai, ai-enablement
   - **Context and problem statement**: what prompted this decision
   - **Decision drivers**: key factors influencing the choice
   - **Considered options**: at least two, each with Good/Bad because points
   - **Decision outcome**: chosen option with justification
   - **Consequences**: what follows from this decision
3. Create the file at `decisions/NNN-kebab-title.md` using the template from `reference/templates/decision.md`.
4. Fill in all frontmatter fields:
   - title: "NNN — Decision title"
   - created: today's date
   - updated: today's date
   - domain: as provided
   - type: decision
   - status: accepted (or proposed if the user indicates it's not final)
   - tags: as appropriate
5. Populate all body sections from gathered information.
6. Report the created file path.
