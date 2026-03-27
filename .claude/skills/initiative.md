# /initiative — Create or Update Initiative

Create a new initiative or update an existing one.

## When to use

When capturing a new AI initiative (especially self-started ones that need governance) or updating progress on an existing one.

## Steps — New initiative

1. Gather the following (ask the user if not provided, or infer from context):
   - **Title**: short descriptive name
   - **Owner**: who owns this initiative
   - **Domain**: one of engineering-workflows, operational-tooling, product-ai, ai-enablement
   - **Status**: active, paused, completed, or abandoned
   - **Origin**: self-started, directed, or proposed
   - **Summary**: one paragraph
   - **Goal**: what success looks like
   - **Current state**: where things stand now
   - **Dependencies**: what this needs from others
   - **Risks**: what could go wrong
   - **Next actions**: immediate next steps
2. Create the file at `initiatives/kebab-title.md` using the template from `reference/templates/initiative.md`.
3. Fill in all frontmatter and body sections.
4. If origin is `self-started`, add guidance per CLAUDE.md: honour the owner, note what changes under governance, identify what the owner needs.

## Steps — Update existing initiative

1. Ask which initiative to update, or infer from context. Read the existing file.
2. Update the relevant sections with new information.
3. Bump the `updated` date in frontmatter.
4. Add a dated log entry at the top of the Log section describing what changed.
5. Report what was updated.
