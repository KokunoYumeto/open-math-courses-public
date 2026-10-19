"""AN01-U099: exact kernel contour and inward imaginary displacement. CC0.
Original figure: GPT-6 Astra (OpenAI), Ultra. Both panels use exact formulas;
the number of plot samples affects drawing resolution, not the proved bounds.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"]="AN01-U099-boundary-geometry"
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle,Polygon
P=Path(__file__).resolve().parent
blue="#164a70";orange="#b85b17";green="#286b50";gray="#637586"
def eta(t):
    out=np.zeros_like(t,dtype=float)
    mask=t>0;out[mask]=np.exp(-1/t[mask])
    return out
def chi(x):
    s=np.abs(x);a=eta(1-s);b=eta(s-.5)
    return a/(a+b)
x=np.linspace(-2,2,1001);cut=chi(x);q=1-.3*cut
assert np.all(q*q<1+x*x)
assert chi(np.array([0.,.5,1.,2.])).tolist()==[1.,1.,0.,0.]
theta=np.array([1.,0.]);y=np.array([.25,.25]);p=y-theta
assert np.dot(p,p)==5/8
fig,axs=plt.subplots(1,2,figsize=(12,5.8),layout="constrained")
fig.patch.set_facecolor("#f8fafc")
for ax in axs:ax.set_facecolor("#f8fafc");ax.tick_params(labelsize=11)
ax=axs[0]
ax.fill_between(x,0,np.sqrt(1+x*x),color="#e2edf3")
ax.plot(x,np.sqrt(1+x*x),color=blue,lw=2,label=r"$q=\sqrt{1+p^2}$: bound in (K2)")
ax.plot(x,np.ones_like(x),"--",color=gray,lw=1.4,label=r"Undeformed height $q=1$")
ax.plot(x,q,color=orange,lw=2.8,label=r"Final height $q=1-\frac{3}{10}\chi(p)$")
ax.scatter([0],[.7],color=orange,zorder=5)
ax.annotate(r"$(0,7/10)$",xy=(0,.7),xytext=(.55,.35),color=orange,
            arrowprops=dict(arrowstyle="->",color=orange),fontsize=12)
ax.set(xlim=(-2,2),ylim=(0,2.45),xlabel="Real kernel coordinate p",ylabel="Imaginary kernel coordinate q")
ax.set_title("Complex kernel plane",loc="left",fontsize=15,color=blue)
ax.legend(loc="upper center",fontsize=10,frameon=False)
ax=axs[1]
ax.add_patch(Circle((0,0),1,facecolor="#e2edf3",edgecolor=blue,lw=2))
ax.add_patch(Polygon([[0,0],[1.18,0],[1.18,1.18],[0,1.18]],facecolor="#dceee3",alpha=.7,edgecolor="none"))
ax.axhline(0,color=gray,lw=.8);ax.axvline(0,color=gray,lw=.8)
ax.scatter([-1,1],[0,0],s=45,color=[orange,blue],zorder=5)
ax.scatter([p[0]],[p[1]],color=green,s=50,zorder=5)
ax.annotate("",xy=p,xytext=(-1,0),arrowprops=dict(arrowstyle="-|>",color=green,lw=2.5))
ax.text(-1.14,-.18,r"$-\theta$",color=orange,fontsize=14)
ax.text(.92,-.18,r"$\theta$",color=blue,fontsize=14)
ax.annotate(r"$y-\theta=(-3/4,1/4)$",xy=p,xytext=(-1.12,.77),
            arrowprops=dict(arrowstyle="->",color=green),fontsize=12,color=green)
ax.text(.12,.86,r"$\Gamma$: axes excluded",fontsize=11,color=green)
ax.text(.12,.62,r"$y=(1/4,1/4)$",fontsize=12,color=green)
ax.text(-.85,-.7,r"$|y-\theta|^2=5/8<1$",fontsize=13,color=blue)
ax.set(xlim=(-1.25,1.25),ylim=(-1.1,1.2),aspect="equal",
       xlabel="First imaginary coordinate",ylabel="Second imaginary coordinate")
ax.set_title("Imaginary parameter plane",loc="left",fontsize=15,color=blue)
for ext in ["png","svg"]:
    fig.savefig(P/("growth-free-boundary-geometry."+ext),dpi=180,
        metadata={"Creator":"GPT-6 Astra (OpenAI), Ultra; CC0","Date":None}
        if ext=="svg" else {"Author":"GPT-6 Astra (OpenAI), Ultra","License":"CC0"})
plt.close(fig)
svg=P/"growth-free-boundary-geometry.svg"
svg.write_text("\n".join(t.rstrip() for t in svg.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8",newline="\n")
