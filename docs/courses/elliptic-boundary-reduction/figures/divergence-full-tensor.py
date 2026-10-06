"""Exact coordinate diagram for DA16--DA17. License: CC0-1.0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(12.6,6.0),constrained_layout=True)
ax=axes[0]
ax.axhline(0,color='#bbbbbb',linewidth=.8);ax.axvline(0,color='#bbbbbb',linewidth=.8)
ax.annotate('',xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#125c99',lw=3))
ax.annotate('',xy=(1,-1),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#ad3c23',lw=3))
ax.plot([1,1],[0,-1],':',color='#666666',linewidth=1.3)
ax.text(.44,.13,r'$\xi=(1,0)$',color='#125c99',fontsize=14)
ax.text(.02,-1.23,r'$\widetilde A(1)\xi=(1,-1)$',color='#ad3c23',fontsize=13)
ax.text(-.12,.53,r'$\rho(1)=e^{\sin 1}$'+'\n'+r'$\xi^{\mathsf{T}}\widetilde A(1)\xi=1$',fontsize=14)
ax.set(xlim=(-.3,1.4),ylim=(-1.4,.9),xlabel='First coordinate component',ylabel='Second coordinate component')
ax.set_aspect('equal');ax.set_title('Full tensor at x = 1',fontsize=16)
ax.text(.02,-.24,'Fixed vectors in the original Euclidean chart.\nThe arrows identify vectors; they are not trajectories.',transform=ax.transAxes,fontsize=10,va='top')
ax=axes[1]
for lo,hi in [(-3,0),(0,3)]:
 x=np.linspace(lo,hi,401)
 beta=(-1 if lo<0 else 1)+np.abs(x)*np.cos(x)
 ax.plot(x,beta,color='#ad3c23',linewidth=2,label=r'$\beta(x)=\operatorname{sgn}x+|x|\cos x$' if lo==0 else None)
x=np.linspace(-3,3,801)
ax.plot(x,np.exp(np.sin(x)),color='#125c99',linewidth=2,label=r'$\rho(x)=e^{\sin x}$')
ax.plot([0,0],[-1,1],'o',mfc='white',mec='#ad3c23',ms=7,zorder=4)
ax.axhline(0,color='#bbbbbb',linewidth=.8);ax.axvline(0,color='#bbbbbb',linewidth=.8)
ax.set(xlim=(-3,3),ylim=(-4.4,4.4),xlabel='Original coordinate x',ylabel='Density and drift coefficient')
ax.set_title('Density and the entire drift coefficient',fontsize=16)
ax.legend(loc='upper left',fontsize=11)
ax.text(.02,-.16,r'$\widetilde L=-\partial_x^2-\partial_y^2-\cos x\,\partial_x-\beta(x)\partial_y$'+'\n'+r'$\widetilde L(y)=-\beta(x)$'+'\nThe two open endpoints record the jump at x = 0.',transform=ax.transAxes,fontsize=11,va='top')
fig.suptitle('The skew tensor still contributes to the full divergence equation',fontsize=17)
fig.savefig(out/'divergence-full-tensor.png',dpi=150,metadata={'Title':'Full density-bearing divergence example','Author':'','License':'CC0-1.0'})
plt.close(fig)
(out/'divergence-full-tensor.json').write_text(json.dumps(dict(license='CC0-1.0',proof='DA16--DA17',dimension=2,coordinates=['x','y'],density='exp(sin(x))',tensor=[['1','abs(x)'],['-abs(x)','1']],vector_input=[1,0],tensor_x=1,vector_output=[1,-1],drift='sgn(x)+abs(x)*cos(x)',plotted_x=[-3,3],zero_endpoints='Both one-sided values are open; the assigned point value is irrelevant almost everywhere.',diagram_is_a_trajectory=False),indent=2)+'\n',encoding='utf-8')
