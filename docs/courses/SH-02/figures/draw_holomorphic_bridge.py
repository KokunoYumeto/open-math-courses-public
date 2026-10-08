"""CC0: exact sector cuts and actual restriction diagram, HB6-HB11."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch

parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,default=Path(__file__).resolve().parent.parent);args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','mathtext.fontset':'dejavusans'})
fig,axes=plt.subplots(1,2,figsize=(15,7.2),gridspec_kw={'width_ratios':[1,1.55]},constrained_layout=True)
ax=axes[0];ax.set_xlim(-1.55,1.4);ax.set_ylim(-2,2)
ax.add_patch(Rectangle((-1,-2),2,4,facecolor='#f5e6cd',edgecolor='none'))
ax.add_patch(Rectangle((-1,-1),2,2,facecolor='#e3eef6',edgecolor='#315d7d',lw=1.7))
ax.axhline(0,color='#cad3da',lw=.8);ax.axvline(0,color='#cad3da',lw=.8)
ax.vlines(-1,-2,2,color='#b94348',lw=2.7)
ax.plot(-1,0,'o',color='#176597',ms=8)
ax.plot(0,0,'o',color='#303c42',ms=5)
ax.text(.35,1.55,r'$D_+: v\geq\eta$',ha='center',color='#78551f')
ax.text(.35,-1.55,r'$D_-: v\leq-\eta$',ha='center',color='#78551f')
ax.text(.38,.45,r'$C$',ha='center',fontsize=19,color='#315d7d')
ax.text(.38,.2,r'$|u|\leq M,\ |v|\leq\eta$',ha='center',fontsize=11)
ax.text(.4,.87,r'$I_+:v=\eta$',ha='center',fontsize=10)
ax.text(.4,-.87,r'$I_-:v=-\eta$',ha='center',fontsize=10)
ax.annotate(r'$L_-:g=-M$',(-1,0),xytext=(-1.47,-.55),fontsize=11,arrowprops={'arrowstyle':'->','color':'#176597'},color='#176597')
ax.annotate(r'$B:u=-M$',(-1,1.75),xytext=(-1.45,1.93),fontsize=10,color='#b94348')
ax.text(.1,-.28,'critical value 0',fontsize=10)
ax.set_xticks([-1,0,1],[r'$-M$','0',r'$M$']);ax.set_yticks([-1,0,1],[r'$-\eta$','0',r'$\eta$'])
ax.set_xlabel(r'$u=\operatorname{Re}g$ (positions divided by $M$)')
ax.set_ylabel(r'$v=\operatorname{Im}g$ (positions divided by $\eta$)')
ax.set_title('Closed sector cuts in the value plane',pad=18)
ax.spines[['top','right']].set_visible(False)
ax.text(.5,-.21,'Exact base inequalities; no assertion about the shape of X or g(X).\nThe radial bound is imposed in X.',ha='center',va='top',transform=ax.transAxes,fontsize=10,color='#667686')

ax=axes[1];ax.set_xlim(0,12);ax.set_ylim(0,7);ax.axis('off')
nodes=[(1.9,5.15,r'$R\Gamma(K_u;F)$'),(6,5.15,r'$R\Gamma(C;F)$'),(10.15,5.15,r'$R\Gamma(K;F)$'),(1.9,2.85,r'$R\Gamma(B;F)$'),(6,2.85,r'$R\Gamma(L_-;F)$'),(10.15,2.85,r'$R\Gamma(L_-;F)$')]
for x,y,label in nodes:ax.text(x,y,label,ha='center',va='center',fontsize=13,bbox={'boxstyle':'round,pad=.55','fc':'#f4f8fb','ec':'#9eb7c9'})
def arrow(start,end,label=None,pos=None,color='#315d7d'):
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=18,linewidth=1.8,color=color))
 if label:ax.text(*pos,label,ha='center',va='center',fontsize=11,color=color)
arrow((3.2,5.15),(4.75,5.15),'res ≃ (HB5)',(4,5.65))
arrow((8.85,5.15),(7.25,5.15),'res ≃ (HB5)',(8.1,5.65))
arrow((3.2,2.85),(4.75,2.85),'res ≃ (HB8–HB9)',(4,2.35))
arrow((8.85,2.85),(7.25,2.85),'identity',(8.1,2.35))
for x in [1.9,6,10.15]:arrow((x,4.65),(x,3.35),'res',(x+.35,4),color='#b94348')
ax.text(6,6.6,'Actual restriction squares before taking fibres',ha='center',fontsize=16,color='#24475f')
ax.text(6,1.3,r'Every top central restriction is the specified isomorphism to $F_0$.',ha='center',fontsize=12)
ax.text(6,.7,r'The bottom left arrow factors through $R\Gamma(B_C;F)$.',ha='center',fontsize=12)
ax.text(6,.12,'The same coefficients are restricted from F; HB10 retains the specialization map.',ha='center',fontsize=11,color='#667686')
fig.savefig(args.out/'holomorphic-real-band-bridge.svg');fig.savefig(args.out/'holomorphic-real-band-bridge.png',dpi=180);plt.close(fig)
