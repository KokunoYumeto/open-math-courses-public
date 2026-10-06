"""Exact U036 circle fixed points, tangent derivatives and full trace factors.

Written and dedicated to the public domain by Codex, October 2026 (CC0).
Complete programme proofs: EC30--EC36 and LC18, with unit circle metrics.
"""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
                     'svg.hashsalt':'an03-u036-fixed-points-264'})
configurations=[(3,['0',r'\pi']),(0,['0']),(-2,['0',r'2\pi/3',r'4\pi/3'])]
fig=plt.figure(figsize=(16,10),facecolor='white')
rows=[]
for index,(k,angle_labels) in enumerate(configurations):
    ax=fig.add_axes([.035+index*.325,.47,.30,.39])
    ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-1.70,1.70),ylim=(-1.65,1.65))
    t=np.linspace(0,2*math.pi,721)
    ax.plot(np.cos(t),np.sin(t),color='#576e85',linewidth=2.2)
    ax.annotate('',xy=(math.cos(.63),math.sin(.63)),
                xytext=(math.cos(.43),math.sin(.43)),
                arrowprops={'arrowstyle':'->','color':'#576e85','lw':2})
    count=abs(k-1); determinant=1-k;sign=1 if determinant>0 else -1
    colour='#28704b' if sign>0 else '#a33c48'
    positions=[]
    for j,label in enumerate(angle_labels):
        angle=2*math.pi*j/count
        point=np.array([math.cos(angle),math.sin(angle)])
        ax.scatter([point[0]],[point[1]],s=110,color=colour,zorder=5)
        ax.text(*(1.29*point),f'${label}$',ha='center',va='center',fontsize=18)
        positions.append({'angle_exact':f'2*pi*{j}/{count}',
                          'coordinate_formula':[f'cos(2*pi*{j}/{count})',f'sin(2*pi*{j}/{count})'],
                          'label':label,'local_sign':sign})
    ax.text(0,.36,rf'$d\phi={k}$',ha='center',fontsize=20)
    ax.text(0,-.10,rf'$\det(I-d\phi)={determinant}$',ha='center',fontsize=17)
    ax.text(0,-.51,rf'$|\det(I-d\phi)|={abs(determinant)}$',ha='center',fontsize=17)
    ax.set_title(rf'$\phi_{{{k},0}}(e^{{ix}})=e^{{i({k})x}}$',fontsize=19,pad=14)
    ax.text(0,-1.57,f'{count} fixed point'+('s' if count!=1 else '')+
            '; local contribution '+('−1' if sign<0 else '+1'),
            ha='center',fontsize=14,color=colour)
    rows.append({'k':k,'phase_c':0,'fixed_point_count':count,
                 'derivative':k,'determinant_I_minus_derivative':determinant,
                 'absolute_determinant':abs(determinant),'local_sign':sign,
                 'fixed_points':positions,'degree_zero_trace':1,
                 'degree_one_trace':k,'full_supertrace':1-k})

ax=fig.add_axes([.07,.15,.86,.25]);ax.axis('off')
table=ax.table(cellText=[
    [str(r['k']),str(r['fixed_point_count']),
     r'$\frac{'+str(r['fixed_point_count'])+'}{'+str(r['absolute_determinant'])+'}=1$',
     r'$\frac{('+str(r['k'])+r')\,'+str(r['fixed_point_count'])+'}{'+str(r['absolute_determinant'])+'}='+str(r['k'])+'$',
     rf'$1-({r["k"]})={r["full_supertrace"]}$'] for r in rows],
    colLabels=[r'$k$',r'Fixed count $|k-1|$',r'Degree 0: count$/|1-k|$',
               r'Degree 1: $k\,$count$/|1-k|$',r'Full alternating trace'],
    colWidths=[.08,.20,.25,.27,.20],cellLoc='center',bbox=[0,0,1,1])
table.auto_set_font_size(False);table.set_fontsize(17)
for (r,c),cell in table.get_celld().items():
    cell.set_edgecolor('#b9c7d4');cell.set_linewidth(.9)
    cell.set_facecolor('#dfe9f3' if r==0 else ('#f1f5f9' if r%2 else 'white'))
    if r==0:cell.set_text_props(fontsize=13,weight='bold')
fig.suptitle('Fixed points with the full derivative and absolute Jacobian',fontsize=24,y=.96)
fig.text(.5,.905,r'$S^1=\mathbb{R}/(2\pi\mathbb{Z}),\quad \mu=dx,\quad h_0=h_1=1,\quad c=0$',
         ha='center',fontsize=17)
fig.text(.5,.435,'Both exterior degrees are retained before their alternating subtraction; the constant map has derivative zero.',
         ha='center',fontsize=15)
fig.text(.5,.085,r'$L(\phi_{k,0})=\sum_{\phi(x)=x}\frac{1-k}{|1-k|}=1-k\quad(k\ne1)$',
         ha='center',fontsize=19)
fig.text(.5,.032,'Exact circle coordinates and fixed-point formula: programme proofs EC30–EC36 and LC18. CC0 reproducible construction.',
         ha='center',fontsize=13)
fig.savefig(HERE/'elliptic-complex-fixed-point-signs.png',dpi=240)
fig.savefig(HERE/'elliptic-complex-fixed-point-signs.svg',
            metadata={'Date':None,'Creator':'Codex; reproducible CC0 programme proof figure'})
(HERE/'elliptic-complex-fixed-point-signs.parameters.json').write_text(json.dumps({
    'license':'CC0-1.0','proof_locators':'EC30--EC36; LC18',
    'configuration_space':'S1=R/(2*pi*Z), embedded as (cos(x),sin(x))',
    'density':'dx','Hermitian_squared_frame_norms':[1,1],
    'half_density_factor':'dx^(1/2) in both source and target',
    'density_quotient_at_each_fixed_point':1,
    'maps_and_full_trace_factors':rows,
    'status':'Exact fixed-point positions and full differential/trace factors; circle drawing samples only its smooth embedding.',
    'circle_embedding_sample_count':721,'render_dpi':240
},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
plt.close(fig)
