"""Exact symbol and matrix plots. Independent new code: CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.size":11,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,3,figsize=(13,4.6),layout="constrained")
fig.suptitle("Matrix weight, block obstruction and regularization",fontsize=16)
t=np.linspace(-1,1,201)
axes[0].plot(t,8+2*np.sqrt(1+t*t),label="Upper eigenvalue",color="#147d92",linewidth=2)
axes[0].plot(t,8-2*np.sqrt(1+t*t),label="Lower eigenvalue",color="#bc5225",linewidth=2)
axes[0].axhline(5,color="#536471",linestyle=":",label="Strict lower bound: 5")
axes[0].set(title="Positive weight (MD31)",xlabel="Matrix parameter t",ylabel="Eigenvalues of 8I + 2k(t)")
axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
axes[1].plot(t,-(1+t*t),label="Polynomial eigenvalue -(1+t²)",color="#147d92",linewidth=2)
axes[1].axhline(0,color="#536471",label="Other eigenvalue: 0")
axes[1].axhline(1,color="#bc5225",linestyle="--",label="Block value on (e₂,e₁): +1")
axes[1].set(title="Block obstruction (MD32)",xlabel="Real normal covariable t",ylabel="Polynomial eigenvalues / block value",ylim=(-2.3,1.8))
axes[1].legend(fontsize=8,loc="upper center");axes[1].grid(alpha=.2)
q=np.linspace(0,4,241)
axes[2].plot(q,2*q*q/(1+q*q),color="#147d92",linewidth=2)
axes[2].axhline(2,color="#bc5225",linestyle=":",label="Upper bound: 2")
axes[2].set(title="Regularization transition (MD33)",xlabel="t = epsilon |eta|",ylabel="2t² / (1+t²)",ylim=(-.1,2.2))
axes[2].legend(fontsize=9);axes[2].grid(alpha=.2)
out=ROOT/"figures/matrix-damping-and-defect.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 illustration"});plt.close(fig)
record={"svg":"figures/"+out.name,"svg_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
        "generator_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_formula_locators":["MD31","MD32","MD33"],"original_illustration":True,
        "numerical_pde_solution_claimed":False,"actually_inspected":False}
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":out.name,"panels":3}))
