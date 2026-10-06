from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).resolve().parent
n=np.arange(1,13)
fig,ax=plt.subplots(figsize=(10,5.5),facecolor="#fbfbf8")
ax.set_facecolor("#fbfbf8")
ax.plot(n,np.sqrt(2*n+1),"o--",color="#838c95",label=r"Original bound: $\sqrt{2n+1}$")
ax.plot(n,np.sqrt(2*n/(n+1)),"o-",color="#20718a",label=r"Sharp full-form norm: $\sqrt{2n/(n+1)}$")
ax.set(xlabel="Dimension n (positive integers)",ylabel="Constant in the original B to L2 bound",
       xlim=(.7,12.3),ylim=(.75,5.3))
ax.set_xticks(n)
ax.grid(alpha=.18)
ax.legend(loc="upper left",fontsize=12)
ax.set_title("The full Bott oscillator: original and sharp upper constants",fontsize=16,pad=15)
fig.text(.5,.04,r"BS1–BS2: same $\mathcal{B}$ norm and full $\mathcal{D}$; equality at $e^{-|x|^2/2}e_1\wedge\cdots\wedge e_n$.",
         ha="center",fontsize=11)
fig.subplots_adjust(bottom=.18)
fig.savefig(out/"bott_full_graph_bound.png",dpi=160,facecolor=fig.get_facecolor())
fig.savefig(out/"bott_full_graph_bound.svg",facecolor=fig.get_facecolor())
plt.close(fig)
print("Saved Bott graph bound PNG/SVG")

