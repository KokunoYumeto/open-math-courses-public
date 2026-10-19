"""Draw the exact support-point model in Lorentz-cone lesson Figure 0.1."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"svg.fonttype":"none", "svg.hashsalt":"rounded-convex-hulls",
                     "font.size":11, "figure.facecolor":"white"})
theta = np.arange(4096)*2*np.pi/4096
n = np.column_stack((np.cos(theta),np.sin(theta)))
a = np.column_stack((.4*np.sign(n[:,0]),np.sign(n[:,1])))
k = np.array([2.,0.])+.3*n
ha = .4*np.abs(n[:,0])+np.abs(n[:,1])
hk = 2*n[:,0]+.3
h = np.where((ha>=hk)[:,None],a,k)
epsilon = .12
fig,ax = plt.subplots(figsize=(11,7.2),layout="constrained")
ax.axvspan(-1,1,color="#e7f1fc",label=r"Known zero set $U: |x_1|<1$")
ax.axvline(-1,color="#7796b4",ls=":")
ax.axvline(1,color="#7796b4",ls=":")
colors = ["#3569a8","#a36b11","#6b4696"]
for t,color in zip([0,.5,1],colors):
    p=(1-t)*a+t*h+epsilon*n
    p=np.vstack((p,p[0]))
    ax.plot(p[:,0],p[:,1],color=color,lw=2,label=rf"$C_t$ at $t={t:g}$")
ax.fill([-.4,.4,.4,-.4],[-1,-1,1,1],color="#8bb1d5",alpha=.4)
circle=np.array([2.,0.])+.3*n
ax.fill(circle[:,0],circle[:,1],color="#d9c7ed",alpha=.7)
ax.plot([-.4,.4],[1.12,1.12],color="#24724b",lw=5)
ax.plot([-.4,.4],[-1.12,-1.12],color="#24724b",lw=5)
ax.annotate(r"Characteristic face: $N=e_2$"+"\n"+r"$R(N)=0$, entire face in $U$",
            xy=(0,1.12),xytext=(.55,1.67),arrowprops={"arrowstyle":"->","color":"#24724b"},
            color="#185c3a",bbox={"facecolor":"white","edgecolor":"none","alpha":.95})
ax.annotate(r"$A=[-2/5,2/5]\times[-1,1]$",xy=(-.2,.25),xytext=(-1.67,.48),
            arrowprops={"arrowstyle":"->"},bbox={"facecolor":"white","edgecolor":"none","alpha":.95})
ax.text(1.82,-.09,r"$K$",fontsize=14)
ax.scatter([2.42],[0],color="#9e3c32",s=35,zorder=6)
ax.annotate(r"Possible contact normal $N=e_1$"+"\n"+r"$R(N)=1\ne0$: Holmgren applies",
            xy=(2.42,0),xytext=(1.18,-1.55),arrowprops={"arrowstyle":"->","color":"#9e3c32"},
            color="#8b3028",bbox={"facecolor":"white","edgecolor":"none","alpha":.95})
ax.set(xlim=(-1.8,3.1),ylim=(-1.85,2.03),xlabel=r"$x_1$",ylabel=r"$x_2$",
       title="Rounded hulls keep characteristic contacts inside the known zero set\n"
             +r"$R(\xi)=\xi_1$, $\varepsilon=3/25$, $V=\mathbb{R}^2$")
ax.set_aspect("equal",adjustable="box")
ax.grid(alpha=.18)
ax.legend(loc="upper left",fontsize=9,framealpha=.97)
out=ROOT/"figures";out.mkdir(exist_ok=True)
fig.savefig(out/"rounded-hulls-and-characteristic-faces.png",dpi=150,
            metadata={"Software":"Matplotlib; original course figure"})
fig.savefig(out/"rounded-hulls-and-characteristic-faces.svg",
            metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI), Ultra","Title":"Rounded hulls and characteristic faces"})
plt.close(fig)
fig,ax=plt.subplots(figsize=(10,6.8),layout="constrained")
angle=np.linspace(0,np.pi,1025)
upper=np.column_stack((3*np.cos(angle),3*np.sin(angle)))
ax.fill(upper[:,0],upper[:,1],color="#b8cfe6",alpha=.8,label=r"$U: y>0,\ x^2+y^2<9$")
for center,label,color in [(-2,r"$B_-$","#b9d6bf"),(2,r"$B_+$","#dfc5a6")]:
    circle=np.array([center,0.])+n
    ax.fill(circle[:,0],circle[:,1],color=color,alpha=.85,label=label)
    ax.plot(circle[:,0],circle[:,1],color="#66717d",lw=1,ls=":")
ax.plot(upper[:,0],upper[:,1],color="#66717d",lw=1,ls=":")
ax.axvline(-1,color="#486aa3",ls="--",label=r"Truncation $x>-1$")
ax.axvline(1,color="#9b6044",ls="--",label=r"Truncation $x<1$")
ax.plot([-3,-1],[0,0],color="#225e39",lw=4)
ax.plot([1,3],[0,0],color="#225e39",lw=4)
ax.plot([-1,1],[0,0],color="#a03431",ls="--",lw=2)
for x in [-3,-1,1,3]:
    ax.scatter([x],[0],s=45,facecolors="white",edgecolors="#225e39",zorder=6)
ax.annotate("Missing horizontal interval",xy=(0,0),xytext=(-.95,-1.65),
            arrowprops={"arrowstyle":"->","color":"#a03431"},color="#8c2b28",
            bbox={"facecolor":"white","edgecolor":"none","alpha":.95})
ax.set(xlim=(-3.55,3.55),ylim=(-2.15,3.55),xlabel=r"$x$",ylabel=r"$y$",
       title=r"Circular domain for $P(\xi)=\xi_1\xi_2$: two support-convex pieces cover a failure")
ax.set_aspect("equal",adjustable="box")
ax.legend(loc="upper right",fontsize=9,framealpha=.96)
ax.grid(alpha=.18)
fig.savefig(out/"circular-domain-and-truncations.png",dpi=150,
            metadata={"Software":"Matplotlib; original course figure"})
fig.savefig(out/"circular-domain-and-truncations.svg",
            metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI), Ultra","Title":"Circular domain and support-convex truncations"})
plt.close(fig)
data={"symbol":"R(xi)=xi_1","known_zero_set":"abs(x_1)<1","ambient":"R^2",
      "seed_rectangle":[[-.4,.4],[-1,1]],"target_center":[2,0],"target_radius":.3,
      "epsilon":epsilon,"parameters":[0,.5,1],"normal_samples":4096,
      "characteristic_normals":[[0,1],[0,-1]],"characteristic_face_height":1.12,
      "rightmost_point":[2.42,0],"rightmost_normal":[1,0],
      "support_functions":{"A":"(2/5)*abs(N_1)+abs(N_2)",
                           "K":"2*N_1+(3/10)*abs(N)",
                           "C_t":"(1-t)*h_A+t*max(h_A,h_K)+(3/25)*abs(N)"},
      "support_of_a_particular_solution_plotted":False,"license":"CC0-1.0",
      "circular_domain":{"upper_half_disk_radius":3,"small_disk_centers":[[-2,0],[2,0]],
                         "small_disk_radius":1,"all_pieces_open":True,
                         "horizontal_zero_slice":[[-3,-1],[1,3]],"slice_intervals_open":True,
                         "covering_halfplanes":["x>-1","x<1"]}}
(ROOT/"rounded-hulls-and-characteristic-faces.json").write_bytes(
    (json.dumps(data,indent=2,sort_keys=True)+"\n").encode())
