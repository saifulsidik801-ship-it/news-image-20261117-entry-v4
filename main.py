#!/usr/bin/env python3
"""news-image-20261117 v4 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file, and the program
copies it to /output/entry.png. The image itself was drawn by the
builder's own render script and committed here; the graded program
needs no network and no third-party package.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
print("wrote", os.path.join(OUT, "entry.png"))
