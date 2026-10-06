"""Reproduce the exact U020 radial threshold diagram; no sampled kernels."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
                     'svg.hashsalt':'AN03-U020-dimensional-resonance-264'})
fig, ax = plt.subplots(figsize=(12.2, 10.5))
fig.patch.set_facecolor('#fafaf7')
ax.set_facecolor('#fafaf7')
colors={'negative power':'#f1d2c8','logarithm':'#f4e3af',
        'odd cusp':'#d4e5f1','even logarithmic cusp':'#dce8d5'}
cells=[]
for n in range(1,7):
    for nu in range(4):
        p=2*nu+2-n
        kind=('negative power' if p<0 else 'odd cusp') if n%2 else (
              'negative power' if p<0 else 'logarithm' if p==0 else 'even logarithmic cusp')
        term=rf'$A_{{{n},{nu}}}r^{{{p}}}$' if n%2 or p<0 else (
             rf'$A^{{\log}}_{{{n},{nu}}}\log r$' if p==0 else rf'$A^{{\log}}_{{{n},{nu}}}r^{{{p}}}\log r$')
        # The grid is the exact first nonsmooth term, never the whole kernel.
        x,y=nu,6-n
        ax.add_patch(Rectangle((x,y),1,1,facecolor=colors[kind],edgecolor='white',linewidth=3))
        ax.text(x+.5,y+.69,term,ha='center',va='center',fontsize=15)
        reg='unbounded' if p<=0 else rf'$C^{{{p-1}}}$, not $C^{{{p}}}$'
        ax.text(x+.5,y+.34,reg,ha='center',va='center',fontsize=11)
        cells.append({'n':n,'nu':nu,'p':p,'classification':kind,'sharp_regularity':reg})
ax.set_xlim(-.3,4);ax.set_ylim(-.2,6.5)
ax.set_xticks([i+.5 for i in range(4)],[rf'$\nu={i}$' for i in range(4)],fontsize=15)
ax.xaxis.tick_top()
ax.set_yticks([6-n+.5 for n in range(1,7)],[rf'$n={n}$' for n in range(1,7)],fontsize=15)
ax.tick_params(length=0,pad=9)
for spine in ax.spines.values():spine.set_visible(False)
fig.suptitle('The first nonsmooth radial term, with every regular term retained',
             fontsize=19,fontweight='bold',y=.968)
fig.text(.5,.921,r'$p=2\nu+2-n\quad;\quad F_\nu^{(n)}=\mathcal{F}^{-1}\!\left[\nu!(|\xi|^2-z)^{-\nu-1}\right]$',
         ha='center',fontsize=16)
fig.subplots_adjust(left=.095,right=.96,top=.855,bottom=.325)
fig.text(.07,.269,'Complete coefficients, not rescaled kernels:',fontsize=12,fontweight='bold')
fig.text(.07,.221,r'$A_{n,\nu}=\frac{(-1)^\nu\nu!}{(n-2)\sigma_{n-1}\prod_{l=1}^{\nu}[2l(2l+2-n)]}\quad(n\ \mathrm{odd})$',fontsize=16)
fig.text(.07,.158,r'$A^{\log}_{2d,\nu}=\frac{(-1)^{\nu-d+2}\nu!}{2\pi^d4^\nu(\nu-d+1)!\,\nu!}\quad(\nu\geq d-1)$',fontsize=16)
fig.text(.07,.105,r'For $n=2d$, $\nu<d-1$: $A_{2d,\nu}=\frac{\nu!(d-\nu-2)!}{4^{\nu+1}\pi^d\nu!}$.',fontsize=15)
fig.text(.07,.053,r'$(-\Delta-z)^{\nu+1}F_\nu^{(n)}=\nu!\delta_0$: the critical point mass remains.',fontsize=14)
fig.text(.07,.019,'Exact proof: U020, HD13–HD20. Full regular coefficients and remainders: HD15–HD19.',fontsize=10,color='#414141')
stem=OUT/'hadamard-dimensional-resonance'
fig.savefig(stem.with_suffix('.png'),dpi=200,metadata={'Software':'U020 exact reproducible diagram'})
fig.savefig(stem.with_suffix('.svg'),metadata={'Date':None,'Creator':'U020 exact reproducible diagram'})
plt.close(fig)
params={'schema_version':1,'kind':'exact discrete threshold diagram, not a kernel plot',
        'source_lesson':'elliptic-hadamard-parametrices.md','proof_locators':'HD13–HD20',
        'parameter_domain':'z outside [0,infinity)','normalization':'original Fourier inverse (2pi)^(-n), full nu!',
        'dimension_range':[1,6],'nu_range':[0,3],'cells':cells,'complete_regular_terms_retained':True,
        'coefficient_source':'Full uncancelled formulas HD17, HD18 and HD19',
        'figure_size_inches':[12.2,10.5],'dpi':200,'colors':colors}
stem.with_suffix('.parameters.json').write_text(json.dumps(params,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
