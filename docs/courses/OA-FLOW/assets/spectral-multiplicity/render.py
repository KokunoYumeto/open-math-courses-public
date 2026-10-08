"""Original exact spectral-multiplicity figures. No source images or font copies.
Run: python render.py --font-dir PATH/TO/typeiii-zero-decomposition
data.json is the exact model contract; assertions check displayed constants.
Output: figures/*.svg, *.png.
"""
from pathlib import Path
import argparse, json, math, hashlib, itertools
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, Rectangle

HERE = Path(__file__).resolve().parent
D = json.loads((HERE / "data.json").read_text(encoding="utf-8"))
assert [m["multiplicity"] for m in D["measures"]] == [3, 2, "countably infinite"]
assert D["cantor"]["drawn_level"] == 5
assert (D["scaling"]["initial_t"], D["scaling"]["final_t"]) == (2, 1)
assert D["scaling"]["s"] == "log(2)"
assert (D["fibers"]["source_dimension"], D["fibers"]["target_dimension"]) == (2, 3)
P = argparse.ArgumentParser(description=__doc__)
P.add_argument("--font-dir", required=True, type=Path)
args = P.parse_args()
regular = args.font_dir / "DejaVuSans.ttf"
bold = args.font_dir / "DejaVuSans-Bold.ttf"
for p in (regular, bold):
    if not p.is_file():
        raise FileNotFoundError(p)
FP = FontProperties(fname=str(regular))
FB = FontProperties(fname=str(bold))
plt.rcParams.update({
    "svg.hashsalt": "oa-flow-spectral-multiplicity-v1",
    "svg.fonttype": "path", "axes.unicode_minus": False,
    "figure.facecolor": "#ffffff", "savefig.facecolor": "#ffffff",
    "lines.solid_capstyle": "round",
})
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
INK, MUTED, ATOM, AC, CANTOR = "#132b3a", "#566875", "#a23d29", "#216d9d", "#68519a"

def text(ax, x, y, s, size=12, color=INK, weight=False, **kw):
    return ax.text(x, y, s, fontproperties=FB if weight else FP,
                   fontsize=size, color=color, **kw)

def arrow(ax, a, b, color=INK, scale=14, style="-|>", **kw):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style,
                               mutation_scale=scale, color=color, linewidth=1.8, **kw))

def base():
    fig = plt.figure(figsize=(13.2, 7.7))
    ax = fig.add_axes([0.035, 0.035, 0.93, 0.93])
    ax.set_xlim(0, 13.2); ax.set_ylim(0, 7.7); ax.axis("off")
    return fig, ax

def save(fig, name):
    title = {"measure-multiplicity": "Measure classes and spectral fiber dimensions",
             "carrier-scaling": "Negative dilation and global versus sector continuity"}[name]
    description = {"measure-multiplicity": "Atomic delta at 3/2, uniform measure on [1,2], and singular Cantor probability have mutually orthogonal bidual supports and fiber multiplicities 3, 2, infinity. A coordinate inclusion C^2 to C^3 exists; its reverse is obstructed.",
                   "carrier-scaling": "At s=log(2), t=2 moves to t=1. A normal point functional of the moving point projection is 1 at zero and 0 otherwise. On the Lebesgue sector, the interval-overlap test is max(1-abs(s),0)."}[name]
    fig.savefig(OUT / (name + ".svg"),
                metadata={"Date": None, "Creator": "Original OA-FLOW spectral-multiplicity renderer", "Title": title, "Description": description})
    fig.savefig(OUT / (name + ".png"), dpi=180,
                metadata={"Software": "Original OA-FLOW spectral-multiplicity renderer", "Title": title, "Description": description})
    plt.close(fig)

def cantor_intervals(level):
    intervals = [(1.0, 2.0)]
    for _ in range(level):
        intervals = [(u, u+(v-u)/3) for u,v in intervals] + [
            (v-(v-u)/3,v) for u,v in intervals]
        intervals.sort()
    return intervals

def coords(ax, x, y, n, color, infinity=False):
    for j in range(n):
        ax.scatter([x+0.31*j], [y], s=43, c=[color], zorder=4)
    if infinity:
        text(ax, x+0.31*n+0.02, y-0.045, "…", size=19, color=color)

fig, ax = base()
text(ax, 0.05, 7.32, "Null sets and fiber dimensions are separate data", 21, weight=True)
text(ax, 0.05, 6.91, "Exact probability measures on [1, 2]; multiplicities are constant on each measure class.", 12.1, color=MUTED)
text(ax, 0.05, 6.32, "SCALAR MEASURE", 11, weight=True)
text(ax, 8.25, 6.32, "FIBER OVER ALMOST EVERY t", 11, weight=True)
x0, x1 = 3.3, 7.55
convert = lambda t: x0+(x1-x0)*(t-1)
rows = [
    (5.56, ATOM, "Atomic", "δ at t = 3/2", 3, "m = 3"),
    (4.28, AC, "Absolutely continuous", "Lebesgue probability", 2, "m = 2"),
    (3.00, CANTOR, "Singular continuous", "Cantor probability", 4, "m = ∞"),
]
for y, col, label, sub, n, mult in rows:
    ax.plot([x0,x1], [y,y], color="#aab6be", lw=1)
    for val in [1,2]:
        ax.plot([convert(val),convert(val)], [y-.065,y+.065], color=MUTED, lw=1)
        text(ax, convert(val), y-.29, str(val), size=10, color=MUTED, ha="center")
    text(ax, .05, y+.11, label, 13.6, color=col, weight=True)
    text(ax, .05, y-.19, sub, 11.8, color=MUTED)
    coords(ax, 8.35, y+.05, n, col, mult=="m = ∞")
    text(ax, 10.17, y-.015, mult, 14, color=col, weight=True)
y=rows[0][0]
ax.vlines(convert(1.5), y, y+.36, color=ATOM, linewidth=2)
ax.scatter([convert(1.5)],[y+.36],s=64,c=ATOM,zorder=4)
text(ax, convert(1.5), y+.51, "mass 1", 11.2, color=ATOM, ha="center")
y=rows[1][0]
ax.add_patch(Rectangle((x0,y+.02), x1-x0, .23, facecolor=AC, alpha=.19))
ax.plot([x0,x1],[y+.25,y+.25],color=AC,lw=2)
text(ax, (x0+x1)/2, y+.38, "density 1 on [1, 2]", 11.2, color=AC, ha="center")
y=rows[2][0]
for u,v in cantor_intervals(D["cantor"]["drawn_level"]):
    ax.add_patch(Rectangle((convert(u),y+.015),convert(v)-convert(u),.25,
                           facecolor=CANTOR,edgecolor="none"))
text(ax, (x0+x1)/2, y+.41, "level-5 support cover; no Lebesgue density", 10.7, color=CANTOR, ha="center")
text(ax, .05, 2.30, "All three measures are mutually singular  ⇒  their bidual support projections are orthogonal.", 12.3, weight=True)
ax.plot([.05,12.8],[2.02,2.02],color="#d2dbe1",lw=1)
text(ax, .05, 1.65, "On the same measure class:", 13, weight=True)
text(ax, .05, 1.27, "the first two coordinates embed isometrically.", 11.6, color=MUTED)
coords(ax, 5.23, 1.39, 2, AC)
coords(ax, 8.25, 1.39, 3, AC)
arrow(ax, (6.05,1.39),(7.78,1.39),AC)
text(ax, 6.94, 1.70, "J : ℂ² → ℂ³", 13, color=AC, ha="center")
text(ax, 6.94, .99, "J(z₁,z₂) = (z₁,z₂,0)", 12.2, color=AC, ha="center")
text(ax, 10.00, 1.43, "No reverse", 12.3, color=ATOM, weight=True)
text(ax, 10.00, 1.11, "isometry ℂ³ → ℂ²", 11.8, color=ATOM)
text(ax, .05, .50, "Comparison also includes the square-root change of measure. Infinite fibers remove only the dimension constraint.", 11.4, color=MUTED)
text(ax, .05, .12, "Proof: SM12–SM18, SM22–SM23. Cantor law: 1 + Σⱼ 2εⱼ3⁻ʲ, independent fair bits εⱼ.", 10.3, color=MUTED)
save(fig,"measure-multiplicity")

fig, ax = base()
text(ax, .05, 7.30, "Negative spectral dilation; two different continuity tests", 20.4, weight=True)
text(ax, .05, 6.86, "Spectral points move by t ↦ exp(−s)t. Functions pull back by f(t) ↦ f(exp(s)t).", 12.5, color=MUTED)
# Upper geometric panel.
text(ax, .05, 6.26, "EXACT MOVEMENT AT s = log 2", 11.2, weight=True)
ax.plot([3.35,9.00],[5.48,5.48],color=MUTED,lw=1.3)
for t,x in [(1,4.0),(2,8.25)]:
    ax.scatter([x],[5.48],s=68,c=ATOM,zorder=4)
    text(ax,x,5.10,"t = "+str(t),12.8,ha="center",color=ATOM)
arrow(ax,(8.17,5.81),(4.08,5.81),ATOM,scale=17)
text(ax,6.15,6.08,"2 ↦ 1",14.5,ha="center",color=ATOM,weight=True)
text(ax,9.5,5.79,"u = log t",12.9,weight=True)
text(ax,9.5,5.39,"log 2 ↦ 0",13,color=ATOM)
text(ax,.05,5.68,"rₛ(t) = e⁻ˢt",17,color=ATOM,weight=True)
text(ax,.05,5.21,"weight: φ ↦ e⁻ˢφ",12.1,color=MUTED)
ax.plot([.05,12.8],[4.76,4.76],color="#d2dbe1",lw=1)
# Exact scalar graphs. Draw axes manually to avoid hidden font fallback.
text(ax,.08,4.34,"ENTIRE GLOBAL CARRIER",12.5,weight=True,color=ATOM)
text(ax,7.10,4.34,"LEBESGUE CORNER",12.5,weight=True,color=AC)
text(ax,.08,3.99,"ωₐ(Θₛ(pδₐ)) = 1 if s = 0; otherwise 0",11.9,color=ATOM)
text(ax,7.10,3.99,"ω(Θₛ(1[0,1])) = max(1 − |s|, 0)",11.9,color=AC)
for left, width, color, mode in [(0.65,4.6,ATOM,"point"),(7.63,4.6,AC,"triangle")]:
    y0, height, bound = 1.62, 1.58, 1.5
    sx=lambda s:left+width*(s+bound)/(2*bound)
    sy=lambda val:y0+height*val
    arrow(ax,(left-.15,y0),(left+width+.25,y0),MUTED,scale=9)
    arrow(ax,(sx(0),y0-.16),(sx(0),sy(1)+.22),MUTED,scale=9)
    for s,label in [(-1,"−1"),(0,"0"),(1,"1")]:
        ax.plot([sx(s),sx(s)],[y0-.05,y0+.05],color=MUTED,lw=1)
        text(ax,sx(s),y0-.28,label,11,ha="center",color=MUTED)
    text(ax,left+width+.18,y0-.28,"s",11.5,color=MUTED)
    text(ax,sx(0)-.15,sy(1),"1",11,ha="right",va="center",color=MUTED)
    if mode=="point":
        ax.plot([sx(-bound),sx(-.035)],[y0,y0],color=color,lw=3)
        ax.plot([sx(.035),sx(bound)],[y0,y0],color=color,lw=3)
        ax.scatter([sx(0)],[y0],s=75,facecolors="white",edgecolors=color,linewidths=2,zorder=7)
        ax.scatter([sx(0)],[sy(1)],s=65,c=color,zorder=7)
    else:
        points=[(-bound,0),(-1,0),(0,1),(1,0),(bound,0)]
        ax.plot([sx(s) for s,v in points],[sy(v) for s,v in points],color=color,lw=2.6)
text(ax,.08,.92,"The normal point test jumps at zero.",12.5,weight=True,color=ATOM)
text(ax,.08,.56,"No connecting curve is part of this function.",11.2,color=MUTED)
text(ax,7.10,.92,"Translation is σ-strong* continuous.",12.1,weight=True,color=AC)
text(ax,7.10,.56,"ω(f) = ∫₀¹ f(u)du; the graph is overlap length.",11.2,color=MUTED)
text(ax,.08,.12,"Proof: SM31–SM36. The Lebesgue corner is a proper central summand of C₀((0,∞))**.",10.5,color=MUTED)
save(fig,"carrier-scaling")

# Verify exact combinatorial and scalar model constraints without modifying data.
assert len(cantor_intervals(D["cantor"]["drawn_level"])) == 2**D["cantor"]["drawn_level"]
assert abs(sum(v-u for u,v in cantor_intervals(5))-(2/3)**5)<1e-12
assert math.isclose(2*math.exp(-math.log(2)),1)
assert D["fibers"]["source_dimension"] <= D["fibers"]["target_dimension"]
assert D["global_test"]["value_at_zero"]==1 and D["global_test"]["value_elsewhere"]==0
for name in ("measure-multiplicity","carrier-scaling"):
    for ext in ("svg","png"):
        p=OUT/(name+"."+ext)
        print(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size)
