"""Original CC0 Rees-specialization and symbol-subquotient diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15.4,10.0),dpi=170)
fig.patch.set_facecolor('#fbfaf6')
ax.set_xlim(0,15.4);ax.set_ylim(0,10);ax.axis('off')
ink,blue,green,orange='#213142','#275f9e','#28734c','#a14f21'

def label(x,y,t,size=17,color=ink,ha='left'):
    ax.text(x,y,t,fontsize=size,color=color,ha=ha,va='center')
def box(x,y,w,h,t,color,size=18):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.08',facecolor='white',edgecolor=color,linewidth=1.8))
    label(x+w/2,y+h/2,t,size,color,'center')
def arrow(x1,y1,x2,y2,c=ink):
    ax.annotate('',(x2,y2),(x1,y1),arrowprops=dict(arrowstyle='->',lw=2,color=c))

label(.5,9.5,'Rees specialization controls the actual projective output symbols',23)
label(.5,8.88,r'$\mathcal{C}=Rp_*(\mathscr{R}_FM\otimes^L_{\mathscr{R}_Z}\mathscr{T}),\qquad H_b=H^b(\mathcal{C})$',19)
box(.8,7.15,5.25,.85,r'$\mathcal{C}\quad\mathrm{derived\ Rees\ image}$',blue)
box(9.15,7.15,5.25,.85,r'$p_+M\quad\mathrm{actual\ operator\ image}$',green)
arrow(6.23,7.57,8.97,7.57,green)
label(7.60,8.03,r'$h=1$',18,green,'center')
box(.8,4.75,13.6,.92,r'$B=\mathfrak{a}_D(\mathcal{C}\otimes^L\mathbf{C}_0)\ \simeq\ Rq_*Lj^*G$',blue)
arrow(3.42,6.98,3.42,5.83,blue)
label(3.85,6.41,r'$h=0$ and analytic extension',17,blue)

label(.8,4.18,r'$\overline{H}_b=H_b/(h\mathrm{-power\ torsion})$',19)
label(8.0,4.18,'A good filtration of the actual image',16,green)
box(.8,2.88,5.0,.83,r'$\mathfrak{a}_D(H_b/hH_b)$',blue)
box(8.65,2.76,5.76,1.06,r'$\mathfrak{a}_D(\overline{H}_b/h\overline{H}_b)$'+'\n'+r'$=\mathfrak{a}_D(\operatorname{gr}_{F\prime}H^b(p_+M))$',green,16)
arrow(5.96,3.29,8.48,3.29,green)
label(7.2,3.75,'surjective',15,green,'center')
box(.8,1.20,5.0,.83,r'$H^b(B)$',blue)
arrow(3.3,2.71,3.3,2.20,blue)
label(3.70,2.43,'injective',15,blue)
label(6.15,1.69,'Actual symbols are a quotient of a submodule of the candidate.',15,green)
label(.8,.55,r'$\mathrm{Ch}\ H^b(p_+M)\ \subseteq\ q(j^{-1}\mathrm{Ch}\ M)$'+'   •   Proof: (5.12q)–(5.12w).',18)

fig.savefig(base/'projective-filtered-characteristic-proof.png',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(base/'projective-filtered-characteristic-proof.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
plt.close(fig)
