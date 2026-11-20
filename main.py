#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261120:
"Sum up 20 November's world news in one image."

Writes the entry image to /output/entry.png. The image ships in this
repository as entry.png: a 1024x1024 newspaper front page carrying 54
sourced stories of Friday 20 November 2026 — Russia's 510-weapon
barrage on Kyiv, Asia's worst market week since 2020, Cyclone Akvan's
landfall in Odisha, GTA VI's record $3.79bn first day, and 50 more —
with a UTC timeline strip, an IN BRIEF numbers strip and a date-check
footer. Copying a fixed
file keeps the program offline and byte-for-byte deterministic
across runs, as required. See SOURCES.md for the reporting behind
every story on the page.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
