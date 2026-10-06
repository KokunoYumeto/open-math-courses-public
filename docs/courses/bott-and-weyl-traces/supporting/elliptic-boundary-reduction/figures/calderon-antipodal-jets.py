"""Exact real section of the complex Cauchy-jet reflection; CC0-1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,2,figsize=(10.5,5.6))
blue='#1268ac';orange='#b24e0d'
x=np.array([-1.35,1.35])
for ax,title in zip(axes,[r'$\eta=(1,0)$',r'$-\eta=(-1,0)$']):
    ax.plot(x,x,color=blue,lw=2.5,label=r'$V^+=\mathbb{C}(1,i)$')
    ax.plot(x,-x,color=orange,lw=2.5,label=r'$V^-=\mathbb{C}(1,-i)$')
    ax.axhline(0,color='#888888',lw=.7);ax.axvline(0,color='#888888',lw=.7)
    ax.set(xlim=(-1.55,1.55),ylim=(-1.55,1.55),aspect='equal',
           xlabel=r'$\operatorname{Re}U_0$',ylabel=r'$\operatorname{Im}U_1$')
    ax.set_title(title,fontsize=15,pad=14);ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    ax.grid(alpha=.16);ax.legend(loc='upper left',fontsize=10,framealpha=.95)
axes[0].scatter([1],[-1],color=orange,s=65,zorder=5)
axes[0].annotate(r'$(1,-i)$',(1,-1),xytext=(.48,-1.40),fontsize=12)
axes[1].scatter([1],[1],color=blue,s=65,zorder=5)
axes[1].annotate(r'$(1,i)$',(1,1),xytext=(.65,1.23),fontsize=12)
arrow=ConnectionPatch(xyA=(1,-1),xyB=(1,1),coordsA='data',coordsB='data',
    axesA=axes[0],axesB=axes[1],arrowstyle='-|>',mutation_scale=18,
    connectionstyle='arc3,rad=.19',color='#333333',lw=1.5)
fig.add_artist(arrow)
fig.text(.5,.085,r'$S(U_0,U_1)=(U_0,-U_1)$',ha='center',fontsize=15,
         bbox=dict(facecolor='white',edgecolor='none',pad=3))
fig.text(.5,.025,r'Exact section: $U_0\in\mathbb{R},\ U_1\in i\mathbb{R}$; proof AP13',ha='center',fontsize=11)
fig.suptitle(r'Original normal polynomial $p(\eta,\zeta)=\zeta^2+\eta_1^2+\eta_2^2$',fontsize=15,y=.97)
fig.subplots_adjust(bottom=.21,top=.82,wspace=.28)
fig.savefig(out/'calderon-antipodal-jets.png',dpi=180,facecolor='white')
params=dict(license='CC0-1.0',dimension_X=3,order=2,bundle_rank=1,
    original_covectors=[[1,0],[-1,0]],original_jet_points=['(1,-i)','(1,i)'],
    plotted_section='U0 real and U1 purely imaginary in the original complex jet space',
    plotted_coordinates=['Re U0','Im U1'],reflection_matrix=[[1,0],[0,-1]],
    original_principal_polynomial='zeta^2+eta_1^2+eta_2^2',proof_locator='AP13',
    whole_complex_space_depicted=False,arbitrary_projection_orthogonality_claimed=False)
(out/'calderon-antipodal-jets.json').write_text(json.dumps(params,indent=2)+'\n',encoding='utf-8')
print('Rendered exact original-coordinate section and retained its parameters.')
