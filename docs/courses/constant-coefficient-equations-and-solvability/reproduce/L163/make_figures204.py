"""Original harmonic-barrier and atomic-division illustrations."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.fonttype":"path",
                     "svg.hashsalt":"slow-decrease204","axes.grid":True,"grid.alpha":.2})
BLUE,RED,GREEN="#15618a","#b44236","#26774f"
def save(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=160,bbox_inches="tight",
                metadata={"Software":"Matplotlib;original mathematical figure"})
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight",
                metadata={"Date":None,"Creator":"Original mathematical figure"})
    plt.close(fig)
t=np.linspace(-1,1,401);s=np.linspace(0,1,301);T,S=np.meshgrid(t,s)
omega=np.sin(np.pi*(T+1)/2)*np.sinh(np.pi*(1-S)/2)/np.sinh(np.pi/2)
fig,axes=plt.subplots(1,2,figsize=(12.4,4.55))
mesh=axes[0].imshow(omega,origin="lower",extent=(-1,1,0,1),aspect="auto",
                    cmap="viridis",vmin=0,vmax=1)
axes[0].set(xlabel=r"Real line parameter $t$",ylabel=r"Imaginary line parameter $s$",
            title=r"Positive harmonic weight $\omega(t,s)$")
axes[0].scatter([0],[.5],color="white",edgecolor=RED,s=55,zorder=5)
axes[0].annotate(r"$\omega(0,1/2)=\sinh(\pi/4)/\sinh(\pi/2)$",
                 xy=(0,.5),xytext=(-.9,.8),color="white",fontsize=10,
                 arrowprops={"arrowstyle":"->","color":"white"})
axes[0].text(0,.035,"Bottom: the small real values",color="white",ha="center",fontsize=10)
axes[0].grid(False);fig.colorbar(mesh,ax=axes[0],fraction=.045,pad=.03,label="Exact harmonic weight")
theta=np.linspace(0,np.pi/2,301);factor=np.cos(1.5*(theta-np.pi/4));c0=np.cos(3*np.pi/8)
axes[1].plot(theta,factor,color=BLUE,lw=2.5,label=r"$H_1(re^{i\theta})/r^{3/2}$")
axes[1].axhline(c0,color=RED,ls="--",lw=2,label=r"$c_0=\cos(3\pi/8)>0$")
axes[1].set(xlabel=r"Angle $\theta$ in the first quadrant",ylabel="Positive angular factor",
            ylim=(0,1.1),title="A barrier stronger than linear growth")
axes[1].set_xticks([0,np.pi/4,np.pi/2],["0",r"$\pi/4$",r"$\pi/2$"])
axes[1].legend(fontsize=10,loc="lower center")
fig.suptitle("From real smallness to complex bounds",fontsize=15)
fig.tight_layout(rect=(0,0,1,.92));save(fig,"real-smallness-and-half-plane-barriers")
center=2*np.pi*10**6;alphas=[.1,.25];radii=[a*np.log(2+center)for a in alphas]
offset=np.linspace(-5,5,1001);modulus=2*np.abs(np.sin(offset/2))
fig,axes=plt.subplots(1,2,figsize=(12.4,4.65))
for a,r,color in zip(alphas,radii,[GREEN,BLUE]):
    axes[0].axvspan(-r,r,color=color,alpha=.1,label=f"a={a}, radius={r:.3f}")
    axes[0].axvline(-r,color=color,ls="--",lw=1)
    axes[0].axvline(r,color=color,ls="--",lw=1)
axes[0].plot(offset,modulus,color=RED,lw=2.5)
axes[0].scatter([-np.pi,0,np.pi],[2,0,2],color=RED,s=32,zorder=5)
axes[0].set(xlabel=r"Real offset $t=\xi-c$, $c=2\pi\cdot10^6$",
            ylabel=r"$|1-e^{-i(c+t)}|=2|\sin(t/2)|$",
            ylim=(-.1,2.4),title="A zero center still has good windows")
axes[0].legend(loc="upper right",fontsize=9)
axes[1].grid(False)
data=[(2,[0,1],[1,-1],r"$u=\delta_0-\delta_1$"),
      (1,[0,1,2],[1,1,1],r"$g=\delta_0+\delta_1+\delta_2$"),
      (0,[0,3],[1,-1],r"$u*g=\delta_0-\delta_3$")]
for y,locations,signs,label in data:
    axes[1].axhline(y,color="#bbbbbb",lw=.8)
    for x,sign in zip(locations,signs):
        color=BLUE if sign>0 else RED
        axes[1].scatter([x],[y],s=80,color=color,zorder=5,marker="o"if sign>0 else"s")
        axes[1].text(x,y+.17,"+1"if sign>0 else"−1",ha="center",color=color,fontsize=11)
    axes[1].text(-.48,y+.39,label,ha="left",va="center",fontsize=10)
axes[1].set(xlim=(-.65,3.3),ylim=(-.45,2.55),xlabel="Point-mass location",
            title="An exact compact atomic quotient")
axes[1].set_yticks([]);axes[1].set_xticks([0,1,2,3])
fig.suptitle("Slow decrease allows infinitely many transform zeros",fontsize=15)
fig.tight_layout(rect=(0,0,1,.92));save(fig,"zeros-in-logarithmic-windows-and-division")
geometry=dict(authorship="Original mathematics and figures;GPT-6.1 Sol (OpenAI),Ultra;CC0 1.0",
    harmonic_rectangle=dict(domain=[[-1,1],[0,1]],
        formula="sin(pi*(t+1)/2)*sinh(pi*(1-s)/2)/sinh(pi/2)",
        boundary="zero on top and vertical sides;between0 and1 on bottom",
        marked_point=[0,.5],marked_value=float(np.sinh(np.pi/4)/np.sinh(np.pi/2)),
        proof_locators=["Formal Lemma2.1","Learner Exercise4"]),
    quadrant_barrier=dict(angles=[0,float(np.pi/2)],power=1.5,
        angular_formula="cos(3*(theta-pi/4)/2)",positive_minimum=float(c0),
        exact_minimum="cos(3*pi/8)",proof_locators=["Formal Lemma3.1","Learner Exercise5"]),
    windows=dict(center="2*pi*10^6",radius_formula="a*log(2+c)",coefficients=alphas,radii=radii,
        exact_real_modulus="2*abs(sin(t/2))",zero_at_center=True,
        peaks_offsets=[-float(np.pi),float(np.pi)],proof_locators=["Learner Example2","Formal Theorem1.1"]),
    atomic_division=dict(divisor={"locations":[0,1],"weights":[1,-1]},
        quotient={"locations":[0,1,2],"weights":[1,1,1]},product={"locations":[0,3],"weights":[1,-1]},
        formula="(1-exp(-i*z))*(1+exp(-i*z)+exp(-2i*z))=1-exp(-3i*z)",
        markers_are_point_masses_not_densities=True),
    references=["Terence Tao,246B Notes2 and245B Notes9","Lars Hörmander,Analysis of Linear Partial Differential Operators I and II"])
(OUT/"geometry204.json").write_text(json.dumps(geometry,indent=2,allow_nan=False)+"\n",encoding="utf-8")
print(json.dumps(dict(figures=2,formats=["PNG","SVG"],exact_geometry=True)))
