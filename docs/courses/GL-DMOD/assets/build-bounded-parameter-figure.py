"""Exact cone, denominator, normal-circle and compact-collar coordinates."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

root=Path(__file__).resolve().parent
out=root if root.name=="assets"else root/"assets"
out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                    "svg.hashsalt":"RC-bounded-parameters",
                    "axes.spines.top":False,"axes.spines.right":False})
fig,axes=plt.subplots(2,2,figsize=(14,11.5))
fig.subplots_adjust(left=.075,right=.965,top=.90,bottom=.22,wspace=.30,hspace=.50)
blue,purple,red,green="#215d8c","#6c4d90","#a54536","#38755b"
mu,nu,K,eps=Fraction(1,4),Fraction(1,2),5,Fraction(1,2)

ax=axes[0,0]
ax.set_title("A  Every denominator zero is inside the cone",loc="left",weight="bold",fontsize=12)
ell=np.linspace(0,1,601)
ax.fill_between(ell,0,np.minimum(1,5*ell),color="#e3eee7",label=r"$r\leq5\ell$ (slice $b=0$)")
ax.plot(ell,np.sqrt(np.maximum(0,1-ell**2)),color="#6c7c8b",lw=1.5)
delta=np.linspace(.25,.5,201)
lam=(np.sqrt(1+4*delta**2)-1)/(2*delta)
rr=np.sqrt(1-lam**2)
ax.plot(lam,rr,color=red,lw=4,label=r"$F_{\delta I}=0,\quad 1/4\leq\delta\leq1/2$")
ax.scatter([1/np.sqrt(26)],[5/np.sqrt(26)],color=green,zorder=5)
ax.annotate(r"$r=5\ell$",xy=(1/np.sqrt(26),5/np.sqrt(26)),
            xytext=(.02,.70),arrowprops={"arrowstyle":"->","color":green},color=green)
ax.text(.42,.62,r"$\ell^2+r^2=1$",color="#475c6b",fontsize=12)
ax.set(xlim=(0,1.02),ylim=(0,1.04),xlabel=r"$\ell=-\operatorname{Re}w_0$",
       ylabel=r"$r=|z|$")
ax.legend(frameon=False,loc="lower right",fontsize=10)
ax.text(0,-.29,"Scalar Hermitian section; strict containment is RC.5–RC.6 for every H.",
        transform=ax.transAxes,fontsize=10)

ax=axes[0,1]
ax.set_title("B  A real section of the denominator bounds",loc="left",weight="bold",fontsize=12)
q=np.linspace(5,12,401)
for val,color in [(.25,blue),(.5,purple)]:
    f=-1/np.sqrt(1+q*q)+val*q*q/(1+q*q)
    ax.plot(q,f,color=color,lw=2.3,label=rf"$\delta={val:g}$")
ax.axhline(0,color="#999999",lw=.8)
ax.set(xlim=(5,12),ylim=(-.01,.46),xlabel=r"$q=|z|/\ell\geq5$",
       ylabel=r"$F_{\delta I}/\rho$ on $b=0,\ \rho=1$")
ax.legend(frameon=False,loc="upper left")
ax.text(0,-.29,"This slice is not the general lower bound c; RC.8 proves that bound.",
        transform=ax.transAxes,fontsize=10)

ax=axes[1,0]
ax.set_title("C  The positive normal circle in either order",loc="left",weight="bold",fontsize=12)
theta=np.linspace(0,2*np.pi,401)
f=.5*np.exp(1j*theta)
ax.plot(f.real,f.imag,color=blue,lw=2.5)
ax.scatter([0,1],[0,0],color=[blue,red],s=45,zorder=4)
ax.annotate("",xy=(f[90].real,f[90].imag),xytext=(f[65].real,f[65].imag),
            arrowprops={"arrowstyle":"->","lw":2,"color":blue})
ax.text(-.06,-.13,"0",color=blue)
ax.text(.94,-.13,"1",color=red)
ax.text(-.64,.62,r"$f/F=e^{i\theta}/2$",fontsize=13,color=blue)
ax.text(.60,.37,"Other pole\nis outside",fontsize=10,color=red)
ax.set_aspect("equal")
ax.set(xlim=(-.72,1.3),ylim=(-.65,.74),xlabel=r"$\operatorname{Re}(f/F)$",
       ylabel=r"$\operatorname{Im}(f/F)$")
ax.text(0,-.35,r"$|f|=|F|/2,\quad |F-f|\geq|F|/2$",
        transform=ax.transAxes,fontsize=12)

ax=axes[1,1]
ax.set_title("D  One collar contains the whole closed family",loc="left",weight="bold",fontsize=12)
ax.add_patch(Rectangle((0,0),2,1,fill=False,ec="#5c6872",lw=1.5))
ax.add_patch(Rectangle((0,0),1.5,.75,fill=False,ec=purple,lw=1.7,ls="--"))
ax.add_patch(Rectangle((0,0),.75,.25,color="#dceaf3",ec=blue,lw=1.4))
ax.add_patch(Rectangle((0,0),.5,9/64,color="#e9d3c8",ec=red,lw=1.3))
ax.text(.02,.07,"Contour family",fontsize=10,color=red)
ax.text(.05,.29,r"$\chi=1$ on the inner box",fontsize=10,color=blue)
ax.text(.84,.60,"Collar support\ninside dashed box",fontsize=10,color=purple)
ax.text(.9,.90,"Actual middle domain",fontsize=10,color="#455966")
ax.set(xlim=(0,2.08),ylim=(0,1.05),xlabel=r"$|y|$",ylabel=r"$|s|$")
ax.text(0,-.28,r"$r_t=r_x=r_w=1/16,\quad |s|\leq9/64,\quad |y|\leq1/2$",
        transform=ax.transAxes,fontsize=11)

fig.suptitle("Bounded Hermitian generating parameters and a common contour collar",
             fontsize=19,weight="bold")
fig.text(.075,.028,
    "A–B: exact scalar sections of RC.3–RC.8.  C: RC.17–RC.19 and RC.24.  D: a projection to norms, with the exact bounds of RC.21–RC.22.\n"
    "The contour family is properly contained in one middle chart; its identification with the microlocal-Hom composition is a separate statement.",
    fontsize=10,color="#334b58")
stem="bounded-generating-parameters-and-collar"
fig.savefig(out/(stem+".png"),dpi=180)
fig.savefig(out/(stem+".svg"),metadata={"Date":None})
plt.close(fig)
data={
    "mu":str(mu),"nu":str(nu),"K":K,"epsilon":str(eps),
    "cone_margin":"2/sqrt(105)",
    "zero_bound":"q^2 <= 1+mu^(-2) = 17 < K^2 = 25",
    "scalar_zero_ell":"(sqrt(1+4*delta^2)-1)/(2*delta)",
    "panel_A":"unit normal section b=0, ell>=0, r>=0, H=delta*I",
    "panel_B":"rho=1, w0=-1/sqrt(1+q^2), |z|=q/sqrt(1+q^2), q>=5",
    "normal_circle":"f/F=exp(i*theta)/2; other pole at1",
    "endpoint_bounds":["1/16","1/16","1/16"],
    "contour_norm_bounds":{"y":"1/2","s":"9/64"},
    "collar_equals_one_box":{"y":"3/4","s":"1/4"},
    "collar_support_box":{"y":"3/2","s":"3/4"},
    "actual_middle_radii":{"y":"2","s":"1"},
    "panel_D":"projection to |y|,|s|, not a picture of the full middle fibre",
    "actual_coefficient_composition_identity_asserted":False,
}
(out/(stem+"-exact-data.json")).write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if root!=out:(out/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print(json.dumps({"pixels":[2520,2070],"assets":4}))
