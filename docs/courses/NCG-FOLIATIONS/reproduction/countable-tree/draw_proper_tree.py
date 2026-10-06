"""Original exact mathematical diagram for PT.1--PT.28; CC0 1.0."""
from pathlib import Path
import json
import html
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

SOURCE_DIR = Path(__file__).resolve().parent
OUT = SOURCE_DIR.parent.parent / 'figures'
OUT.mkdir(parents=True, exist_ok=True)
FONT_DIR = SOURCE_DIR / 'fonts'
font_names = {'DejaVu Sans','DejaVu Sans Display','DejaVu Sans Mono','STIXGeneral','STIXNonUnicode','STIXSizeOneSym','STIXSizeTwoSym','STIXSizeThreeSym','STIXSizeFourSym','STIXSizeFiveSym'}
font_manager.fontManager.ttflist[:] = [f for f in font_manager.fontManager.ttflist if f.name not in font_names]
for font_path in sorted(FONT_DIR.glob('*.ttf')):
    font_manager.fontManager.addfont(str(font_path))
plt.rcParams.update({'svg.fonttype':'path','mathtext.fontset':'dejavusans'})
font_notices = '\n\n'.join((FONT_DIR/n).read_text(encoding='utf-8') for n in ['LICENSE_DEJAVU.txt','LICENSE_STIX.txt'])
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                     "svg.hashsalt": "proper-tree-normal-inverse-20261005"})
fig = plt.figure(figsize=(15, 8), facecolor="#f7f8fb", layout="constrained")
gs = fig.add_gridspec(2, 3, height_ratios=[1, .85])
ax = fig.add_subplot(gs[:, 0])
ax.set_title("The root keeps the full normal Dirac", fontsize=13, loc="left")
ax.set_xlim(-1.85, 1.85)
ax.set_ylim(-2.15, 2.0)
ax.set_aspect("equal")
ax.axis("off")
root = (0, 0)
pos = {"e": root}
letters = ["a", "b", "A", "B"]
inverse = {"a": "A", "A": "a", "b": "B", "B": "b"}
for i, letter in enumerate(letters):
    angle = math.pi/4+i*math.pi/2
    pos[letter] = (0.88*math.cos(angle), 0.88*math.sin(angle))
    available = [s for s in letters if s != inverse[letter]]
    for j, s in enumerate(available):
        a = angle+(j-1)*0.36
        pos[letter+s] = (1.58*math.cos(a), 1.58*math.sin(a))
for word, xy in pos.items():
    if word == "e":
        continue
    parent = "e" if len(word) == 1 else word[:-1]
    p = pos[parent]
    ax.plot([p[0], xy[0]], [p[1], xy[1]], color="#576b85", lw=1.3, zorder=0)
    mid = ((p[0]+xy[0])/2, (p[1]+xy[1])/2)
    ax.scatter(*mid, marker="s", s=27, color="#df9550", zorder=2)
    start = ((2*xy[0]+p[0])/3, (2*xy[1]+p[1])/3)
    ax.annotate("", xy=mid, xytext=start,
                arrowprops={"arrowstyle": "->", "color": "#237a5b", "lw": 1.1})
for word, xy in pos.items():
    ax.scatter(*xy, s=75 if word == "e" else 43,
               color="#bb4068" if word == "e" else "#346aa0", zorder=3)
    displacement = .115 if word != "e" else .19
    ax.text(xy[0], xy[1]+displacement, word, ha="center", va="bottom", fontsize=9)
ax.text(0, -1.88, "A = a inverse; B = b inverse\n"
        "Blue vertices (+) pair to orange parent edges (−).\n"
        "Radius two is shown; the tree is infinite.",
        ha="center", va="top", fontsize=9, linespacing=1.5)

av = fig.add_subplot(gs[0, 1])
av.axis("off")
av.set_title("Finite stabilizers give a literal reduced embedding", fontsize=12, loc="left")
av.text(.02, .88, r"$\Gamma=F_2\times C_2,\quad H=C_2=\{1,c\}$", fontsize=12)
av.text(.02, .66, r"$J\delta_g=(\delta_{(g,1)}+\delta_{(g,c)})/\sqrt{2}$", fontsize=13)
av.text(.02, .43, "Two orthogonal regular vectors, one unit vector.\n"
        "Left translation intertwines exactly.\n"
        "Normal transport stays in the coefficient.", fontsize=11, linespacing=1.8)
av.text(.02, .09, r"$Q^*Q=1-P_o,\quad QQ^*=1,\quad \mathrm{Index}\,Q=+1$",
        fontsize=12, bbox={"boxstyle": "round,pad=.5", "fc": "#edf4f0", "ec": "#a5c5b6"})

ap = fig.add_subplot(gs[0, 2])
ap.axis("off")
ap.set_title("The whole inverse phase and sign survive", fontsize=12, loc="left")
ap.text(.02, .88, r"$zs\ \longmapsto\ z^{-1}\rho_t(s)$", fontsize=16)
ap.text(.02, .65, r"$q=4,\quad k_q=6,\quad\mathcal{D}_N=C_4,\quad c_j=-L_{t_j}$", fontsize=12)
ap.text(.02, .42, r"$z=(-1)^\epsilon:\quad z^2=1,\quad z^{-1}=z$", fontsize=14)
ap.text(.02, .20, "The determinant is trivial in this example.\n"
        "The specified central sign still acts on spinors.\n"
        "The tree factor is even: normal degree stays four.",
        fontsize=11, linespacing=1.8)

asp = fig.add_subplot(gs[1, 1])
nu = np.linspace(-4, 4, 401)
for n, col in [(1, "#356fa7"), (2, "#ca823e")]:
    eig = np.sqrt(nu*nu+n*n)
    asp.plot(nu, eig, color=col, label=f"depth n = {n}")
    asp.plot(nu, -eig, color=col)
asp.plot(nu, nu, color="#bb4068", lw=2, ls="--", label="root: normal eigenvalue ν")
asp.set_xlabel("Normal eigenvalue parameter ν")
asp.set_ylabel("Exact product block eigenvalues")
asp.set_title(r"Nonroot blocks: $\pm\sqrt{\nu^2+n^2}$", fontsize=12, loc="left")
asp.grid(alpha=.17)
asp.legend(fontsize=8, frameon=False, loc="upper left")
asp.text(.02, .03, "Parameter curves; no normal spectrum is sampled.",
         transform=asp.transAxes, fontsize=8,
         bbox={"fc":"white", "ec":"none", "alpha":.85})

ac = fig.add_subplot(gs[1, 2])
ac.axis("off")
ac.set_title("The original Bott class has pairing one", fontsize=12, loc="left")
ac.text(.02, .87, r"$E^*\ \to\ pA:\quad \overline{\eta}\mapsto\theta_{\xi,\eta}$", fontsize=14)
ac.text(.02, .64, "Normalized plaque bump and counting norm: 1.\n"
        "Tree creation connections and positivity are checked.", fontsize=11, linespacing=1.8)
ac.text(.02, .40, r"$[\Pi_B,F_B]|_{C(N)}=[D_N],\qquad(i_*b_U)z_G=1$", fontsize=12)
ac.text(.02, .15, "Proved for the stated proper-tree family.\n"
        "General return groupoids and a local differential\n"
        "replacement for the discrete tree term remain open.",
        fontsize=11, linespacing=1.8, color="#654b45")
fig.suptitle("A reduced graph-column completion with finite tree stabilizers", fontsize=17, x=.03, ha="left")
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
fb = fig.bbox
outside=[]
texts=fig.findobj(match=matplotlib.text.Text)
hidden_ticks={id(t) for axis in fig.axes if not axis.axison
              for t in axis.get_xticklabels()+axis.get_yticklabels()}
checked_texts=0
for t in texts:
    if not t.get_visible() or not t.get_text() or id(t) in hidden_ticks:
        continue
    checked_texts+=1
    b=t.get_window_extent(renderer)
    if b.x0 < fb.x0-1 or b.y0 < fb.y0-1 or b.x1 > fb.x1+1 or b.y1 > fb.y1+1:
        outside.append(t.get_text())
fig.savefig(OUT/"kt-proper-tree-normal-inverse.png", dpi=150, metadata={"Software":"Original programme diagram; CC0 1.0"})
fig.savefig(OUT/"kt-proper-tree-normal-inverse.svg", metadata={"Date":None,"Creator":"Original programme diagram; CC0 1.0"})
(SOURCE_DIR/"FIGURE-BOUNDS.json").write_text(json.dumps({"checked_texts":checked_texts,"outside_figure":outside,"objects":"exact radius-two F2 tree, finite C2 coset average, full rank-four inverse signs, exact parameter block curves; no spectrum or infinite-tail numerical proof"},indent=2)+"\n",encoding="utf-8")
assert not outside, outside

# Exact actual glyph licences accompany the outlined SVG.
svg_path = OUT / 'kt-proper-tree-normal-inverse.svg'
svg_text = svg_path.read_text(encoding='utf-8')
svg_text = svg_text.replace('</metadata>', '</metadata>\n <desc id="font-notices">'+html.escape(font_notices)+'</desc>', 1)
svg_path.write_text(svg_text, encoding='utf-8', newline='\n')
plt.close(fig)
