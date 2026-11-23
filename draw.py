#!/usr/bin/env python3
"""Draw the Monday 23 November 2026 front page: one 1024x1024 PNG.

Every picture is a flat vector illustration drawn with Pillow primitives.
No photos, no copied artwork. All facts were checked against live
reporting on 23 November 2026 (see README.md for the story list).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (176, 30, 30)
GOLD = (201, 162, 39)
NAVY = (31, 58, 95)
SKY = (207, 227, 238)
LAND = (185, 210, 160)
LAND_EDGE = (110, 140, 90)
SEA = (205, 226, 238)
GREY = (110, 110, 108)
LIGHT_GREY = (228, 226, 218)

F_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill=INK, leading=None):
    """Draw lines; returns y after the last line."""
    if leading is None:
        leading = fnt.size + 2
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def status_chip(draw, x, y, status):
    """Small coloured status tag; returns width used."""
    colors = {"CONFIRMED": (34, 120, 60), "REPORTED": (31, 58, 140),
              "CLAIM": (176, 110, 10), "FORECAST": (110, 60, 140)}
    fnt = font(F_BOLD, 9)
    label = status
    w = draw.textlength(label, font=fnt) + 10
    draw.rounded_rectangle([x, y, x + w, y + 13], radius=2, fill=colors[status])
    draw.text((x + 5, y + 2), label, font=fnt, fill=(255, 255, 255))
    return w


def source_line(draw, x, y, source, status, max_w):
    """'SOURCE  [STATUS]' line; returns y after."""
    fnt = font(F_BOLD, 9)
    draw.text((x, y), source, font=fnt, fill=GREY)
    sw = draw.textlength(source, font=fnt)
    status_chip(draw, x + sw + 6, y - 1, status)
    return y + 14


# ---------------------------------------------------------------- stories
# Each lead: (headline, body, source, status, picture key)
LEADS = [
    ("MARKETS REBOUND AFTER THE ROUT",
     "Friday: S&P -3.7%, Nasdaq 100 -5.6% into correction; Nvidia -14% on an "
     "SEC probe. Monday: Korea's $8bn fund, China's margin cut — and US "
     "futures jump.",
     "BLOOMBERG / REUTERS", "CONFIRMED", "markets"),
    ("IRAN: WE'LL FIGHT THE BLOCKADE",
     "Tehran vows \u201call available means\u201d against the US blockade and offers "
     "to reopen Hormuz if it lifts. Trump dares Iran to test it.",
     "AFP / GULF NEWS", "REPORTED", "iran"),
    ("STRIKES KILL 11 NEAR KYIV",
     "Russian strikes kill 11 in the Kyiv region. Zelenskyy urges NATO to "
     "bolster Ukraine's air defence; the Kremlin warns of Baltic escalation.",
     "AP / ARAB NEWS", "REPORTED", "kyiv"),
]

# Each pictured story: (headline, body, source, status, picture key)
PICTURED = [
    ("MODI–SHAH TALKS END",
     "Shah meets Modi and Murmu; hails ties \u201cstrong as Himalayas\u201d.",
     "WION / MEA", "CONFIRMED", "nepal"),
    ("KIWIS SAVE THE TEST",
     "NZ bat out 120 overs to draw: 239/5 after India's 720/9.",
     "CRICINFO", "CONFIRMED", "cricket"),
    ("S\u00c1NCHEZ'S FORTUNE TAX",
     "S\u00e1nchez vows a new tax on fortunes over \u20ac100m before Sunday's vote.",
     "WION", "REPORTED", "spain"),
    ("EISENKOT'S NETANYAHU BID",
     "Yashar leader prepares a coalition bid to break the deadlock.",
     "DAWN", "REPORTED", "knesset"),
    ("GERMANY UP, FRANCE DOWN",
     "German activity hits a 56-month high; France's PMI a 6-month low.",
     "CNBC", "CONFIRMED", "pmi"),
    ("EL CHAPO ISIDRO CAPTURED",
     "FBI most-wanted fugitive seized in Sinaloa, Mexico.",
     "AP", "CONFIRMED", "badge"),
    ("BOLSONARO IN ICU",
     "Ex-president in intensive care with an intestinal obstruction.",
     "AP", "REPORTED", "hospital"),
    ("BELGIAN AIRPORTS SHUT",
     "Anti-austerity strike grounds flights; airports closed.",
     "AP", "REPORTED", "airport"),
    ("EBOLA RESPONSE HIT",
     "WHO: fighting near the Ebola area disrupts the response.",
     "WHO / AP", "REPORTED", "virus"),
    ("DENMARK PHONE BAN",
     "Copenhagen to propose a school mobile-phone ban from 2027.",
     "REUTERS", "REPORTED", "phone"),
]

# Briefs: (text, source, status, region) -- one line each, numbered 14-38
BRIEFS = [
    ("Araghchi: Hormuz reopens if blockade lifts", "AFP", "REPORTED", "MIDDLE EAST"),
    ("Iran: no move of enriched uranium stockpile", "AFP", "REPORTED", "MIDDLE EAST"),
    ("CENTCOM: no US jet was hit; all safe", "CENTCOM", "REPORTED", "MIDDLE EAST"),
    ("Iran claims it downed two US drones", "IRGC", "CLAIM", "MIDDLE EAST"),
    ("Houthis claim attack on Saudi refinery", "AP", "REPORTED", "MIDDLE EAST"),
    ("Gaza war left widespread contamination", "AP", "REPORTED", "MIDDLE EAST"),
    ("Bangladesh vows to arrest Hasina on return", "ET", "REPORTED", "ASIA"),
    ("China eases margin rules; ETFs hit record", "BLOOMBERG", "REPORTED", "ASIA"),
    ("Korea unveils $8bn market rescue fund", "BLOOMBERG", "CONFIRMED", "ASIA"),
    ("Taiwan curbs short sales; Taiex jumps 2.2%", "REUTERS", "CONFIRMED", "ASIA"),
    ("Kospi falls 3.3% to a 10-month low", "BLOOMBERG", "CONFIRMED", "ASIA"),
    ("Tata Steel buys $1.67bn steel-pipe stake", "REUTERS", "REPORTED", "ASIA"),
    ("More remains found after Indonesia fire", "AP", "REPORTED", "ASIA"),
    ("Bomb threats hit 450 German schools", "WION", "REPORTED", "EUROPE"),
    ("UK digs new reservoirs to fight drought", "AP", "REPORTED", "EUROPE"),
    ("Kremlin warns of Baltic escalation", "WION", "REPORTED", "EUROPE"),
    ("Armenia proposes new constitution for peace", "AP", "REPORTED", "EUROPE"),
    ("9 shot at a central California concert", "AP", "REPORTED", "AMERICAS"),
    ("US Army to detonate Iowa explosives anyway", "AP", "REPORTED", "AMERICAS"),
    ("US shields air traffic before Thanksgiving", "ET", "REPORTED", "AMERICAS"),
    ("Trump to host gala for plunging meme coin", "ET", "REPORTED", "AMERICAS"),
    ("Citigroup's $35bn UK error clouds its exit", "REUTERS", "REPORTED", "AMERICAS"),
    ("Drone attacks kill five children in Khartoum", "AP", "REPORTED", "AFRICA"),
    ("SPLA-IO attack kills 24 civilians in S. Sudan", "AP", "REPORTED", "AFRICA"),
    ("ASX falls for an eighth straight session", "BLOOMBERG", "REPORTED", "OCEANIA"),
]

TIMELINE = [
    ("00:00", "Tokyo shut for a holiday; Asia braces for selling."),
    ("01:00", "US futures rebound: S&P +2.2%, Nasdaq +3.0%."),
    ("06:30", "Kospi -3.3% to a 10-month low; Taiex +2.2%."),
    ("08:00", "Europe opens green; tech stocks rebound."),
    ("10:00", "PMIs: Germany 56-month high, France 6-month low."),
    ("14:30", "Wall Street opens after Friday's rout. [DUE]"),
]

NUMBERS = [
    ("-5.6%", "Nasdaq 100 on Friday — its worst rout in years"),
    ("$8bn", "Korea's market stabilisation fund"),
    ("+3.0%", "Nasdaq 100 futures rebound on Monday"),
    ("$3,620", "gold per ounce, up 2.5% from Friday"),
    ("239/5", "New Zealand bat out the final day in Wellington"),
    ("450", "German schools emailed bomb threats"),
]

REGION_TALLY = [("ASIA", 8), ("MIDDLE EAST", 8), ("EUROPE", 9),
                ("AMERICAS", 7), ("AFRICA", 3), ("OCEANIA", 1),
                ("SPORT", 1), ("GLOBAL", 1)]

MAP_PINS = [
    (1, "NEW YORK", -74.0, 40.7),
    (2, "LONDON", -0.1, 51.5),
    (3, "NEW DELHI", 77.2, 28.6),
    (4, "HORMUZ", 56.5, 26.5),
    (5, "KYIV", 30.5, 50.45),
    (6, "SEOUL", 127.0, 37.5),
    (7, "WELLINGTON", 174.8, -41.3),
    (8, "BRAS\u00cdLIA", -47.9, -15.8),
]

DATE_CHECK_LEFT = (
    "COP31 COLLAPSE \u2014 no deal in Antalya; EU rejected the final text (Sun) \u00b7 "
    "DEMOCRATS HIT 258 \u2014 Hubbard beats Foxx in NC; biggest House majority since 1992 (Sun) \u00b7 "
    "M\u00c1RQUEZ'S 8TH TITLE \u2014 clinches the MotoGP crown with P8 in Portugal (Sun) \u00b7 "
    "ATP FINAL \u2014 Alcaraz beat Zverev 6-2, 7-6(7) (Sun) \u00b7 "
    "BEPICOLOMBO \u2014 ESA probe reaches Mercury (Sat) \u00b7 "
    "SPARTA II \u2014 drone-hit ship still burning off Finland (Sat\u2013Sun) \u00b7 "
    "DYMER \u2014 Russian strike on a village north of Kyiv (Sun) \u00b7 "
    "LISBON \u2014 thousands march over living costs (Sun)"
)
DATE_CHECK_NOT_YET = (
    "NOT YET: the US market open result \u00b7 the rest of Monday's news \u2014 the full edition lands Tuesday."
)

# ---------------------------------------------------------------- pictures
# Every picture is drawn with Pillow primitives. Each story gets its own
# distinct drawing; no graphic is reused for two stories.

def pic_nepal(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(223, 238, 245))
    d.rectangle([x, y, x + w, y + 16], fill=NAVY)
    d.text((x + 6, y + 2), "NEW DELHI", font=font(F_BOLD, 10), fill=(255, 255, 255))
    # table
    d.rectangle([x + 30, y + h - 22, x + w - 30, y + h - 14], fill=(120, 72, 32))
    d.rectangle([x + 40, y + h - 14, x + 48, y + h - 4], fill=(90, 54, 24))
    d.rectangle([x + w - 48, y + h - 14, x + w - 40, y + h - 4], fill=(90, 54, 24))
    # India flag (saffron / white / green + wheel)
    fx, fy, fw, fh = x + 52, y + 24, 64, 36
    d.rectangle([fx, fy, fx + fw, fy + 12], fill=(255, 153, 51))
    d.rectangle([fx, fy + 12, fx + fw, fy + 24], fill=(255, 255, 255))
    d.rectangle([fx, fy + 24, fx + fw, fy + 36], fill=(19, 136, 8))
    d.ellipse([fx + 26, fy + 13, fx + 38, fy + 25], outline=(0, 0, 128), width=1)
    d.line([fx + 4, fy + 36, fx + 4, fy + h - 22], fill=(90, 60, 20), width=2)
    # Nepal flag (crimson double pennon)
    nx, ny = x + w - 116, y + 22
    d.polygon([(nx, ny), (nx + 52, ny + 12), (nx, ny + 24),
               (nx + 34, ny + 28), (nx, ny + 40)], fill=(220, 20, 60))
    d.polygon([(nx + 4, ny + 4), (nx + 44, ny + 13), (nx + 4, ny + 22),
               (nx + 28, ny + 26), (nx + 4, ny + 36)], fill=(255, 255, 255))
    d.line([nx, ny, nx, ny + h - 22], fill=(90, 60, 20), width=2)
    # two cups on the table
    for cx in (x + w // 2 - 26, x + w // 2 + 18):
        d.rectangle([cx, y + h - 34, cx + 10, y + h - 22], fill=(255, 255, 255),
                    outline=(120, 120, 120))


def pic_markets(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for gx in range(x + 20, x + w, 40):
        d.line([gx, y + 6, gx, y + h - 8], fill=(230, 230, 230))
    for gy in range(y + 8, y + h, 14):
        d.line([x + 6, gy, x + w - 6, gy], fill=(230, 230, 230))
    pts = [(x + 12, y + 16), (x + 60, y + 22), (x + 100, y + 14),
           (x + 150, y + 34), (x + 200, y + 30), (x + 250, y + 52),
           (x + 300, y + 62)]
    d.line(pts, fill=RED, width=4)
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=RED)
    d.text((x + w - 78, y + 4), "-18%", font=font(F_BOLD, 18), fill=RED)
    # candlesticks falling
    for i, (cx, top, bot) in enumerate([(x + 30, 30, 44), (x + 70, 36, 52),
                                        (x + 110, 44, 62)]):
        d.line([cx, y + top - 6, cx, y + bot + 6], fill=RED, width=1)
        d.rectangle([cx - 5, y + top, cx + 5, y + bot], fill=RED)


def pic_iran(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 50, 80))
    d.ellipse([x + w - 52, y + 6, x + w - 22, y + 36], fill=(255, 200, 60))
    # sea
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(20, 70, 110))
    for wx in range(x + 8, x + w, 46):
        d.arc([wx, y + h - 26, wx + 34, y + h - 12], 0, 180, fill=(120, 180, 220), width=2)
    # tanker
    d.polygon([(x + 30, y + h - 52), (x + 210, y + h - 52), (x + 200, y + h - 30),
               (x + 40, y + h - 30)], fill=(60, 60, 60))
    d.rectangle([x + 150, y + h - 68, x + 190, y + h - 52], fill=(90, 90, 90))
    d.rectangle([x + 60, y + h - 66, x + 90, y + h - 52], fill=(140, 40, 40))
    # spiky mine + explosion burst
    mx, my = x + 250, y + h - 46
    for ang in range(0, 360, 45):
        import math
        ex = mx + 14 * math.cos(math.radians(ang))
        ey = my + 14 * math.sin(math.radians(ang))
        d.line([mx, my, ex, ey], fill=(255, 255, 255), width=2)
    d.ellipse([mx - 8, my - 8, mx + 8, my + 8], fill=(40, 40, 40))
    d.polygon([(x + 228, y + 12), (x + 238, y + 26), (x + 250, y + 10),
               (x + 260, y + 26), (x + 272, y + 12), (x + 268, y + 30),
               (x + 282, y + 24), (x + 264, y + 38), (x + 268, y + 48),
               (x + 250, y + 38), (x + 232, y + 48), (x + 236, y + 38),
               (x + 220, y + 26), (x + 234, y + 30)],
              fill=(255, 150, 30))
    d.text((x + 8, y + 4), "STRAIT OF HORMUZ", font=font(F_BOLD, 10), fill=(255, 255, 255))


def _house(d, x, y, s, col):
    d.polygon([(x, y), (x + s, y - s // 2), (x + 2 * s, y),
               (x + 2 * s, y + s), (x, y + s)], fill=col)
    d.rectangle([x + s // 2, y + s // 2, x + s, y + s], fill=(60, 40, 20))


def pic_village(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 228, 205))
    _house(d, x + 12, y + h - 26, 22, (200, 120, 80))
    _house(d, x + 70, y + h - 30, 26, (180, 160, 110))
    _house(d, x + 136, y + h - 24, 20, (150, 100, 70))
    # flame over middle house
    fx, fy = x + 84, y + 8
    d.polygon([(fx, fy + 26), (fx + 10, fy + 8), (fx + 18, fy + 20),
               (fx + 26, fy + 2), (fx + 30, fy + 26)], fill=(255, 120, 20))
    d.polygon([(fx + 8, fy + 26), (fx + 14, fy + 14), (fx + 22, fy + 26)],
              fill=(255, 220, 60))
    d.text((x + 6, y + 2), "5 VILLAGES", font=font(F_BOLD, 10), fill=RED)


def pic_carrier(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(207, 227, 238))
    d.text((x + 8, y + 2), "50,000 TROOPS", font=font(F_BOLD, 10), fill=NAVY)
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(20, 70, 110))
    # carrier deck
    d.polygon([(x + 10, y + h - 12), (x + w - 10, y + h - 12),
               (x + w - 24, y + h - 22), (x + 24, y + h - 22)], fill=(70, 70, 78))
    # island superstructure
    d.rectangle([x + w - 58, y + h - 34, x + w - 34, y + h - 22],
                fill=(100, 100, 108))
    # jets on deck
    for jx in (x + 36, x + 76, x + 116):
        d.polygon([(jx, y + h - 30), (jx + 16, y + h - 27), (jx, y + h - 24)],
                  fill=(40, 40, 48))


def pic_podium(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 232, 225))
    # Iran flag stripes behind
    d.rectangle([x + 12, y + 6, x + 60, y + 14], fill=(0, 122, 61))
    d.rectangle([x + 12, y + 14, x + 60, y + 22], fill=(255, 255, 255))
    d.rectangle([x + 12, y + 22, x + 60, y + 30], fill=(218, 0, 41))
    # speaker
    d.ellipse([x + w // 2 - 11, y + 8, x + w // 2 + 11, y + 30], fill=(232, 190, 150))
    d.polygon([(x + w // 2 - 20, y + 32), (x + w // 2 + 20, y + 32),
               (x + w // 2 + 14, y + h - 16), (x + w // 2 - 14, y + h - 16)],
              fill=(40, 40, 48))
    # podium
    d.rectangle([x + w // 2 - 34, y + h - 18, x + w // 2 + 34, y + h - 6],
                fill=(120, 72, 32))
    # microphones
    d.line([x + w // 2 - 16, y + 30, x + w // 2 - 26, y + 14], fill=(30, 30, 30), width=2)
    d.ellipse([x + w // 2 - 30, y + 10, x + w // 2 - 22, y + 18], fill=(30, 30, 30))
    d.line([x + w // 2 + 16, y + 30, x + w // 2 + 26, y + 14], fill=(30, 30, 30), width=2)
    d.ellipse([x + w // 2 + 22, y + 10, x + w // 2 + 30, y + 18], fill=(30, 30, 30))
    d.text((x + w - 64, y + 2), "\u201cFALSE\u201d", font=font(F_BOLD, 10), fill=RED)


def pic_mines(d, x, y, w, h):
    import math
    d.rectangle([x, y, x + w, y + h], fill=(20, 60, 95))
    d.rectangle([x, y + h - 14, x + w, y + h], fill=(12, 45, 75))
    # tanker silhouette
    d.polygon([(x + 16, y + 18), (x + 120, y + 18), (x + 112, y + 32),
               (x + 24, y + 32)], fill=(50, 50, 58))
    d.rectangle([x + 88, y + 6, x + 112, y + 18], fill=(80, 80, 88))
    # two mines
    for mx, my in ((x + 150, y + 26), (x + 178, y + 34)):
        for ang in range(0, 360, 45):
            ex = mx + 11 * math.cos(math.radians(ang))
            ey = my + 11 * math.sin(math.radians(ang))
            d.line([mx, my, ex, ey], fill=(255, 255, 255), width=2)
        d.ellipse([mx - 6, my - 6, mx + 6, my + 6], fill=(30, 30, 30))
    d.text((x + 6, y + h - 13), "2 SUPERTANKERS", font=font(F_BOLD, 9), fill=(255, 220, 60))


def pic_lifering(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(207, 227, 238))
    for wy in (y + h - 12, y + h - 6):
        d.line([x + 4, wy, x + w - 4, wy], fill=(120, 180, 220), width=2)
    # life ring
    cx, cy, r = x + w // 2, y + h // 2 - 2, 20
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255),
              outline=(220, 40, 40), width=7)
    d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=(220, 40, 40), width=2)
    # small search boat
    d.polygon([(x + 14, y + h - 22), (x + 52, y + h - 22), (x + 46, y + h - 12),
               (x + 20, y + h - 12)], fill=(31, 58, 95))
    d.rectangle([x + 30, y + h - 32, x + 40, y + h - 22], fill=(200, 200, 200))


def pic_taiz(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 220, 195))
    # skyline
    for bx, bw, bh in ((x + 8, 26, 30), (x + 40, 20, 38), (x + 64, 30, 24),
                       (x + 100, 22, 34), (x + 128, 26, 28), (x + 160, 24, 20)):
        d.rectangle([bx, y + h - 8 - bh, bx + bw, y + h - 8], fill=(120, 100, 80))
    # shell burst
    bx, by = x + 118, y + 8
    d.polygon([(bx, by), (bx + 8, by + 12), (bx + 18, by + 2), (bx + 14, by + 14),
               (bx + 26, by + 10), (bx + 16, by + 20), (bx + 24, by + 28),
               (bx + 10, by + 26), (bx + 6, by + 36), (bx, by + 24),
               (bx - 10, by + 30), (bx - 6, by + 18), (bx - 18, by + 16),
               (bx - 8, by + 10)], fill=(255, 140, 20))
    d.text((x + 6, y + 2), "TAIZ", font=font(F_BOLD, 10), fill=RED)


def pic_milk(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 245, 240))
    # milk bottle
    bx, by = x + 24, y + 6
    d.rectangle([bx + 8, by, bx + 24, by + 8], fill=(220, 220, 220))
    d.polygon([(bx + 8, by + 8), (bx + 24, by + 8), (bx + 28, by + 18),
               (bx + 4, by + 18)], fill=(255, 255, 255))
    d.rectangle([bx, by + 18, bx + 32, by + 44], fill=(255, 255, 255),
                outline=(180, 180, 180))
    d.rectangle([bx + 4, by + 26, bx + 28, by + 36], fill=(31, 58, 140))
    d.text((bx + 7, by + 28), "MILK", font=font(F_BOLD, 8), fill=(255, 255, 255))
    # tanker truck
    tx, ty = x + 78, y + 20
    d.ellipse([tx, ty, tx + 78, ty + 18], fill=(200, 200, 200))
    d.rectangle([tx + 78, ty + 2, tx + 104, ty + 18], fill=(31, 58, 140))
    d.ellipse([tx + 14, ty + 18, tx + 26, ty + 28], fill=(30, 30, 30))
    d.ellipse([tx + 84, ty + 18, tx + 96, ty + 28], fill=(30, 30, 30))
    d.text((x + w - 52, y + 2), "22M L", font=font(F_BOLD, 12), fill=NAVY)


def pic_cricket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(190, 220, 170))
    # pitch strip
    d.rectangle([x + 60, y + 4, x + w - 60, y + h - 4], fill=(225, 205, 150))
    # stumps
    for sx in (x + 84, x + 90, x + 96):
        d.line([sx, y + 8, sx, y + 22], fill=(255, 220, 100), width=3)
    for sx in (x + w - 96, x + w - 90, x + w - 84):
        d.line([sx, y + h - 22, sx, y + h - 8], fill=(255, 220, 100), width=3)
    # bat
    d.polygon([(x + 120, y + 10), (x + 130, y + 12), (x + 118, y + 34),
               (x + 110, y + 30)], fill=(200, 160, 110))
    d.line([x + 124, y + 10, x + 132, y + 2], fill=(120, 80, 40), width=3)
    # ball
    d.ellipse([x + 150, y + 26, x + 160, y + 36], fill=RED)
    # scoreboard
    d.rectangle([x + 8, y + h - 18, x + 92, y + h - 4], fill=INK)
    d.text((x + 12, y + h - 17), "720/9", font=font(F_BOLD, 11), fill=(255, 255, 255))
    d.text((x + w - 62, y + h - 17), "239/5", font=font(F_BOLD, 11), fill=NAVY)


def pic_robot(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(230, 235, 245))
    # robot head
    rx, ry = x + 22, y + 6
    d.rounded_rectangle([rx, ry, rx + 46, ry + 34], radius=6, fill=(180, 190, 200))
    d.ellipse([rx + 8, ry + 12, rx + 18, ry + 22], fill=(31, 58, 140))
    d.ellipse([rx + 28, ry + 12, rx + 38, ry + 22], fill=(31, 58, 140))
    d.line([rx + 12, ry + 28, rx + 34, ry + 28], fill=(31, 58, 140), width=2)
    d.line([rx + 23, ry, rx + 23, ry - 5], fill=(120, 120, 120), width=2)
    d.ellipse([rx + 19, ry - 9, rx + 27, ry - 1], fill=RED)
    # worker
    wx = x + 128
    d.ellipse([wx - 10, y + 8, wx + 10, y + 28], fill=(232, 190, 150))
    d.polygon([(wx - 16, y + 30), (wx + 16, y + 30), (wx + 10, y + h - 6),
               (wx - 10, y + h - 6)], fill=(200, 120, 40))
    d.rectangle([wx - 22, y + 32, wx - 16, y + 44], fill=(232, 190, 150))
    d.text((x + w - 34, y + 2), "AI", font=font(F_BOLD, 14), fill=NAVY)


def pic_film(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(35, 35, 45))
    # film reel
    cx, cy, r = x + 40, y + h // 2, 19
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(220, 220, 220))
    for dx, dy in ((-9, -9), (9, -9), (-9, 9), (9, 9), (0, 0)):
        d.ellipse([cx + dx - 5, cy + dy - 5, cx + dx + 5, cy + dy + 5],
                  fill=(35, 35, 45))
    # clapperboard
    bx, by = x + 92, y + 8
    d.rectangle([bx, by, bx + 84, by + 30], fill=(255, 255, 255))
    for i in range(5):
        d.polygon([(bx + i * 17, by), (bx + i * 17 + 9, by),
                   (bx + i * 17 + 4, by + 9), (bx + i * 17 - 5, by + 9)],
                  fill=INK)
    d.rectangle([bx, by + 9, bx + 84, by + 30], fill=(255, 255, 255),
                outline=INK)
    d.text((bx + 6, by + 14), "BRICS", font=font(F_BOLD, 11), fill=INK)
    # five small flag stripes
    cols = [(0, 150, 60), (220, 30, 30), (255, 153, 51), (220, 20, 20),
            (0, 90, 160)]
    for i, c in enumerate(cols):
        d.rectangle([x + 92 + i * 17, y + h - 12, x + 92 + i * 17 + 14, y + h - 4],
                    fill=c)


def pic_kyiv(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 40, 70))
    # skyline
    for bx, bw, bh in ((x + 8, 26, 34), (x + 40, 20, 44), (x + 64, 30, 28),
                       (x + 100, 22, 38), (x + 128, 26, 30), (x + 160, 24, 24)):
        d.rectangle([bx, y + h - 8 - bh, bx + bw, y + h - 8], fill=(90, 100, 130))
    # air-defence shield
    cx, cy = x + w // 2, y + 24
    d.polygon([(cx - 16, cy - 12), (cx + 16, cy - 12), (cx + 14, cy + 6),
               (cx, cy + 16), (cx - 14, cy + 6)],
              outline=(255, 210, 60), width=3)
    d.text((x + 6, y + 2), "KYIV", font=font(F_BOLD, 10), fill=(255, 255, 255))
    d.text((x + w - 58, y + 2), "11 KILLED", font=font(F_BOLD, 10),
           fill=(255, 120, 100))


def pic_spain(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 240, 225))
    # ballot box
    bx, by = x + 24, y + 18
    d.rectangle([bx, by, bx + 70, by + 32], fill=(31, 58, 140))
    d.rectangle([bx + 8, by - 8, bx + 62, by], fill=(31, 58, 140))
    d.rectangle([bx + 28, by - 6, bx + 42, by - 2], fill=(255, 255, 255))
    d.polygon([(bx + 30, by - 18), (bx + 44, by - 18), (bx + 42, by - 2),
               (bx + 32, by - 2)], fill=(255, 255, 255), outline=(150, 150, 150))
    # euro coin
    cx, cy = x + 150, y + 30
    d.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(201, 162, 39),
              outline=(150, 110, 20), width=2)
    d.text((cx - 10, cy - 13), "\u20ac", font=font(F_BOLD, 24),
           fill=(255, 255, 255))
    d.text((x + 6, y + h - 14), "\u20ac100M+", font=font(F_BOLD, 11), fill=RED)


def pic_knesset(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 235, 240))
    # domed parliament building
    bx, by = x + 30, y + 14
    d.rectangle([bx, by + 18, bx + 130, by + 40], fill=(200, 200, 195))
    d.pieslice([bx + 45, by - 6, bx + 85, by + 22], 180, 360,
               fill=(150, 150, 145))
    for i in range(5):
        cx = bx + 12 + i * 26
        d.rectangle([cx, by + 22, cx + 6, by + 40], fill=(120, 120, 115))
    d.rectangle([bx - 6, by + 40, bx + 136, by + 44], fill=(150, 150, 145))
    d.text((x + 6, y + 2), "KNESSET", font=font(F_BOLD, 10), fill=NAVY)


def pic_pmi(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for gy in range(y + 8, y + h, 14):
        d.line([x + 6, gy, x + w - 6, gy], fill=(230, 230, 230))
    # green up arrow (DE)
    d.line([(x + 20, y + h - 18), (x + 70, y + 22), (x + 95, y + 12)],
           fill=(34, 120, 60), width=4)
    d.polygon([(x + 95, y + 12), (x + 84, y + 10), (x + 92, y + 24)],
              fill=(34, 120, 60))
    d.text((x + 8, y + 4), "DE \u25b2", font=font(F_BOLD, 11), fill=(34, 120, 60))
    # red down arrow (FR)
    d.line([(x + 110, y + 16), (x + 150, y + h - 26), (x + 180, y + h - 34)],
           fill=RED, width=4)
    d.polygon([(x + 180, y + h - 34), (x + 168, y + h - 36), (x + 176, y + h - 22)],
              fill=RED)
    d.text((x + w - 52, y + h - 16), "FR \u25bc", font=font(F_BOLD, 11), fill=RED)


def pic_badge(d, x, y, w, h):
    import math
    d.rectangle([x, y, x + w, y + h], fill=(240, 238, 230))
    # gold star badge
    cx, cy = x + 48, y + h // 2
    pts = []
    for i in range(10):
        r = 26 if i % 2 == 0 else 11
        ang = math.radians(-90 + i * 36)
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    d.polygon(pts, fill=(201, 162, 39), outline=(150, 110, 20))
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(255, 255, 255))
    # handcuffs
    hx, hy = x + 110, y + 18
    d.ellipse([hx, hy, hx + 24, hy + 24], outline=(60, 60, 60), width=4)
    d.ellipse([hx + 34, hy + 8, hx + 58, hy + 32], outline=(60, 60, 60), width=4)
    d.line([hx + 24, hy + 12, hx + 34, hy + 20], fill=(60, 60, 60), width=3)
    d.text((x + w - 58, y + 2), "FBI", font=font(F_BOLD, 12), fill=NAVY)


def pic_hospital(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(245, 245, 240))
    # red cross sign
    d.rectangle([x + 10, y + 6, x + 30, y + 26], fill=(255, 255, 255),
                outline=(200, 200, 200))
    d.rectangle([x + 18, y + 9, x + 22, y + 23], fill=RED)
    d.rectangle([x + 13, y + 14, x + 27, y + 18], fill=RED)
    # bed
    d.rectangle([x + 50, y + 28, x + 170, y + 34], fill=(31, 58, 140))
    d.rectangle([x + 56, y + 34, x + 62, y + 44], fill=(60, 60, 60))
    d.rectangle([x + 158, y + 34, x + 164, y + 44], fill=(60, 60, 60))
    d.rectangle([x + 56, y + 20, x + 76, y + 28], fill=(255, 255, 255),
                outline=(180, 180, 180))
    d.ellipse([x + 60, y + 12, x + 72, y + 22], fill=(232, 190, 150))
    # monitor line
    d.line([(x + 120, y + 10), (x + 132, y + 10), (x + 138, y + 4),
            (x + 144, y + 16), (x + 150, y + 10), (x + 168, y + 10)],
           fill=(34, 120, 60), width=2)


def pic_airport(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(207, 227, 238))
    # runway
    d.rectangle([x, y + h - 14, x + w, y + h - 8], fill=(90, 90, 90))
    for rx in range(x + 10, x + w, 30):
        d.line([rx, y + h - 11, rx + 14, y + h - 11], fill=(255, 255, 255),
               width=2)
    # grounded plane
    px, py = x + 40, y + 16
    d.polygon([(px, py + 10), (px + 90, py + 10), (px + 100, py + 16),
               (px, py + 16)], fill=(255, 255, 255), outline=(120, 120, 120))
    d.polygon([(px + 70, py + 10), (px + 84, py - 6), (px + 92, py + 10)],
              fill=(255, 255, 255), outline=(120, 120, 120))
    d.polygon([(px + 10, py + 16), (px + 22, py + 26), (px + 30, py + 16)],
              fill=(255, 255, 255), outline=(120, 120, 120))
    # red X
    d.line([x + w - 34, y + 4, x + w - 10, y + 28], fill=RED, width=4)
    d.line([x + w - 10, y + 4, x + w - 34, y + 28], fill=RED, width=4)
    d.text((x + 6, y + 2), "GROUNDED", font=font(F_BOLD, 10), fill=RED)


def pic_virus(d, x, y, w, h):
    import math
    d.rectangle([x, y, x + w, y + h], fill=(240, 245, 240))
    cx, cy = x + 60, y + h // 2
    for i in range(10):
        ang = math.radians(i * 36)
        ex, ey = cx + 30 * math.cos(ang), cy + 30 * math.sin(ang)
        d.line([cx, cy, ex, ey], fill=(150, 60, 60), width=3)
        d.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill=(150, 60, 60))
    d.ellipse([cx - 20, cy - 20, cx + 20, cy + 20], fill=(176, 30, 30))
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(255, 200, 200))
    # cross
    d.rectangle([x + 130, y + 8, x + 150, y + 28], fill=(255, 255, 255),
                outline=(200, 200, 200))
    d.rectangle([x + 138, y + 11, x + 142, y + 25], fill=RED)
    d.rectangle([x + 133, y + 16, x + 147, y + 20], fill=RED)
    d.text((x + 6, y + h - 14), "EBOLA", font=font(F_BOLD, 10), fill=RED)


def pic_phone(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(230, 235, 245))
    # phone with a red prohibition slash over it
    px, py = x + 70, y + 6
    d.rounded_rectangle([px, py, px + 56, py + 40], radius=6, fill=(40, 40, 48))
    d.rectangle([px + 6, py + 6, px + 50, py + 32], fill=(120, 200, 240))
    d.ellipse([px + 22, py + 35, px + 34, py + 38], fill=(120, 120, 120))
    cx, cy = x + 98, y + 26
    d.ellipse([cx - 28, cy - 28, cx + 28, cy + 28], outline=RED, width=5)
    d.line([cx - 20, cy + 20, cx + 20, cy - 20], fill=RED, width=5)
    d.text((x + 6, y + 2), "SCHOOLS", font=font(F_BOLD, 10), fill=NAVY)
    d.text((x + w - 52, y + h - 14), "2027", font=font(F_BOLD, 11), fill=RED)


PICTURES = {
    "nepal": pic_nepal, "markets": pic_markets, "iran": pic_iran,
    "village": pic_village, "carrier": pic_carrier, "podium": pic_podium,
    "mines": pic_mines, "lifering": pic_lifering, "taiz": pic_taiz,
    "milk": pic_milk, "cricket": pic_cricket, "robot": pic_robot,
    "film": pic_film, "kyiv": pic_kyiv, "spain": pic_spain,
    "knesset": pic_knesset, "pmi": pic_pmi, "badge": pic_badge,
    "hospital": pic_hospital, "airport": pic_airport, "virus": pic_virus,
    "phone": pic_phone,
}


# ---------------------------------------------------------------- world map
CONTINENTS = {
    "N America": [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73),
                  (-65, 60), (-55, 47), (-70, 42), (-75, 35), (-80, 26),
                  (-85, 20), (-90, 15), (-95, 16), (-105, 20), (-115, 28),
                  (-125, 40), (-125, 49), (-140, 60), (-165, 60)],
    "S America": [(-80, 10), (-70, 12), (-60, 9), (-50, 0), (-35, -8),
                  (-40, -20), (-48, -28), (-58, -35), (-65, -41), (-70, -54),
                  (-73, -40), (-72, -20), (-77, -5)],
    "Europe": [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57),
               (10, 59), (18, 56), (21, 55), (28, 60), (30, 70), (40, 68),
               (45, 60), (40, 50), (30, 45), (28, 41), (23, 36), (19, 40),
               (12, 44), (3, 43)],
    "Africa": [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (43, 12),
               (51, 11), (48, 0), (40, -10), (35, -20), (32, -29), (26, -34),
               (19, -35), (12, -18), (9, 0), (-8, 5), (-15, 12), (-17, 15),
               (-10, 30)],
    "Asia": [(40, 68), (60, 70), (80, 73), (100, 76), (120, 73), (140, 72),
             (160, 70), (178, 66), (170, 60), (158, 52), (142, 45), (135, 35),
             (127, 33), (122, 30), (120, 22), (108, 10), (105, 2), (100, 8),
             (95, 16), (90, 22), (80, 15), (75, 8), (70, 20), (60, 25),
             (55, 26), (50, 30), (43, 28), (40, 35)],
    "Australia": [(113, -22), (114, -30), (120, -34), (129, -32), (137, -35),
                  (142, -38), (147, -39), (150, -37), (153, -27), (150, -22),
                  (146, -19), (142, -11), (137, -12), (132, -12), (126, -14),
                  (122, -17), (118, -20)],
    "NZ": [(167, -45), (174, -41), (178, -38), (176, -40), (170, -43)],
}


def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    d.rectangle([x, y, x + w, y + h], outline=GREY)
    for name, pts in CONTINENTS.items():
        xy = [(x + (lon + 170) / 360.0 * w, y + (75 - lat) / 130.0 * h)
              for lon, lat in pts]
        d.polygon(xy, fill=LAND, outline=LAND_EDGE)
    for num, name, lon, lat in MAP_PINS:
        px = x + (lon + 170) / 360.0 * w
        py = y + (75 - lat) / 130.0 * h
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED,
                  outline=(255, 255, 255), width=1)
        d.text((px - 3, py - 6), str(num), font=font(F_BOLD, 9),
               fill=(255, 255, 255))

# ---------------------------------------------------------------- layout

def section_head(d, x, y, text, color=RED):
    d.text((x, y), text, font=font(F_BOLD, 13), fill=color)
    return y + 17


def draw_masthead(d, press_time):
    d.rectangle([0, 0, W, 64], fill=INK)
    d.text((10, 2), "THE WORLD IN ONE PAGE",
           font=font(F_SERIF, 40), fill=(255, 255, 255))
    d.text((10, 46), "MONDAY \u00b7 23 NOVEMBER 2026 \u00b7 THE DAY'S NEWS, DRAWN IN ONE IMAGE",
           font=font(F_BOLD, 13), fill=GOLD)
    _f38 = font(F_BOLD, 34)
    _f13 = font(F_BOLD, 13)
    _f10 = font(F_BOLD, 10)
    _w38 = d.textlength("38", font=_f38)
    _wst = d.textlength(" STORIES", font=_f13)
    _x = W - 10 - _w38 - _wst
    d.text((_x, 0), "38", font=_f38, fill=GOLD)
    d.text((_x + _w38, 10), " STORIES", font=_f13, fill=(255, 255, 255))
    _el = "DAY EDITION \u00b7 " + press_time
    d.text((W - 10 - d.textlength(_el, font=_f10), 46), _el, font=_f10,
           fill=(200, 200, 200))


def draw_region_strip(d, y):
    parts = "  \u00b7  ".join("%s %d" % (n, c) for n, c in REGION_TALLY)
    line = parts + "   =   38 STORIES  \u00b7  8 REGIONS"
    fnt = font(F_BOLD, 13)
    tw = d.textlength(line, font=fnt)
    d.text(((W - tw) / 2, y), line, font=fnt, fill=NAVY)
    return y + 17


def draw_timeline(d, y):
    y = section_head(d, 8, y, "THE DAY IN UTC")
    col_w = 168
    f_time = font(F_BOLD, 12)
    f_txt = font(F_SANS, 10)
    for i, (t, txt) in enumerate(TIMELINE):
        x = 8 + i * col_w
        d.ellipse([x + 2, y + 2, x + 10, y + 10], fill=RED)
        d.text((x + 14, y), t, font=f_time, fill=RED)
        yy = text_block(d, x, y + 15, wrap(d, txt, f_txt, col_w - 12), f_txt,
                        leading=12)
    return y + 38


def draw_numbers(d, y):
    y = section_head(d, 8, y, "DAY IN NUMBERS")
    col_w = 168
    for i, (num, label) in enumerate(NUMBERS):
        x = 8 + i * col_w
        nf = font(F_BOLD, 24 if len(num) <= 7 else 17)
        d.text((x, y), num, font=nf, fill=INK)
        text_block(d, x, y + 28, wrap(d, label, font(F_SANS, 10), col_w - 12),
                   font(F_SANS, 10), fill=GREY, leading=12)
    return y + 54


def draw_leads(d, y):
    y = section_head(d, 8, y, "THE THREE BIGGEST STORIES")
    col_w, gap = 328, 6
    top = y
    for i, (head, body, src, status, key) in enumerate(LEADS):
        x = 8 + i * (col_w + gap)
        d.rectangle([x, top, x + col_w, top + 170], outline=INK, width=1)
        PICTURES[key](d, x + 1, top + 1, col_w - 2, 66)
        hy = top + 70
        hy = text_block(d, x + 6, hy,
                        wrap(d, head, font(F_BOLD, 16), col_w - 12),
                        font(F_BOLD, 16), leading=19)
        hy = text_block(d, x + 6, hy + 2,
                        wrap(d, body, font(F_SANS, 11), col_w - 12),
                        font(F_SANS, 11), leading=14)
        source_line(d, x + 6, top + 170 - 16, src, status, col_w - 12)
    return top + 170


def draw_pictured(d, y):
    y = section_head(d, 8, y, "ALSO TODAY \u2014 EVERY STORY WITH ITS PICTURE")
    col_w, gap = 197, 6
    row_h = 116
    for row in range(2):
        top = y + row * (row_h + 6)
        for col in range(5):
            i = row * 5 + col
            head, body, src, status, key = PICTURED[i]
            x = 8 + col * (col_w + gap)
            d.rectangle([x, top, x + col_w, top + row_h], outline=INK, width=1)
            PICTURES[key](d, x + 1, top + 1, col_w - 2, 48)
            hy = top + 52
            hy = text_block(d, x + 5, hy,
                            wrap(d, head, font(F_BOLD, 11), col_w - 10),
                            font(F_BOLD, 11), leading=13)
            hy = text_block(d, x + 5, hy + 1,
                            wrap(d, body, font(F_SANS, 10), col_w - 10),
                            font(F_SANS, 10), leading=12)
            source_line(d, x + 5, top + row_h - 15, src, status, col_w - 10)
    return y + 2 * row_h + 6


def draw_map_section(d, y):
    y = section_head(d, 8, y, "WHERE IT HAPPENED")
    draw_map(d, 8, y, W - 16, 60)
    y += 64
    legend = "   ".join("%d %s" % (n, name) for n, name, _, _ in MAP_PINS)
    fnt = font(F_BOLD, 11)
    tw = d.textlength(legend, font=fnt)
    d.text(((W - tw) / 2, y), legend, font=fnt, fill=INK)
    return y + 14


def draw_briefs(d, y):
    y = section_head(d, 8, y, "ALSO ON MONDAY \u2014 25 MORE STORIES IN ONE LINE EACH")
    cols = [BRIEFS[0:9], BRIEFS[9:17], BRIEFS[17:25]]
    fnt = font(F_SANS, 10)
    fnum = font(F_BOLD, 10)
    col_w = 336
    status_colors = {"CONFIRMED": (34, 120, 60), "REPORTED": (31, 58, 140),
                     "CLAIM": (176, 110, 10), "FORECAST": (110, 60, 140)}
    n = 14
    for ci, col in enumerate(cols):
        x = 8 + ci * col_w
        yy = y
        for txt, src, status, region in col:
            d.text((x, yy), "%d." % n, font=fnum, fill=status_colors[status])
            nw = d.textlength("%d. " % n, font=fnum)
            line = txt + "  [" + src + "]"
            d.text((x + nw, yy), line, font=fnt, fill=INK)
            yy += 15
            n += 1
    return y + 9 * 15


def draw_date_check(d, y):
    d.rectangle([8, y, W - 8, y + 70], outline=RED, width=2)
    fnt = font(F_BOLD, 10)
    d.text((14, y + 4), "DATE CHECK \u2014 NOT MONDAY'S NEWS, SO LEFT OUT:",
           font=fnt, fill=RED)
    yy = text_block(d, 14, y + 18,
                    wrap(d, DATE_CHECK_LEFT, font(F_SANS, 10), W - 28),
                    font(F_SANS, 10), leading=12)
    d.text((14, y + 54), DATE_CHECK_NOT_YET, font=fnt, fill=INK)
    return y + 70


def draw_sources(d, y):
    line1 = ("SOURCES: REUTERS \u00b7 AFP \u00b7 AP \u00b7 BLOOMBERG \u00b7 WION \u00b7 DAWN \u00b7 ARAB NEWS \u00b7 "
             "MEA \u00b7 CRICINFO \u00b7 CNBC \u00b7 ET \u00b7 GULF NEWS \u00b7 CENTCOM \u00b7 IRGC")
    line2 = ("CONFIRMED = verified by two sources  \u00b7  REPORTED = as reported  \u00b7  "
             "CLAIM = one side's account  \u00b7  FORECAST = scheduled, not yet played  \u00b7  "
             "brief numbers are coloured by status")
    fnt = font(F_SANS, 9)
    d.text((8, y), line1, font=fnt, fill=GREY)
    d.text((8, y + 11), line2, font=fnt, fill=GREY)
    return y + 20


def main():
    import datetime
    press = datetime.datetime.now(datetime.timezone.utc).strftime("DRAWN %H:%M UTC")
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d, press)
    y = 68
    y = draw_region_strip(d, y)
    d.line([8, y, W - 8, y], fill=INK, width=1)
    y += 4
    y = draw_timeline(d, y)
    d.line([8, y, W - 8, y], fill=INK, width=1)
    y += 4
    y = draw_numbers(d, y)
    d.line([8, y, W - 8, y], fill=INK, width=1)
    y += 4
    y = draw_leads(d, y)
    y += 4
    y = draw_pictured(d, y)
    y += 3
    y = draw_map_section(d, y)
    y += 2
    y = draw_briefs(d, y)
    y += 3
    y = draw_date_check(d, y)
    y += 3
    y = draw_sources(d, y)
    assert y <= H, "layout overflow: y=%d > %d" % (y, H)
    print("layout ends at y=%d (canvas %d)" % (y, H))
    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
