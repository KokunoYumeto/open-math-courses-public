"""Exact original base directions; the physical wave frequency remains explicit."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(14,6))
fig.subplots_adjust(left=.05,right=.98,bottom=.29,top=.80,wspace=.28)
fig.suptitle('Twelve rational directions in three perpendicular planes',fontsize=18,weight='bold')
specs=[
    ('The 12-plane',r'$\xi_1$',r'$\xi_2$',[(3,4),(3,-4)],r'$A_\xi=e_3$'),
    ('The 23-plane',r'$\xi_2$',r'$\xi_3$',[(3,4),(3,-4)],r'$A_\xi=e_1$'),
    ('The 13-plane',r'$\xi_1$',r'$\xi_3$',[(4,3),(-4,3)],r'$A_\xi=e_2$')]
for ax,(title,xlab,ylab,pairs,pol) in zip(axes,specs):
    ax.add_patch(Circle((0,0),1,fill=False,lw=1,color='#9ea8b0'))
    ax.axhline(0,color='#a7b1b8',lw=.6);ax.axvline(0,color='#a7b1b8',lw=.6)
    for j,(x,y) in enumerate(pairs):
        color=['#246d96','#26826e'][j]
        for sign in [1,-1]:
            xx,yy=sign*x/5,sign*y/5
            ax.annotate('',xy=(xx,yy),xytext=(0,0),arrowprops=dict(arrowstyle='-|>',color=color,lw=2))
            ax.plot(xx,yy,'o',color=color,ms=4)
            label=rf'$({sign*x}/5,{sign*y}/5)$'
            ax.text(xx*1.13,yy*1.13,label,ha='center',va='center',fontsize=10)
    ax.set(xlim=(-1.35,1.35),ylim=(-1.3,1.3),aspect='equal',xlabel=xlab,ylabel=ylab)
    ax.set_title(title+'\n'+pol,fontsize=13)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    ax.spines[['top','right']].set_visible(False)
fig.text(.5,.13,r'Each pair and its negatives remain distinct.  $\sum_{i,\pm}(I_3-\xi_{i,\pm}\otimes\xi_{i,\pm})=4I_3$.',ha='center',fontsize=13)
fig.text(.5,.075,r'Original cube period $L$: physical wave vector $(2\pi\lambda/L)\xi$; polarization $B_\xi=(A_\xi+i\,\xi\times A_\xi)/\sqrt{2}$.',ha='center',fontsize=12)
fig.text(.5,.025,'Proof: BG1–BG3, BG11–BG19. Source comparison: Buckmaster–Vicol, arXiv:1709.10033v4, original propositions p:Beltrami and p:split.',ha='center',fontsize=10)
fig.savefig(out/'original-rational-beltrami-directions.png',dpi=160)
fig.savefig(out/'original-rational-beltrami-directions.svg')
