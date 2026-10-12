"""Original integration regions, full logarithmic remainder and physical selector."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
P=Path(__file__).resolve();mp.mp.dps=70

def regular(B):
    if B==0:return 1-3*mp.log(2)/2
    D=2+4*B+4*B*B
    return ((mp.log(2)-mp.log(D)+2*mp.log(1+2*B))/B
            +2/B*(mp.pi/4-mp.atan(1+2*B)+mp.atan(2*B))
            -2*mp.log(D)+2*mp.log(1+4*B*B)+4*mp.log(1+2*B)-4*mp.log(2))/4

def physical(x,h,p):
    if x==0:return mp.mpf(0)
    B=x/h
    return x**p*(regular(B)-mp.log(B))

fig,axs=plt.subplots(2,2,figsize=(13,10),layout="constrained")
fig.suptitle("Original weighted velocity integral: the valid exponent and the counterexample\n"
             "Chen–Hou source comparison · complete proof WJ1–WJ20",fontsize=14)
ax=axs[0,0]
ax.add_patch(Rectangle((-1,0),1,2,facecolor="#6ab0bf",alpha=.6))
ax.add_patch(Rectangle((0,0),2,2,facecolor="#e5b96d",alpha=.6))
ax.scatter([0,-2],[0,0],color=["#a53d34","#6e7785"],zorder=3)
ax.annotate("Integrable source singularity",(0,0),xytext=(-.7,-.45),fontsize=9,
            arrowprops=dict(arrowstyle="->",color="#a53d34"))
ax.annotate("Shifted pole outside both regions",(-2,0),xytext=(-2.1,-.7),fontsize=8)
ax.text(-.85,1.05,"J₁(B)",fontsize=15);ax.text(.65,1.05,"J₂(B)",fontsize=15)
ax.text(-1.95,2.4,"Original B = 1/2, L = 1/B = 2\nBoth shifted kernel terms and all endpoints are retained.",fontsize=9)
ax.set(xlim=(-2.25,2.25),ylim=(-.85,2.8),xlabel="Original coordinate s₁",
       ylabel="Original coordinate s₂",title="Full original integration regions · WJ1–WJ5")
ax.grid(alpha=.18)

ax=axs[0,1];B=np.linspace(0,.5,201)
curve=np.array([float(regular(mp.mpf(str(x)))) for x in B])
c=float(regular(mp.mpf(0)))
ax.plot(B,curve,color="#246e84",label="R(B), numerical illustration",lw=2)
ax.plot(B,c+B,ls="--",color="#b3722e",label="Proved upper bound R(0) + B")
ax.plot(B,c+B/2,ls=":",color="#428746",label="Proved lower bound R(0) + B/2")
ax.axhline(0,color="#8a929a",lw=.8)
ax.scatter([0],[c],color="#a53d34")
ax.annotate("R(0) = 1 − (3/2) log 2 < 0",(0,c),xytext=(.055,-.025),fontsize=9)
ax.set(xlim=(0,.5),xlabel="Original reciprocal cutoff B",ylabel="R(B) = J₂(B) + log B",
       title="Exact regular part and derivative bounds · WJ6–WJ12")
ax.legend(fontsize=8,loc="upper left");ax.grid(alpha=.15)

h=mp.mpf(3)/5
ax=axs[1,0];upper=h*mp.exp(-2)
xs=[upper*k/200 for k in range(201)]
ys=[float(physical(x,h,mp.mpf(1)/2)) for x in xs]
ax.plot(list(map(float,xs)),ys,color="#246e84",lw=2)
ax.scatter([float(upper)],[ys[-1]],color="#a53d34",s=28)
ax.text(.03,.94,"Original h = 3/5 and α = 1/2\n"
        "Every cell endpoint zᵘ ≤ h exp(−2) is valid.\n"
        "The complete product increases, including x = 0.",
        transform=ax.transAxes,va="top",fontsize=9)
ax.set(xlabel="Original physical rescaled coordinate x",
       ylabel="F₁/₂,ₕ(x) = x¹/² J₂(x/h)",
       title="The exponent used by the source is recovered · WJ13–WJ17",
       ylim=(0,.8))
ax.grid(alpha=.18)

ax=axs[1,1];upper=h*mp.exp(-10);lower=mp.mpf(999)/1000*upper;p=mp.mpf(1)/10
xs=[lower+(upper-lower)*k/200 for k in range(201)]
end=physical(upper,h,p)
ys=[float(physical(x,h,p)-end) for x in xs]
ax.plot(list(map(float,xs)),ys,color="#a53d34",lw=2)
ax.axhline(0,color="#737e85",lw=.8)
ax.ticklabel_format(axis="both",style="sci",scilimits=(0,0),useOffset=False)
ax.text(.03,.94,"Original h = 3/5 and α = 9/10\n"
        "zˡ = (999/1000) h exp(−10), zᵘ = h exp(−10)\n"
        "The complete derivative bracket is < −575/227328.",
        transform=ax.transAxes,va="top",fontsize=9)
ax.set(xlabel="Original physical rescaled coordinate x",
       ylabel="F₉/₁₀,ₕ(x) − F₉/₁₀,ₕ(zᵘ)",
       title="The stated general exponent range fails · WJ18–WJ20")
ax.set_ylim(-1e-8,max(ys)*1.6);ax.grid(alpha=.18)
fig.supxlabel("Curves are numerical illustrations of the full formulas; the inequalities and counterexample have exact proofs.\n"
              "Human sources: Jiajie Chen and Thomas Y. Hou, Part II v3, original author TeX lines3002–3072. "
              "No main-theorem failure is established.",fontsize=9)
for ext in ["png","svg"]:fig.savefig(P.with_suffix("."+ext),dpi=165)
plt.close(fig)
meta=dict(at=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),
    proof="CHEN_HOU_WEIGHTED_J2_WORK_20261012.md",locators="WJ1–WJ20",
    original_geometry=dict(B="1/2",h="3/5",actual_exponent="1/2",counterexample_exponent="9/10"),
    source_attribution="Jiajie Chen and Thomas Y. Hou, original Part II v3 numerical supplement lines3002–3072.",
    plotted_curves_are_numerical_illustrations=True,visual_inspection="pending")
P.with_suffix(".json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(figure=str(P.with_suffix(".png")))))
