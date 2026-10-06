"""Original CC0 exact support bounds and cutoff weight-gap diagram.

The unknown support F and actual cutoff chi are not chosen or drawn.
Only the proved admissible regions, level curves and weight map are shown.
Run this file; all outputs stay in this author-owned directory.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import math
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np

OUT=Path(__file__).resolve().parent
PNG=OUT/"convexity-gap047.png"
CHECKS=OUT/"author-checks.json"
r,delta,s,t=F(1,4),F(1,64),F(1,128),F(1,256)
assert 0<t<s<delta<r*r/2
assert -r*r < -delta < -s < -t < 0
assert 1-2*r==F(1,2)
# On the sphere, q=y-r^2. Intersections with q=-delta:
y_intersection=r*r-delta
x_intersection_squared=r*r-y_intersection*y_intersection
assert y_intersection==F(3,64)
assert x_intersection_squared==F(247,4096)
# For y<=0, q=y-x^2-y^2>=-s implies x^2+y^2<=s+y<=s.
assert s<r*r and delta<r*r
for n in range(1,16):
    tn=delta*(1-F(1,2)**n)
    sn=(tn+delta)/2
    assert 0<tn<sn<delta
illustrative_lambda=20
a=math.exp(-illustrative_lambda*float(s))
b=math.exp(-illustrative_lambda*float(t))
assert 0<a<b<1
assert 2*2-1==3

def q(x,y):
    return y-x*x-y*y

def lower_level(x,level):
    """Exact lower branch of y-x^2-y^2=level, sampled for plotting."""
    discriminant=1-4*x*x-4*level
    return np.where(discriminant>=0,(1-np.sqrt(np.maximum(discriminant,0)))/2,np.nan)

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "mathtext.fontset":"dejavusans","axes.spines.top":False,
                     "axes.spines.right":False,"xtick.labelsize":10,
                     "ytick.labelsize":10})
fig=plt.figure(figsize=(18,10.5),dpi=180,facecolor="white")
fig.text(0.045,0.96,"Compact support levels create a strict weight gap",
         fontsize=24,weight="bold",va="top",color="#182b40")
fig.text(0.045,0.906,
         r"$\psi=y,\quad q=\psi_\epsilon=y-x^2-y^2,\quad r=\frac{1}{4},"
         r"\quad\delta=\frac{1}{64},\quad s=\frac{1}{128},\quad t=\frac{1}{256}$",
         fontsize=16)
fig.text(0.045,0.875,
         r"$Y=\{x^2+y^2<r^2,\ q>-\delta\},\qquad"
         r"F=\operatorname{supp}_Y u\ \subset\ Y\cap\{y\leq0\}$",
         fontsize=14,color="#324458")

blue="#216b97"
green="#237e60"
orange="#b56515"
gray="#6b7380"
ax=fig.add_axes([0.055,0.395,0.260,0.425])
bx=fig.add_axes([0.386,0.395,0.260,0.425])
cx=fig.add_axes([0.725,0.395,0.235,0.425])
ax.set_title("A  Neighborhood and strict replacement",fontsize=14,weight="bold",pad=13)
bx.set_title("B  Enlarged support-level bounds",fontsize=14,weight="bold",pad=13)
cx.set_title("C  Increasing weight map",fontsize=14,weight="bold",pad=13)

# Panel A: exact region definitions evaluated on a rectangular grid.
gx=np.linspace(-0.27,0.27,1001)
gy=np.linspace(-0.27,0.27,1001)
X,Y=np.meshgrid(gx,gy)
Q=q(X,Y)
ball=X*X+Y*Y<float(r*r)
domain=ball&(Q>-float(delta))
support_region=domain&(Y<=0)
ax.contourf(X,Y,np.where(ball,1,np.nan),levels=[0.5,1.5],colors=["#f0f2f5"])
ax.contourf(X,Y,np.where(domain,1,np.nan),levels=[0.5,1.5],colors=["#e5f0f8"])
ax.contourf(X,Y,np.where(support_region,1,np.nan),levels=[0.5,1.5],colors=["#f5d7b6"])
theta=np.linspace(0,2*np.pi,900)
ax.plot(float(r)*np.cos(theta),float(r)*np.sin(theta),color=gray,lw=1.5)
xx=np.linspace(-0.27,0.27,1001)
for level,color,style in [(0,green,":"),(-float(delta),orange,"-")]:
    ax.plot(xx,lower_level(xx,level),color=color,lw=1.8,ls=style)
ax.axhline(0,color="#283b4f",lw=1.3)
ax.plot([0,float(r)],[0,0],color=gray,lw=1.0)
ax.scatter([0],[0],s=25,color="#20364b",zorder=6)
ax.text(0.032,-0.035,r"$0$",fontsize=11)
ax.text(-0.13,0.14,r"$Y\cap\{y>0\}$"+"\nKnown zero side",color=blue,fontsize=11)
ax.text(0.12,-0.02,r"$r=1/4$",fontsize=10.8,color=gray)
ax.annotate(r"$q=0$",xy=(0.17,float(lower_level(np.array([0.17]),0)[0])),
            xytext=(0.05,0.087),fontsize=10.8,color=green,
            arrowprops={"arrowstyle":"->","color":green,"lw":1})
ax.annotate(r"$q=-\delta$",xy=(-0.195,float(lower_level(np.array([-0.195]),-float(delta))[0])),
            xytext=(-0.254,0.073),fontsize=10.8,color=orange,
            arrowprops={"arrowstyle":"->","color":orange,"lw":1})
ax.set_xlim(-0.27,0.27);ax.set_ylim(-0.27,0.27)
ax.set_aspect("equal")
ax.set_xticks([-0.25,0,0.25],[r"$-1/4$","0",r"$1/4$"])
ax.set_yticks([-0.25,0,0.25],[r"$-1/4$","0",r"$1/4$"])
ax.set_xlabel(r"$x$");ax.set_ylabel(r"$y$")
ax.grid(color="#dce2e8",alpha=0.5,lw=0.7)

# Panel B: the support is unknown. Fill only upper bounds on its regions.
gx2=np.linspace(-0.145,0.145,1201)
gy2=np.linspace(-0.019,0.0055,701)
XX,YY=np.meshgrid(gx2,gy2)
QQ=q(XX,YY)
R=(YY<=0)&(QQ>-float(delta))
R_s=(YY<=0)&(QQ>=-float(s))
R_t=(YY<=0)&(QQ>=-float(t))
strip=(YY<=0)&(QQ>-float(delta))&(QQ<-float(s))
bx.contourf(XX,YY,np.where(R,1,np.nan),levels=[0.5,1.5],colors=["#f5e2cb"])
bx.contourf(XX,YY,np.where(strip,1,np.nan),levels=[0.5,1.5],colors=["#ecc699"])
bx.contourf(XX,YY,np.where(R_s,1,np.nan),levels=[0.5,1.5],colors=["#cfe3f3"])
bx.contourf(XX,YY,np.where(R_t,1,np.nan),levels=[0.5,1.5],colors=["#badfce"])
bx.axhline(0,color="#283b4f",lw=1.3)
for level,color in [(-float(delta),orange),(-float(s),blue),(-float(t),green)]:
    curve=lower_level(gx2,level)
    bx.plot(gx2,np.where(curve<=0,curve,np.nan),lw=1.7,color=color)
for fraction,color in [(delta,orange),(s,blue),(t,green)]:
    e=math.sqrt(float(fraction))
    bx.scatter([-e,e],[0,0],s=22,color=color,zorder=5)
bx.text(-0.139,0.0025,r"$y>0$: known zero side",color=blue,fontsize=10.5)
bx.text(-0.14,-0.0177,"Vertical scale enlarged; axes give exact coordinates.",
        fontsize=9.6,color="#45566a")
bx.set_xlim(-0.145,0.145);bx.set_ylim(-0.019,0.0055)
bx.set_xticks([-0.125,-0.0625,0,0.0625,0.125],
              [r"$-1/8$",r"$-1/16$","0",r"$1/16$",r"$1/8$"])
bx.set_yticks([-float(delta),-float(s),-float(t),0],
              [r"$-\delta$",r"$-s$",r"$-t$","0"])
bx.set_xlabel(r"$x$");bx.set_ylabel(r"$y$")
bx.grid(color="#dce2e8",alpha=0.6,lw=0.7)
bx.legend(handles=[
    Patch(facecolor="#cfe3f3",label=r"$K_s\subset R_s=\{y\leq0,\ q\geq-s\}$"),
    Patch(facecolor="#badfce",label=r"Target support bound: $y\leq0,\ q\geq-t$"),
    Patch(facecolor="#ecc699",label=r"Allowed error bound: $y\leq0,\ -\delta<q<-s$")],
    loc="lower center",bbox_to_anchor=(0.50,-0.47),fontsize=10,
    frameon=False,ncol=1,handlelength=1.2,handleheight=1.1)

# Panel C: z denotes the scalar q level, not a base coordinate.
z=np.linspace(-float(delta),0,601)
w=np.exp(illustrative_lambda*z)
cx.axvspan(-float(delta),-float(s),color="#f6dfc4")
cx.axvspan(-float(t),0,color="#d5eadf")
cx.plot(z,w,color="#223f60",lw=2.6)
cx.scatter([-float(s),-float(t)],[a,b],c=[orange,green],s=55,zorder=5)
cx.hlines([a,b],-float(delta),[-float(s),-float(t)],
          colors=[orange,green],linestyles=":",linewidths=1.2)
mid=-(float(s)+float(t))/2
cx.annotate("",xy=(mid,b),xytext=(mid,a),
            arrowprops={"arrowstyle":"<->","color":blue,"lw":1.5})
cx.text(mid+0.0007,(a+b)/2,r"$b-a>0$",fontsize=11,color=blue,va="center")
cx.annotate(r"$a=e^{-\lambda s}$",xy=(-float(s),a),
            xytext=(-0.0145,0.965),fontsize=11,color=orange,
            arrowprops={"arrowstyle":"->","color":orange,"lw":1.1})
cx.annotate(r"$b=e^{-\lambda t}$",xy=(-float(t),b),
            xytext=(-0.0064,0.760),fontsize=11,color=green,
            arrowprops={"arrowstyle":"->","color":green,"lw":1.1})
cx.set_xlim(-float(delta)-0.0003,0.0003);cx.set_ylim(0.715,1.035)
cx.set_xticks([-float(delta),-float(s),-float(t),0],
              [r"$-\delta$",r"$-s$",r"$-t$","0"])
cx.set_yticks([0.75,0.85,0.95,1])
cx.set_xlabel(r"level $z=q$");cx.set_ylabel(r"$\phi=e^{\lambda z}$")
cx.grid(color="#dce2e8",alpha=0.6,lw=0.7)
cx.text(0.04,0.94,r"$\lambda=20$ is illustrative.",transform=cx.transAxes,
        fontsize=10.2,va="top",color="#47566a")
fig.text(0.727,0.298,"The proof fixes one admissible λ first.\n"
         "For every such λ>0, a<b;\nthen the Carleman parameter τ grows.",
         fontsize=11.5,color="#364a60",va="top")

fig.text(0.055,0.326,
         r"Only a support region is shown: $F\subset Y\cap\{y\leq0\}$.",
         fontsize=10.7,color="#405268")
fig.text(0.055,0.297,
         r"$q\leq\psi=y$, strictly away from $0$."+"\n"
         r"On $F$: $q\leq\psi\leq0$."+"\n"
         r"Sphere limits with $y\leq0$: $q\leq-1/16<-s$."+"\n"
         r"At the other boundary: $q=-1/64<-s$.",
         fontsize=10.7,color="#364a60",va="top")

fig.text(0.045,0.167,
         r"Compact cutoff: choose $\chi\in C_c^\infty(Y)$ with $\chi=1$ near $K_s$."
         r"  Then $\operatorname{supp}[P,\chi]u\subset\{q<-s\}$ and $\chi u=u$ on $\{q\geq-t\}$.",
         fontsize=13.5)
fig.text(0.045,0.126,
         r"$\|u\|^2_{L^2(Y\cap\{q\geq-t\})}\leq4C_0A^2\,\tau^{-3}"
         r"\exp[-2\tau(b-a)]\ \longrightarrow0,"
         r"\qquad A=\|[P,\chi]u\|_2,\quad a=e^{-\lambda s}<b=e^{-\lambda t}$",
         fontsize=14)
fig.text(0.045,0.088,
         r"Exhaustion: for every $0<t<s<\delta$ choose a fixed cutoff; "
         r"$t_n=\delta(1-2^{-n})\uparrow\delta,\quad s_n=(t_n+\delta)/2$ gives vanishing throughout $Y$.",
         fontsize=12)
fig.text(0.045,0.051,
         "Exact levels and regions; boundaries are sampled from exact formulas. F and the actual cutoff are unspecified. "
         "Proof: U1–U12, EX9. Human source: Hörmander IV, Theorem28.3.4, printed pp.241–242. Original CC0.",
         fontsize=10.4,color="#45566a")

fig.canvas.draw()
renderer=fig.canvas.get_renderer()
clipped=[]
text_count=0
width,height=fig.canvas.get_width_height()
for artist in fig.findobj(match=Text):
    if artist.get_visible() and artist.get_text():
        box=artist.get_window_extent(renderer)
        text_count+=1
        if box.x0<0 or box.y0<0 or box.x1>width or box.y1>height:
            clipped.append(artist.get_text())
assert not clipped,clipped
fig.savefig(PNG,dpi=180,metadata={"Title":"Compact support levels and the strict Carleman weight gap",
                                 "Description":"Exact region bounds, not a chosen solution or cutoff",
                                 "License":"CC0-1.0","Software":"Matplotlib"})
plt.close(fig)

checks={
 "scope":"Author exact geometry and numerical plotting self-check; not independent review",
 "python":sys.version.split()[0],"numpy":np.__version__,"matplotlib":matplotlib.__version__,
 "parameters":{"r":str(r),"delta":str(delta),"s":str(s),"t":str(t)},
 "psi":"y","smooth_replacement_q":"y-x^2-y^2",
 "gradient":"(-2x,1-2y); second component>=1/2 on closedB_1/4",
 "exact_ordering":"0<t<s<delta<r^2/2",
 "circle_support_bound":"q<=-r^2=-1/16<-s on y<=0",
 "other_domain_boundary":"q=-delta=-1/64<-s",
 "circle_level_intersection":{"y":"3/64","x_squared":"247/4096","x":"+-sqrt(247)/64"},
 "support_definition":"F is unspecified relative support,onlyF subsetY intersect{y<=0} is shown",
 "potential_compact_bound":"K_s subsetR_s={y<=0,q>=-s};|z|^2<=s+y<=s<r^2",
 "allowed_error_bound":"supp[P,chi]u subsetF intersect{-delta<q<-s}; region is an upperbound,not actual commutator support",
 "cutoff":"Chosen abstractly afterK_s compactness; no particular chi drawn",
 "level_formula":"lower levelq=c has y=(1-sqrt(1-4x^2-4c))/2",
 "level_endpoints":"Ony=0,q=-c givesx=+-sqrt(c); delta endpoints+-1/8,t endpoints+-1/16,s endpoints+-sqrt(2)/16",
 "weight_map":"z=q maps to exp(lambda*z); a=exp(-lambda*s)<b=exp(-lambda*t) forlambda>0",
 "illustrative_lambda":illustrative_lambda,
 "illustrative_lambda_claimed_admissible":False,
 "illustrative_weight_values":{"a":a,"b":b,"b_minus_a":b-a},
 "parameter_order":"Actual admissiblelambda fixed byproof,cutofffixed,weakgraphlimit atfixedtau,then tau increases",
 "norm_bound":"4C0A^2 tau^-3 exp[-2tau(b-a)] for the ordertwo exercise; actualu/values not drawn",
 "exhaustion":"All0<t<s<delta;tn=delta(1-2^-n),sn=(tn+delta)/2",
 "text_boxes_checked":text_count,"text_clipped_at_canvas":[],"dimensions":[width,height],
 "png_sha256":hashlib.sha256(PNG.read_bytes()).hexdigest().upper(),
 "original_license":"CC0-1.0","independent_review":False,
 "actual_author_pixels_inspected":"Separate receipt after generation"
}
CHECKS.write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"png":str(PNG),"png_sha256":checks["png_sha256"],
                  "checks":str(CHECKS),"text_boxes_checked":text_count,"dimensions":[width,height]}))
