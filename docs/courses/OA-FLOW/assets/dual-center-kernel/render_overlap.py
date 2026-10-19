"""Exact two-point models for the independently organized central-overlap proof."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'assets')
args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'svg.hashsalt':'L115-owner-overlap-20261005'})
ink='#15304b';muted='#476176';blue='#1769aa';green='#20774d';red='#aa3e43';paper='#f6f8fb'
fig=plt.figure(figsize=(18,13),dpi=200,facecolor=paper)
title=fig.text(.5,.968,'A frequency survives exactly where central projections overlap',ha='center',va='top',fontsize=29,fontweight='bold',color=ink)
subtitle=fig.text(.5,.918,'An integrable action with continuous eigenunitaries · two exact finite models',ha='center',va='top',fontsize=19,color=muted)

def panel(bounds,color):
    ax=fig.add_axes(bounds);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.add_patch(FancyBboxPatch((.01,.015),.98,.97,boxstyle='round,pad=.008,rounding_size=.025',edgecolor=color,facecolor='white',lw=1.8))
    return ax
def text(ax,x,y,value,size=18,color=ink,**kw):
    return ax.text(x,y,value,fontsize=size,color=color,transform=ax.transAxes,**kw)
def arrow(ax,a,b,color=muted):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color=color,lw=1.8,transform=ax.transAxes))

general=panel([.045,.575,.91,.295],blue)
text(general,.035,.88,'GENERAL MECHANISM',18,blue,fontweight='bold')
text(general,.035,.75,r'$B=P^\beta,\quad\beta_s(\mu_p)=p(s)\mu_p,\quad\delta_p=\mathrm{Ad}(\mu_p)|_{Z(B)}$',23)
text(general,.035,.60,r'$0\ne e\in\mathrm{Proj}\,Z(B),\qquad P_p=\{x:\beta_s(x)=p(s)x\ \mathrm{for\ all}\ s\}$',21)
text(general,.5,.435,r'$eP_p e=B\,e\,\delta_p(e)\,\mu_p$',29,blue,ha='center')
text(general,.5,.295,r'$eP_p e\ne\{0\}\quad\Longleftrightarrow\quad e\,\delta_p(e)\ne0$',24,ha='center')
text(general,.035,.135,r'If $\delta_p=\mathrm{id}$: every central corner detects $p$.',17,green)
text(general,.035,.055,'If it moves the center: local displacement and integrability exclude a neighborhood in one corner.',16,red)

left=panel([.045,.125,.435,.415],red)
right=panel([.52,.125,.435,.415],green)
text(left,.045,.915,'ONE FREQUENCY IS EXCLUDED',19,red,fontweight='bold')
text(left,.045,.835,r'Original system: $M=\mathbb{C}$, trivial $\alpha$',19)
text(left,.045,.755,r'$P=M_2,\quad\beta_1=\mathrm{Ad}(R),\quad B=\mathrm{span}(I,R)$',18)
text(left,.045,.668,r'$e_+=(I+R)/2,\qquad e_-=(I-R)/2$',22)
for x,label in [(.25,'e₊'),(.75,'e₋')]:
    left.scatter([x],[.50],s=430,color=red,zorder=5)
    text(left,x,.415,label,25,red,ha='center')
arrow(left,(.29,.545),(.71,.545),red)
arrow(left,(.71,.465),(.29,.465),red)
text(left,.50,.595,r'$\delta_1=\mathrm{Ad}(D)$',18,red,ha='center')
text(left,.045,.285,r'$D e_+D=e_-,\qquad e_+e_-=0$',23)
text(left,.045,.185,r'The rank-one $e_+$ corner has only frequency $0$.',17)
text(left,.50,.068,r'$\Gamma(\beta)=\ker\delta=\{0\}$',25,red,ha='center')

text(right,.045,.915,'BOTH FREQUENCIES SURVIVE',19,green,fontweight='bold')
text(right,.045,.835,r'Original system: $M=\mathbb{C}\oplus\mathbb{C}$, $\alpha_1$ swaps entries',17)
text(right,.045,.755,r'$P=M_2\oplus M_2,\quad\beta_1(x,y)=(RyR,RxR)$',18)
text(right,.045,.668,r'$B=\{(a,RaR):a\in M_2\}\cong M_2$',22)
right.scatter([.5],[.50],s=750,color=green,zorder=5)
text(right,.5,.425,r'$1_B=(I,I)$',23,green,ha='center')
text(right,.5,.595,r'$Z(B)=\mathbb{C}1_B$',21,green,ha='center')
text(right,.045,.285,r'$\mu_1=(D,D),\qquad 1_B\delta_p(1_B)=1_B$',22)
text(right,.045,.185,'The center has one nonzero projection; the fixed algebra has many.',15.5)
text(right,.50,.068,r'$\Gamma(\beta)=\ker\delta=\{0,1\}$',25,green,ha='center')

fig.text(.045,.083,r'FINITE MODELS: $G=\widehat G=\mathbb{Z}/2$, $Re_0=e_1$, $Re_1=e_0$, $D=\mathrm{diag}(1,-1)$, $RDR=-D$.',fontsize=18,color=ink)
fig.text(.045,.052,'Counting Haar makes both finite actions integrable. The models illustrate the theorem; the general proof uses fixed-corner detection and local displacement.',fontsize=14,color=muted)
fig.text(.045,.029,'Proof locators: K26–27 (corners), K32 (principal eigenspaces), K34–35 (overlap), K36–42 (kernel).',fontsize=14,color=muted)

# Renderer checks only geometry; the mathematical identities are checked exactly below.
fig.canvas.draw();renderer=fig.canvas.get_renderer()
assert title.get_window_extent(renderer).y0-subtitle.get_window_extent(renderer).y1>=18
fig.savefig(args.output/'central-overlap.png',dpi=200,metadata={'Software':'Original local L115 overlap renderer'})
fig.savefig(args.output/'central-overlap.svg',metadata={'Date':None,'Creator':'Original local L115 overlap renderer'})
plt.close(fig)
I=sp.eye(2);R=sp.Matrix([[0,1],[1,0]]);D=sp.diag(1,-1);ep=(I+R)/2;em=(I-R)/2
assert R*D*R==-D and D*ep*D==em and ep*em==sp.zeros(2)
assert ep*ep==ep and em*em==em and ep.rank()==em.rank()==1
a,b,c,d=sp.symbols('a b c d');X=sp.Matrix([[a,b],[c,d]])
assert R*(R*X*R)*R==X and R*(D*(R*X*R)*D)*R==D*X*D
matrix=lambda X:[[str(x) for x in row] for row in X.tolist()]
data={'group':'Z/2','dual':'Z/2','pairing':'(-1)^(s*p)','Haar':'counting',
 'matrices':{'R':matrix(R),'D':matrix(D),'e_plus':matrix(ep),'e_minus':matrix(em)},
 'general_hypotheses':['arbitrary LCH abelian group G','point-ultraweakly continuous integrable beta on nonzero P','strongly continuous unitary representation mu of the dual with beta_s(mu_p)=p(s)mu_p'],
 'general_conclusions':{'principal':'P_p=B mu_p','corner':'e P_p e=B e delta_p(e) mu_p','nonzero_criterion':'e delta_p(e) !=0','kernel':'Gamma(beta)=ker(delta)'},
 'models':[{'original':'C, trivial action','ambient':'M2','fixed':'span(I,R)','center':'span(I,R)','eigenunitary_1':'D','center_action_1':'exchanges e_plus and e_minus','Gamma':[0]},
 {'original':'C direct-sum C, swap action','ambient':'M2 direct-sum M2','fixed':'{(a,R a R)}','center':'C(I,I)','eigenunitary_1':'(D,D)','center_action_1':'identity','Gamma':[0,1]}],
 'exact_checks_passed':True,'general_theorem_proved_by_finite_models':False,
 'proof_locators':['K26-K27','K32','K34-K35','K36-K42'],
 'dimensions':[3600,2600]}
(args.output/'central-overlap-data.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'output':str(args.output),'exact_checks_passed':True,'dimensions':data['dimensions']}))
