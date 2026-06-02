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

## Step 2 — Install dependencies

In Terminal, navigate to the folder containing these files:

```
cd ~/Downloads/moss-month-end
```

(Adjust the path if you unzipped the folder somewhere else.)

Then run:

```
pip3 install -r requirements.txt
```

You should see it download and install `fastmcp` and `requests`. This only needs to be done once.

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

## Step 4 — Find the full path to server.py

In Terminal, run:

```
echo "$(pwd)/server.py"
```

Copy the output — it will look something like `/Users/anneliese/Downloads/moss-month-end/server.py`. You'll need this in the next step.

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

Replace the entire contents of the file with the following — filling in your own values for the three placeholders:

```json
{
  "mcpServers": {
    "moss": {
      "command": "python3",
      "args": ["/Users/anneliese/Downloads/moss-month-end/server.py"],
      "env": {
        "MOSS_API_PUBLIC_KEY": "kid_your_key_id_here",
        "MOSS_API_SECRET_KEY": "sk_your_secret_key_here"
      }
    }
  }
}
```

Replace:
- `/Users/anneliese/Downloads/moss-month-end/server.py` → the path you copied in Step 4
- `kid_your_key_id_here` → your Key ID from MOSS
- `sk_your_secret_key_here` → your Secret Key from MOSS

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

**"python3: command not found" or similar**
- Python isn't installed, or the wrong Python is being used. Try replacing `"command": "python3"` with `"command": "/usr/local/bin/python3"` (or run `which python3` in Terminal to find the right path).

**Claude runs the check but shows "Unknown" for vendors or categories**
- The field names in your MOSS account may differ slightly. Note which values are showing as Unknown and share with Tom to update the script.
