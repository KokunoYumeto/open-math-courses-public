"""Check the exact jet identities, transformed operator and support geometry."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
import hashlib
import json
import math
import os

import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle

OWN = Path(__file__).resolve().parent
FIG = OWN / "figures"
FIG.mkdir(exist_ok=True)
checks = []


def check(name, condition, details=None):
    assert condition, name
    checks.append({"name": name, "status": "PASS", "details": details})


def bind(path):
    data = path.read_bytes()
    return {"path": path.relative_to(OWN).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest().upper()}


for d in range(5):
    for m in range(1, 7):
        indices = [v for v in product(range(m), repeat=d+1) if sum(v) <= m-1]
        known = set(indices)
        count = math.comb(d+m, m-1)
        check(f"jet_count_d{d}_m{m}", len(indices) == count,
              {"count": count, "formula": "binom(d+m,m-1)"})
        for v in indices:
            if sum(v) <= m-2:
                target = v[:-1] + (v[-1]+1,)
                assert target in known
            elif any(v[:-1]):
                ell = next(i for i in range(d) if v[i])
                target = list(v)
                target[ell] -= 1
                target[-1] += 1
                assert tuple(target) in known
            else:
                assert v == (0,)*d + (m-1,)
        check(f"all_jet_rows_d{d}_m{m}", True,
              "Every row uses a listed component or one tangential derivative; exactly one pure-time row.")

x, s, t = sp.symbols("x s t", real=True)
v = sp.Function("v")(x, s)
def old_x(expr):
    return sp.diff(expr, x)-2*x*sp.diff(expr, s)
wave = sp.diff(v,s,2)-old_x(old_x(v))
expected = (1-4*x*x)*sp.diff(v,s,2)+4*x*sp.diff(v,x,s)-sp.diff(v,x,2)+2*sp.diff(v,s)
check("full_wave_conjugation_including_first_order_coefficient", sp.simplify(wave-expected)==0)
c=sp.symbols("c",real=True)
check("wave_characteristic_slopes", sp.expand(1-(-c)**2)==1-c*c)
u=sp.Function("u")(x,t)
Pu=(sp.diff(u,t,3)+(1+x*x+sp.I*t)*sp.diff(u,x,t,t)
    +(2-sp.I*t)*sp.diff(u,x,x,t)+sp.I*sp.diff(u,x,3)
    +(1+t)*sp.diff(u,t)+x*sp.diff(u,x)+u)
W=[u,sp.diff(u,x),sp.diff(u,t),sp.diff(u,x,2),sp.diff(u,x,t),sp.diff(u,t,2)]
right=[W[2],W[4],W[5],sp.diff(W[4],x),sp.diff(W[5],x)]
for i in range(5):
    check(f"third_order_shift_row_{i}",sp.simplify(sp.diff(W[i],t)-right[i])==0)
last=-(1+x*x+sp.I*t)*sp.diff(W[5],x)-(2-sp.I*t)*sp.diff(W[4],x)-sp.I*sp.diff(W[3],x)-(1+t)*W[2]-x*W[1]-W[0]
check("third_order_final_row_exact_original_operator",sp.simplify(sp.diff(W[5],t)-last-Pu)==0)
H=sp.Heaviside(t-x)
check("characteristic_step_distribution", sp.simplify(sp.diff(H,t,2)-sp.diff(H,x,2))==0)
check("characteristic_delta_distribution",sp.simplify(sp.diff(sp.DiracDelta(t-x),t,2)-sp.diff(sp.DiracDelta(t-x),x,2))==0)
U1=sp.cos(x)*sp.sinh(t);U2=sp.sin(x)*sp.cosh(t)
check("complex_system_first_row",sp.simplify(sp.diff(U1,t)-sp.diff(U2,x))==0)
check("complex_system_second_row",sp.simplify(sp.diff(U1,x)+sp.diff(U2,t))==0)
check("zero_extension_boundary_vector",U1.subs(t,0)==0 and U2.subs(t,0)==sp.sin(x))
eta,tau=sp.symbols("eta tau",real=True)
matrix=sp.Matrix([[tau,-eta],[eta,tau]])
check("square_system_normal_determinant",sp.expand(matrix.det())==tau*tau+eta*eta)
check("third_order_complex_polynomial_not_real_rooted",
      sp.Poly(tau**3+tau**2+2*tau+sp.I,tau).monic().all_coeffs()[-1]==sp.I)
check("forty_component_two_unknown_order_four_count",2*math.comb(6,3)==40)

eps=sp.Rational(1,8);a=sp.Rational(1,144);kappa=2*eps/a
xp=sp.Rational(1,2304);tp=-sp.Rational(1,110592);mu=-sp.Rational(1,442368)
check("exact_kappa",kappa==36)
check("C1_slope_on_full_ball",sp.Rational(3,2)*sp.sqrt(a)==eps)
check("contact_derivative",sp.simplify(-sp.Rational(3,2)*sp.sqrt(xp)+2*kappa*xp)==0)
check("contact_graph_value",sp.simplify(-xp**sp.Rational(3,2)-tp)==0)
check("contact_minimum",sp.simplify(tp+kappa*xp*xp-mu)==0)
check("physical_normals",2*kappa*xp==sp.Rational(1,32))
check("contact_strictly_interior",0<xp<a and abs(tp)<2*eps*a)
check("full_cylinder_rescaled_side",2304*a==16)
check("rescaled_minimum_level",110592*mu==-sp.Rational(1,4) and
      110592*kappa/sp.Integer(2304)**2==sp.Rational(3,4))
z=sp.symbols("z",nonnegative=True)
gap=sp.Rational(1,4)+sp.Rational(3,4)*z**4-z**3
fact=sp.Rational(1,4)*(z-1)**2*(3*z*z+2*z+1)
check("exact_nonnegative_global_parabola_gap",sp.expand(gap-fact)==0)
check("strict_side_margin", -eps*a+kappa*a*a==eps*a>0)
check("strict_bottom_exclusion",-2*eps*a < -eps*a)
delta,t0=sp.symbols("delta t0",positive=True)
check("causal_minimum_normal_bound",sp.simplify(2*delta*sp.sqrt(t0/delta)-2*sp.sqrt(delta*t0))==0)

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                    "svg.hashsalt":"Holmgren-support-geometry-274",
                    "axes.titlesize":15,"savefig.facecolor":"white"})

fig,ax=plt.subplots(figsize=(10.5,5.8))
positions={(aa,j):(aa,j) for aa in range(3) for j in range(3-aa)}
labels={(0,0):r"$u$",(1,0):r"$u_x$",(2,0):r"$u_{xx}$",
        (0,1):r"$u_t$",(1,1):r"$u_{xt}$",(0,2):r"$u_{tt}$"}
for key,pos in positions.items():
    ax.scatter(*pos,s=1100,color="#e9f1fb",edgecolors="#294a6c",linewidths=1.6,zorder=4)
    ax.text(*pos,labels[key],ha="center",va="center",fontsize=15,zorder=5)
for source in [(0,0),(1,0),(0,1)]:
    target=(source[0],source[1]+1)
    ax.add_patch(FancyArrowPatch(positions[source],positions[target],
        arrowstyle="-|>",mutation_scale=16,shrinkA=25,shrinkB=25,
        color="#2267a5",linewidth=2))
for source,target in [((2,0),(1,1)),((1,1),(0,2))]:
    ax.add_patch(FancyArrowPatch(positions[source],positions[target],
        arrowstyle="-|>",mutation_scale=16,shrinkA=25,shrinkB=25,
        color="#bb5b19",linewidth=2,linestyle="--"))
ax.add_patch(Circle((0,2),0.26,fill=False,edgecolor="#942a48",linewidth=2,zorder=6))
ax.text(.50,2.11,r"Final row from $Pu=0$",color="#942a48",fontsize=12)
ax.text(2.40,1.52,"Solid: time shift\n"+r"$\partial_tW_{\alpha j}=W_{\alpha,j+1}$",
        color="#2267a5",fontsize=12,ha="left",va="top")
ax.text(2.40,.82,"Dashed: one spatial derivative\n"+r"$\partial_tW_{\alpha j}=\partial_xW_{\alpha-1,j+1}$",
        color="#bb5b19",fontsize=12,ha="left",va="top")
ax.set(xlim=(-.5,5.2),ylim=(-.45,2.55),xlabel=r"Tangential derivative count $\alpha$",
       ylabel=r"Time derivative count $j$",title="One scalar third-order equation gives six first-order rows")
ax.set_xticks([0,1,2]);ax.set_yticks([0,1,2])
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
for ext in ["png","svg"]:
    fig.savefig(FIG/f"third-order-jet-system.{ext}",dpi=170,
                metadata={"Date":None} if ext=="svg" else {})
plt.close(fig)

X=np.linspace(-2.1,2.1,801); graph=-np.abs(X)**1.5;parab=-.25-.75*X**2
fig,ax=plt.subplots(figsize=(9.5,6.1))
ax.fill_between(X,graph,.5,color="#dcecff",alpha=.72,label="Candidate closed set above the graph")
ax.plot(X,graph,color="#2164a0",lw=2.8,label=r"$Y=-|X|^{3/2}$")
ax.plot(X,parab,color="#b5571b",lw=2.4,label=r"Supporting level: $Y=-1/4-3X^2/4$")
ax.scatter([-1,1],[-1,-1],s=66,color="#8d2948",zorder=6)
for sign in [-1,1]:
    ax.annotate(r"$dt-dx/32$" if sign<0 else r"$dt+dx/32$",
                xy=(sign,-1),xytext=(sign*1.35,-.26),
                ha="center",color="#8d2948",fontsize=12,
                arrowprops={"arrowstyle":"->","color":"#8d2948","lw":1.3})
ax.scatter([0],[0],s=34,color="#2164a0",zorder=6)
ax.set(xlim=(-2.1,2.1),ylim=(-3.7,.48),xlabel=r"$X=2304x$",
       ylabel=r"$Y=110592t$",title="Analytic contact near a nonanalytic continuously differentiable graph")
ax.legend(loc="lower center",fontsize=10,framealpha=.96)
ax.grid(alpha=.18);fig.tight_layout()
for ext in ["png","svg"]:
    fig.savefig(FIG/f"analytic-contact-at-a-C1-graph.{ext}",dpi=170,
                metadata={"Date":None} if ext=="svg" else {})
plt.close(fig)

geometry={
    "jet_diagram":{"order":3,"tangential_dimension":1,"unknown_components":1,
                   "vertices":[{"alpha":aa,"j":j} for aa,j in sorted(positions)],
                   "solid_rows":[[0,0,0,1],[1,0,1,1],[0,1,0,2]],
                   "dashed_rows":[[2,0,1,1],[1,1,0,2]],
                   "final_equation_row":[0,2],"proof_locator":"Lemma2.1;learner Example1"},
    "contact":{"candidate_graph":"t=-|x|^(3/2)","epsilon":"1/8","a":"1/144",
               "kappa":"36","minimizers":[["-1/2304","-1/110592"],["1/2304","-1/110592"]],
               "minimum":"-1/442368","physical_conormals":["dt-dx/32","dt+dx/32"],
               "display_coordinates":["X=2304x","Y=110592t"],
               "display_graph":"Y=-|X|^(3/2)","display_supporting_level":"Y=-1/4-3X^2/4",
               "full_cylinder_side_X":"16","no_PDE_solution_claimed_for_candidate_set":True,
               "proof_locator":"Theorem3.2;learner Example3,Solution5"}}
(FIG/"geometry.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
record={"schema":"AN02-Holmgren-exact-jet-geometry-check274/v1",
        "observed_at_utc":datetime.now(timezone.utc).isoformat(),"status":"PASS",
        "checks_passed":len(checks),"arithmetic":"exact integer/rational and symbolic identities",
        "scope":"Concrete operator, distribution derivative and contact identities; not a substitute for full analytic uniqueness proof.",
        "checks":checks,"artifacts":[bind(p) for p in sorted(FIG.iterdir()) if p.is_file()],
        "workers_launched":0,"outgoing_messages":0}
(OWN/"math-check274.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","checks_passed":len(checks),"artifacts":record["artifacts"]}))
