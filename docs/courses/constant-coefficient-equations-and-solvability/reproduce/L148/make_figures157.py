"""Exact original scientific figures for CF17–CF25 and CF44–CF46; no TeX."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = Path(__file__).resolve().parent
OUT = HERE/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.titlesize": 12, "axes.labelsize": 11, "legend.fontsize": 9,
    "svg.hashsalt": "AN02-L148-original-CF-2026-10",
    "savefig.facecolor": "white",
})


def save(fig, name):
    fig.savefig(OUT/(name+".png"), dpi=180, metadata={"Software":"Original AN-02 L148; GPT-6.1 Sol, Ultra; CC0"})
    fig.savefig(OUT/(name+".svg"), metadata={"Date":None, "Creator":"Original AN-02 L148; GPT-6.1 Sol, Ultra; CC0"})
    plt.close(fig)


fig, ax = plt.subplots(1, 3, figsize=(13.2, 4.7))
fig.subplots_adjust(left=.055, right=.985, bottom=.25, top=.83, wspace=.38)
fig.suptitle("Compact support controls imaginary Fourier shifts", fontsize=15, y=.97)
x = np.linspace(-1.5, 1.5, 1801)
inside = (abs(x)<=1)
ax[0].plot(x, inside.astype(float), color="#475569", lw=2, label=r"$u=1_{[-1,1]}$")
ax[0].plot(x, np.where(inside,np.exp(x),0), color="#2563eb", lw=2,
           label=r"$e^x u$ (shift $\eta=1$)")
ax[0].fill_between(x,0,inside.astype(float),color="#cbd5e1",alpha=.5)
ax[0].axvline(-1,color="#64748b",ls=":",lw=1)
ax[0].axvline(1,color="#64748b",ls=":",lw=1)
ax[0].set(xlabel=r"$x$", ylabel="physical function", title=r"$K=[-1,1]$, $H_K(\eta)=|\eta|$",
          xlim=(-1.5,1.5), ylim=(-.05,3.15))
ax[0].legend(loc="upper left")
xi = np.linspace(-8,8,1601)
for eta, color in zip((0.,.5,1.,2.),("#475569","#2563eb","#ea580c","#059669")):
    if eta == 0:
        energy = 4*np.sinc(xi/np.pi)**2
    else:
        q = np.exp(-2*eta)
        energy = (1+q*q-2*q*np.cos(2*xi))/(xi*xi+eta*eta)
    ax[1].plot(xi,energy,color=color,lw=1.4,label=rf"$\eta={eta:g}$")
ax[1].set(xlabel=r"$\xi$", ylabel=r"$e^{-2|\eta|}|F_u(\xi+i\eta)|^2$",
          title="Exact support-damped transforms", xlim=(-8,8), ylim=(-.03,4.15))
ax[1].legend(loc="upper right")
eta = np.linspace(0,6,1201)
ratio = np.ones_like(eta)
ratio[1:] = -np.expm1(-4*eta[1:])/(4*eta[1:])
ax[2].plot(eta,ratio,color="#2563eb",lw=2,label=r"$e^{-2|\eta|}I_1(\eta)/(4\pi)$")
ax[2].axhline(1,color="#64748b",ls="--",lw=1,label="proved interval ceiling")
sample = np.array([.5,1,2,4])
physical = [quad(lambda x: math.exp(2*t*x-2*t),-1,1)[0]/2 for t in sample]
ax[2].scatter(sample,physical,color="#ea580c",s=26,zorder=4,label="physical quadrature")
ax[2].set(xlabel=r"$|\eta|$", ylabel="normalized plane energy", title="Exponential growth removed",
          xlim=(0,6), ylim=(0,1.13))
ax[2].legend(loc="upper right")
for a in ax: a.grid(alpha=.2)
fig.text(.055,.11,r"$F_u(z)=2\sin z/z$, with $F_u(0)=2$.  "
         r"$I_1(\eta)=2\pi\int_{-1}^{1}e^{2\eta x}\,dx$.",fontsize=11)
fig.text(.055,.045,"Proof: CF3–CF6; exact interval calculation: learner example 1. "
         "The ceiling one is specific to this model.",fontsize=10)
save(fig,"complex-planes-and-support-damping")

fig, ax = plt.subplots(1, 2, figsize=(12.2,5.5))
fig.subplots_adjust(left=.075,right=.98,bottom=.25,top=.83,wspace=.34)
fig.suptitle("A singular measure can define a weak integral without pointwise absolute convergence",
             fontsize=13,y=.96)
ax[0].axhline(0,color="#be123c",lw=3,label=r"$d\mu=d\xi$ on the real axis")
ax[0].axvline(0,color="#94a3b8",lw=1)
center=(.25,.5)
ax[0].add_patch(Circle(center,1,fill=False,color="#2563eb",ls="--",lw=1.7))
half=math.sqrt(3)/2
ends=[center[0]-half,center[0]+half]
ax[0].plot(ends,[0,0],color="#be123c",lw=7,alpha=.4)
ax[0].scatter(ends,[0,0],s=45,facecolor="white",edgecolor="#be123c",zorder=4)
ax[0].scatter([center[0]],[center[1]],color="#2563eb",s=22)
ax[0].annotate(r"center $1/4+i/2$",xy=center,xytext=(-1.8,1.2),
               arrowprops={"arrowstyle":"->","color":"#2563eb"},fontsize=10)
ax[0].annotate(r"real-axis mass $=\sqrt{3}\leq 2$",xy=(.25,0),xytext=(-1.85,-.8),
               arrowprops={"arrowstyle":"->","color":"#be123c"},fontsize=10)
ax[0].set(xlabel=r"$\xi$",ylabel=r"$\eta$",title="Open unit ball; measure in one real dimension",
          xlim=(-2.1,2.1),ylim=(-1.15,1.65),aspect="equal")
ax[0].legend(loc="lower right",fontsize=8.5)
V=lambda t:(1+t*t)**(-3/8)
Ts=np.geomspace(1.05,1e5,180)
absolute=np.array([2*quad(V,0,T,epsabs=1e-8,epsrel=1e-9,limit=300)[0] for T in Ts])
squared=np.array([2*quad(lambda t:V(t)**2,0,T,epsabs=1e-8,epsrel=1e-9,limit=300)[0] for T in Ts])
lower=8*2**(-3/8)*(Ts**.25-1)
data_total=2*quad(lambda t:V(t)**2,0,np.inf,epsabs=1e-9,limit=300)[0]
ax[1].loglog(Ts,absolute,color="#be123c",lw=2,label=r"$2\int_0^T V(\xi)\,d\xi$")
ax[1].loglog(Ts,lower,color="#be123c",ls=":",lw=1.6,label="proved divergence lower bound")
ax[1].loglog(Ts,squared,color="#2563eb",lw=2,label=r"$2\int_0^T V(\xi)^2\,d\xi$")
ax[1].axhline(data_total,color="#2563eb",ls="--",lw=1,label="finite squared integral (quadrature)")
ax[1].set(xlabel=r"truncation $T>1$",ylabel="positive integrals",
          title=r"$V(\xi)=(1+\xi^2)^{-3/8}$",xlim=(1,1e5))
ax[1].legend(loc="lower right")
for a in ax:a.grid(alpha=.2)
fig.text(.075,.115,r"$X=(-2,2)$, $k=1$, $\phi(\xi+i\eta)=2\sqrt{1+\eta^2}$; "
         r"the squared-data norm is $e^4$ times the blue integral.",fontsize=10.5)
fig.text(.075,.055,"Proof: CF8–CF12. Unit-ball mass ≤ 2; squared-data tail ≤ "
         r"$4T^{-1/2}$. Absolute integral diverges for every real $x$.",fontsize=10)
save(fig,"singular-measure-and-weak-integral")

geometry={
    "schema":"AN02-L148-original-figure-geometry/v1",
    "interval":{"support":[-1,1],"shifted_physical_eta":1,"complex_plane_eta":[0,.5,1,2],
                "support_function":"abs(eta)","plane_ratio":"(1-exp(-4*abs(eta)))/(4*abs(eta)); value 1 at eta=0",
                "plane_ratio_ceiling_is_model_specific":True,"proof":"CF3–CF6; learner example 1"},
    "measure":{"support":"entire real axis in C","unit_ball_center":[.25,.5],"unit_ball_radius":1,
               "intersection_endpoints":ends,"mass":math.sqrt(3),"uniform_unit_ball_mass_bound":2,
               "V":"(1+xi^2)^(-3/8)","phi":"2*sqrt(1+eta^2)","data_squared_multiplier":"exp(4)",
               "T_min":float(Ts[0]),"T_max":float(Ts[-1]),"proved_squared_tail":"4*T^(-1/2)",
               "proved_divergence_lower_bound":"8*2^(-3/8)*(T^(1/4)-1)",
               "finite_squared_integral_quadrature":data_total,"proof":"CF8–CF12"},
    "figures_are_original":True,"numeric_curves_do_not_replace_proofs":True,
    "no_protected_source_media":True,"Blender_needed":False,
    "Blender_reason":"Exact one-dimensional functions and a two-dimensional measure geometry are clearer as reproducible scientific plots.",
}
(OUT/"geometry.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure_pairs":2,"geometry":"figures/geometry.json"}))
