from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,10),facecolor='white')
ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(x,y,w,h,txt,c,fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.009',fc=c,ec='#465c71',lw=1.3))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,linespacing=1.4)
def arrow(x,y,xx,yy):ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops=dict(arrowstyle='->',lw=1.8,color='#476887'))
box(.03,.80,.43,.13,'Holomorphic base resolution, L.1\nH=C{u}, n=d+1; Koszul resolves C in length n\nMinimal resolution of M̄₀ terminates by degree n','#e9f1fc',11.5)
box(.54,.80,.43,.13,'Polynomial resolution, L.2\nAdjoin zᵢ one at a time by cone(y−Ỹ)\nd(a,b)=(da+(y−Ỹ)b, −db); q=n+d=2d+1','#e9f1fc',11.5)
arrow(.475,.865,.525,.865)
box(.03,.56,.43,.15,'Actual R₀ syzygy, L.3\nFinite actual relation segment; h is injective\nK̄_q ⊕ Sˢ ≅ Sʳ by explicit fibre-product comparison\nLift that principal basis to actual relations','#f1f3f7',11)
box(.54,.56,.43,.15,'Bounded actual complex, L.4\n0 → E^r_q → ⋯ → E^r₀ → M → 0\nMatrices Pⱼ lie in R₀; length q=2d+1\nExact normal completion detects actual homology','#e6f5ec',11)
arrow(.755,.785,.755,.725);arrow(.245,.785,.245,.725);arrow(.475,.635,.525,.635)
box(.03,.30,.94,.17,'One base neighbourhood U, L.5–L.6\nHomogenize polynomial kernels; one finite set of coefficient identities works in every degree.\n'
    'For pᵢ(u,Z)=Zᵇ+Σₖ<ᵦ aᵢₖ(u)Zᵏ, choose Σₖ<ᵦ |aᵢₖ(u)| δ^(k−b) < 1/2.\n'
    'Then every root has |Z|<δ; the actual module vanishes outside that covector polydisc.\n'
    'The fixed polynomial matrices are exact on {u∈U, τ≠0}, including all branches and supported sections.','#edf6e6',11)
arrow(.755,.545,.755,.485);arrow(.245,.545,.245,.485)
box(.03,.075,.57,.14,'Exact nonreduced example, L.10–L.11\nJ=[[0,1],[0,0]], A=diag(0,1), T=tI−hA, Z=zI−J\n'
    'd₁(v,w)=vT+wZ;  d₂(u)=(uZ, −u(T−hI))\n'
    'Actual ZT−(T−hI)Z=0; principal support t=0, z²=0','#e6f5ec',10.5)
box(.66,.075,.31,.14,'OPEN: E∞ / A∞ comparison,\nsectorial vanishing and continuation,\nfinite D-type embedding and finite poles,\nmicrolocal order, C1 and analytic properness','#fff0dc',10.5)
arrow(.30,.285,.30,.235);arrow(.81,.285,.81,.235)
fig.suptitle('A bounded actual generic-position complex with polynomial operator matrices',fontsize=16,y=.98)
fig.text(.055,.025,'Exact premise: the actual finite lattice and finite principal fibre G.1. Proof: L.1–L.6; signed example: L.8.\n'
         'The bound and matrices are finite-order conclusions. Free human proof target: Kashiwara–Kawai, HolIII, III.5.3–III.5.8.',fontsize=10,color='#42566b')
fig.subplots_adjust(top=.94,bottom=.06)
fig.savefig(HERE/'bounded-polynomial-complex.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'bounded-polynomial-complex.svg',bbox_inches='tight')
print('Rendered bounded-polynomial-complex.png and .svg')
