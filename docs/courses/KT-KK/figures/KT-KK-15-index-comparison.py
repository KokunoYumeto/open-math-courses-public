from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

base = Path(__file__).resolve().parent
im = Image.new("RGB", (1400, 940), "white")
d = ImageDraw.Draw(im)
fontfile = "C:/Windows/Fonts/segoeui.ttf"
def txt(x, y, text, n=25, c="#17364a"):
    d.text((x, y), text, font=ImageFont.truetype(fontfile, n), fill=c)
def arrow(a, b, color="#246745", width=4):
    d.line((a, b), fill=color, width=width)
    vx, vy = b[0] - a[0], b[1] - a[1]
    norm = math.hypot(vx, vy); vx /= norm; vy /= norm
    px, py = -vy, vx
    d.polygon([b, (b[0]-14*vx+7*px, b[1]-14*vy+7*py),
               (b[0]-14*vx-7*px, b[1]-14*vy-7*py)], fill=color)

txt(42, 22, "Universal quantization and the embedding index", 37)
d.rounded_rectangle((40, 90, 1360, 430), radius=16, fill="#f3f8fc", outline="#c5d8e5", width=2)
txt(66, 110, "One KK morphism handles every symbol and every graded Clifford class", 28, "#285c80")
txt(128, 182, "A_M", 35); txt(626, 182, "B = C₀(T*M)", 32); txt(1166, 182, "C", 35)
arrow((248, 207), (586, 207), "#285c80"); txt(338, 164, "e₀   (invertible in KK)", 22, "#285c80")
arrow((586, 252), (248, 252), "#285c80"); txt(414, 260, "z = e₀ inverse", 22, "#285c80")
arrow((865, 207), (1125, 207), "#285c80"); txt(885, 160, "a_M = Dolbeault J−", 22, "#285c80")
arrow((248, 330), (1125, 330), "#285c80"); txt(487, 344, "e₁ followed by Hilbert-space Morita", 24, "#285c80")
txt(68, 389, "xV · a_M = Clifford Dirac; multiply by yV to identify a_M.   [CI.47–49]", 24)

d.rounded_rectangle((40, 462, 910, 891), radius=16, fill="#f4faf5", outline="#c6dfcd", width=2)
txt(66, 482, "Doubled normal and compact tubular support", 28, "#276346")
txt(93, 552, "a in K₀(T*M)", 28); txt(542, 552, "i_cot*(a) in K₀(T*Rᴺ)", 23)
arrow((309, 582), (520, 582)); txt(329, 530, "Thom + extension", 20, "#276346")
arrow((169, 620), (169, 715)); txt(202, 650, "Dolbeault J−", 22, "#276346")
arrow((686, 620), (686, 715)); txt(485, 650, "outward Bott inverse", 21, "#276346")
txt(150, 733, "Z", 31); txt(670, 733, "Z", 31); d.line((238, 751, 616, 751), fill="#276346", width=3)
txt(338, 719, "same pairing", 23, "#276346")
txt(67, 814, "Relative defect support stays compact in the tubular region.", 22)
txt(67, 851, "Normal Gaussian reduction + local resolvent comparison.  [CI.50–59]", 21)

d.rounded_rectangle((940, 462, 1360, 891), radius=16, fill="#fff8f2", outline="#e5d0bf", width=2)
txt(963, 482, "One normal real line", 28, "#984d28")
ox, oy = 1055, 663
arrow((ox-63, oy), (ox+123, oy), "#984d28")
arrow((ox, oy+67), (ox, oy-91), "#984d28")
txt(1177, 662, "u", 22, "#984d28"); txt(1068, 560, "η", 22, "#984d28")
txt(963, 740, "Thom:  c(u) + f(η)", 23)
txt(963, 780, "Dirac:  f(du) + c(dη)", 23)
txt(963, 821, "w = (00 + 11)/√2", 24, "#984d28")
txt(963, 856, "even; invariant under O(1)", 21, "#984d28")
txt(43, 907, "The all-rank invariant exterior tensor and its full operator/domain proof are CI.53–55.", 23)
im.save(base / "KT-KK-15-index-comparison.png")
