"""Reproducible exact curvature, stabilized-maxima and support-gap illustrations."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
OUT=HERE/"figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family":"DejaVu Sans","font.size":11,"axes.labelsize":11,
    "axes.titlesize":12,"legend.fontsize":9,
    "svg.hashsalt":"AN02-L149-original-variable-scale-2026-10",
    "savefig.facecolor":"white",
})


def save(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=180,metadata={"Software":"Original AN-02 L149; GPT-6.1 Sol, Ultra; CC0"})
    fig.savefig(OUT/(name+".svg"),metadata={"Date":None,"Creator":"Original AN-02 L149; GPT-6.1 Sol, Ultra; CC0"})
    plt.close(fig)


fig,axes=plt.subplots(1,2,figsize=(13.8,5.6))
fig.subplots_adjust(left=.065,right=.985,bottom=.255,top=.82,wspace=.30)
fig.suptitle("Exact correction curvature and local stabilization",fontsize=16,y=.97)
q=np.geomspace(.01,1e5,1500)
radial=1/(4*(1+q*q)**.75)+(q*q-2)/(16*(1+q*q))
axes[0].semilogx(q,radial,color="#2563eb",lw=2,label=r"$\lambda_\parallel M^{3/2}$ (exact)")
axes[0].axhline(1/16,color="#64748b",ls="--",lw=1.4,label=r"correction bound $1/16$")
axes[0].axhline(1/18,color="#059669",ls="--",lw=1.4,label=r"retained bound $1/18$")
axes[0].fill_between(q,1/18,1/16,color="#fb7185",alpha=.22)
axes[0].annotate(r"allowable loss $1/144$",xy=(1500,(1/16+1/18)/2),
                 xytext=(2,.08),arrowprops={"arrowstyle":"->","color":"#be123c"},
                 fontsize=10,color="#9f1239")
axes[0].set(xlabel=r"$r/t$, where $r=|\eta|$",ylabel="normalized minimum Levi eigenvalue",
            title=r"$k=1$: radial complex eigenline",xlim=(.01,1e5),ylim=(.05,.132))
axes[0].legend(loc="upper right")
axes[0].grid(alpha=.2)
ts=np.array([64.,144.,256.])
radii=np.array([.5,1.,1.5])
offsets=np.array([1.,160.,800.])


def branch(r,j):
    M=np.hypot(ts[j],r)
    return radii[j]*np.abs(r)+M/math.sqrt(ts[j])-np.sqrt(M)-offsets[j]


R=np.linspace(0,1800,1801)
colors=["#64748b","#ea580c","#a855f7"]
for j in range(3):
    axes[1].plot(R,branch(R,j),color=colors[j],lw=1.2,
                 label=rf"$\psi_{j+1}-G_{j+1}$")
maximum=np.maximum.reduce([branch(R,j) for j in range(3)])
axes[1].plot(R,maximum,color="#059669",lw=2.3,label=r"$\phi_3=\max_{j\leq3}(\psi_j-G_j)$")
switches=[brentq(lambda r:branch(r,1)-branch(r,0),1,1000),
          brentq(lambda r:branch(r,2)-branch(r,1),800,2000)]
for i,r in enumerate(switches):
    y=branch(r,i)
    axes[1].scatter([r],[y],color="#059669",s=25,zorder=5)
    axes[1].annotate(f"branch {i+1} → {i+2}",xy=(r,y),
                     xytext=(r+80,y+230),arrowprops={"arrowstyle":"->","color":"#059669"},
                     fontsize=9,color="#047857")
axes[1].set(xlabel=r"$|\eta|$",ylabel="finite-stage weight value",
            title="Three nested-support seeds",xlim=(0,1800),ylim=(-850,2200))
axes[1].grid(alpha=.2)
axes[1].legend(loc="upper left",fontsize=8.8)
inset=axes[1].inset_axes([.54,.15,.42,.26])
small=np.linspace(0,5,251)
inset.plot(small,branch(small,0),color="#64748b",lw=2)
inset.plot(small,np.maximum.reduce([branch(small,j) for j in range(3)]),
           color="#059669",ls="--",lw=1.4)
inset.set(xlim=(0,5),ylim=(-1.2,1.8),title=r"$\phi_3=\phi_1$ on $|\eta|\leq5$")
inset.tick_params(labelsize=8)
inset.title.set_fontsize(9)
inset.set_xlabel(r"$|\eta|$",fontsize=8)
inset.grid(alpha=.15)
fig.text(.065,.13,"Finite seed parameters: interval radii (1/2, 1, 3/2); "
         "t = (64, 144, 256); G = (1, 160, 800).",fontsize=10.5)
fig.text(.065,.073,"Proof: VS12–VS20 and PW15–PW19; learner examples 2–3. "
         "The right panel is a finite construction stage.",fontsize=10)
fig.text(.065,.032,"The general smoothed log-weight consumes at most the shaded curvature margin; "
         "the left curve depicts the exact correction alone.",fontsize=9.5)
save(fig,"curvature-and-stabilized-maxima")

fig,axes=plt.subplots(1,2,figsize=(13,5.3))
fig.subplots_adjust(left=.075,right=.985,bottom=.25,top=.82,wspace=.30)
fig.suptitle("An exterior support creates a small coefficient in a growing strip norm",fontsize=14,y=.96)
axes[0].plot([-1,1],[.6,.6],color="#2563eb",lw=8,solid_capstyle="butt",label=r"$K=[-1,1]$")
axes[0].plot([2,3],[1.15,1.15],color="#be123c",lw=8,solid_capstyle="butt",label=r"$C=[2,3]$")
axes[0].plot([2.25,2.75],[1.15,1.15],color="#059669",lw=8,solid_capstyle="butt",
             label=r"$\operatorname{supp}u=[9/4,11/4]$")
axes[0].annotate("",xy=(2,1.65),xytext=(1,1.65),
                 arrowprops={"arrowstyle":"<->","color":"#475569"})
axes[0].text(1.5,1.78,r"gap $1$; direction $\theta=+1$",ha="center",fontsize=10)
axes[0].vlines([1,2],.35,1.7,color="#94a3b8",ls=":",lw=1)
axes[0].text(-1.2,.02,r"$H_C(-\eta)+H_K(\eta)=-\eta$ for $\eta\geq0$",fontsize=11)
axes[0].set(xlabel=r"physical coordinate $x$",title="Strictly separated convex supports",
            xlim=(-1.4,3.5),ylim=(-.18,2.2),yticks=[])
axes[0].legend(loc="upper left",bbox_to_anchor=(0,1.02),fontsize=9)
axes[0].grid(axis="x",alpha=.15)
eta=np.linspace(0,6,801)
energy=np.ones_like(eta)
product=np.ones_like(eta)
energy[1:]=np.exp(2.5*eta[1:])*np.expm1(eta[1:])/eta[1:]
product[1:]=np.exp(.5*eta[1:])*np.expm1(eta[1:])/eta[1:]
factor=np.exp(-2*eta)
axes[1].semilogy(eta,energy,color="#ea580c",lw=2,label=r"$E_\eta/\pi$ (exact exterior box)")
axes[1].semilogy(eta,product,color="#2563eb",lw=1.8,label=r"$e^{-2\eta}E_\eta/\pi$")
axes[1].semilogy(eta,factor,color="#059669",lw=1.8,label=r"small coefficient $e^{-2\eta}$")
axes[1].set(xlabel=r"positive imaginary shift $\eta$",ylabel="comparison energy and coefficient",
            title="The coefficient multiplies a plane integral",xlim=(0,6))
axes[1].legend(loc="upper left")
axes[1].grid(alpha=.2)
fig.text(.075,.125,r"$E_\eta=e^{-2H_K(\eta)}\int_{\mathbb{R}}|F_u(\xi+i\eta)|^2\,d\xi$; "
         r"$u=1_{[9/4,11/4]}$, $k=1$, $E_0=\pi$.",fontsize=11)
fig.text(.075,.072,"Proof: PW24–PW28; learner example 4. "
         "The seminorm induction enlarges the imaginary integration domain.",fontsize=10)
fig.text(.075,.032,"The whole transform may grow on these planes; strict separation "
         "makes the norm's coefficient arbitrarily small.",fontsize=9.8)
save(fig,"exterior-supports-and-imaginary-shifts")

geometry={
    "schema":"AN02-L149-original-figure-geometry/v1",
    "curvature":{"model":"k=1; correction p_t only",
                 "q_min":float(q[0]),"q_max":float(q[-1]),
                 "normalized_minimum":"1/(4*(1+q^2)^(3/4))+(q^2-2)/(16*(1+q^2))",
                 "correction_bound":"1/16","general_log_error_budget":"1/144","retained_bound":"1/18",
                 "proof":"VS12–VS20; learner example 2"},
    "finite_maximum":{"interval_radii":radii.tolist(),"t":ts.tolist(),"G":offsets.tolist(),
                      "analytic_stabilized_strip_radius":5,"shown_stage_count":3,
                      "switches_are_numeric_roots_of_exact_functions":switches,
                      "full_exhaustion_is_not_numerically_sampled":True,
                      "proof":"PW15–PW19; learner example 3"},
    "exterior":{"K":[-1,1],"C":[2,3],"u_support":[2.25,2.75],"separating_direction":1,"gap":1,
                "positive_shift_support_sum":"-eta","negative_shift_support_sum":"-4*eta",
                "small_coefficient":"exp(-2*eta)",
                "comparison_energy_over_pi":"(exp(3.5*eta)-exp(2.5*eta))/eta; value 1 at eta=0",
                "multiplied_energy_over_pi":"(exp(1.5*eta)-exp(.5*eta))/eta; value 1 at eta=0",
                "proof":"PW24–PW28; learner example 4"},
    "original_artwork":True,"numerical_samples_do_not_prove_general_statements":True,
    "protected_book_media_included":False,"Blender_needed":False,
    "Blender_reason":"Exact scalar curves and real support intervals are best shown by reproducible scientific plots.",
}
(OUT/"geometry.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure_pairs":2,"geometry":"figures/geometry.json"}))
