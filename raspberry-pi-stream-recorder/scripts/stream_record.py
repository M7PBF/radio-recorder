#!/usr/bin/env python3
"""
stream_record.py
Records an online audio stream for a fixed duration.

Configure:
- STREAM_URL: The stream you want to record
- DURATION: Duration in seconds
- SAVE_DIR: Where recordings go
"""

import subprocess
import datetime
import os

STREAM_URL = "http://example.com/stream.mp3"
DURATION = 1800  # 30 minutes
SAVE_DIR = "/home/pi/recordings/"

os.makedirs(SAVE_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
outfile = os.path.join(SAVE_DIR, f"recording_{timestamp}.mp3")

cmd = [
    "ffmpeg",
    "-y",
    "-i", STREAM_URL,
    "-t", str(DURATION),
    "-acodec", "copy",
    outfile
]

subprocess.run(cmd)