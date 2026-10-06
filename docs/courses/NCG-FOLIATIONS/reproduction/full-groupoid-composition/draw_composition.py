"""Full-arrow composition and exact finite cyclic-label mass cancellation.

Original expression CC0-1.0; unmodified bundled font terms fully embedded.
"""
from pathlib import Path
import argparse
import os
import tempfile

HERE=Path(__file__).resolve().parent
CACHE=tempfile.TemporaryDirectory(prefix="full-groupoid-composition-")
os.environ["MPLCONFIGDIR"]=CACHE.name
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyArrowPatch, Rectangle

ap=argparse.ArgumentParser()
ap.add_argument("--output-dir",type=Path,default=HERE.parents[1]/"figures")
out=ap.parse_args().output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
REG=FontProperties(fname=str(HERE/"fonts/DejaVuSans.ttf"))
BOLD=FontProperties(fname=str(HERE/"fonts/DejaVuSans-Bold.ttf"))
plt.rcParams.update({"svg.fonttype":"path","svg.hashsalt":"full-groupoid-composition-20261006"})
INK,BLUE,GREEN,RED="#223647","#2865a5","#26785b","#b6404b"
fig,axes=plt.subplots(2,2,figsize=(16,10.4))
fig.patch.set_facecolor("white")
def label(a,x,y,s,size=11,bold=False,color=INK,ha="center"):
    return a.text(x,y,s,fontsize=size,fontproperties=BOLD if bold else REG,
                  color=color,ha=ha,va="center",transform=a.transAxes,
                  linespacing=1.30,zorder=10)
def arrow(a,p,q,color=BLUE,curve=0):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=16,
             linewidth=2,color=color,transform=a.transAxes,
             connectionstyle="arc3,rad="+str(curve)))
for a in axes.flat:
    a.set_xlim(0,1);a.set_ylim(0,1);a.axis("off")

a=axes[0,0]
label(a,.5,.95,"A. The arrows have three different types",14,True)
label(a,.10,.73,"H:",12,True)
label(a,.46,.73,"b",13,True);label(a,.89,.73,"F(a)",13,True)
arrow(a,(.50,.73),(.81,.73));label(a,.66,.82,"η : b → F(a)",11,True,BLUE)
arrow(a,(.46,.66),(.46,.48),GREEN);arrow(a,(.89,.66),(.89,.48),GREEN)
label(a,.39,.565,"P",11,True,GREEN);label(a,.82,.565,"P",11,True,GREEN)
label(a,.10,.405,"K:",12,True)
label(a,.23,.405,"c",13,True);label(a,.46,.405,"P(b)",13,True)
label(a,.89,.405,"PF(a)",13,True)
arrow(a,(.27,.405),(.395,.405));label(a,.33,.49,"ρ",12,True,BLUE)
arrow(a,(.535,.405),(.81,.405));label(a,.66,.49,"Pη",12,True,BLUE)
arrow(a,(.23,.35),(.89,.35),RED,curve=.45)
label(a,.55,.16,"α = Pη ρ : c → PF(a)",12,True,RED)
label(a,.5,.04,"(Pη)⁻¹α : c → P(b) belongs to the g cutoff space.",10)

a=axes[0,1]
label(a,.5,.95,"B. Every intermediate cyclic label is retained",14,True)
label(a,.5,.85,"F : Z × C₂ → Z × C₄,     F(k,u) = (2k,0)",12)
label(a,.5,.745,"η = (ℓ,v),     f(ℓ,v) = 1/2 on ℓ = 0,1",11,True)
for j in range(4):
    label(a,.15+.21*j,.65,"v = "+str(j),10)
for ell in range(2):
    y=.525-.17*ell
    label(a,.025,y,"ℓ = "+str(ell),10,ha="left")
    for j in range(4):
        x=.15+.21*j
        a.add_patch(Rectangle((x-.073,y-.055),.146,.11,
                     facecolor="#ecf4fa",edgecolor=BLUE,transform=a.transAxes))
        label(a,x,y,"1/2",12,True,BLUE)
label(a,.5,.195,"Eight supported arrows: total mass 8 × 1/2 = 4.",12,True)
label(a,.5,.075,"C_F f = 2 × (1/2) = 1 on each action orbit.\nTwo source kernel labels repeat each transporter.",10)

a=axes[1,0]
label(a,.5,.95,"C. Four equal contributions at each composite label",14,True)
label(a,.5,.84,"P : Z × C₄ → Z,     P(ℓ,v) = 3ℓ",12)
label(a,.16,.705,"g(ρ):",11,True)
for j in range(3):
    x=.40+.20*j
    a.add_patch(Rectangle((x-.072,.65),.144,.11,
                 facecolor="#edf7f1",edgecolor=GREEN,transform=a.transAxes))
    label(a,x,.705,"1/4",12,True,GREEN)
    label(a,x,.60,str(j),10)
label(a,.5,.52,"ρ = 0,1,2; total 3/4.      C_P g = 4 × (1/4) = 1.",10)
label(a,.09,.375,"h(α):",11,True)
for j in range(6):
    x=.23+.13*j
    a.add_patch(Rectangle((x-.050,.32),.10,.11,
                 facecolor="#fff1f1",edgecolor=RED,transform=a.transAxes))
    label(a,x,.375,"1/2",11,True,RED);label(a,x,.27,str(j),10)
label(a,.5,.175,"α = 3ℓ+ρ; each α receives 4 × (1/2)(1/4) = 1/2.",11,True)
label(a,.5,.065,"All six supported labels: total 6 × 1/2 = 3.\nDifferent η labels are not merged when Pη is equal.",10)

a=axes[1,1]
label(a,.5,.95,"D. The kernel intersection and the mass ledger",14,True)
label(a,.5,.82,"ker F = {0} × C₂,      ker P = {0} × C₄",12)
label(a,.5,.69,"im F = 2Z × {0}\nker P ∩ im F = {identity}",12,True,BLUE)
label(a,.5,.525,"|ker PF| = 2 × 1 = 2, rather than 2 × 4.",12,True)
label(a,.5,.38,"(mt/s)(n/t) = (2·4/2)(3/4) = 3 = mn/s",12,True,GREEN)
a.add_patch(Rectangle((.08,.145),.84,.135,facecolor="#edf7f1",
                     edgecolor=GREEN,transform=a.transAxes))
label(a,.5,.212,"Countable coarse fibres + finite isotropy kernels\n⇒ proper full-arrow functor; images compose.",11,True,GREEN)
label(a,.5,.065,"Abstract one-unit groups; no germ-realisation assertion.\nGeneral historical Borel leaf-map interface remains open.",10)

fig.subplots_adjust(left=.02,right=.985,bottom=.075,top=.925,wspace=.11,hspace=.12)
fig.text(.5,.985,"Full countable-groupoid image: composition keeps the arrow multiplicities",
         ha="center",va="top",fontproperties=BOLD,fontsize=18,color=INK)
fig.text(.5,.026,"Figure 5.25. Theorems 5.30–5.31 and Exercises 24–26. "
         "m = 2, n = 3, s = 2, t = 4; complete cutoff supports in infinite groups.",
         ha="center",fontproperties=REG,fontsize=11,color=INK)
notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
description="Original illustration CC0-1.0. Complete unmodified font notice follows.\n"+notice
png=out/"full-groupoid-composition.png";svg=out/"full-groupoid-composition.svg"
fig.savefig(png,dpi=160,metadata={"Description":description,
                               "Software":"Matplotlib "+matplotlib.__version__})
fig.savefig(svg,metadata={"Date":None,"Description":description})
plt.close(fig)
print("Rendered full-groupoid-composition.png and full-groupoid-composition.svg")
CACHE.cleanup()
