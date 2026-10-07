"""Reproduce exact-coordinate lifted-orbit models with clearly labeled samples.

Run python render.py. No external data or network access is used.
Original diagram, exact data and renderer: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Circle, Wedge, FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                     "mathtext.fontset":"dejavusans","svg.fonttype":"none"})
BLUE="#176495"
ORANGE="#ae5625"
GREEN="#2c7c50"
INK="#203141"
MUTED="#596b79"
fig,axes=plt.subplots(2,2,figsize=(18,12))
fig.patch.set_facecolor("#fbfcfe")
fig.subplots_adjust(left=.035,right=.975,bottom=.065,top=.88,hspace=.24,wspace=.12)
fig.suptitle("Lifted orbit models: the basepoint trace and the invariant coordinate",
             fontsize=23,fontweight="bold",color=INK,y=.966)
fig.text(.5,.922,"Infinite nonfree circle orbits and the weighted three-point S₃ orbit",
         ha="center",fontsize=16,color=MUTED)

def panel(ax,title):
    ax.set(xlim=(0,1),ylim=(0,1))
    ax.axis("off")
    ax.add_patch(Rectangle((0,0),1,1,fill=False,edgecolor="#cbd5df",lw=1.2))
    ax.text(.03,.95,title,va="top",fontsize=18,fontweight="bold",color=INK)

def txt(ax,x,y,t,**kw):
    ax.text(x,y,t,color=kw.pop("color",INK),**kw)

def arrow(ax,start,end,color=MUTED):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=15,
                                color=color,lw=1.5))

ax=axes[0,0]
panel(ax,"A  A nonfree irrational circle action")
txt(ax,.5,.81,r"$R x=x+\alpha\ (\mathrm{mod}\ 1),\qquad\alpha=\sqrt{2}-1$",ha="center",fontsize=18)
circle=ax.inset_axes([.045,.13,.49,.61])
circle.set(xlim=(-1.32,1.32),ylim=(-1.32,1.32),aspect="equal")
circle.axis("off")
circle.add_patch(Wedge((0,0),1,0,120,facecolor="#dcefe3",edgecolor="none"))
circle.add_patch(Circle((0,0),1,fill=False,edgecolor="#738695",lw=1.4))
alpha=np.sqrt(2)-1
samples=[]
for n in range(9):
    x=(n*alpha)%1
    theta=2*np.pi*x
    px,py=np.cos(theta),np.sin(theta)
    hit=bool(0<=x<1/3)
    color=GREEN if hit else BLUE
    circle.scatter([px],[py],s=46,color=color,zorder=4)
    circle.text(1.15*px,1.15*py,str(n),ha="center",va="center",color=color,fontsize=12)
    samples.append({"n":n,"exact_x":f"fractional_part({n}*(sqrt(2)-1))",
                    "integer_part":int(np.floor(n*alpha)),"in_B":hit})
circle.text(.13,.20,r"$B=[0,1/3)$",color=GREEN,fontsize=12)
txt(ax,.72,.66,r"$G=\mathbb{Z}\times C_2$",ha="center",fontsize=19)
txt(ax,.72,.53,r"$G_x=\{0\}\times C_2$",ha="center",fontsize=18)
txt(ax,.72,.40,r"$\delta=1,\quad\lambda_y=\lambda$",ha="center",fontsize=17)
txt(ax,.72,.27,r"basis: $e_{R^n x}$, $n\in\mathbb{Z}$",ha="center",fontsize=15)
txt(ax,.5,.065,"Labels 0–8 mark nine samples, not a proof of density or divergence.",
    ha="center",fontsize=12,color=MUTED)

ax=axes[0,1]
panel(ax,"B  One diagonal entry versus the whole fiber")
txt(ax,.5,.80,r"circle model: $p=1_{(1,2)}(\lambda)\,1$",ha="center",fontsize=18)
txt(ax,.5,.69,r"for $1<\lambda<2$, the fiber operator is $I_{\ell^2(\mathbb{Z})}$",
    ha="center",fontsize=16)
for j,n in enumerate(range(-2,3)):
    x=.24+j*.12
    color=ORANGE if n==0 else BLUE
    ax.add_patch(Rectangle((x-.048,.48),.096,.11,facecolor="#edf4f8",edgecolor="#bdcedb"))
    txt(ax,x,.535,"1",ha="center",va="center",fontsize=20,color=color)
    txt(ax,x,.43,rf"$n={n}$",ha="center",fontsize=12,color=MUTED)
txt(ax,.13,.535,"…",ha="center",va="center",fontsize=26,color=MUTED)
txt(ax,.85,.535,"…",ha="center",va="center",fontsize=26,color=MUTED)
txt(ax,.5,.325,r"$\tau_{\rm bp}(p)=1,\qquad \tau_{\rm core}(p)=\frac{1}{2\pi}$",
    ha="center",fontsize=19,color=ORANGE)
txt(ax,.5,.20,r"$\operatorname{Tr}_{\rm fiber}(p)=\sum_{n\in\mathbb{Z}}1=\infty$",
    ha="center",fontsize=19,color=BLUE)
txt(ax,.5,.065,r"Full theorem: $\mathcal{W}(T)=\infty$ for every $0\ne T\in N_+$.",
    ha="center",fontsize=15)

ax=axes[1,0]
panel(ax,"C  All three points of one weighted lifted orbit")
txt(ax,.5,.80,r"finite model: $(\mu_1,\mu_2,\mu_3)=(1,2,4),\quad w=2$",
    ha="center",fontsize=17)
coords=ax.inset_axes([.14,.32,.77,.39])
coords.set(xlim=(.65,3.45),ylim=(0,2.6))
coords.set_xticks([1,2,3])
coords.set_yticks([.5,1,2],["1/2","1","2"])
coords.spines[["top","right"]].set_visible(False)
coords.set_xlabel("x  (three discrete points)",fontsize=12)
coords.set_ylabel(r"$\lambda$",fontsize=15,rotation=0,labelpad=13)
for x,lam,color,label in [(1,2,BLUE,"(1, 2)"),(2,1,GREEN,"(2, 1)"),(3,.5,ORANGE,"(3, 1/2)")]:
    coords.plot([x,x],[0,lam],":",color="#b0c0cd",lw=1)
    coords.scatter([x],[lam],s=95,color=color,zorder=3)
    coords.text(x+.07,lam+.12,label,fontsize=13,color=color)
coords.grid(axis="y",color="#e2e8ed",lw=.7)
txt(ax,.5,.135,r"$w=\mu_x\lambda=\mu_y\lambda_y,\qquad \lambda_y=w/\mu_y$",
    ha="center",fontsize=18)
txt(ax,.5,.045,r"$\sum_x\mu_x\,d\lambda=\sum_x dw$  under the separate base changes",
    ha="center",fontsize=13,color=MUTED)

ax=axes[1,1]
panel(ax,"D  The exact finite-model normalization")
txt(ax,.5,.81,r"$h_\varphi(w)=h/w,\quad h=\operatorname{diag}(1,2,4)$",
    ha="center",fontsize=18)
txt(ax,.5,.70,r"$P(w)=I_3\,1_{(1,2)}(w),\quad (\theta_s A)(w)=A(e^s w)$",
    ha="center",fontsize=16)
wx=lambda w:.18+.32*w
for lo,hi,y,color in [(1,2,.55,BLUE),(.5,1,.40,ORANGE)]:
    ax.plot([wx(lo),wx(hi)],[y,y],lw=9,color=color,solid_capstyle="butt")
    ax.scatter([wx(lo),wx(hi)],[y,y],s=30,facecolor="#fbfcfe",edgecolor=color,zorder=4)
txt(ax,.06,.55,r"$P$",color=BLUE,va="center",fontsize=18)
txt(ax,.035,.40,r"$\theta_{\log2}P$",color=ORANGE,va="center",fontsize=15)
arrow(ax,(.23,.29),(.93,.29))
for w,label in [(.5,"1/2"),(1,"1"),(2,"2")]:
    ax.plot([wx(w),wx(w)],[.275,.305],color=MUTED,lw=1)
    txt(ax,wx(w),.225,label,ha="center",fontsize=12)
txt(ax,.95,.28,r"$w$",fontsize=15)
txt(ax,.5,.125,r"$\tau_{\rm bp}(P)=3,\qquad\tau_{\rm core}(P)=\frac{3}{2\pi}$",
    ha="center",fontsize=18,color=BLUE)
txt(ax,.5,.04,r"$\tau_{\rm core}(\theta_{\log2}P)=\frac{3}{4\pi}$",
    ha="center",fontsize=17,color=ORANGE)

fig.text(.5,.022,"Exact finite coordinates and trace constants. Circle points are finitely many samples; the complete analytic proofs are retained in Sections 7–8.",
         ha="center",fontsize=13,color=MUTED)
for ext in ("png","svg"):
    fig.savefig(HERE/f"lifted-orbit-flow.{ext}",dpi=160,facecolor=fig.get_facecolor())
plt.close(fig)

data={
 "title":"Lifted orbit flow: basepoint trace and invariant coordinate",
 "license":"CC0-1.0 to the extent of rights held; font terms separate",
 "circle":{
   "space":"R/Z","measure":"normalized Lebesgue measure","alpha":"sqrt(2)-1",
   "action":"(n,epsilon).x=x+n*alpha mod 1","stabilizer":"{0} x C2","delta":1,
   "lift":"(n,epsilon).(x,lambda)=(x+n*alpha,lambda)","basis":"distinct points R^n x, one per integer n",
   "samples":samples,"B":"[0,1/3)","sampling_notice":"Only n=0,...,8 is displayed. Pigeonhole density, L2 averaging ergodicity, and the full almost-everywhere divergence proof are in LFT7.b-d and LFT7.k-m.",
   "projection":"p=1_(1,2)(lambda) I","basepoint_trace":"1","canonical_core_trace":"1/(2*pi)",
   "full_fiber_trace":"infinity","full_obstruction":"W(T)=infinity for every nonzero positive T in N",
   "center":"L-infinity((0,infinity),d lambda)","center_action":"c(lambda) -> c(exp(s)*lambda)"
 },
 "finite":{
   "space":[1,2,3],"masses":[1,2,4],"group":"S3","invariant":"w=mu_x*lambda",
   "w_sample":2,"complete_lifted_orbit":[[1,2],[2,1],[3,"1/2"]],
   "unitary":"V eta(y,x,w)=eta(y,x,w/mu_x)","coordinate_measure":"dw in each of the three base columns",
   "algebra":"M3 tensor L-infinity(dw)","density":"diag(1,2,4)/w",
   "core_group":"diag(1,2,4)^it * w^-it","basepoint_trace":"integral Tr(A(w)) dw",
   "canonical_core_trace":"(1/(2*pi))*integral Tr(A(w)) dw",
   "dual_weight":"(1/(2*pi))*integral Tr(diag(1,2,4)*A(w)) dw/w",
   "projection":"P=I3*1_(1,2)(w)","basepoint_projection_trace":3,
   "canonical_projection_trace":"3/(2*pi)","dual_projection_weight":"7*log(2)/(2*pi)",
   "s":"log(2)","translated_projection_support":["1/2",1],"translated_canonical_trace":"3/(4*pi)"
 },
 "proof_locators":["LFT7.b-d","LFT7.g-o","LFT7.p-v","LFT8.b","LFT8.e-f"]
}
(HERE/"data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font=Path(font_manager.findfont("DejaVu Sans"))
license_file=font.parent/"LICENSE_DEJAVU"
if not license_file.is_file():raise FileNotFoundError("Font license must accompany the figure.")
shutil.copyfile(license_file,HERE/"FONT-LICENSE.txt")
(HERE/"TERMS.md").write_text(
 "# Figure terms\n\nOriginal diagram, renderer and exact mathematical data: CC0-1.0 to the extent of rights held. "
 "DejaVu font terms are retained in FONT-LICENSE.txt. No external image or book excerpt is included. "
 "Run python render.py with NumPy and Matplotlib to regenerate PNG, editable SVG and data. "
 "Circle coordinates are numerical renderings of the exact algebraic expressions recorded in data.json; "
 "the finite samples are not evidence for density or almost-everywhere divergence. "
 "Both full analytic proofs are retained in the lesson.\n",encoding="utf-8")
print("Rendered PNG/SVG with exact data and font terms.")
