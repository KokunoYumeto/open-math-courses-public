"""Exact two-radius floor mechanism and all-rank fractional gaps. CC0."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fixed_fractional_boost_bounds import certificate

data=certificate();q=3;U=F(1001);xi=F(24,25)
small=(xi*U/q-1)//2;large=(xi*U-1)//2
assert small==159 and large==479 and q*small<=large
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(left,right)=plt.subplots(1,2,figsize=(14,5.9),gridspec_kw={'width_ratios':[1.25,1]})
fig.suptitle('More integer zeros supply the full fractional field cost',fontsize=17,fontweight='bold')
levels=[(2,25,'Original interval: radius 25; 51 nodes'),(1,small,'First extension: radius 159; 319 nodes'),(0,large,'Second extension: radius 479; 959 nodes')]
colors=['#879aaf','#267ca1','#c37d2d']
for (y,r,label),color in zip(levels,colors):
    left.plot([-r,r],[y,y],color=color,lw=6,solid_capstyle='butt')
    left.scatter([-r,r],[y,y],color=color,s=35)
    left.text(0,y+.22,label,ha='center',fontsize=11)
left.set(xlim=(-535,535),ylim=(-.75,2.75),xticks=[-479,-159,0,159,479],yticks=[])
left.set_title('Exact floor illustration: q = 3; U/θ = 1001; ξ = 24/25',fontsize=11)
left.text(0,-.5,'Same selected order O at each interval; 3 × 159 = 477 ≤ 479.',ha='center',fontsize=10)
for side in ['top','left','right']:left.spines[side].set_visible(False)
table=data['table'];positions=list(range(len(table)))
gaps=[r['fractional_strict_margin_per_million']/1000000 for r in table]
right.barh(positions,gaps,color='#267ca1')
for pos,val in zip(positions,gaps):right.text(val+.018,pos,f'{val:.6f}',va='center',fontsize=10)
right.set(yticks=positions,yticklabels=[x['case'] for x in table],xlim=(0,.97),xlabel=r'Strict fractional gap $P_3$ after division by $q^r$')
right.invert_yaxis();right.set_title('All original cases; every rank',fontsize=12)
for side in ['top','right']:right.spines[side].set_visible(False)
fig.text(.5,.025,'Integer comparisons remain in K. The fractional comparison retains the full qʳ factor.\nThe two parity recurrences prove the infinite rank range; no equal-prime valuation assertion is used.',ha='center',fontsize=10)
fig.subplots_adjust(left=.045,right=.98,top=.76,bottom=.25,wspace=.3)
out=Path(__file__).resolve().parent/'fixed-fractional-boost-profile.png';fig.savefig(out,dpi=155,bbox_inches='tight');plt.close(fig)
print(json.dumps({'figure':str(out),'radii':[int(small),int(large)],'nodes':[int(2*small+1),int(2*large+1)]}))
