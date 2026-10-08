"""Render the exact stable-range diagram. Run: python render.py

No sampled proof claim is made. Coordinates and sign checks use Fraction;
SymPy verifies the finite-matrix diagnostic when available.
The SVG uses embedded font paths and deterministic metadata.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import hashlib
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))

def floor(x):
    return x.numerator // x.denominator

def frac(x):
    return x - floor(x)

u, s, t = (F(DATA["sign_test"][k]) for k in ("u", "s", "t"))
wrong = lambda x, a: floor(x + 2*a) - floor(x + a)
correct = lambda x, a: -floor(x-a)
assert [wrong(u,s+t), wrong(u,s)+wrong(frac(u-s),t)] == [1,0]
assert [correct(u,s+t), correct(u,s)+correct(frac(u-s),t)] == [1,1]
roof = F(DATA["deck"]["roof_at_omega"])
height = F(DATA["deck"]["height"])
assert height - roof == F(DATA["deck"]["height_after_deck"])
assert 0 <= height-roof < F(DATA["deck"]["roof_at_Tomega"])
assert DATA["deck"]["cover_before"] - 1 == DATA["deck"]["cover_after"]

# Exact rational diagnostics; the manuscript proves the all-parameter law.
checked = 0
for a in (F(j,17) for j in range(17)):
    for b in (F(j,7) for j in range(-9,10)):
        for c in (F(j,11) for j in range(-9,10)):
            assert floor(a+b+c) == floor(frac(a+c)+b)+floor(a+c)
            assert correct(a,b+c) == correct(a,b)+correct(frac(a-b),c)
            checked += 1

matrix_checked = False
try:
    import sympy as sp
    I = sp.eye(2)
    X = sp.Matrix([[0,1],[1,0]])
    Y = sp.Matrix([[0,-sp.I],[sp.I,0]])
    Z = sp.diag(1,-1)
    V, W = (I+sp.I*X)/sp.sqrt(2), (I+sp.I*Z)/sp.sqrt(2)
    e = (I+Z)/2
    assert sp.simplify(W*V*e*V.adjoint()*W.adjoint()-(I+X)/2) == sp.zeros(2)
    assert sp.simplify(V*W*e*W.adjoint()*V.adjoint()-(I+Y)/2) == sp.zeros(2)
    matrix_checked = True
except ImportError:
    pass

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "font.size": 12,
    "svg.fonttype": "path",
    "svg.hashsalt": "oa-flow-stable-range-original-v1",
})
INK, BLUE, ORANGE, GREEN, RED = "#172b46", "#24609b", "#b56a14", "#19735f", "#a4363f"
PALE, GRID = "#f4f7fb", "#cbd6e3"
fig = plt.figure(figsize=(18,12), facecolor="white")
fig.text(.04,.958,"Stable ranges: the full algebra and the correct signs",
         size=24, weight="bold", color=INK)
fig.text(.04,.924,
         "Exact cover coordinates, normal regular models, and the Hilbert-space density",
         size=13, color="#42536b")
axes = [fig.add_axes(b) for b in [(.04,.49,.44,.395),(.52,.49,.44,.395),
                                 (.04,.075,.44,.36),(.52,.075,.44,.36)]]

def panel(ax, title):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle="round,pad=0.008,rounding_size=.018",
                              facecolor=PALE,edgecolor=GRID,lw=1))
    ax.text(.035,.93,title,size=16,weight="bold",color=INK,va="top")

def arrow(ax, start, end, color=BLUE, lw=2):
    ax.annotate("",xy=end,xytext=start,
                arrowprops=dict(arrowstyle="-|>",color=color,lw=lw,
                                mutation_scale=14,shrinkA=0,shrinkB=0))

def node(ax, x, y, label, width=.28, height=.14, size=13):
    ax.add_patch(FancyBboxPatch((x-width/2,y-height/2),width,height,
                              boxstyle="round,pad=.005,rounding_size=.012",
                              facecolor="white",edgecolor=BLUE,lw=1.5))
    ax.text(x,y,label,ha="center",va="center",color=INK,size=size)

ax=axes[0]
panel(ax,"A  One deck step, two lifts of the same point")
Xmap=lambda q:.20+.16*float(q)
for yy,rr,lab in [(.65,roof,r"$\omega$"),(.32,F(DATA["deck"]["roof_at_Tomega"]),r"$T\omega$")]:
    ax.add_patch(Rectangle((Xmap(0),yy-.036),Xmap(rr)-Xmap(0),.072,
                           facecolor="#dfeaf5",edgecolor="none"))
    arrow(ax,(Xmap(-F(1,5)),yy),(Xmap(F(17,4)),yy),BLUE,1.3)
    ax.text(.06,yy,lab,va="center",color=INK,size=15)
    for val in [F(0),rr]:
        ax.plot([Xmap(val)]*2,[yy-.055,yy+.055],color=BLUE,lw=1)
    ax.text(Xmap(0),yy-.09,"0",ha="center",color=BLUE)
    ax.text(Xmap(rr),yy-.09,("3/2" if rr==roof else "2"),ha="center",color=BLUE)
ax.plot(Xmap(height),.65,"o",ms=9,color=ORANGE)
ax.plot(Xmap(height-roof),.32,"o",ms=9,color=ORANGE)
ax.text(Xmap(height)+.015,.70,r"$s=9/4,\quad\Phi(s,\omega)=(1,y)$",
        color=INK,size=12,ha="left")
ax.text(Xmap(height-roof)+.115,.40,r"$s_1=3/4,\quad\Phi(s_1,T\omega)=(0,y)$",
        color=INK,size=12,ha="left")
arrow(ax,(Xmap(height)-.012,.625),(Xmap(height-roof)+.012,.347),ORANGE,2.4)
ax.text(.14,.49,r"$s_1=s-3/2$",color=ORANGE,size=13,
        bbox=dict(facecolor=PALE,edgecolor="none",pad=2))
ax.text(.035,.12,r"$B(s,\omega)=(s-r(\omega),T\omega)$",color=INK,size=14)
ax.text(.035,.06,"Half-open shading = roof strips; local points on an aperiodic base.",
        color="#52627a",size=10.5)
ax.text(.035,.017,"Proof: SR8–SR10; Diagnostic 2.",color="#52627a",size=10)

ax=axes[1]
panel(ax,"B  Normal onto maps, with normal inverses")
xs=[.16,.50,.84]
top=[r"$Q$",r"$R=Q\rtimes\mathbb{R}$",r"$R\rtimes_\chi\mathbb{Z}$"]
bot=[r"$L^\infty(\mathbb{R})\,\bar\otimes\,Q_0$",
     r"$B(L^2\mathbb{R})\,\bar\otimes\,Q_0$",
     "$B(\\ell^2\\mathbb{Z})$\n"+r"$\bar\otimes\,(P\rtimes_\theta\mathbb{R})$"]
for xx,aa,bb in zip(xs,top,bot):
    node(ax,xx,.70,aa,size=13)
    node(ax,xx,.37,bb,size=11.7,height=.17)
    arrow(ax,(xx,.614),(xx,.477),GREEN)
    ax.text(xx+.025,.544,r"$\cong$",color=GREEN,size=15,va="center")
for k,label in [(0,r"$\rtimes\mathbb{R}$"),(1,r"$\rtimes\mathbb{Z}$")]:
    arrow(ax,(xs[k]+.147,.70),(xs[k+1]-.147,.70),BLUE,1.4)
    ax.text((xs[k]+xs[k+1])/2,.815,label,size=12,color=BLUE,ha="center")
ax.text(.035,.245,"P, Q, Q₀ and R have the same coarse type (SR31–SR33).",size=10.5,color=GREEN)
ax.text(.035,.19,r"$d_1\mapsto D_1,\qquad D_1\delta_m=\delta_{m-1}$",size=12.5,color=INK)
ax.text(.035,.125,r"$\lambda_t^\gamma\mapsto U_t\lambda_t^0,\qquad"
        r"U_t(z)=S_{n(t,S_{-t}z)}$",size=13,color=INK)
ax.text(.035,.067,r"$Z(R)=Z(Q_0)=L^\infty(\Omega),\quad \chi|_Z:f\mapsto f\circ T^{-1}$",
        size=11.5,color=INK)
ax.text(.035,.015,"Proof: AC3, AC6–AC7; SR19–SR33. Horizontal arrows mean “cross by”.",
        size=10,color="#52627a")

ax=axes[2]
panel(ax,"C  The inverse base point is essential")
ax.text(.035,.79,r"$u=13/100,\qquad s=1/5,\qquad t=2/5$",size=14,color=INK)
ax.text(.035,.68,r"$a_t(u)=\lfloor u+2t\rfloor-\lfloor u+t\rfloor$",size=13,color=RED)
ax.text(.035,.58,r"$b_t(u)=-\lfloor u-t\rfloor$",size=13,color=GREEN)
cx=[.20,.58,.84]
ax.text(cx[0],.45,"Exponent",ha="center",weight="bold",color=INK)
ax.text(cx[1],.45,r"$c_{s+t}(u)$",ha="center",weight="bold",color=INK)
ax.text(cx[2],.45,r"$c_s(u)+c_t(\{u-s\})$",ha="center",size=11.8,color=INK)
ax.plot([.04,.96],[.408,.408],color=GRID)
for yy,label,left,right,col in [(.32,"Wrong:  "+r"$c=a$",1,0,RED),
                               (.22,"Correct: "+r"$c=b$",1,1,GREEN)]:
    ax.text(cx[0],yy,label,ha="center",color=col,size=13)
    ax.text(cx[1],yy,str(left),ha="center",color=col,size=16,weight="bold")
    ax.text(cx[2],yy,str(right),ha="center",color=col,size=16,weight="bold")
ax.text(.035,.10,"Every wrap also transports the aperiodic base by T.",size=11,color="#52627a")
ax.text(.035,.027,"Proof: AC10; Diagnostic 3. All numbers are exact rational calculations.",
        size=10,color="#52627a")

ax=axes[3]
panel(ax,"D  Affine Haar measure: where the density belongs")
ax.text(.035,.80,r"$(a,b)(a_1,b_1)=(aa_1,\,b+ab_1),\qquad a,a_1>0$",size=13,color=INK)
ax.text(.035,.68,r"$dh=a^{-2}\,da\,db,\qquad \Delta_H(a,b)=a^{-1}$",size=14,color=INK)
ax.text(.035,.55,r"$h(e^t,0)=(ae^t,b),\qquad"
        r"\int|\xi(ae^t,b)|^2\,dh=e^t\|\xi\|^2$",size=12.8,color=ORANGE)
ax.text(.035,.405,"Unitary on vectors",color=GREEN,weight="bold",size=12)
ax.text(.43,.405,r"$\xi(a,b)\mapsto e^{-t/2}\xi(ae^t,b)$",color=GREEN,size=13)
ax.text(.035,.285,"Algebra pullback",color=BLUE,weight="bold",size=12)
ax.text(.43,.285,r"$f(a,b)\mapsto f(ae^t,b)$",color=BLUE,size=13)
ax.text(.035,.14,"The scalar factor cancels in conjugation; the algebra action is unital.",
        color="#52627a",size=11)
ax.text(.035,.027,"Proof: SR3, SR6, SR39–SR41; Diagnostic 4.",size=10,color="#52627a")

fig.text(.04,.028,"Original exact diagram • Proofs: From a central cocycle to a full return algebra",
         size=11,color="#42536b")
fig.savefig(ROOT/"stable-range.png",dpi=160,facecolor="white",
            metadata={"Software":"Matplotlib; original stable-range diagram"})
fig.savefig(ROOT/"stable-range.svg",facecolor="white",
            metadata={"Date":None,"Creator":"Original stable-range diagram",
                      "Title":"Stable ranges: full algebra and correct signs"})
plt.close(fig)
glyph_ids = re.findall(r'<path id="([^"]+)"',
                       (ROOT/"stable-range.svg").read_text(encoding="utf-8"))
font_components = sorted({name.rsplit("-",1)[0] for name in glyph_ids if "-" in name})
assert all(name.startswith(("DejaVu","STIX")) for name in font_components), font_components
print(json.dumps({
    "fraction_grid_cases":checked,
    "exact_matrix_order_check":matrix_checked,
    "matplotlib":matplotlib.__version__,
    "svg_font_components":font_components,
    "outputs":{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
               for name in ("stable-range.png","stable-range.svg")}
},indent=2))
