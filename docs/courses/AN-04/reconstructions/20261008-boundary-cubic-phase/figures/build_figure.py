"""Exact BC35-BC38 coordinate plots for the variable-base example. CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"svg.fonttype":"none","font.size":10,"svg.hashsalt":"AN04-BCP-20261008"})
fig,ax=plt.subplots(1,3,figsize=(13,4.6),layout="constrained")
y1=.4;mu=-.12
f=lambda q:np.exp(y1/4)*(q+q*q/5)
df=lambda q:np.exp(y1/4)*(1+2*q/5)
q=np.linspace(-.15,.4,401)
ax[0].fill_between(q,-f(q),.25,color="#e4f4ef")
ax[0].plot(q,-f(q),color="#007f97",lw=2,label="caustic")
ax[0].axvline(0,color="#546171",ls="--",lw=1)
ax[0].axhline(mu,color="#b34f0d",ls=":",lw=1)
ax[0].set(title="Caustic and attained side (BC37)",xlabel=r"$q$",ylabel=r"$\mu$",ylim=(-.5,.25))
ax[0].text(.06,.1,r"$f+\mu\geq0$",color="#276a53")
ax[0].text(-.145,-.46,r"$q=0$: boundary",fontsize=9)
qc=(-5+np.sqrt(25-20*mu*np.exp(-y1/4)))/2
u=np.linspace(qc,.4,301)
a=np.maximum(f(u)+mu,0)
phase=2*a**1.5/3
momentum=df(u)*np.sqrt(a)
for panel,values,title,ylabel in [
 (ax[1],phase,"Two characteristic phases (BC4)",r"$\phi_\pm-\theta$"),
 (ax[2],momentum,"Actual normal covectors (BC38)",r"$\partial_q\phi_\pm$")]:
 panel.plot(u,values,color="#007f97",lw=2,label="plus branch")
 panel.plot(u,-values,color="#b34f0d",lw=2,label="minus branch")
 panel.scatter([qc],[0],color="#172b44",s=28,zorder=3)
 panel.axvline(qc,color="#546171",ls=":",lw=1)
 panel.set(title=title,xlabel=r"$q$; fixed $\mu=-0.12$",ylabel=ylabel,xlim=(0,.4))
 panel.text(.006,.03,"no real\nsheet",transform=panel.transAxes,fontsize=9)
for panel in ax:
 panel.axhline(0,color="#718096",lw=.8);panel.grid(True,alpha=.2);panel.set_axisbelow(True)
fig.suptitle("Boundary cubic phase: exact variable-base example, lambda = 1 and y1 = 0.4",fontsize=13)
out=ROOT/"figures/boundary-cubic-phase-and-caustic.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 mathematical illustration"});plt.close(fig)
record=dict(svg=out.relative_to(ROOT).as_posix(),svg_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
 generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exact_formula_locators=["BC4","BC35","BC37","BC38"],original_illustration=True,
 numerical_scope="Coordinate plots of exact phase and covector formulas in the verified variable-base example.",
 actually_inspected=False)
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"generated":True,"figure":out.name,"caustic_at_fixed_mu":float(qc)}))
