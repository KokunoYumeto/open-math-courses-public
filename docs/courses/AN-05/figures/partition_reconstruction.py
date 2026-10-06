"""Exact partition algebra and finite reconstruction mechanism for L044.
CC0; GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October2026.
Numerical panels are pointwise coefficient examples,not assigned operators.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'figure.facecolor':'#fffdfa','axes.facecolor':'#fffdfa'})
fig=plt.figure(figsize=(14,9.2),dpi=150)
gs=fig.add_gridspec(2,2,left=.07,right=.95,top=.82,bottom=.14,hspace=.45,wspace=.38,height_ratios=[1,1.25])
fig.text(.055,.947,'A partition needs operator reconstruction',fontsize=25,weight='bold',color='#172d44')
fig.text(.055,.89,'Exact coefficient examples above; the full finite operator mechanism below',fontsize=17,color='#414b57')
ax=fig.add_subplot(gs[0,0]);ax.set_title(r'Ordered values: $\psi_1=\psi_2=\psi_3=1/2$',fontsize=17,pad=15)
vals=[.5,.25,.125,.125];labels=['1/2','1/4','1/8','1/8'];colors=['#4773a0','#4c8f84','#8a6f40','#b9bec4']
start=0
for value,label,color in zip(vals,labels,colors):
    ax.barh(.6,value,left=start,height=.35,color=color,edgecolor='white',lw=2)
    ax.text(start+value/2,.6,label,ha='center',va='center',color='white' if start<.875 else '#172d44',fontsize=17,weight='bold');start+=value
ax.set(xlim=(0,1),ylim=(0,1.15));ax.set_yticks([]);ax.set_xticks([0,.5,.75,.875,1],['0','1/2','3/4','7/8','1'])
ax.text(.5,.05,r'$\Psi=7/8,\quad 1-\Psi=1/8$',ha='center',fontsize=19,color='#172d44')
ax.spines[['left','right','top']].set_visible(False)
ax=fig.add_subplot(gs[0,1]);ax.set_title('Mixed matrix at one phase point',fontsize=17,pad=15)
matrix=np.array([[.5,0],[1,0]])
ax.imshow(matrix,cmap='Blues',vmin=0,vmax=1,aspect='equal')
for row in range(2):
    for col in range(2):ax.text(col,row,['1/2','0','1','0'][2*row+col],ha='center',va='center',fontsize=23,color='white' if matrix[row,col]>.6 else '#172d44')
ax.set_xticks([0,1],[r'$m_1=2A$',r'$m_2=3A$']);ax.set_yticks([0,1],[r'$M_1=A$',r'$M_2=2A$']);ax.tick_params(length=0)
ax.text(.5,-.40,r'$\gamma=(1,0),\quad A>0,\quad\|c^0\|=\sqrt{5}/2$',transform=ax.transAxes,ha='center',fontsize=16,color='#172d44')
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',ec=color,fc='white',lw=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=16,color='#172d44')
box(.015,.72,.28,.22,'Cutoff coefficient maps\n'+r'$\Theta:\mathbb{C}\to\ell^2,\quad\Gamma:\ell^2\to\mathbb{C}$','#4773a0')
box(.36,.72,.28,.22,'Exact operators\n'+r'$S_0=\Gamma\Theta,\quad E=I-S_0$','#4c8f84')
box(.705,.72,.28,.22,'Finite symbol cancellation\n'+r'$\|E^NBH_\lambda\|\leq C_N R_i^{-2N}$','#8a6f40')
for x in [.30,.645]:ax.annotate('',(x+.055,.83),(x,.83),arrowprops={'arrowstyle':'->','lw':2,'color':'#172d44'})
ax.text(.5,.46,r'$U_i=\left(\sum_{l=0}^{N-1}E^l\Gamma\right)\Theta U_i+E^NBH_\lambda u$',ha='center',fontsize=21,color='#172d44')
ax.text(.5,.25,'Use the radius of the actual family; keep weighted tails in the coefficient operator norm.',ha='center',fontsize=14,color='#414b57')
ax.text(.5,.11,r'$R_i=\lambda^{-\kappa_i},\quad M_j,m_a\leq C\lambda^{-2},\quad 2\kappa_1N-2\geq L$',ha='center',fontsize=19,color='#172d44')
ax.text(.5,-.03,r'Example: $\kappa_1=1/8,\ N=12\ \Longrightarrow\ \lambda^{2\kappa_1N-2}=\lambda$',ha='center',fontsize=16,color='#4773a0')
fig.text(.055,.073,'Proof: Sections2–6,(2.1)–(2.3),(3.1)–(3.5),(4.1)–(4.3). Exact examples: Exercises1,3,4,(7.1).',fontsize=12,color='#414b57')
fig.text(.055,.031,'Hörmander IV,Lemmas27.6.2–27.6.3,printed213–214. No full adaptive symbol is assigned to either numerical panel. Original diagram;CC0.',fontsize=11.5,color='#414b57')
target=Path(__file__).with_name('partition-reconstruction.png')
fig.savefig(target,dpi=150,metadata={'Software':'AN05-L044 reproducible mathematical illustration; CC0'});plt.close(fig);print(target.name)
