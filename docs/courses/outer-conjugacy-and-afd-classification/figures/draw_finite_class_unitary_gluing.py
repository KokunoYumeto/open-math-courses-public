"""Exact four-point finite-class gluing diagram for Proposition 5.1."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams['svg.hashsalt']='oa-classify-finite-class-unitary-gluing-v1'
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(6.5,10.7));fig.patch.set_facecolor('#fbfcff')
ax.set(xlim=(0,6.5),ylim=(0,10.7));ax.axis('off')
def text(x,y,s,size=18,**kw):ax.text(x,y,s,ha='center',va='center',fontsize=size,color='#17304b',**kw)
def box(x,y,w,h):ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',facecolor='#eaf2ff',edgecolor='#476ea1',linewidth=2))
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color='#476ea1',linewidth=2))
text(3.25,10.1,'Merge finite classes',23);text(3.25,9.65,'Keep old unitary comparisons exactly',17)
box(.35,7.8,2.65,1.2);box(3.5,7.8,2.65,1.2)
text(1.68,8.62,r'$\{0,1\}$',21);text(4.83,8.62,r'$\{2,3\}$',21)
text(1.68,8.14,r'root $0$: retain $W_{10}$',17);text(4.83,8.14,r'root $2$: retain $W_{32}$',17)
arrow((1.68,7.7),(2.45,6.85));arrow((4.83,7.7),(4.05,6.85))
box(.35,4.95,5.8,1.85)
text(3.25,6.46,r'$\{0,1,2,3\}$, root $0$',21)
text(3.25,5.95,r'$v_0=1,\quad v_1=W_{10}$',21)
text(3.25,5.42,r'$v_2$ selected; $v_3=W_{32}\beta_{32}(v_2)$',18)
arrow((3.25,4.8),(3.25,4.2))
text(3.25,3.78,'Every new comparison',19)
text(3.25,3.22,r'$W^{\mathrm{new}}_{xy}=v_x\beta_{xy}(v_y^*)$',22)
box(.35,1.15,5.8,1.35)
text(3.25,2.08,r'$W^{\mathrm{new}}_{10}=W_{10}$',22)
text(3.25,1.52,r'$W^{\mathrm{new}}_{32}=W_{32}$',22)
text(3.25,.58,'Finite example of equations (5.3)–(5.8)',16)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig(out/'finite-class-unitary-gluing.svg',metadata={'Date':None,'Creator':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
fig.savefig(out/'finite-class-unitary-gluing.png',dpi=180,metadata={'Software':'OA-CLASSIFY Writing AI; GPT-6.1 Sol Ultra; original CC0'})
plt.close(fig)
