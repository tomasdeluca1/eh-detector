# 🎙️ Eh Detector

Ever watched your own video and thought: _“Damn, do I really say 'uh' that much?”_
Now you can **find out exactly how many filler words and awkward pauses you make** — straight from a YouTube link.

---

## ⚡ What it does

- Downloads the audio from a YouTube video
- Transcribes the speech using [OpenAI Whisper](https://github.com/openai/whisper)
- Counts all the nasty little filler words like:

  - `uh`, `um`, `eh`, `well`, `you know`, `i mean`, `like`, and more...

- Detects long pauses (default: >1.5 seconds)

---

## 🧠 Why?

If you're a content creator, podcaster, or speaker, this helps you:

- Improve your delivery
- Speak more clearly
- Sound less like you're buffering

---

## 🚀 Quickstart

### 1. Install dependencies

```bash
pip3 install yt-dlp openai-whisper ffmpeg-python
```

Make sure you have [`ffmpeg`](https://ffmpeg.org/) installed:

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

---

### 2. Run it with a YouTube URL

```bash
python3 detect_fillers.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

✅ That’s it. You’ll see something like:

```
Downloading audio...
Transcribing with Whisper...
Analyzing...

Result:
uh: 14
um: 8
like: 10
well: 6
e: 4
long pauses (>1.5s): 5
```

---

## 🛠 Tech Stack

- 🧠 [Whisper](https://github.com/openai/whisper) for speech-to-text
- 🔊 `yt-dlp` for YouTube audio extraction
- 🧪 Good ol' Python regex magic

---

## 📌 Coming Soon

- Export to JSON or CSV
- Highlight timestamps of each filler
- Web UI?

---

## 🤘 Author

Built by [Tomás Deluca](https://github.com/tomasdeluca1) aka [Huevsite](https://x.com/_huevsite) — powered by every “eh” he said on camera.

---

## 🧼 Pro tip

Wanna improve faster? Run this script after each upload. Track your progress like an athlete tracks their reps.
