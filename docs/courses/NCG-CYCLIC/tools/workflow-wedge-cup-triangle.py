"""Exact triangle witness for workflow-wedge-cup-proof.md, WC7.

Reproducible planar figure; the displayed rationals are checked with Fraction.
The mathematical vertices are (0,0),(1,0),(0,1). Their screen image is the
affine map (x,y) -> (panel_left+120+360*x,550-360*y), with no geometry fitting.
Run with the bundled Python; only the already bundled Pillow is required.
"""

from fractions import Fraction
from pathlib import Path
import json
import math

from PIL import Image, ImageDraw, ImageFont


VERTICES = ((0, 0), (1, 0), (0, 1))
PREFERRED_EDGES = ((0, 1), (0, 2), (1, 2))
BOUNDARY = (((1, 2), 1), ((0, 2), -1), ((0, 1), 1))


def dx(edge):
    i, j = edge
    return Fraction(VERTICES[j][0] - VERTICES[i][0])


def dy(edge):
    i, j = edge
    return Fraction(VERTICES[j][1] - VERTICES[i][1])


def h_value(edge):
    # On e(s)=vi+s(vj-vi), x-x(vi)=s*dx(e), dy=dy(e)*ds.
    return dx(edge) * dy(edge) * Fraction(1, 2)


F_VALUE = Fraction(1, 2)
G_VALUE = dx((0, 1)) * dy((1, 2))
H_VALUES = {edge: h_value(edge) for edge in PREFERRED_EDGES}
DELTA_H = sum(sign * H_VALUES[edge] for edge, sign in BOUNDARY)
assert G_VALUE == 1
assert H_VALUES == {(0, 1): 0, (0, 2): 0, (1, 2): Fraction(-1, 2)}
assert F_VALUE - G_VALUE == DELTA_H == Fraction(-1, 2)

SCALE = 2
WIDTH, HEIGHT = 1800, 760
image = Image.new("RGB", (WIDTH*SCALE, HEIGHT*SCALE), "white")
draw = ImageDraw.Draw(image)
FONT_DIR = Path("C:/Windows/Fonts")


def font(size, bold=False):
    name = "seguisb.ttf" if bold else "seguisym.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size*SCALE)


def text(x, y, value, size=26, fill="#253448", anchor="mm", bold=False):
    draw.text((round(x*SCALE), round(y*SCALE)), value, font=font(size, bold),
              fill=fill, anchor=anchor)


def point(panel, index):
    x, y = VERTICES[index]
    return (panel*600 + 120 + 360*x, 550 - 360*y)


def line(points, fill, width):
    draw.line([(round(x*SCALE), round(y*SCALE)) for x, y in points],
              fill=fill, width=width*SCALE)


def arrow(panel, edge, color, width=4):
    a, b = (point(panel, index) for index in edge)
    x0, y0 = (a[c] + .14*(b[c]-a[c]) for c in (0, 1))
    x1, y1 = (a[c] + .86*(b[c]-a[c]) for c in (0, 1))
    line(((x0, y0), (x1, y1)), color, width)
    length = math.hypot(x1-x0, y1-y0)
    ux, uy = (x1-x0)/length, (y1-y0)/length
    tip = (x1, y1)
    base = (x1-17*ux, y1-17*uy)
    triangle = (tip, (base[0]-7*uy, base[1]+7*ux),
                (base[0]+7*uy, base[1]-7*ux))
    draw.polygon([(round(x*SCALE), round(y*SCALE)) for x, y in triangle],
                 fill=color)


text(900, 40, "Closed forms a = dx and b = dy on the exact oriented triangle",
     size=33, bold=True)
for separator in (600, 1200):
    line(((separator, 93), (separator, 710)), "#e0e6ed", 1)

for panel in range(3):
    pts = [point(panel, index) for index in range(3)]
    draw.polygon([(x*SCALE, y*SCALE) for x, y in pts], fill="#edf4fa")
    line(pts + [pts[0]], "#697586", 2)
    for x, y in pts:
        draw.ellipse(((x-5)*SCALE, (y-5)*SCALE,
                      (x+5)*SCALE, (y+5)*SCALE), fill="#253448")

text(300, 110, "Wedge integration", size=30, bold=True)
for edge in ((0, 1), (1, 2), (2, 0)):
    arrow(0, edge, "#2d5b87")
text(120, 590, "v₀ = (0,0)", size=24)
text(480, 590, "v₁ = (1,0)", size=24)
text(120, 158, "v₂ = (0,1)", size=24, anchor="lm")
text(235, 385, "dx ∧ dy", size=33)
text(235, 440, "area = 1/2", size=27)
text(300, 680, "I(dx ∧ dy)([012]) = 1/2", size=30)

text(900, 110, "Alexander–Whitney cup", size=30, bold=True)
arrow(1, (0, 1), "#b24a35", 6)
arrow(1, (1, 2), "#7652a7", 6)
text(709, 589, "v₀", size=24)
text(1093, 590, "v₁", size=24)
text(727, 158, "v₂", size=24)
text(894, 586, "[01]: ∫ dx = 1", size=26, fill="#b24a35")
text(1020, 304, "[12]: ∫ dy = 1", size=26, fill="#7652a7")
text(850, 460, "shared vertex: v₁", size=24)
text(900, 680, "((I dx) ∪ (I dy))([012]) = 1", size=29)

text(1500, 110, "The cochain homotopy", size=30, bold=True)
arrow(2, (0, 1), "#697586")
arrow(2, (0, 2), "#697586")
arrow(2, (1, 2), "#b24a35", 6)
text(1309, 589, "v₀", size=24)
text(1693, 590, "v₁", size=24)
text(1327, 158, "v₂", size=24)
text(1494, 586, "H₀₁ = 0", size=26)
text(1304, 375, "H₀₂ = 0", size=24, anchor="rm")
text(1620, 304, "H₁₂ = −1/2", size=28, fill="#b24a35")
text(1440, 420, "x − 1 = −s", size=28)
text(1440, 471, "dy = ds", size=28)
text(1500, 668, "δH = H₁₂ − H₀₂ + H₀₁", size=29)
text(1500, 712, "= −1/2 = 1/2 − 1", size=29)

output = Path(__file__).resolve().parents[1]/"public/assets/workflow-wedge-cup-triangle.png"
image.save(output)
print(json.dumps({"figure": str(output), "F": str(F_VALUE), "G": str(G_VALUE),
                  "H01": str(H_VALUES[(0, 1)]), "H02": str(H_VALUES[(0, 2)]),
                  "H12": str(H_VALUES[(1, 2)]), "delta_H": str(DELTA_H),
                  "exact_checks": "passed"}))
