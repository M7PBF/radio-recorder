#!/bin/bash
ffmpeg -i "http://example.com/stream.mp3" -t 20 -acodec copy test.mp3