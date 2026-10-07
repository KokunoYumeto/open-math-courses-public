"""Reproduce the exact finite-orbit diagram and sampled domain contributions.

Run python render.py. No external data or network access is required.
Original diagram, renderer and data: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
from fractions import Fraction
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                     "mathtext.fontset":"dejavusans","svg.fonttype":"none"})
BLUE="#176495"
ORANGE="#ac5424"
GREEN="#28784e"
INK="#203141"
MUTED="#566675"
fig,axes=plt.subplots(2,2,figsize=(18,12))
fig.patch.set_facecolor("#fbfcfe")
fig.subplots_adjust(left=.035,right=.975,bottom=.075,top=.88,hspace=.24,wspace=.12)
fig.suptitle("Count distinct orbit points; the measure fixes the modular ratios",
             fontsize=24,fontweight="bold",color=INK,y=.965)
fig.text(.5,.921,"The S₃ orbit with masses (1, 2, 4), and an exact graph-domain example on ℤ",
         ha="center",fontsize=16,color=MUTED)

def panel(ax,title):
    ax.set(xlim=(0,1),ylim=(0,1))
    ax.axis("off")
    ax.add_patch(Rectangle((0,0),1,1,fill=False,edgecolor="#cbd5df",lw=1.2))
    ax.text(.03,.95,title,va="top",color=INK,fontsize=18,fontweight="bold")

def txt(ax,x,y,text,**kw):
    ax.text(x,y,text,color=kw.pop("color",INK),**kw)

def arrow(ax,start,end,color=INK):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=16,
                                lw=1.6,color=color))

def grid(ax,left,top,entries,cell=.075,title=None,highlight=None):
    for y in range(3):
        for x in range(3):
            c=ORANGE if highlight==(y,x) else BLUE
            bg="#fbece1" if highlight==(y,x) else "#edf4f8"
            ax.add_patch(Rectangle((left+x*cell,top-(y+1)*cell),cell,cell,
                                  facecolor=bg,edgecolor="#c2d1dc",lw=1))
            txt(ax,left+(x+.5)*cell,top-(y+.5)*cell,str(entries[y][x]),
                ha="center",va="center",fontsize=13,color=c)
    if title:
        txt(ax,left+1.5*cell,top+.055,title,ha="center",fontsize=17)

ax=axes[0,0]
panel(ax,"A  Three orbit coordinates, with stabilizers")
txt(ax,.24,.78,r"permutations $g\in S_3$",ha="center",fontsize=16)
txt(ax,.67,.78,r"distinct points $g1$",ha="center",fontsize=16)
groups=[("1, (23)","1","1"),("(12), (123)","2","2"),("(13), (132)","3","4")]
for row,(g,y,mu) in enumerate(groups):
    yy=.64-row*.18
    ax.add_patch(Rectangle((.075,yy-.055),.33,.11,facecolor="#edf4f8",edgecolor="#bdd0df"))
    txt(ax,.24,yy,g,ha="center",va="center",fontsize=17)
    arrow(ax,(.43,yy),(.585,yy))
    ax.add_patch(Rectangle((.615,yy-.055),.105,.11,facecolor="#eaf4ee",edgecolor="#a9cbb6"))
    txt(ax,.667,yy,y,ha="center",va="center",fontsize=19,color=GREEN)
    txt(ax,.78,yy,rf"$\mu_{y}={mu}$",va="center",fontsize=16)
txt(ax,.5,.10,r"$|G_1|=2,\qquad |G/G_1|=3,\qquad \dim H=3\cdot3=9$",
    ha="center",fontsize=17)

ax=axes[0,1]
panel(ax,"B  Row and column measures on all nine pairs")
mu=[1,2,4]
right=[[mu[x] for x in range(3)] for y in range(3)]
left=[[mu[y] for x in range(3)] for y in range(3)]
delta=[[str(Fraction(mu[y],mu[x])) for x in range(3)] for y in range(3)]
for lx,table,title in [(.055,right,r"$\nu_r(y,x)=\mu_x$"),
                       (.37,left,r"$\nu_l(y,x)=\mu_y$"),
                       (.685,delta,r"$\delta(y,x)=\mu_y/\mu_x$")]:
    grid(ax,lx,.69,table,cell=.08,title=title,highlight=(0,1))
    txt(ax,lx+.12,.35,"columns x = 1, 2, 3",ha="center",fontsize=11,color=MUTED)
txt(ax,.5,.80,"row y increases downward; column x increases to the right",
    ha="center",fontsize=13,color=MUTED)
txt(ax,.5,.25,r"marked pair $(y,x)=(1,2):\quad 1/2=1\div2$",
    ha="center",fontsize=16,color=ORANGE)
txt(ax,.5,.10,r"$\nu_r(E)=\nu_l(E)=21,\qquad \delta(y,x)\delta(x,z)=\delta(y,z)$",
    ha="center",fontsize=16)

ax=axes[1,0]
panel(ax,"C  The modular sign from the two GNS norms")
e12=[[0,1,0],[0,0,0],[0,0,0]]
e21=[[0,0,0],[1,0,0],[0,0,0]]
grid(ax,.12,.75,e12,cell=.09,title=r"$\Lambda(e_{12})$",highlight=(0,1))
grid(ax,.60,.75,e21,cell=.09,title=r"$S\Lambda(e_{12})=\Lambda(e_{21})$",highlight=(1,0))
arrow(ax,(.405,.62),(.575,.62))
txt(ax,.49,.68,r"$S$",ha="center",fontsize=19)
txt(ax,.255,.385,r"$\|\Lambda(e_{12})\|^2=2$",ha="center",fontsize=17,color=BLUE)
txt(ax,.735,.385,r"$\|\Lambda(e_{21})\|^2=1$",ha="center",fontsize=17,color=ORANGE)
txt(ax,.5,.255,r"$\Delta e_{12}=\frac{1}{2}e_{12},\qquad t_*=\frac{\pi}{2\log2}$",
    ha="center",fontsize=18)
txt(ax,.5,.115,r"$\sigma_{t_*}^{\varphi}(e_{12})=-i e_{12}$",
    ha="center",fontsize=23,color=ORANGE)

ax=axes[1,1]
panel(ax,"D  A graph-domain vector outside D(Δ)")
txt(ax,.5,.80,r"$\xi_{n,0}=2^{-n}\ (n\geq1),\quad \mu_x=2^x$",
    ha="center",fontsize=17)
plot=ax.inset_axes([.105,.28,.845,.43])
n=np.arange(1,9)
plot.set_facecolor("#fbfcfe")
plot.plot(n,4.0**(-n),"o",color=BLUE,label=r"$\|\xi\|^2$ term: $4^{-n}$",ms=6)
plot.plot(n,2.0**(-n),"s",color=GREEN,label=r"$\|S\xi\|^2$ term: $2^{-n}$",ms=5.5)
plot.plot(n,np.ones_like(n),"^",color=ORANGE,label=r"$D(\Delta)$ test term: $1$",ms=6)
plot.set(yscale="log",xlim=(.5,8.5),ylim=(2.0**-17,2))
plot.set_yticks([1,2.0**-4,2.0**-8,2.0**-12,2.0**-16],
               [r"$1$",r"$2^{-4}$",r"$2^{-8}$",r"$2^{-12}$",r"$2^{-16}$"])
plot.set_xticks(n)
plot.tick_params(labelsize=10)
plot.set_xlabel("n  (the first eight exact terms)",fontsize=11)
plot.grid(axis="y",color="#dce3e9",lw=.6)
plot.spines[["top","right"]].set_visible(False)
plot.legend(loc="lower left",fontsize=10,framealpha=.95)
txt(ax,.5,.135,r"full sums: $\frac{1}{3},\ 1,\ \infty$;  $\xi\in D(S)=D(\Delta^{1/2})$",
    ha="center",fontsize=15)
txt(ax,.5,.045,r"graph-norm tail squared: $\frac{4^{-N}}{3}+2^{-N}\longrightarrow0$",
    ha="center",fontsize=15)

fig.text(.5,.028,"Finite panels show every entry. The last panel shows eight exact terms; the complete series and graph-core proof are in REL Diagnostic E.",
         ha="center",fontsize=13,color=MUTED)
for ext in ("png","svg"):
    fig.savefig(HERE/f"countable-orbit-algebras.{ext}",dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)

data={
 "title":"Countable orbit algebras: exact S3 and weighted integer examples",
 "license":"CC0-1.0 to the extent of rights held; font terms separate",
 "finite":{
   "X":[1,2,3],"group":"S3","action":"g.x = g(x)","masses":mu,
   "stabilizer_at_1":["identity","(23)"],"cosets_reaching_1":["identity","(23)"],
   "cosets_reaching_2":["(12)","(123)"],"cosets_reaching_3":["(13)","(132)"],
   "fiber_dimension":3,"relation_pairs":9,"right_counting":right,"left_counting":left,
   "delta":delta,"right_total":21,"left_total":21,"wrong_group_counting_total":42,
   "matrix_algebra":"M3(C), acting on the left","expectation":"diag(A11,A22,A33)",
   "weight":"Tr(diag(1,2,4) A)","weight_identity":7,
   "norm_Lambda_e12_squared":2,"norm_S_Lambda_e12_squared":1,
   "delta_e12":"1/2","t_star":"pi/(2*log(2))","sigma_tstar_e12":"-i e12",
   "coordinates":"row y; column x"
 },
 "infinite":{
   "X":"Z","group":"Z","action":"m.x=x+m","mass":"mu_x=2^x","delta":"2^(y-x)",
   "vector":"xi(n,0)=2^-n for n>=1, zero elsewhere","sampled_indices":list(range(1,9)),
   "sampled_H_norm_terms":[str(Fraction(1,4**int(j))) for j in n],
   "sampled_S_norm_terms":[str(Fraction(1,2**int(j))) for j in n],
   "sampled_Delta_norm_terms":[1]*8,
   "full_sums":["1/3","1","infinity"],"graph_norm_tail_squared":"4^-N/3+2^-N",
   "Delta_truncation_norm_squared":"N",
   "sampling_notice":"Only n=1,...,8 is plotted. Full convergence and divergence follow from the exact infinite series proved in REL7.i-j."
 },
 "proof_locators":["REL6.a-j","REL6.k-t","REL7.a-c","REL7.h-j"]
}
(HERE/"data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font=Path(font_manager.findfont("DejaVu Sans"))
license_file=font.parent/"LICENSE_DEJAVU"
if not license_file.is_file():
    raise FileNotFoundError("The font license must accompany the figure.")
shutil.copyfile(license_file,HERE/"FONT-LICENSE.txt")
(HERE/"TERMS.md").write_text(
 "# Figure terms\n\nOriginal diagram, renderer and exact data: CC0-1.0 to the extent of rights held. "
 "No external image or source excerpt is included. DejaVu font terms are retained in FONT-LICENSE.txt. "
 "Run python render.py with Matplotlib and NumPy to regenerate both images and data. "
 "The displayed finite tables are complete; the infinite panel shows the first eight exact terms "
 "of sequences whose full convergence and divergence are proved in the accompanying lesson.\n",
 encoding="utf-8")
print("Rendered PNG/SVG and saved exact data and font terms.")
