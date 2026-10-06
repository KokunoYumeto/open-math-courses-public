"""Exact operator directions and orders in a portrait proof diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
here=Path(__file__).resolve().parent;dest=here/'invariant-fold-transfer.svg'
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans','font.size':16})
fig,ax=plt.subplots(figsize=(7.2,9.6));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
blue='#185c88';orange='#a34e11'
def row(y,boxes,arrows,color):
    centers=[.095,.365,.635,.905]
    for x,label in zip(centers,boxes):
        ax.add_patch(FancyBboxPatch((x-.08,y-.042),.16,.084,
                      boxstyle='round,pad=0.008',fc='#f7f9fb',ec=color,lw=1.5))
        ax.text(x,y,label,ha='center',va='center',fontsize=15)
    for i,label in enumerate(arrows):
        left=centers[i]+.087;right=centers[i+1]-.087
        ax.annotate('',(right,y),(left,y),arrowprops={'arrowstyle':'->','color':color,'lw':1.7})
        ax.text((left+right)/2,y+.054,label,ha='center',va='bottom',fontsize=15,color=color)
ax.text(.5,.97,'Transfer the fold estimate',ha='center',va='top',fontsize=22,weight='bold',color=blue)
ax.text(.02,.885,'Canonical charts: every graph factor has order 0',fontsize=15,color=blue)
row(.79,['model\ninput','Y','X','model\noutput'],[r'$G_Y$',r'$T_j$',r'$G_X$'],blue)
ax.text(.5,.705,r'$B=G_XT_jG_Y,\quad \operatorname{ord}B=m$',ha='center',fontsize=17)
row(.59,['Y','model\ninput','model\noutput','X'],[r'$H_Y$',r'$B$',r'$H_X$'],blue)
ax.text(.5,.505,r'$T_j=H_XBH_Y+S_j$',ha='center',fontsize=18)
ax.text(.5,.467,r'$S_j$ has a smooth localized kernel; (4.4).',ha='center',fontsize=14)
ax.plot([.02,.98],[.42,.42],color='#bbb',lw=1)
ax.text(.02,.375,r'Sobolev reduction: $t=s-m-1/6$',fontsize=17,color=orange)
row(.27,[r'$L^2(Y)$',r'$H^s(Y)$',r'$H^t(X)$',r'$L^2(X)$'],
    ['$C_Y$\norder $-s$','$A_0$\norder $m$','$B_X$\norder $t$'],orange)
ax.text(.5,.185,r'$T=B_XA_0C_Y,\quad \operatorname{ord}T=-1/6$',ha='center',fontsize=17)
ax.text(.5,.127,r'$A_0=C_XTB_Y+S$',ha='center',fontsize=18)
ax.text(.5,.077,r'$B_Y:H^s\to L^2,\quad C_X:L^2\to H^t$',ha='center',fontsize=17)
ax.text(.5,.024,'All supports are localized; both errors are retained.\nExact recovery: (5.4)–(5.6).',ha='center',fontsize=13)
fig.subplots_adjust(left=.035,right=.965,top=.985,bottom=.01)
fig.savefig(dest)
fig.savefig(here/'invariant-fold-transfer.png',dpi=160)
print(dest.name)
