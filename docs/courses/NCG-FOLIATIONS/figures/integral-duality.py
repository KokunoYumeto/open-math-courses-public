"""Reproducible, deliberately schematic scientific diagram for Lemmas 8C.3–8."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Ellipse

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
                     'svg.fonttype':'none','savefig.facecolor':'white'})
fig,axs=plt.subplots(2,2,figsize=(17,11),dpi=160)
blue='#215c90'; green='#247957'; orange='#ae5a15'; grey='#555b65'
for ax in axs.flat:
    ax.set_xlim(0,10);ax.set_ylim(0,7);ax.axis('off')
def title(ax,t):
    ax.text(0,6.8,t,ha='left',va='top',fontsize=16,fontweight='bold',color=blue)
def arrow(ax,a,b,color=grey,label=None):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,
                                lw=1.8,color=color))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.12,label,
                    ha='center',va='bottom',color=color,fontsize=12)

ax=axs[0,0];title(ax,'A. Compact double; the coefficient lives on one face')
ax.add_patch(FancyBboxPatch((.6,2.1),8.7,3.3,boxstyle='round,pad=0,rounding_size=.65',
                            facecolor='#f2f6fa',edgecolor=blue,lw=2))
ax.plot([1.3,8.6],[3.75,3.75],color=grey,ls='--',lw=1.3)
ax.add_patch(Ellipse((4.7,4.55),3,1.05,facecolor='#d4eddf',edgecolor=green,lw=2))
ax.text(4.7,4.55,r'$K\subset\mathrm{int}\,W$',ha='center',va='center',color=green)
ax.text(1.5,5.85,r'$D W=\partial\,\mathrm{round}(W\times[-1,1])$',fontsize=14)
ax.text(1.4,4.03,r'upper face: $E_0-E_1$',color=green)
ax.text(1.4,2.8,r'lower face: $E_1-E_1=0$',color=grey)
ax.text(5.9,3.31,r'collar: $\varphi:E_0\cong E_1$',fontsize=12)
arrow(ax,(4.6,2),(4.6,1.25),label=r'$p_N r$')
ax.text(4.6,.95,r'$V$  (the source $D W$ is compact)',ha='center',fontsize=14)
ax.text(.5,.2,'Lemma 8C.3; (C.c)–(C.e). Rounded-box schematic.',fontsize=11,color=grey)

ax=axs[0,1];title(ax,'B. Carrier independence is a compact bordism')
ax.add_patch(FancyBboxPatch((.7,2),8.6,3.8,boxstyle='round,pad=0,rounding_size=.5',
                            facecolor='#e8eff6',edgecolor=blue,lw=2))
ax.add_patch(FancyBboxPatch((2.25,2.95),5.5,1.9,boxstyle='round,pad=0,rounding_size=.3',
                            facecolor='white',edgecolor=orange,lw=2))
ax.text(5,3.9,r'removed: $W_1\times[-\epsilon,\epsilon]$',ha='center',fontsize=12)
ax.text(5,5.36,r'$W_2\times[-1,1]$',ha='center',fontsize=14)
ax.text(5,2.37,r'$Q$ carries $E_Q-r_Q^*E_1$',ha='center',color=blue)
arrow(ax,(8.55,4.1),(9.65,4.1),blue)
arrow(ax,(1.9,3.65),(2.95,3.65),orange)
ax.text(9.6,4.6,'outer\nnormal',ha='right',fontsize=11,color=blue)
ax.text(3.8,3.08,'inner normal points into the removed box',fontsize=10.5,color=orange)
ax.text(.8,1.2,r'boundary: $(D W_2,y_{D W_2})-(D W_1,y_{D W_1})$',fontsize=13)
ax.text(.8,.65,r'$E_0$ above; $E_1$ below; glue with $\varphi$ outside $W_1$.',fontsize=12)
ax.text(.5,.2,'Lemma 8C.4; (C.f). No noncompact geometric cycle.',fontsize=11,color=grey)

ax=axs[1,0];title(ax,'C. The embedding bordism recovers the native cycle')
ax.add_patch(Ellipse((5,4.3),8.8,3.6,facecolor='#e8eff6',edgecolor=blue,lw=2))
ax.add_patch(Ellipse((4.7,4.3),3.6,1.5,facecolor='white',edgecolor=orange,lw=2))
ax.text(4.7,4.3,r'removed disk of $\nu\oplus\mathbb{C}\oplus\mathbb{R}$',ha='center',fontsize=10.5)
ax.text(5,5.55,r'$W\subset D^3\times Z$',ha='center',color=blue)
arrow(ax,(6.5,4.3),(9.35,4.3),green)
ax.text(8.1,4.7,r'$e:[\epsilon,1]\times M$',ha='center',fontsize=11,color=green)
ax.text(.6,2.2,r'outer: $S^2\times Z$; reduced north class $n_Z{}_!h_!x$',fontsize=12)
ax.text(.6,1.65,r'inner: $S(\nu\oplus\mathbb{C}\oplus\mathbb{R})$; full opposite',fontsize=12)
ax.text(.6,1.1,r'$e_!\mathrm{pr}_M^*x$ extends the exact two boundary coefficients.',fontsize=12)
ax.text(.6,.57,r'disk correction + even modification  $\Longrightarrow$  $[M,x,fh]=[Z,h_!x,f]$',fontsize=12)
ax.text(.5,.2,'Lemma 8C.5; (C.g). Schematic; removed-disk rank is rank(ν)+3.',fontsize=10.7,color=grey)

ax=axs[1,1];title(ax,'D. Two inverse identities, both integral degrees')
ax.text(.8,5.55,r'$\mathcal{C}_{j,\tau}(V)$',fontsize=20,color=blue)
ax.text(6.15,5.55,r'$K_c^{j+d}(V)$',fontsize=20,color=green)
arrow(ax,(3.45,5.6),(6.05,5.6),label=r'$\kappa$')
arrow(ax,(6.05,4.75),(3.45,4.75),label=r'$\Gamma_p(x)=\beta_p(xB_p)$')
ax.text(.8,3.8,r'$\kappa\Gamma_p(x)=(xB_p)A_p=x$',fontsize=17,color=green)
ax.text(.8,2.95,r'$\Gamma_p\kappa(c)=\beta_N((\kappa c)B_N)$',fontsize=16,color=blue)
ax.text(4,2.35,r'$=\beta_N(j_!E)=c$',fontsize=16,color=blue)
ax.text(.8,1.6,r'$p=j+d\;({\rm mod}\;2)$; $N\equiv p$; normal rank $n+N-m$ is even.',fontsize=12)
ax.text(.8,1.04,'Full module evaluations preserve lines, torsion and stable grading.',fontsize=12)
ax.text(.8,.55,'Relations used: sum, compact bordism, even spin-c modification.',fontsize=12)
ax.text(.5,.2,'Lemmas 8C.6–7; Theorem 8C.8; (C.h)–(C.l).',fontsize=11,color=grey)

fig.suptitle('Integral native manifold duality: compact carriers and geometric normalization',
             fontsize=20,y=.988,color=blue)
fig.subplots_adjust(top=.945,bottom=.02,left=.035,right=.98,hspace=.12,wspace=.12)
fig.savefig(HERE/'integral-duality.svg',metadata={'Date':None,'Creator':'Reproducible matplotlib source'})
fig.savefig(HERE/'integral-duality.png',dpi=160)
print('Rendered integral-duality.svg and integral-duality.png (2720×1760).')
