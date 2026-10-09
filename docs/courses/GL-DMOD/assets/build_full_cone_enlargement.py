"""Exact slices for AN.19 support enlargement and proper intermediate fibers."""
from pathlib import Path
from fractions import Fraction
import argparse, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser()
parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent)
out=parser.parse_args().output;out.mkdir(parents=True,exist_ok=True)
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
    "svg.hashsalt":"full-cone-enlargement-v1"})
rows=[]
for k in range(21):
    s=Fraction(k,20);m=min(s,1-s)
    rows.append({"sigma":str(s),"normal_imaginary_radius":str(m/2),"spatial_radius":str(2*m)})
data={"epsilon":"1/2","A":"2","endpoint_difference":{"w":"-1","zeta":"0"},
    "fiber_samples":rows,"support_map_injectivity_asserted":False,
    "cone_open_or_derived_instantiation_asserted":False}
(out/"full-cone-enlargement-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
fig,axs=plt.subplots(1,3,figsize=(15.6,5.1));fig.patch.set_facecolor("#f7fafc")
s=np.linspace(0,1,201)
ax=axs[0];ax.fill_between(-s,-s/2,s/2,color="#dce8f6")
ax.plot(-s,s/2,color="#315b94");ax.plot(-s,-s/2,color="#315b94")
ax.plot(-s,0*s,color="#bd7629",linewidth=3,label=r"initial $\mathrm{Im}\,w=0$")
ax.set_title("Line-time support enlarges to a wedge",fontweight="bold")
ax.set_xlabel(r"$\mathrm{Re}\,w=-\sigma$");ax.set_ylabel(r"$\mathrm{Im}\,w$")
ax.set_xlim(-1.12,.08);ax.set_ylim(-.62,.62);ax.legend(loc="upper right",fontsize=9)
ax.text(-.65,.07,r"$\epsilon=1/2$",fontsize=12)
ax.text(-1.04,-.57,r"$|\mathrm{Im}\,w|\leq\sigma/2$",fontsize=11)
ax=axs[1];bound=np.minimum(s,1-s)/2
ax.fill_between(s,-bound,bound,color="#d7efe8");ax.plot(s,bound,color="#138477");ax.plot(s,-bound,color="#138477")
ax.scatter([0,1],[0,0],color="#138477",s=30,zorder=4)
ax.set_title("Proper normal intermediate fiber",fontweight="bold")
ax.set_xlabel(r"intermediate $\sigma\in[0,1]$");ax.set_ylabel(r"intermediate $\eta=\mathrm{Im}\,w_1$")
ax.set_xlim(-.07,1.07);ax.set_ylim(-.31,.31)
ax.text(.5,.285,r"$|\eta|\leq\frac{1}{2}\min(\sigma,1-\sigma)$",ha="center",fontsize=11)
ax.text(.5,-.29,r"endpoints: $w=0$ and $w=-1$",ha="center",fontsize=10)
ax=axs[2];radius=2*np.minimum(s,1-s)
ax.plot(s,radius,color="#a24676",linewidth=2.5);ax.fill_between(s,0,radius,color="#f1dfeb")
xs=[float(Fraction(r["sigma"])) for r in rows];ys=[float(Fraction(r["spatial_radius"])) for r in rows]
ax.scatter(xs,ys,color="#a24676",s=16,zorder=4)
ax.set_title("Closed complex spatial discs",fontweight="bold")
ax.set_xlabel(r"intermediate $\sigma$");ax.set_ylabel(r"spatial-disc radius, $A=2$")
ax.set_xlim(-.05,1.05);ax.set_ylim(-.04,1.17)
ax.text(.5,1.08,r"$|\zeta_1|\leq2\min(\sigma,1-\sigma)$",ha="center",fontsize=11)
fig.text(.5,.025,"AN.19: exact normal-plane slices and rational spatial-radius samples. Support enlargement is a chain map; injectivity and derived hypotheses are not inferred.",ha="center",fontsize=9)
fig.subplots_adjust(left=.065,right=.985,top=.88,bottom=.16,wspace=.28)
fig.savefig(out/"full-cone-enlargement.png",dpi=150,facecolor=fig.get_facecolor(),metadata={"Software":"Matplotlib"})
fig.savefig(out/"full-cone-enlargement.svg",facecolor=fig.get_facecolor(),metadata={"Date":None,"Creator":"Matplotlib"})
plt.close(fig)
print(json.dumps({"outputs":["full-cone-enlargement.png","full-cone-enlargement.svg","full-cone-enlargement-data.json"]}))
