"""Reproduce the exact finite measured-component example in OA-FLOW ED.

Original code, data and diagram: CC0-1.0. Requires matplotlib.
DejaVu font terms are retained in FONT_LICENSE_DEJAVU.txt.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parent
base=[F(1,3),F(2,3)]
conditional=[[F(1,4),F(3,4)],[F(2,5),F(3,5)]]
global_mass=[[b*q for q in row] for b,row in zip(base,conditional)]
density=[[row[1]/row[0],row[0]/row[1]] for row in conditional]
assert sum(base)==1 and all(sum(row)==1 for row in conditional)
assert sum(sum(row) for row in global_mass)==1
assert density==[[F(3),F(1,3)],[F(3,2),F(2,3)]]
assert all(row[0]*row[1]==1 for row in density)
assert all(conditional[j][i]*density[j][i]==conditional[j][1-i]
           for j in range(2) for i in range(2))
def fs(q):return str(q)
data={'license':'CC0-1.0','proof_locator':'OA-FLOW-ED.md#oa-flow.ergdec.example; E1-E5',
      'group':'C2={e,s}, s^2=e','action':'s(y,i)=(y,1-i)',
      'base_points':['a','b'],'base_masses':list(map(fs,base)),
      'conditional_masses':[[fs(q) for q in row] for row in conditional],
      'global_masses':[[fs(q) for q in row] for row in global_mass],
      'pushforward_density_at_i':[[fs(q) for q in row] for row in density],
      'conditional_invariance':[False,False],'conditional_ergodicity':[True,True],
      'unitarity_check':'mu_y(i)*r_s(y,i)=mu_y(1-i)',
      'group_law_check':'r_s(y,0)*r_s(y,1)=1'}
(OUT/'exact-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                    'mathtext.fontset':'dejavusans','svg.fonttype':'path',
                    'svg.hashsalt':'oa-flow-conditional-ergodic-components'})
fig=plt.figure(figsize=(15,10),facecolor='#f7fafc')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ink='#192e3b';muted='#536b7a';blue='#176b9d';green='#177a66';orange='#b65b20'
ax.text(.045,.966,'Ergodic components can have non-invariant probabilities',
        fontsize=23,weight='bold',color=ink,va='top')
ax.text(.045,.906,r'$s(y,i)=(y,1-i)$: a swap inside each invariant fibre',
        fontsize=20,color=muted)
def box(x,y,w,h,fc,ec='#b4c7d2'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008',
                              fc=fc,ec=ec,lw=1.2))
def texfrac(q):
    return str(q.numerator) if q.denominator==1 else r'\frac{'+str(q.numerator)+'}{'+str(q.denominator)+'}'
for j,(x,name,col) in enumerate([(.055,'a',blue),(.535,'b',green)]):
    box(x,.29,.41,.55,'#eef4f6')
    ax.text(x+.025,.799,rf'Base point ${name}$:  $\nu({name})={texfrac(base[j])}$',
            fontsize=21,weight='bold',color=col)
    ax.text(x+.025,.746,'Global point masses',fontsize=15,color=muted)
    for i,cx in enumerate([x+.10,x+.31]):
        ax.text(cx,.689,rf'$\mu({name},{i})={texfrac(global_mass[j][i])}$',
                ha='center',fontsize=21,color=ink)
    ax.plot([x+.025,x+.385],[.652,.652],color='#c7d4dc',lw=1)
    ax.text(x+.025,.612,rf'Conditional probability $\mu_{name}$',fontsize=17,color=col)
    for i,cx in enumerate([x+.10,x+.31]):
        ax.scatter([cx],[.544],s=1800,color=col,alpha=.12,edgecolors=col,linewidths=1.5)
        ax.text(cx,.544,rf'${i}$',ha='center',va='center',fontsize=22,color=col)
        ax.text(cx,.475,rf'${texfrac(conditional[j][i])}$',ha='center',fontsize=25,color=ink)
    ax.add_patch(FancyArrowPatch((x+.137,.544),(x+.273,.544),arrowstyle='<->',
                                mutation_scale=19,color=orange,lw=2))
    ax.text(x+.205,.574,r'$s$',ha='center',color=orange,fontsize=17)
    ax.text(x+.025,.411,r'Pushforward density $r_s(i)=\mu_y(1-i)/\mu_y(i)$',
            fontsize=15,color=muted)
    for i,cx in enumerate([x+.10,x+.31]):
        ax.text(cx,.344,rf'${texfrac(density[j][i])}$',ha='center',fontsize=26,color=orange)
ax.text(.055,.229,'All ratios are positive: each conditional measure class is preserved.',
        fontsize=18,color=green,weight='bold')
ax.text(.055,.179,'Each pair is one orbit: its only invariant subsets are empty or the whole pair.',
        fontsize=17,color=ink)
ax.text(.055,.124,r'Unequal masses: neither $\mu_a$ nor $\mu_b$ is invariant under the swap.',
        fontsize=17,color=ink)
ax.text(.055,.070,r'$|V_y(s)1_y|^2=r_s(y,\cdot)$   and   $r_s(y,0)r_s(y,1)=1$',
        fontsize=19,color=blue)
ax.text(.055,.022,'Exact finite system · OA-FLOW ED · equations (E1)–(E5)',
        fontsize=11,color=muted)
fig.savefig(OUT/'conditional-ergodic-components.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(OUT/'conditional-ergodic-components.svg',facecolor=fig.get_facecolor(),metadata={'Date':None})
plt.close(fig)
print(json.dumps({'exact_fraction_checks':'passed','image_dimensions':[2700,1800]}))
