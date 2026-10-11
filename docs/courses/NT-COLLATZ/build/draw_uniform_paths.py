"""Finite actual-path illustration; the exact bounds are in check_uniform_paths.py."""
from pathlib import Path
from fractions import Fraction
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"svg.fonttype":"none","font.family":"DejaVu Sans"})
n=1048587;xs=[n];raw=[n];P=Fraction(1);s=0
while xs[-1]>1024:
    x=xs[-1]
    if x%2:
        raw.append(3*x+1);P*=Fraction(3*x,3*x+1);s+=1
    y=(3*x+1)//2 if x%2 else x//2
    xs.append(y);raw.append(y)
for j,x in enumerate(xs):
    assert 3**j*n*n<=81*4**j*x*x and 4**j*x*x<=81*3**j*n*n
assert P>=Fraction(999,1000) and len(xs)==38 and len(raw)==55
d=math.log(2)-math.log(3)/2;E=math.log(9);a=math.log(1000/999)
B=(E+a)/math.log(3);radius=E+2*d*B/3+math.log(2)-2*d/3
fig,axes=plt.subplots(2,1,figsize=(7.0,7.0))
z=8192
for ax,values,slope,rad,title in [
 (axes[0],xs,d,E,"Shortcut steps"),
 (axes[1],raw,2*d/3,radius,"Ordinary steps, including inserted states")]:
    times=list(range(len(values)));center=[math.log(n)-slope*j for j in times]
    ax.fill_between(times,[v-rad for v in center],[v+rad for v in center],
                    color="#e9f2f7",label="proved finite error band")
    ax.plot(times,center,linestyle="--",color="#577f9a",linewidth=1.2,label="centered drift")
    ax.plot(times,[math.log(x) for x in values],color="#165767",marker=".",markersize=4,label="actual log value")
    first=next(j for j,x in enumerate(values) if x<=z)
    ax.axhline(math.log(z),color="#935528",linestyle=":",linewidth=1)
    ax.scatter([first],[math.log(values[first])],color="#935528",s=34,zorder=4)
    ax.annotate("first value ≤ 8192\nat time "+str(first),
      xy=(first,math.log(values[first])),xytext=(first+2,math.log(z)+1.15),
      fontsize=9,arrowprops={"arrowstyle":"->","color":"#935528"},color="#74431f")
    ax.set(title=title,xlabel="step number",ylabel="natural logarithm of value")
    ax.set_xlim(0,len(values)-1);ax.grid(alpha=.15)
axes[0].legend(fontsize=8,loc="upper right")
fig.suptitle("One finite path, two clocks, the same first crossing",fontsize=13)
fig.tight_layout(rect=(0,0,1,.95),h_pad=2.0)
fig.savefig(Path(__file__).resolve().parents[1]/"figures/uniform-paths.svg",bbox_inches="tight")
plt.close(fig)

