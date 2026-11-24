"""Draws the lead-magnet page's marker scenes with the carousel helpers (same strokes, same wobble) and
writes them into index.html between <!--scene:NAME--> and <!--/scene--> markers.

Run after changing a scene: python3 make_scenes.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "carousels", "engine"))
from scenes import INK, S, F, head, hand, body, face, drop  # noqa: E402


def calculator():
    """A big calculator reading RM ? with a grid of round keys."""
    keys = "".join(f'<rect x="{128 + c * 64}" y="{228 + r * 62}" width="46" height="40" rx="12" fill="{INK}"/>'
                   for r in range(3) for c in range(3))
    return (f'<rect x="96" y="56" width="256" height="420" rx="30" {F}/>'
            f'<rect x="124" y="88" width="200" height="104" rx="14" {F} stroke-width="11"/>'
            f'<text x="224" y="160" font-size="56" text-anchor="middle" fill="{INK}">RM ?</text>{keys}'
            f'<rect x="128" y="414" width="174" height="40" rx="12" fill="{INK}"/>')


SCENES = {
    # Intro: pointing at a giant calculator that reads RM ?
    "kira": f'''{calculator()}
      <path d="M434 358 L422 466 L394 466 M466 358 L478 466 L506 466" {S}/>
      <path d="M418 250 L362 224 M482 250 L520 304 L488 340" {S}/>
      {body(450, 230)}
      {hand(356, 222)}{hand(486, 338)}
      {face(450, 230, "smile")}
      <path d="M548 112 l22 -14 M556 150 l26 2 M540 76 l8 -24" {S} stroke-width="11"/>''',

    # Result, with someone who depends on them: dad and kid dry under one umbrella in the rain
    "payung": f'''
      <path d="M44 70 l-14 34 M76 168 l-14 34 M34 270 l-14 34 M74 372 l-14 34 M552 76 l-14 34 M582 178 l-14 34
               M546 282 l-14 34 M580 384 l-14 34 M190 14 l-10 26 M420 14 l-10 26" {S} stroke-width="9"/>
      <path d="M300 180 L300 404 Q300 434 274 434 Q250 434 250 410" {S}/>
      <path d="M100 180 Q300 -10 500 180 Q450 150 400 180 Q350 150 300 180 Q250 150 200 180 Q150 150 100 180 Z" {F}/>
      <path d="M300 86 L300 58" {S}/>
      <path d="M204 390 L196 468 L170 468 M236 390 L244 468 L270 468" {S}/>
      <path d="M248 300 L298 332 M192 300 L168 372" {S}/>
      {body(220, 280, h=110)}
      {hand(300, 332)}{hand(166, 374, 13)}
      {face(220, 280, "smile")}
      <path d="M380 414 L376 468 L356 468 M400 414 L404 468 L424 468" {S}/>
      <path d="M368 356 L308 384 M412 356 L432 402" {S}/>
      {body(390, 340, w=24, h=74)}
      {hand(304, 384, 12)}{hand(432, 404, 12)}
      {face(390, 340, "smile", r=30)}''',

    # Result, nobody depends on them: alone and dry under the umbrella
    "payung_solo": f'''
      <path d="M44 70 l-14 34 M76 168 l-14 34 M34 270 l-14 34 M74 372 l-14 34 M552 76 l-14 34 M582 178 l-14 34
               M546 282 l-14 34 M580 384 l-14 34 M190 14 l-10 26 M420 14 l-10 26" {S} stroke-width="9"/>
      <path d="M330 180 L330 404 Q330 434 356 434 Q380 434 380 410" {S}/>
      <path d="M100 180 Q300 -10 500 180 Q450 150 400 180 Q350 150 300 180 Q250 150 200 180 Q150 150 100 180 Z" {F}/>
      <path d="M300 86 L300 58" {S}/>
      <path d="M264 390 L256 468 L230 468 M296 390 L304 468 L330 468" {S}/>
      <path d="M308 300 L330 330 M252 300 L228 372" {S}/>
      {body(280, 280, h=110)}
      {hand(332, 332)}{hand(226, 374, 13)}
      {face(280, 280, "smile")}''',
}

LABELS = {
    "kira": "Lukisan: seorang lelaki menunjuk kalkulator besar yang tertulis RM ?",
    "payung": "Lukisan: ayah dan anak kering di bawah satu payung ketika hujan",
    "payung_solo": "Lukisan: seorang lelaki kering di bawah payung ketika hujan",
}


def svg(name, n):
    return (f'<svg viewBox="0 0 600 520" role="img" aria-label="{LABELS[name]}" font-family="Plus Jakarta Sans" font-weight="800">'
            f'<filter id="hand{n}"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="{n + 3}"/>'
            f'<feDisplacementMap in="SourceGraphic" scale="6"/></filter>'
            f'<g filter="url(#hand{n})">{" ".join(SCENES[name].split())}</g></svg>')


path = os.path.join(HERE, "index.html")
html = open(path, encoding="utf-8").read()
for n, name in enumerate(SCENES):
    html, hits = re.subn(rf"<!--scene:{name}-->.*?<!--/scene-->",
                         lambda m: f"<!--scene:{name}-->{svg(name, n)}<!--/scene-->", html, flags=re.S)
    print(name, "placed" if hits else "NO MARKER IN index.html")
open(path, "w", encoding="utf-8").write(html)
