"""Reproduce exact Hermite collision scales and branched projection area."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "svg.hashsalt":"AN02-L151-original166",
                     "axes.spines.top":False,"axes.spines.right":False})
def save(fig,stem):
    fig.savefig(OUT/(stem+'.png'),dpi=150,bbox_inches='tight',
                metadata={"Software":"Original AN-02 figure source166"})
    fig.savefig(OUT/(stem+'.svg'),bbox_inches='tight',
                metadata={"Date":None,"Creator":"Original AN-02 figure source166"})
    plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(12,5.2),constrained_layout=True)
t=np.linspace(-1,1,801)
parameters=[(.2,'#235a93'),(.4,'#22816c'),(.8,'#a3632b')]
for eps,color in parameters:
    y=-3*eps*t*t+2*t**3
    axes[0].plot(t,y,color=color,linewidth=2,label=rf"$\varepsilon={eps}$")
    axes[0].scatter([-1,eps],[-2-3*eps,-eps**3],color=color,s=28,zorder=4)
axes[0].scatter([0],[0],color='#222222',s=25,zorder=5)
axes[0].axhline(0,color='#555555',alpha=.35,linewidth=.8)
axes[0].set(xlabel=r"real slice $t$",ylabel=r"$\varepsilon^3q_\varepsilon(t)$",
            title="Exact normalized cubic; both node slopes are zero",ylim=(-4.9,2.2))
axes[0].legend(loc='upper left',fontsize=10)
eps=np.geomspace(.03,.9,600)
norm=3/eps**2+2/eps**3
axes[1].loglog(eps,norm,color='#235a93',linewidth=2,
              label=r"$\|q_\varepsilon\|=3\varepsilon^{-2}+2\varepsilon^{-3}$")
axes[1].loglog(eps,2+3*eps,color='#22816c',linewidth=2,
              label=r"$D^3\|q_\varepsilon\|=2+3\varepsilon$")
axes[1].loglog(eps,2*eps**3+3*eps**4,color='#a3632b',linewidth=2,
              label=r"$\Delta^3\|q_\varepsilon\|=2\varepsilon^3+3\varepsilon^4$")
axes[1].set(xlabel=r"root separation $\varepsilon$",ylabel="exact unit-disk supremum / normalization",
            title=r"$D=\varepsilon,\quad\Delta=\varepsilon^2,\quad|R|=\varepsilon^2$")
axes[1].legend(loc='center left',fontsize=9,framealpha=.95)
for ax in axes:ax.grid(alpha=.2)
fig.suptitle("Full double-node jets and the exact discriminant collision scale",fontsize=15)
save(fig,'hermite-collision-and-root-products')

b=(np.sqrt(5)-1)/2
radius=np.sqrt(b)
sample=9/20
angle=np.pi/6
t0=sample*np.exp(1j*angle)
y0=t0*t0
fig,axes=plt.subplots(1,3,figsize=(14.3,4.9),constrained_layout=True)
for ax,rad,label in [(axes[0],radius,r"$|t|<\sqrt{b}$"),
                      (axes[1],b,r"$|y|<b$")]:
    ax.add_patch(Circle((0,0),rad,facecolor='#5ba399',edgecolor='#235a93',alpha=.20,linewidth=2))
    ax.axhline(0,color='#666666',alpha=.35,linewidth=.8)
    ax.axvline(0,color='#666666',alpha=.35,linewidth=.8)
    ax.set_aspect('equal')
    ax.set_xlim(-rad*1.3,rad*1.3)
    ax.set_ylim(-rad*1.3,rad*1.3)
    ax.text(0,rad*1.10,label,ha='center',fontsize=12)
    ax.grid(alpha=.15)
axes[0].scatter([t0.real,-t0.real],[t0.imag,-t0.imag],
                color=['#723b83','#b16b32'],s=55,zorder=5)
axes[0].plot([0,t0.real],[0,t0.imag],color='#723b83',linestyle='--')
axes[0].plot([0,-t0.real],[0,-t0.imag],color='#b16b32',linestyle='--')
axes[0].annotate(r"$t_0$",xy=(t0.real,t0.imag),xytext=(t0.real+.12,t0.imag+.08))
axes[0].annotate(r"$-t_0$",xy=(-t0.real,-t0.imag),xytext=(-t0.real-.20,-t0.imag-.14))
axes[0].set(xlabel=r"$\operatorname{Re}t$",ylabel=r"$\operatorname{Im}t$",
            title="Parameter-plane projection")
axes[1].scatter([y0.real],[y0.imag],color='#222222',s=55,zorder=5)
axes[1].plot([0,y0.real],[0,y0.imag],color='#555555',linestyle='--')
axes[1].annotate(r"$t_0^2=(-t_0)^2$",xy=(y0.real,y0.imag),
                 xytext=(-.34,-.20),arrowprops=dict(arrowstyle='->'),fontsize=10)
axes[1].set(xlabel=r"$\operatorname{Re}y$",ylabel=r"$\operatorname{Im}y$",
            title=r"Branched projection $y=t^2$")
rad=np.linspace(0,radius,501)
surface=1+4*rad**2
projected=4*rad**2
axes[2].plot(rad,surface,color='#235a93',linewidth=2,
             label=r"$dS/dA_t=1+4|t|^2$")
axes[2].plot(rad,projected,color='#a3632b',linewidth=2,
             label=r"projected $dA_y/dA_t=4|t|^2$")
axes[2].fill_between(rad,projected,surface,color='#235a93',alpha=.12)
axes[2].text(radius*.41,.90,"difference = 1",ha='center',fontsize=10)
axes[2].set(xlabel=r"$|t|$",ylabel="exact real Jacobian / area density",
            title="The full graph metric adds one")
axes[2].legend(loc='upper left',fontsize=9)
axes[2].grid(alpha=.18)
fig.suptitle(r"Graph $(t,t^2)\subset\mathbb{C}^2$: two projections and its exact area",fontsize=15)
save(fig,'branched-projection-and-surface-area')
geometry={
    "schema":"AN02-L151-exact-figure-geometry166/v1",
    "figure_A":{"nodes":[0,"epsilon"],"multiplicities":[2,2],
                "q":"-3*t^2/epsilon^2+2*t^3/epsilon^3",
                "normalized_q":"-3*epsilon*t^2+2*t^3",
                "displayed_epsilon":[.2,.4,.8],"unordered_D":"epsilon","ordered_Delta":"epsilon^2",
                "usual_discriminant":"epsilon^2","exact_supremum":"3/epsilon^2+2/epsilon^3",
                "supremum_attained_at_boundary_t":-1,
                "figure_curves_are_real_slices_of_the_exact_polynomial":True,
                "proof_locators":["H1-H7","H22-H24","L151.1-L151.5"]},
    "figure_B":{"graph":"(t,t^2) in C^2, real dimension 2 in real dimension 4",
                "panels_1_and_2_are_projections_not_the_full_graph":True,
                "unit_ball_b":"(sqrt(5)-1)/2","parameter_radius":"sqrt(b)","projection_radius":"b",
                "sample_t":"(9/20)*exp(i*pi/6)","sample_opposite_t":"-(9/20)*exp(i*pi/6)",
                "projected_sample":"(81/400)*exp(i*pi/3)",
                "surface_density":"1+4*|t|^2","projected_density":"4*|t|^2",
                "surface_minus_projected_density":1,
                "fiber_count_nonzero":2,"critical_projection_point":0,
                "exact_surface_integral":"2*pi*(b^(3/2)/3+4*b^(5/2)/5)",
                "exact_fiber_integral":"8*pi*b^(5/2)/5",
                "proof_locators":["H31-H32","L151.11-L151.13"]},
    "figures_are_original":True,"protected_book_media_used":False,
    "Blender_use":"The complex curve has four real ambient coordinates; exact plane projections and metric densities convey the map without an inexact 3D embedding."}
(OUT/'geometry.json').write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({"rendered":["hermite-collision-and-root-products","branched-projection-and-surface-area"],
                  "exact_geometry":str(OUT/'geometry.json'),"new_workers_messages_backups":0}))
