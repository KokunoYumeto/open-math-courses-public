"""Reproduce the endpoint/frame diagram and exact coefficient checks.

This is an explanatory schematic, not a picture of the whole base K.
Proof locators: workflow-odd-clutch-binding.md, O1-O5.
"""
from pathlib import Path
from math import factorial
import json
import sympy as s
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]/'public/assets'
a, c, sn = s.symbols("a c sn", nonzero=True)
R = s.Matrix([[c, -sn], [sn, c]])
W = s.diag(a, 1) * R * s.diag(1/a, 1) * R.T
assert W.subs({c: 1, sn: 0}) == s.eye(2)
assert W.subs({c: 0, sn: 1}) == s.diag(a, 1/a)
assert s.simplify(W.subs(a, 1) - (c*c + sn*sn)*s.eye(2)) == s.zeros(2)
z = s.symbols("z")
checks = []
for m in range(9):
    beta = s.integrate(z**m * (1-z)**m, (z, 0, 1))
    assert beta == s.Rational(factorial(m)**2, factorial(2*m+1))
    # geometric (-1)^(m+1), interval minus, and (f^2-f)^m sign
    sign = (-1)**(m+1) * (-1) * (-1)**m
    coefficient = s.Rational(sign*(m+1), factorial(m+1))*beta
    assert coefficient == s.Rational(factorial(m), factorial(2*m+1))
    checks.append({"m": m, "beta": str(beta), "positive_coefficient": str(coefficient)})

navy, blue, teal, red = "#16304b", "#245b88", "#147d78", "#b54d45"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "mathtext.fontset": "dejavusans"})
fig = plt.figure(figsize=(15, 9), facecolor="#fbfcfe")
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 15); ax.set_ylim(0, 9); ax.axis("off")
def txt(x, y, t, size=13, color=navy, **kw):
    return ax.text(x, y, t, fontsize=size, color=color, va="center", **kw)
def arrow(x0, y0, x1, y1, color=blue, style="-|>", scale=17, lw=2, **kw):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style,
                               mutation_scale=scale, linewidth=lw, color=color, **kw))

txt(.6, 8.5, "One frame calculation fixes the entire suspension sign", 23, weight="bold")
txt(.6, 8.0, r"$p=jj^*,\quad W_0=1,\quad W_1=\mathrm{diag}(a,a^{-1}),\quad q_t=W_tj$", 17)
txt(.6, 7.5, "The interval is first and oriented by increasing t. The drawings of K are schematic.", 12)

for y, label, aval, clutch, result, color in [
    (5.05, "Blackadar's map", r"a=u", r"u", r"\theta([u])", blue),
    (2.5, "The course's positive map", r"a=u^{-1}", r"u^{-1}",
     r"\theta([u^{-1}])=-\theta([u])", teal)]:
    txt(.6, y+1.78, label, 16, color, weight="bold")
    ax.add_patch(Rectangle((.7, y), 7.15, 1.1, facecolor="#e9f1f8", edgecolor=color, linewidth=1.7))
    ax.plot([.7, .7], [y, y+1.1], color=color, linewidth=4)
    ax.plot([7.85, 7.85], [y, y+1.1], color=color, linewidth=4)
    txt(.9, y+.72, r"$q_0v=jv$", 14)
    txt(5.45, y+.72, rf"$q_1v=j({clutch}v)$", 14)
    arrow(2.3, y+.38, 6.2, y+.38, color)
    txt(3.25, y+.72, rf"${aval}$", 15, color)
    txt(.65, y-.3, r"$t=0$", 12)
    txt(7.3, y-.3, r"$t=1$", 12)
    arrow(7.7, y+1.24, .9, y+1.24, color, connectionstyle="arc3,rad=0.09")
    txt(3.45, y+1.13, rf"end to start: $v\mapsto {clutch}v$", 12, color,
        bbox={"facecolor": "#fbfcfe", "edgecolor": "none", "pad": 2})
    txt(8.5, y+.9, rf"$(1,x,v)\sim(0,x,{clutch}v)$", 15, color)
    txt(8.5, y+.38, rf"${result}$", 17, color)
    if aval == r"a=u^{-1}":
        txt(8.5, y-.15, r"$\mathrm{ch}_{\mathrm{odd}}^+(u)=-\sigma^{-1}\mathrm{ch}(\theta[u])$", 15)

txt(.65, 1.65, r"Relative safeguard: $B=(\{0\}\times K)\cup(S^1\times L)$ has the fixed frame $j$.", 13)
txt(.65, 1.18, r"$u|_L=1\ \Longrightarrow\ W_t|_L=1,\ e|_B=p;\quad (S^1\times K)/B=S^1\wedge(K/L).$", 14)
txt(.65, .65, r"All degrees: $\sigma^{-1}\mathrm{ch}_{2m+2}(\theta[u^{-1}])="
    r"\frac{m!}{(2m+1)!(2\pi i)^{m+1}}[\mathrm{Tr}(u^{-1}du)^{2m+1}]$.", 15)
txt(.65, .17, "Proof: O1-O5. Human sources: Blackadar 8.2.2 (pp. 61-62); Atiyah-Hirzebruch 1.10 (p. 206).", 10)

fig.savefig(ROOT / "workflow-odd-clutch-frame.png", dpi=150, bbox_inches="tight", pad_inches=.08)
fig.savefig(ROOT / "workflow-odd-clutch-frame.svg", bbox_inches="tight", pad_inches=.08)
plt.close(fig)
(ROOT / "workflow-odd-clutch-exact-checks.json").write_text(json.dumps({
    "checks": checks,
    "endpoint_identity": "W_0=1; W_1=diag(a,a^-1); W_t(1)=1",
    "interpretation": "Arithmetic and endpoint corroboration; not a substitute for the all-degree proof."
}, indent=2)+"\n", encoding="utf-8")
print("Endpoint identities and m=0,...,8 beta/coefficient checks passed; frame PNG/SVG rendered.")
