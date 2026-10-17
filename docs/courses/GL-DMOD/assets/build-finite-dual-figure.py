"""Exact degree-window illustration for the conditional algebraic proof FD.3."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

root=Path(__file__).resolve().parent
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path)
args=parser.parse_args()
out=args.output_dir.resolve() if args.output_dir else root
out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.hashsalt':'finite-dual-A4-r2-c3','mathtext.fontset':'dejavusans'})
r,c=2,3
cols=list(range(r+1)); rows=list(range(c,c+3))
fig=plt.figure(figsize=(14,7),dpi=180,facecolor='#fbfbfd')
ax=fig.add_axes([.065,.22,.49,.62])
ax.set_xlim(-.65,3.25);ax.set_ylim(2.42,6.15);ax.axis('off')
data=[]
for q in rows:
    for p in cols:
        total=p+q;shifted=total-r
        face='#d9edfb' if shifted==c-r else '#eaf3f9'
        ax.add_patch(Rectangle((p-.44,q-.38),.88,.76,facecolor=face,edgecolor='#294c68',linewidth=1.3))
        ax.text(p,q+.10,rf'$p+q={total}$',ha='center',va='center',fontsize=15)
        ax.text(p,q-.15,rf'$p+q-r={shifted}$',ha='center',va='center',fontsize=12,color='#294c68')
        data.append({'p':p,'q':q,'total_degree':total,'shifted_degree':shifted})
    ax.text(-.56,q,rf'$q={q}$',ha='right',va='center',fontsize=14)
for p in cols:
    ax.text(p,2.5,rf'$p={p}$',ha='center',va='center',fontsize=14)
    ax.annotate('',xy=(p,5.9),xytext=(p,5.46),arrowprops={'arrowstyle':'->','color':'#294c68','linewidth':1.8})
ax.text(1,6.03,r'Further rows $q\geq6$',ha='center',va='center',fontsize=14)
fig.text(.31,.175,r'All resolution columns $0\leq p\leq r$',ha='center',va='center',fontsize=13,color='#294c68')
fig.text(.065,.93,'Finite Hom degrees after the [r] shift',fontsize=22,weight='bold',color='#173b55')
fig.text(.065,.875,r'Illustration of proof FD.3 with $r=2$, $c=3$; the coefficient rows begin at $q=c$.',fontsize=14)
fig.text(.62,.735,r'$\mathrm{Hom}(R^{-p},C^q)$',fontsize=22,color='#173b55')
fig.text(.62,.645,r'Total degree: $p+q\geq c$',fontsize=17)
fig.text(.62,.565,r'After $[r]$: $p+q-r\geq c-r$',fontsize=17)
fig.text(.62,.47,r'Here: $c-r=1>0$',fontsize=18,weight='bold',color='#173b55')
fig.text(.62,.385,'Degree zero has no terms.\nThe algebraic degree bound is conditional\non the stated coefficient-depth premise.',fontsize=14,linespacing=1.6,va='top')
fig.text(.065,.08,'This is a complex-degree schematic, not a geometric model. The vertical window is finite;\nthe arrows retain all higher coefficient rows. Proof locator: Section 5.50, FD.3.',fontsize=12,linespacing=1.5,va='top')
fig.savefig(out/'finite-dual-degree-bound.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(out/'finite-dual-degree-bound.svg',facecolor=fig.get_facecolor(),metadata={'Date':None,'Creator':'Open mathematics course proof diagram'})
plt.close(fig)
payload={'proof_locator':'Section 5.50, FD.3','kind':'complex-degree schematic','r':r,'c':c,'p_columns':cols,'q_rows_shown':rows,'higher_q_rows_retained':'q >= 6','general_hypothesis':'H^q(C)=0 for q<c, R in degrees -r,...,0','general_bound':'p+q-r >= c-r','cells':data,'figure_alone_proves_analytic_coefficient_depth':False,'I23_proved':False}
(out/'finite-dual-degree-bound-data.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
print('Finite-dual diagram and exact degree data generated.')
