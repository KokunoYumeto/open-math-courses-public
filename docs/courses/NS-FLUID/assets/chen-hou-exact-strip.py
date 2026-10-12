"""Original physical strip geometry and samples of the proved exact formulas."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import beta,betainc
from scipy.integrate import quad

P=Path(__file__).resolve();a=13/10;b=39/10
kap=beta(5/4,1/4)/(2*np.sqrt(2))
def A(r):
    return np.arcsin(r)-np.arcsin(np.clip(np.sqrt(2)*r/np.sqrt(1+r*r),0,1))/np.sqrt(2)+r*np.sqrt(np.maximum(0,1-r*r))/(1+r*r)
def C(aa,bb):
    r=aa/bb;x=4*r*r/(1+r*r)**2
    return np.sqrt(bb)*A(r)+np.sqrt(aa)/(2*np.sqrt(2))*beta(5/4,1/4)*(1-betainc(1/4,5/4,x))
def fs(v):return quad(lambda w:w*w/(1+w**4),0,v,epsabs=1e-11)[0]
fig,axs=plt.subplots(2,2,figsize=(13,10),layout='constrained')
fig.suptitle('Original K2 strips: exact transport, full costs and physical endpoints\nPhysical width a = 13/10; equations SQ3–SQ25',fontsize=14)
ax=axs[0,0];u=np.linspace(0,a,400)
ax.fill_between(u,0,u*u/b,color='#eac46a',label='Positive residual: 0 < t < u²/b')
ax.fill_between(u,u*u/b,u,color='#86bdc4',label='Positive matched interval')
ax.fill_between(u,u,b,color='#bab5d9',label='Negative matched interval')
ax.plot(u,u,color='#284b63',lw=1.2)
ax.plot(u,u*u/b,color='#986c14',lw=1.2)
uu=3*a/5;tt=2*b/3;partner=uu*uu/tt
ax.plot([uu,uu],[partner,tt],'o',color='#ad3535',ms=4)
ax.annotate('',xy=(uu,partner),xytext=(uu,tt),arrowprops=dict(arrowstyle='->',color='#ad3535',lw=1.7))
ax.text(uu+.055,1.5,'t ↦ u²/t\nu fixed',fontsize=9,color='#8f2525')
ax.set(xlim=(0,a+.28),ylim=(0,b+.15),xlabel='Original first coordinate u',ylabel='Original height t',title='Signed partner and the retained residual · SQ3–SQ6')
ax.set_aspect('equal',adjustable='box');ax.legend(fontsize=8,loc='upper left',bbox_to_anchor=(1,1))

ax=axs[0,1];bb=np.linspace(a,6*a,181)
cost=C(a,bb);source=np.array([np.sqrt(a)*(fs(np.sqrt(v/a))-fs(1)+np.pi/2-np.pi/(2*np.sqrt(2))) for v in bb])
ax.plot(bb,cost,color='#187786',label='Exact paired cost C(a,b)')
ax.plot(bb,source,'--',color='#b45339',label='Source upper bound, corrected sign')
ax.axhline(np.sqrt(a)*kap,color='#62666b',ls=':',label='Full infinite cost √a κ')
ax.set(xlabel='Actual upper height b',ylabel='Original paired cost',title='Strict coefficient improvement for b > a · SQ9–SQ18')
ax.legend(fontsize=8);ax.grid(alpha=.2)

ax=axs[1,0];rr=np.linspace(1,16,201);xx=4*rr*rr/(rr*rr+1)**2
tail=beta(1/4,5/4)*betainc(1/4,5/4,xx)/(2*np.sqrt(2))
ax.plot(rr,tail,color='#187786',label='Exact complete tail E(R)')
ax.plot(rr,2/np.sqrt(rr),'--',color='#b45339',label='Source bound 2/√R')
ax.set(xlabel='Original ratio cutoff R',ylabel='Full tail integral',title='No infinite contribution discarded · SQ19')
ax.legend(fontsize=8);ax.grid(alpha=.2)

ax=axs[1,1];delta=a/5;mm=np.linspace(a,a+1.7*delta,201);ee=np.maximum(mm,a+delta)
strips=4*kap*(np.sqrt(ee+a)-np.sqrt(mm+a)+np.sqrt(ee-a)-np.sqrt(mm-a))/(np.pi*np.sqrt(2*a))
ax.plot(mm,strips,color='#187786')
ax.axvline(a+delta,color='#62666b',ls=':')
ax.text(a+delta+.014,.16,'Both strip widths are zero\nfor M ≥ a + δ',fontsize=9)
ax.set(xlabel='Physical midpoint M',ylabel='Two strip terms / (π√(2a))',title='Exact exterior strip contribution; δ = a/5 · SQ23')
ax.text(.40,.95,'The remaining Cvert(a,E) term\nis retained in the proof; not plotted here.',transform=ax.transAxes,va='top',fontsize=9)
ax.grid(alpha=.2)
fig.supxlabel('Curves are numerical samples of proved formulas. Rational certification of κ uses SQ24–SQ25, not these plots.',fontsize=10)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=175)
plt.close(fig)
meta={'at':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
      'proof':'CHEN_HOU_EXACT_STRIP_WORK_20261011.md','locators':'SQ3–SQ25',
      'original_parameters':{'a':'13/10','geometry_b':'39/10','exterior_delta':'a/5'},
      'scope':'Actual-coordinate geometry and samples of complete exact cost formulas; separate rational coefficient certificate.',
      'visual_inspection':'pending'}
P.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':str(P.with_suffix('.png'))}))
