"""Render the exact two-dimensional carriers and a specified frequency cell."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,Rectangle

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN02-nonconvex192'})
blue='#17658a';red='#bb553f';green='#32765c';gray='#737a82'
geometry={
 'schema':'AN02-nonconvex-localization-original-geometry192/v1',
 'physical':{'K1':{'x1':-2,'x2_interval':[-1,1]},'K2':{'x1_interval':[-1,1],'x2':2},
 'convex_hull_vertices':[[-2,-1],[1,2],[-1,2],[-2,1]],
 'x0':[-1.5,1],'distance_to_K1':0.5,'distance_to_K2':'sqrt(5)/2',
 'r':{'numerator':2,'denominator':5},'smooth_ball_radius':0.2,
 'theta1':[1,0],'theta2':[0,-1],'translated_support_bounds':[-0.5,-1],
 'mathematical_status':'Example3 proves singular support and closed profile-carrier union equal K1 union K2;individual proper carriers are contained in one component;no complete classification is asserted.',
 'proof_locators':['Learner Worked example3','Formal Lemmas1.3,2.2','Formal Theorem1.1']},
 'frequency':{'n':1,'N':1,'derivative_budget':2,'r':2,'epsilon':{'numerator':1,'denominator':10000},
 'j':26,'ell':260000,'K':26,'T':260000,'lattice_index':256,'center':66560000,'R':66560000,
 'real_support_bound_about_center':[-195000,195000],
 'imaginary_transport_interval':[0,260000],'m':50495,
 'direction':[1],'complex_coordinates':'Real and imaginary displacement from center,in units ell;the rectangle bounds the cutoff support and transport,not its exact pointwise values.',
 'sum_factor_power':5,'correction_base':{'numerator':13,'denominator':2000},
 'top_exponential_rate':5000,'shared_unspecified_estimate_constant_omitted':True,
 'proof_locators':['Formal Proposition3.4','Formal Lemma4.1','Formal Proposition5.1','Learner Worked example4']},
 'Blender_assessment':'Flat exact carrier geometry and one complex-coordinate slice are directly represented in vector plots;three-dimensional scenes would add no mathematical information.'}
(OUT/'geometry192.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')

def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=160,bbox_inches='tight',facecolor='white')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Date':None})
 plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(14.6,6.0),gridspec_kw={'width_ratios':[1.05,1]})
ax=axes[0]
hull=np.array(geometry['physical']['convex_hull_vertices'])
ax.add_patch(Polygon(hull,closed=True,facecolor='#e7edf1',edgecolor=gray,linestyle='--',linewidth=1.5))
ax.plot([-2,-2],[-1,1],color=blue,lw=5,label='K₁: vertical singular segment')
ax.plot([-1,1],[2,2],color=red,lw=5,label='K₂: horizontal singular segment')
ax.text(-2.19,0,'K₁',color=blue,fontsize=14,ha='center',va='center',rotation=90)
ax.text(0,2.12,'K₂',color=red,fontsize=14,ha='center')
x0=np.array([-1.5,1.0]);ax.add_patch(Circle(x0,.2,facecolor='#dfeee5',edgecolor=green,lw=1.5))
ax.scatter(*x0,color='#172b35',zorder=6,s=38)
ax.annotate('x₀ = (−3/2, 1)',x0,xytext=(-1.08,.62),fontsize=11,arrowprops={'arrowstyle':'-','color':gray})
ax.annotate('',x0+np.array([.6,0]),x0,arrowprops={'arrowstyle':'->','lw':2,'color':blue})
ax.text(-.95,1.06,'θ₁ = (1, 0)',color=blue,fontsize=11)
ax.annotate('',x0+np.array([0,-.65]),x0,arrowprops={'arrowstyle':'->','lw':2,'color':red})
ax.text(-1.92,.13,'θ₂ = (0, −1)',color=red,fontsize=11)
ax.text(-2.35,-1.32,'Solid segments: A(u) = sing supp u',fontsize=11)
ax.text(-2.35,-1.56,'Dashed polygon: their convex hull',fontsize=11)
ax.set(xlim=(-2.5,1.4),ylim=(-1.72,2.42),xlabel='x₁',ylabel='x₂',
 title='A smooth point inside the common convex hull')
ax.set_aspect('equal');ax.grid(alpha=.16)
ax=axes[1]
angle=np.linspace(-np.pi,np.pi,1201)
cx=np.cos(angle);sy=np.sin(angle)
h1=-.5*cx+np.maximum(-2*sy,0)
h2=1.5*cx+np.abs(cx)+sy
ax.plot(angle/np.pi,h1,color=blue,lw=2,label='H(K₁ − x₀)')
ax.plot(angle/np.pi,h2,color=red,lw=2,label='H(K₂ − x₀)')
ax.axhline(-.4,color=green,ls='--',lw=1.5,label='−r = −2/5')
ax.scatter([0],[-.5],color=blue,zorder=5)
ax.scatter([-.5],[-1],color=red,zorder=5)
ax.annotate('θ₁: bound −1/2',(0,-.5),xytext=(.1,-1.16),fontsize=10,
 arrowprops={'arrowstyle':'-','color':blue})
ax.annotate('θ₂: bound −1',(-.5,-1),xytext=(-.93,-1.64),fontsize=10,
 arrowprops={'arrowstyle':'-','color':red})
ax.set(xlim=(-1,1),ylim=(-1.85,3.15),xlabel='angle / π; θ = (cos angle, sin angle)',
 ylabel='translated support function',title='Each component uses its own separating normal')
ax.grid(alpha=.16);ax.legend(loc='upper right',fontsize=10)
fig.suptitle('Nonconvex localization retains the gap between frequency carriers',fontsize=17,y=1.02)
fig.tight_layout()
save(fig,'nonconvex-carriers-and-separating-normals')

fig,axes=plt.subplots(1,3,figsize=(18.2,5.4),gridspec_kw={'width_ratios':[1.25,1,1]})
ax=axes[0]
ax.add_patch(Rectangle((-.75,0),1.5,1,facecolor='#e6eff4',edgecolor=blue,lw=1.3))
ax.plot([-.75,.75],[0,0],color=blue,lw=3)
ax.plot([-.75,.75],[1,1],color=red,lw=3)
for real in [-.55,0,.55]:
 ax.annotate('',(real,.97),(real,.04),arrowprops={'arrowstyle':'->','lw':1.5,'color':green})
ax.text(0,.08,'real cutoff support bound',ha='center',fontsize=10)
ax.text(0,1.04,'top: t = T = ℓ',ha='center',fontsize=11,color=red)
ax.text(0,.52,'finite Taylor correction\nalong θ = 1',ha='center',va='center',fontsize=12,color=green)
ax.text(-.91,-.24,'ℓ = 260000; c = R = 66560000',fontsize=10)
ax.text(-.91,-.36,'|ζ − c| ≤ 1.25ℓ < m log R',fontsize=10)
ax.set(xlim=(-1,1),ylim=(-.44,1.24),xlabel='(Re ζ − c) / ℓ',ylabel='Im ζ / ℓ',
 title='Specified one-dimensional complex cell')
ax.grid(alpha=.16)
j=np.arange(26,37,dtype=float)
log_error=5*j*np.log10(2)+(j+1)*np.log10(13/2000)
log_top=5*j*np.log10(2)-5000*j/np.log(10)
axes[1].plot(j,log_error,'o-',color=green)
axes[1].set(xlabel='dyadic level j',ylabel='log₁₀ of correction summation factor',
 title='Correction: 2^(5j) (13/2000)^(j+1)')
axes[1].grid(alpha=.2)
axes[2].plot(j,log_top,'o-',color=red)
axes[2].set(xlabel='dyadic level j',ylabel='log₁₀ of top summation factor',
 title='Top: 2^(5j) exp(−5000j)')
axes[2].grid(alpha=.2)
axes[2].ticklabel_format(style='plain',axis='y')
fig.suptitle('Finite Taylor order grows with j; both summation factors decrease',fontsize=17,y=1.025)
fig.text(.53,-.02,'n = 1, N = 1, b = 2, r = 2, ε = 1/10000; the shared estimate constant C is omitted.',ha='center',fontsize=11)
fig.tight_layout()
save(fig,'logarithmic-cell-and-taylor-correction')
manifest=[]
for p in sorted(OUT.iterdir()):
 if p.is_file():
  b=p.read_bytes();manifest.append({'path':p.name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest().upper()})
(ROOT/'figure-manifest192.json').write_text(json.dumps({'original_geometry':True,'files':manifest},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figures':2,'PNG_and_SVG_pairs':2,'exact_geometry':True}))
