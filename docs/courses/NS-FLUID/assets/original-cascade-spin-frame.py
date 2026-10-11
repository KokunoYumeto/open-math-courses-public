"""Reproduce the exact original frequency triangle and all eight coefficients."""
from pathlib import Path
from itertools import product
import json
import sympy as s
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
signs=list(product([-1,1],repeat=3))
coeff=[-a+s.Rational(1,1)/s.sqrt(2)*b-a*b*c/s.sqrt(2) for a,b,c in signs]
labels=[''.join('+' if x==1 else '−' for x in sig) for sig in signs]
fig=plt.figure(figsize=(15,9),facecolor='white')
grid=fig.add_gridspec(2,2,height_ratios=[1.55,1],hspace=.48,wspace=.34)
ax=fig.add_subplot(grid[0,0])
vectors=[(0,1),(-1,-1),(1,0)]
colors=['#176b75','#bd611e','#534994']
for v,c in zip(vectors,colors):
 ax.add_patch(FancyArrowPatch((0,0),v,arrowstyle='-|>',mutation_scale=19,linewidth=2.5,color=c))
ax.text(.06,1.05,r'$\eta_1^0=(0,1,0)$',color=colors[0],fontsize=13)
ax.text(-1.13,-1.2,r'$\eta_2^0=(-1,-1,0)$',color=colors[1],fontsize=13)
ax.text(.61,-.24,r'$\eta_3^0=(1,0,0)$',color=colors[2],fontsize=13)
ax.axhline(0,color='#d3d9dd',lw=.8,zorder=-1);ax.axvline(0,color='#d3d9dd',lw=.8,zorder=-1)
ax.set_xlim(-1.3,1.45);ax.set_ylim(-1.4,1.4);ax.set_aspect('equal')
ax.set_xlabel('Original first coordinate');ax.set_ylabel('Original second coordinate')
ax.set_title('Original source frequencies in the third-coordinate-zero plane',fontsize=12,pad=12)
ax.text(.5,-.33,r'$H=1,\quad n=(0,0,1),\quad(r_1,r_2,r_3)=(1,\sqrt{2},1)$',
 transform=ax.transAxes,ha='center',fontsize=12)
bx=fig.add_subplot(grid[0,1])
bx.bar(range(8),[float(v) for v in coeff],color=['#176b75' if v>0 else '#bd611e' for v in coeff],width=.65)
bx.axhline(0,color='#44545d',lw=.8)
bx.set_xticks(range(8),labels);bx.set_ylim(-3.1,3.1)
bx.set_ylabel(r'Exact real value of $8i\,c_\sigma(\eta^0)$')
bx.set_xlabel(r'Original sign triple $(\sigma_1,\sigma_2,\sigma_3)$')
bx.set_title('All eight original coefficients are nonzero',fontsize=13,pad=12)
for idx,v in enumerate(coeff):
 label=s.latex(v)
 bx.text(idx,float(v)+(.14 if v>0 else -.14),'$'+label+'$',ha='center',va='bottom' if v>0 else 'top',fontsize=10)
bx.text(.5,-.29,r'$\min_\sigma |c_\sigma(\eta^0)|=(\sqrt{2}-1)/8$',transform=bx.transAxes,ha='center',fontsize=13)
cx=fig.add_subplot(grid[1,:]);cx.axis('off')
cx.text(.5,1.02,'Exact recovery and the orthogonal decomposition at equal first and second radii',
 ha='center',va='top',fontsize=15,color='#243b46')
cx.text(.02,.68,r'$r_1\ne r_2:\quad A_\eta T_\eta=I_E,\quad \dim_{\mathbb{C}}E=8$',fontsize=16)
cx.text(.02,.38,r'$r_1=r_2:\quad E=E_{\rm lost}\oplus E_{\rm seen},\quad \dim_{\mathbb{C}}E_{\rm lost}=\dim_{\mathbb{C}}E_{\rm seen}=4$',fontsize=15)
cx.text(.02,.07,r'$A_\eta^+T_\eta=P_{\rm seen},\quad \ker T_\eta=\operatorname{span}\{U_\sigma:\sigma_1=\sigma_2\}$',fontsize=15)
fig.suptitle('The complete tensor observation keeps every original frequency and coefficient',fontsize=18,y=.98)
fig.subplots_adjust(top=.9,bottom=.16,left=.07,right=.97)
fig.text(.5,.074,'SP1–SP33: full trilinear form, coefficient derivation, Lebesgue angle measure and inverse proof.',ha='center',fontsize=11)
fig.text(.5,.045,'Human source: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex739–821. The exact correction and rank classification are editorial derivations.',ha='center',fontsize=10)
fig.text(.5,.019,'The bar heights evaluate exact radical expressions; they are not a numerical fluid trajectory. The preceding averaging construction remains separate.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(HERE/f'original-cascade-spin-frame.{ext}',dpi=160,facecolor='white')
data=dict(base_frequencies=[[0,1,0],[-1,-1,0],[1,0,0]],H=1,n=[0,0,1],
 coefficients=[dict(signs=list(sig),eight_i_c_exact=str(v),eight_i_c_evaluation=float(v)) for sig,v in zip(signs,coeff)],
 proof='ORIGINAL_CASCADE_SPIN_FRAME_20261010.md SP1–SP33',
 source='Terence Tao arxiv:1402.0290v3 navier-blowup.tex739–821')
(HERE/'original-cascade-spin-frame-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
