"""Reproduce Figure IRG.1. CC0-1.0; schematic operator diagram, no metric scale."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'none'})
fig=plt.figure(figsize=(10,14),dpi=160,facecolor='#f7f9fc');ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(y,h,title,body,color='#e7effb'):
 ax.add_patch(FancyBboxPatch((.06,y),.88,h,boxstyle='round,pad=0.014',facecolor=color,edgecolor='#7185a3',linewidth=1.2))
 ax.text(.085,y+h-.025,title,va='top',weight='bold',fontsize=16,color='#18314e')
 ax.text(.085,y+h-.062,body,va='top',linespacing=1.65,fontsize=14,color='#1c293a')
ax.text(.06,.974,'Scalar central profiles in the affine model',weight='bold',fontsize=23,va='top',color='#163d65')
ax.text(.06,.937,'Original trace, original expectations, one fixed actual core',fontsize=14,color='#52677e')
box(.729,.171,'Indicator rigidity — IRG.2–IRG.3',
 r'$z^2=z,\quad \beta=P_0z,\quad T=Q_\kappa P_0$'+'\n'+
 r'$\|z-Tz\|_1=2\tau(\kappa z(1-\beta))$'+'\n'+
 r'$\|\zeta-P_0\zeta\|_1\leq d\|\zeta-T\zeta\|_1+2(d+1)\|\zeta-tz\|_1$')
box(.523,.154,'Every matrix deletion returns to the same B — IRG.8–IRG.10',
 r'$A_0\,\bar\otimes\,L(D)\ \subset\ B_0\,\bar\otimes\,L(D)$'+'\n'+
 r'$\widetilde A=A_0\,\bar\otimes\,B(L^2D)\ \subset\ \widetilde B$'+'\n'+
 r'$\sigma_p(x)=\widetilde{\operatorname{Tr}}(px)/c\quad(x\in B)$'+'\n'+
 'The center operators, probabilities and old expectation are retained.')
ax.annotate('',xy=(.5,.694),xytext=(.5,.719),arrowprops=dict(arrowstyle='->',lw=2,color='#234d79'))
box(.309,.159,'Index ten: the two constraints — IRG.11–IRG.13',
 r'Physical Følner commutators $\longrightarrow 0$'+'\n'+
 r'Stationarity defect $\Gamma\longrightarrow0$, but $\liminf J(p)\geq3/5$'+'\n'+
 r'Exact profile $tz$: $J(p)\leq10\Gamma\longrightarrow0$ (impossible)'+'\n'+
 r'Any profile: $\liminf\inf_{t,z}\|\zeta-tz\|_1/c\geq3/110$',color='#e9f4ee')
ax.annotate('',xy=(.5,.485),xytext=(.5,.509),arrowprops=dict(arrowstyle='->',lw=2,color='#234d79'))
box(.104,.153,'The quantifier boundary — Theorem IRG.3 and Exercise IRG.3',
 'Fix the actual affine core first; then allow every matrix deletion.\n'+
 'A finite physical test set obstructs constant multiplicity.\n'+
 'BF may choose a different ordinary tunnel after seeing the targets.\n'+
 'The general BF and fixed-WM endpoint questions remain open.',color='#fff1df')
ax.annotate('',xy=(.5,.274),xytext=(.5,.295),arrowprops=dict(arrowstyle='->',lw=2,color='#234d79'))
ax.text(.06,.059,'Schematic maps and bounds; no area represents trace or dimension.',fontsize=12,color='#52677e')
ax.text(.06,.035,'Sources: Popa (1994), Theorem 4.2.2, pp. 213–214; AH/AB/AO; 52.3; 68.5.',fontsize=11,color='#52677e')
stem='indicator-rigidity-and-affine-rounding'
fig.savefig(out/(stem+'.png'),dpi=160)
fig.savefig(out/(stem+'.svg'))
p=out/(stem+'.svg');p.write_text(re.sub(r'[ \t]+(?=\r?$)','',p.read_text(),flags=re.M),encoding='utf-8')
