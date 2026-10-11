"""Reproduce the character-period and stable-line proofs in Theorem1.3B."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
from PIL import Image
root=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,ax=plt.subplots(figsize=(5,17),dpi=180)
ax.set(xlim=(0,5),ylim=(0,17));ax.axis('off')
ax.text(2.5,16.45,'Character periods and\nstable-line units',ha='center',va='center',fontsize=20,weight='bold')
ax.text(2.5,15.78,'Every finite K; every prime, including p = 2',ha='center',fontsize=11)
boxes=[
 (14.83,'Infinite-inertia case: deep units',r'$s(i+e_F)=s(i)+1$'+'; eventual jump spacing '+r'$e_F$','Earlier reciprocity + unit filtration; LC2, LC7–LC8','#edf4ff'),
 (12.97,r'$D_n=n+c+q p^{-n}$',r'$v(T_nx)\geq v(x)-C p^{-n}$',r'$C=|q|+1/e_F$'+'; rounding retained; LC10–LC14','#edf4ff'),
 (11.11,r'$T_n:\widehat{E_\infty}\to E_n;\quad T_nx\to x$','Equivariance kills every projected infinite-inertia period','Completed fixed field proved earlier; LC3, LC15–LC17','#edf4ff'),
 (9.25,'Nonzero '+r'$C_p$'+' period ⇒ finite inertia image','Existence and one-dimensionality use the units below','Vanishing LC17; finite-inertia descent LC20','#edf8ef'),
 (7.39,r'$\sigma^f(a)=\lambda a;\quad a\in W(\overline{\mathbf{F}}_p)^\times$',r'$f$'+' is the residue degree of a finite L/K',r'$\lambda=\eta({\rm Frob}_{L,ar})$'+'; p2 lifting; LC18–LC19','#edf8ef'),
 (5.53,r'$b=h a t^n;\quad h\in L_0^\times$',r'$b^{-1}=h^{-1}a^{-1}t^{-n}\in B_{\rm cris}$','Stable rational crystalline line; signed t-order n; LC21–LC24','#fff4dc'),
 (3.48,'Separate semistable degree argument',r'$b/b_d\in F(y)^{G_K}=K_0$',r'$b_d$'+' is the top coefficient; degree zero; LC25','#fff4dc'),
 (1.62,'Crystalline and semistable line units','Both period rings satisfy Lemma1.3 (10a)','Fraction invariants + units give admissibility algebra','#edf8ef'),
]
for y,title,body,loc,colour in boxes:
 ax.add_patch(FancyBboxPatch((.22,y-.68),4.56,1.36,boxstyle='round,pad=.08',facecolor=colour,edgecolor='#27445f',linewidth=1.3))
 ax.text(2.5,y+.33,title,ha='center',va='center',fontsize=12)
 ax.text(2.5,y-.07,body,ha='center',va='center',fontsize=10.4)
 ax.text(2.5,y-.49,loc,ha='center',fontsize=8.3,color='#37516a')
for ys in ([14.83,12.97,11.11,9.25,7.39,5.53],[3.48,1.62]):
 for a,b in zip(ys,ys[1:]):
  ax.add_patch(FancyArrowPatch((2.5,a-.79),(2.5,b+.79),arrowstyle='-|>',mutation_scale=17,color='#27445f',linewidth=1.4))
ax.annotate('',xy=(4.86,1.64),xytext=(4.86,5.5),arrowprops={'arrowstyle':'-|>','color':'#27445f','lw':1.3})
ax.text(2.5,4.43,'Use the earlier proved F(y) invariants',ha='center',fontsize=10,weight='bold')
ax.text(2.5,.42,'Arrows summarize proof dependencies.\nThe monic-degree step requires no leading-coefficient unit.',ha='center',fontsize=9.6)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
p=root/'assets/character-line-proof-map.png'
fig.savefig(p,facecolor='white',metadata={'Software':'Matplotlib'});plt.close(fig)
with Image.open(p) as im:im.copy().save(p)
