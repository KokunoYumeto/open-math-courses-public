"""Reproduce the normal smooth-maximum section and coherent vanishing diagram."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10.5,
                     "svg.hashsalt":"GL-DMOD-CX-20261020"})
nodes,weights=np.polynomial.legendre.leggauss(64)
bump=np.exp(-1/(1-nodes**2))
weights=weights*bump
weights=weights/weights.sum()
eta=.2
shift=eta*nodes
ww=weights[:,None]*weights[None,:]
ts=np.linspace(-1,1,401)
values=[]
for t in ts:
 p=t*t+.5*t
 q=t*t-.5*t
 values.append(float((np.maximum(p+shift[:,None],q+shift[None,:])*ww).sum()))
values=np.asarray(values)
lower=ts**2+.5*np.abs(ts)
blue="#2758aa";teal="#00818d";ink="#15213b";gold="#b6781d"
fig,(a,b)=plt.subplots(1,2,figsize=(13.4,7.8),facecolor="#f7f9fd")
a.set_facecolor("#ffffff")
a.fill_between(ts,lower,lower+eta,color="#dce8fb",
               label=r"Exact envelope: $\max\phi_\pm\leq M\leq\max\phi_\pm+1/5$")
a.plot(ts,lower,color=gold,lw=1.5,ls="--",label=r"$t^2+|t|/2$")
a.plot(ts,values,color=teal,lw=2.2,label=r"CX.8: numerical 64 by 64 quadrature")
for t in [-.4,.4]:a.axvline(t,color=blue,lw=1,ls=":")
a.set_xlabel(r"Real normal coordinate $t$: $z=0,\ w=t$")
a.set_ylabel("Function value on the specified section")
a.set_title("Smooth maximum and exact deletion",pad=18,weight="bold")
a.set_xlim(-1,1);a.set_ylim(-.035,1.78)
a.legend(loc="upper center",fontsize=8.6,framealpha=.98)
a.grid(alpha=.2)
a.text(.5,-.15,r"Exact deletion for $|t|>2/5$; identity lower Levi bound",
       transform=a.transAxes,ha="center",va="center",color=ink,fontsize=9.8)
b.set_xlim(0,1);b.set_ylim(0,1);b.axis("off")
b.set_title("Coherent coefficients and the global passage",pad=18,weight="bold")
rows=[
 (.82,"Actual ambient quotient; local acyclicity","CX.G / SC.D–SC.E"),
 (.64,"Finite bumps give surjective positive cohomology","CX.H–CX.J"),
 (.46,"Compact maps give finite Hausdorff cohomology","CX.J / ML.C"),
 (.28,"Density kills the connecting map; sections glue","CX.K"),
 (.10,"Convergent inverse limits; global vanishing and generators","CX.L–CX.M / ML.H")]
for y,title,loc in rows:
 b.add_patch(FancyBboxPatch((.025,y),.95,.125,boxstyle="round,pad=0.012",
             facecolor="white",edgecolor="#acbfde",linewidth=1.1))
 b.text(.5,y+.083,title,ha="center",va="center",color=ink,fontsize=8.8)
 b.text(.5,y+.036,loc,ha="center",va="center",color=blue,fontsize=10)
for upper,lowerrow in zip(rows,rows[1:]):
 b.annotate("",xy=(.5,lowerrow[0]+.141),xytext=(.5,upper[0]-.016),
             arrowprops={"arrowstyle":"->","color":teal,"lw":1.6})
fig.subplots_adjust(left=.06,right=.985,top=.91,bottom=.14,wspace=.20)
for ext in ["png","svg"]:
 kwargs={"dpi":160}if ext=="png"else{"metadata":{"Date":None}}
 fig.savefig(r/("coherent-cartan."+ext),facecolor=fig.get_facecolor(),**kwargs)
plt.close(fig)
data={"proof_locators":["CX.67","CX.68","CX.G--CX.M"],
 "coordinates":"z=0, w=t real; full ambient space is C^2",
 "phi_plus":"|z|^2+|w|^2+(1/2)Re(w)",
 "phi_minus":"|z|^2+|w|^2-(1/2)Re(w)",
 "each_smoothing_radius":"1/5","exact_deletion_threshold":"2/5",
 "exact_lower_envelope":"t^2+|t|/2","exact_upper_envelope":"t^2+|t|/2+1/5",
 "levi_lower_bound":"identity matrix",
 "quadrature":"64-point Gauss-Legendre in each variable, even smooth bump reweighted and normalized",
 "sample_count":len(ts),
 "samples":[{"t":float(t),"quadrature_value":float(v),"exact_lower":float(l)}
            for t,v,l in zip(ts,values,lower)],
 "finite_quadrature_is_not_the_proof":True}
(r/"coherent-cartan-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
