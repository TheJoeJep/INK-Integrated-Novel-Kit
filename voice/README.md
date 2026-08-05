# Voice

Two-way voice for the writing loop on **Windows**. No installs, no API keys, no dependencies.

---

## Input — built in, nothing to set up

Claude Code has native voice dictation. It works on Windows, doesn't consume tokens, and needs no
configuration.

```
/voice tap
```

Tap `Space`, speak, tap again — it transcribes and submits automatically (three words or more).
`/voice hold` is push-to-talk instead if you prefer.

**Why tap mode suits the writing loop:** most replies in `/write` are a letter or a short
redirection — *"B, but she doesn't speak yet"* — which is exactly what tap mode is good at.

Full docs: <https://code.claude.com/docs/en/voice-dictation>

**Requirements:** a Claude.ai account (not an API key), and a local microphone. It does not work
over SSH or on Claude Code for the web.

---

## Output — `speak.ps1`

The community voice-mode projects for Claude Code are almost all macOS-only — they lean on the
`say` command or Apple Silicon audio models. Windows has a perfectly good speech synthesiser
built into .NET that none of them use.

`speak.ps1` is a **Stop hook**. When a reply finishes, it reads the transcript, pulls the last
assistant message, strips everything unbearable to hear read aloud, and speaks it.

### Install

Add to `.claude/settings.json` in the story workspace:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "powershell -NoProfile -ExecutionPolicy Bypass -File \"path\\to\\ink\\voice\\speak.ps1\""
          }
        ]
      }
    ]
  }
}
```

### Controlling what gets said

**Default:** the reply is cleaned and truncated. Stripped out — code fences, markdown and
box-drawing tables, receipt blocks, URLs, file paths, headings, emphasis marks, and status
symbols. Truncation prefers a sentence boundary.

**Better:** wrap the part worth hearing in `<speak>` tags and only that is spoken.

```
<speak>Three directions for the next beat. A, he goes inside for supplies.
B, the dragon speaks. C, a car slows on the street.</speak>
```

For the `/write` loop this is the right pattern — you want to hear **the prose just written and
the options offered**, not the receipt block listing which documents changed.

### Options

```powershell
speak.ps1 -MaxChars 700 -Rate 1 -Voice "Microsoft Zira Desktop"
```

| | |
|---|---|
| `-MaxChars` | Cutoff before truncating. Default 700 |
| `-Rate` | `-10` slowest to `10` fastest. Default `1` |
| `-Voice` | Leave empty for the system default |

Voices installed on this machine: **Microsoft David Desktop**, **Microsoft Zira Desktop**.
Windows Settings → Time & Language → Speech adds more.

---

## What this is not

**It is not a live conversation.** You speak, it transcribes, I reply, it reads the reply. Turn
by turn — no interruption mid-sentence, no barge-in.

The macOS projects that do full duplex ([mcp-voice-hooks](https://github.com/johnmatthewtennant/mcp-voice-hooks),
[voice-mcp](https://github.com/shreyaskarnik/voice-mcp), [mcp-claude-say](https://github.com/alamparelli/mcp-claude-say))
get there by running speech recognition continuously in a browser or via MLX audio, and feeding
input while the model is still working. Porting one to Windows is possible — browser-based
recognition is cross-platform — but it's a real project, not a config change.

**Turn-by-turn is a reasonable fit for drafting anyway.** You want to hear a beat, think, and
answer — not talk over it.

---

## Reading on your phone

Separate from voice, and easier:

```powershell
python serve.py "path\to\your-novel" 8778 --lan
```

Prints a `http://<your-ip>:8778` address readable from any device on your wifi, sidebar and all.

**`--lan` means anyone on your network can read your manuscript.** Off by default for that
reason. You may also need to allow the port through Windows Firewall the first time.
