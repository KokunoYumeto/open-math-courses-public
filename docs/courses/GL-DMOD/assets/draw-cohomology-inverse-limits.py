"""Reproduce the compact-quotient and convergent-primitive diagram."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "svg.hashsalt":"GL-DMOD-ML-20261020"})
fig,axes=plt.subplots(1,2,figsize=(13.5,6.8),facecolor="#f7f9fd")
blue="#2856a8";teal="#007c88";ink="#17213a";gold="#bc791d"
for ax in axes:
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
def box(ax,x,y,w,h,lines):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
        facecolor="white",edgecolor="#a8bddd",linewidth=1.1))
    for i,(line,color) in enumerate(lines):
        ax.text(x+w/2,y+h-(i+1)*h/(len(lines)+1),line,
                ha="center",va="center",color=color)
def arrow(ax,x,y0,y1):
    ax.annotate("",xy=(x,y1),xytext=(x,y0),
                arrowprops={"arrowstyle":"->","color":teal,"lw":1.6})
a=axes[0]
a.text(.5,.975,"Compact perturbation and actual cohomology",
       ha="center",va="top",color=ink,weight="bold")
box(a,.04,.70,.92,.19,[
    (r"$g:Z^q(E)\oplus F^{q-1}\longrightarrow Z^q(F)$",blue),
    (r"$g(x,y)=\rho^q x+d_Fy$; $g$ is surjective",ink)])
arrow(a,.5,.686,.620)
box(a,.04,.42,.92,.19,[
    (r"$h(x,y)=-\rho^q x$ is compact",teal),
    (r"$(g+h)(x,y)=d_Fy$",blue)])
arrow(a,.5,.406,.340)
box(a,.04,.12,.92,.21,[
    (r"$B^q(F)$ is closed and has finite codimension",ink),
    (r"$H^q(F)=Z^q(F)/B^q(F)$",blue),
    ("Finite dimensional and Hausdorff (ML.A–ML.C)",ink)])
a.text(.5,.035,"The premise is surjectivity of "+r"$H^q(\rho)$.",
       ha="center",va="center",color=ink)
a=axes[1]
a.text(.5,.975,"Corrections in the preceding degree",
       ha="center",va="top",color=ink,weight="bold")
box(a,.04,.72,.92,.17,[
    (r"$r_nx_{n+1}-x_n=d_ny_n$",blue),
    (r"$B_n(y_n,0)<2^{-n-1}$",teal)])
arrow(a,.5,.706,.640)
box(a,.04,.43,.92,.20,[
    (r"$Y_k=\sum_{n\geq k}r_{nk}y_n$",blue),
    (r"$\xi_k=x_k+d_kY_k$",teal),
    (r"$r_k\xi_{k+1}=\xi_k$ (ML.25–ML.29)",ink)])
a.text(.5,.365,"Error bounds; these are envelopes, not measured errors",
       ha="center",va="center",fontsize=9,color=ink)
for n in range(6):
    x=.11+n*.15;val=2**(-n-1)
    a.bar(x,val*.35,bottom=.12,width=.075,color=teal,alpha=.75)
    a.text(x,.092,str(n),ha="center",va="center",fontsize=9,color=ink)
a.text(.5,.045,r"$\sum_{n=0}^{5}2^{-n-1}=63/64$; tail $=1/64$",
       ha="center",va="center",color=gold,fontsize=10)
fig.subplots_adjust(left=.025,right=.975,top=.98,bottom=.025,wspace=.13)
for ext in ["png","svg"]:
    args={"dpi":160}if ext=="png"else{"metadata":{"Date":None}}
    fig.savefig(root/("cohomology-inverse-limits."+ext),facecolor=fig.get_facecolor(),**args)
plt.close(fig)
data={"proof_locators":["ML.A--ML.C","ML.25--ML.29"],
      "cycle_discrepancy":"r_n x_(n+1) - x_n = d_n y_n",
      "primitive_error_bound":"B_n(y_n,0) < 2^(-n-1)",
      "envelopes":[{"n":n,"bound":str(Fraction(1,2**(n+1)))}for n in range(6)],
      "finite_envelope_sum":str(sum(Fraction(1,2**(n+1))for n in range(6))),
      "remaining_envelope_sum":"1/64",
      "compact_map":"h(x,y)=-rho^q(x)",
      "surjection":"g(x,y)=rho^q(x)+d_F(y)",
      "perturbed_image":"B^q(F)",
      "not_a_numerical_error_sample":True}
(root/"cohomology-inverse-limits-exact-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
