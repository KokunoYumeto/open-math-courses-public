"""Reproducible numerical slices of the exact OC.2 exhaustion. CC0."""
from pathlib import Path
import json, math, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'ordinary-puncture-OC2'})
def psi(r): return r*r-math.log(1-r*r)+1/(r*r)
def stationary_polynomial(s): return -s**3+2*s*s+s-1
def bisect(fn,lo,hi):
    flo=fn(lo)
    for _ in range(100):
        mid=(lo+hi)/2
        if fn(mid)*flo<=0:hi=mid
        else:lo=mid;flo=fn(lo)
    return (lo+hi)/2
s0=bisect(stationary_polynomial,0.01,0.99);r0=math.sqrt(s0)
levels=[]
for c in [4,6,9]:
    a=bisect(lambda r:psi(r)-c,0.02,r0)
    b=bisect(lambda r:psi(r)-c,r0,1-1e-12)
    levels.append({'level':c,'inner_radius_numerical':a,'outer_radius_numerical':b})
data={'exact_domain':'0 < |w| < 1','exact_exhaustion':'psi(w)=|w|^2-log(1-|w|^2)+|w|^-2',
 'exact_Levi_coefficient':'1+(1-|w|^2)^(-2)+|w|^(-4)',
 'stationary_squared_radius_polynomial':'-s^3+2*s^2+s-1=0',
 'unique_stationary_radius_numerical':r0,'minimum_numerical':psi(r0),
 'method':'100 bisection steps on each monotone radial branch; numerical drawing only',
 'levels':levels,'proof_locator':'OC.1–OC.2, equations OC.2–OC.4',
 'scope':'The N=1 example with unit base radii and base coordinates fixed at zero. Additional punctured normal coordinates in a higher-dimensional slice must instead be fixed at nonzero constants, shifting the exhaustion by an additive constant. The full product exhaustion is the sum in OC.2.'}
(ROOT/'puncture-exhaustion-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
fig,(ax,ay)=plt.subplots(1,2,figsize=(12.8,6.4),gridspec_kw={'width_ratios':[1.2,1]})
fig.patch.set_facecolor('#f5f8fc')
r=np.linspace(0.12,1-1e-8,2000)
ax.plot(r,[psi(float(x)) for x in r],color='#087e8b',lw=2.3)
colors=['#087e8b','#496fbe','#b04785']
for row,color in zip(levels,colors):
    c,a,b=row['level'],row['inner_radius_numerical'],row['outer_radius_numerical']
    ax.hlines(c,a,b,color=color,lw=1.8)
    ax.scatter([a,b],[c,c],color=color,s=28,zorder=3)
ax.set(xlim=(0,1.015),ylim=(0,12),xlabel=r'$r=|w|$',ylabel=r'$\psi(r)$',title='Divergence at both excluded boundaries')
ax.axvline(1,color='#53616d',ls='--',lw=1)
ax.annotate(r'$\psi\to+\infty$',xy=(0.2,11.8),xytext=(0.045,10.3),arrowprops={'arrowstyle':'->','color':'#53616d'})
ax.annotate(r'$\psi\to+\infty$',xy=(0.999,11.8),xytext=(0.73,10.3),arrowprops={'arrowstyle':'->','color':'#53616d'})
ax.grid(alpha=0.15)
for row,color in reversed(list(zip(levels,colors))):
    a,b=row['inner_radius_numerical'],row['outer_radius_numerical']
    ay.add_patch(Wedge((0,0),b,0,360,width=b-a,facecolor=color,edgecolor='none',alpha=0.15))
    for rad in [a,b]:ay.add_patch(Circle((0,0),rad,fill=False,color=color,lw=1.4))
    ay.plot([],[],color=color,label=f"level {row['level']}: radii {a:.6f}, {b:.6f}")
ay.add_patch(Circle((0,0),1,fill=False,color='#53616d',ls='--',lw=1.2))
ay.plot(0,0,'x',color='#a62e56',ms=8,mew=2)
ay.annotate('excluded puncture',xy=(0,0),xytext=(0.11,-0.13),fontsize=9)
ay.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15),aspect='equal',xlabel=r'$\operatorname{Re}w$',ylabel=r'$\operatorname{Im}w$',title=r'Compact sublevels $\{\psi\leq c\}$')
ay.legend(loc='upper center',bbox_to_anchor=(0.5,-0.15),fontsize=9,frameon=False)
fig.suptitle('Ordinary puncture cohomology: an explicit strictly plurisubharmonic exhaustion',fontsize=15,fontweight='bold',y=0.97)
fig.text(0.5,0.89,r'$\psi(w)=|w|^2-\log(1-|w|^2)+|w|^{-2},\quad 0<|w|<1,\qquad \partial_w\partial_{\bar w}\psi=1+(1-|w|^2)^{-2}+|w|^{-4}>0$',ha='center',fontsize=11)
fig.text(0.5,0.015,'Exact function and domains; level radii are numerical bisection samples. Proof: OC.1–OC.2 (OC.2–OC.4).',ha='center',fontsize=9)
fig.subplots_adjust(top=0.82,bottom=0.23,left=0.07,right=0.96,wspace=0.3)
fig.savefig(ROOT/'puncture-exhaustion.png',dpi=200,metadata={'Software':'Matplotlib','Title':'Ordinary puncture exhaustion OC.2'})
fig.savefig(ROOT/'puncture-exhaustion.svg',metadata={'Date':None,'Creator':'Matplotlib','Title':'Ordinary puncture exhaustion OC.2'})
plt.close(fig)
print(json.dumps({'levels':levels,'minimum_numerical':psi(r0),'files':{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['puncture-exhaustion.png','puncture-exhaustion.svg','puncture-exhaustion-data.json']}}))
