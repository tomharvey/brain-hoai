# MOSS Month-End Checker — Setup Guide

This tool connects Claude Desktop to your MOSS account so you can run month-end checks by asking Claude in plain English — no spreadsheets, no manual review.

**What it checks:**
- Invoices coded inconsistently (same merchant, different categories across months)
- Recurring vendors missing from this month (likely need accruing)
- Unapproved recurring items that haven't been signed off yet

---

## What you'll need

- A Mac
- Claude Desktop installed
- Admin access to your MOSS account (to generate an API key)
- 15 minutes

---

## Step 1 — Install Python

Open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter) and run:

```
python3 --version
```

If you see something like `Python 3.11.4`, Python is already installed — skip to Step 2.

If you see a pop-up saying **"The xcode-select command requires the command line developer tools"**, click **Install** and wait for it to finish (~5 minutes). Then move to Step 2.

If nothing happens, download and install Python from **[python.org/downloads](https://www.python.org/downloads/)** — click the big yellow "Download Python" button, open the downloaded file, and follow the installer. Then move to Step 2.

---

## Step 2 — Copy the files and create a virtual environment

In Terminal, run these commands one at a time:

```
mkdir -p ~/mcp-servers/moss-mcp-server
cp ~/Downloads/moss-month-end/* ~/mcp-servers/moss-mcp-server/
cd ~/mcp-servers/moss-mcp-server
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

What each line does:
1. Creates the folder `~/mcp-servers/moss-mcp-server/`
2. Copies the server files into it
3. Changes into that folder
4. Creates an isolated Python environment (`.venv`) so the dependencies don't affect anything else on your Mac
5. Installs `fastmcp` and `requests` into that environment

This only needs to be done once.

---

## Step 3 — Generate your MOSS API keys

1. Log into MOSS and go to **Settings → Company Settings → API Keys**
2. Click **Generate API Key**
3. Set the scope to **read only**
4. Give it a name like `Claude`
5. Copy both values immediately — **MOSS only shows them once:**
   - **Key ID** — starts with `kid_...`
   - **Secret Key** — starts with `sk_...`
6. Paste them somewhere safe (your password manager, or a private note) before closing the window

---

## Step 4 — Find your username

In Terminal, run:

```
echo $HOME
```

The output will look like `/Users/anneliese`. Note down the part after `/Users/` — that's your username. You'll need it in the next step.

---

## Step 5 — Configure Claude Desktop

Claude Desktop has a configuration file that tells it which tools to load. You need to add the MOSS server to it.

### Open the config file

In Terminal, run:

```
open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

If you get an error saying the file doesn't exist, run this to create it first:

```
echo '{}' > ~/Library/Application\ Support/Claude/claude_desktop_config.json && open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Edit the file

Replace the entire contents of the file with the following — substituting your username and API keys:

```json
{
  "mcpServers": {
    "moss": {
      "command": "/Users/your-username/mcp-servers/moss-mcp-server/.venv/bin/python",
      "args": ["/Users/your-username/mcp-servers/moss-mcp-server/server.py"],
      "env": {
        "MOSS_API_PUBLIC_KEY": "kid_your_key_id_here",
        "MOSS_API_SECRET_KEY": "sk_your_secret_key_here"
      }
    }
  }
}
```

Replace:
- `your-username` (in both places) → your username from Step 4, e.g. `anneliese`
- `kid_your_key_id_here` → your Key ID from MOSS
- `sk_your_secret_key_here` → your Secret Key from MOSS

The `command` points directly at the Python inside your virtual environment, which ensures the right packages are always used.

Save the file (`Cmd + S`) and close TextEdit.

> **Already have other MCP servers?** Add the `"moss": { ... }` block inside your existing `"mcpServers"` section rather than replacing the whole file.

---

## Step 6 — Restart Claude Desktop

Quit Claude Desktop completely (`Cmd + Q`) and reopen it.

Click the **🔨 hammer icon** in the chat input area. You should see `run_month_end_check` and `get_vendor_history` listed. If you don't see the hammer, or the tools aren't listed, check the Troubleshooting section below.

---

## Using it

Just ask Claude in plain English:

> "Run the MOSS month-end check"

> "Check MOSS for May 2026"

> "What has Stripe been coded to in MOSS over the last 6 months?"

Claude will call MOSS directly and show you the results.

---

## Sharing with a colleague

Each person needs their own MOSS API key — keys are linked to the account that created them.

Send your colleague this zip file and ask them to follow this guide from Step 1. They generate their own key in Step 3 and use their own path in Step 4.

**Never share your `sk_...` secret key over Slack, email, or chat.**

---

## Troubleshooting

**Tools don't appear after restarting Claude Desktop**
- Check the config file is valid JSON (no missing commas or brackets). Paste it into [jsonlint.com](https://jsonlint.com) to check.
- Make sure the path to `server.py` is correct and the file exists at that location.

**"MOSS authentication failed"**
- Your keys are wrong or expired. Return to MOSS → API Keys, generate a new pair, and update the config file. Restart Claude Desktop.

**"python3: command not found" or "No such file or directory"**
- The path to the virtual environment Python is wrong. In Terminal, run `ls ~/mcp-servers/moss-mcp-server/.venv/bin/python` — if you get an error, the venv wasn't created. Go back to Step 2 and re-run the setup commands.

**Claude runs the check but shows "Unknown" for vendors or categories**
- The field names in your MOSS account may differ slightly. Note which values are showing as Unknown and share with Tom to update the script.
