"""Reproduce original Fourier zero-density illustrations. CC0 1.0.

The plots use a finite two-atom measure and its exact zero formula.
Floating point is used only for illustrative coordinates and disk counts.
The theorem and all limits are proved in the accompanying lesson.
"""
from pathlib import Path
import json
import math
import bisect
import numpy as np
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderSVG, renderPDF
from reportlab.lib.colors import HexColor, white
import pypdfium2 as pdfium

HERE = Path(__file__).resolve().parent
INK = "#253650"
TEAL = "#007e87"
PLUM = "#a63463"
GOLD = "#a26600"
A, B, WIDTH = -1.0, 2.0, 3.0
THETA = math.pi / 4
HEIGHT = 0.5
SCALES = [4.0, 12.0, 30.0]


def text(d, x, y, value, size=13, anchor="middle", color=INK):
    d.add(String(x, y, value, fontName="Helvetica", fontSize=size,
                 textAnchor=anchor, fillColor=HexColor(color)))


def save(d, name):
    renderSVG.drawToFile(d, str(HERE / (name + ".svg")))
    path = HERE / (name + ".pdf")
    renderPDF.drawToFile(d, str(path))
    pdf = pdfium.PdfDocument(str(path))
    pdf[0].render(scale=1.7).to_pil().save(HERE / (name + ".png"))
    pdf.close()


def real_zero(k):
    return (THETA + (2 * k + 1) * math.pi) / WIDTH


def zeros_in_disk(radius):
    # This bound includes every possible lattice index in the disk.
    kmax = math.ceil(WIDTH * radius / (2 * math.pi)) + 3
    return [(real_zero(k), HEIGHT) for k in range(-kmax, kmax + 1)
            if math.hypot(real_zero(k), HEIGHT) < radius]


def disk_axes(d, cx, cy, r):
    for tick in [-1, 0, 1]:
        xx, yy = cx + r * tick, cy + r * tick
        if tick:
            d.add(Line(xx, cy-r, xx, cy+r, strokeColor=HexColor("#e7ebee"), strokeWidth=.5))
            d.add(Line(cx-r, yy, cx+r, yy, strokeColor=HexColor("#e7ebee"), strokeWidth=.5))
        d.add(Line(xx, cy-3, xx, cy+3, strokeColor=HexColor("#939fa8"), strokeWidth=.6))
        text(d, xx, cy-r-22, f"{tick:g}", 11)
    d.add(Line(cx-r-10, cy, cx+r+10, cy, strokeColor=HexColor("#939fa8"), strokeWidth=.7))
    d.add(Line(cx, cy-r-10, cx, cy+r+10, strokeColor=HexColor("#939fa8"), strokeWidth=.7))
    d.add(Circle(cx, cy, r, fillColor=None, strokeColor=HexColor("#526580"), strokeWidth=1.2))
    text(d, cx+r+12, cy+9, "Re z", 11, "end")
    text(d, cx+8, cy+r+10, "Im z", 11, "start")


d = Drawing(1560, 550)
d.add(Rect(0, 0, 1560, 550, fillColor=white, strokeColor=None))
text(d, 780, 515, "Scaled zeros become uniform length on the real axis", 24)
text(d, 780, 485, "a = -1, b = 2, c = exp(-3/2) exp(i pi/4); all zeros are simple", 15)
centers = [210, 590, 970, 1350]
cy, r = 262, 145
panels = []
for cx, scale in zip(centers[:3], SCALES):
    disk_axes(d, cx, cy, r)
    text(d, cx, 435, f"Scale R = {scale:g}", 19)
    points = zeros_in_disk(scale)
    marker_radius = 10 / math.sqrt(scale)
    for xx, yy in points:
        d.add(Circle(cx+r*xx/scale, cy+r*yy/scale, marker_radius,
                     fillColor=HexColor(TEAL), strokeColor=None))
    text(d, cx, 72, f"height = 1/(2R) = {HEIGHT/scale:.4f}", 13)
    text(d, cx, 50, f"{len(points)} dots; mass = {len(points)/scale:.4f}", 13, color=TEAL)
    panels.append({"R":scale, "zeros_in_open_disk":len(points),
                   "restricted_mass":len(points)/scale,
                   "scaled_points":[[x/scale,y/scale] for x,y in points],
                   "marker_radius_points":marker_radius})
cx = centers[3]
disk_axes(d, cx, cy, r)
text(d, cx, 435, "Limiting measure", 19)
d.add(Line(cx-r, cy, cx+r, cy, strokeColor=HexColor(PLUM), strokeWidth=4))
for xx in [cx-r, cx+r]:
    d.add(Circle(xx, cy, 4.2, fillColor=white, strokeColor=HexColor(PLUM), strokeWidth=1.8))
text(d, cx, 337, "density = 3/(2 pi)", 15, color=PLUM)
text(d, cx, 72, "real axis: equal mass per unit length", 12)
text(d, cx, 50, f"disk mass = 3/pi = {WIDTH/math.pi:.4f}", 13, color=PLUM)
text(d, 780, 18, "Equal horizontal and vertical scales. Each dot has weight 1/R; its displayed area is proportional to that weight.", 13)
save(d, "scaled-zero-measures")


rs = np.linspace(2.0, 80.0, 2401)
kmax = math.ceil(WIDTH * 81 / (2 * math.pi)) + 3
zero_radii = sorted(math.hypot(real_zero(k), HEIGHT) for k in range(-kmax,kmax+1))
counts = [bisect.bisect_left(zero_radii, float(radius)) for radius in rs]
ratios = [count / float(radius) for count,radius in zip(counts,rs)]
d = Drawing(1240, 650)
d.add(Rect(0, 0, 1240, 650, fillColor=white, strokeColor=None))
text(d, 620, 612, "Disk counts retain multiplicity", 24)
text(d, 620, 580, "Exact lattice counts at sampled radii; connecting segments illustrate the samples", 15)
p = LinePlot()
p.x, p.y, p.width, p.height = 82, 120, 1050, 385
p.data = [list(zip(rs.tolist(),ratios)),
          list(zip(rs.tolist(),[3*x for x in ratios])),
          [(2,0),(80,0)], [(2,WIDTH/math.pi),(80,WIDTH/math.pi)],
          [(2,3*WIDTH/math.pi),(80,3*WIDTH/math.pi)]]
p.xValueAxis.valueMin, p.xValueAxis.valueMax = 2, 80
p.xValueAxis.valueSteps = [2,20,40,60,80]
p.yValueAxis.valueMin, p.yValueAxis.valueMax = -.08, 4.1
p.yValueAxis.valueSteps = [0,1,2,3,4]
for axis in [p.xValueAxis,p.yValueAxis]:
    axis.labels.fontName, axis.labels.fontSize = "Helvetica", 12
    axis.strokeColor = HexColor("#8a929b")
for yy in [0,1,2,3,4]:
    y = p.y + (yy + .08) * p.height / 4.18
    d.add(Line(p.x,y,p.x+p.width,y,strokeColor=HexColor("#e5e8eb"),strokeWidth=.6))
for i,color in enumerate([TEAL,PLUM,GOLD,TEAL,PLUM]):
    p.lines[i].strokeColor = HexColor(color)
    p.lines[i].strokeWidth = 1.5 if i < 3 else 1
    if i >= 3: p.lines[i].strokeDashArray = [6,5]
d.add(p)
text(d, 82, 520, "N(R)/R", 15, "start")
text(d, 607, 70, "Open disk radius R", 15)
for x,label,color in [(95,"two atoms: simple zeros",TEAL),
                       (495,"third convolution power: triple zeros",PLUM),
                       (1000,"point support: no zeros",GOLD)]:
    d.add(Line(x,548,x+28,548,strokeColor=HexColor(color),strokeWidth=2))
    text(d,x+37,544,label,13,"start")
for value,label,color in [(WIDTH/math.pi,"3/pi",TEAL),(3*WIDTH/math.pi,"9/pi",PLUM)]:
    y = p.y + (value+.08)*p.height/4.18
    text(d,1144,y+4,label,13,"start",color)
text(d,620,32,"Finite samples illustrate the exact formulas (Z24)-(Z26); the continuous-cutoff argument proves the general limit.",13)
save(d,"zero-count-density")

geometry = {
    "schema":"AN02-original-L137-figures/v1", "license":"CC0-1.0",
    "author":"GPT-6.1 Sol (OpenAI)",
    "human_source_credit":"Lars Hormander, The Analysis of Linear Partial Differential Operators II (1983; second revised printing 1990; reprint 2005), Theorem 16.1.9, printed page 313; original illustrations and examples",
    "measure":{"a":A,"b":B,"width":WIDTH,
               "formula":"delta_a + c delta_b",
               "c":"exp(-3/2) exp(i*pi/4)","argument":"pi/4"},
    "zeros":{"formula":"(pi/4+(2*k+1)*pi)/3 + i/2, k in Z",
             "height":HEIGHT,"spacing":"2*pi/3","multiplicity":1},
    "scaled_zero_measures":{"domain":"open unit disk in the Euclidean complex plane",
                            "metric":"identical horizontal and vertical scales",
                            "mass_per_dot":"1/R",
                            "displayed_dot_area":"100*pi/R square drawing points",
                            "panels":panels,
                            "limit_density":"3/(2*pi) length on embedded real axis",
                            "limit_disk_mass":"3/pi",
                            "limit_boundary_mass":0,
                            "proof_locators":"Lemma Z2 and sections 3-5, (Z17)-(Z22)"},
    "zero_count_density":{"domain":"R from 2 to 80",
                          "sample_radii":rs.tolist(),"simple_counts":counts,
                          "method":"bisect_left on exact-formula zero radii; strict open disk",
                          "floating_point_scope":"illustrative evaluation only",
                          "convolution_power":3,"convolution_support_hull":[-3,6],
                          "simple_limit":"3/pi","triple_limit":"9/pi","point_limit":0,
                          "proof_locators":"Examples A-D, (Z24)-(Z27); section 5"},
    "output":{"svg":"vector figure","pdf":"original one-page vector figure",
              "png":"rendered from own PDF at scale 1.7"}
}
(HERE/"geometry.json").write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"figures":2,"scaled_panel_counts":[p["zeros_in_open_disk"] for p in panels],
                  "scales":SCALES,"last_sample_R":float(rs[-1]),
                  "last_simple_N_over_R":ratios[-1],"limit":WIDTH/math.pi}))
