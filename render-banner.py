#!/usr/bin/env python3
"""Render banner.svg, the header at the top of the profile readme.

A readme cannot carry a font, so the words are baked into vector outlines here
and the file that ships has no font-family in it at all. This is the same
approach as the header on the archy repository, with a different motif.

    python3 render-banner.py
    rsvg-convert -w 1600 banner.svg -o /tmp/banner.png    # to look at it

When the artwork changes, bump the ?v= in README.md too. Both the browser and
GitHub cache an image by its URL, so the same filename serves the old picture and
the page looks like nothing happened.
"""
import sys
from pathlib import Path

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent / "banner.svg"

FONT_CANDIDATES = [
    "/usr/share/fonts/TTF/JetBrainsMonoNerdFont-Bold.ttf",
    "/usr/share/fonts/TTF/JetBrainsMono-Bold.ttf",
    "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf",
    "/usr/share/fonts/TTF/CaskaydiaCoveNerdFont-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
]

BG_TOP, BG_BOTTOM = "#070b10", "#0a161d"
INK, ACCENT, DIM = "#eaf4f7", "#4fe3ff", "#4a6b78"
W, H = 1280, 300


class Outliner:
    """Text to SVG path data, so the letters do not depend on the reader's fonts."""

    def __init__(self, path: str):
        self.font = TTFont(path)
        self.upem = self.font["head"].unitsPerEm
        self.glyphs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.advance = self.font["hmtx"]

    def text(self, s: str, size: float, x: float, y: float,
             tracking: float = 0.0) -> tuple[str, float]:
        scale = size / self.upem
        parts, pen_x = [], x
        for ch in s:
            name = self.cmap.get(ord(ch))
            if name is None:
                pen_x += self.advance["space"][0] * scale + tracking
                continue
            pen = SVGPathPen(self.glyphs)
            self.glyphs[name].draw(TransformPen(
                pen, Transform(scale, 0, 0, -scale, pen_x, y)))
            parts.append(pen.getCommands())
            pen_x += self.advance[name][0] * scale + tracking
        return " ".join(parts), pen_x - x


def motif(x0: float, y0: float) -> str:
    """A dot grid that fades out, with two accent strokes across it."""
    dots = []
    for row in range(11):
        for col in range(16):
            fade = 1 - col / 15
            cx, cy = x0 + col * 30, y0 + row * 30
            dots.append(f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="{ACCENT}" '
                        f'fill-opacity="{0.22 * fade:.3f}"/>')
    lines = [
        f'<line x1="{x0 - 20}" y1="{y0 - 30}" x2="{x0 + 480}" y2="{y0 + 330}" '
        f'stroke="{ACCENT}" stroke-opacity="0.30" stroke-width="1.4"/>',
        f'<line x1="{x0 + 150}" y1="{y0 - 30}" x2="{x0 - 60}" y2="{y0 + 330}" '
        f'stroke="{ACCENT}" stroke-opacity="0.14" stroke-width="1.4"/>',
    ]
    return "\n      ".join(dots + lines)


def main() -> int:
    font_path = next((p for p in FONT_CANDIDATES if Path(p).exists()), None)
    if font_path is None:
        print("no usable mono font found; looked at:\n  " + "\n  ".join(FONT_CANDIDATES))
        return 1

    outliner = Outliner(font_path)
    wordmark, _ = outliner.text("itsdope", 118, 56, 172, tracking=-4)
    tagline, _ = outliner.text("learning ai and ml, building in public", 24, 60, 222)
    caption, _ = outliner.text("from nepal   github.com/Dopethedev", 17, 60, 262)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <title>itsdope</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{BG_TOP}"/>
      <stop offset="1" stop-color="{BG_BOTTOM}"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{ACCENT}" stop-opacity="0.9"/>
      <stop offset="0.55" stop-color="{ACCENT}" stop-opacity="0.25"/>
      <stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" rx="16" fill="url(#bg)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" fill="none"
        stroke="{ACCENT}" stroke-opacity="0.18"/>
  <rect x="24" y="0" width="560" height="3" rx="1.5" fill="url(#edge)"/>

  <g clip-path="inset(0 round 16px)">
      {motif(720, 60)}
  </g>

  <path d="{wordmark}" fill="{INK}"/>
  <path d="{tagline}" fill="{ACCENT}" fill-opacity="0.82"/>
  <path d="{caption}" fill="{DIM}"/>
</svg>
"""
    OUT.write_text(svg)
    print(f"{OUT.name}  {W}x{H}  font {Path(font_path).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
