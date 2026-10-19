"""Exact algebraic comparison arrows; no measure-space geometry is depicted."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

DEST=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':23,
 'svg.fonttype':'path','svg.hashsalt':'trace-scaling-flow-comparison-v1'})
fig,ax=plt.subplots(figsize=(7.2,10.4),layout='constrained')
ax.set_xlim(0,10);ax.set_ylim(0,14.4);ax.axis('off')
ax.text(5,14.0,'Comparing trace-scaling flows',ha='center',fontsize=24,color='#154b65')

def card(bottom,height,title,color):
 ax.add_patch(FancyBboxPatch((.25,bottom),9.5,height,boxstyle='round,pad=.02',facecolor='#f5f8f7',edgecolor=color,linewidth=2))
 ax.text(5,bottom+height-.52,title,ha='center',fontsize=23,color=color)

card(9.6,3.7,'The common trace multiplier','#154b65')
ax.text(1.8,11.9,r'$x$',ha='center',fontsize=29)
ax.text(8.2,11.9,r'$T_t x$',ha='center',fontsize=29)
ax.add_patch(FancyArrowPatch((2.4,12.0),(7.4,12.0),arrowstyle='-|>',mutation_scale=27,linewidth=2,color='#154b65'))
ax.text(5,12.22,r'$T_t$',ha='center',fontsize=23)
ax.text(5,10.95,r'$m_1(t,x)=m_2(t,x)=e^{-t}/J_t(x)$',ha='center',fontsize=23)
ax.text(5,10.15,'Proposition 3.1',ha='center',fontsize=21,color='#154b65')

card(5.0,4.0,'A relative correction','#146b59')
ax.text(5,7.7,r'$f(x)\in\ker m=\overline{\mathrm{Inn}(N)}$',ha='center',fontsize=22)
ax.text(5,6.85,r'$\gamma_t=\Psi\theta_t^1\Psi^{-1}$',ha='center',fontsize=26)
ax.text(5,6.05,r'$\theta_t^2=\mathrm{Ad}(U_t)\gamma_t$',ha='center',fontsize=25)
ax.text(5,5.38,r'$U_{s+t}=U_s\gamma_s(U_t)$',ha='center',fontsize=24)
ax.text(5,4.43,'Theorem 4.1',ha='center',fontsize=21,color='#146b59')

card(.6,3.35,'The normal crossed-product lift','#6a4b96')
ax.text(5,2.72,r'$\lambda_t^1\ \longmapsto\ U_t^*\lambda_t^2$',ha='center',fontsize=29)
ax.text(5,1.9,r'$b\ \longmapsto\ \Psi(b)$',ha='center',fontsize=26)
ax.text(5,1.05,'Proposition 5.1',ha='center',fontsize=21,color='#6a4b96')

for top,bottom in [(9.54,9.12),(4.27,4.0)]:
 ax.add_patch(FancyArrowPatch((5,top),(5,bottom),arrowstyle='-|>',mutation_scale=23,linewidth=2,color='#4c5965'))
fig.savefig(DEST/'trace-scaling-flow-comparison.svg',metadata={'Date':None,'Creator':'Matplotlib','Description':'Exact common-multiplier, cocycle-conjugacy and normal crossed-product arrows in Propositions 3.1, 5.1 and Theorem 4.1.'})
fig.savefig(DEST/'trace-scaling-flow-comparison.png',dpi=190,metadata={'Software':'Matplotlib'})
plt.close(fig)
