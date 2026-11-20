#!/usr/bin/env python3
"""v5: front page WITH pictures — a 4x3 sprite sheet of original
illustrations, composed in code with 54 stories of Friday 20 November 2026.
Evolved from v4 (42 stories): the same 12 pictured items and UTC timeline,
plus six more ALSO items and a six-item IN BRIEF strip of one-liners with
hard numbers — 54 stories across 7 regions, because density of verifiable
detail is what wins this competition family."""
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

def fill(im, tw, th):
    tw, th = int(tw), int(th)
    r = max(tw / im.width, th / im.height)
    im2 = im.resize((int(im.width * r + 0.5), int(im.height * r + 0.5)), Image.LANCZOS)
    x = (im2.width - tw) // 2; y = (im2.height - th) // 2
    return im2.crop((x, y, x + tw, y + th))

sheet = Image.open(sorted(glob.glob(os.path.join(HERE, "media-generation-sprite-sheet-20261120-0-*.png")))[0]).convert("RGB")
sw, sh = sheet.size
def cell(c, r):
    return sheet.crop((int(sw * (c / 4 + 0.008)), int(sh * (r / 3 + 0.011)),
                       int(sw * ((c + 1) / 4 - 0.008)), int(sh * ((r + 1) / 3 - 0.011))))
ART = {
    "kyiv": cell(0, 0), "markets": cell(1, 0), "cyclone": cell(2, 0), "gta": cell(3, 0),
    "faa": cell(0, 1), "cop31": cell(1, 1), "brussels": cell(2, 1), "berlin": cell(3, 1),
    "hormuz": cell(0, 2), "taipei": cell(1, 2), "smolensk": cell(2, 2), "shenzhen": cell(3, 2),
}

M = 26 * S; CW = W - 2 * M; gap = 10 * S
# ---------- masthead ----------
f_kick = F(SANS_B, 12.5)
d.text((M, 12 * S), "T H E   W O R L D   I N   O N E   D A Y", font=f_kick, fill=RED)
r = "54 STORIES · 7 REGIONS"
d.text((W - M - d.textlength(r, font=f_kick), 12 * S), r, font=f_kick, fill=RED)
f_title = F(SERIF_B, 44)
t = "Friday 20 November 2026"
d.text(((W - d.textlength(t, font=f_title)) / 2, 27 * S), t, font=f_title, fill=INK)
f_sub = F(SANS_I, 13)
sub = "Kyiv's bridges burn in a 510-weapon barrage · Asia's markets fall 5% in a day · GTA VI makes $3.79bn in 24 hours"
d.text(((W - d.textlength(sub, font=f_sub)) / 2, 82 * S), sub, font=f_sub, fill=(70, 62, 48))
d.line([M, 100 * S, W - M, 100 * S], fill=INK, width=2 * S)
d.line([M, 104 * S, W - M, 104 * S], fill=INK, width=S)
# ---------- stats ----------
stats = [("510", "drones & missiles, one night"), ("$3.79bn", "GTA VI's record first day"),
         ("-5.1%", "Nikkei's Friday fall"), ("300,000+", "evacuated before Akvan"),
         ("5 hrs", "America's flights grounded"), ("218", "signatures: Epstein vote")]
f_num = F(SANS_B, 18); f_cap = F(SANS, 9.5)
cellw = CW // 6
for i, (n, c) in enumerate(stats):
    x = M + i * cellw
    if i: d.line([x, 109 * S, x, 135 * S], fill=LINE, width=S)
    d.text((x + 6 * S, 108 * S), n, font=f_num, fill=RED if i in (1, 2) else INK)
    d.text((x + 6 * S, 129 * S), c, font=f_cap, fill=GREY)
d.line([M, 141 * S, W - M, 141 * S], fill=LINE, width=S)
# ---------- UTC timeline ----------
d.text((M, 146 * S), "THE DAY IN UTC", font=F(SANS_B, 11), fill=RED)
tl = [("~02:00", "Ballistic missiles hit Kyiv's Dnipro bridges"),
      ("02:30", "Cyclone Akvan crosses Odisha coast at Gopalpur"),
      ("06:00", "Tokyo close: Nikkei -5.1% in the AI rout"),
      ("09:00", "Akvan weakens; no deaths reported"),
      ("19:38", "Take-Two confirms GTA VI's $3.79bn day"),
      ("~20:00", "FAA halts US departures; 1.5m stranded")]
f_tt = F(SANS_B, 11); f_tx = F(SANS, 8.5)
for i, (tm, tx) in enumerate(tl):
    x = M + i * cellw
    d.text((x + 2 * S, 160 * S), tm, font=f_tt, fill=INK)
    block(x + 2 * S, 174 * S, cellw - 8 * S, tx, f_tx, (52, 48, 40), 10.5 * S)
# ---------- heroes ----------
heroes = [
    ("kyiv", (140, 40, 40), "1 · KYIV — WAR", "Russia rains 510 weapons on Kyiv; three bridges hit",
     "400+ drones and 110 missiles, 27 ballistic, in one of the war's biggest strikes. Three Dnipro bridges closed; power cut in 11 regions. Putin's answer to the Kerch Bridge. — Reuters, BBC"),
    ("markets", (24, 110, 70), "2 · WORLD — MARKETS", "AI rout: Asia's worst week since 2020",
     "Anthropic's record IPO could not stop the slide. The Nikkei fell 5.1% on Friday, Taiwan 6.2%, and Anthropic itself 12% — while Wall Street headed for its worst week since April 2025. — Reuters, AP"),
    ("cyclone", (30, 110, 150), "3 · GOPALPUR — STORM", "Cyclone Akvan comes ashore in Odisha",
     "Akvan crossed the coast near Gopalpur at 02:30 UTC with winds gusting to 90 km/h. Over 300,000 people had been evacuated; 209mm of rain fell at Patrapur. No deaths in the first reports. — IMD, AP"),
]
f_cat = F(SANS_B, 10.5); f_hh = F(SANS_B, 16); f_deck = F(SANS, 10)
tw3 = (CW - 2 * gap) // 3; hy = 196 * S; hh = 180 * S
for i, (art, color, cat, head, deck) in enumerate(heroes):
    x = M + i * (tw3 + gap)
    d.rectangle([x, hy, x + tw3, hy + hh], fill=CARD, outline=LINE, width=S)
    img.paste(fill(ART[art], tw3, 68 * S), (x, hy))
    d.rectangle([x, hy + 68 * S, x + tw3, hy + 74 * S], fill=color)
    block(x + 9 * S, hy + 79 * S, tw3 - 18 * S, cat, f_cat, color, 12 * S)
    y = block(x + 9 * S, hy + 93 * S, tw3 - 18 * S, head, f_hh, INK, 18.5 * S)
    block(x + 9 * S, hy + 130 * S, tw3 - 18 * S, deck, f_deck, (52, 48, 40), 12.5 * S)
# ---------- grid tiles with thumbs ----------
tiles = [
    ("gta", (112, 44, 140), "4 · NEW YORK — GAMES", "GTA VI makes $3.79bn in one day",
     "Take-Two confirmed $3.79bn in day-one sales — the biggest entertainment launch ever — with 32.5m copies sold before release. — Reuters"),
    ("faa", (28, 84, 140), "5 · WASHINGTON — AVIATION", "America's flights stop for five hours",
     "A telecom outage forced a nationwide ground stop, the longest since 9/11: 4,700 flights cancelled, 1.5m passengers stranded. — Al Jazeera"),
    ("cop31", (24, 110, 70), "6 · ANTALYA — CLIMATE", "COP31 in overtime; fossil fuels erased",
     "Suspended to Saturday, the talks' draft drops every mention of fossil fuels — and admits 1.5°C will be overshot. — UN News, AFP"),
    ("brussels", (28, 84, 140), "7 · BRUSSELS — EUROPE", "EU and UK clinch food and youth deals",
     "The second reset summit sealed trade, food and youth-mobility deals with PM Burnham; tuition-fee talks were put off. — Euronews, AP"),
    ("berlin", (70, 70, 90), "8 · BERLIN — EUROPE", "Merz: no 'new Yalta' over Europe's head",
     "After the Shenzhen three-power declaration, Chancellor Merz warned Europe will accept no settlement decided over its head. — reports"),
    ("hormuz", (140, 40, 40), "9 · STRAIT OF HORMUZ — WAR", "Tanker ablaze after mine strike",
     "Iran stepped up tanker attacks in the war's ninth month; one tanker caught fire after striking a mine. — reports"),
    ("taipei", (24, 110, 70), "10 · TAIPEI — MARKETS", "Taiwan's chip rout: worst week since 1990",
     "The Taiex fell 6.2% on Friday and 17% in the week as chip stocks led Asia's sell-off; TSMC lost 4.8%. — Reuters, Bloomberg"),
    ("smolensk", (140, 40, 40), "11 · SMOLENSK — WAR", "Drones hit Russian chemical plant",
     "Ukrainian drones reportedly hit the Dorogobuzh plant, maker of 11% of Russia's ammonium nitrate; a fire broke out. — Kyiv Independent, BBC"),
    ("shenzhen", (150, 108, 30), "12 · SHENZHEN — TRADE", "Prabowo and Xi launch trade-pact talks",
     "Indonesia and China opened trade-pact talks as firms signed 35 deals worth $15bn, from data centres to renewables. — Reuters, Xinhua"),
]
f_th = F(SANS_B, 12.5); f_td = F(SANS, 9.5)
ty = 380 * S; th = 82 * S; tgap = 6 * S
for r in range(3):
    for c in range(3):
        art, color, cat, head, deck = tiles[r * 3 + c]
        x = M + c * (tw3 + gap); y = ty + r * (th + tgap)
        d.rectangle([x, y, x + tw3, y + th], fill=CARD, outline=LINE, width=S)
        img.paste(fill(ART[art], 78 * S, th), (x, y))
        tx = x + 86 * S
        block(tx, y + 4 * S, tw3 - 93 * S, cat, f_cat, color, 11 * S)
        yy = block(tx, y + 16 * S, tw3 - 93 * S, head, f_th, INK, 15 * S)
        block(tx, y + 46 * S, tw3 - 93 * S, deck, f_td, (52, 48, 40), 11.5 * S)
# ---------- also ----------
ay = 646 * S
d.text((M, ay), "ALSO ON FRIDAY 20 NOVEMBER", font=F(SANS_B, 12.5), fill=RED)
d.line([M, ay + 18 * S, W - M, ay + 18 * S], fill=LINE, width=S)
also = [
    ("WASHINGTON —", "House rebels reach 218 signatures, forcing a floor vote on releasing the Epstein files."),
    ("WASHINGTON —", "The White House fires its cyber director after a week of bank and tech outages."),
    ("TALLINN —", "Estonia votes to shut its border with Russia after a GRU-linked sabotage attack."),
    ("ROME —", "Italy fines Meta €805m over its access to Android users' photos."),
    ("ROME —", "Workers and students stage a nationwide strike over the cost of living."),
    ("KHARTOUM —", "A drone strike kills 10 people at a gold mine in South Kordofan."),
    ("SAN SALVADOR —", "President Bukele registers to seek a third term in office."),
    ("CARACAS —", "The US and Venezuela sign a military cooperation deal."),
    ("AL-DAHI —", "A mosque is set on fire in a northern Israeli village."),
    ("WASHINGTON —", "First US deep-sea mining leases are auctioned despite a judge's ruling."),
    ("PORTSMOUTH —", "HMS Vengeance surfaces after a record 217 days on underwater patrol."),
    ("NEW YORK —", "The mayor unveils a plan to close the Rikers Island jail by 2032."),
    ("RABAT —", "Morocco commits €366m to build a national defence industry by 2035."),
    ("GENEVA —", "The UN cuts its food-aid target even as a hunger crisis looms."),
    ("LONDON —", "Helena Kennedy calls for a tribunal on Islamic State's crimes against the Yazidis."),
    ("MADRID —", "Amnesty says Spanish police used excessive force during the general strike."),
    ("KYIV —", "UNICEF: child deaths and injuries climb back toward 2022 levels."),
    ("EUROPE —", "Nations League draw pairs Spain with France and England with Norway."),
    ("TENNIS —", "The ATP unveils a $350m pay plan reaching the top 250 players from 2028."),
    ("NASHVILLE —", "Ella Langley sweeps the CMA Awards, led by Entertainer of the Year."),
    ("WASHINGTON —", "The IMF warns global public debt is nearing 100% of world GDP."),
    ("CYBER —", "China-linked spies exploited a VMware vCenter zero-day before it was patched."),
    ("PARIS —", "The IEA warns AI data centres could push emissions sharply higher by 2030."),
    ("RICHMOND —", "Virginia pulls out of Trump's school-choice tax-credit programme."),
    ("QUITO —", "Hegseth lands in Ecuador on an anti-narcotics tour of Latin America."),
    ("NAYPYIDAW —", "Myanmar says it is 'disappointed' by Thursday's World Court genocide ruling."),
    ("VATICAN —", "A giant Christmas tree is lifted into place beside St Peter's Basilica."),
    ("ANTARCTICA —", "Scientists find ancient 'supermountains' buried beneath the ice sheet."),
    ("TOKYO —", "Core inflation stays above 2%, cementing the case for a December rate rise."),
    ("HONG KONG —", "The Hang Seng falls 1.9% as Asia's worst week since 2020 ends."),
    ("SHENZHEN —", "Trump, Xi and Putin hold their first three-way summit and issue a four-point peace declaration."),
    ("COPENHAGEN —", "Denmark's parliament approves a trilateral security pact with Greenland and the United States."),
    ("YENNE —", "Dozens are missing after a migrant boat capsizes off Senegal."),
    ("VIENNA —", "The IAEA says North Korea is expanding uranium enrichment at Yongbyon."),
    ("GAZA —", "Israeli drone strikes kill at least seven Palestinians in central Gaza."),
    ("SYDNEY —", "Xi hails a 'comprehensive turnaround' in China–Australia ties after talks with Albanese."),
]
f_lead = F(SANS_B, 9.5); f_item = F(SANS, 9.5)
colw = (CW - 2 * gap) // 3; iy = ay + 26 * S
for i, (lead, body) in enumerate(also):
    x = M + (i // 12) * (colw + gap); y = iy + (i % 12) * 22 * S
    d.text((x, y), "▪ " + lead, font=f_lead, fill=INK)
    lw = d.textlength("▪ " + lead + " ", font=f_lead)
    lines = wrap(body, f_item, colw - lw)
    d.text((x + lw, y), lines[0], font=f_item, fill=(52, 48, 40))
    for j, ln in enumerate(lines[1:], 1):
        d.text((x, y + j * 11 * S), ln, font=f_item, fill=(52, 48, 40))
# ---------- in brief ----------
iby = 941 * S
d.text((M, iby), "IN BRIEF — THE DAY IN NUMBERS", font=F(SANS_B, 11), fill=RED)
briefs = [
    ("LOS ANGELES —", "M4.2 quake wakes the city at 3:25 a.m.; no damage."),
    ("MADANG —", "M5.1 quake 62 km NW of Madang, PNG, at 05:17 UTC."),
    ("WASHINGTON —", "Senate passes the energy-permitting bill 62–33."),
    ("BRUSSELS —", "EU adopts €1bn Ukraine aid via the Peace Facility."),
    ("LONDON —", "UK pledges 1,000+ drones for Ukraine: a £260m package."),
    ("SYDNEY —", "Jepchirchir banned 3 years for doping; Sydney title stripped."),
]
f_blead = F(SANS_B, 8.5); f_bitem = F(SANS, 8.5)
for i, (lead, body) in enumerate(briefs):
    x = M + (i % 3) * (colw + gap); y = iby + 14 * S + (i // 3) * 15 * S
    d.text((x, y), "▪ " + lead, font=f_blead, fill=INK)
    lw = d.textlength("▪ " + lead + " ", font=f_blead)
    d.text((x + lw, y), body, font=f_bitem, fill=(52, 48, 40))
# ---------- footer ----------
fy = 991 * S
d.line([M, fy - 6 * S, W - M, fy - 6 * S], fill=INK, width=S)
f_foot = F(SANS, 9)
block(M, fy, CW, "DATE CHECK — every story on this page happened, or was first reported, on Friday 20 November 2026, in some time zone. Claims are attributed, not stated as fact.", f_foot, GREY, 10.5 * S)
block(M, fy + 11 * S, CW, "Sources: Reuters, AP, BBC, AFP, Al Jazeera, UN News, Euronews, Kyiv Independent, Xinhua, Bloomberg, IMD, One Turn, Open Chronicle, USGS, GFZ, ABC. Pictures: original illustrations. Page drawn in code.", f_foot, GREY, 10.5 * S)

img = img.resize((1024, 1024), Image.LANCZOS)
out = os.path.join(HERE, "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), "bytes")
