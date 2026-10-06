"""Reproduce the exact classical constant-strength example and its two figures.

Mathematical proof: ../src/local-elliptic-coefficients.md Section14, CS1--CS53 and CE1--CE34.
Run this file to reproduce its two PNG/SVG pairs and their validation record. The lesson source is read without changes. New Section14 material and this figure source: CC0-1.0.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import os

ROOT = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "mpl-config"))

import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.collections import LineCollection
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 12.2,
    "axes.labelsize": 11,
    "figure.titlesize": 16,
    "svg.fonttype": "none",
    "svg.hashsalt": "an03-constant-strength-example-ce",
    "savefig.facecolor": "white",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# The original full polynomial and all original derivative contributions.
xi1, xi2, z = sp.symbols("xi1 xi2 z", real=True)
p = xi1**2 + sp.I*xi2
indices = [(a,b) for a in range(3) for b in range(3) if a+b <= 2]
strength_sq = sp.simplify(sum(sp.diff(p,xi1,a,xi2,b)*sp.conjugate(sp.diff(p,xi1,a,xi2,b)) for a,b in indices))
assert sp.expand(strength_sq - (xi1**4+xi2**2+4*xi1**2+1+4)) == 0

grid = [(sp.Rational(j1,2),sp.Rational(j2,2)) for j1 in range(3) for j2 in range(3)]
grid_values = [sp.simplify(p.subs({xi1:1+w1,xi2:w2}) * sp.conjugate(p.subs({xi1:1+w1,xi2:w2}))) for w1,w2 in grid]
expected = [sp.Rational(v) for v in [1,sp.Rational(5,4),2,sp.Rational(81,16),sp.Rational(85,16),sp.Rational(97,16),16,sp.Rational(65,4),17]]
assert grid_values == expected
best_value = max(grid_values)
theta_star = grid[grid_values.index(best_value)]
assert theta_star == (1,1) and best_value == 17

V = sp.Matrix([[1,0,0],[1,sp.Rational(1,2),sp.Rational(1,4)],[1,1,1]])
Vinv = sp.Matrix([[1,0,0],[-3,4,-1],[2,-4,2]])
assert V*Vinv == sp.eye(3)
C = Vinv.T*Vinv
assert C == sp.Matrix([[14,-20,7],[-20,32,-12],[7,-12,5]])
lam = sp.symbols("lambda", real=True)
f_lam = lam**3-51*lam**2+85*lam-16
charpoly = C.charpoly()
assert sp.expand(charpoly.as_expr().subs(charpoly.gen,lam)-f_lam) == 0
assert f_lam.subs(lam,49) == -653 and f_lam.subs(lam,50) == 1734
interval_lo = sp.Rational(4928181370,100000000)
interval_hi = sp.Rational(4928181372,100000000)
assert f_lam.subs(lam,interval_lo) < 0 < f_lam.subs(lam,interval_hi)
lambda_star = float(np.max(np.linalg.eigvalsh(np.array(C).astype(float))))
kappa = 1.0/(41472*lambda_star)
J = np.sqrt(33.0)

u_exact = sp.sqrt((sp.sqrt(17)-1)/2)
v_exact = sp.sqrt((sp.sqrt(17)+1)/2)
s_exact = (1+sp.sqrt(17))/2
u, v, ss = [float(e.evalf()) for e in (u_exact,v_exact,s_exact)]
root_in_exact = (u_exact-2+sp.I*(v_exact-1))/2
root_out_exact = -(u_exact+2+sp.I*(v_exact+1))/2
r_original = z**2+(2+sp.I)*z+1
root_in = complex(sp.N(root_in_exact,17))
root_out = complex(sp.N(root_out_exact,17))
assert sp.simplify(root_in_exact+root_out_exact+2+sp.I) == 0
assert sp.simplify(root_in_exact*root_out_exact-1) == 0
assert abs(root_in**2+(2+1j)*root_in+1) < 1e-14
assert abs(root_out**2+(2+1j)*root_out+1) < 1e-14
r_in, r_out = (ss-np.sqrt(ss))/2, (ss+np.sqrt(ss))/2
assert np.isclose(abs(root_in),r_in) and np.isclose(abs(root_out),r_out)
assert 0 < r_in < 0.75 < 1 < 2 < r_out

# The ordered selector tests radius 1 first; CE13 proves its exact minimum is 1.
radii = [sp.Rational(1),sp.Rational(3,2),sp.Rational(2)]
threshold = kappa*np.sqrt(10.0)
assert np.sqrt(10.0)/(41472*32) < 1
assert threshold < 1
rho_star = radii[0]
assert rho_star == 1

R = sp.Rational(1,4)
a_exact = sp.sqrt((sp.sqrt(2)-1)/2)
a = float(a_exact.evalf())
K = 41472*lambda_star*np.sqrt(33)*np.exp(2)
epsilon = 2/(K*a)
assert np.isclose((epsilon/4)*K*a,0.5)

BLUE = "#245b8f"
RED = "#b3423e"
GREEN = "#217567"
INK = "#23313e"
LIGHT = "#edf3f7"

def sampled_curve(ax, w, color="twilight_shifted", linewidth=2.2):
    pts = np.column_stack([w.real,w.imag])
    segs = np.stack([pts[:-1],pts[1:]],axis=1)
    lc = LineCollection(segs,cmap=color,norm=Normalize(0,2*np.pi),linewidth=linewidth,zorder=3)
    lc.set_array(t[:-1])
    ax.add_collection(lc)

def orientation_arrow(ax, curve, at):
    idx = int(at/(2*np.pi)*(len(curve)-1))
    lo, hi = max(0,idx-20), min(len(curve)-1,idx+20)
    ax.annotate("",xy=(curve[hi].real,curve[hi].imag),xytext=(curve[lo].real,curve[lo].imag),
                arrowprops={"arrowstyle":"-|>","color":INK,"lw":1.8,"mutation_scale":13},zorder=6)

fig, axs = plt.subplots(2,2,figsize=(12,10),dpi=150)
fig.subplots_adjust(left=.075,right=.985,bottom=.155,top=.9,wspace=.28,hspace=.4)
fig.suptitle(r"The full polynomial $p(\xi_1,\xi_2)=\xi_1^2+i\xi_2$: strength and the selected circle",y=.975)
fig.text(.5,.935,r"Original frequency sample $\xi_*=(1,0)$; actual choices $\theta_*=(1,1)$ and $\rho_*=1$",ha="center",fontsize=12)

ax = axs[0,0]
g = np.linspace(-2,2,401)
G1,G2 = np.meshgrid(g,g)
strength = np.sqrt(G1**4+G2**2+4*G1**2+1+4)
image = ax.pcolormesh(G1,G2,strength,cmap="Blues",shading="auto",vmin=np.sqrt(5),vmax=np.sqrt(41),rasterized=True)
levels = [np.sqrt(10),4,5]
cs = ax.contour(G1,G2,strength,levels=levels,colors="white",linewidths=.65)
ax.clabel(cs,fmt={np.sqrt(10):r"$\sqrt{10}$",4:"4",5:"5"},fontsize=9)
ax.axvline(0,color=INK,ls="--",lw=1)
ax.plot(0,0,"D",ms=5,color="black",zorder=4)
ax.plot(1,0,"*",ms=13,color=RED,zorder=5)
ax.annotate(r"$\xi_*=(1,0)$"+"\n"+r"$|p(\xi_*)|=1$"+"\n"+r"$\widetilde p(\xi_*)=\sqrt{10}$",xy=(1,0),xytext=(.68,-1.23),fontsize=10,
            bbox={"boxstyle":"round,pad=.35","facecolor":"white","edgecolor":"#b8c8d4","alpha":.97},
            arrowprops={"arrowstyle":"-","color":RED},zorder=6)
ax.text(-.13,1.92,r"$p_2=0$",rotation=90,va="top",ha="right",fontsize=9)
ax.set(xlim=(-2,2),ylim=(-2,2),xlabel=r"Original $\xi_1$",ylabel=r"Original $\xi_2$")
ax.set_aspect("equal")
ax.set_title("(a) Every contribution to full strength",pad=9)
ax.text(.5,-.2,r"$\widetilde p^2=\xi_1^4+\xi_2^2+4\xi_1^2+1+4$",transform=ax.transAxes,ha="center",fontsize=11)
cbar = fig.colorbar(image,ax=ax,pad=.025,shrink=.87)
cbar.set_ticks([np.sqrt(5),np.sqrt(10),5,np.sqrt(41)],labels=[r"$\sqrt{5}$",r"$\sqrt{10}$","5",r"$\sqrt{41}$"])
cbar.set_label(r"$\widetilde p(\xi)$",rotation=0,labelpad=12)

ax = axs[0,1]
ax.set_title(r"(b) Actual grid $W=\{0,\frac{1}{2},1\}^2$",pad=9)
for (w1,w2),value in zip(grid,grid_values):
    xx,yy = float(w1),float(w2)
    selected = (w1,w2) == theta_star
    ax.scatter(xx,yy,s=190 if selected else 85,marker="*" if selected else "o",
               color=RED if selected else BLUE,zorder=3)
    label = str(value) if value.q == 1 else rf"$\frac{{{value.p}}}{{{value.q}}}$"
    offset = (-.12,.085) if selected else (.08,.035)
    ax.text(xx+offset[0],yy+offset[1],label,fontsize=11,color=RED if selected else INK,
            ha="right" if selected else "left",va="bottom")
ax.annotate(r"Unique first maximizer"+"\n"+r"$\theta_*=(1,1)$",xy=(1,1),xytext=(.05,1.27),
            arrowprops={"arrowstyle":"->","color":RED,"lw":1.1},color=RED,fontsize=10.5)
ax.set(xlim=(-.15,1.3),ylim=(-.12,1.48),xlabel=r"Real shift $w_1$",ylabel=r"Real shift $w_2$")
ax.set_xticks([0,.5,1],["0",r"$1/2$","1"])
ax.set_yticks([0,.5,1],["0",r"$1/2$","1"])
ax.grid(color="#dae2e8",lw=.6)
ax.set_aspect("equal")
ax.text(.5,-.2,r"Point labels: $|p(\xi_*+w)|^2=(1+w_1)^4+w_2^2$",transform=ax.transAxes,ha="center",fontsize=10.5)

t = np.linspace(0,2*np.pi,1601)
zcurve = np.exp(1j*t)
pcircle = (1+zcurve)**2+1j*zcurve
assert np.max(abs(pcircle-zcurve*(2+2*np.cos(t)+1j))) < 5e-15

ax = axs[1,0]
ax.set_title("(c) The selected circle avoids both original roots",pad=10)
sampled_curve(ax,zcurve)
orientation_arrow(ax,zcurve,np.pi/3)
ax.axhline(0,color="#d8dee4",lw=.8); ax.axvline(0,color="#d8dee4",lw=.8)
ax.scatter([0],[0],s=28,color=INK,zorder=4)
for root,label,color in [(root_in,r"$\lambda_+$",RED),(root_out,r"$\lambda_-$",BLUE)]:
    unit = root/abs(root)
    ax.plot([root.real,unit.real],[root.imag,unit.imag],color=color,lw=2,zorder=4)
    ax.scatter(root.real,root.imag,s=48,color=color,zorder=5)
    ax.scatter(unit.real,unit.imag,s=22,facecolor="white",edgecolor=color,zorder=5)
    if root == root_in:
        ax.annotate(label,xy=(root.real,root.imag),xytext=(.05,.38),color=color,fontsize=12,
                    arrowprops={"arrowstyle":"-","color":color})
        mid=(root+unit)/2
        ax.annotate(r"$d_{\rm in}$",xy=(mid.real,mid.imag),xytext=(-1.3,.83),color=color,fontsize=10,
                    arrowprops={"arrowstyle":"-","color":color,"lw":.8})
    else:
        ax.text(root.real-.13,root.imag-.16,label,color=color,fontsize=12,ha="right")
        mid=(root+unit)/2
        ax.text(mid.real-.07,mid.imag+.11,r"$d_{\rm out}$",color=color,fontsize=10,ha="right")
ax.text(.88,1.13,r"$z=e^{it}$",fontsize=11,color=INK)
ax.text(1.2,.22,r"$\rho_*=1$",fontsize=11,color=INK)
ax.set(xlim=(-2.15,1.6),ylim=(-1.8,1.65),xlabel=r"$\operatorname{Re}z$",ylabel=r"$\operatorname{Im}z$")
ax.set_aspect("equal")
ax.text(.5,-.2,r"$r(z)=z^2+(2+i)z+1=(z-\lambda_+)(z-\lambda_-)$",transform=ax.transAxes,ha="center",fontsize=10.5)

ax = axs[1,1]
ax.set_title(r"(d) Actual image $p(1+e^{it},e^{it})$",pad=10)
sampled_curve(ax,pcircle)
orientation_arrow(ax,pcircle,np.pi/3)
ax.plot(zcurve.real,zcurve.imag,color=GREEN,ls="--",lw=1.15,zorder=2)
ax.axhline(0,color="#d8dee4",lw=.8); ax.axvline(0,color="#d8dee4",lw=.8)
ax.scatter(0,0,s=35,marker="x",color=INK,zorder=6)
marked = [(0,4+1j,r"$4+i$",(.35,.25)),(np.pi/2,-1+2j,r"$-1+2i$",(-.08,.25)),
          (np.pi,-1j,r"$-i$",(-.65,-.27)),(3*np.pi/2,1-2j,r"$1-2i$",(.15,-.28))]
for tt,val,label,offset in marked:
    ax.scatter(val.real,val.imag,s=30,color=INK,zorder=5)
    ax.text(val.real+offset[0],val.imag+offset[1],label,fontsize=10.5,
            ha="right" if val.real<0 else "left")
ax.plot([0,0],[0,-1],color=GREEN,lw=1.5,zorder=4)
ax.text(.18,-.58,r"$\min|r|=1$",color=GREEN,fontsize=10.5)
ax.set(xlim=(-1.8,4.9),ylim=(-3,4.15),xlabel=r"$\operatorname{Re}p$",ylabel=r"$\operatorname{Im}p$")
ax.set_aspect("equal")
ax.text(.5,-.2,r"$|r(e^{it})|^2=(2+2\cos t)^2+1\geq1$",transform=ax.transAxes,ha="center",fontsize=10.5)

fig.text(.5,.058,r"Sample minimum $|r|=1$; global $\kappa=1/(41472\lambda_*)$ controls the complete family of circles.",
         ha="center",fontsize=9.5,color=INK)
fig.text(.5,.027,"Exact values and proofs: CE1–CE24. Colored curves follow increasing t; numerical drawing of exact formulas.",
         ha="center",fontsize=9,color=INK)
fig.savefig(ROOT/"constant_strength_circle_example.png",dpi=150)
fig.savefig(ROOT/"constant_strength_circle_example.svg",metadata={"Date":None,"Creator":"Matplotlib"})
plt.close(fig)

# A separate figure keeps the functional-analytic domains and constants legible.
fig = plt.figure(figsize=(12,7),dpi=150)
gs=fig.add_gridspec(1,2,width_ratios=[.85,1.5],left=.045,right=.985,bottom=.12,top=.84,wspace=.09)
ax0=fig.add_subplot(gs[0,0]); ax1=fig.add_subplot(gs[0,1])
for ax in (ax0,ax1): ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
fig.suptitle(r"The proved local maps for $P(x,D)=D_1^2+iD_2+\varepsilon x_1D_1$",y=.96)
fig.text(.5,.9,"Continuous coefficients act on the already controlled L² derivatives of the solution.",ha="center",fontsize=12)

lines=[
    (r"Spatial point $x_0=(0,0)$",.95),
    (r"$U=(-\frac{1}{4},\frac{1}{4})^2$, $R=\frac{1}{4}$",.875),
    (r"$p(D)=D_1^2+iD_2$, $q_0(D)=D_1$",.785),
    (r"$a=\|q_0\|_p=\sqrt{(\sqrt{2}-1)/2}$",.695),
    (r"$K=41472\lambda_*\sqrt{33}\,e^2$",.605),
    (r"$\varepsilon=2/(Ka)$, $c(x)=\varepsilon x_1$",.515),
    (r"$B=M_cD_1S_U$, $T=I+B$",.425),
    (r"$\|B\|\leq\frac{1}{2}$, $\|T^{-1}\|\leq2$",.335),
]
for label,yy in lines: ax0.text(.01,yy,label,fontsize=11.3,color=INK,va="center")
ax0.text(.01,.20,r"$\lambda_*$ is the largest eigenvalue of",fontsize=10.2,color=INK)
ax0.text(.01,.105,"[ 14  -20    7 ]\n[-20   32  -12 ]\n[  7  -12    5 ]",fontsize=10.2,color=INK,fontfamily="DejaVu Sans Mono",va="center")

def box(ax,center,text,width=.25,height=.145,face=LIGHT):
    x,y=center
    patch=FancyBboxPatch((x-width/2,y-height/2),width,height,boxstyle="round,pad=.015,rounding_size=.025",
                        linewidth=1,edgecolor="#7b96aa",facecolor=face)
    ax.add_patch(patch)
    ax.text(x,y,text,fontsize=11.5,ha="center",va="center",color=INK)
    return (x-width/2,x+width/2,y-height/2,y+height/2)

def arrow(ax,start,end,label,offset=(0,.036)):
    ax.annotate("",xy=end,xytext=start,arrowprops={"arrowstyle":"->","lw":1.55,"color":BLUE,"mutation_scale":13})
    mx=(start[0]+end[0])/2+offset[0]; my=(start[1]+end[1])/2+offset[1]
    ax.text(mx,my,label,fontsize=11.4,color=BLUE,ha="center",va="bottom")

box(ax1,(.13,.79),r"$f\in L^2(U)$",width=.21)
box(ax1,(.45,.79),r"$g\in L^2(U)$",width=.23)
box(ax1,(.83,.79),r"$Ef=S_Ug$"+"\n"+r"$\in\mathcal{H}_p(U)$",width=.28)
arrow(ax1,(.25,.79),(.325,.79),r"$T^{-1}$")
arrow(ax1,(.58,.79),(.68,.79),r"$S_U$")
ax1.text(.49,.965,r"$E=S_UT^{-1}$",ha="center",fontsize=13,color=INK)

box(ax1,(.44,.49),r"$q(D)Ef$"+"\n"+r"$\in L^2(U)$",width=.25)
box(ax1,(.83,.49),r"$PEf=f$"+"\n"+r"$\in L^2(U)$",width=.28,face="#edf6f0")
arrow(ax1,(.76,.705),(.48,.575),r"$q(D)$",offset=(-.028,-.01))
arrow(ax1,(.83,.705),(.83,.575),r"$P$",offset=(.04,0))
ax1.text(.60,.34,r"$\|q(D)E\|\leq 2K\|q\|_p$ for every $q\in V_p$",fontsize=10.8,ha="center",color=INK)

box(ax1,(.135,.14),r"$u\in C_c^\infty(U)$",width=.23)
box(ax1,(.47,.14),r"$Pu\in L^2(U)$",width=.25)
box(ax1,(.83,.14),r"$EPu=u$",width=.27,face="#edf6f0")
arrow(ax1,(.265,.14),(.335,.14),r"$P$")
arrow(ax1,(.61,.14),(.68,.14),r"$E$")
ax1.text(.50,.02,r"Left identity uses $T p(D)u=Pu$ and $S_Up(D)u=u$.",fontsize=10.3,ha="center",color=INK)
fig.text(.5,.041,"Exact domains, strengths, constants and identities: CE25–CE34; full construction CS38–CS50.",
         ha="center",fontsize=9.3,color=INK)
fig.savefig(ROOT/"constant_strength_solver_maps.png",dpi=150)
fig.savefig(ROOT/"constant_strength_solver_maps.svg",metadata={"Date":None,"Creator":"Matplotlib"})
plt.close(fig)

artifacts=["constant_strength_circle_example.png","constant_strength_circle_example.svg",
           "constant_strength_solver_maps.png","constant_strength_solver_maps.svg"]
receipt={
    "observed_utc":datetime.now(timezone.utc).isoformat(),
    "mathematical_proof":"../src/local-elliptic-coefficients.md Section14 CS1--CS53 and CE1--CE34",
    "original_polynomial":"xi1^2 + i*xi2",
    "full_strength_squared":"xi1^4 + xi2^2 + 4*xi1^2 + 1 + 4",
    "sample_frequency":[1,0],"actual_theta":[1,1],"actual_first_admissible_radius":"1",
    "candidate_radii":["1","3/2","2"],
    "ordered_grid":[[str(w1),str(w2)] for w1,w2 in grid],
    "exact_grid_values_squared":[str(q) for q in grid_values],
    "selected_polynomial":"z^2 + (2+i)*z + 1",
    "exact_sample_minimum":"1","sample_strength":"sqrt(10)",
    "global_kappa_exact":"1/(41472*lambda_star)",
    "global_kappa_numeric":kappa,"sample_global_threshold_numeric":threshold,
    "lambda_star_interval":[str(interval_lo),str(interval_hi)],
    "root_in_exact":str(root_in_exact),"root_out_exact":str(root_out_exact),
    "root_in_render_position":[root_in.real,root_in.imag],"root_out_render_position":[root_out.real,root_out.imag],
    "spatial_U":"(-1/4,1/4)^2","spatial_frozen_point":[0,0],
    "K_exact":"41472*lambda_star*sqrt(33)*exp(2)",
    "a_exact":"sqrt((sqrt(2)-1)/2)","epsilon_exact":"2/(K*a)",
    "perturbation_norm_bound_exact":"1/2",
    "status":"exact_algebra_assertions_passed; native visual inspection recorded separately",
    "native_png_sizes":[[1800,1500],[1800,1050]],
    "rendering_versions":{"matplotlib":matplotlib.__version__,"numpy":np.__version__,"sympy":sp.__version__},
    "artifact_sha256":{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in artifacts},
    "complete_lesson_source_sha256":hashlib.sha256((ROOT.parent/"src"/"local-elliptic-coefficients.md").read_bytes()).hexdigest(),
    "no_shared_source_git_tex_or_sidebar_mutation":True,
}
(ROOT/"illustration-validation.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":receipt["status"],"artifacts":artifacts,"proof_hash":receipt["complete_lesson_source_sha256"]},indent=2))
