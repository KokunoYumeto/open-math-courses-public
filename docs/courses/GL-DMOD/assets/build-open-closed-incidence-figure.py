"""Reproduce the normal-cone section and exact connecting signs."""
from pathlib import Path
from fractions import Fraction as Q
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,FancyArrowPatch
import numpy as np

parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent);args=parser.parse_args()
args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'GL-DMOD-OCM-20261019','mathtext.fontset':'dejavusans'})
point=(Q(4,5),Q(0));R=Q(2)
samples=[(Q(-6,5),Q(13,10)),(Q(1,2),Q(6,5)),(Q(-4,5),Q(-11,10)),(Q(7,5),Q(-7,10))]
data={'normal_section':{'coordinates':['a','b'],'other_normal_coordinates':0,'R':str(R),'L':'1','cone':'a<=0 and abs(b)<=-a','point_e':[str(x)for x in point]},'paths':[],'general_proof':['OCM.5–OCM.7','OCM.9–OCM.13','OCM.20–OCM.22'],'finite_path_samples_are_not_the_general_cone_proof':True}
for v in samples:
 assert sum(x*x for x in v)<R*R
 points=[]
 for step in range(17):
  t=Q(step,16);n=tuple((1-t)*a+t*b for a,b in zip(v,point))
  assert not(n[0]<=0 and abs(n[1])<=-n[0]);assert sum(x*x for x in n)<R*R
  points.append({'s':str(t),'normal':[str(x)for x in n]})
 data['paths'].append({'start':[str(x)for x in v],'sampled_points':points})

fig=plt.figure(figsize=(16,10),dpi=150,facecolor='#f5f7fc')
fig.suptitle('The open/closed incidence comparison keeps the connecting degree',fontsize=22,y=.965,fontweight='bold')
ax=fig.add_axes([.055,.23,.43,.61],aspect='equal',facecolor='white')
ax.add_patch(Circle((0,0),float(R),facecolor='#ffffff',edgecolor='#355c8c',linewidth=2))
theta=np.linspace(3*np.pi/4,5*np.pi/4,300)
vertices=np.vstack([[0,0],np.column_stack([2*np.cos(theta),2*np.sin(theta)]),[0,0]])
ax.add_patch(Polygon(vertices,closed=True,facecolor='#d9e0e8',edgecolor='#8292a7',linewidth=1.5))
colors=['#007c91','#a14783','#267c45','#bc681f']
for v,color in zip(samples,colors):
 a,b=map(float,v);e,f=map(float,point)
 ax.plot([a,e],[b,f],color=color,lw=2,alpha=.85)
 ax.scatter([a],[b],s=38,color=color,zorder=5)
 ax.add_patch(FancyArrowPatch((a,b),(a*.4+e*.6,b*.4+f*.6),arrowstyle='-|>',mutation_scale=16,color=color,lw=2))
ax.scatter([float(point[0])],[float(point[1])],s=70,color='#1b355b',zorder=6)
ax.text(float(point[0])+.1,float(point[1])-.08,r'$e=(4/5,0)$',fontsize=13,va='top')
ax.text(-1.7,.10,r'$G$',fontsize=24,color='#35465a')
ax.text(-1.84,-.35,r'$|b|\leq-a$',fontsize=14,color='#35465a')
ax.text(.1,1.7,r'$B_2\setminus G$',fontsize=15,color='#1b355b')
ax.axhline(0,color='#c6ced9',lw=.7,zorder=0);ax.axvline(0,color='#c6ced9',lw=.7,zorder=0)
ax.set(xlim=(-2.15,2.15),ylim=(-2.15,2.15),xlabel=r'first real normal coordinate $a$',ylabel=r'one transverse real normal coordinate $b$')
ax.set_title('A. One normal section; every path stays outside the cone',fontsize=15,pad=17)
ax.spines[['top','right']].set_visible(False)

right=fig.add_axes([.535,.20,.43,.66]);right.axis('off')
right.text(0,1,'B. Relative primitive and the contravariant connecting map',fontsize=15,fontweight='bold',va='top')
right.text(.02,.90,r'$h_s(n)=(1-s)n+se$',fontsize=21)
right.text(.02,.815,r'$dK+Kd=j\varepsilon-1$',fontsize=21)
right.text(.02,.725,r'$T(a,b)=(j_A\varepsilon_Bb-K_Aa,\ K_Bb)$',fontsize=19)
right.text(.02,.64,r'$dT+Td=1$',fontsize=21,color='#267c45')
right.text(.02,.56,'Same homotopy on the ball and its complement.',fontsize=13)
right.text(.02,.515,'The relative differential is',fontsize=13)
right.text(.02,.46,r'$d(a,b)=(da,\ ra-db).$',fontsize=18)
right.text(.02,.355,r'$\mu\mathrm{hom}(\mathbb{C}_M,F)=0\quad(p\ne0)$',fontsize=18,color='#267c45')
right.text(.02,.265,r'$\mu\mathrm{hom}(\mathbb{C}_{\Omega},F)$',fontsize=19)
right.annotate('',xy=(.42,.16),xytext=(.42,.23),arrowprops={'arrowstyle':'-|>','lw':1.8,'color':'#1b355b'})
right.text(.48,.18,r'$\partial^\vee$',fontsize=20)
right.text(.02,.10,r'$\mu\mathrm{hom}(\mathbb{C}_{S},F)[1]$',fontsize=19)
right.text(.02,.035,r'$=\mu\mathrm{hom}(\mathbb{C}_{S}[-1],F)$',fontsize=19)
fig.text(.56,.155,r'Relative connecting map: $(a,b)\mapsto(ca,-cb)$.',fontsize=15,color='#1b355b')
fig.text(.055,.117,r'The left panel is a real two-plane section of the normal ball; all other normal coordinates are zero.',fontsize=13)
fig.text(.055,.078,r'Incidence: $N=d+1$,  $\dim_{\mathbb{C}}M=2N$,  projection shift $[4N]$;  the topological inverse uses $[2N]$.',fontsize=15)
fig.text(.055,.035,'Cone and primitive: OCM.5–OCM.13. Connecting signs and degree: OCM.20–OCM.24. Inverse kernel products are separate.',fontsize=12,color='#526174')
name='open-closed-incidence-connecting-map'
fig.savefig(args.output_dir/(name+'.png'),dpi=150,metadata={'Software':'Open mathematics course figures'})
fig.savefig(args.output_dir/(name+'.svg'),metadata={'Date':None,'Creator':'Open mathematics course figures'})
(args.output_dir/(name+'-exact-data.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
plt.close(fig)
print(json.dumps({'outputs':3,'png_size':[2400,1500],'exact_rational_path_points':68}))
