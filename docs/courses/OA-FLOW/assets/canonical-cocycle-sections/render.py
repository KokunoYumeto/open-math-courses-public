"""Reproduce the three original mathematical figures and exact/numerical checks.

Run: python render.py
Dependencies: Python 3, NumPy, Matplotlib. No source-publication image is used.
CC0-1.0 for original code and figure design, to the extent of rights held.
"""
from pathlib import Path
import json
import math
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "axes.titlesize": 13, "axes.labelsize": 11,
                     "svg.fonttype": "none", "svg.hashsalt": "canonical-cocycle-sections-v1",
                     "figure.facecolor": "white",
                     "savefig.facecolor": "white"})
BLUE, RED, GREEN, PURPLE = "#22669d", "#b64843", "#278471", "#7c58a5"
diagnostics = {"role": "Numerical and exact construction checks, not a proof substitute",
               "source": "Original constructions in WC13, CS27, WCH22–33",
               "versions": {"numpy": np.__version__, "matplotlib": matplotlib.__version__}}


def finish(fig, name):
    for ax in fig.axes:
        if ax.axison:
            ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(ROOT / (name + ".svg"), bbox_inches="tight", metadata={"Date": None})
    fig.savefig(ROOT / (name + ".png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), constrained_layout=True)
a = 2.0
p = np.linspace(-2.0, 2.0, 500)
for coeff, color in [(3, BLUE), (1, GREEN)]:
    threshold = math.log(a / coeff)
    axes[0].plot(p, coeff*np.exp(p), color=color, label=fr"$h_{{{coeff}}}(p)={coeff}e^p$")
    axes[0].axvline(threshold, color=color, linestyle="--", alpha=.7)
    axes[0].text(threshold + .03, 5.5 if coeff == 3 else 7.0,
                 fr"$\log(a/{coeff})={threshold:.3f}$", color=color)
axes[0].axhline(a, color="#555555", linewidth=1, linestyle=":")
axes[0].text(-1.95, a+.2, "$a=2$")
axes[0].set(xlim=(-2,2), ylim=(0,9), xlabel="$p$ (positive Fourier coordinate)",
            ylabel="spectral multiplier", title="Two density entries, two strict cut thresholds")
axes[0].legend(loc="upper left", frameon=False)
x = np.linspace(.3, 6, 500)
axes[1].plot(x, 4/(2*np.pi*x), color=PURPLE, linewidth=2)
axes[1].scatter([a], [4/(2*np.pi*a)], color=PURPLE)
axes[1].annotate(r"$4/(2\pi a)=1/\pi$ at $a=2$", (a, 1/np.pi),
                 xytext=(2.6,.85), arrowprops={"arrowstyle":"->", "color": PURPLE})
axes[1].set(xlabel="cut level $a>0$", ylabel=r"$\tau(1_{(a,\infty)}(h))$",
            title="Exact normalized tail: WC13", ylim=(0,2.2))
fig.suptitle(r"Finite nontracial weight: $k=\mathrm{diag}(3,1)$, $\varphi(1)=4$", fontsize=15)
finish(fig, "weight-coordinates")
diagnostics["weight_coordinates"] = {"a":a,"thresholds":[math.log(a/3),math.log(a)],
                                     "tail":4/(2*math.pi*a), "exact_tail":"4/(2*pi*a)"}


fig, axes = plt.subplots(1,2,figsize=(12,5), constrained_layout=True)
omega = .7
z,q = np.meshgrid(np.linspace(-2,2,241), np.linspace(-2,2,241))
phase = omega*(2*z*q-q*q)
im = axes[0].pcolormesh(z,q,phase,cmap="coolwarm",shading="auto",vmin=-8.4,vmax=8.4)
axes[0].annotate("", xy=(.95,.5), xytext=(.15,-.3),
                 arrowprops={"arrowstyle":"->", "color":"#202020", "lw":2})
axes[0].text(-1.85,1.55,r"$(z,q)\mapsto(z+s,q+s)$", fontsize=11,
             bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
axes[0].set(xlabel="center coordinate $z$", ylabel="independent coordinate $q$",
            title=r"True joint coordinate: phase $0.7(2zq-q^2)$", aspect="equal")
fig.colorbar(im, ax=axes[0], label="unwrapped phase (radians)", shrink=.8)
grid=np.linspace(-2,2,401)
for width,color in [(1.0,"#d5e5f1"),(.4,"#9abed8"),(.1,BLUE)]:
    axes[1].fill_between(grid, np.maximum(-2,grid-width),np.minimum(2,grid+width),
                          color=color,label=fr"$|q-p|<{width:g}$")
axes[1].plot(grid,grid,color=RED,linewidth=1.5,label="diagonal (product measure zero)")
axes[1].set(xlim=(-2,2),ylim=(-2,2),xlabel="$q$",ylabel="$p$",aspect="equal",
            title="False diagonal evaluation: CS26")
axes[1].legend(loc="upper left", fontsize=8.6, framealpha=.95)
axes[1].text(-1.8,-1.65,"Each strip restricts to 1;\nthe strips decrease to 0 a.e.",
             fontsize=10, bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"})
fig.suptitle("Canonical section: independence makes normal evaluation possible",fontsize=15)
finish(fig,"canonical-section")
s=.31
boundary_phase=phase-omega*(2*(z+s)*(q+s)-(q+s)**2)
expected=-omega*(2*z*s+s*s)
diagnostics["canonical_section"]={"omega":omega,"s":s,
  "phase_boundary_max_error":float(np.max(np.abs(boundary_phase-expected))),
  "proved_identity":"phase(z,q)-phase(z+s,q+s)=-omega*(2*z*s+s^2)"}


def fat_cantor(stage):
    """Exact dyadic rational endpoints; returns survivors and removed gaps."""
    intervals=[(0.,1.)]
    gaps=[]
    for m in range(1,stage+1):
        new=[]
        for left,right in intervals:
            mid=(left+right)/2
            half=4.**(-m)/2
            lo,hi=mid-half,mid+half
            assert left<lo<hi<right
            new.extend([(left,lo),(hi,right)])
            gaps.append((lo,hi))
        intervals=new
    return intervals,gaps


def maps(n):
    """Choose actual removed gaps; each persists in the infinite complement."""
    stage=1
    while True:
        _,gaps=fat_cantor(stage)
        selected=[]
        for j in range(n):
            candidates=[(max(lo,j/n),min(hi,(j+1)/n)) for lo,hi in gaps]
            candidates=[(lo,hi) for lo,hi in candidates if hi>lo]
            if not candidates:
                break
            lo,hi=max(candidates,key=lambda ab:ab[1]-ab[0])
            # A closed middle half lies strictly inside both the cell and gap.
            selected.append((lo+(hi-lo)/4,hi-(hi-lo)/4))
        if len(selected)==n:
            break
        stage+=1
        assert stage<=12
    xx=[]; yy=[]
    d=1/(2*n*n)
    for j,(lo,hi) in enumerate(selected):
        cellx=[j/n,j/n+d,(j+1)/n-d,(j+1)/n]
        celly=[j/n,lo,hi,(j+1)/n]
        xx.extend(cellx if j==0 else cellx[1:])
        yy.extend(celly if j==0 else celly[1:])
    xx=np.array(xx); yy=np.array(yy)
    assert np.all(np.diff(xx)>0) and np.all(np.diff(yy)>0)
    assert np.max(np.abs(xx-yy))<=1/n+1e-15
    return xx,yy,stage


fig = plt.figure(figsize=(12,8), constrained_layout=True)
gs = fig.add_gridspec(3,2,height_ratios=[.65,2,.68])
ax=fig.add_subplot(gs[0,:]); ax.axis("off")
ax.text(.02,.83,"Balanced matrix construction (WCH10–11)",fontsize=15,weight="bold")
ax.text(.02,.38,r"$a_\Phi=\mathrm{diag}(a_\varphi,a_\psi),\quad"
                   r"\beta_c^\Phi(E_{12})=w(c)E_{12},\quad"
                   r"w(c)=a_\varphi(c)a_\psi(c)^*\in M$", fontsize=15)
ax.text(.02,.02,r"$w(c_1c_2)=w(c_1)\,\beta_{c_1}^{\psi}(w(c_2))$"
                 "     — exact phase, ordered factors",fontsize=13,color=BLUE)
left=fig.add_subplot(gs[1,0]); right=fig.add_subplot(gs[1,1])
n=8; xx,yy,stage=maps(n)
left.plot([0,1],[0,1],color="#888888",linestyle="--",label="identity")
left.plot(xx,yy,color=BLUE,lw=1.8,label="$T_8$ (exact affine pieces)")
for j in range(n+1):
    left.axvline(j/n,color="#dddddd",lw=.5)
left.set(xlim=(0,1),ylim=(0,1),xlabel="$r$",ylabel="$T_8(r)$",aspect="equal",
         title="A large part of each cell enters one gap")
left.legend(loc="upper left",fontsize=8.5,framealpha=.95)
ns=np.arange(3,41)
right.plot(ns,4*(.5-1/ns),color=RED,lw=2,label=r"lower bound for $\|(b_n-b)\xi\|^2$")
right.plot(ns,1/ns,color=BLUE,lw=2,label=r"upper bound for $\|T_n-\mathrm{id}\|_\infty$")
right.plot(ns,1/(4*ns),color=GREEN,lw=2,label=r"upper bound for resolvent norm at $-1$")
right.axhline(2,color=RED,linestyle=":",alpha=.5)
right.set(xlabel="$n$",ylabel="proved bound",ylim=(0,2.12),
          title="The section stays apart as densities converge")
right.legend(loc="center right",fontsize=9,frameon=False)
strip=fig.add_subplot(gs[2,:])
survivors,_=fat_cantor(6)
for lo,hi in survivors:
    strip.add_patch(Rectangle((lo,.15),hi-lo,.7,facecolor=PURPLE,edgecolor="none"))
strip.set(xlim=(0,1),ylim=(0,1),yticks=[],xlabel="$r$",
          title="Stage 6 outer approximation to E; the infinite set has measure exactly 1/2")
strip.spines[["left","top","right"]].set_visible(False)
fig.suptitle("Dominant weights: scalar spectral limits do not control the joint section",fontsize=15)
finish(fig,"weight-change")
mapdata=[]
for n in [3,4,8,16,32]:
    xx,yy,stage=maps(n)
    mapdata.append({"n":n,"gap_selection_stage":stage,
                    "maximum_displacement_at_vertices":float(np.max(np.abs(xx-yy))),
                    "displacement_bound":1/n,"exceptional_domain_length":1/n,
                    "squared_section_distance_lower_bound":4*(.5-1/n),
                    "resolvent_norm_upper_bound":1/(4*n),
                    "source_vertices":[float(v) for v in xx],
                    "target_vertices":[float(v) for v in yy]})
diagnostics["weight_change"]={"map_constructions":mapdata,
 "fat_cantor_removed_length_exact":"sum_{m>=1} 2^(m-1)*4^(-m)=1/2",
 "stage6_outer_measure":sum(hi-lo for lo,hi in survivors),
 "infinite_set_measure":.5,
 "proof_warning":"The rendered finite Cantor stage is not used to estimate infinite-set membership."}
diagnostics["artifacts"]={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(ROOT.glob("*.svg"))}
(ROOT/"diagnostics.json").write_text(json.dumps(diagnostics,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rendered":[p.name for p in sorted(ROOT.glob("*.png"))],
                  "boundary_phase_error":diagnostics["canonical_section"]["phase_boundary_max_error"],
                  "map_count":len(mapdata)},indent=2))
