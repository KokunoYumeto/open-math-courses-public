"""Actual Rees specializations, symbol subquotient and an exact real cotangent section."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
r=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'GL-DMOD-GP-20261021','font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(17,10),facecolor='#f7f9fc')
ax=fig.add_axes([.02,.10,.59,.85]);ax.set_axis_off()
blue,green,orange='#285ca6','#087c83','#b36a14'
def box(x,y,w,h,title,sub):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',fc='white',ec=blue,lw=1.3))
 ax.text(x+w/2,y+h*.65,title,ha='center',va='center',color=blue,fontsize=17)
 ax.text(x+w/2,y+h*.23,sub,ha='center',va='center',fontsize=11)
ax.text(.5,1,'Actual Rees and cotangent comparisons',ha='center',fontsize=20,weight='bold')
box(.12,.75,.76,.13,'Derived Rees image C','Nonflat coherent coefficients; supported strict finite segment. GP.14–GP.22')
box(.02,.46,.40,.14,r'$h=1:\quad f_+M$','Actual right operator action. GP.23, GP.28')
box(.55,.46,.42,.14,r'$h=0:\quad Rv_*L\rho^*G$','Analytic parameter comparison. GP.5, GP.27')
ax.annotate('',(.22,.62),(.36,.74),arrowprops={'arrowstyle':'->','color':green,'lw':2})
ax.annotate('',(.76,.62),(.65,.74),arrowprops={'arrowstyle':'->','color':green,'lw':2})
box(.12,.13,.76,.20,'Actual output symbol is a subquotient',
 'Keep derived torsion; remove uniform h-power torsion only after specialization.')
ax.text(.5,.055,'GP.29: coherent good pieces and characteristic containment',ha='center',color=green,fontsize=14)
ax.annotate('',(.29,.34),(.22,.44),arrowprops={'arrowstyle':'-','linestyle':'--','color':green,'lw':1.5})
ax.annotate('',(.70,.34),(.76,.44),arrowprops={'arrowstyle':'-','linestyle':'--','color':green,'lw':1.5})

plot=fig.add_axes([.69,.37,.27,.42]);plot.set_xlim(-2,2);plot.set_ylim(-2,2);plot.set_aspect('equal')
plot.spines[['top','right']].set_visible(False)
plot.spines['left'].set_position('zero');plot.spines['bottom'].set_position('zero')
plot.set_xticks([-2,-1,1,2]);plot.set_yticks([-2,-1,1,2]);plot.grid(alpha=.15)
plot.plot([-2,2],[0,0],color=blue,lw=5,zorder=3)
plot.plot([0,0],[-2,2],color=orange,lw=5,zorder=4)
plot.text(1.17,.19,'zero section',color=blue,fontsize=11)
plot.text(.15,1.55,'critical fibre',color=orange,fontsize=11)
plot.set_title(r'$y=x^2:\quad B=\{\eta=0\}\cup\{y=0\}$',fontsize=17,pad=22)
plot.text(1.92,-.40,r'$\operatorname{Re}y$',ha='right',fontsize=13)
plot.text(.10,1.86,r'$\operatorname{Re}\eta$',ha='left',fontsize=13)
fig.text(.825,.265,r'Exact section $\operatorname{Im}y=\operatorname{Im}\eta=0$',ha='center',fontsize=14)
fig.text(.825,.22,'Displayed window: [−2, 2] in both real coordinates.',ha='center',fontsize=11)
fig.text(.825,.15,'Each full complex component has dimension 1.',ha='center',fontsize=13,color=green)
fig.text(.825,.105,'This is the cotangent candidate; equality with',ha='center',fontsize=11)
fig.text(.825,.075,'every operator image characteristic set is not asserted.',ha='center',fontsize=11)
fig.savefig(r/'general-analytic-characteristic.png',dpi=180)
fig.savefig(r/'general-analytic-characteristic.svg',metadata={'Date':None})
plt.close(fig)
samples=[]
for n in range(4):
 for m in range(4):
  s=3*n+2*m+2
  samples.append({'n':n,'m':m,'s':s,'Rees_cone':[-n-s-1,2*n-s-1],
   'zero_Rees_cone':[-n-s-2,2*n-s-1],'analytic_cone':[-n-s-1,2*(n+m)-s-1],
   'lowest_comparison_degree':-n-1})
data={'proofs':['GP.5','GP.14--GP.29','GP.30--GP.34'],
 'specializations':{'h=1':'actual right D image','h=0':'derived symbol candidate with exact analytic extension'},
 'symbol_relation':'quotient of a submodule; derived h-torsion is retained until both specializations',
 'general_segment':'s=3n+2m+2','finite_interval_samples':samples,
 'curve_example':{'e':2,'f':'y=x^2','cotangent_map':'xi=2*x*eta','reduced_image':'{eta=0} union {y=0}',
  'displayed_real_section':{'Im y':0,'Im eta':0,'Re y':[-2,2],'Re eta':[-2,2]},
  'complex_component_dimensions':[1,1],'candidate_not_universal_equality':True},
 'finite_samples_are_general_proof':False}
(r/'general-analytic-characteristic-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
