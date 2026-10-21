"""Figure22.4: exact formulas from Example22.57, in units of log(2)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).resolve().parent
e=np.arange(9)
t=np.linspace(0,8,401)
fig,axes=plt.subplots(1,2,figsize=(11.4,4.4),layout="constrained")
blue="#126ca6"; orange="#bf5b16"; purple="#70539e"
ax=axes[0]
ax.plot(t,t,color=blue,lw=1.8,alpha=.6)
ax.scatter(e,e,color=blue,s=36,label=r"Additive: $e$")
ax.plot(t,2.**(-t),color=orange,lw=1.8,alpha=.6)
ax.scatter(e,2.**(-e),color=orange,s=36,label=r"Multiplicative: $2^{-e}$")
ax.set_title("Division by $2^e$ in each group")
ax.set_ylabel(r"Arithmetic height $h\,/\,\log 2$")
ax.legend(loc="upper left",frameon=False)
ax=axes[1]
ax.plot(t,t+2.**(-t),color=purple,lw=1.8,alpha=.65)
ax.scatter(e,e+2.**(-e),color=purple,s=36,label=r"Product: $e+2^{-e}$")
ax.plot(t,t+1,color="#656565",ls="--",lw=1.4,label=r"Upper bound: $e+1$")
ax.set_title("The Segre product adds the heights")
ax.legend(loc="upper left",frameon=False)
for ax in axes:
    ax.set_xlabel("Number of divisions, $e$")
    ax.set_xlim(-.25,8.25);ax.set_xticks(e)
    ax.set_ylim(-.25,9.6)
    ax.grid(True,alpha=.18)
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(root/"dyadic-division-heights.png",dpi=175,facecolor="white")
plt.close(fig)
