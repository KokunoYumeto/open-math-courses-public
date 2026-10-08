from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(16,10.8),dpi=145)
fig.patch.set_facecolor("#fbfbf7")
ax.set_xlim(0,16);ax.set_ylim(0,10.8);ax.axis("off")
ink="#163b3a"; muted="#416261"
def box(x,y,w,h,face):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.12,rounding_size=0.13",facecolor=face,edgecolor=ink,linewidth=1.5))
def label(x,y,s,size=16,bold=False,color=ink):
 ax.text(x,y,s,ha="left",va="top",fontsize=size,fontweight="bold" if bold else "normal",color=color,linespacing=1.5)
def arrow(x1,y1,x2,y2):
 ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=17,color=ink,linewidth=1.6))
label(.3,10.45,"Singular pieces are included in the isotropic image bound",24,True)
label(.3,9.93,r"$Z=\mathbf{P}^n\times D$,  $\dim D=m$,  $\dim Z=d=n+m$;  $\Lambda\subset T^*Z$ closed, conic and Lagrangian",15,color=muted)
box(.3,6.55,15.4,2.78,"#e9eef9")
label(.62,9.02,"1. An actual finite-branch family reaches a singular analytic piece",19,True)
label(.62,8.48,r"Finite parametrization $\pi:A_0\to V_0$; a local analytic $S\subset A$ may lie wholly in $A_{\rm sing}$.",15)
label(.62,7.92,r"$\pi F(s,u)=(s,b\,u^e)$",21)
label(6.2,7.92,r"$F(s,u)\in A_{\rm reg}$ for $u\ne0$",21)
label(.62,7.28,r"$F(s,0)=\sigma(s)\in S$;  $e$ kills the finite covering monodromy.",17)
label(.62,6.89,r"Bounded removal gives $F$ holomorphic at $u=0$:  $F^*\alpha=0\ \Longrightarrow\ \alpha|_{S_{\rm reg}}=0$  (Lemma 5.11.1).",15)
arrow(8,6.42,8,6.05)
box(.3,3.06,15.4,2.78,"#e4f0ec")
label(.62,5.56,"2. The cotangent correspondence retains the tautological one-form",19,True)
label(.62,4.99,r"$W=Z\times_D T^*D$",20)
label(6.2,4.99,r"$j(x,y;\eta)=(x,y;0,\eta)$",20)
label(.62,4.42,r"$q(x,y;\eta)=(y,\eta)$",20)
label(6.2,4.42,r"$j^*\theta_Z=q^*\theta_D$",20)
label(.62,3.86,r"$\theta_Z=\iota_E(d\theta_Z)$ vanishes on $\Lambda_{\rm reg}$; Lemma 5.11.1 carries this to every smooth piece of $j^{-1}\Lambda$.",15)
label(.62,3.44,"The zero in j is the vertical covector. Neither smoothness of the intersection nor transversality is assumed.",14,color=muted)
arrow(8,2.93,8,2.55)
box(.3,.32,15.4,2.05,"#f4edd7")
label(.62,2.12,"3. Proper coherent image + the proved rank cover give the target bound",19,True)
label(.62,1.58,r"$B=q(j^{-1}\Lambda)$ is closed conic analytic; countable constant-rank pieces cover its source.",15)
label(.62,1.09,r"$\theta_D|_{B_{\rm smooth}}=0\quad\Longrightarrow\quad d\theta_D|_{B_{\rm smooth}}=0\quad\Longrightarrow\quad\dim B\leq m$",21)
label(.62,.56,"Schematic proof mechanism (5.11a–5.11l). Actual output-symbol comparison: Theorem 5.12, (5.12e).",14,color=muted)
fig.tight_layout(pad=.4)
fig.savefig(base/"projective-isotropic-image-proof.png",bbox_inches="tight",facecolor=fig.get_facecolor())
fig.savefig(base/"projective-isotropic-image-proof.svg",bbox_inches="tight",facecolor=fig.get_facecolor())
