"""Reproducible original illustration of AI37-AI39. CC0-1.0."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import airy
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({"svg.fonttype":"none","font.size":10,"svg.hashsalt":"AN04-AOI-20261008"})
fig,ax=plt.subplots(1,3,figsize=(13,4.5),layout="constrained")
mu=np.linspace(-5,5,501);lv=16.
ai,aip,bi,bip=airy(mu*lv**(-1/3));phi=(aip-1j*bip)/(ai-1j*bi);h=1/(1j*lv**(2/3)*phi)
kernel=(h-h[len(h)//2])*np.exp(-mu**2/4)
ax[0].plot(mu,np.abs(kernel),color="#007f97",lw=2)
ax[0].set(title="Noncommuting Gaussian factor (AI37)",xlabel=r"Output frequency $\mu$; incoming $\mu=0$",ylabel=r"$|h(\mu,16)-h(0,16)|e^{-\mu^2/4}$")
ll=np.geomspace(1,1000,201)
ax[1].loglog(ll,ll**(2/3),color="#b34f0d",lw=2)
ax[1].set(title="Ordinary derivative bound fails (AI38)",xlabel=r"Tangential frequency $\lambda$",ylabel=r"$|\partial_\mu h(0,\lambda)|/\lambda^{-5/3}$")
kk=np.arange(1,7);ax[2].bar(kk,2*kk/3,color="#007f97")
ax[2].set(title="Finite residual gain (AI39)",xlabel="Number of corrections k",ylabel="Sobolev derivatives gained",xticks=kk,yticks=[0,1,2,3,4])
for a in ax:a.grid(True,alpha=.18,which="both");a.set_axisbelow(True)
fig.suptitle("Matrix Airy inverses: operator order, transition scale and complete remainders",fontsize=14)
out=ROOT/"figures/airy-operator-order-and-remainders.svg"
fig.savefig(out,metadata={"Date":None,"Creator":"Independent AN-04 mathematical illustration"});plt.close(fig)
record={"svg":out.relative_to(ROOT).as_posix(),"svg_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
    "generator_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "exact_formula_locators":["AI37","AI38","AI39"],"original_illustration":True,
    "numerical_scope":"First panel: Airy samples of the exact normalized Fourier-kernel factor at lambda=16. Other panels: exact powers and proven residual orders.",
    "numerical_pde_solution_claimed":False,"actually_inspected":False}
(ROOT/"figure-check.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":str(out),"generated":True}))
