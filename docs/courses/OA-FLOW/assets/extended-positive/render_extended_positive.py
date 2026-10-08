"""A closed form with an infinite projection, and exact bounded truncations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "OA-FLOW-extended-positive-v1"

d=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,7))
gs=fig.add_gridspec(1,3,left=.03,right=.98,top=.76,bottom=.34,wspace=.3)
ax=fig.add_subplot(gs[0],projection="3d")
th=np.linspace(0,2*np.pi,241)
ax.plot(np.cos(th),.5*np.sin(th),np.zeros_like(th),color="#176d80",lw=3)
xx,yy=np.meshgrid(np.linspace(-1.1,1.1,3),np.linspace(-.65,.65,3))
ax.plot_surface(xx,yy,np.zeros_like(xx),alpha=.13,color="#4b9c9b")
ax.plot([0,0],[0,0],[0,1.1],color="#b15d28",lw=2,ls="--")
ax.scatter([0],[0],[1],s=35,color="#b15d28")
ax.text(0,.06,1.04,r"$e_3:\ q=\infty$",fontsize=11,color="#a95424")
ax.text(-.9,-.6,.02,r"$q=1$",fontsize=12,color="#176d80")
ax.set_xlabel(r"$x_1$",labelpad=2);ax.set_ylabel(r"$x_2$",labelpad=2);ax.set_zlabel(r"$x_3$",labelpad=2)
ax.set_xlim(-1.15,1.15);ax.set_ylim(-.7,.7);ax.set_zlim(0,1.15)
ax.set_xticks([-1,1]);ax.set_yticks([-.5,.5]);ax.set_zticks([0,1])
ax.view_init(elev=22,azim=-52);ax.set_box_aspect((1.5,1,1))
ax.set_title("Finite domain: a complex 2-plane\nD = span(e₁, e₂); real slice shown",fontsize=12,pad=9)
ax.text2D(.5,-.23,r"$q(x_1,x_2,0)=|x_1|^2+4|x_2|^2$"+"\n"+r"$q(x_1,x_2,x_3)=\infty$ if $x_3\ne0$",
          transform=ax.transAxes,ha="center",fontsize=11)

ax=fig.add_subplot(gs[1]);theta=np.linspace(0,np.pi/2,251)
for n,c in zip([1,2,4,8,16],["#666666","#507c91","#308578","#b48a27","#ac4c28"]):
    ax.plot(theta,np.cos(theta)**2+n*np.sin(theta)**2,color=c,lw=2,label=f"n = {n}")
ax.set_title(r"$v_\theta=\cos\theta\,e_1+\sin\theta\,e_3$",fontsize=13,pad=14)
ax.set_xlabel(r"$\theta$");ax.set_ylabel(r"$\langle a_n v_\theta,v_\theta\rangle$")
ax.set_xticks([0,np.pi/4,np.pi/2],["0",r"$\pi/4$",r"$\pi/2$"])
ax.set_ylim(0,17);ax.grid(alpha=.15);ax.legend(loc="upper left",fontsize=9,frameon=False)
ax.text(.5,-.31,r"$\cos^2\theta+n\sin^2\theta$"+"\n"+r"Limit: $1$ at $\theta=0$; $\infty$ at every $\theta>0$",
        transform=ax.transAxes,ha="center",fontsize=11)

ax=fig.add_subplot(gs[2]);delta=np.linspace(0,1,251)
for n,c in zip([4,8,16],["#308578","#b48a27","#ac4c28"]):
    ax.plot(delta,4*(1-delta)+n*delta,color=c,lw=2,label=f"n = {n}")
ax.scatter([0],[4],color="#176d80",s=40,zorder=5)
ax.set_title(r"$f_\delta=(1-\delta)\omega_{e_2}+\delta\omega_{e_3}$",fontsize=13,pad=14)
ax.set_xlabel(r"$\delta$");ax.set_ylabel(r"$f_\delta(a_n)$")
ax.set_ylim(0,17);ax.grid(alpha=.15);ax.legend(loc="upper left",fontsize=10,frameon=False)
ax.text(.5,-.31,r"$4(1-\delta)+n\delta$ for $n\geq4$"+"\n"+r"$m(f_0)=4$; $m(f_\delta)=\infty$ for every $\delta>0$",
        transform=ax.transAxes,ha="center",fontsize=11)
fig.suptitle("The infinite-value part belongs to the extended positive element",fontsize=18,fontweight="bold",y=.985)
fig.text(.5,.885,r"$e=\mathrm{diag}(1,1,0),\quad A=\mathrm{diag}(1,4)\ \mathrm{on}\ e\mathbb{C}^3,\quad p=1-e,\quad a_n=\mathrm{diag}(1,\min(4,n),n)$",
         ha="center",fontsize=13)
fig.text(.5,.035,"Exact M₃ example. EP-2–3 prove the arbitrary-Hilbert representation; EP-5 preserves the infinite part in scalar-weight extension.",
         ha="center",fontsize=11)
fig.savefig(d/"assets"/"extended-positive.png",dpi=180,bbox_inches="tight")
fig.savefig(d/"assets"/"extended-positive.svg",bbox_inches="tight",metadata={"Date":None})
plt.close(fig)
(d/"extended-positive-numerics.json").write_text(json.dumps({
 "finite_projection":[1,1,0],"finite_operator_eigenvalues":[1,4],"infinite_projection":[0,0,1],
 "cutoff_diagonal":"[1,min(4,n),n] for integers n>=1",
 "vector_path":"cos(theta)e1+sin(theta)e3, 0<=theta<=pi/2",
 "vector_cutoff":"cos(theta)^2+n sin(theta)^2",
 "functional_path":"(1-delta)omega_e2+delta omega_e3",
 "functional_cutoff":"4(1-delta)+n delta for n>=4",
 "complete_proof":"EXTENDED-POSITIVE-FIGURE.md",
 "scope":"All formulas exact; finite set of plotted cutoffs only illustrates the proved increasing limit."
},indent=2)+"\n",encoding="utf-8")
