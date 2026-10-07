"""Reproducible diagram of Lesson12 Theorem8A.1, sized for legible print."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                    'mathtext.fontset':'dejavusans','svg.fonttype':'none'})
ink,blue,orange,green='#172a3a','#1678a5','#d66a24','#347f53'
def box(ax,xy,w,h,txt,color=blue,size=11):
    ax.add_patch(FancyBboxPatch(xy,w,h,boxstyle='round,pad=.012',
                  facecolor='#f7f9fb',edgecolor=color,lw=1.2))
    ax.text(xy[0]+w/2,xy[1]+h/2,txt,ha='center',va='center',
            fontsize=size,color=ink,linespacing=1.5)
def arrow(ax,start,end,label='',offset=(0,.05),size=11):
    ax.annotate('',end,start,arrowprops={'arrowstyle':'->','color':ink,'lw':1.4})
    ax.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],
            label,ha='center',va='center',fontsize=size,color=ink)
fig,axs=plt.subplots(3,1,figsize=(7.8,7.0),facecolor='white',
                    gridspec_kw={'height_ratios':[.8,1.0,1.5],'hspace':.23})
for ax in axs:ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax=axs[0]
ax.text(.5,.96,r'The unital field algebra $A_\ell$ (CB.1)',ha='center',fontsize=13,color=ink)
box(ax,(.025,.22),.40,.53,
    '\n'.join(['Diagonal fields',r'$C_b(\mathbb{R},\mathcal{B}(H))$']),blue,12)
box(ax,(.575,.22),.40,.53,
    '\n'.join(['Off-diagonal fields',r'$C_0(\mathbb{R},\mathcal{K}(H))$']),orange,12)
ax.text(.5,.025,r'$H=\ell^2(\mathbb{N})$; all fields are operator-norm-continuous.',
        ha='center',fontsize=10.5,color=ink)
ax=axs[1]
ax.text(.5,.98,'Every scalar cycle becomes degenerate (CB.16)',ha='center',fontsize=12.5,color=ink)
box(ax,(.025,.32),.35,.43,
    '\n'.join([r'$F_\infty=\mathrm{diag}(T_+,T_-)\otimes1_H$',
               r'$T_\pm^*=T_\pm,\quad T_\pm^2=1$']),blue,10.5)
box(ax,(.475,.32),.50,.43,
    '\n'.join([r'$G_t=\mathrm{diag}(T_+,V_tT_-V_t^*)\otimes1_H$',
               r'$G_1=\mathrm{diag}(T_+,T_+)\otimes1_H$']),green,10.5)
arrow(ax,(.39,.54),(.46,.54),r'$V_t$',offset=(0,.13))
ax.text(.5,.13,r'$V_t=e^{itL}$, even; $\|L\|\leq\pi$; $V_0=1$; $V_1T_-V_1^*=T_+$.',
        ha='center',fontsize=10.5,color=ink)
ax.text(.5,.015,r'$(V_t-1)\psi(f)$ is compact and continuous in $t$ (Lemmas 8A.2–8A.5).',
        ha='center',fontsize=10,color=ink)
ax=axs[2]
ax.text(.5,.98,'Zero Bott image and a nonzero Hardy detector',ha='center',fontsize=12.5,color=ink)
box(ax,(.025,.61),.38,.25,
    '\n'.join([r'$KK_h(A_\ell,\mathbb{C})=0$', 'every scalar cycle is null']),blue,11)
box(ax,(.595,.61),.38,.25,
    '\n'.join([r'$w\in KK_h(A_\ell,SCl_1),\quad w\ne0$',r'$F_w=(2P-1)\otimes L_e$']),orange,10.5)
arrow(ax,(.425,.74),(.575,.74),r'$\mathfrak{b}_1$: image $\{0\}$',offset=(0,.10),size=10)
box(ax,(.025,.20),.38,.24,
    '\n'.join([r'$v\in KK_h(C(\mathbb{T}),Cl_1)$',r'$\mathrm{index}(PUP)=-1$']),green,11)
box(ax,(.595,.20),.38,.24,
    '\n'.join([r'$\tau_S(v)\in KK_h(SC(\mathbb{T}),SCl_1)$',
               r'$j^*w=\tau_S(v)\ne0$']),green,10)
arrow(ax,(.425,.32),(.575,.32),r'$\tau_S$',offset=(0,.10),size=12)
arrow(ax,(.785,.59),(.785,.46),r'$j^*$',offset=(.055,0),size=12)
ax.text(.5,.08,r'$j(f\otimes g)(r)=f(r)g(U)$ (CB.19–CB.20).',ha='center',fontsize=10.5,color=ink)
ax.text(.5,.01,r'$Ue_n=e_{n+1}$; $P$ selects $n\geq0$; $\tau_S$ uses Proposition 8.2.',
        ha='center',fontsize=10.5,color=ink)
fig.subplots_adjust(top=.975,bottom=.035,left=.025,right=.975)
fig.savefig(base/'KT-KK-12-coefficient-bott-counterexample.png',dpi=220)
fig.savefig(base/'KT-KK-12-coefficient-bott-counterexample.svg')
plt.close(fig)
