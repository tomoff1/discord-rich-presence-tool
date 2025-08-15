# Discord Rich Presence (RPC) — Minimal Tool

> **Public, safe & privacy-friendly version.**  
> No personal IDs or links are included. The user sets their own **Application ID (client_id)** and **IMAGE KEY**.

## What it does
Shows a custom Rich Presence in your Discord profile using the official RPC (no selfbot).

## Quick Start (Windows / macOS / Linux)
1. Create an app at https://discord.com/developers/applications → copy your **Application ID**.  
2. In **Rich Presence → Art Assets**, upload a square logo (512x512+) and note the **IMAGE KEY** (e.g. `logo`).  
3. Clone this repo or download the ZIP.  
4. Install deps:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Configure your values in **`config.json`** (see below).  
6. Start Discord (desktop), then run:
   ```bash
   python main.py
   ```

## Configuration
Edit `config.json`:
```jsonc
{
  "client_id": "PASTE_YOUR_APPLICATION_ID_HERE",
  "details": "My custom activity",
  "state": "discord.gg/yourinvite",
  "large_image": "logo",          // IMAGE KEY from Art Assets
  "large_text": "Hover text",
  "start_timestamp": true,
  "buttons": [
    { "label": "Join", "url": "https://discord.com" },
    { "label": "Website", "url": "https://example.com" }
  ]
}
```
Tips:
- Use max **2 buttons** (Discord limit).
- To show **two lines** in your profile (game + custom), keep a game running while this script runs.

## Troubleshooting
- **`Client ID is Invalid`** → `client_id` does not match your app’s **Application ID**.
- **Image not showing** → `large_image` must match the **IMAGE KEY** exactly (case-sensitive). Also fully quit and relaunch Discord (cache).
- **No module named pypresence** → run `python -m pip install -r requirements.txt`.
- Still stuck? Run `python diag.py` for a printed check.

## License
MIT — see `LICENSE`.
