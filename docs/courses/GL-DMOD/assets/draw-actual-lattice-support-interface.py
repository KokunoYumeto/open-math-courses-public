from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,10),facecolor='white');ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(x,y,w,h,txt,c,fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.008',fc=c,ec='#456077',lw=1.4))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,linespacing=1.45)
def arr(x,y,xx,yy):ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.8,color='#446e8b'))
box(.025,.81,.95,.12,'Arbitrary actual coherent E-module germ M, J.1\n'
    'Finite generators mⱼ; stalk lattice M₀=ΣE₀mⱼ inside M; finite actual presentation P₀\n'
    'No regular invariant lattice or canonical cutoff is assumed.','#e9f1fc',11.5)
box(.025,.56,.43,.16,'First finite neighbourhood check\nE ⊗E₀ P₀ → M is an isomorphism at p₀\n'
    'Extend its finite inverse and presentation identities.\n'
    'Then it is an isomorphism near p₀.','#edf3fa',11)
box(.545,.56,.43,.16,'Second finite neighbourhood check\nh: σ⁻¹P₀ → P₀ is injective at p₀\n'
    'Its coherent kernel vanishes near p₀.\n'
    'Therefore P₀ embeds in its localization.','#edf3fa',11)
arr(.24,.795,.24,.735);arr(.76,.795,.76,.735)
box(.025,.325,.95,.15,'Actual coherent lattice M₀ ⊂ M exists on one neighbourhood, J.2–J.4\n'
    'M̄₀,p=0  ⇔  M₀,p=0  ⇔  M_p=0\n'
    'Finite actual h-Nakayama       Injective normal localization\n'
    'Supp M = Supp(M₀/hM₀) as reduced sets; all nilpotents and supported sections are retained.','#e6f5ec',11.5)
arr(.24,.545,.24,.49);arr(.76,.545,.76,.49)
box(.025,.075,.60,.15,'For a holonomic actual support, J.3\n'
    'Q puts the whole Lagrangian germ in generic position.\n'
    'Maximal minors + analytic Nullstellensatz give finite fibre V.\n'
    'G / F / L then apply to the entire arbitrary actual germ.','#edf6e6',11)
box(.685,.075,.29,.15,'Still open: infinite-order comparison,\n'
    'sectorial action and separation,\n'
    'faithful finite D-type / finite poles,\n'
    'microlocal order and full C1','#fff0dc',10.5)
arr(.325,.31,.325,.245);arr(.83,.31,.83,.245)
fig.suptitle('An actual lattice and principal-support interface for every coherent finite-order germ',fontsize=16,y=.98)
fig.text(.055,.025,'Proof locators: J.1–J.3. The equality concerns reduced support sets, not equality of the two modules.\n'
         'Free human context: Kashiwara–Kawai, HolIII, I.1.13 and III.5.5. The complete actual finite-presentation argument is retained.',fontsize=10,color='#43596c')
fig.subplots_adjust(top=.94,bottom=.065)
fig.savefig(HERE/'actual-lattice-support-interface.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'actual-lattice-support-interface.svg',bbox_inches='tight')
print('Rendered actual-lattice-support-interface.png and .svg')
