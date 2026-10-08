"""Reproducible mathematical diagrams; no external artwork or fonts copied."""
from pathlib import Path
import json,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
import numpy as np
HERE=Path(__file__).resolve().parent
OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none','svg.hashsalt':'OA-FLOW-cf-foundations-v1'})
fig,axes=plt.subplots(1,2,figsize=(13,6.2),gridspec_kw={'width_ratios':[1,1.3]})
ax=axes[0];t=np.linspace(0,2*np.pi,601)
ax.plot(np.cos(t),np.sin(t),color='#495d75',lw=1.5,label='unit circle')
ax.axhline(0,color='#cad1d8',lw=.7);ax.axvline(0,color='#cad1d8',lw=.7)
delta=.25
ax.add_patch(Rectangle((1-delta,-delta),2*delta,2*delta,facecolor='#80c5a5',alpha=.3,edgecolor='#16714c',lw=2))
for x,y,label,offset in [(1,0,'1',(1.1,.2)),(0,1,'i',(.12,1.06)),(-1,0,'−1',(-1.2,.13))]:
 ax.scatter([x],[y],s=62,c='#16714c' if x==1 else '#495d75',zorder=4)
 ax.text(*offset,label,fontsize=13)
ax.scatter([1],[0],s=135,facecolors='none',edgecolors='#16714c',lw=2,zorder=5)
ax.text(-1.22,-.7,'Matrix example: u = diag(1, i, −1)\nCut at λ = 1 isolates E₁₁.\nδ = 1/4; ε = 6/5.',ha='left',va='top')
ax.set(xlim=(-1.35,1.4),ylim=(-1.25,1.3),xlabel='Re u: scalar coordinate a',ylabel='Im u: scalar coordinate b')
ax.set_aspect('equal');ax.set_title('A continuous cut and its support',pad=13)
ax=axes[1];ax.set_axis_off();ax.set(xlim=(0,1),ylim=(0,1));ax.set_title('Finite central assembly',pad=13)
for y,number in [(.78,'1'),(.57,'2'),(.36,'N')]:
 ax.add_patch(Rectangle((.04,y-.05),.21,.13,facecolor='#e4eaf0',edgecolor='#495d75'))
 ax.text(.145,y+.015,f'$z_{number} H$',ha='center',va='center')
 ax.add_patch(Rectangle((.39,y-.05),.23,.13,facecolor='#c5e6d7',edgecolor='#16714c'))
 ax.text(.505,y+.015,f'$z_{number}p_{number} H$',ha='center',va='center')
 ax.add_patch(FancyArrowPatch((.26,y+.015),(.38,y+.015),arrowstyle='->',mutation_scale=14,color='#495d75'))
 ax.text(.66,y+.015,f'central support $=z_{number}$',va='center')
ax.text(.32,.28,'Each selected block: ‖(u − λⱼ)zⱼpⱼ‖ ≤ 2δ',ha='center',va='center')
ax.text(.5,.17,'e = Σ zⱼpⱼ     z(e) = Σ zⱼ = 1',ha='center',fontsize=12,color='#16714c')
ax.text(.5,.065,'‖Ad(u)|eMe − id‖ ≤ 4δ < ε',ha='center',fontsize=12,color='#16714c')
fig.suptitle('Small full fixed corners: localization → central cuts → norm bound',fontsize=14,y=.98)
fig.tight_layout(rect=[0,.05,1,.94])
fig.savefig(OUT/'small-full-corner.svg',bbox_inches='tight',metadata={'Date':None});fig.savefig(OUT/'small-full-corner.png',dpi=160,bbox_inches='tight');plt.close(fig)
fig,ax=plt.subplots(figsize=(13,3.6));ax.set_axis_off();ax.set(xlim=(0,1),ylim=(0,1))
nodes=[(.11,.55,'§1–2\nNorm separation\nResolvent / radius'),(.36,.55,'§3–5\nLaplace inverse\nCharacters / density'),(.62,.55,'§6–7\nCalculus / positivity\nF1 + abstract F2'),(.87,.55,'§8\nHilbert / adjoints\nF3 + concrete F2')]
for x,y,label in nodes:
 ax.add_patch(Rectangle((x-.105,y-.2),.21,.4,facecolor='#e4eaf0',edgecolor='#495d75',lw=1.5))
 ax.text(x,y,label,ha='center',va='center')
for a,b in zip(nodes,nodes[1:]):
 ax.add_patch(FancyArrowPatch((a[0]+.107,.55),(b[0]-.107,.55),arrowstyle='->',mutation_scale=16,color='#16714c',lw=1.7))
ax.text(.5,.15,'All nodes contain local proofs; no citation stands in for an edge.',ha='center',color='#16714c')
ax.set_title('A complete local provider for the L34 inputs',fontsize=14,pad=10)
fig.tight_layout();fig.savefig(OUT/'foundation-proof-route.svg',metadata={'Date':None});fig.savefig(OUT/'foundation-proof-route.png',dpi=160);plt.close(fig)
(OUT/'figure-data.json').write_text(json.dumps({'matrix_unitary_eigenvalues':[[1,0],[0,1],[-1,0]],'selected_centre':[1,0],'delta':.25,'epsilon':1.2,'cut_square':[[.75,-.25],[1.25,.25]],'localization_bound':.5,'commutator_bound':1,'central_assembly':'schematic finite arbitrary-M blocks, not a spectral measure','sources':['L34-scope-completion-supplement.md Section 1','minimal-CF-Hilbert-provider.md Sections 1–8'],'external_artwork':False,'blender':'Not useful for this planar exact construction.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Rendered two SVG/PNG diagrams with exact proof constants.')
