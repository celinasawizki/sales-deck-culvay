#!/usr/bin/env python3
"""Rebuild ../index.html from the slide text files in this folder.

Run from anywhere:  python3 build.py
"""
import re, glob, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "_template.html")
OUT = os.path.join(HERE, "..", "index.html")

def to_html(text):
    text = text.strip("\n")
    # protect existing entities, then escape bare ampersands
    text = re.sub(r"&(?!#?\w+;)", "&amp;", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text, flags=re.S)
    return "<br>".join(text.split("\n"))

values = {}
for path in sorted(glob.glob(os.path.join(HERE, "[0-9][0-9]-*.txt"))):
    key, buf = None, []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            m = re.fullmatch(r"\[(\d\d\.\d+)\]", line.strip())
            if m:
                if key: values[key] = "\n".join(buf)
                key, buf = m.group(1), []
            elif key is not None and not line.startswith("#"):
                buf.append(line)
        if key: values[key] = "\n".join(buf)

tpl = open(TEMPLATE, encoding="utf-8").read()
missing = []
def sub(m):
    k = m.group(1)
    if k not in values:
        missing.append(k); return ""
    return to_html(values[k])
out = re.sub(r"\{\{(\d\d\.\d+)\}\}", sub, tpl)
open(OUT, "w", encoding="utf-8").write(out)
print(f"Updated index.html from {len(values)} text blocks.")
if missing:
    print("Warning: these blocks were missing and left empty:", ", ".join(missing))
