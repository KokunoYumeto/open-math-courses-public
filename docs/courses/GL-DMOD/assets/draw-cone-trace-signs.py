from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

ROOT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,10),facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,16);ax.set_ylim(0,10);ax.axis('off')
ax.text(8,9.55,'The relative connecting sign and the holomorphic trace',ha='center',fontsize=23,weight='bold',color='#152238')
ax.text(8,9.13,'Ordinary coefficient lines; antiholomorphic factors first; input frame ordered',ha='center',fontsize=15,color='#41536c')

def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06',facecolor='white',edgecolor=color,linewidth=2))
    ax.text(x+w/2,y+h-.37,title,ha='center',fontsize=17,weight='bold',color=color)
    for j,line in enumerate(lines):ax.text(x+w/2,y+h-.92-j*.5,line,ha='center',va='center',fontsize=17,color='#17263d')

box(.5,5.57,7.15,2.94,'V.1  The specified relative cone',[
    r'$C_Z^q=I^q(M)\oplus I^{q-1}(M\setminus Z)$',
    r'$d(a,b)=(\delta a,ra-\delta b)$',
    r'$(0,-f)+d(F,0)=(\delta F,0)$',
    'Positive connecting class; extension only when it exists.'
],'#305b9b')
box(8.35,5.57,7.15,2.94,'V.2, V.6  Ordered normal classes',[
    r'$\varphi=f_1\cdots f_N,\qquad\epsilon=(-1)^{\sum_{i<j}q_i r_j}$',
    r'$\mathrm{top\ cube}=r_N(-1)^N\varphi$',
    r'$r_N=(-1)^{N(N-1)/2}$',
    'Normalized class: the ordered lines supply r_N once.'
],'#305b9b')
box(.5,1.81,7.15,2.94,'V.3, V.5  Cup before the trace shift',[
    r'$|a|=|b|=N,\qquad c(a,b)=(\alpha\wedge\beta)\otimes(\eta_A\wedge\eta_B)$',
    r'$J(c(a,b))=(-1)^{N^2}J(a)\wedge J(b)$',
    r'$J(\alpha\otimes\eta)=\alpha\wedge\eta$',
    'The intermediate coefficient precedes the remaining one.'
],'#177653')
box(8.35,1.81,7.15,2.94,'V.4, V.5  The shifted trace',[
    r'$\mathrm{Tr}_q=(-1)^{N(q-N)}I_q$',
    r'$\mathrm{Tr}_{q+1}(-1)^N\delta=\delta\,\mathrm{Tr}_q$',
    r'$\mathrm{Tr}_{2N}c(a,b)=J_{\rm out}^{-1}p_*(J(a)\wedge J(b))$',
    'The two between-kernel parities cancel; residue scalar is 1.'
],'#177653')
for start,end in [((7.8,7.05),(8.2,7.05)),((4.08,5.42),(4.08,4.91)),((11.92,5.42),(11.92,4.91)),((7.8,3.28),(8.2,3.28))]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=20,color='#60728a',linewidth=2))
ax.text(8,1.3,'Full resolution and controlled excision: §5.34. Unrestricted-input collar and action: §5.37.',ha='center',fontsize=13.5,color='#9f4825')
ax.text(8,.88,'Exact proof: §5.35, V.1–V.6. The normalized top cube includes the ordered-line factor r_N.',ha='center',fontsize=12.8,color='#41536c')
ax.text(8,.45,'Free source target: Kashiwara–Schapira, Micro-hyperbolic systems, §3.1.  Original diagram and proof: CC0.',ha='center',fontsize=12.8,color='#41536c')
fig.savefig(ROOT/'cone-trace-signs.png',dpi=150)
fig.savefig(ROOT/'cone-trace-signs.svg',metadata={'Date':None})

