"""Original BS exact norm example and integration/localization/recovery mechanism. CC0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
D=Path(__file__).resolve().parent;OUT=D/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                    "svg.hashsalt":"OA-FLOW-BS-v1"})
blue="#146bac";orange="#cc6e1e";green="#238250";purple="#7d58a1";dark="#19334e"
s=np.arange(6);zeta=np.exp(2j*np.pi/6)
alphas=np.array([[[1,zeta**u-1],[0,zeta**u]] for u in s],dtype=complex)
norms=np.sum(abs(alphas),axis=1).max(axis=1)
expected=np.array([1,2,1+np.sqrt(3),3,1+np.sqrt(3),2])
assert np.max(abs(norms-expected))<1e-14
assert np.max(abs(alphas[3]@np.array([0,1])-np.array([-2,-1])))<1e-14
assert max(np.max(abs(alphas[u]@alphas[v]-alphas[(u+v)%6])) for u in s for v in s)<1e-14
filters=np.array([sum(zeta**(n*u)/6*alphas[u] for u in s) for n in s])
P0=np.array([[1,-1],[0,0]],dtype=complex);P5=np.array([[0,1],[0,1]],dtype=complex)
assert np.max(abs(filters[0]-P0))<1e-14
assert np.max(abs(filters[5]-P5))<1e-14
assert np.max(abs(filters[1:5]))<1e-14
fig=plt.figure(figsize=(16,12),dpi=200,facecolor="white")
fig.text(.045,.961,"Banach spectral calculus: bounds, domains and recovery",fontsize=25,
         weight="bold",color=dark)
fig.text(.045,.924,"A: exact noncontractive Z/6Z model.   B–D: the arbitrary-LCA proof, with its integration topologies explicit.",
         fontsize=15,color=dark)
gs=fig.add_gridspec(2,2,left=.06,right=.96,top=.857,bottom=.055,
                     hspace=.29,wspace=.17,height_ratios=[1,1.12])
ax=fig.add_subplot(gs[0,0])
ax.set_title("A. The constant C cannot be dropped",loc="left",color=dark,fontsize=17,pad=14)
ax.bar(s,norms,width=.6,color=[blue,blue,blue,orange,blue,blue],zorder=3)
for u,y in zip(s,norms):
 ax.text(u,y+.08,["1","2",r"$1+\sqrt{3}$","3",r"$1+\sqrt{3}$","2"][u],
         ha="center",fontsize=13,color=dark)
ax.axhline(3,color=orange,lw=1.5,ls="--")
ax.set_ylim(0,3.7);ax.set_xlim(-.55,5.6);ax.set_xticks(s)
ax.set_xlabel(r"$s\in\mathbb{Z}/6\mathbb{Z}$");ax.set_ylabel(r"$\|\alpha_s\|_{\ell^1\to\ell^1}$")
ax.grid(axis="y",alpha=.14,zorder=0)
ax.text(.03,.97,"αₛ = [[1, ζˢ−1], [0, ζˢ]]",
        transform=ax.transAxes,va="top",fontsize=14,color=dark)
ax.text(.64,.97,r"$\zeta=e^{2\pi i/6}$",transform=ax.transAxes,va="top",fontsize=14,color=dark)
ax.text(.04,.11,r"$\alpha_3(0,1)=(-2,-1),\quad\|\alpha_3(0,1)\|_1=3$",
        transform=ax.transAxes,color="white",fontsize=13,
        bbox={"boxstyle":"round,pad=.35","facecolor":dark,"edgecolor":dark})

def box(ax,x,y,w,h,txt,color,fontsize=13):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.012",
                            fc=color+"10",ec=color,lw=1.4))
 ax.text(x+w/2,y+h/2,txt,ha="center",va="center",fontsize=fontsize,color=dark,
         linespacing=1.55)
def arrow(ax,xy,xytext):
 ax.annotate("",xy=xy,xytext=xytext,
             arrowprops={"arrowstyle":"->","color":dark,"lw":1.5})
ax=fig.add_subplot(gs[0,1]);ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title("B. Integrate in the correct Banach space",loc="left",color=dark,fontsize=17,pad=14)
box(ax,.025,.57,.41,.25,"(B) strong Banach action\n"+r"$\int f(s)\alpha_sx\,ds\in X$",blue,14)
box(ax,.59,.57,.38,.25,r"$T_fx$"+"\n"+r"$\tau=$ norm",blue,14)
arrow(ax,(.575,.69),(.45,.69))
box(ax,.025,.18,.41,.25,"(D) specified "+r"$X=Y^*$"+"\n"+r"$S_fy=\int f(s)a_sy\,ds\in Y$",purple,13)
box(ax,.59,.18,.38,.25,r"$T_f=S_f^*$"+"\n"+r"$\tau=\sigma(X,Y)$",purple,14)
arrow(ax,(.575,.3),(.45,.3));ax.text(.512,.345,"adjoint",ha="center",fontsize=10,color=purple)
ax.text(.5,.055,r"Whole $L^1$ domain: $\|T_f\|\leq C_\alpha\|f\|_1$",
        ha="center",fontsize=15,color=dark)
ax.text(.5,.95,"Norm-continuous vector or predual orbits\non sigma compact integrable carriers",
        ha="center",va="top",fontsize=12,color=dark,linespacing=1.3)

ax=fig.add_subplot(gs[1,0]);ax.set_axis_off();ax.set_xlim(-1.8,1.8);ax.set_ylim(0,1)
ax.set_title("C. Compact cores and open-space closure",loc="left",color=dark,fontsize=17,pad=14)
ax.text(0,.94,r"$x_i=T_{k_i}x\ \longrightarrow_\tau\ x,\qquad \|x_i\|\leq C_\alpha\|x\|$",
        ha="center",fontsize=16,color=dark)
ax.text(0,.85,"Positive mass-one kernels; compact frequency supports (BS2–3)",
        ha="center",fontsize=11.5,color=dark)
windows=[(-1.5,1.5,.63,"V open",purple),(-1,1,.47,"E closed",blue),
         (-.5,.5,.31,"U open",green)]
for lo,hi,y,label,col in windows:
 ax.plot([lo,hi],[y,y],color=col,lw=10,alpha=.35,solid_capstyle="butt")
 ax.scatter([lo,hi],[y,y],s=55,color=col,facecolors="white" if "open" in label else col,zorder=4)
 ax.text(1.65,y,label,ha="right",va="bottom",fontsize=12,color=col)
ax.text(0,.16,r"$X_\alpha^0(U)\ \subset\ X_\alpha(E)\ \subset\ X_\alpha^0(V)$",
        ha="center",fontsize=16,color=dark)
ax.text(0,.055,r"$X_\alpha(E)=\bigcap_{V\supset E\ {\rm open}}X_\alpha^0(V)$",
        ha="center",fontsize=15,color=dark)
ax.text(-1.78,.735,"Frequency windows drawn in R for the schematic",fontsize=10.5,color="#576a7d")

ax=fig.add_subplot(gs[1,1]);ax.set_axis_off();ax.set_xlim(-.55,1.5);ax.set_ylim(0,1)
ax.set_title("D. Two filters force zero mixed frequency",loc="left",color=dark,fontsize=17,pad=14)
ax.text(.475,.94,r"$W_r(A)=\beta_rA\alpha_{-r},\quad AX_\alpha(K)\subset X_\beta(K)$",
        ha="center",fontsize=15,color=dark)
ax.plot([-.4,.4],[.78,.78],color=blue,lw=12,alpha=.25,solid_capstyle="butt")
ax.plot([1,1.4],[.78,.78],color=orange,lw=12,alpha=.55,solid_capstyle="butt")
ax.text(0,.845,r"$4V=[-0.4,0.4]$",ha="center",fontsize=12,color=blue)
ax.text(1.2,.845,r"$D_h=[1,1.4]$",ha="center",fontsize=12,color=orange)
ax.plot([-.1,.1],[.61,.61],color=green,lw=8,solid_capstyle="butt")
ax.plot([0,.2],[.56,.56],color=purple,lw=8,solid_capstyle="butt")
ax.text(.34,.585,r"$F_i\cap G_j\ne\varnothing$",fontsize=12,color=dark,va="center")
ax.text(.475,.455,r"$G_j-F_i=[-0.1,0.3]\subset 4V,\qquad D_h\cap4V=\varnothing$",
        ha="center",fontsize=13,color=dark)
ax.text(.475,.34,r"$\widehat K(\chi,\eta)=\widehat h(\eta-\chi)\widehat f_i(\chi)\widehat g_j(\eta)=0$",
        ha="center",fontsize=14,color=dark)
ax.text(.475,.245,"Disjoint patches instead vanish by the compact-space hypothesis.",
        ha="center",fontsize=11.5,color=dark)
ax.text(.475,.15,r"Two ordered core limits $\Rightarrow W_hA=0\Rightarrow{\rm sp}_W(A)\subset\{0\}$",
        ha="center",fontsize=13,color=dark)
ax.text(.475,.055,r"Singleton synthesis $\Rightarrow\beta_rA=A\alpha_r$; take $A=I$ to recover the action",
        ha="center",fontsize=12.5,color=dark)
fig.savefig(OUT/"banach-spectral-calculus.png",dpi=200,metadata={"Software":"OA-FLOW original CC0 BS renderer"})
fig.savefig(OUT/"banach-spectral-calculus.svg",metadata={"Date":None,"Creator":"OA-FLOW original CC0 BS renderer"})
def c(v):return [float(v.real),float(v.imag)]
data={"convention":"Negative forward transform; physical counting Haar and dual point mass1/6",
 "finite_model":{"zeta":"exp(2 pi i/6)","space":"C² with l1 norm","predual":"C² with linfinity norm, bilinear pairing",
  "exact_norms":["1","2","1+sqrt(3)","3","1+sqrt(3)","2"],"C":3,
  "exact_alpha3":[[1,-2],[0,-1]],"exact_alpha3_e2":[-2,-1],
  "spectral_basis":{"0":[1,0],"5":[1,1]},
  "exact_selectors":{"0":[[1,-1],[0,0]],"5":[[0,1],[0,1]]},
  "numeric_matrices":[[[c(v) for v in row] for row in m] for m in alphas],
  "numeric_norms":norms.tolist(),
  "norm_cross_check_max_error":float(max(abs(norms-expected)))},
 "schematic_windows":{"group_for_drawing_only":"Gamma=R","U":["-1/2","1/2","open"],
  "E":["-1","1","closed"],"V":["-3/2","3/2","open"],
  "recovery_small_V":["-1/10","1/10"],"4V":["-2/5","2/5"],
  "Dh":["1","7/5"],"Fi":["-1/10","1/10"],"Gj":["0","1/5"],
  "Gj_minus_Fi":["-1/10","3/10"],
  "not_a_generality_reduction":True,"schematic_intervals_are_not_claimed_numeric_filter_data":True},
 "proof_locators":["BS0–1","BS2–4","BS6–7","BS8"],"license":"CC0"}
(OUT/"banach-spectral-calculus-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"assets":[p.name for p in OUT.iterdir()],"norm_error":data["finite_model"]["norm_cross_check_max_error"]}))
