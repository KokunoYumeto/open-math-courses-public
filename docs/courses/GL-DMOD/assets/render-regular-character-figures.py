"""Reproduce exact RA.54--55 data and the two inspected mathematical figures.

Numerical coordinates are used only to render the exact rational weight data.
All vector arithmetic and Weyl calculations precede rendering over Fraction.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import sqrt
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
HERE.mkdir(parents=True, exist_ok=True)
add = lambda a,b: tuple(x+y for x,y in zip(a,b))
neg = lambda a: tuple(-x for x in a)
sub = lambda a,b: add(a,neg(b))
strvec = lambda a: [str(x) for x in a]
rho = (F(1),F(0),F(-1))
lam = (F(2,3),F(-1,3),F(-1,3))
gamma = add(lam,rho)
w = lambda a: (a[2],a[0],a[1])  # s1(s2(a)): s2 exchanges 2,3; s1 exchanges 1,2
mu0 = sub(neg(w(rho)),rho)
fibre = neg(w(lam))
mulam = sub(neg(w(gamma)),rho)
wrong = sub(mu0,lam)
ap = [(F(1),F(-1),F(0)),(F(0),F(1),F(-1)),(F(1),F(0),F(-1))]
orbit = sorted(set(permutations(gamma)))
minusorbit = sorted(set(permutations(neg(gamma))))
cubic = lambda a: a[0]*a[1]*a[2]
assert sum(gamma)==sum(mulam)==0
assert set(orbit).isdisjoint(minusorbit)
assert mulam==add(mu0,fibre)
assert mu0==(F(0),F(-1),F(1))
assert mulam==(F(1,3),F(-5,3),F(4,3))
assert wrong==(F(-2,3),F(-2,3),F(4,3))
assert cubic(gamma)==F(20,27) and cubic(neg(gamma))==F(-20,27)
data = {
    'proof_locators':['RA.1','RA.5','RA.10','RA.54','RA.55'],
    'human_source':'https://www.math.utah.edu/~milicic/Eprints/book.pdf',
    'human_locators':'Chapter2 section2; Chapter5 section1; convention comparison only',
    'group':'SL3; actual dominant lambda=omega1',
    'exact_cartan_coordinates':'(zeta1,zeta2,zeta3), sum=0',
    'render_coordinates':'x=(zeta1-zeta2)/sqrt(2), y=(zeta1+zeta2-2*zeta3)/sqrt(6)',
    'rho':strvec(rho),'lambda':strvec(lam),'gamma':strvec(gamma),
    'minus_gamma':strvec(neg(gamma)),
    'gamma_orbit':[strvec(x) for x in orbit],
    'minus_gamma_orbit':[strvec(x) for x in minusorbit],
    'cubic_gamma':str(cubic(gamma)),'cubic_minus_gamma':str(cubic(neg(gamma))),
    'w':'s1*s2; apply s2 first; w(a1,a2,a3)=(a3,a1,a2)',
    'Sigma_w':['alpha1','alpha1+alpha2'],'Gamma_w':['-alpha2'],
    'mu0':strvec(mu0),'line_fibre_minus_wlambda':strvec(fibre),
    'mulambda':strvec(mulam),'incorrect_mu0_minus_lambda':strvec(wrong),
    'PBW_negative_directions':[strvec(neg(x)) for x in ap],
    'translation_hypothesis':'Every dominant actual lambda in X(T), including zero and non-ample cases',
    'forward':{'finite_module':'F_{-w0 lambda}','source_parameter':'tau0=-rho',
               'selected_weight':'-lambda','target_parameter':'tau0-lambda=-gamma',
               'sheaf_map':'p_A:(A tensor Fprime)^[chi_-gamma] -> L tensor A',
               'endpoint':'E.5/E.20; regularity belongs to original tau0'},
    'reverse':{'finite_module':'F_lambda','source_parameter':'tau0-lambda=-gamma',
               'selected_weight':'lambda','target_parameter':'tau0=-rho',
               'sheaf_map':'k_B:L^-1 tensor B -> (B tensor F)^[chi_-rho]',
               'endpoint':'E.4/E.18; target comparison uses tau=tau0'},
    'projector_linearity':'C-linear and U-linear; no O_X-linearity assertion',
    'factor_structure':'shifted TDO action transported through the selected endpoint isomorphism',
    'geometric_inverse_maps':'RA.42; BB counits then inverse-line evaluation then inverse BB unit',
    'scope_exclusions':'generalized, singular, parabolic, KL, affine, critical, factorization and analytic claims'
}
(HERE/'regular-character-figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'svg.fonttype':'none','svg.hashsalt':'regular-character-RA-20261009','figure.facecolor':'#f6f8fc',
                     'axes.facecolor':'#ffffff'})
ink='#17283b'; teal='#007e8a'; coral='#b83f78'; blue='#275dba'; grey='#789'
xy=lambda a: ((float(a[0])-float(a[1]))/sqrt(2),
              (float(a[0])+float(a[1])-2*float(a[2]))/sqrt(6))

fig,axs=plt.subplots(1,2,figsize=(16,8),dpi=160)
fig.subplots_adjust(left=.055,right=.965,top=.80,bottom=.25,wspace=.30)
fig.suptitle('Regular actual characters: opposite centre and Weyl-transported line fibre',
             fontsize=20,fontweight='bold',color=ink,y=.96)
fig.text(.5,.90,r'Type $A_2$: $G=\mathrm{SL}_3$, $\lambda=\omega_1$, $\gamma=\lambda+\rho=(5,-1,-4)/3$',
         ha='center',fontsize=17,color=ink)
ax=axs[0]
ax.set_title('Two exact Weyl orbits',fontsize=17,color=ink,pad=17)
for root in ap:
    xx,yy=xy(root)
    ax.plot([-2*xx,2*xx],[-2*yy,2*yy],color='#d4deeb',lw=1,zorder=0)
op=list(zip(*map(xy,orbit))); om=list(zip(*map(xy,minusorbit)))
ax.scatter(*op,s=90,color=teal,label=r'$W\gamma$',zorder=3)
ax.scatter(*om,s=100,marker='x',lw=2.5,color=coral,label=r'$W(-\gamma)$',zorder=3)
for a in (gamma,neg(gamma)):
    xx,yy=xy(a)
    ax.annotate(r'$\gamma$' if a==gamma else r'$-\gamma$',(xx,yy),
                xytext=(12,13 if a==gamma else -25),textcoords='offset points',
                fontsize=18,fontweight='bold',color=teal if a==gamma else coral)
ax.set_xlim(-2.8,2.8);ax.set_ylim(-2.8,2.8);ax.set_aspect('equal')
ax.legend(loc='upper left',frameon=False,fontsize=15)
ax.set_xlabel(r'$(\zeta_1-\zeta_2)/\sqrt{2}$');ax.set_ylabel(r'$(\zeta_1+\zeta_2-2\zeta_3)/\sqrt{6}$')
ax.text(.5,-.20,'Coordinate multisets differ.  The invariant cubic has values\n'
        r'$20/27$ and $-20/27$: $\chi_\gamma\ne\chi_{-\gamma}$.',
        ha='center',va='top',transform=ax.transAxes,fontsize=14,color=ink)
ax=axs[1]
ax.set_title(r'Cell $w=s_1s_2$: the actual fibre shift',fontsize=17,color=ink,pad=17)
a0=xy(mu0); al=xy(mulam); aw=xy(wrong)
ax.scatter(*a0,s=100,color=grey,zorder=4)
ax.scatter(*al,s=110,color=teal,zorder=4)
ax.scatter(*aw,s=85,marker='x',lw=2.5,color=coral,zorder=4)
ax.add_patch(FancyArrowPatch(a0,al,arrowstyle='-|>',mutation_scale=20,lw=2.5,color=teal))
ax.add_patch(FancyArrowPatch(a0,aw,arrowstyle='-|>',mutation_scale=17,lw=1.8,
                            linestyle='--',color=coral))
ax.annotate(r'$\mu_w^0=-\alpha_2$',a0,xytext=(8,12),textcoords='offset points',fontsize=15,color=ink)
ax.annotate(r'$\mu_w^\lambda=(1,-5,4)/3$',al,xytext=(10,9),textcoords='offset points',fontsize=15,color=teal)
ax.annotate(r'$\mu_w^0-\lambda$ (incorrect)',aw,xytext=(6,-24),textcoords='offset points',
            fontsize=13,ha='left',color=coral)
ax.text(.5,.91,r'Actual line fibre: $-w\lambda=(1,-2,1)/3$',
        ha='center',transform=ax.transAxes,fontsize=14,color=teal)
for root,label,offset in [(ap[0],r'$-\alpha_1$',(-10,5)),
                           (ap[1],r'$-\alpha_2$',(7,-15)),
                           (ap[2],r'$-(\alpha_1+\alpha_2)$',(7,-18))]:
    d=xy(neg(root));end=(al[0]+.65*d[0],al[1]+.65*d[1])
    ax.add_patch(FancyArrowPatch(al,end,arrowstyle='-|>',mutation_scale=14,
                                lw=1.6,color=blue,linestyle=':'))
    ax.annotate(label,end,xytext=offset,textcoords='offset points',fontsize=12,color=blue)
ax.set_xlim(-1.0,2.95);ax.set_ylim(-3.6,-.55);ax.set_aspect('equal')
ax.set_xlabel(r'$(\zeta_1-\zeta_2)/\sqrt{2}$');ax.set_ylabel(r'$(\zeta_1+\zeta_2-2\zeta_3)/\sqrt{6}$')
ax.text(.5,-.20,r'$\Sigma_w=\{\alpha_1,\alpha_1+\alpha_2\}$, $\Gamma_w=\{-\alpha_2\}$.'+'\n'
        'The three dotted directions are independent PBW exponents.',
        ha='center',va='top',transform=ax.transAxes,fontsize=14,color=ink)
for ax in axs:
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(colors='#69768b')
fig.text(.5,.018,'Exact weight-plane coordinates, not an embedding of the 3-dimensional flag chart.  Proof: RA.1, RA.5, RA.54–55.',
         ha='center',fontsize=12,color=ink)
for ext in ('png','svg'):
    fig.savefig(HERE/f'regular-character-a2-calibration.{ext}',dpi=160,
                metadata={'Description':'Exact RA.54-55 calibration; reproducible Fraction data and rendering source retained.',
                          **({'Date':None} if ext=='svg' else {})})
plt.close(fig)

fig,ax=plt.subplots(figsize=(17,11),dpi=160)
fig.subplots_adjust(left=.02,right=.98,bottom=.02,top=.98)
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.965,'Actual inverse translations and the two endpoint maps',ha='center',
        va='top',fontsize=23,fontweight='bold',color=ink)
ax.text(.5,.916,r'$\lambda\in X(T)$ dominant; $L=\mathcal{L}(-\lambda)$; $\tau_0=-\rho$; $\tau_\lambda=-\gamma=-\rho-\lambda$',
        ha='center',fontsize=18,color=ink)
def box(x,y,wid,hei,txt,color=ink,size=17):
    patch=FancyBboxPatch((x-wid/2,y-hei/2),wid,hei,boxstyle='round,pad=0.012,rounding_size=0.016',
                         edgecolor=color,facecolor='white',lw=1.8)
    ax.add_patch(patch);ax.text(x,y,txt,ha='center',va='center',fontsize=size,color=color)
def arrow(a,b,label,pos,color=blue,size=16):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='<->',mutation_scale=18,lw=2,color=color))
    ax.text(*pos,label,ha='center',va='center',fontsize=size,color=color,
            bbox={'facecolor':'#f6f8fc','edgecolor':'none','pad':3})
box(.20,.81,.27,.085,r'$\mathcal{O}_\rho^{\mathrm{ex}}$',teal,20)
box(.80,.81,.30,.085,r'$\mathcal{O}_{-\gamma}^{\mathrm{ex}}$',teal,20)
box(.20,.61,.27,.09,'Coherent strong B modules\n'+r'over $\mathscr{D}_0$',ink,17)
box(.80,.61,.30,.09,'Coherent strong B modules\n'+r'over $\mathscr{D}_\lambda$',ink,17)
arrow((.35,.81),(.63,.81),r'$\mathcal{F}_\lambda\quad/\quad\mathcal{G}_\lambda$',(.49,.847),teal,19)
arrow((.35,.61),(.63,.61),r'$L\otimes -\quad/\quad L^{-1}\otimes -$',(.49,.655),blue,18)
arrow((.20,.75),(.20,.67),r'$\mathrm{Loc}_0\,/\,\Gamma_0$',(.19,.710),blue,15)
arrow((.80,.75),(.80,.67),r'$\mathrm{Loc}_\lambda\,/\,\Gamma_\lambda$',(.81,.710),blue,15)
ax.text(.50,.528,'Inverse maps: BB counit → evaluate the inverse lines → inverse BB unit (RA.42).',
        ha='center',fontsize=15,color=ink)
ax.plot([.04,.96],[.497,.497],color='#ccd7e7',lw=1.6)
box(.50,.423,.90,.10,
    r'Forward: $A=\mathrm{Loc}_0M$,  $F^{\prime}=F_{-w_0\lambda}$'+'\n'+
    r'$p_A:(A\otimes F^{\prime})^{[\chi_{-\gamma}]}\ \overset{\sim}{\longrightarrow}\ L\otimes A$',teal,18)
ax.text(.50,.337,'Final quotient weight −λ occurs once. E.5 uses regularity of the original τ₀ = −ρ.',
        ha='center',fontsize=15,color=teal)
box(.50,.248,.90,.10,
    r'Reverse: $B=\mathrm{Loc}_\lambda N$,  $F=F_\lambda$'+'\n'+
    r'$k_B:L^{-1}\otimes B\ \overset{\sim}{\longrightarrow}\ (B\otimes F)^{[\chi_{-\rho}]}$',blue,18)
ax.text(.50,.160,'Initial highest weight λ occurs once. E.4 compares τ₀ − λ + ν with τ₀ = −ρ.',
        ha='center',fontsize=15,color=blue)
ax.text(.50,.119,'Bundle maps are O-linear. Central projections are C-linear and U-compatible.',
        ha='center',fontsize=16,fontweight='bold',color=ink)
ax.text(.50,.077,'The selected factor carries its shifted TDO action through the displayed isomorphism.',
        ha='center',fontsize=15,color=ink)
ax.text(.50,.032,'RA.41–51. No ampleness premise; generalized, singular, parabolic and KL claims remain outside this theorem.',
        ha='center',fontsize=12,color=ink)
for ext in ('png','svg'):
    fig.savefig(HERE/f'regular-character-translation-maps.{ext}',dpi=160,
                metadata={'Description':'Exact categories, actual bundle endpoint maps and projector linearity; proof RA.41-51.',
                          **({'Date':None} if ext=='svg' else {})})
plt.close(fig)
print('Rendered 2 PNGs and 2 editable SVGs from exact rational calibration data.')
