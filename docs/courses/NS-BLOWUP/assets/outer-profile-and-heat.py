"""Reproduce the exact construction diagram in N2.2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','font.size':13})
fig=plt.figure(figsize=(14,11.2),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1400);ax.set_ylim(1120,0);ax.axis('off')
ink='#152c42';blue='#17639b';orange='#b35c23'
def text(x,y,s,size=14,color=ink,**kw):ax.text(x,y,s,fontsize=size,color=color,va='top',**kw)
def box(x,y,w,h,fill='#e7eff6',edge='#bdd0df'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=12',
        facecolor=fill,edgecolor=edge,linewidth=1.2))
text(35,24,'Constructing the outer profile and heat exterior',23)
text(35,63,'Ordered intervals, exact moment restoration, and the limiting stress direction',14)
text(35,103,'RADIAL SCHEDULE — O0–O8',15,blue,weight='bold')
text(35,131,r'Each local $y=\log(X/X_{\rm left})$ starts at its interval’s left endpoint.',12)
stages=[
 ('1  Temporary inner reference',r'$y\leq0:\quad U=4\eta,\quad E=P_*f\,e^{y/10},\quad l=3/5$'),
 ('2  First transition',r'$1$ unit: $U=4\eta,\quad l=(3/5)(1-\sigma(y))$'),
 ('3  Gradual axial transition',r'$T_d=e^{M_d}+10:\quad U=k(y)\eta,\quad l=0$'),
 ('4  Long interval and four reserved patches',r'$1$ unit to $l=-\lambda$; then $T_w=60\log(1/\lambda)$'),
 ('5  Axial pulse and two end corrections',r'$13/\lambda$ units: $U=ER_b,\quad l=-\lambda,\quad M=J=S(\infty)=0$'),
 ('6  Angular interpolation and two corrections',r'$T_f+30\log(1/\lambda):\quad U=0,\quad I=XH/(1-\lambda),\quad\Delta C_p=0$'),
 ('7  Steep release and explicit final hold',r'$1+4\log(1/h)+1+T_{\rm hold}$ units; $E$ drops by $h^6$ on the steep hold'),
 ('8  Terminal interval and exterior',r'$0\leq y\leq3:\quad E=E_{\rm pow}f_o;\quad y\geq3:\ E=E_{\rm pow}$')]
for i,(title,formula) in enumerate(stages):
    y=165+i*94;box(35,y,700,75)
    text(52,y+10,title,14,blue,weight='bold');text(52,y+40,formula,12)
    if i<7:ax.add_patch(FancyArrowPatch((385,y+75),(385,y+92),arrowstyle='-|>',mutation_scale=12,color=blue))
text(35,934,'PARAMETER ORDER',14,blue,weight='bold')
text(35,961,r'$M_d\ \longrightarrow\ T_d\ \longrightarrow\ P_*\ \longrightarrow\ \lambda\ \longrightarrow\ h\ \longrightarrow\ X_R$',16)
text(35,1003,r'$0<h\ll\min(\lambda,e^{-T_d})$; all strict estimates precede the large-radius choice.',12)
text(35,1040,'Interval boxes are not to scale. Every omitted shape formula is supplied in O0.',12)
text(775,103,'EXACT HEAT COMPENSATION — K0, H0–H3',15,orange,weight='bold')
box(775,142,590,173,'#fff0e3','#e3c4ac')
text(793,158,r'$\mathcal{H}(Z)=\frac{1}{\Gamma(1+h)}\int_0^\infty e^{-v}v^h(1+Zv)^{-h}\,dv$',17)
text(793,213,r'$E_H=E_{\rm cl}[1+\chi_K(y)(\mathcal{H}(2d/X)-1)]$',15)
text(793,254,r'$X_K=e^{1/5}X_{\rm tail},\quad X_b=e^3X_{\rm tail}$',15)
text(793,284,r'$\chi_K=0$ for $y\leq1/5$; $\chi_K=1$ for $y\geq1/2$.',12)
box(775,338,590,225)
text(793,354,'The second reserved patch restores all three totals',14,blue,weight='bold')
text(793,390,r'$\Delta C_p=\int_0^\infty\frac{E_{\rm new}^2-E_{\rm cl}^2}{2X}\,dX=0$',15)
text(793,437,r'$\Delta S=-\frac{1}{2}\int_0^\infty(E_{\rm new}^2-E_{\rm cl}^2)\,dX=0$',15)
text(793,484,r'$\Delta\mathcal{I}=\int_0^\infty\sqrt{2X}(E_{\rm new}-E_{\rm cl})\,dX=0$',15)
text(793,531,'U is unchanged; M and J agree at every X. The axis pressure is preserved.',11)
text(775,588,'STRESS AT THE OUTER EDGE — H4–H6',15,orange,weight='bold')
box(775,627,590,275,'#fff0e3','#e3c4ac')
text(793,644,r'$\delta=\log(X_b/X)=3-y\ \longrightarrow\ 0^+$',17)
text(793,687,r'$\mathcal{T}_{0,\theta}=e^{-4/\delta^2}\delta^{-3}b_\theta,\qquad b_\theta(0,\eta)>0$',17)
text(793,733,r'$\mathcal{T}_{0,z}=e^{-4/\delta^2}\delta^3b_z$',17)
text(793,779,r'$\mathcal{T}_{0,z}/\mathcal{T}_{0,\theta}=\delta^6 b_z/b_\theta$',17)
text(793,825,r'$\mathcal{T}_0\to(0,0),\qquad\mathcal{T}_0/|\mathcal{T}_0|\to(1,0)$',17)
text(793,861,'Both coefficients are smooth on the closed collar.',11)
text(793,881,'Every stress derivative vanishes at the edge.',11)
box(775,925,590,137)
text(793,942,'The physical factors stay explicit',14,blue,weight='bold')
text(793,978,r'$T_\nu=\nu q_\nu^{-A-1/2}\mathcal{T}_0(X_\nu,\eta_\nu)$',17)
text(793,1018,'The positive common factor preserves the ratio and direction.',12)
text(35,1089,'Source: OpenAI, Appendix A, pp. 129–144. Complete independent derivation: N2.2 O0–H7 and X0. CC0 figure.',11)
fig.savefig(HERE/'outer-profile-and-heat.svg',metadata={'Title':'Outer profile, heat moments and endpoint stress','Creator':'GPT-6 Astra (OpenAI)'})
fig.savefig(HERE/'outer-profile-and-heat.png',dpi=100)
plt.close(fig)
p=HERE/'outer-profile-and-heat.svg'
t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="806.4pt"' in t
p.write_text(t.replace('width="1008pt" height="806.4pt"','width="1400" height="1120"'),encoding='utf8')
