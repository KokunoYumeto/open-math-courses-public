"""Numerical Airy quotient samples and an exact scaling curve. CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
from scipy.special import airy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"font.size":11,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,3,figsize=(13,4.6),layout="constrained")
fig.suptitle("A zero-free outgoing quotient and its boundary inverse",fontsize=15)
t=np.linspace(-9,9,501)
ai,aip,bi,bip=airy(t)
q=(aip-1j*bip)/(ai-1j*bi)
axes[0].plot(t,q.real,label="Real part",color="#147d92",linewidth=2)
axes[0].plot(t,q.imag,label="Imaginary part",color="#bc5225",linewidth=2)
axes[0].axhline(0,color="#536471",linewidth=.7)
axes[0].set(title="Outgoing quotient (AB13)",xlabel="Real Airy variable t",ylabel="F′(t) / F(t)")
axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
axes[1].plot(t,(1+t*t)**.25/np.abs(q),color="#147d92",linewidth=2)
axes[1].set(title="Inverse after its weight (AB15)",xlabel="Real Airy variable t",ylabel="⟨t⟩^(1/2) / |F′(t)/F(t)|")
axes[1].grid(alpha=.2)
lam=np.geomspace(1,1000,301)
axes[2].loglog(lam,lam**(-2/3),color="#147d92",linewidth=2,label="Exact exponent: −2/3")
axes[2].set(title="At the transition t₀ = 0 (AB36)",xlabel="Tangential frequency λ",ylabel="Normalized inverse magnitude")
axes[2].legend(fontsize=9);axes[2].grid(which="both",alpha=.2)
out=ROOT/"figures/airy-quotient-and-boundary-inverse.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 illustration"});plt.close(fig)
record={"svg":"figures/"+out.name,"svg_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
    "generator_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "exact_formula_locators":["AB13","AB15","AB36"],"original_illustration":True,
    "numerical_scope":"First two panels: SciPy Airy samples using the Bi normalization proved after AB14. Third panel: exact normalized power law.",
    "numerical_pde_solution_claimed":False,"actually_inspected":False}
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":out.name,"panels":3}))
