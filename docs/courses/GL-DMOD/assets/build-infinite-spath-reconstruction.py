from pathlib import Path
from fractions import Fraction
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'full-infinite-spath-reconstruction-public-v1','axes.spines.top':False,'axes.spines.right':False})
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
root=Path(__file__).resolve().parent;out=args.output or root/'figures';out.mkdir(parents=True,exist_ok=True)
def save(fig,name):
    fig.savefig(out/(name+'.png'),dpi=150,metadata={'Software':'Matplotlib; reproducible original mathematical illustration'})
    fig.savefig(out/(name+'.svg'),metadata={'Date':None,'Creator':'Reproducible original mathematical illustration'})
    plt.close(fig)
fig,axes=plt.subplots(1,3,figsize=(17,8),gridspec_kw={'width_ratios':[1,1,1.1]})
fig.subplots_adjust(left=.055,right=.975,top=.79,bottom=.31,wspace=.34)
fig.suptitle('Full spatial division preserves nilpotents and the actual infinite-order class',fontsize=18,y=.965)
fig.text(.5,.887,'J = [[0,1],[0,0]],  '+r'$L=zI-J,\quad v=(1,0),\quad F=v/(1-z)$',ha='center',fontsize=13)
zs=[Fraction(k,100) for k in range(-60,61)]
values=[float(1/(1-z)) for z in zs]
ax=axes[0];ax.plot([float(z) for z in zs],values,color='#1d4ed8',lw=2,label=r'$q_1=q_2=1/(1-z)$')
ax.plot([float(z) for z in zs],[1]*len(zs),'--',color='#15803d',lw=2,label=r'$s_1=s_2=1$')
ax.set_xlim(-.6,.6);ax.set_ylim(0,2.7);ax.set_xlabel(r'Real slice $z$, with $|z|\leq3/5$');ax.set_ylabel('Exact rational coordinate value')
ax.set_title('Infinitely many spatial Taylor indices',fontsize=12,pad=17);ax.grid(alpha=.2);ax.legend(fontsize=9,loc='upper left')
ax.text(.5,-.22,r'$F=q(zI-J)+s,\quad s=v(I+J)=(1,1)$'+'\n'+r'$q(zI-J)=(z/(1-z),-1)$'+'\nThe nilpotent second coordinate survives.',ha='center',va='top',transform=ax.transAxes,fontsize=10,linespacing=1.6)
ax=axes[1];bs=list(range(0,21));ratios=[2**b for b in bs]
ax.semilogy(bs,ratios,'o-',color='#b45309',ms=4,lw=2);ax.axhline(1,color='#94a3b8',lw=1)
ax.set_xlabel(r'Spatial degree $b$');ax.set_ylabel(r'$b!|J_b|/\delta^b=2^b$');ax.set_xlim(-.5,20.5);ax.set_ylim(.5,2e6);ax.grid(alpha=.2)
ax.set_title('Full ring differs from the special class',fontsize=12,pad=17)
ax.text(.5,-.22,r'$P=\tau^{-1}/(1-z),\quad t-s=1/4,\quad\delta=1/8$'+'\n'+r'$J_b=(t-s)^b/b!$'+'\nThese exact samples illustrate the all-b failure of coefficient bound ISF.3.',ha='center',va='top',transform=ax.transAxes,fontsize=10,linespacing=1.6)
ax=axes[2];ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title('One common domain for the entire inverse',fontsize=12,pad=17)
def box(axis,y,height,label,color):
    axis.add_patch(FancyBboxPatch((.025,y),.95,height,boxstyle='round,pad=.014',fc=color,ec='#94a3b8',lw=1.2))
    axis.text(.5,y+height/2,label,ha='center',va='center',fontsize=10,linespacing=1.6)
box(ax,.74,.22,'Principal holomorphic division\n'+r'$\mathsf{d}_\nu,\mathsf{p}_\nu:\quad \|A_\nu\|<R_\nu^*/8$'+'\nUniform coefficient bounds on fixed radius profiles','#eff6ff')
box(ax,.39,.23,'Actual inverse, all losses K and input degrees m\n'+r'$(1+\mathsf{d}_\nu E_\nu)^{-1}$'+'\n'+r'$C_1^K(|m|+K)!/|m|!$','#f0fdf4')
box(ax,.04,.23,'All spatial variables eliminated sequentially\n'+r'$F=\sum_\nu a_\nu(D_\nu-B_\nu)+s$'+'\n'+r'$s\in(A^\infty)^r$'+'; a sum, no simultaneous uniqueness','#fff7ed')
for a,b in [(.73,.635),(.38,.285)]:ax.annotate('',(.5,b),(.5,a),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#475569'})
ax.text(.5,-.22,'Every positive epsilon; negative factorial tails.\nAll spatial indices; fixed derivative tails.\nNo radius chosen separately for any index.',ha='center',va='top',transform=ax.transAxes,fontsize=10,linespacing=1.6)
fig.text(.055,.065,'Equations ISD.4–ISD.15 and ISF.3–ISF.10; complete lowering proof sections ISB.1–ISB.5. The first two panels are exact stated real/rational samples;\nthe right panel is an algebraic/estimate diagram, not geometric scale. Free human context: author-hosted HolIII III.3/III.5, pp.888–889/900–903.',fontsize=10,color='#475569',linespacing=1.5)
save(fig,'infinite-spath-division-and-special-class')
rows=[{'z':str(z),'F':[str(1/(1-z)),'0'],'q':[str(1/(1-z)),str(1/(1-z))],'qL':[str(z/(1-z)),'-1'],'s':['1','1']} for z in zs]
(out/'infinite-spath-division-and-special-class-data.json').write_text(json.dumps({'proof_locators':['ISD.4–ISD.15','ISF.3–ISF.10','ISB.1–ISB.5'],'J':[[0,1],[0,0]],'v':[1,0],'r':1,'real_slice_z':['-3/5','3/5'],'nilpotent_preserved':True,'samples':rows,'special_exclusion':{'t_minus_s':'1/4','delta':'1/8','samples':[{'b':b,'ratio':2**b} for b in bs]},'right_panel':'Exact coefficient identities and proved bounds, no geometric scale'},indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(16,8),facecolor='white');grid=fig.add_gridspec(1,2,width_ratios=[1.2,1],left=.055,right=.97,top=.80,bottom=.28,wspace=.24)
fig.suptitle('Balanced reconstruction uses two distinct rings and retains the whole germ',fontsize=18,y=.965)
fig.text(.5,.889,'Every tensor is algebraic; multiplication inverses are literal unit maps. All singular branches and nilpotents remain.',ha='center',fontsize=12,color='#334155')
ax=fig.add_subplot(grid[0]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title(r'On the ray $p\in\mathbf{C}^\times p_0$',fontsize=13,pad=18)
box(ax,.76,.18,r'$B_p\otimes_{R^\infty}N$'+'\nBalance only uniform finite spatial polynomials','#eff6ff')
box(ax,.40,.19,r'$B_p\otimes_{\widetilde{E}^\infty_{q_0}}N$'+'\nAdd the actual special fibration relations','#f0fdf4')
box(ax,.025,.21,r'$N=M^\infty_{p_0}=\sum_i A^\infty u_i$'+'\n'+r'$\mu(b\otimes n)=bn,\qquad\iota(n)=1\otimes n$','#fff7ed')
ax.annotate('',(.42,.60),(.42,.75),arrowprops={'arrowstyle':'->','lw':1.4});ax.annotate('',(.58,.75),(.58,.60),arrowprops={'arrowstyle':'->','lw':1.4})
ax.text(.02,.674,r'$q$',fontsize=11);ax.text(.68,.674,r'$q^{-1}=\iota_R\mu_S$',fontsize=11)
ax.annotate('',(.42,.245),(.42,.39),arrowprops={'arrowstyle':'->','lw':1.4});ax.annotate('',(.58,.39),(.58,.245),arrowprops={'arrowstyle':'->','lw':1.4})
ax.text(.02,.315,r'$\mu_S$',fontsize=11);ax.text(.70,.315,r'$\iota_S$',fontsize=11)
ax.text(.5,-.17,'The sum decomposition kills relation tensors and balances the remainder.\nNo free A-infinity identification; no replacement of the special tensor.',ha='center',va='top',transform=ax.transAxes,fontsize=10,linespacing=1.6)
ax=fig.add_subplot(grid[1]);ks=list(range(1,13));inverse=[k+k*k for k in ks]
ax.plot(ks,inverse,'o-',color='#1d4ed8',lw=2,ms=5);ax.grid(alpha=.2);ax.set_xticks([1,3,6,9,12]);ax.set_xlabel(r'Exact sample $z=1/k$, $\tau=1$, $t=x=0$');ax.set_ylabel(r'Row-sum norm of $(zI-J)^{-1}$')
ax.set_title(r'Off the ray: $(zI-J)^{-1}=z^{-1}I+z^{-2}J$',fontsize=12,pad=18)
ax.text(.5,-.17,r'$\|(zI-J)^{-1}\|_\infty=k+k^2,\quad z=1/k$'+'\nThe inverse has no extension across z=0.\nBoth balanced tensors vanish for every off-ray point (proof section ISR.4).',ha='center',va='top',transform=ax.transAxes,fontsize=10,linespacing=1.6)
fig.text(.055,.065,'Equations ISR.2–ISR.13, ISD.12 and ISF.9. The left panel is an exact module diagram; the right is a stated real slice of the nilpotent principal inverse.\nSection 5.48 proves faithful extension and detection of the whole original finite support. Free human context: author-hosted HolIII III.5, (3.5.8)/(3.5.16), pp.901/903.',fontsize=10,color='#475569',linespacing=1.5)
save(fig,'infinite-balanced-reconstruction-and-off-ray')
(out/'infinite-balanced-reconstruction-and-off-ray-data.json').write_text(json.dumps({'proof_locators':['ISR.2–ISR.13','ISD.12','ISF.9'],'left_panel':'Exact balanced module diagram; no geometric scale','rings_distinct':['R-infinity','decorated-special-E-infinity','A-infinity','full-E-infinity'],'tensors':'ordinary algebraic','nilpotent_J':[[0,1],[0,0]],'sample_slice':{'tau':1,'t':0,'x':0,'z':'1/k'},'inverse_samples':[{'k':k,'z':str(Fraction(1,k)),'row_sum_norm':k+k*k} for k in ks],'inverse_domain_excludes':'z=0','faithful_proof_locator':'Section5.48, FEP.8–FEP.9'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':6,'directory':str(out)}))
