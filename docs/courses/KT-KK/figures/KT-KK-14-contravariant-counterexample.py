"""Exact contravariant obstruction in Theorem8B.1; reproducible original diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                    'mathtext.fontset':'dejavusans','svg.fonttype':'none'})
ink,blue,red,green='#172a3a','#1678a5','#bd512c','#347f53'
fig,axs=plt.subplots(3,1,figsize=(8.0,6.7),facecolor='white',
                    gridspec_kw={'height_ratios':[.8,1.1,1.0],'hspace':.35})
for ax in axs:ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(ax,x,y,w,h,text,color=blue,size=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',
                  facecolor='#f7f9fb',edgecolor=color,lw=1.3))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,
            color=ink,linespacing=1.45)
def arrow(ax,a,b,label='',dy=.1):
    ax.annotate('',b,a,arrowprops={'arrowstyle':'->','color':ink,'lw':1.5})
    ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha='center',
            va='center',fontsize=11,color=ink)
ax=axs[0]
ax.text(.5,.98,'One unital semisplit extension; all three algebras are sigma-unital',
        ha='center',fontsize=12.5,color=ink)
for x,txt in [(.10,r'$J=\mathcal{K}(H)$'),(.42,r'$E$'),(.74,r'$B$')]:
    box(ax,x,.30,.16,.37,txt,blue,12)
ax.text(.03,.485,'0',ha='center',va='center')
ax.text(.97,.485,'0',ha='center',va='center')
arrow(ax,(.05,.485),(.09,.485))
arrow(ax,(.28,.485),(.40,.485),r'$j$')
arrow(ax,(.60,.485),(.72,.485),r'$\pi$')
arrow(ax,(.91,.485),(.95,.485))
ax.text(.5,.03,r'$H=\ell^2(\mathbb{N}_0)$; $B$ has no nonzero separable Hilbert-space representation.',
        ha='center',fontsize=10.5,color=ink)
ax=axs[1]
ax.text(.5,.98,'Contravariant scalar sequence: exactness is impossible',ha='center',
        fontsize=12.5,color=ink)
box(ax,.025,.39,.27,.37,r'$KK_h(E,\mathbb{C})=0$',blue,11.5)
box(ax,.365,.39,.27,.37,'\n'.join([r'$KK_h(J,\mathbb{C})\ni z$',r'$p_0^*z=1$']),red,11.5)
box(ax,.705,.39,.27,.37,r'$KK_h^1(B,\mathbb{C})=0$',blue,11)
arrow(ax,(.31,.575),(.35,.575),r'$j^*$')
arrow(ax,(.65,.575),(.69,.575),r'$\delta$')
ax.text(.5,.18,r'$\mathrm{im}(j^*)=\{0\}$; $\ker(\delta)=KK_h(J,\mathbb{C})\ne0$.',
        ha='center',fontsize=11.5,color=red)
ax.text(.5,.025,'Theorem 8B.1; the ideal class is the compact action on an even Hilbert space (CC.8).',
        ha='center',fontsize=10.5,color=ink)
ax=axs[2]
ax.text(.5,.98,'The canonical ideal / cone test also fails',ha='center',
        fontsize=12.5,color=ink)
box(ax,.045,.38,.35,.35,r'$KK_h(C_\pi,\mathbb{C})=0$',blue,12)
box(ax,.605,.38,.35,.35,r'$KK_h(J,\mathbb{C})\ni z\ne0$',red,11.5)
arrow(ax,(.415,.555),(.585,.555),r'$j_{\rm cone}^*$')
ax.text(.5,.18,r'$0\to SB\to C_\pi\to E\to0$; all separable $SB$-representations vanish.',
        ha='center',fontsize=11,color=ink)
ax.text(.5,.025,'The covariant exact sequences and separable extension formulas keep their proved hypotheses.',
        ha='center',fontsize=10.5,color=green)
fig.subplots_adjust(left=.02,right=.98,bottom=.035,top=.97)
fig.savefig(base/'KT-KK-14-contravariant-counterexample.png',dpi=220)
fig.savefig(base/'KT-KK-14-contravariant-counterexample.svg')
plt.close(fig)
