"""Finite normal moments, physical corner energy and a partition obstruction.

Exposition and figure by GPT-6.1 Sol (OpenAI). CC0-1.0.
Proof locators: general-tail-supports-and-controlled-tunnels, TP.7–TP.10.
Scholarly context: S. Popa, Classification of amenable subfactors of type II,
Theorem 4.3.1, printed pp. 217–219. Matrix coordinates below are exact;
boxes and arrows are schematic, with no metric or trace-area interpretation.
Run this file with Python and matplotlib to reproduce the SVG and PNG.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":17,
                     "svg.fonttype":"path","svg.hashsalt":"tail-physical-moments",
                     "mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(8,24),facecolor="#f8fafc")
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,640);ax.set_ylim(0,1920);ax.axis("off")
ink="#17324d";blue="#126c97";red="#a52c3f"
def text(x,y,s,size=17,**kw):
    ax.text(x,y,s,fontsize=size,color=ink,va="top",**kw)
def panel(y,h,title):
    ax.add_patch(FancyBboxPatch((20,y-h),600,h,boxstyle="round,pad=0,rounding_size=12",
        facecolor="white",edgecolor="#cad5e0",linewidth=1.2))
    text(40,y-20,title,19,weight="bold")
text(30,1896,"Physical moments at one tail stage",23,weight="bold")
text(30,1850,"Exact selection, energy and its partition boundary",16)

panel(1800,390,"1. A compact moment slice  ·  TP.7")
text(40,1744,r"$0\leq x\leq p\quad$ in a finite type II algebra $C$")
text(40,1704,r"$K=\{0\leq y\leq p:\ T_C(y)=T_C(x),$")
text(66,1668,r"$\varphi_j(y)=\varphi_j(x)\ (1\leq j\leq m)\}$")
text(40,1620,"A nonprojection has a fractional spectral band:")
text(60,1582,r"$e=1_{[\epsilon,\,1-\epsilon]}(y)\ne0$")
text(40,1536,r"$n^2-1>2m\ \Longrightarrow\ \exists\,h=h^*\ne0$")
text(60,1498,r"$h=ehe,\quad T_C(h)=0,\quad\varphi_j(h)=0$")
text(40,1454,r"$y-h,\ y+h\in K$: extreme points are projections.",16)

panel(1388,355,"2. The physical coefficients stay fixed  ·  TP.9")
text(40,1330,r"$A=N_l'\cap M,\quad C=N_l\cap S,\quad f\in B_l$")
text(40,1288,r"$a=\tau(x)>0,\quad v=\tau(f)>0$")
text(40,1246,r"$0\leq x\leq p\quad\longrightarrow\quad q=q^2\leq p$",20)
text(40,1198,r"$T_C(q)=T_C(x),\qquad\tau(q)=a$")
text(40,1156,r"$E_A(uq)=E_A(ux)\quad(u\in U)$")
text(40,1114,r"$T_S(qf)=T_S(xf),\qquad\tau(qf)=av$")
text(40,1072,"Same stage, same tunnel, every earlier Jones cup.",16)

panel(1010,350,"3. One exact combined energy  ·  TP.8–TP.9")
text(40,954,r"$\Phi_x(u)=a^{-1}fE_A(ux)f,\quad s=qf$")
text(40,912,r"$D_x(u)=1-\|\Phi_x(u)\|_2^2/v,\quad 0\leq D_x\leq1$")
text(40,868,r"$\mathcal{D}=sAs,\quad c_u=\|[u,s]\|_2/\sqrt{av}$")
text(40,826,r"$e_u=\|sus-E_{\mathcal{D}}(sus)\|_2/\sqrt{av}$")
ax.text(60,780,r"$c_u^2+2e_u^2=2D_x(u)$",fontsize=23,color=blue,va="top")
text(40,728,r"$c_u\leq\sqrt{2D_x(u)},\qquad e_u\leq\sqrt{D_x(u)}$")
text(40,686,"Noncentral f is allowed. Physical targets are unchanged.",15)

panel(638,540,"4. Three effects obstruct a partition  ·  TP.10")
# Euclidean coordinates are exact: three unit vectors at 0,120,240 degrees.
cx,cy,r=184,435,108
ax.add_patch(Circle((cx,cy),r,fill=False,edgecolor="#b7c9d6",linewidth=1.2))
ax.plot([cx-r-10,cx+r+10],[cy,cy],color="#d5dfe7",linewidth=1)
ax.plot([cx,cx],[cy-r-10,cy+r+10],color="#d5dfe7",linewidth=1)
for vx,vy in [(1,0),(-.5,math.sqrt(3)/2),(-.5,-math.sqrt(3)/2)]:
    ax.annotate("",xy=(cx+r*vx,cy+r*vy),xytext=(cx,cy),
                arrowprops=dict(arrowstyle="-|>",lw=2,color=blue))
text(300,448,r"$v_1=(1,0)$",16)
text(40,574,r"$v_2=(-1/2,\sqrt{3}/2)$",16)
text(40,300,r"$v_3=(-1/2,-\sqrt{3}/2)$",16)
text(328,514,r"$P_i=v_iv_i^*$",17)
text(328,476,r"$x_i=\frac{2}{3}P_i\otimes1$",17)
text(328,390,r"$\sum_i x_i=1$",17)
text(328,352,r"$E(q_i)=\frac{2}{3}P_i$",17)
text(40,248,r"$q_i=P_i\otimes r_i,\qquad\tau_{R_0}(r_i)=2/3$")
text(40,204,"Orthogonality would force the rᵢ to be orthogonal.",16)
ax.text(40,164,r"$\sum_i r_i\leq1\quad$ but $\quad\tau_{R_0}(\sum_i r_i)=2>1$",
        fontsize=17,color=red,va="top")
text(30,74,"One effect and its full complement retain all moments.",16)
text(30,44,"Positive inputs with small physical defects still require proof.",15)
out=Path(__file__).with_suffix("")
fig.savefig(out.with_suffix(".svg"),bbox_inches=None,metadata={"Date":None})
fig.savefig(out.with_suffix(".png"),dpi=160,bbox_inches=None)
plt.close(fig)
svg_path=out.with_suffix(".svg")
svg_path.write_text("\n".join(line.rstrip() for line in
                    svg_path.read_text(encoding="utf-8").splitlines())+"\n",
                    encoding="utf-8")
