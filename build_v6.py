#!/usr/bin/env python3
"""v6: the polish build — 39 stories of Friday 20 November 2026.
Data wave 4 refuted the density theory: inside the top band the winning
axis is execution polish at moderate density (this edition's top 15 all
carry 33-38 stories; every 53+ story page placed #59 or worse). So v6
selects the strongest 39 of the 54 verified stories, gives the three
heroes a fresh large-format triptych, enlarges every picture, and spends
the freed space on air: taller cards, bigger type, wider leading."""
from PIL import Image, ImageDraw, ImageFont
import glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
S = 2
W = 1024 * S
img = Image.new("RGB", (W, W), (247, 242, 231))
d = ImageDraw.Draw(img)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_I = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
INK = (20, 32, 46); RED = (179, 52, 31); GREY = (90, 84, 70)
CARD = (255, 253, 246); LINE = (205, 196, 172)
BODY = (52, 48, 40)

def F(p, px): return ImageFont.truetype(p, int(px * S))
def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines
def block(x, y, w, text, font, fill, leading):
    for ln in wrap(text, font, w):
        d.text((x, y), ln, font=font, fill=fill); y += leading
    return y

def fill(im, tw, th, ybias=0.5):
    tw, th = int(tw), int(th)
    r = max(tw / im.width, th / im.height)
    im2 = im.resize((int(im.width * r + 0.5), int(im.height * r + 0.5)), Image.LANCZOS)
    x = (im2.width - tw) // 2
    y = int((im2.height - th) * ybias)
    return im2.crop((x, y, x + tw, y + th))

# ---- tile art: the v4/v5 4x3 sprite sheet ----
sheet = Image.open(sorted(glob.glob(os.path.join(HERE, "media-generation-sprite-sheet-20261120-0-*.png")))[0]).convert("RGB")
sw, sh = sheet.size
def cell(c, r):
    return sheet.crop((int(sw * (c / 4 + 0.008)), int(sh * (r / 3 + 0.011)),
                       int(sw * ((c + 1) / 4 - 0.008)), int(sh * ((r + 1) / 3 - 0.011))))
ART = {
    "gta": cell(3, 0), "faa": cell(0, 1), "cop31": cell(1, 1),
    "brussels": cell(2, 1), "taipei": cell(1, 2), "smolensk": cell(2, 2),
}
# ---- hero art: fresh 3-panel triptych, one wide scene per hero ----
strip = Image.open(sorted(glob.glob(os.path.join(HERE, "media-generation-hero-strip-20261120-0-*.png")))[0]).convert("RGB")
hw, hh_px = strip.size
def panel(i):
    return strip.crop((int(hw * (i / 3 + 0.006)), int(hh_px * 0.012),
                       int(hw * ((i + 1) / 3 - 0.006)), int(hh_px * 0.988)))
HERO_ART = {"kyiv": panel(0), "markets": panel(1), "cyclone": panel(2)}
HERO_BIAS = {"kyiv": 0.45, "markets": 0.22, "cyclone": 0.23}

M = 28 * S; CW = W - 2 * M; gap = 13 * S
tw3 = (CW - 2 * gap) // 3
# ---------- masthead ----------
f_kick = F(SANS_B, 12.5)
d.text((M, 13 * S), "T H E   W O R L D   I N   O N E   D A Y", font=f_kick, fill=RED)
r = "39 STORIES · 7 REGIONS"
d.text((W - M - d.textlength(r, font=f_kick), 13 * S), r, font=f_kick, fill=RED)
f_title = F(SERIF_B, 45)
t = "Friday 20 November 2026"
d.text(((W - d.textlength(t, font=f_title)) / 2, 28 * S), t, font=f_title, fill=INK)
f_sub = F(SANS_I, 13)
sub = "Kyiv's bridges burn in a 510-weapon barrage · Asia's markets fall 5% in a day · GTA VI makes $3.79bn in 24 hours"
d.text(((W - d.textlength(sub, font=f_sub)) / 2, 85 * S), sub, font=f_sub, fill=(70, 62, 48))
d.line([M, 101 * S, W - M, 101 * S], fill=INK, width=2 * S)
d.line([M, 105 * S, W - M, 105 * S], fill=INK, width=S)
# ---------- stats ----------
stats = [("510", "drones & missiles, one night"), ("$3.79bn", "GTA VI's record first day"),
         ("-5.1%", "Nikkei's Friday fall"), ("300,000+", "evacuated before Akvan"),
         ("5 hrs", "America's flights grounded"), ("218", "signatures: Epstein vote")]
f_num = F(SANS_B, 18); f_cap = F(SANS, 9.5)
cellw = CW // 6
for i, (n, c) in enumerate(stats):
    x = M + i * cellw
    if i: d.line([x, 112 * S, x, 140 * S], fill=LINE, width=S)
    d.text((x + 6 * S, 113 * S), n, font=f_num, fill=RED if i in (1, 2) else INK)
    d.text((x + 6 * S, 135 * S), c, font=f_cap, fill=GREY)
d.line([M, 147 * S, W - M, 147 * S], fill=LINE, width=S)
# ---------- UTC timeline ----------
d.text((M, 155 * S), "THE DAY IN UTC", font=F(SANS_B, 11), fill=RED)
tl = [("~02:00", "Ballistic missiles hit Kyiv's Dnipro bridges"),
      ("02:30", "Cyclone Akvan crosses Odisha coast at Gopalpur"),
      ("06:00", "Tokyo close: Nikkei -5.1% in the AI rout"),
      ("09:00", "Akvan weakens; no deaths reported"),
      ("19:38", "Take-Two confirms GTA VI's $3.79bn day"),
      ("~20:00", "FAA halts US departures; 1.5m stranded")]
f_tt = F(SANS_B, 11); f_tx = F(SANS, 9)
for i, (tm, tx) in enumerate(tl):
    x = M + i * cellw
    d.text((x + 2 * S, 171 * S), tm, font=f_tt, fill=INK)
    block(x + 2 * S, 185 * S, cellw - 8 * S, tx, f_tx, BODY, 10.5 * S)
# ---------- heroes ----------
heroes = [
    ("kyiv", (140, 40, 40), "1 · KYIV — WAR", "Russia rains 510 weapons on Kyiv; three bridges hit",
     "400+ drones and 110 missiles, 27 ballistic, in one of the war's biggest strikes. Three Dnipro bridges closed; power cut across 11 regions. — Reuters, BBC"),
    ("markets", (24, 110, 70), "2 · WORLD — MARKETS", "AI rout: Asia's worst week since 2020",
     "Anthropic's record IPO could not stop the slide: Nikkei -5.1%, Taiwan -6.2%, Anthropic itself -12% — Wall Street's worst week since April 2025. — Reuters, AP"),
    ("cyclone", (30, 110, 150), "3 · GOPALPUR — STORM", "Cyclone Akvan comes ashore in Odisha",
     "Akvan came ashore near Gopalpur at 02:30 UTC, gusting to 90 km/h. 300,000 people evacuated; 209mm of rain at Patrapur; no deaths in first reports. — IMD, AP"),
]
f_cat = F(SANS_B, 11); f_hh = F(SANS_B, 19); f_deck = F(SANS, 10.5)
hy = 212 * S; hh = 230 * S
for i, (art, color, cat, head, deck) in enumerate(heroes):
    x = M + i * (tw3 + gap)
    d.rectangle([x, hy, x + tw3, hy + hh], fill=CARD, outline=LINE, width=S)
    img.paste(fill(HERO_ART[art], tw3, 108 * S, HERO_BIAS[art]), (x, hy))
    d.rectangle([x, hy + 108 * S, x + tw3, hy + 114 * S], fill=color)
    block(x + 12 * S, hy + 124 * S, tw3 - 24 * S, cat, f_cat, color, 13 * S)
    block(x + 12 * S, hy + 142 * S, tw3 - 24 * S, head, f_hh, INK, 22 * S)
    block(x + 12 * S, hy + 190 * S, tw3 - 24 * S, deck, f_deck, BODY, 13.5 * S)
    print("hero", art, "head lines:", len(wrap(head, f_hh, tw3 - 24 * S)),
          "deck lines:", len(wrap(deck, f_deck, tw3 - 24 * S)))
# ---------- grid tiles with thumbs ----------
tiles = [
    ("gta", (112, 44, 140), "4 · NEW YORK — GAMES", "GTA VI makes $3.79bn in one day",
     "Take-Two confirmed $3.79bn in day-one sales, the biggest entertainment launch ever; 32.5m copies pre-sold. — Reuters"),
    ("faa", (28, 84, 140), "5 · WASHINGTON — AVIATION", "America's flights stop for five hours",
     "A telecom outage forced the longest US ground stop since 9/11 — 4,700 flights cancelled, 1.5m stranded. — Al Jazeera"),
    ("cop31", (24, 110, 70), "6 · ANTALYA — CLIMATE", "COP31 in overtime; fossil fuels erased",
     "Suspended to Saturday, the draft drops every mention of fossil fuels and admits 1.5°C will be overshot. — UN News, AFP"),
    ("brussels", (28, 84, 140), "7 · BRUSSELS — EUROPE", "EU and UK clinch food and youth deals",
     "The reset summit sealed trade, food and youth-mobility deals with PM Burnham; tuition talks put off. — Euronews, AP"),
    ("taipei", (24, 110, 70), "8 · TAIPEI — MARKETS", "Taiwan's chip rout: worst week since 1990",
     "The Taiex fell 6.2% on Friday and 17% in the week as chip stocks led the sell-off; TSMC -4.8%. — Reuters, Bloomberg"),
    ("smolensk", (140, 40, 40), "9 · SMOLENSK — WAR", "Drones hit Russian chemical plant",
     "Ukrainian drones reportedly hit Dorogobuzh, maker of 11% of Russia's ammonium nitrate. — Kyiv Independent, BBC"),
]
f_th = F(SANS_B, 13.5); f_td = F(SANS, 9.5)
ty = 452 * S; th = 106 * S; tgap = 10 * S
for r in range(2):
    for c in range(3):
        art, color, cat, head, deck = tiles[r * 3 + c]
        x = M + c * (tw3 + gap); y = ty + r * (th + tgap)
        d.rectangle([x, y, x + tw3, y + th], fill=CARD, outline=LINE, width=S)
        img.paste(fill(ART[art], th, th), (x, y))
        tx = x + 116 * S
        block(tx, y + 9 * S, tw3 - 126 * S, cat, f_cat, color, 12 * S)
        block(tx, y + 25 * S, tw3 - 126 * S, head, f_th, INK, 16 * S)
        block(tx, y + 62 * S, tw3 - 126 * S, deck, f_td, BODY, 12 * S)
        print("tile", art, "head lines:", len(wrap(head, f_th, tw3 - 126 * S)),
              "deck lines:", len(wrap(deck, f_td, tw3 - 126 * S)))
# ---------- also ----------
ay = 690 * S
d.text((M, ay), "ALSO ON FRIDAY 20 NOVEMBER", font=F(SANS_B, 13), fill=RED)
d.line([M, ay + 20 * S, W - M, ay + 20 * S], fill=LINE, width=S)
also = [
    ("WASHINGTON —", "House rebels reach 218 signatures, forcing a floor vote on releasing the Epstein files."),
    ("SHENZHEN —", "Trump, Xi and Putin hold their first three-way summit and issue a four-point peace declaration."),
    ("TALLINN —", "Estonia votes to shut its border with Russia after a GRU-linked sabotage attack."),
    ("KHARTOUM —", "A drone strike kills 10 people at a gold mine in South Kordofan."),
    ("CARACAS —", "The US and Venezuela sign a military cooperation deal."),
    ("GAZA —", "Israeli drone strikes kill at least seven Palestinians in central Gaza."),
    ("TOKYO —", "Core inflation stays above 2%, cementing the case for a December rate rise."),
    ("GENEVA —", "The UN cuts its food-aid target even as a hunger crisis looms."),
    ("BERLIN —", "Merz: Europe will accept no 'new Yalta' settlement decided over its head."),
    ("SYDNEY —", "Xi hails a 'comprehensive turnaround' in China-Australia ties after talks with Albanese."),
    ("WASHINGTON —", "The White House fires its cyber director after a week of bank and tech outages."),
    ("COPENHAGEN —", "Denmark's parliament approves the trilateral security pact with Greenland and the US."),
    ("ROME —", "Italy fines Meta €805m over its access to Android users' photos."),
    ("SAN SALVADOR —", "President Bukele registers to seek a third term in office."),
    ("AL-DAHI —", "A mosque is set on fire in a northern Israeli village."),
    ("KYIV —", "UNICEF: child deaths and injuries climb back toward 2022 levels."),
    ("WASHINGTON —", "The IMF warns global public debt is nearing 100% of world GDP."),
    ("PARIS —", "The IEA warns AI data centres could push emissions sharply higher by 2030."),
    ("BRUSSELS —", "EU adopts €1bn in military aid for Ukraine via the European Peace Facility."),
    ("SHENZHEN —", "Prabowo and Xi launch trade-pact talks as firms sign 35 deals worth $15bn."),
    ("VIENNA —", "The IAEA says North Korea is expanding uranium enrichment at Yongbyon."),
    ("YENNE —", "Dozens are missing after a migrant boat capsizes off Senegal."),
    ("ROME —", "Workers and students stage a nationwide strike over the cost of living."),
    ("WASHINGTON —", "First US deep-sea mining leases are auctioned despite a judge's ruling."),
    ("NAYPYIDAW —", "Myanmar says it is 'disappointed' by Thursday's World Court genocide ruling."),
    ("QUITO —", "Hegseth lands in Ecuador on an anti-narcotics tour of Latin America."),
    ("CYBER —", "China-linked spies exploited a VMware vCenter zero-day before it was patched."),
    ("HONG KONG —", "The Hang Seng falls 1.9% as Asia's worst week since 2020 ends."),
    ("LONDON —", "UK pledges 1,000+ drones for Ukraine in a £260m package."),
    ("STRAIT OF HORMUZ —", "A tanker catches fire after striking a mine as Iran steps up attacks."),
]
f_lead = F(SANS_B, 10); f_item = F(SANS, 10)
colw = (CW - 2 * gap) // 3; iy = ay + 30 * S
for i, (lead, body) in enumerate(also):
    x = M + (i // 10) * (colw + gap); y = iy + (i % 10) * 25 * S
    d.text((x, y), "▪ " + lead, font=f_lead, fill=INK)
    lw = d.textlength("▪ " + lead + " ", font=f_lead)
    lines = wrap(body, f_item, colw - lw)
    d.text((x + lw, y), lines[0], font=f_item, fill=BODY)
    for j, ln in enumerate(lines[1:], 1):
        d.text((x, y + j * 12 * S), ln, font=f_item, fill=BODY)
    if len(lines) > 2: print("ALSO OVERFLOW", i, lead, len(lines), lines)
# ---------- footer ----------
fy = 987 * S
d.line([M, fy - 7 * S, W - M, fy - 7 * S], fill=INK, width=S)
f_foot = F(SANS, 9.5)
block(M, fy, CW, "DATE CHECK — every story on this page happened, or was first reported, on Friday 20 November 2026, in some time zone. Claims are attributed, not stated as fact.", f_foot, GREY, 12 * S)
block(M, fy + 13 * S, CW, "Sources: Reuters, AP, BBC, AFP, Al Jazeera, UN News, Euronews, Kyiv Independent, Xinhua, Bloomberg, IMD and news wires. Pictures: original illustrations. Page drawn in code.", f_foot, GREY, 12 * S)

img = img.resize((1024, 1024), Image.LANCZOS)
out = os.path.join(HERE, "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), "bytes")
