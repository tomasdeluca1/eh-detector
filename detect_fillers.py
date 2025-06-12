import sys
import os
import subprocess
import whisper
import re
import json
from yt_dlp import YoutubeDL

VIDEO_URL = sys.argv[1]
AUDIO_FILE = "audio.wav"
# Extended list of common fillers
FILLERS = [
    "uh", "um", "eh", "like", "you know", "i mean", "so", "actually", "basically",
    "right", "well", "hmm", "okay", "e"
]
PAUSE_THRESHOLD = 1.5  # seconds


def download_audio(url):
    print("Downloading audio...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def transcribe():
    print("Transcribing with Whisper...")
    model = whisper.load_model("large")
    return model.transcribe(AUDIO_FILE, word_timestamps=True)


def analyze_fillers(text):
    results = {}
    text = text.lower()
    for filler in FILLERS:
        # Special handling for "e" to avoid matching every word with "e" in it
        if filler == "e":
            results[filler] = len(re.findall(rf"\b{filler}\b", text))
        else:
            results[filler] = len(re.findall(rf"\b{re.escape(filler)}\b", text))
    return results


def analyze_pauses(segments):
    pauses = 0
    for i in range(1, len(segments)):
        prev_end = segments[i - 1]['end']
        curr_start = segments[i]['start']
        if curr_start - prev_end > PAUSE_THRESHOLD:
            pauses += 1
    return pauses


def main():
    download_audio(VIDEO_URL)
    result = transcribe()

    print("Analyzing...")
    fillers = analyze_fillers(result['text'])
    pauses = analyze_pauses(result['segments'])

    print("\nResult:")
    for word, count in fillers.items():
        print(f"{word}: {count}")
    print(f"long pauses (>{PAUSE_THRESHOLD}s): {pauses}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python detect_fillers.py <YouTube URL>")
        sys.exit(1)
    main()
