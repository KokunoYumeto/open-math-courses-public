"""Exact fixed-rectangle certificate and original figure; CC0."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
term=total=F(1)
for n in range(1,25):term*=F(7,n);total+=term
assert total>F(1631,2)
left=F(22,7);pieces=[F(47,20),F(1,4),F(1,7)]
assert left-sum(pieces)==F(2,5)
assert F(47,20)**2>F(11,2)
assert F(1,4)**2*21>1
constant=F(539,2)+F(7,3)
assert constant==F(1631,6) and 283-constant==F(67,6)>0
assert F(329,10)+F(7,30)<34<constant
record={'state':'passed_exact_rational_certificate','L':7,'k':'11/2','z':'strictly greater than3','q':'strictly greater than1','left_lower':str(left),'right_upper':str(sum(pieces)),'positive_determinant_margin':'2/5','constant_upper':str(constant),'positive_constant_margin':'67/6','collision_upper':34,'coverage':'Full independent rational-pair bound with heightboundsH1>2,H2>3/2, positive normalizedheights ofanysize; coprimea>b>=1 includingauxiliaryprimeb1case; everyoddprimeunitp andeveryintegern>=1.'}
(ROOT/'fermat-283-endpoints.json').write_text(json.dumps(record,indent=2)+'\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(11.8,4.0),constrained_layout=True)
ax=axes[0];x=0
for v,color,label in zip(pieces,['#195a83','#68a2b7','#d7a849'],['Height: 47/20','Rounded sides: 1/4','Logarithm: 1/7']):
    ax.barh(0,float(v),left=x,color=color,label=label);x+=float(v)
ax.axvline(float(left),color='#8f3527',ls='--',label='Left side: 22/7')
ax.text(float(sum(pieces)),.4,'Exact gap 2/5',ha='right')
ax.set(xlim=(0,3.5),ylim=(-.5,.8),yticks=[],xlabel='Contribution after division by zL²',title='Fixed determinant comparison')
ax.legend(loc='upper left',fontsize=9)
ax=axes[1];ax.barh(0,float(F(539,2)),color='#195a83',label='kL² = 539/2')
ax.barh(0,float(F(7,3)),left=float(F(539,2)),color='#d7a849',label='Rounding: L/z < 7/3')
ax.axvline(283,color='#8f3527',ls='--',label='Stated coefficient: 283')
ax.text(float(constant),.4,'1631/6 < 283',ha='right')
ax.set(xlim=(0,300),ylim=(-.5,.8),yticks=[],xlabel='Uniform coefficient for N/z',title='Fermat-difference coefficient')
ax.legend(loc='upper left',fontsize=9)
fig.suptitle('L = 7, k = 11/2: both proofs hold for every z > 3 and q > 1',fontsize=13)
fig.savefig(ROOT/'fermat-283-bound.png',dpi=160);plt.close(fig)
print(json.dumps({'state':record['state'],'margin':'2/5','constant_upper':str(constant)}))
