"""Reproduce the actual cover maps, integer cone and split graph geometry."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
matplotlib.rcParams['svg.hashsalt']='quasiordinary-SNC-geometry'
pa=argparse.ArgumentParser();pa.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent);args=pa.parse_args()
out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
bg='#f5f8fd';blue='#2466a3';green='#147e6b';orange='#bc6828';ink='#203d55';muted='#536b83'
fig=plt.figure(figsize=(18,17),facecolor=bg)
fig.text(.5,.969,'Power splitting and a proper SNC cover',ha='center',fontsize=26,color=ink)
fig.text(.5,.943,'A. Monomial discriminant on a polydisc; actual maps QG.9, QG.22 and QG.30',ha='center',fontsize=14,color=muted)
ax=fig.add_axes([.035,.785,.93,.135]);ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.add_patch(FancyBboxPatch((.005,.01),.99,.97,boxstyle='round,pad=.008',edgecolor='#adc4da',facecolor='white',transform=ax.transAxes))
nodes=[(.08,r'$Z$'),(.35,r'$D_R\times B^\prime$'),(.64,r'$D_R\times\widetilde B$'),(.91,r'$X=D_R\times B$')]
for x,t in nodes:ax.text(x,.66,t,ha='center',va='center',fontsize=20,color=blue)
for x0,x1,label in [(.13,.25,r'$\mu$'),(.45,.53,r'$1\times\beta$'),(.75,.81,r'$1\times q$')]:
 ax.annotate('',(x1,.65),(x0,.65),arrowprops={'arrowstyle':'->','lw':2,'color':green})
 ax.text((x0+x1)/2,.80,label,ha='center',fontsize=16,color=green)
ax.text(.5,.32,r'$z_i=u_i^{m!}\ (i\leq k),\qquad \deg(F|_{X\setminus S})=(m!)^k$',ha='center',fontsize=19,color=green)
ax.text(.5,.10,'Every map is proper and locally projective. The reduced inverse boundary is SNC.',ha='center',fontsize=12,color=muted)
fig.text(.26,.747,'B. Principalizing (x³, y²): integer cone',ha='center',fontsize=17,color=muted)
fan=fig.add_axes([.065,.475,.39,.25],facecolor='white')
rays=[(1,0),(1,1),(2,3),(1,2),(0,1)]
for a,b in rays:
 d=3*a-2*b
 fan.annotate('',(a,b),(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':green if d==0 else blue if d>0 else orange})
 dx,dy={ (1,0):(.05,-.05),(1,1):(.06,-.04),(2,3):(-.60,.10),(1,2):(.08,.04),(0,1):(.05,.08)}[(a,b)]
 fan.text(a+dx,b+dy,f'({a}, {b}); d={d}',fontsize=11,color=green if d==0 else blue if d>0 else orange)
fan.set_xlim(-.15,2.9);fan.set_ylim(-.25,3.6);fan.set_aspect('equal')
fan.set_xticks([0,1,2]);fan.set_yticks([0,1,2,3]);fan.grid(alpha=.18)
fan.set_xlabel('a',fontsize=12);fan.set_ylabel('b',fontsize=12)
fig.text(.26,.436,'Exact primitive rays; d(a,b)=3a−2b. Equal lattice scales.',ha='center',fontsize=11,color=muted)
fig.text(.26,.416,'All adjacent determinants are 1; maximal sums 5 → 3 → 2.',ha='center',fontsize=11,color=muted)
fig.text(.74,.747,'C. Split roots of t²−x³ after x=u²',ha='center',fontsize=17,color=muted)
roots=fig.add_axes([.57,.475,.34,.25],facecolor='white')
u=np.linspace(-1,1,501)
roots.plot(u,u**3,color=green,lw=2.4,label='t = u³');roots.plot(u,-u**3,color=blue,lw=2.4,label='t = −u³')
roots.set_xlim(-1.1,1.1);roots.set_ylim(-1.1,1.1);roots.set_aspect('equal');roots.grid(alpha=.18)
roots.set_xlabel('Re u',fontsize=12);roots.set_ylabel('Re t',fontsize=12);roots.legend(frameon=False,loc='upper center',fontsize=11)
fig.text(.74,.436,'Im u = Im t = 0; −1 ≤ u ≤ 1; equal axes.',ha='center',fontsize=11,color=muted)
fig.text(.74,.416,'Collision ideal (u³): W = 3 → 2 → 1 → 0.',ha='center',fontsize=11,color=muted)
fig.text(.26,.377,'D. Final real coordinate slice',ha='center',fontsize=17,color=muted)
sep=fig.add_axes([.11,.10,.30,.25],facecolor='white')
sep.axvline(0,color=orange,lw=2,label='u = 0')
sep.axhline(0,color=green,lw=2,label='v = 0')
sep.axhline(-2,color=blue,lw=2,label='v = −2')
sep.plot([0,0],[0,-2],'o',color=orange,markersize=5)
sep.set_xlim(-.9,.9);sep.set_ylim(-2.6,.6);sep.set_aspect('equal');sep.grid(alpha=.18)
sep.set_xlabel('Re u',fontsize=12);sep.set_ylabel('Re v',fontsize=12)
sep.text(.13,.10,'v = 0',color=green,fontsize=12);sep.text(.13,-1.86,'v = −2',color=blue,fontsize=12)
fig.text(.26,.058,'The two graph sections are disjoint and transverse to u=0.',ha='center',fontsize=11,color=muted)
fig.text(.74,.342,r'$v_0=t-u^3=u^3v$',ha='center',fontsize=23,color=blue)
fig.text(.74,.290,r'$x=u^2,\qquad t=u^3(1+v)$',ha='center',fontsize=23,color=green)
fig.text(.74,.238,r'$P=u^6v(v+2),\qquad xP=u^8v(v+2)$',ha='center',fontsize=22,color=green)
fig.text(.74,.187,r'$\det\frac{\partial(x,t)}{\partial(u,v)}=2u^4$',ha='center',fontsize=23,color=blue)
fig.text(.74,.130,'Three global graph blowups; every complementary chart is QG.37–QG.38.',ha='center',fontsize=11,color=muted)
fig.text(.5,.025,'Panels C and D are real slices of complex two-dimensional charts. Algebraic map panels have no metric scale.',ha='center',fontsize=12,color=muted)
fig.savefig(out/'quasiordinary-SNC-geometry.png',dpi=150,metadata={'Software':'Matplotlib'})
fig.savefig(out/'quasiordinary-SNC-geometry.svg',metadata={'Date':None});plt.close(fig)
data={'equations':['QG.9','QG.22','QG.30','QG.34–QG.38'],
 'power_exponent':'m!','complement_cover_degree':'(m!)^k',
 'fan':{'input_ideal':['x^3','y^2'],'rays':rays,'difference':'3a-2b','adjacent_determinants':[1,1,1,1],'maximal_sum_sequence':[5,3,2],'metric':'equal integer lattice scales'},
 'split_real_slice':{'u_min':-1,'u_max':1,'roots':['u^3','-u^3'],'imaginary_coordinates':0,'equal_axes':True},
 'graph_weights':[3,2,1,0],'final_map':{'x':'u^2','t':'u^3(1+v)','P':'u^6 v(v+2)','xP':'u^8 v(v+2)','jacobian':'2u^4'},
 'final_real_slice':{'u_min':'-9/10','u_max':'9/10','v_min':'-13/5','v_max':'3/5','boundary':['u=0','v=0','v=-2'],'equal_axes':True}}
(out/'quasiordinary-SNC-geometry-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
