"""Exact sector geometry, actual gauge maps and the two support-purity steps."""
from pathlib import Path
import argparse,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge,FancyBboxPatch,FancyArrowPatch
parser=argparse.ArgumentParser()
parser.add_argument("--output-dir",type=Path,default=Path(__file__).parent)
out=parser.parse_args().output_dir
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,
                     "svg.hashsalt":"GL-DMOD-SG-FG-GM-exact-v1"})
fig=plt.figure(figsize=(17,13),dpi=150,facecolor="#f7f9fc")
a=fig.add_axes([0,0,1,1])
a.set(xlim=(0,17),ylim=(0,13));a.axis("off")
ink,blue,green,muted="#14263f","#155ca5","#17765d","#52627a"
def text(x,y,value,size=18,color=ink):
    a.text(x,y,value,ha="center",va="center",fontsize=size,color=color)
def box(x,y,w,h,value,size=18):
    a.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,
        boxstyle="round,pad=0.08,rounding_size=0.1",facecolor="white",
        edgecolor=blue,linewidth=1.5))
    text(x,y,value,size)
def arrow(p,q,color=blue):
    a.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=16,lw=1.6,color=color))
text(8.5,12.5,"Full Gevrey gauges and comparison on singular holonomic germs",24)
text(8.5,11.98,r"$h=\tau^{-1},\quad B=\mathscr{E}^{\infty},\quad C=\mathscr{E}^{\mathbb{R}}$",20,muted)
geom=fig.add_axes([.025,.535,.40,.35],facecolor="#f7f9fc")
geom.set_aspect("equal");geom.set(xlim=(-3.1,3.1),ylim=(-3.1,3.1))
geom.axis("off")
colors=["#4c90d6","#63ad88","#bb88ce","#e1a565"]
for j,color in enumerate(colors):
    geom.add_patch(Wedge((0,0),2.45,j*90-67.5,j*90+67.5,width=1.45,
                         facecolor=color,edgecolor=color,alpha=.20,lw=1))
    angle=j*np.pi/2
    geom.text(2.8*np.cos(angle),2.8*np.sin(angle),f"S{j}",
              ha="center",va="center",fontsize=17,color=color)
    angle+=np.pi/4
    direction=np.array([np.cos(angle),np.sin(angle)])
    geom.annotate("",xy=2.62*direction,xytext=direction,
                   arrowprops={"arrowstyle":"->","lw":1.8,"color":blue})
    geom.text(*(2.22*direction+np.array([.14,-.12])),rf"$\Gamma_{j}$",
              ha="center",va="center",fontsize=15,color=blue)
phi=np.linspace(0,2*np.pi,300)
geom.plot(np.cos(phi),np.sin(phi),color=muted,lw=1)
geom.plot([-2.7,2.7],[0,0],color=muted,lw=.6)
geom.plot([0,0],[-2.7,2.7],color=muted,lw=.6)
geom.text(.25,.25,"0",color=muted,fontsize=14)
geom.text(.40,.84,r"$|\zeta|/R_1=1$",fontsize=12,color=muted)
text(3.8,6.77,r"$\arg S_j=j\pi/2\ \pm 3\pi/8$",18,blue)
text(3.8,6.32,r"$\arg\Gamma_j=j\pi/2+\pi/4$",18,blue)
text(3.8,5.91,"Outward rays continue to infinity.  [SG.2, SG.7]",15,muted)
box(12.15,10.72,8.6,.92,
    r"$T_j,\ Z_{i,j}\quad\mathrm{from\ finite\ Laplace\ integrals}$",20)
arrow((12.15,10.15),(12.15,9.74))
box(12.15,9.20,8.6,.88,r"$\|Y_j\|+\|Y_j^{-1}\|\leq K e^{L|\zeta|^\alpha},\quad\alpha<1$",20)
text(12.15,8.52,"Nilpotent stack; uniform in the parameters.  [FG.6–FG.8]",15,muted)
arrow((12.15,8.19),(12.15,7.79))
box(12.15,7.22,8.6,.88,r"$V_j=A_jJ_j e^{-w_jH},\quad e^{2\pi iH}=M$",21)
text(12.15,6.53,"Both inverse families have exponentially flat jumps.  [FG.14–FG.17]",14,muted)
arrow((12.15,6.18),(12.15,5.78))
box(12.15,5.22,8.6,.88,r"$V,W\in\mathrm{GL}_r(\mathcal{R}^{\infty}),\quad VW=WV=I$",21)
text(12.15,4.57,"Cauchy–Heine descent and exact mixed products.  [SG.7–SG.16]",14,green)
a.plot([.6,16.4],[4.15,4.15],color="#d7dfea",lw=1.2)
text(8.5,3.70,"Two separate uses of the full support-purity theorem",21,blue)
box(3.5,2.70,5.6,1.0,r"$Z=\Lambda\cap\{g(x)=0\}$"+"\n"+r"$\mathrm{codim}\,Z\geq n+1$",20)
box(9.27,2.70,4.7,1.0,r"$W=\mathrm{fixed\ analytic}$"+"\n"+r"$\mathrm{exceptional\ set}$",19)
box(14.40,2.70,4.0,1.0,r"$B\otimes_E M$"+"\n"+r"$\hookrightarrow C\otimes_E M$",19)
arrow((6.42,2.70),(6.78,2.70))
arrow((11.75,2.70),(12.22,2.70))
text(3.50,1.88,"Generic parameter open → every smooth point",14,muted)
text(9.27,1.88,r"$\mathrm{codim}\,W\geq n+1$",17,muted)
text(14.40,1.88,"Every holonomic germ",15,green)
text(8.5,1.16,"A kernel section is supported first on Z, then on W; each support group in degree zero vanishes.",16,muted)
text(8.5,.56,"Exact cover angles and proved maps.  Radial extent of the sector picture is truncated; no numerical solution is shown.",15,muted)
fig.savefig(out/"sectoral-gevrey-and-real-comparison.png",dpi=150)
fig.savefig(out/"sectoral-gevrey-and-real-comparison.svg",metadata={"Date":None})
plt.close(fig)
data={"kind":"exact sector geometry and proved map diagram; no numerical solution",
 "sector_cover":{"centres":["0","pi/2","pi","3pi/2"],"angular_half_width":"3pi/8",
   "adjacent_overlap_opening":"pi/4","opposite_intersections":"empty",
   "Cauchy_rays":["pi/4","3pi/4","5pi/4","7pi/4"],
   "radial_coordinate":"|zeta|/R1","inner_radius":1,"displayed_outer_radius":2.45,
   "rays_continue_to":"infinity","proof":"SG.2, SG.7–SG.11"},
 "gauge":{"sector_matrices":"finite Laplace representatives of arbitrary Gevrey coefficients",
   "growth_exponent":"alpha=1-1/max(2,k), N^k=0",
   "monodromy":"M=L3^-1 L2^-1 L1^-1 L0^-1",
   "Euler_matrix":"(H-I)^transpose, exp(2pi i H)=M",
   "actual_inverse":"VW=WV=I in full coefficient ring","proof":"FG.1–FG.17; SG.1–SG.16"},
 "purity":{"first":"Z=Lambda intersect {g(x)=0}; codim>=n+1",
   "second":"fixed analytic exceptional set W containing the singular/intersection loci; codim>=n+1",
   "conclusion":"B tensor_E M injects into C tensor_E M for every coherent holonomic M",
   "proof":"GM.13–GM.16, exact earlier PG.1–PG.2"},
 "general_C_over_B_flatness_asserted":False}
(out/"sectoral-gevrey-and-real-comparison-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
