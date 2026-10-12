"""Original full-cost domains and the certified physical coefficient."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve();S=P.parent.parent/'state'
c=json.loads((S/'CHEN_HOU_VERTICAL_VX_CERTIFICATE_128.json').read_text(encoding='utf-8'))
d=json.loads((S/'CHEN_HOU_VERTICAL_FULL_COST_DIAGNOSTIC.json').read_text(encoding='utf-8'))['rows'][-1]
num=lambda v:float(Fraction(v))
fig,axs=plt.subplots(2,2,figsize=(13,10),layout='constrained')
fig.suptitle('The complete original vertical vₓ estimate\nOriginal source radius a = 1 · full physical receiving proof VN1–VN22',fontsize=14)
def sigma(s):return abs(s*s-1)/np.sqrt(s*s+1+2*np.sqrt(s**4-s*s+1))
ax=axs[0,0];s=np.linspace(0,1,501);sig=sigma(s);b=np.sqrt((1-s*s)/3)
ax.fill_between(s,0,sig,color='#82bac5',label='Paired negative branch')
ax.fill_between(s,b,1,color='#e7c97c',label='Unpaired positive tail, continuing to infinity')
ax.plot(s,sig,color='#185c70');ax.plot(s,b,color='#96671a')
ax.set(xlim=(0,1),ylim=(0,1),xlabel='Original displacement s',ylabel='Original height t',title='Complete inner paired and residual costs · VN2, VN7')
ax.legend(fontsize=8,loc='upper right');ax.text(.1,.34,'Both original shifted kernels are retained',fontsize=9)
ax=axs[0,1];s=np.linspace(1,4,401)
ax.fill_between(s,sigma(s),4,color='#bbb3d8',label='Positive vertical-partner branch')
ax.plot(s,sigma(s),color='#615088')
ss=2.;tt=2.;lo=0.;hi=tt
for _ in range(70):
 m=(lo+hi)/2
 if tt*m*(m*m+tt*m+tt*tt+2*ss*ss+2)<(ss*ss-1)**2:lo=m
 else:hi=m
partner=(lo+hi)/2
ax.annotate('',xy=(ss,partner),xytext=(ss,tt),arrowprops=dict(arrowstyle='->',color='#a33737',lw=2))
ax.scatter([ss,ss],[partner,tt],color='#a33737',s=18)
ax.text(ss+.13,1.15,'t ↦ V₁,ₛ(t)\ns is fixed',fontsize=10,color='#a33737')
ax.text(1.15,3.55,'Both s and t continue to infinity',fontsize=9)
ax.set(xlim=(1,4),ylim=(0,4),xlabel='Original displacement s',ylabel='Original height t',title='Full exterior and exact cubic partner · VN8–VN10')
ax=axs[1,0];labels=['Inner paired','Inner residual','Entire exterior'];pos=np.arange(3)
samples=[d['inner_paired'],d['inner_residual'],d['exterior']]
upper=[num(c['full_paired_upper']),num(c['full_residual_upper']),num(c['full_exterior_upper'])]
ax.bar(pos-.16,samples,width=.3,color='#96afb9',label='Numerical sample')
ax.bar(pos+.16,upper,width=.3,color='#187786',label='Proved upper enclosure')
ax.set_xticks(pos,labels);ax.set(ylabel='Complete original cost',title='All singular and infinite endpoints included · VN17–VN21')
ax.legend(fontsize=9);ax.grid(axis='y',alpha=.2)
ax=axs[1,1]
values=[d['vx_vertical_coefficient'],num(c['complete_vx_coefficient_upper']),2.59,num('1462528955430077/562949953421312'),2.60]
names=['Numerical sample','Certified upper endpoint','Proved rational bound','Original saved lower endpoint','Paper’s printed constant']
for i,(name,val) in enumerate(zip(names,values)):
 ax.plot(val,i,'o',color='#187786' if i in [1,2] else '#777e88')
 ax.text(val+.0003,i,'< 2.588768' if i==1 else f'{val:.6f}',va='center',fontsize=8)
ax.set_yticks(range(5),names,fontsize=9);ax.invert_yaxis()
ax.set(xlim=(2.582,2.605),xlabel='Full coefficient, including τ/2',title='The saved vertical vₓ bound remains valid · VN22')
ax.grid(axis='x',alpha=.2)
fig.supxlabel('Geometry panels show finite windows of the full domains. Only vₓ is certified here; uᵧ and full stability remain under audit.',fontsize=10)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=175)
plt.close(fig)
meta=dict(at=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),
 proof='CHEN_HOU_VERTICAL_FULL_COST_WORK_20261012.md',locators='VN1–VN22',original_a='1',
 source_attribution='Jiajie Chen and Thomas Y. Hou, original numerical supplement to Part II v3, vertical transport section; all source and proof links in the accompanying note.',
 scope='Complete original costs and certified scalar coefficient; numerical samples and finite plotting windows are explicitly identified.',visual_inspection='pending')
P.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(figure=str(P.with_suffix('.png')))))
