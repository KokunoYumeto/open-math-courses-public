"""Exact coefficient and boundary-form plots. Independent new code: CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.size":11,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,3,figsize=(13,4.4),layout="constrained")
fig.suptitle("Removing the normal derivative keeps a boundary term",fontsize=16)
x=np.linspace(0,1,201)
axes[0].plot(x,1+2*x,label="Real part: 1 + 2x",color="#147d92",linewidth=2)
axes[0].plot(x,-1+x,label="Imaginary part: -1 + x",color="#bc5225",linewidth=2)
axes[0].set(title="Ordered gauge (NC29)",xlabel="Normal coordinate x",ylabel="Off-diagonal entry of kappa")
axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
e=np.linspace(0,1.2,241)
axes[1].plot(e,np.exp(-4*e*e)-np.exp(-9*e*e),color="#147d92",linewidth=2)
axes[1].set(title="Robin defect, n = 2 (NC30)",xlabel="Smoothing parameter epsilon",ylabel="exp(-4 epsilon^2) - exp(-9 epsilon^2)")
axes[1].axhline(0,color="#536471",linewidth=.6);axes[1].grid(alpha=.2)
v=[-3,-1,-2]
axes[2].bar(range(3),v,color=["#65778a","#147d92","#bc5225"],width=.6)
axes[2].set_xticks(range(3),["exp(-x)","x exp(-x)","(1+x) exp(-x)"],fontsize=9)
axes[2].set(title="Boundary form, r = 2 (NC31)",ylabel="Oriented boundary contribution",ylim=(-3.8,.3))
axes[2].axhline(0,color="#536471",linewidth=.8)
for k,a in enumerate(v):axes[2].text(k,a-.12,str(a),ha="center",va="top")
axes[2].text(.5,.03,"t = 0, b = 0: volume contribution = 0",transform=axes[2].transAxes,ha="center",fontsize=8)
out=ROOT/"figures/gauge-boundary-identity.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 illustration"})
plt.close(fig)
record={"svg":"figures/"+out.name,"svg_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
        "generator_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_formula_locators":["NC29","NC30","NC31"],
        "original_illustration":True,"numerical_pde_solution_claimed":False,
        "actually_inspected":False}
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":out.name,"panels":3}))
