"""Reproduce the opposite pole, tensor evaluations and ordinary period diagram."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,FancyArrowPatch,FancyBboxPatch
root=Path(__file__).resolve().parent;out=root if root.name=='assets'else root/'assets';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'OI-ordered-periods'})
fig,axes=plt.subplots(2,2,figsize=(14,9))
fig.suptitle('The opposite incidence kernel and its ordered periods',fontsize=19,y=.995)
ax=axes[0,0];ax.axis('off');ax.set_title('A. Actual whole-ring maps and algebraic evaluations',fontsize=12)
for x,label in [(.07,r'$B_X$'),(.7,r'$B_Y$')]:
 ax.add_patch(FancyBboxPatch((x,.55),.2,.2,boxstyle='round,pad=.02',facecolor='#e4eff3',edgecolor='#26678a'))
 ax.text(x+.1,.65,label,ha='center',va='center',fontsize=17)
ax.add_patch(FancyArrowPatch((.68,.73),(.29,.73),arrowstyle='->',mutation_scale=15,color='#26678a',lw=1.6))
ax.add_patch(FancyArrowPatch((.29,.57),(.68,.57),arrowstyle='->',mutation_scale=15,color='#b65f26',lw=1.6))
ax.text(.48,.82,r'$\phi=\mathcal{L}_0$',ha='center',fontsize=13)
ax.text(.48,.42,r'$\psi=J\mathcal{L}_d=\phi^{-1}$',ha='center',fontsize=13)
ax.text(.48,.24,r'$\mathrm{ev}_X(e^+\otimes e^-)=1$',ha='center',fontsize=13)
ax.text(.48,.09,r'$\mathrm{ev}_Y(e^-\otimes e^+)=1$'+'\nOI.7 and OI.11–OI.15',ha='center',fontsize=12)
ax=axes[0,1];ax.set_title('B. Dimension and the opposite pole',fontsize=12)
d=list(range(5));ax.plot(d,[1]*5,'o-',label=r'Forward: $f^{-1}\eta_Y$',color='#26678a')
ax.plot(d,[x+1 for x in d],'s-',label=r'Opposite: $g^{-(d+1)}\eta_X$',color='#b65f26')
ax.set(xlabel='Spatial dimension d',ylabel='Pole order',xticks=d,yticks=list(range(1,6)),ylim=(.6,5.5))
ax.legend(loc='upper left',fontsize=10)
ax.text(.5,.12,r'$N=d+1$; d = 0 is included.'+'\n'+r'Inverse time shift: $+d\sigma^{-1}$.'+'\nOI.6–OI.8.',
 transform=ax.transAxes,fontsize=10)
ax=axes[1,0];ax.set_title('C. Both positively oriented normal circles',fontsize=12)
for yy,orders,formula in [(1.1,(1,3),r'$[f(A-f)^3]^{-1}\,df$'),(-1.1,(3,1),r'$[g^3(A-g)]^{-1}\,dg$')]:
 ax.plot([-1,4],[yy,yy],color='#aebbc4',lw=1)
 ax.add_patch(Circle((0,yy),.45,fill=False,color='#26678a',lw=1.5))
 ax.add_patch(FancyArrowPatch((.45,yy),(.42,yy+.17),arrowstyle='->',mutation_scale=12,color='#26678a'))
 ax.plot([0,3],[yy,yy],'x',color='#b65f26',ms=8)
 ax.text(0,yy-.7,f'0: pole order {orders[0]}',ha='center',fontsize=10)
 ax.text(3,yy-.7,f'A = 3: order {orders[1]}',ha='center',fontsize=10)
 ax.text(1.65,yy+.25,formula,ha='center',fontsize=13)
ax.text(1.45,2.15,r'$\frac{1}{2\pi i}\int = A^{-3}=\frac{1}{27}$ in both rows.',ha='center',fontsize=13)
ax.set(xlim=(-1.3,4),ylim=(-2.3,2.9),aspect='equal');ax.axis('off')
ax=axes[1,1];ax.set_title('D. A spatial period and its denominator bound',fontsize=12)
data=[]
for k in range(-80,81):
 b=F(k,40);period=F(2,1)/(9-b*b);bound=F(2,1)/(3-abs(b))**2
 data.append({'b':str(b),'period':str(period),'bound':str(bound)})
ax.plot([float(F(x['b']))for x in data],[float(F(x['period']))for x in data],color='#26678a',label=r'$F_1(3,b)=2/(9-b^2)$')
ax.plot([float(F(x['b']))for x in data],[float(F(x['bound']))for x in data],color='#b65f26',ls='--',label=r'$2/(3-|b|)^2$')
ax.plot([0],[2/9],'o',color='#26678a')
ax.set_yscale('log');ax.set(xlabel='Real spatial parameter b; epsilon = 1',ylabel='Ordinary compact period / bound',xlim=(-2.1,2.1))
ax.legend(fontsize=10,loc='upper center')
ax.annotate(r'$F_1(3,0)=2/9$',xy=(0,2/9),xytext=(-.8,1.2),fontsize=11,
 arrowprops={'arrowstyle':'->','color':'#26678a'})
for ax in [axes[0,1],axes[1,1]]:ax.spines[['top','right']].set_visible(False)
fig.text(.5,.014,'A: balanced bimodule maps. C–D: ordinary compact periods. These maps do not by themselves identify the analytic relative cup/excision/proper-trace products.',
 ha='center',fontsize=10)
fig.tight_layout(rect=(0,.055,1,.96))
fig.savefig(out/'opposite-incidence-ordered-periods.png',dpi=180,facecolor='white')
fig.savefig(out/'opposite-incidence-ordered-periods.svg',facecolor='white',metadata={'Date':None})
record={'dimension_window':d,'forward_pole_orders':[1]*5,'opposite_pole_orders':[n+1 for n in d],
 'normal_residue_sample':{'N':3,'A':'3','residue':'1/27','pole_orders':[[1,3],[3,1]],'positive_orientation':True,
 'circle_picture':'Schematic: the displayed circle surrounds only zero; the proof permits every radius 0<r<|A|.'},
 'spatial_period_sample':{'d':1,'epsilon':'1','a':'3','exact_rational_values':data},
 'proof_locators':['OI.6–OI.15','OI.18–OI.20','OI.21–OI.25'],
 'analytic_inverse_product_claimed':False,'free_context':'https://arxiv.org/abs/2102.08861v2'}
(out/'opposite-incidence-ordered-periods-exact-data.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print('Wrote 2520x1620 PNG, deterministic SVG and exact rational data.')
