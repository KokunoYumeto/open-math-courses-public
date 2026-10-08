"""Original reproducible models. No source pages or font files are copied."""
from pathlib import Path
from fractions import Fraction
import json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":16,
 "axes.labelsize":12,"svg.fonttype":"none","svg.hashsalt":"oa-flow-core-orbits-v1",
 "mathtext.fontset":"dejavusans","savefig.facecolor":"#f7f9fb"})
NAVY,TEAL,ORANGE,RED="#16324f","#087f8c","#c67524","#b44545"
def save(fig,stem):
 fig.savefig(OUT/(stem+".svg"),bbox_inches="tight",metadata={"Date":None,"Creator":"Original OA-FLOW mathematical model"})
 fig.savefig(OUT/(stem+".png"),dpi=160,bbox_inches="tight")
 plt.close(fig)
fig=plt.figure(figsize=(16,9))
fig.suptitle("Finite orbit blocks produce compatible expectations",fontsize=22,color=NAVY,y=.97)
ax=fig.add_axes([.10,.43,.86,.43])
xmin,xmax=-4.6,12.6
ax.set(xlim=(xmin,xmax),ylim=(-.65,3.05))
ax.set_yticks([2.4,1.25,.1],[r"$n=1,\ r=2$",r"$n=3,\ r=8$",r"$n=5,\ r=32$"])
ax.set_xticks(range(-4,13));ax.set_xlabel("integer positions on one orbit (finite displayed window)")
for row,n in enumerate([1,3,5]):
 y=2.4-row*1.15;width=2**n;residue=sum(2**k for k in range(n) if k%2==0)
 for j in range(math.floor((xmin-residue)/width), math.floor((xmax-residue)/width)+1):
  b=residue+j*width
  if b+width<xmin or b>xmax:continue
  ax.add_patch(Rectangle((b,y-.27),width,.54,facecolor="#d7edf0" if j%2 else "#e5eaf3",edgecolor=TEAL,lw=1.5))
  if xmin<=b<=xmax:ax.scatter([b],[y+.32],marker="v",s=40,color=TEAL,zorder=4)
 ax.scatter(range(-4,13),[y]*17,s=18,color=NAVY,zorder=5)
 same=((4-residue)//width)==((2-residue)//width)
 assert same==(n!=1)
 color=TEAL if same else RED
 ax.annotate("",xy=(4,y+.04),xytext=(2,y+.04),arrowprops={"arrowstyle":"->","color":color,"lw":2.4,"connectionstyle":"arc3,rad=-.5"})
 ax.text(6.1,y+.38,"coefficient survives" if same else "coefficient removed",color=color,fontsize=11)
ax.spines[["top","right","left"]].set_visible(False);ax.tick_params(axis="y",length=0,pad=14)
ax.text(0,1.06,r"$E_n(aU^k)=p_{n,k}aU^k$;  $p_{n,k}=1$ exactly when the two endpoints share a block.",
 transform=ax.transAxes,fontsize=14,color=NAVY)
ax2=fig.add_axes([.035,.06,.93,.27]);ax2.axis("off")
boxes=[(r"$F_n=\prod_{r\geq1}\quad M_r(p_{r,0}N)$","variable finite block sizes\nin the full theorem"),
 (r"$E_nE_m=E_n\quad(n\leq m)$",r"$\omega E_n=\omega$"),
 (r"$\|\eta E_n-\eta\|\to0$",r"$\tau F_n^{\,C}=\tau$"),
 (r"$\|\eta|_{Z(C_n)}\|$","converges to "+r"$\|\eta|_{Z(C)}\|$")]
for i,(title,sub) in enumerate(boxes):
 x=.012+i*.25
 ax2.add_patch(FancyBboxPatch((x,.29),.218,.61,boxstyle="round,pad=.008",facecolor="white",edgecolor=TEAL,lw=1.3))
 ax2.text(x+.109,.72,title,ha="center",va="center",fontsize=13,color=NAVY)
 ax2.text(x+.109,.48,sub,ha="center",va="center",fontsize=11,color=NAVY)
 if i<3:ax2.annotate("",xy=(x+.245,.6),xytext=(x+.221,.6),arrowprops={"arrowstyle":"->","color":ORANGE,"lw":2})
ax2.text(.5,.08,"The centers need not be nested.  Proofs: FB2–FB11 and CM3–CM10.",ha="center",color=NAVY,fontsize=12)
save(fig,"finite-block-expectations")

assert Fraction(1,3)*2+Fraction(2,3)*Fraction(1,2)==1
assert Fraction(1,3)+Fraction(2,3)==1
fig,axes=plt.subplots(2,2,figsize=(15,10),layout="constrained")
fig.suptitle("The center retains the location of each trace tail",fontsize=22,color=NAVY)
a=np.linspace(0,2.5,1001)
tails=[((a<2).astype(float),2*(a<.5).astype(float),r"Fibre A: $\mu(A)=1/3$",r"$D_A=1(1/2)+1(3/2)=2$"),
 (.5*(a<1).astype(float),(a<1).astype(float),r"Fibre B: $\mu(B)=2/3$",r"$D_B=(1/2)(1)=1/2$")]
for ax,(f,g,title,eq) in zip(axes[0],tails):
 ax.step(a,f,where="post",color=TEAL,lw=2.5,label=r"$f_\phi$");ax.step(a,g,where="post",color=ORANGE,lw=2.5,label=r"$f_\psi$")
 ax.fill_between(a,f,g,step="post",color="#b7c7da",alpha=.65)
 ax.set(title=title,xlabel=r"threshold $a>0$",ylabel="trace of the strict spectral tail",xlim=(0,2.5),ylim=(-.05,2.45))
 ax.set_xticks([0,.5,1,2]);ax.grid(alpha=.15)
 ax.text(.06,.89,eq,transform=ax.transAxes,color=NAVY,fontsize=14);ax.legend(loc="upper right")
 for t in [.5,1,2]:
  idx=np.searchsorted(a,t);ax.scatter([t,t],[f[idx],g[idx]],s=22,color=[TEAL,ORANGE],zorder=5)
q=np.linspace(-1.3,3.4,1401)
fA=(np.exp(-q)<2).astype(float);gA=2*(np.exp(-q)<.5).astype(float)
fB=.5*(np.exp(-q)<1).astype(float);gB=(np.exp(-q)<1).astype(float)
ax=axes[1,0]
ax.plot(q,np.exp(-q)*np.abs(fA-gA)/3,color=TEAL,lw=2.5,label=r"fibre A: $(1/3)e^{-q}|f_\phi-f_\psi|$")
ax.plot(q,np.exp(-q)*np.abs(fB-gB)*2/3,color=ORANGE,lw=2.5,label=r"fibre B: $(2/3)e^{-q}|f_\phi-f_\psi|$")
ax.set(title="The same distance in the real-core coordinate",xlabel=r"$q=-\log a$",ylabel="central norm density",xlim=(-1.3,3.4),ylim=(0,.78))
ax.set_xticks([-math.log(2),0,math.log(2),2,3],[r"$-\log2$","0",r"$\log2$","2","3"])
ax.grid(alpha=.15);ax.legend(loc="upper right",fontsize=10)
ax.text(.04,.08,r"Both exponential tails continue to $q=+\infty$.",transform=ax.transAxes,color=NAVY,fontsize=10)
ax=axes[1,1];ax.axis("off")
for txt,y in [(r"$\phi(1)=\frac{1}{3}(2)+\frac{2}{3}(\frac{1}{2})=1$",.82),
 (r"$\psi(1)=\frac{1}{3}(1)+\frac{2}{3}(1)=1$",.63),
 (r"$\delta_N(\phi,\psi)=\|\chi_\phi-\chi_\psi\|$",.41),
 (r"$=\frac{1}{3}D_A+\frac{2}{3}D_B=\frac{2}{3}+\frac{1}{3}=1$",.24)]:
 ax.text(.03,y,txt,fontsize=19 if y<.5 else 17,color=NAVY)
ax.text(.03,.04,"Exact step profiles in type II∞ fibres; proofs SA8–SA12.\nShading shows the absolute tail difference, not projection order.",fontsize=11,color=NAVY)
save(fig,"central-fibre-tails")

L=math.log(4);C=Fraction(4,3)
fig,axes=plt.subplots(1,2,figsize=(15,6),layout="constrained")
fig.suptitle("A periodic profile becomes the actual central functional",fontsize=21,color=NAVY)
ax=axes[0];qq=np.linspace(0,L,401)
ax.plot(qq,float(C)*np.exp(-qq),color=TEAL,lw=3,label=r"$p(q)=(4/3)e^{-q}$ on $0<q<L$")
for lo,hi,mult in [(0,L/2,1),(L/2,L,4)]:
 qq=np.linspace(lo,hi,201);ax.plot(qq,mult*float(C)*np.exp(-qq),color=ORANGE,lw=2.5)
ax.plot([],[],color=ORANGE,lw=2.5,label=r"$p_{2\phi}(q)=2p(q+\log2\ \mathrm{mod}\ L)$")
ax.scatter([0,L/2,L],[float(C),float(C)/2,float(C)],color=ORANGE,s=40,zorder=4)
ax.scatter([L/2],[2*float(C)],facecolors="white",edgecolors=ORANGE,s=48,zorder=5)
ax.scatter([0,L],[float(C)/4,float(C)/4],color=TEAL,s=35,zorder=6)
ax.scatter([0],[float(C)],facecolors="white",edgecolors=TEAL,s=95,zorder=7)
ax.scatter([0],[float(C)],color=ORANGE,s=23,zorder=8)
ax.set(title=r"Circle density, $\lambda=1/4,\ L=\log4$",xlabel=r"height $q$ in one period",ylabel="density with respect to dq",xlim=(-.05,L+.05),ylim=(0,3.4))
ax.set_xticks([0,L/2,L],["0",r"$\log2$",r"$L=\log4$"]);ax.grid(alpha=.15);ax.legend(fontsize=10,loc="upper right",bbox_to_anchor=(1,.84))
ax.text(.05,.93,r"$\int_0^L p\,dq=1$;  $\int_0^L p_{2\phi}\,dq=2$",transform=ax.transAxes,color=NAVY,fontsize=13)
ax=axes[1]
for k in [-1,0,1]:
 yy=float(C)*4**k
 ax.plot([k*L,(k+1)*L],[yy,yy],color=TEAL,lw=3)
 ax.scatter([k*L],[yy],facecolors="white",edgecolors=TEAL,s=45,zorder=5)
 ax.scatter([(k+1)*L],[yy],color=TEAL,s=35,zorder=5)
 if k<1:ax.plot([(k+1)*L]*2,[yy,4*yy],color="#a9bdc7",ls=":",lw=1.5)
ax.scatter([-L],[float(C)/16],color=TEAL,s=35,zorder=5)
ax.set(title=r"The lifted function $g(q)=e^q p(q)$",xlabel="unwrapped real height",ylabel="increasing left-continuous profile",xlim=(-L-.08,2*L+.08),ylim=(0,6.8))
ax.set_xticks([-L,0,L,2*L],[r"$-L$","0",r"$L$",r"$2L$"])
ax.set_yticks([1/3,4/3,16/3],[r"$1/3$",r"$4/3$",r"$16/3$"]);ax.grid(alpha=.15)
ax.text(.08,.93,r"$g(q+L)=4g(q)$;  $f(a)=g(-\log a)$",transform=ax.transAxes,fontsize=14,color=NAVY)
ax.text(.08,.82,r"$\chi(z)=\int_0^L z(q)e^{-q}f(e^{-q})\,dq$",transform=ax.transAxes,fontsize=13,color=NAVY)
fig.text(.5,-.035,"Exact model on the full equivariant flag. Proofs PCO9–PCO16; endpoints use strict tails.",ha="center",fontsize=11,color=NAVY)
assert abs(float(C)*(1-.25)-1)<1e-14
assert abs(float(C)*(1-.5)+4*float(C)*(.5-.25)-2)<1e-14
save(fig,"periodic-central-profile")

data={"terms":"Original mathematical models; CC0-1.0 to the extent of rights held.",
 "fonts":{"family":"DejaVu Sans","reference":"matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf","svg_text":"Text retained; no font files copied or embedded."},
 "blocks":{"algebra_formula":"F_n=product_(r>=1) M_r(p_(r,0) N)","projection_convention":"At fixed n, p_(r,0) is the block-base central projection, as in FB3-FB5.","sample_positions":list(range(-4,13)),"levels":[1,3,5],"residue_formula":"r_n=sum(2^k for 0<=k<n with k even)","block_formula":"[r_n+j*2^n,r_n+(j+1)*2^n)","tested_endpoints":[2,4],"survival":[False,True,True],"scope":"A finite sample of a compatible single-orbit model; variable sizes retained in theorem.","proofs":["FB2","FB7","FB9","FB11","CM3","CM6","CM10"]},
 "fibres":{"base_masses":["1/3","2/3"],"phi_profiles":["1 on (0,2), 0 on [2,infinity)","1/2 on (0,1), 0 on [1,infinity)"],"psi_profiles":["2 on (0,1/2), 0 on [1/2,infinity)","1 on (0,1), 0 on [1,infinity)"],"fibre_distances":["2","1/2"],"integrated_distance":"1","phi_mass":"1","psi_mass":"1","proofs":["SA8","SA9","SA10","SA11","SA12"]},
 "periodic":{"lambda":"1/4","L":"log(4)","P":"2*pi/log(4)","p_on_open_period":"(4/3)*exp(-q)","periodic_left_endpoint_value":"1/3","g_on_kL_to_kplus1L":"(4/3)*4^k on (kL,(k+1)L]","scalar_c":"2","scalar_covariance":"p_(2phi)(q)=2*p(q+log(2) mod L)","masses":["1","2"],"proofs":["PCO9","PCO10","PCO13","PCO15","PCO16"]}}
(OUT/"model-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(OUT/"TERMS.md").write_text("""# Figure terms and reproduction

The three diagrams, exact data and Python renderer are original programme work, dedicated under CC0-1.0 to the extent of rights held. They contain no copied source illustration or source-page image.

Run python generate_models.py with Python, NumPy and matplotlib. SVG output retains text, has deterministic IDs and omits date metadata. PNG output is a rendered preview.

The installed DejaVu Sans family is referenced through matplotlib's bundled mpl-data/fonts/ttf/DejaVuSans.ttf; no font file is copied or embedded. DejaVu font terms remain with the installed distribution.

Human-source context: Haagerup–Størmer, Equivalence of Normal States on von Neumann Algebras and the Flow of Weights, Adv. Math. 83 (1990), §§5–8. Exact proof locators and model data are in model-data.json and the accompanying lessons. The finite displayed orbit is a sample; no finite-dimensional type III algebra is claimed.
""",encoding="utf-8")
print("Generated three SVG/PNG pairs and exact model data.")
