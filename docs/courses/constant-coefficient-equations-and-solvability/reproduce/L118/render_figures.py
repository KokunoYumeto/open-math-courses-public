"""Exact LC035 figure sources; run from any directory.

Figures are explanatory affine slices and coordinate trajectories. Their
finite samples are never mathematical evidence for the general theorem.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

BASE = Path(__file__).resolve().parent
OUT = BASE / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 12, "axes.labelsize": 11,
    "svg.hashsalt": "LC035-exact-cone-figures-v1",
})
blue, orange, green = "#175b8e", "#ba5a1b", "#237755"

def save(fig, stem):
    fig.savefig(OUT / (stem + ".png"), dpi=180, bbox_inches="tight",
                metadata={"Software": "LC035 exact reproducible matplotlib source"})
    fig.savefig(OUT / (stem + ".svg"), bbox_inches="tight",
                metadata={"Date": None, "Creator": "LC035 exact reproducible matplotlib source"})
    plt.close(fig)

fig, ax = plt.subplots(2, 3, figsize=(13.5, 8.2))
titles = [
    r"Crossing: $\xi_0=(1,1,1)$, $\mu=2$",
    r"Simple: $\xi_d=(1,1,1+d)$, $\mu=1$",
    r"Noncharacteristic: $\zeta_d=(1,1+d,1+d)$, $\mu=0$",
]
for j in range(3):
    a=ax[0,j]; a.set_title(titles[j], pad=16)
    a.set(xlim=(-1.6,1.7), ylim=(-1.6,1.7),
          xlabel=r"$v_1$ in slice $v_\tau=1$", ylabel=r"$v_2$")
    a.set_aspect("equal"); a.grid(alpha=.18)
    if j==0:
        a.add_patch(Polygon([(-1.6,-1.6),(1,-1.6),(1,1),(-1.6,1)],
                            color=blue,alpha=.16))
        a.axvline(1,color=blue,ls="--"); a.axhline(1,color=blue,ls="--")
        a.text(-1.38,.57,r"$v_1<1,\quad v_2<1$",color=blue)
    elif j==1:
        a.axvspan(-1.6,1,color=blue,alpha=.16)
        a.axvline(1,color=blue,ls="--")
        a.text(-1.32,.57,r"$v_1<1$; $v_2$ free",color=blue)
    else:
        a.set_facecolor("#e8f1f7")
        a.text(-1.3,.57,r"$\Gamma_{\zeta_d}=\mathbb{R}^3$",color=blue)
    a.scatter([0],[0],color=green,s=45,zorder=5)
    a.annotate(r"$N$", (0,0),xytext=(.16,-.25),color=green)
    b=ax[1,j]
    b.set(xlim=(-1.25,.35),ylim=(-1.25,.35),
          xlabel=r"$x_1$ in slice $x_\tau=1$",ylabel=r"$x_2$")
    b.set_aspect("equal"); b.grid(alpha=.18)
    if j==0:
        b.plot([-1,0],[0,-1],color=orange,lw=3)
        b.scatter([-1,0],[0,-1],color=orange,s=55,zorder=5)
        b.text(-1.1,-1.16,r"$s+t=1,\ s,t\geq0$",color=orange)
        b.set_title("Positive polar slice: closed segment")
    elif j==1:
        b.scatter([-1],[0],color=orange,s=65,zorder=5)
        b.annotate(r"$(x_1,x_2)=(-1,0)$",(-1,0),xytext=(-1.12,-.31),color=orange)
        b.set_title("Positive polar slice: one included point")
    else:
        b.text(-1.1,-.48,"Empty slice",fontsize=16,color=orange)
        b.text(-1.1,-.71,r"$C_{\zeta_d}=\{0\}$ has $x_\tau=0$",color=orange)
        b.set_title("Positive polar slice: empty")
fig.suptitle("Exact variation of tangent components and positive polars",
             fontsize=17,y=.99)
fig.text(.5,.015,"Top boundaries are excluded. Lower polar points and segment are included. "
         "d is any nonzero real number.",ha="center",fontsize=10)
fig.subplots_adjust(hspace=.40,wspace=.28,top=.91,bottom=.10)
save(fig,"crossing-cone-variation")

fig, ax=plt.subplots(1,3,figsize=(15,4.8))
a=ax[0]
a.add_patch(Circle((0,0),1,facecolor=blue,alpha=.07,edgecolor="none"))
t=np.linspace(-1.6,1.6,400)
phis=[0,np.pi/3,2*np.pi/3]
colors=[blue,orange,green]
for phi,col in zip(phis,colors):
    normal=np.array([np.cos(phi),np.sin(phi)])
    tangent=np.array([-np.sin(phi),np.cos(phi)])
    pts=normal[:,None]+tangent[:,None]*t
    a.plot(pts[0],pts[1],ls="--",color=col,
           label=rf"$\phi={round(phi/np.pi*3):d}\pi/3$")
    a.annotate("",xy=.55*normal,xytext=normal,
               arrowprops={"arrowstyle":"->","color":col,"lw":1.8})
a.add_patch(Circle((0,0),1,fill=False,color="#777777",lw=1))
a.scatter([0],[0],color="#333333",s=30)
a.text(.07,-.16,r"$N$",fontsize=11)
a.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65),xlabel=r"$v_1$",
      ylabel=r"$v_2$",title=r"Wave tangent halfplanes: $v_\tau=1$")
a.set_aspect("equal"); a.grid(alpha=.16); a.legend(fontsize=9,loc="lower left")

eps=np.linspace(0,1,300)
b=ax[1]
b.plot(eps**2/4,eps/np.sqrt(2),color=blue,label="plus imaginary push")
b.plot(eps**2/4,-eps/np.sqrt(2),color=orange,label="minus imaginary push")
b.scatter([0],[0],s=70,facecolors="white",edgecolors="black",zorder=6)
b.annotate(r"$\varepsilon=0$ excluded",(0,0),xytext=(.055,.075),fontsize=10)
for e in (.5,1):
    b.scatter([e*e/4],[e/np.sqrt(2)],color=blue,s=24)
    b.annotate(rf"$\varepsilon={e:g}$",(e*e/4,e/np.sqrt(2)),
               xytext=(5,-14),textcoords="offset points",fontsize=9)
b.set(xlim=(-.025,.325),ylim=(-.79,.79),xlabel=r"$\operatorname{Re}F$",
      ylabel=r"$\operatorname{Im}F$",
      title=r"$F(\xi_*\pm i\varepsilon V)=\varepsilon^2/4\pm i\varepsilon/\sqrt{2}$")
b.grid(alpha=.18); b.legend(fontsize=9,loc="lower left")

tau=np.linspace(-1,1,1501); u=tau*tau; e=.25
re=2*u-1+e*e*u*(1-u); im=2*e*tau*(1-u)
mod=np.sqrt(re*re+im*im)
c=ax[2]
c.plot(tau,mod,color=blue,lw=2,label=r"exact modulus, $\varepsilon=1/4$")
c.axhline(e/4,color=orange,ls="--",label=r"proved bound $\varepsilon/4=1/16$")
for q in (-1/np.sqrt(2),1/np.sqrt(2)):
    c.axvline(q,color="#777777",ls=":",alpha=.55)
c.set(xlim=(-1,1),ylim=(0,1.05),xlabel=r"$\tau$ on the unit meridian",
      ylabel=r"$|F(\xi\pm i\varepsilon V(\xi))|$",
      title="Uniform exclusion includes noncharacteristic zeros of V")
c.grid(alpha=.16); c.legend(fontsize=9,loc="upper center")
fig.suptitle("Exact wave geometry and the imaginary exclusion mechanism",fontsize=17,y=1.015)
fig.tight_layout()
save(fig,"wave-imaginary-exclusion")

record={
 "schema":"LC035-exact-figure-geometry/v1",
 "crossing":{
  "polynomial":"(tau-eta1)(tau-eta2)","normal":[1,0,0],
  "crossing_frequency":[1,1,1],"simple_frequency":"(1,1,1+d), d != 0",
  "noncharacteristic_frequency":"(1,1+d,1+d), d != 0",
  "component_slice":"v_tau=1",
  "crossing_component_inequalities":["v1<1","v2<1"],
  "simple_component_inequalities":["v1<1"],
  "polar_slice":"x_tau=1",
  "crossing_polar_segment":[[-1,0],[0,-1]],
  "simple_polar_point":[-1,0],"noncharacteristic_polar_slice_empty":True,
 },
 "wave":{
  "polynomial":"tau^2-eta1^2-eta2^2","normal":[1,0,0],
  "field":"(0,-tau*eta/(tau^2+|eta|^2))",
  "angles_radians":[0,float(np.pi/3),float(2*np.pi/3)],
  "frequency_trajectory":"xi_star=(1,1,0)/sqrt(2)",
  "F_trajectory":"eps^2/4 +/- i*eps/sqrt(2)",
  "meridian":"xi=(tau,sqrt(1-tau^2),0), -1<=tau<=1",
  "eps_meridian":e,"proved_uniform_lower_bound":e/4,
  "all_boundaries_and_directions":"exact formulas; sampled only for rendering",
 },
 "proof_locators":["LC035-2","LC035-3","LC035-4","lesson E1-E3"],
 "not_claimed":["full cone volumes drawn","sampling establishes theorem","root multiplicity is a simple-root count"],
}
(OUT/"geometry.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print("Rendered two exact figures as PNG and SVG; geometry.json retained.")
