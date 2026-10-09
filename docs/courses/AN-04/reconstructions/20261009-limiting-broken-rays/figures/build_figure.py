"""Exact compressed strip-ray convergence, equations LR19 and LR20."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':10,'svg.fonttype':'none','svg.hashsalt':'an04-limiting-broken-rays-20261009'})
fig,axs=plt.subplots(2,1,figsize=(12,6.8),sharex=True)
fig.subplots_adjust(top=.81,bottom=.20,left=.08,right=.98,hspace=.24)
data=[(0,'#172f42','limit h = 0',2.2),(1/8,'#cf6d33','h = 1/8',1.5),(1/32,'#4c8c73','h = 1/32',1.3),(1/128,'#746aa1','h = 1/128',1.2)]
for h,color,label,lw in data:
 cuts=[0,.5-h,1.5-h,2.5-h,3]
 for j,(lo,hi) in enumerate(zip(cuts,cuts[1:])):
  t=np.linspace(lo,hi,151)
  r=[.5+h+t,1.5-h-t,t-1.5+h,3.5-h-t][j]
  rho=[-1,1,-1,1][j]
  axs[0].plot(t,r,c=color,lw=lw,label=label if j==0 else None)
  axs[1].plot(t,r*(1-r)*rho,c=color,lw=lw)
 axs[0].scatter([0,3],[.5+h,.5-h],c=color,s=18,zorder=5)
for ax in axs:
 for v in [.5,1.5,2.5]:ax.axvline(v,c='#aab5bd',ls='--',lw=.7)
 ax.set_xlim(0,3);ax.grid(alpha=.17)
axs[0].set_ylim(-.06,1.08);axs[0].set_ylabel('Normal position r')
axs[0].legend(ncol=4,loc='upper center',bbox_to_anchor=(.5,1.31),frameon=False)
axs[1].set_ylim(-.29,.29);axs[1].axhline(0,c='#aab5bd',lw=.7)
axs[1].set_ylabel(r'Compressed component $\zeta=r(1-r)\rho$')
axs[1].set_xlabel('Physical time t  (Hamilton parameter s = −t/2)')
fig.suptitle('Reflection times move; the compressed rays converge uniformly',fontsize=15,fontweight='bold',y=.98)
fig.text(.5,.10,r'$p=\rho^2-\tau^2,\quad \tau=1,\quad \rho=\pm1,\quad |r_h-r_0|\leq h,\quad |\zeta_h-\zeta_0|\leq2h.$',ha='center',fontsize=11)
fig.text(.5,.045,'Dashed lines: limiting wall hits. Dots: interior endpoints. These exact rays are transverse; the theorem also permits glancing limits.\nCurves show singular-set geometry, not amplitudes. Proof and all four branches: Exercise 1.',ha='center',fontsize=9)
svg=P/'limiting-strip-rays.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'AN-04 independent reproducible mathematical figure'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'exact_parameters':{'h':['0','1/8','1/32','1/128'],'time_interval':['0','3'],'tau':'1','normal_momenta':['-1','1','-1','1']},
 'uniform_bounds':{'normal_position':'h','compressed_normal_component':'2h'},
 'omitted_coordinates':'tau=1; rho=-dr/dt; Hamilton parameter s=-t/2',
 'actually_inspected':False,'exact_coordinate_review_complete':False,'not_a_solution_intensity':True}
(P.parent/'figure-check.json').write_text(json.dumps(report,indent=2)+'\n','utf-8')
print(json.dumps(report))
