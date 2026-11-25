"""Draws the checklist's marker scenes with the carousel helpers (same strokes, same wobble as the reels) and
writes them into index.html between the /*art*/ and /*/art*/ markers, as the ART object the page uses.

Scenes change with what the visitor chooses:
- the 2 opening questions: one scene per kind of work (mula = nothing chosen yet), plus a small house when they have a house loan
- the result: dry under an umbrella (few gaps) or a leaking umbrella (many gaps)

Run after changing a scene: python3 make_scenes.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "carousels", "engine"))
from scenes import INK, S, F, body, drop, envelope, face, hand, person  # noqa: E402

PAPER = "#FFFFFF"  # the page background, used to punch holes in the umbrella
RED = "#D31145"


def question():
    """A big marker question mark above a head at x=cx."""
    return (f'<path d="M278 50 Q278 18 302 18 Q326 18 326 44 Q326 62 302 70 L302 94" {S} stroke-width="12"/>'
            f'<circle cx="302" cy="122" r="9" fill="{INK}"/>')


def awning(x0=40, x1=400, y=110, h=50):
    """A stall awning with a scalloped edge."""
    n, w = 10, (x1 - x0) / 10
    edge = "".join(f" Q{x1 - w * (k + .5):.0f} {y + h + 26} {x1 - w * (k + 1):.0f} {y + h}" for k in range(n))
    return f'<path d="M{x0} {y} L{x1} {y} L{x1} {y + h}{edge} Z" {F}/>'


WORK = {
    # Nothing chosen yet: not sure, a question mark over the head
    "mula": f'''{question()}
      {person(300, 252, "worry", [(222, 352), (378, 352)])}''',

    # Makan gaji: an office block behind, holding up the monthly pay envelope
    "gaji": f'''
      <rect x="30" y="140" width="150" height="340" rx="6" {F}/>
      {"".join(f'<rect x="{56 + c * 62}" y="{170 + r * 66}" width="36" height="38" rx="4" {F} stroke-width="10"/>' for r in range(3) for c in range(2))}
      <path d="M88 480 L88 428 L122 428 L122 480" {S} stroke-width="12"/>
      {envelope(232, 62, w=176, h=118, rot=-4, label="GAJI", size=40)}
      {person(322, 262, "smile", [(262, 196), (384, 190)])}''',

    # Kerja sendiri: behind the counter of their own stall
    "sendiri": f'''
      <path d="M62 150 L62 482 M378 150 L378 482" {S}/>
      {person(220, 214, "smile", [(150, 322), (290, 322)])}
      <rect x="290" y="268" width="70" height="56" rx="6" {F} stroke-width="12"/>
      <rect x="34" y="326" width="372" height="66" rx="8" {F}/>
      <text x="220" y="374" font-size="40" font-weight="800" text-anchor="middle" fill="{INK}">KEDAI</text>
      {awning()}''',

    # Gig / p-hailing: on a motorbike with a delivery box
    "gig": f'''
      <path d="M8 392 L58 392 M20 432 L64 432" {S} stroke-width="11"/>
      <rect x="40" y="226" width="116" height="104" rx="8" {F}/>
      <path d="M40 262 L156 262" {S} stroke-width="11"/>
      <circle cx="126" cy="430" r="48" {F}/><circle cx="342" cy="430" r="48" {F}/>
      <path d="M126 430 L196 360 L306 360 L342 430 M306 360 L292 296 M276 290 L322 284" {S}/>
      <path d="M150 350 L262 350" {S} stroke-width="22"/>
      <path d="M212 332 L268 372 L250 428" {S}/>
      <path d="M244 254 L292 294" {S}/>
      {body(222, 232, w=30, h=100)}
      {hand(296, 296)}
      {face(222, 232, "smile", r=38)}''',
}

# A small house with LOAN under it, on the right side (only when they have a house loan)
HOUSE = f'''
      <rect x="458" y="300" width="118" height="112" rx="4" {F}/>
      <path d="M440 306 L517 236 L594 306 Z" {F}/>
      <path d="M502 412 L502 352 L532 352 L532 412" {S} stroke-width="11"/>
      <text x="517" y="470" font-size="38" font-weight="800" text-anchor="middle" fill="{INK}">LOAN</text>'''

# Hero (wide, 900x430): salary goes into a bucket marked GAJI, but it leaks; one leak is circled in red and labelled JURANG
HERO = f'''
      {person(140, 160, "worry", [(262, 268), (44, 262)])}
      <circle cx="430" cy="62" r="30" {F} stroke-width="11"/><text x="430" y="72" font-size="24" font-weight="800" text-anchor="middle" fill="{INK}">RM</text>
      <circle cx="548" cy="92" r="30" {F} stroke-width="11"/><text x="548" y="102" font-size="24" font-weight="800" text-anchor="middle" fill="{INK}">RM</text>
      <path d="M430 12 L430 22 M548 40 L548 52 M490 30 L490 46" {S} stroke-width="8"/>
      <path d="M330 170 Q490 60 650 170" {S}/>
      <path d="M318 170 L662 170 L622 404 L358 404 Z" {F}/>
      <text x="490" y="290" font-size="78" font-weight="800" text-anchor="middle" fill="{INK}">GAJI</text>
      <circle cx="420" cy="372" r="13" fill="{INK}"/><circle cx="548" cy="372" r="13" fill="{INK}"/><circle cx="640" cy="300" r="13" fill="{INK}"/>
      <path d="M416 392 Q400 404 398 420 M546 392 Q556 408 558 420" {S} stroke-width="9"/>
      {drop(396, 384)}{drop(560, 386)}
      <path d="M652 302 Q700 308 708 362" {S} stroke-width="9"/>
      {drop(710, 372)}{drop(700, 402)}
      <path d="M690 262 C622 258 604 316 618 372 C634 428 734 434 760 378 C782 326 760 264 678 268" fill="none" stroke="{RED}" stroke-width="9" stroke-linecap="round"/>
      <path d="M800 196 Q790 232 752 256 M752 256 l6 -24 M752 256 l24 -2" {S} stroke-width="7"/>
      <text x="800" y="172" font-family="Caveat, cursive" font-size="62" font-weight="700" text-anchor="middle" fill="{INK}" transform="rotate(-6 800 172)">JURANG</text>'''

CANOPY = "M100 180 Q300 -10 500 180 Q450 150 400 180 Q350 150 300 180 Q250 150 200 180 Q150 150 100 180 Z"
RAIN = " ".join(f"M{x} {y} l-14 34" for x, y in [(44, 70), (76, 168), (34, 270), (74, 372), (552, 76), (582, 178),
                                                 (546, 282), (580, 384), (190, 14), (420, 14)])
RESULT = {
    # Few gaps: dry under the umbrella in the rain
    "kering": f'''
      <path d="{RAIN}" {S} stroke-width="9"/>
      <path d="M300 180 L300 330 Q300 358 324 358 Q346 358 346 336" {S}/>
      <path d="{CANOPY}" {F}/><path d="M300 86 L300 58" {S}/>
      {person(236, 262, "smile", [(300, 300), (180, 360)])}''',

    # Many gaps: the umbrella has holes and the rain gets through
    "bocor": f'''
      <path d="{RAIN}" {S} stroke-width="9"/>
      <path d="M300 180 L300 330 Q300 358 324 358 Q346 358 346 336" {S}/>
      <path d="{CANOPY}" {F}/><path d="M300 86 L300 58" {S}/>
      <circle cx="214" cy="124" r="15" fill="{PAPER}" stroke="{INK}" stroke-width="9"/>
      <circle cx="372" cy="96" r="13" fill="{PAPER}" stroke="{INK}" stroke-width="9"/>
      <circle cx="430" cy="150" r="12" fill="{PAPER}" stroke="{INK}" stroke-width="9"/>
      {drop(214, 160)}{drop(206, 206)}{drop(372, 128)}{drop(430, 190)}
      {person(236, 262, "worry", [(300, 300), (180, 360)])}''',
}


# One small drawing per checklist section, for the gap cards (same order as LIST in index.html)
SECTION = [
    # Kalau MC lama: sick in bed
    f'''<path d="M40 300 L40 478 M560 380 L560 478" {S}/>
      <rect x="40" y="360" width="520" height="46" rx="8" {F}/>
      <ellipse cx="124" cy="338" rx="60" ry="24" {F}/>
      <rect x="182" y="300" width="378" height="72" rx="30" {F}/>
      <circle cx="128" cy="292" r="44" {F}/>
      <circle cx="114" cy="286" r="6" fill="{INK}"/><circle cx="142" cy="286" r="6" fill="{INK}"/>
      <path d="M112 312 Q128 302 144 312" {S} stroke-width="8"/>
      <path d="M150 250 L196 212" {S} stroke-width="13"/><circle cx="204" cy="206" r="12" fill="{INK}"/>
      <text x="420" y="190" font-size="76" font-weight="800" text-anchor="middle" fill="{INK}">MC</text>''',
    # Kalau kemalangan atau hilang upaya: on a crutch, one leg bandaged
    f'''<path d="M408 220 L408 492 M378 228 L438 228" {S}/>
      {person(300, 228, "worry", [(408, 236), (220, 330)])}
      <path d="M244 420 L292 420 M244 446 L288 446 M246 470 L286 470" {S} stroke-width="10"/>''',
    # Kalau sakit kritikal: a heart with a heartbeat line through it
    f'''<path d="M300 150 C230 40 70 100 120 250 C150 340 240 400 300 460 C360 400 450 340 480 250 C530 100 370 40 300 150 Z" fill="{INK}"/>
      <path d="M60 300 L200 300 L236 230 L282 380 L330 260 L360 300 L540 300" fill="none" stroke="#fff" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M60 300 L200 300 L236 230 L282 380 L330 260 L360 300 L540 300" {S} stroke-width="14"/>''',
    # Kalau korang tiada: the family under an umbrella
    f'''<path d="M300 180 L300 300" {S}/>
      <path d="{'M100 180 Q300 -10 500 180 Q450 150 400 180 Q350 150 300 180 Q250 150 200 180 Q150 150 100 180 Z'}" {F}/>
      {person(210, 300, "smile", [(150, 400), (296, 300)], legs=200)}
      <path d="M392 404 L380 498 M408 404 L420 498 M378 362 L340 410 M422 362 L452 410" {S}/>
      {body(400, 350, w=24, h=60)}{face(400, 350, "smile", r=30)}''',
    # Supaya pelan tak lupus: an hourglass running low
    f'''<path d="M190 40 L410 40 M190 480 L410 480" {S}/>
      <path d="M214 48 C214 170 282 220 282 260 C282 300 214 350 214 472 L386 472 C386 350 318 300 318 260 C318 220 386 170 386 48 Z" {F}/>
      <path d="M272 232 L328 232 L300 262 Z" fill="{INK}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>
      <path d="M226 466 Q300 360 374 466 Z" fill="{INK}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>''',
]


def clean(svg):
    return re.sub(r"\s+", " ", svg).strip()


# ---------- SME page (sme/index.html): its own hero, business-type scenes and section drawings ----------
GHOST = "#C9C6D3"
# Hero (wide, 960x440): the team holds up the company; one place is empty, so that end sags. The empty place is circled and labelled GAP
SME_HERO = f'''
      {person(120, 214, "smile", [(62, 116), (178, 116)], legs=206)}
      {person(310, 214, "smile", [(252, 116), (368, 116)], legs=206)}
      {person(500, 214, "worry", [(442, 116), (558, 124)], legs=206)}
      <path d="M30 40 L600 40 L840 74 L840 138 L600 104 L30 104 Z" {F}/>
      <text x="318" y="90" font-size="44" font-weight="800" text-anchor="middle" fill="{INK}">YOUR COMPANY</text>
      <circle cx="720" cy="196" r="38" fill="none" stroke="{GHOST}" stroke-width="10"/>
      <path d="M702 240 L738 240 L738 352 L702 352 Z M706 352 L692 420 M734 352 L748 420 M700 262 L664 322 M740 262 L776 322" fill="none" stroke="{GHOST}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M716 132 C630 128 618 250 630 344 C644 448 800 452 812 344 C822 246 812 138 704 138" fill="none" stroke="{RED}" stroke-width="9" stroke-linecap="round"/>
      <path d="M892 196 Q880 228 838 250 M838 250 l8 -24 M838 250 l25 0" {S} stroke-width="7"/>
      <text x="894" y="176" font-family="Caveat, cursive" font-size="64" font-weight="700" text-anchor="middle" fill="{INK}" transform="rotate(-6 894 176)">GAP</text>'''

SME_WORK = {
    "mula": WORK["mula"],
    # Sdn Bhd: an office block with the owner beside it
    "sdn": f'''
      <rect x="40" y="120" width="190" height="360" rx="6" {F}/>
      {"".join(f'<rect x="{70 + c * 78}" y="{154 + r * 72}" width="44" height="42" rx="4" {F} stroke-width="10"/>' for r in range(3) for c in range(2))}
      <path d="M112 480 L112 420 L158 420 L158 480" {S} stroke-width="12"/>
      {person(390, 252, "smile", [(310, 352), (470, 352)])}''',
    # Partnership: two partners side by side
    "partner": f'''
      {person(200, 252, "smile", [(120, 352), (296, 300)])}
      {person(400, 252, "smile", [(304, 300), (480, 352)])}''',
    # Sole proprietor: behind the counter of their own shop
    "sole": f'''
      <path d="M62 150 L62 482 M378 150 L378 482" {S}/>
      {person(220, 214, "smile", [(150, 322), (290, 322)])}
      <rect x="34" y="326" width="372" height="66" rx="8" {F}/>
      <text x="220" y="374" font-size="40" font-weight="800" text-anchor="middle" fill="{INK}">SHOP</text>
      {awning()}''',
}

SME_SECTION = [
    SECTION[0],   # an employee falls sick
    SECTION[1],   # an employee is injured or can't work again
    # a key person: someone holding a big key
    f'''{person(230, 232, "smile", [(360, 262), (150, 330)])}
      <circle cx="430" cy="170" r="50" {F}/><circle cx="430" cy="170" r="12" fill="{INK}"/>
      <path d="M430 220 L430 430 M430 372 L478 372 M430 418 L466 418" {S}/>''',
    SECTION[3],   # the owner's family
]


def write(page, art):
    html = open(page, encoding="utf-8").read()
    block = "/*art*/const ART = " + json.dumps(art, ensure_ascii=False) + ";/*/art*/"
    html, n = re.subn(r"/\*art\*/.*?/\*/art\*/", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit(f"{page} needs exactly one /*art*/ ... /*/art*/ marker")
    open(page, "w", encoding="utf-8").write(html)


art = {"hero": clean(HERO), "work": {k: clean(v) for k, v in WORK.items()}, "house": clean(HOUSE),
       "result": {k: clean(v) for k, v in RESULT.items()}, "sec": [clean(v) for v in SECTION]}
write(os.path.join(HERE, "index.html"), art)
print("index.html:", ", ".join(["hero"] + list(WORK) + ["house"] + list(RESULT) + [f"sec{i}" for i in range(len(SECTION))]))

sme = os.path.join(HERE, "sme", "index.html")
if os.path.exists(sme):
    write(sme, {"hero": clean(SME_HERO), "work": {k: clean(v) for k, v in SME_WORK.items()}, "house": "",
                "result": {k: clean(v) for k, v in RESULT.items()}, "sec": [clean(v) for v in SME_SECTION]})
    print("sme/index.html:", ", ".join(["hero"] + list(SME_WORK) + list(RESULT) + [f"sec{i}" for i in range(len(SME_SECTION))]))
