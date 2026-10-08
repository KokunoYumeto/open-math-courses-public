"""Exact two-arc and natural-chain-map schematic for the SNC proof."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
from matplotlib.font_manager import FontProperties, findfont

ROOT = Path(__file__).resolve().parent
S = 2
im = Image.new("RGB", (1580*S, 1040*S), "#f5f8fb")
d = ImageDraw.Draw(im)

def text(x, y, value, size=24, bold=False, fill="#122c40"):
    path = findfont(FontProperties(family="DejaVu Sans", weight="bold" if bold else "normal"))
    d.text((x*S, y*S), value, font=ImageFont.truetype(path, size*S), fill=fill)

def box(x1, y1, x2, y2, fill="#ffffff", stroke="#8295a2"):
    d.rounded_rectangle((x1*S, y1*S, x2*S, y2*S), radius=14*S,
                        fill=fill, outline=stroke, width=2*S)

def arrow(x1, y1, x2, y2, fill="#21799a"):
    d.line((x1*S, y1*S, x2*S, y2*S), fill=fill, width=3*S)
    a = math.atan2(y2-y1, x2-x1)
    pts = [(x2*S, y2*S)]
    for delta in [-0.55, 0.55]:
        pts.append(((x2-12*math.cos(a+delta))*S,
                    (y2-12*math.sin(a+delta))*S))
    d.polygon(pts, fill=fill)

text(45, 29, "The natural de Rham comparison and its period sign", 32, True)
text(45, 81, "One coordinate shown; the proof iterates the exact chain map at every SNC crossing.", 24)
box(35, 131, 720, 833)
box(752, 131, 1544, 833)
text(62, 156, "Two arcs of one positively oriented circle", 25, True)
text(62, 202, "epsilon = pi/8; overlaps at 0 and pi", 23)
cx, cy, radius = 372, 423, 146
eps = math.pi/8

def arc(lo, hi, color):
    pts = [((cx+radius*math.cos(t))*S, (cy-radius*math.sin(t))*S)
           for t in [lo+(hi-lo)*j/160 for j in range(161)]]
    d.line(pts, fill=color, width=18*S, joint="curve")
    for x,y in pts:
        d.ellipse((x-9*S,y-9*S,x+9*S,y+9*S), fill=color)

arc(eps, math.pi-eps, "#3988c8")
arc(math.pi+eps, 2*math.pi-eps, "#dc8a34")
for lo, hi in [(-eps, eps), (math.pi-eps, math.pi+eps)]:
    arc(lo, hi, "#9a67ba")
d.ellipse(((cx-5)*S,(cy-5)*S,(cx+5)*S,(cy+5)*S), fill="#778895")
text(333, 293, "I0", 25, True)
text(333, 515, "I1", 25, True)
text(533, 413, "0 = 2pi", 23)
text(143, 413, "pi", 23)
arrow(393, 266, 346, 268, "#236188")
arrow(345, 579, 393, 579, "#a65d17")
text(71, 602, "Middle seam: identical lifts, coefficient b - a.", 23)
text(71, 642, "End seam: I1 lift is 2pi; coefficient b - R a.", 23)
text(71, 688, "R = T^(-1) = exp(2pi i A)", 26, True)
text(71, 731, "delta(a,b) = (b-a, b-Ra)", 26, True)
text(71, 778, "p0(a,b)=a;  p1(c,d)=c-d;  d_K=R-I.", 23)

text(778, 156, "The actual comparison chain maps", 27, True)
box(825, 215, 1457, 285, "#e5eff8")
text(850, 236, "Meromorphic flat de Rham forms", 26, True)
arrow(1405, 298, 1405, 337)
text(797, 304, "actual restriction map", 21)
box(825, 351, 1457, 424, "#e5eff8")
text(850, 372, "Smooth flat forms on U", 26, True)
arrow(1405, 437, 1405, 476)
text(786, 444, "Cech augmentation / radial restriction", 20)
box(825, 488, 1457, 560, "#f2eafa")
text(850, 510, "Sector Cech / angular de Rham total", 25)
arrow(1405, 573, 1405, 613)
text(797, 579, "explicit F, formula (5.4m)", 21)
box(825, 626, 1457, 700, "#e4f3e9")
text(850, 648, "K(R_i - I; W): actual cubical periods", 25)
text(780, 728, "F on constants = Cech reduction p.", 23)
text(780, 770, "F on global forms = backwards-transport integral.", 22)

box(35, 862, 1544, 1006)
text(63, 885, "Zero Laurent term:  period in coordinates I = product(Q_i) v_I", 28, True)
text(63, 934, "Q_i = integral_0^(2pi i) exp(u A_i) du;    Q_i A_i = R_i - I.", 26)
text(63, 975, "Proof: seams (5.4i)-(5.4n); totalization (5.4o)-(5.4p); cube signs (5.4s)-(5.4u).", 19)
im.save(ROOT / "snc-period-comparison.png")
print(str(ROOT / "snc-period-comparison.png"))
