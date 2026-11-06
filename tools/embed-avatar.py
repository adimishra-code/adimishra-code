#!/usr/bin/env python3
"""
Embed your GitHub avatar into assets/hero.svg (circular, inside the purple glow ring).

Why this exists: GitHub README images cannot load other images from inside an SVG,
so the avatar has to be embedded into hero.svg itself.

Usage (run from anywhere, Python 3 only, no extra packages):
    python tools/embed-avatar.py                 # downloads github.com/adimishra-code.png
    python tools/embed-avatar.py my-photo.png    # or use a local PNG / JPG / WEBP

Then commit and push assets/hero.svg. You can re-run it any time to change the photo.
"""
import base64
import pathlib
import re
import sys
import urllib.request

USER = "adimishra-code"
HERO = pathlib.Path(__file__).resolve().parent.parent / "assets" / "hero.svg"
CX, CY, R = 130, 186, 80          # must match the avatar circle in hero.svg
MAX_BYTES = 400 * 1024


def sniff(data):
    if data.startswith(b"\x89PNG"):
        return "image/png"
    if data.startswith(b"\xff\xd8"):
        return "image/jpeg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    raise SystemExit("Unsupported image type. Use PNG, JPG or WEBP.")


def load(src):
    if src:
        data = pathlib.Path(src).read_bytes()
    else:
        url = f"https://github.com/{USER}.png?size=240"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    return data, sniff(data)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else None
    data, mime = load(src)
    if len(data) > MAX_BYTES:
        raise SystemExit(f"Image is {len(data)//1024} KB. Please use one under {MAX_BYTES//1024} KB (a 240x240 image is plenty).")
    b64 = base64.b64encode(data).decode("ascii")
    block = (
        "<!--AVATAR_START-->\n"
        f'<clipPath id="avatarClip"><circle cx="{CX}" cy="{CY}" r="{R}"/></clipPath>\n'
        f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="#151126"/>\n'
        f'<image href="data:{mime};base64,{b64}" x="{CX-R}" y="{CY-R}" width="{2*R}" height="{2*R}" '
        'preserveAspectRatio="xMidYMid slice" clip-path="url(#avatarClip)"/>\n'
        "<!--AVATAR_END-->"
    )
    svg = HERO.read_text(encoding="utf-8")
    new, n = re.subn(r"<!--AVATAR_START-->.*?<!--AVATAR_END-->", lambda m: block, svg, flags=re.S)
    if n != 1:
        raise SystemExit("Could not find the AVATAR_START / AVATAR_END markers in hero.svg.")
    HERO.write_text(new, encoding="utf-8")
    print(f"Avatar embedded into {HERO} ({len(data)//1024} KB). Now commit and push assets/hero.svg.")


if __name__ == "__main__":
    main()
