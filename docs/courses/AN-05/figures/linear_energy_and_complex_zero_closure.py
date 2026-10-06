"""Original CC0 diagram: sharp linear energy and an exact tangent-zero closure.

Run this saved file with Python, numpy and matplotlib. Outputs stay beside it.
No source prose or source figures are reused. Algebraic checks use exact
Fraction arithmetic; Gaussian numerical checks are distinct from those checks.
"""
from pathlib import Path
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text

parser = argparse.ArgumentParser()
parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent / "linear-energy-and-complex-zero-closure.png")
PNG = parser.parse_args().output
OUT = PNG.parent
CHECKS = PNG.with_suffix(".checks.json")

# Exact polynomial algebra, variables (x1,x2,xi1,xi2).
def add(a,b):
    result = dict(a)
    for monomial, coefficient in b.items():
        result[monomial] = result.get(monomial,F(0)) + coefficient
    return {m:c for m,c in result.items() if c}

def scale(a,c):
    return {m:v*c for m,v in a.items() if v*c}

def multiply(a,b):
    result={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(u+v for u,v in zip(ma,mb))
            result[m]=result.get(m,F(0))+ca*cb
    return {m:c for m,c in result.items() if c}

def derivative(a,j):
    result={}
    for m,c in a.items():
        if m[j]:
            n=list(m)
            n[j]-=1
            result[tuple(n)]=c*m[j]
    return result

def bracket(a,b):
    result={}
    for j in range(2):
        result=add(result,multiply(derivative(a,j+2),derivative(b,j)))
        result=add(result,scale(multiply(derivative(a,j),derivative(b,j+2)),F(-1)))
    return result

def evaluate(a,point):
    return sum((c*math.prod(v**power for v,power in zip(point,m))
                for m,c in a.items()),F(0))

def exact_complex_square_plus_t(re,im,t):
    return (re*re-im*im+t,2*re*im)

def polynomial_receipt(a):
    return [{"powers":list(m),"coefficient":str(c)} for m,c in sorted(a.items())]

p={(0,0,2,0):F(1),(1,0,0,2):F(1)}
phi={(1,0,0,0):F(-1)}
point=(F(0),F(0),F(0),F(1))
hp_phi=bracket(p,phi)
double=bracket(p,hp_phi)   # bar p = p in this real-coefficient model.
assert hp_phi=={(0,0,1,0):F(-2)}
assert double=={(0,0,0,2):F(2)}
assert evaluate(p,point)==0
assert evaluate(derivative(p,0),point)==1
assert evaluate(hp_phi,point)==0
assert evaluate(double,point)==2
assert bracket(p,p)=={}   # Principal normality holds with constant zero.

epsilons=[F(1,2),F(1,4),F(1,8)]
root_checks=[]
for epsilon in epsilons:
    for sign_t in (-1,1):
        t=sign_t*epsilon**2
        roots=[(sign*epsilon,F(0)) if sign_t<0 else
               (F(0),sign*epsilon) for sign in (-1,1)]
        for re,im in roots:
            residual=exact_complex_square_plus_t(re,im,t)
            assert residual==(0,0)
            # xi0+sN=(-s,1), x=(t,0), N=(-1,0).
            # Thus p=t+(-s)^2=F(s,t), including complex roots.
            root_checks.append({"epsilon":str(epsilon),"t":str(t),
                                "s_real":str(re),"s_imaginary":str(im),
                                "x":[str(t),"0"],
                                "real_covector":[str(-re),"1"],
                                "tau":str(im),
                                "exact_residual":[str(v) for v in residual]})

# Closed Gaussian integrals: ||g_a||^2=1 and
# int x^2|g_a|^2 dx=1/(2|a|). Hence the displayed exact energies.
# Numerical quadrature verifies the sampled curves independently.
x_check=np.linspace(-9,9,18001)
gaussian_checks=[]
for a in (-1,1):
    b=abs(a)
    g=(b/math.pi)**0.25*np.exp(-b*x_check*x_check/2)
    norm=float(np.trapezoid(g*g,x_check))
    moment=float(np.trapezoid(x_check*x_check*g*g,x_check))
    exact_energy=F((b+a)**2,2*b)
    exact_adjoint_energy=F((b-a)**2,2*b)
    energy=float(np.trapezoid((b+a)**2*x_check*x_check*g*g,x_check))
    adjoint_energy=float(np.trapezoid((b-a)**2*x_check*x_check*g*g,x_check))
    assert abs(norm-1)<2e-13
    assert abs(moment-1/(2*b))<2e-13
    assert abs(energy-float(exact_energy))<4e-13
    assert abs(adjoint_energy-float(exact_adjoint_energy))<4e-13
    assert exact_energy==max(2*a,0)
    gaussian_checks.append({"a":a,"exact_norm_squared":"1",
                            "exact_second_moment":str(F(1,2*b)),
                            "exact_L_energy":str(exact_energy),
                            "exact_adjoint_energy":str(exact_adjoint_energy),
                            "numerical_norm_squared":norm,
                            "numerical_L_energy":energy,
                            "numerical_adjoint_energy":adjoint_energy,
                            "annihilator":"L" if a<0 else "L_adjoint"})

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "mathtext.fontset":"dejavusans","axes.spines.top":False,
                     "axes.spines.right":False,"axes.linewidth":0.9,
                     "xtick.labelsize":11,"ytick.labelsize":11,
                     "savefig.facecolor":"white"})
fig=plt.figure(figsize=(14.4,9.6),dpi=200,facecolor="white")
fig.text(0.055,0.967,"Sharp energy and the approach to a real characteristic",
         fontsize=22,weight="bold",va="top",color="#152438")

fig.text(0.075,0.902,"A  Sharp linear energy",fontsize=17,weight="bold")
fig.text(0.075,0.861,
         r"$L_a=D+i a x,\quad D=-i\,\partial_x,\qquad"
         r"E(a)=\inf_{\psi\in C_c^\infty,\ \|\psi\|_2=1}\|L_a\psi\|_2^2"
         r"=\max(2a,0)$",fontsize=13)
ax=fig.add_axes([0.075,0.325,0.410,0.470])
neg="#bb551e"
pos="#1761a1"
a_negative=np.linspace(-1.30,0,400)
a_positive=np.linspace(0,1.30,400)
ax.plot(a_negative,np.zeros_like(a_negative),color=neg,lw=3,zorder=3)
ax.plot(a_positive,2*a_positive,color=pos,lw=3,zorder=3)
ax.axvline(0,color="#c3cad2",lw=0.9,zorder=0)
ax.scatter([-1],[0],s=90,color=neg,edgecolor="white",linewidth=1,zorder=6)
ax.scatter([1],[2],s=90,color=pos,edgecolor="white",linewidth=1,zorder=6)
ax.set_xlim(-1.4,1.4)
ax.set_ylim(-0.13,2.82)
ax.set_xticks([-1,0,1])
ax.set_yticks([0,1,2])
ax.set_xlabel(r"coefficient $a$",labelpad=10)
ax.set_ylabel(r"infimum of squared energy $E(a)$",labelpad=10)
ax.grid(axis="y",color="#e9edf1",lw=0.8,zorder=0)
ax.annotate(r"$a=-1$"+"\n"+r"$L_{-1}g=0$"+"\n"+r"$\|L_{-1}g\|_2^2=0$",
            xy=(-1,0),xytext=(-1.30,0.82),fontsize=12,va="top",ha="left",
            color=neg,arrowprops={"arrowstyle":"->","color":neg,
                                 "lw":1.1,"connectionstyle":"angle3"},
            bbox={"facecolor":"white","edgecolor":"none","pad":2.5})
ax.annotate(r"$a=+1$"+"\n"+r"$L_1^*g=0$"+"\n"+r"$\|L_1g\|_2^2=2$",
            xy=(1,2),xytext=(0.05,2.67),fontsize=12,va="top",ha="left",
            color=pos,arrowprops={"arrowstyle":"->","color":pos,
                                 "lw":1.1,"connectionstyle":"angle3"},
            bbox={"facecolor":"white","edgecolor":"none","pad":2.5})

# The two profiles are identical because |a|=1, not two displaced curves.
inset=ax.inset_axes([0.065,0.515,0.385,0.405])
xx=np.linspace(-3.2,3.2,600)
gg=math.pi**(-0.25)*np.exp(-xx*xx/2)
inset.fill_between(xx,gg,color="#ddd2eb",alpha=0.65)
inset.plot(xx,gg,color="#744795",lw=2.1)
inset.set_xlim(-3.2,3.2)
inset.set_ylim(0,0.85)
inset.set_xticks([-2,0,2])
inset.set_yticks([0,0.5])
inset.tick_params(labelsize=9)
inset.set_xlabel(r"$x$",fontsize=10,labelpad=1)
inset.text(0.045,0.94,r"$g(x)$",transform=inset.transAxes,
           fontsize=10,va="top",color="#5a3675")
inset.set_title(r"$g_{-1}=g_1=\pi^{-1/4}e^{-x^2/2}$",
                fontsize=10.5,pad=7)
inset.set_facecolor("#fcfafc")

fig.text(0.075,0.244,
         r"$g_a(x)=(|a|/\pi)^{1/4}e^{-|a|x^2/2},\quad \|g_a\|_2=1"
         r"\quad(a\ne0)$",fontsize=12)
fig.text(0.075,0.217,"Schwartz equality profiles; smooth compact cutoffs approach these energies.",
         fontsize=10.8,color="#364354")
fig.text(0.075,0.190,r"At $a=0$, the infimum is $0$ and has no normalized $L^2$ minimizer.",
         fontsize=10.8,color="#364354")

fig.text(0.565,0.902,"B  Exact complex-zero closure",fontsize=17,weight="bold")
fig.text(0.565,0.864,r"$p(x,\xi)=\xi_1^2+x_1\xi_2^2,\qquad \phi=-x_1,\quad N=-e_1$",
         fontsize=13.5)
fig.text(0.565,0.832,r"$x_0=(0,0),\quad \xi_0=(0,1),\quad"
         r"F(s,t)=p((t,0),\xi_0+sN)=s^2+t$",fontsize=12)
bx=fig.add_axes([0.585,0.325,0.325,0.4875])
bx.set_aspect("equal",adjustable="box")
bx.set_xlim(-0.64,0.64)
bx.set_ylim(-0.64,0.64)
ticks=[-0.5,-0.25,0,0.25,0.5]
labels=[r"$-\frac{1}{2}$",r"$-\frac{1}{4}$","0",r"$\frac{1}{4}$",r"$\frac{1}{2}$"]
bx.set_xticks(ticks,labels)
bx.set_yticks(ticks,labels)
bx.tick_params(labelsize=12)
bx.set_xlabel(r"$\operatorname{Re}s$",labelpad=8)
bx.set_ylabel(r"$\operatorname{Im}s$",labelpad=8)
bx.grid(color="#e8edf2",lw=0.8,zorder=0)
bx.axhline(0,color="#718094",lw=1.1,zorder=1)
bx.axvline(0,color="#718094",lw=1.1,zorder=1)
# Inward arrows denote epsilon decreasing; exact root markers lie above them.
for start in [(0.56,0),(-0.56,0),(0,0.56),(0,-0.56)]:
    end=tuple(v*0.105/0.56 for v in start)
    bx.annotate("",xy=end,xytext=start,
                arrowprops={"arrowstyle":"->","color":"#8d98a8",
                            "lw":1.3,"mutation_scale":10},zorder=2)
colors=["#1761a1","#bf6b15","#248574"]
for epsilon,color in zip(epsilons,colors):
    e=float(epsilon)
    bx.scatter([-e,e],[0,0],s=90,marker="o",facecolors=color,
               edgecolors="white",linewidths=0.9,zorder=5)
    bx.scatter([0,0],[-e,e],s=95,marker="D",facecolors="white",
               edgecolors=color,linewidths=2,zorder=6)
bx.scatter([0],[0],s=20,color="#172438",zorder=7)
bx.text(0.035,-0.056,r"$0$",fontsize=11,ha="left",va="top",color="#172438")
legend=[Line2D([],[],color=color,lw=2.8,label=label)
        for color,label in zip(colors,[r"$\epsilon=1/2$",r"$\epsilon=1/4$",r"$\epsilon=1/8$"])]
bx.legend(handles=legend,loc="upper left",fontsize=10.5,
          frameon=True,facecolor="white",edgecolor="#d6dde5",
          framealpha=0.96,borderpad=0.7,handlelength=1.2)
fig.text(0.565,0.244,r"$\bullet\quad t=-\epsilon^2:\ s=\pm\epsilon"
         r"\qquad\diamond\quad t=+\epsilon^2:\ s=\pm i\epsilon$",
         fontsize=12)
fig.text(0.565,0.216,r"$\epsilon=\frac{1}{2},\frac{1}{4},\frac{1}{8},\ldots\ \longrightarrow0$:"
         r" all roots approach $s=0$.",fontsize=11.5)
fig.text(0.565,0.188,r"At the tangent point: $p_{x_1}=1,\quad p_\xi\!\cdot N=0,"
         r"\quad\{\bar p,\{p,\phi\}\}=2.$",fontsize=11.5)
fig.text(0.565,0.159,r"Necessary constraint if the Carleman estimate holds: $1\leq4K.$",
         fontsize=11.5,weight="bold",color="#273d57")

fig.text(0.055,0.105,
         "Proof locators: linear model — IV 28.2.2, p.235; closure — PN14–PN22; "
         "real constraint — PN25 / IV 28.2.1′, pp.238–239.",
         fontsize=10.7,color="#3e4958")
fig.text(0.055,0.076,
         "Coordinates and roots are exact. The Gaussian curve samples the displayed formula. "
         "Original CC0 figure.",
         fontsize=10.7,color="#3e4958")

fig.canvas.draw()
renderer=fig.canvas.get_renderer()
clipped=[]
text_boxes_checked=0
for artist in fig.findobj(match=Text):
    if artist.get_visible() and artist.get_text():
        box=artist.get_window_extent(renderer)
        text_boxes_checked+=1
        if box.x0 < 0 or box.y0 < 0 or box.x1 > 2880 or box.y1 > 1920:
            clipped.append(artist.get_text())
assert not clipped,clipped
fig.savefig(PNG,dpi=200,metadata={"Title":"Sharp linear energy and exact complex-zero closure",
                                "Description":"Original exact mathematical diagram; no theorem-existence claim.",
                                "License":"CC0-1.0","Software":"matplotlib"})
plt.close(fig)

checks={
    "scope":"Original figure algebra/numerical self-check; not independent theorem review",
    "python":sys.version.split()[0],"numpy":np.__version__,"matplotlib":matplotlib.__version__,
    "D_convention":"D=-i partial_x","linear_bracket":"{bar L,L}/i=2a",
    "sharp_energy_infimum":"max(2a,0)",
    "norm_domain":"normalized compact smooth tests; Schwartz equality profiles are approached by compact cutoffs",
    "a_zero":"infimum0, no normalized L2 minimizer",
    "gaussian_checks":gaussian_checks,
    "polynomial_model":polynomial_receipt(p),"phi":polynomial_receipt(phi),
    "Hp_phi":polynomial_receipt(hp_phi),"double_bracket":polynomial_receipt(double),
    "tangent_point":[str(v) for v in point],"dp_x1":"1","p_xi_dot_N":"0",
    "double_bracket_at_tangent":"2","principal_normality":"{bar p,p}=0 identically",
    "F(s,t)":"s^2+t","root_checks":root_checks,
    "necessary_constraint":"1<=4K if the Carleman estimate holds; not existence of an estimate",
    "png":PNG.name,"png_sha256":hashlib.sha256(PNG.read_bytes()).hexdigest().upper(),
    "png_dimensions":[2880,1920],"original_license":"CC0-1.0",
    "text_bounding_boxes_checked":text_boxes_checked,"text_clipped_at_canvas_boundary":clipped,
    "actual_pixel_inspection":"Recorded separately in figure-plan.json after generation",
}
CHECKS.write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"png":str(PNG),"sha256":checks["png_sha256"],
                  "checks":str(CHECKS),"exact_root_checks":len(root_checks)}))
