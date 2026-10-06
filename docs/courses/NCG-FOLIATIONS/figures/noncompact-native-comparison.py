"""Reproducible exact-coordinate proof diagram; no numerical evidence substitutes for proof."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none',
                     'axes.titleweight':'bold','mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(17,15),dpi=160,facecolor='#fbfcff')
fig.suptitle('The whole noncompact native comparison',fontsize=25,fontweight='bold',y=.969)
fig.text(.5,.937,'One global geometry · one completed interval module · two actual native inverse identities',
         ha='center',fontsize=13,color='#334155')
gs=fig.add_gridspec(2,2,left=.065,right=.965,bottom=.14,top=.89,hspace=.60,wspace=.19)
blue='#2563eb';green='#047857';orange='#d97706';red='#b91c1c';gray='#475569'

ax=fig.add_subplot(gs[0,0]);ax.set_facecolor('white')
x=np.linspace(-5,5,1201);a=1/(1+x*x)
ax.fill_between(x,-a,a,color='#dbeafe',alpha=.7)
ax.plot(x,a,'--',color=blue,lw=2,label=r'$|w|<a(x),\quad a(x)=(1+x^2)^{-1}$')
ax.plot(x,-a,'--',color=blue,lw=2)
for v,col in [(1,green),(4,orange),(-1,green),(-4,orange)]:
 w=v/np.sqrt(1+v*v/a**2)
 ax.plot(x,w,color=col,lw=1.4,alpha=.83,label=rf'$v={v}$' if v>0 else None)
ax.axhline(0,color='#94a3b8',lw=.7)
ax.set(xlim=(-5,5),ylim=(-1.12,1.12),xlabel=r'noncompact base $x$',ylabel=r'compressed fibre $w$')
ax.set_title('A. Positive radius; no global lower bound',loc='left',fontsize=14,pad=10)
ax.legend(loc='upper right',fontsize=10,framealpha=.94)
ax.text(.02,.06,r'$q_a(x,v)=\left(x,\;v/\sqrt{1+v^2/a(x)^2}\right)$',
        transform=ax.transAxes,fontsize=14,bbox=dict(facecolor='white',alpha=.94,edgecolor='none'))
ax.text(.02,.90,'Exact trivial-line example\nDisk boundary is not included',
        transform=ax.transAxes,fontsize=10,color=gray,va='top')
ax.text(.5,-.26,'Lemma 8D.2; Exercise 93. Compact level sets stay compact\nin the joint interval image, even when a(x) tends to zero.',
        transform=ax.transAxes,ha='center',va='top',fontsize=10.5,color=gray)

ax=fig.add_subplot(gs[0,1]);ax.set_facecolor('white')
ax.set_title('B. Signed transverse deformation',loc='left',fontsize=14,pad=10)
ax.set(xlim=(-1.65,1.65),ylim=(-1.15,1.15),xlabel=r'transverse base $y$',ylabel=r'disk coordinate $t$')
ax.axhline(0,color='#cbd5e1',lw=.7);ax.axvline(0,color='#cbd5e1',lw=.7)
for s,start,col in [(0,(-1.,-.60),blue),(.5,(.1,-.6),green),(1,(1.3,-.6),orange)]:
 dy=-s*.96;dt=.96
 end=(start[0]+dy,start[1]+dt)
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=16,lw=2.5,color=col))
 ax.plot([start[0]],[start[1]],'o',ms=4,color=col)
 ax.text(end[0]+.06,end[1]+.05,rf'$s={s:g}$',color=col,fontsize=12)
ax.text(.05,.88,r'$d^\perp h_s=dy+s\,dt,\qquad \ker(d^\perp h_s)\ni\partial_t-s\partial_y$',
        transform=ax.transAxes,fontsize=12.5)
ax.text(.04,.11,r'$\chi(\eta,t)=(0,-t,\eta_1,\eta_2),\quad h_s=(x,y+st)$',
        transform=ax.transAxes,fontsize=12)
ax.text(.04,.035,r'$de\,L_1(v,k)=dJk+v$',transform=ax.transAxes,fontsize=13,color=red)
ax.text(.5,-.26,'Lemma 8D.3; Exercise 92. Exact translation model in disk coordinates.\nThe retained directions are x, eta_1, eta_2. Every arrow parameter h remains.',
        transform=ax.transAxes,ha='center',va='top',fontsize=10.5,color=gray)

ax=fig.add_subplot(gs[1,0]);ax.axis('off')
ax.set_title('C. Compact defects before endpoint evaluation',loc='left',fontsize=14,pad=10)
ax.text(.04,.87,r'$\mathcal{E}$ over $C([0,1],A)\widehat\otimes C_N$',fontsize=17,color=blue)
ax.text(.04,.69,r'$Q=J_\chi^*\operatorname{diag}(Q_i)J_\chi,\qquad\|Q\|\leq1$',fontsize=17)
ax.text(.04,.52,r'$c(Q^2-1),\;[Q,c]\in\mathcal{K}(\mathcal{E})$',fontsize=17)
ax.text(.04,.42,r'$c\in C_0([0,1]\times E)$: compact support meets finitely many buffers.',
        fontsize=10.8,color=gray)
ax.text(.04,.26,r'$d_E\,\ell_{\rm an}\ \longleftrightarrow\ g_!\,A_N$',fontsize=20,color=green)
ax.text(.04,.10,'Both creation errors: finite rectangular compact kernels\n+ the uniform L2 Euclidean tail bound (D.l).',fontsize=12,color=gray)
ax.text(.04,-.10,'Lemma 8D.4. This is one actual homotopy on one completed module.\nNo family of separate endpoint KK tests replaces it.',fontsize=10.5,color=gray)

ax=fig.add_subplot(gs[1,1]);ax.axis('off')
ax.set_title('D. Full compact carrier and both inverse maps',loc='left',fontsize=14,pad=10)
positions={'native':(.17,.73),'base':(.80,.73),'A':(.80,.27)}
labels={'native':r'$\mathcal{C}_j^{\rm native}$','base':r'$K_c^{j+d}(V)$','A':r'$K_j(A)$'}
for key,p in positions.items():
 ax.text(*p,labels[key],ha='center',va='center',fontsize=19,
         bbox=dict(boxstyle='round,pad=.38',facecolor='white',edgecolor='#cbd5e1',lw=1.5))
def arrow(p,q,text,pos,col=blue):
 ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=16,lw=1.8,color=col))
 ax.text(*pos,text,ha='center',fontsize=12,color=col)
arrow((.34,.78),(.62,.78),r'$\kappa R$',(.48,.85))
arrow((.62,.67),(.34,.67),r'$I\Gamma_p$',(.48,.55),green)
arrow((.87,.61),(.87,.39),r'$\ell=s_d\Theta_H$',(.94,.49))
arrow((.70,.39),(.70,.61),r'$\delta=s_dD_H$',(.55,.49),green)
arrow((.27,.62),(.63,.29),r'$\mu$',(.39,.33),orange)
ax.text(.07,.05,r'$\mu(I\Gamma_p(y\delta))=y,\qquad I\Gamma_p((\kappa Rc)\ell\delta)=c$',
        fontsize=12)
ax.text(.07,-.07,r'$p=j+d\ ({\rm mod}\ 2),\quad s_d=(-1)^{\lfloor d/2\rfloor},\quad j=0,1$',
        fontsize=12,color=red)
ax.text(.07,-.18,'Theorems 8D.5, 8D.7, 8D.8; R1 Theorem 8C.8.\nAll geometric carrier sources are closed compact; V remains noncompact.',
        fontsize=10.5,color=gray)

fig.text(.065,.031,'Figure 8D.1 · exact examples and proof diagram · CC0 1.0 · noncompact-native-comparison.py',
         fontsize=10.5,color=gray)
fig.text(.965,.031,'Human-source context: Connes, survey §§9–12, Theorem 5.\nFull proof: Lemmas 8D.1–4; Theorems 8D.5/7/8.',
         ha='right',fontsize=10,color=gray)
for name in ('noncompact-native-comparison.svg','noncompact-native-comparison.png'):
 fig.savefig(HERE/name,dpi=160,facecolor=fig.get_facecolor(),
             metadata={'Date':None} if name.endswith('.svg') else {'Software':'Matplotlib; original CC0 proof diagram'})
plt.close(fig)
print('Rendered exact proof diagram: 2720 x 2400; SVG and PNG.')

