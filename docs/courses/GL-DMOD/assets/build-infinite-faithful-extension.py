from pathlib import Path
from fractions import Fraction
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'full-infinite-faithful-extension-Section548','axes.spines.top':False,'axes.spines.right':False})
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
root=Path(__file__).resolve().parent;out=args.output or root;out.mkdir(parents=True,exist_ok=True)
fig=plt.figure(figsize=(16,9),facecolor='white')
grid=fig.add_gridspec(1,2,width_ratios=[1.02,1.12],left=.05,right=.97,top=.81,bottom=.34,wspace=.23)
fig.suptitle('Proper ideals remain proper in the actual full infinite-order ring',fontsize=18,y=.963)
fig.text(.5,.89,'A complete coefficient quotient fixes 1 and annihilates every algebraic ideal element.',ha='center',fontsize=12,color='#334155')
left=fig.add_subplot(grid[0]);left.axis('off');left.set_xlim(0,1);left.set_ylim(0,1)
left.set_title('Actual source correction and quotient',fontsize=13,pad=18)
def box(y,height,text,color):
 patch=FancyBboxPatch((.035,y),.93,height,boxstyle='round,pad=.02',fc=color,ec='#94a3b8',lw=1.2)
 left.add_patch(patch);left.text(.5,y+height/2,text,ha='center',va='center',fontsize=11,linespacing=1.6)
box(.76,.21,'Proper principal ideal: no constant Taylor head\n'+r'$\mathsf{d}1=0,\quad\mathsf{p}1=1$', '#eff6ff')
box(.42,.25,'Correct every actual source vector using lifted relations\n'+r'$RW=0,\quad b=cR+v,\quad v\in V$'+'\n'+r'$Tb=Tv,\quad v=\mathsf{d}(T_0v)$','#f0fdf4')
box(.065,.27,r'$\mathcal{P}=\mathsf{p}(1+E\mathsf{d})^{-1}$'+'\n'+r'$\mathcal{P}T=0,\quad\mathcal{P}1=1$'+'\n'+r'$1\notin BI,\qquad B/BI\neq0$','#fff7ed')
for a,b in [(.75,.685),(.41,.345)]:
 left.annotate('',(.5,b),(.5,a),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#475569'})
left.text(.5,-.15,'Coefficient operators are bounded complex linear.\nActual row products retain all contractions and tails.\nProper-ideal proof uses no scalar-extension flatness.',ha='center',va='top',fontsize=10,color='#334155')
ax=fig.add_subplot(grid[1]);orders=list(range(1,21))
weighted=[2**ell for ell in orders];entire=[float(Fraction(1,2**ell*math.factorial(ell))) for ell in orders]
ax.semilogy(orders,weighted,'o-',color='#b45309',ms=4,lw=1.5,label=r'Required weighted norm: $2^L$')
ax.semilogy(orders,[1]*20,'s-',color='#1d4ed8',ms=3,lw=1.5,label=r'Absolute quotient value: $|\mathcal{P}r_L|=1$')
ax.semilogy(orders,entire,'o-',color='#15803d',ms=4,lw=1.5,label=r'Entire-function residual: $2^{-L}/L!$')
ax.set_xlim(.5,20.5);ax.set_xticks([1,5,10,15,20]);ax.set_ylim(1e-26,1e7);ax.set_yticks([10.**k for k in [-25,-20,-15,-10,-5,0,5]])
ax.grid(which='major',alpha=.23);ax.set_xlabel(r'Exact truncation index $L$');ax.set_ylabel('Absolute value, logarithmic scale')
ax.set_title(r'Exact sample: $r_x=1/2,\ \varepsilon=1/4,\ x=1/2,\ \tau=1$',fontsize=12,pad=18)
ax.legend(loc='lower left',fontsize=9,framealpha=.95)
ax.text(.5,-.16,r'$b_L\circ x=1+r_L,\quad \mathcal{P}r_L=-1$'+'\nThe signed quotient value remains −1 at every L.\nFinite plotted samples illustrate the all-L equations (FEP.20)–(FEP.21).',transform=ax.transAxes,ha='center',va='top',fontsize=10,color='#334155')
consequence_panel=FancyBboxPatch((.05,.075),.92,.11,boxstyle='round,pad=.012',transform=fig.transFigure,fc='#eff6ff',ec='#1d4ed8',lw=1.1,linestyle='-')
fig.add_artist(consequence_panel)
fig.text(.51,.13,'Right flatness in §5.47 (proof sections MF.1–MF.7) + the proper-ideal theorem:\nunit injectivity and faithful exact extension for every algebraic left module (proof sections FEP.7–FEP.9).',ha='center',va='center',fontsize=12,color='#1e3a8a',linespacing=1.5)
fig.text(.05,.025,'Proof sections: FEA.1–FEA.4, FEB.1–FEB.5, FEP.1–FEP.10. Free human context: Micro-hyperbolic systems §1.3 p.6 and §8 pp.42–46. No theorem is supplied by the plot.',fontsize=10,color='#475569')
fig.savefig(out/'infinite-faithful-extension-joint-domain.png',dpi=150,metadata={'Software':'Matplotlib; reproducible local proof illustration'})
fig.savefig(out/'infinite-faithful-extension-joint-domain.svg',metadata={'Date':None,'Creator':'Reproducible local proof illustration'})
plt.close(fig)
rows=[]
for ell in orders:
 rows.append({'L':ell,'weighted_residual_norm':2**ell,'entire_residual_exact':str(Fraction(1,2**ell*math.factorial(ell))),'signed_quotient_residual':-1})
data={'proof_locators':['equations (FEP.6)–(FEP.15)','equations (FEP.20)–(FEP.21)','proof sections FEA.1–FEA.4, FEB.1–FEB.5 and FEP.1–FEP.10'],'exact_parameters':{'base_radius_r_x':'1/2','epsilon':'1/4','x':'1/2','tau':'1'},'candidate':'(1-exp(-x*tau))/x; holomorphic at x=0, excluded by the every-epsilon bound on every common base neighborhood','finite_truncation':'sum_{j=1}^L (-1)^(j+1)*x^(j-1)*tau^j/j!','residual':'(-1)^(L+1)*x^L*tau^L/L!','all_L_identity':'b_L circle x = 1+r_L; P r_L=-1','samples':rows,'left_panel':'Exact operator identities; no geometric scale represented','proper_ideal_proof_uses_flatness':False,'unit_injectivity_uses_right_flatness':True,'right_flatness_proof':'Section 5.47, proof sections MF.1–MF.7'}
(out/'infinite-faithful-extension-joint-domain-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':3,'directory':str(out)}))
