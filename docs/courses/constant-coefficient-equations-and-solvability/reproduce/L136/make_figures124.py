"""Reproducible exact examples for the horizontal-integral asymptotic proof."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OWN=Path(__file__).resolve().parent;FIG=OWN/'figures';FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':16,'axes.labelsize':13,'svg.hashsalt':'AN02-L136-integrated-halfspace-kernels'})
def save(fig,name):
 fig.savefig(FIG/(name+'.png'),dpi=180,bbox_inches='tight',metadata={'Software':'Original AN02 mathematical figure'})
 fig.savefig(FIG/(name+'.svg'),bbox_inches='tight',metadata={'Date':None,'Creator':'Open Mathematics Courses','Description':'Exact functions accompanying the independent proof A1–A23'})
 plt.close(fig)
s=np.linspace(0,2,801)
fig,axes=plt.subplots(1,2,figsize=(12.4,5.3))
axes[0].plot(s,np.minimum(s,1),color='#246392',lw=2.5)
axes[0].scatter([1],[1],color='#246392',zorder=5)
axes[0].axvline(1,color='#89959d',lw=1,ls='--')
axes[0].set_title('The exact horizontal Green integral (A11)')
axes[0].set_ylabel('Horizontal integral of g')
axes[0].text(.34,.16,'source height a = 1\n∫ g((z,s),(0,1)) dz = min(s,1)',transform=axes[0].transAxes,bbox={'facecolor':'white','alpha':.94,'edgecolor':'#cad5df'})
for lam,color in [(1,'#246392'),(2,'#ba761d'),(4,'#286f59')]:
 values=np.minimum(s,1/lam)/lam
 axes[1].plot(s,values,color=color,lw=2.4,label=f'dilation λ = {lam}; source height 1/{lam}')
 axes[1].fill_between(s,0,values,color=color,alpha=.065)
 axes[1].scatter([1/lam],[1/lam**2],color=color,zorder=5)
axes[1].set_title('Scaled source and its full-slab integral (A21–A22)')
axes[1].set_ylabel('λ⁻¹ min(s, λ⁻¹),  n = 2')
axes[1].legend(fontsize=10,loc='upper center',bbox_to_anchor=(.5,-.23))
for ax in axes:ax.set(xlabel='Observation height s',xlim=(0,2),ylim=(0,1.1));ax.grid(alpha=.18)
fig.tight_layout();save(fig,'green-horizontal-integral')

lam=np.geomspace(1,32,301)
fig,ax=plt.subplots(figsize=(9.5,5.6))
ax.loglog(lam,2/lam**2,color='#246392',lw=2.6,label='Boundary atom: full horizontal slab 0 < s < 2')
ax.loglog(lam,2/lam**2-.5/lam**3,color='#ba761d',lw=2.6,label='Interior atom at height 1: same full slab')
ax.loglog(lam,1/lam,color='#286f59',lw=2.6,label='Affine datum β = 1: compact window of volume 1')
ax.set(xlabel='Dilation factor λ',ylabel='Exact integral error',title='Exact error formulas for three stated observation windows (A20–A23)')
ax.set_xticks([1,2,4,8,16,32],labels=['1','2','4','8','16','32']);ax.grid(alpha=.2,which='both');ax.legend(fontsize=10,loc='lower left')
fig.tight_layout();save(fig,'exact-integral-errors')
(FIG/'geometry.json').write_text(json.dumps({'dimension':2,'green_horizontal_integral':{'source_height':1,'height_interval':[0,2],'dilations':[1,2,4],'formula':'lambda^(-1)*min(s,lambda^(-1))','proof_locators':['A11','A21','A22']},
 'exact_error_curves':{'dilation_interval':[1,32],'boundary_atom':'2*lambda^(-2)','interior_atom':'2*lambda^(-2)-(1/2)*lambda^(-3)','atom_windows':'all horizontal coordinates and0<s<2; unbounded slabs used to bound compact windows','affine':'lambda^(-1)','affine_window_volume':1,'proof_locators':['A20','A22','A23']},
 'status':'Samples of explicit exact functions; the written proof supplies normalization and the general convergence','source_text':'linear-profile-under-dilation.md'},indent=2)+'\n',encoding='utf-8')
print('Rendered both original mathematical PNG/SVG pairs and geometry metadata.')
