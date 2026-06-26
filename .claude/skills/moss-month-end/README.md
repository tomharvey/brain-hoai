# MOSS Month-End Checker

Connects Claude Desktop to your MOSS account so you can run month-end checks by asking Claude in plain English.

**What it checks:**
- Invoices coded inconsistently (same merchant, different categories across months)
- Recurring vendors missing from this month (likely need accruing)
- Unapproved recurring items that haven't been signed off yet

---

## Setup (~10 minutes)

### 1. Generate your MOSS API keys

Ask **Kirsty** or **Jade** to generate a read-only API key for you in MOSS, or if you have admin access:

1. Log into MOSS and go to **Settings > Company Settings > API Keys**
2. Click **Generate API Key** — set scope to **read only**
3. Copy both values immediately — MOSS only shows them once:
   - **Key ID** — starts with `kid_...`
   - **Secret Key** — starts with `sk_...`
4. Save them in your password manager

### 2. Run the installer

1. Open the downloaded `moss-month-end` folder in Finder
2. Right-click the folder and choose **New Terminal at Folder** (or **Services > New Terminal at Folder** on older macOS)
3. In the Terminal window that opens, type the following and press Enter:

```
bash install.sh
```

The script will:
- Check Python 3 is installed (if not, it tells you where to get it)
- Create a hidden environment at `~/.moss-month-end/`
- Install the required packages
- Print a JSON block to add to your Claude Desktop config

If Python 3 is missing, download and install it from:
https://www.python.org/ftp/python/3.13.14/python-3.13.14-macos11.pkg

Then re-run the installer.

### 3. Configure Claude Desktop

Open the Claude Desktop config file. In Terminal:

```
open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

If the file doesn't exist, create it first:

```
echo '{}' > ~/Library/Application\ Support/Claude/claude_desktop_config.json
open -a TextEdit ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Paste the JSON block the installer printed inside the `"mcpServers"` object. Replace the placeholder key values with your actual MOSS API keys from step 1.

Save (`Cmd + S`) and close TextEdit.

> **Already have other MCP servers?** Add the `"moss": { ... }` block inside your existing `"mcpServers"` section rather than replacing the whole file.

### 4. Restart Claude Desktop

Quit Claude Desktop (`Cmd + Q`) and reopen it. Click the **hammer icon** in the chat input — you should see the MOSS tools listed.

---

## Using it

Ask Claude in plain English:

> "Run the MOSS month-end check"

> "Check MOSS for May 2026"

> "What has Stripe been coded to in MOSS over the last 6 months?"

---

## Updating

When you receive an updated version, just re-run the installer:

```
bash /path/to/install.sh
```

It will update the server and dependencies in place. Restart Claude Desktop afterwards.

---

## Sharing with a colleague

Each person needs their own MOSS API key — keys are linked to the account that created them.

Send this folder to your colleague and ask them to follow this guide from step 1. They generate their own key and run the installer themselves.

**Never share your `sk_...` secret key over Slack, email, or chat.**

---

## Troubleshooting

**Tools don't appear after restarting Claude Desktop**
- Check the config file is valid JSON (no missing commas or brackets). Paste it into [jsonlint.com](https://jsonlint.com) to check.
- Make sure the paths in the config match what the installer printed.

**"MOSS authentication failed"**
- Your keys are wrong or expired. Generate a new pair in MOSS and update the config file. Restart Claude Desktop.

**"Python 3 not found"**
- Download and install from: https://www.python.org/ftp/python/3.13.14/python-3.13.14-macos11.pkg
- Then re-run the installer.

**Claude shows "Unknown" for vendors or categories**
- The field names in your MOSS account may differ. Note which values show as Unknown and share with Tom to update the script.
