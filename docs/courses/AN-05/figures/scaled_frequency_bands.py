"""Conformal phase scaling and exact band integrals; original mathematical figure, CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':11})
fig=plt.figure(figsize=(14,10),dpi=150,facecolor='#fffdfa')
ink='#193249'; muted='#4b5867'; blue='#4389b7'; green='#497a64'
fig.text(.045,.956,'A continuous family of bands recovers the fractional norm',fontsize=20,weight='bold',color=ink)
fig.text(.045,.918,'Exact phase scaling, an explicitly labelled scalar integration example, and the operator remainder orders',fontsize=11.2,color=muted)

ax=fig.add_axes([.045,.57,.91,.29]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(x,y,w,h,lines,fill='#eaf3f8'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=fill,edgecolor='#587a92',lw=1.3))
    for j,line in enumerate(lines):
        ax.text(x+w/2,y+h*(1-(j+1)/(len(lines)+1)),line,ha='center',va='center',fontsize=12,color=ink)
def arrow(a,b):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,lw=1.4,color='#587a92'))
box(.02,.43,.28,.45,[r'$(t,\sigma,y,\zeta)$',r'$\omega_s=d\sigma\wedge dt+\sum_jd\zeta_j\wedge dy_j$'])
box(.37,.43,.61,.45,[r'$F_\lambda=(t,\lambda^2\sigma,\lambda y,\lambda\zeta+\eta_0)$',r'$F_\lambda^*\omega=\lambda^2\omega_s$',r'$\{f\circ F_\lambda,g\circ F_\lambda\}=\lambda^2\{f,g\}\circ F_\lambda$'])
arrow((.305,.66),(.355,.66))
ax.text(.5,.235,r'$q_{I,\lambda}=\lambda^{-2}p_I\circ F_\lambda\quad\mathrm{for\ every\ word\ }I$',ha='center',fontsize=14,color=ink)
ax.text(.5,.07,'Each new bracket contributes one contraction factor and cancels one extra scale factor.',ha='center',fontsize=11,color=muted)

band=fig.add_axes([.09,.315,.39,.19],facecolor='#fffdfa')
band.set_title('Scalar sharp-band example only',fontsize=13,weight='bold',pad=14)
band.hlines([1,2],[.25,.125],[.5,.25],lw=13,colors=[blue,green])
band.plot([.25,.5],[1,1],'|',color=ink,ms=17)
band.plot([.125,.25],[2,2],'|',color=ink,ms=17)
band.set_xlim(0,.75);band.set_ylim(.4,2.6)
band.set_xticks([0,.125,.25,.5,.75]);band.set_xticklabels(['0','1/8','1/4','1/2','3/4'])
band.set_yticks([1,2]);band.set_yticklabels([r'$r=16$',r'$r=64$'])
band.set_xlabel(r'$\lambda:\quad 1\leq\lambda^2r\leq4$')
band.grid(axis='x',alpha=.2)
for s in band.spines.values():s.set_color('#bdc7ce')
fig.text(.565,.478,r'$\alpha=1/4,\quad a=1,\quad b=4,\quad\lambda_0=3/4$',fontsize=12,color=ink)
fig.text(.565,.426,r'$I(r)=\int\lambda^{-4\alpha}\mathbf{1}_{[a,b]}(\lambda^2r)\,d\lambda/\lambda$',fontsize=12,color=ink)
fig.text(.565,.374,r'$I(r)=\frac{r^{2\alpha}}{4\alpha}(a^{-2\alpha}-b^{-2\alpha})=\frac{\sqrt{r}}{2}$',fontsize=13,color=ink)
fig.text(.565,.323,r'$I(16)=2,\qquad I(64)=4$',fontsize=13,color=ink)
fig.text(.565,.282,'The indicator is an integration example; the proof uses smooth cutoffs.',fontsize=9.5,color=muted)

patch=FancyBboxPatch((.045,.105),.91,.125,transform=fig.transFigure,boxstyle='round,pad=0.008',facecolor='#f4f7f8',edgecolor='#587a92',lw=1.3)
fig.add_artist(patch)
fig.text(.5,.203,r'$R:\ \mathrm{order}\ 0;\quad \mathcal{D}_{2,\alpha}\mathcal{A}_1-\mathcal{T}_\alpha:\ \mathrm{order}\ \alpha-1$',ha='center',fontsize=13,color=ink)
fig.text(.5,.157,r'$\Phi=\mathcal{T}_\alpha^*\mathcal{T}_\alpha,\quad F_0\geq c|\eta|^{2\alpha};\quad 2\alpha-1\leq0$',ha='center',fontsize=13,color=ink)
fig.text(.5,.119,'Restrict the full frequency cone before comparing the quadratic form with a full Sobolev norm.',ha='center',fontsize=10,color=muted)
fig.text(.045,.062,'Proof: Lemma2.1; (3.2)–(3.4), (4.1)–(4.6), (5.2)–(5.4), (6.4); scalar example: Exercise2.',fontsize=9,color=muted)
fig.text(.045,.036,'Hörmander IV, proof of Theorem27.1.11, pp218–219. Original figure and reproducible Python source; CC0.',fontsize=9,color=muted)
fig.savefig(Path(__file__).with_name('scaled-frequency-bands.png'),dpi=150)
