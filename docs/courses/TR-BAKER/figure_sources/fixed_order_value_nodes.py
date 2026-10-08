"""Exact illustrative full-node interpolation with values only. CC0.
Proposed10.145. This example illustrates normal interpolation, not a full
choice of the original logarithmic contradiction parameters.
"""
from pathlib import Path
from fractions import Fraction as F
from math import prod
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

nodes=list(range(-2,3));x=F(1,2)
cardinals=[prod((x-t)/F(s-t) for t in nodes if t!=s) for s in nodes]
assert cardinals==[F(3,128),-F(5,32),F(45,64),F(15,32),-F(5,128)]
assert sum(cardinals)==1
value=prod(F(5)*x-5*s for s in nodes)
assert value==F(140625,32)==5**5*F(45,32)
def valuation(a,p):
    n=a.numerator;d=a.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v
assert valuation(value,5)==6 and all(valuation(a,5)>=0 for a in cardinals)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15})
fig,(ax,proof)=plt.subplots(1,2,figsize=(13,5.8),gridspec_kw={'width_ratios':[1.05,1]},layout='constrained')
fig.suptitle('Full integer nodes: one value condition per node',fontsize=20,fontweight='bold')
ink='#20374e';blue='#267ba3';orange='#c47727'
ax.plot([-2,2],[1,1],color='#bbc5d0',lw=2)
ax.scatter(nodes,[1]*5,color=blue,s=90,zorder=3)
ax.scatter([.5],[1],color=orange,s=160,marker='*',zorder=4)
ax.annotate(r'Target $x=1/2\in\mathbb{Z}_5$',xy=(.5,1),xytext=(.6,1.5),ha='center',fontsize=14,
            arrowprops={'arrowstyle':'->','color':orange})
ax.text(0,2.12,r'$p=5,\quad q=2,\quad R=2,\quad N=5,\quad\theta=1$',ha='center',fontsize=15,color=ink)
for s,a in zip(nodes,cardinals):
    ax.text(s,.42,str(a),ha='center',fontsize=12,color=ink)
    ax.text(s,.05,str(valuation(a,5)),ha='center',fontsize=13,color=blue)
ax.text(0,-.33,r'Cardinal values $L_s(1/2)$ and their nonnegative $v_5$',ha='center',fontsize=13,color=ink)
ax.set(xlim=(-2.35,2.35),ylim=(-.65,2.48),yticks=[],xticks=nodes,xlabel='Integer node s; no extra ordinary jet')
ax.set_title('Every full-interval cardinal is integral',fontsize=16,pad=16)
for spine in ['top','left','right']:ax.spines[spine].set_visible(False)
proof.axis('off')
proof.set_title('Exact normal root-polynomial example',fontsize=16,pad=16)
for ypos,text in [(.86,r'$W(Z)=\prod_{s=-2}^{2}(Z-5s)$'),
                  (.62,r'$W(5/2)=5^5\frac{45}{32}=\frac{140625}{32}$'),
                  (.34,r'$v_5(W(5/2))=6\geq5=N\theta$')]:
    proof.text(.5,ypos,text,ha='center',va='center',fontsize=19,color=ink,
               bbox={'boxstyle':'round,pad=.7','facecolor':'#f1f5f8','edgecolor':'#aec1cf'})
proof.text(.5,.04,'The normal quotient supplies Nθ.\nThis is a local precision bound; a global\nzero comparison needs its own field proof.',ha='center',va='center',fontsize=14,color=ink)
target=Path(__file__).with_name('fixed-order-value-nodes.png')
fig.savefig(target,dpi=175,facecolor='white');plt.close(fig)
print(target)
