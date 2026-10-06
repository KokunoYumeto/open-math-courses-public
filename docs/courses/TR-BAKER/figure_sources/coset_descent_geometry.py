"""Exact exponent-coset example for TR-BAKER-10; original figure, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

folder = Path(__file__).resolve().parent
destination = folder.parent / 'figures' if folder.name == 'figure_sources' else folder
destination.mkdir(exist_ok=True)
points = np.array([(x,y) for x in range(-2,4) for y in range(-2,4)])
origin = np.array([1,0])
selected = np.all((points-origin)%2==0,axis=1)
new = (points[selected]-origin)//2
assert len(points)==36 and len(new)==9
assert {tuple(p) for p in new}=={(x,y) for x in range(-1,2) for y in range(-1,2)}
fig, axes = plt.subplots(1,2,figsize=(12.5,6.6))
colors = {(0,0):'#7697bb',(0,1):'#879983',(1,0):'#c44f24',(1,1):'#b695bf'}
for residue, color in colors.items():
    subset=np.all(points%2==np.array(residue),axis=1)
    axes[0].scatter(points[subset,0],points[subset,1],s=70,color=color,
                    alpha=1 if residue==(1,0) else .43,label=str(residue))
axes[0].scatter([1],[0],s=170,facecolors='none',edgecolors='#161616',linewidths=1.5)
axes[0].annotate(r'$m_*=(1,0)$',xy=(1,0),xytext=(1.2,.34),fontsize=17)
axes[0].set_title('Four exponent classes modulo 2',fontsize=18)
axes[0].set_xticks(range(-2,4));axes[0].set_yticks(range(-2,4))
axes[0].set_xlim(-2.5,3.6);axes[0].set_ylim(-2.5,3.5)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, title='Residues of (m1, m2) modulo 2',
           loc='upper center',bbox_to_anchor=(.275,.30),ncol=4,fontsize=14,title_fontsize=14)
axes[0].set_xlabel(r'$m_1$');axes[0].set_ylabel(r'$m_2$')
axes[1].scatter(new[:,0],new[:,1],s=75,color=colors[(1,0)])
axes[1].scatter([0],[0],s=170,facecolors='none',edgecolors='#161616',linewidths=1.5)
axes[1].annotate(r'$m_*\mapsto(0,0)$',xy=(0,0),xytext=(.12,.28),fontsize=17)
axes[1].set_title(r'Retained class: $n=(m-m_*)/2$',fontsize=18)
axes[1].set_xticks(range(-1,2));axes[1].set_yticks(range(-1,2))
axes[1].set_xlim(-1.6,1.8);axes[1].set_ylim(-1.6,1.6)
axes[1].set_xlabel(r'$n_1$');axes[1].set_ylabel(r'$n_2$')
for ax in axes:
    ax.tick_params(labelsize=16);ax.xaxis.label.set_size(17);ax.yaxis.label.set_size(17)
    ax.set_aspect('equal');ax.grid(alpha=.18);ax.set_axisbelow(True)
    ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.075,right=.96,bottom=.42,top=.86,wspace=.33)
fig.suptitle('Extract one exact zero sum, then divide exponent differences by 2',fontsize=21,y=.97)
fig.text(.53,.12,'Original coordinate width: 5.  Retained width: 4.  New width: 2.',ha='center',fontsize=17)
fig.text(.53,.045,r'$\eta^{s m}=\eta^{s m_*}\vartheta^{s n},\quad \eta_i^2=\vartheta_i;\quad s$ odd.',ha='center',fontsize=18)
fig.savefig(destination/'coset-descent-geometry.png',dpi=200)
plt.close(fig)
