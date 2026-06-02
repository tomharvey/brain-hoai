---
name: moss-month-end
description: Run MOSS month-end consistency checks via API
---

# MOSS Month-End Consistency Checker

Connects to MOSS via API and checks for the three most time-consuming parts of month-end close.

## What it checks

1. **Coding inconsistencies** — merchants coded to different expense accounts or cost centres across months (e.g. "Stripe" in platform costs one month, subscriptions the next).
2. **Missing recurring vendors** — vendors appearing in 10+ of the last 12 months but absent this month. Usually means a contractor invoice hasn't come in yet and needs accruing.
3. **Unapproved recurring items** — current-month expenses from recurring vendors not yet approved.

## Tools available in Claude (once set up)

| Tool | What to say |
|---|---|
| `run_month_end_check` | "Run the MOSS month-end check" or "Check MOSS for May 2026" |
| `get_vendor_history` | "Show me the last 6 months of Stripe in MOSS" |

---

## Setup — Claude Desktop (one-time, ~10 minutes)

### Step 1: Install Python dependencies

Open **Terminal** and run:

```bash
pip3 install fastmcp requests
```

If `pip3` isn't found, first run: `xcode-select --install`

### Step 2: Note the full path to server.py

In Terminal:

```bash
echo ~/.claude/skills/moss-month-end/server.py
```

Copy the output — you'll need it in Step 4. (Or wherever you've saved this skill.)

### Step 3: Generate your MOSS API keys

1. Log into MOSS with admin access
2. Go to **Settings → Company Settings → API Keys**
3. Click **Generate API Key** — set scope to **read only**
4. Copy both the **Key ID** (`kid_...`) and **Secret Key** (`sk_...`) immediately — MOSS only shows them once
5. Save them in your password manager

### Step 4: Add to Claude Desktop config

Open this file in TextEdit (or any text editor):

```
~/Library/Application Support/Claude/claude_desktop_config.json
```

If the file doesn't exist yet, create it. Add the `moss` block inside `mcpServers`:

```json
{
  "mcpServers": {
    "moss": {
      "command": "python3",
      "args": ["/Users/YOUR_NAME/path/to/server.py"],
      "env": {
        "MOSS_API_PUBLIC_KEY": "kid_your_key_id_here",
        "MOSS_API_SECRET_KEY": "sk_your_secret_key_here"
      }
    }
  }
}
```

Replace `/Users/YOUR_NAME/path/to/server.py` with the path from Step 2, and fill in your actual keys.

If you already have other MCP servers configured, add `moss` alongside them inside `mcpServers` — don't replace the whole file.

### Step 5: Restart Claude Desktop

Quit Claude Desktop completely and reopen it. You should see a hammer icon (🔨) in the chat input area — click it to confirm the MOSS tools are listed.

---

## Usage

Once set up, just ask Claude in plain English:

> "Run the MOSS month-end check"
> "Check MOSS for last month"
> "What has Stripe been coded to in MOSS over the last 6 months?"

Claude calls the tools and presents the results inline — no Terminal needed.

---

## CLI alternative (Terminal)

If you prefer to run from the command line instead of Claude Desktop:

```bash
# Create moss-config.json next to server.py with your keys:
# {"public_key": "kid_...", "secret_key": "sk_..."}

python3 server.py  # starts the MCP server (for Desktop)

# Or use the bash script for a quick terminal report:
bash moss_month_end.sh
bash moss_month_end.sh 2026-05
```

---

## Distributing to team members

Each person needs their own API keys from MOSS (**Settings → Company Settings → API Keys**). Keys are user-scoped — they cannot share yours.

Share this zip. Each person follows the setup steps above with their own keys.

**Do not commit `moss-config.json` or share API keys over Slack/email.** Use a password manager.

---

## Adjusting thresholds

Two constants near the top of `server.py` control detection sensitivity:

| Constant | Default | Meaning |
|---|---|---|
| `RECURRENCE_THRESHOLD` | 10 | Months out of last 12 to count as recurring |
| `CONSISTENCY_MIN_MONTHS` | 3 | Minimum appearances before consistency is checked |

## Troubleshooting

**"MOSS credentials not found"** — check the env vars in `claude_desktop_config.json` match exactly, and restart Claude Desktop after saving.

**"MOSS authentication failed"** — the keys are wrong or expired. Regenerate in MOSS and update the config.

**Unexpected "Unknown" values** — the field names in your MOSS account may differ from the defaults. Raise with Tom to update the extractor lists in `server.py`.
