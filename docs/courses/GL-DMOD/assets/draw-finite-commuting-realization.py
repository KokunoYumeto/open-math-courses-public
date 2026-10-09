from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
HERE=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,9),facecolor='white')
grid=fig.add_gridspec(1,2,width_ratios=[1,1.35],wspace=.18)
ax=fig.add_subplot(grid[0,0]); bx=fig.add_subplot(grid[0,1])
for i in range(7):
    for j in range(7):
        color='#e7f4ed' if i<2 and j<3 else '#e8effa' if i>=2 else '#fae8d7'
        ax.add_patch(Rectangle((i-.43,j-.43),.86,.86,facecolor=color,edgecolor='#d4d9e0'))
        ax.text(i,j,f'({i},{j})',ha='center',va='center',fontsize=10,color='#1c344a')
ax.scatter([2,0],[0,3],marker='s',s=190,facecolors='none',edgecolors=['#2567a0','#bc7027'],linewidths=2.5,zorder=4)
ax.set_xlim(-.65,6.65); ax.set_ylim(-.65,6.65)
ax.set_aspect('equal'); ax.set_xticks(range(7)); ax.set_yticks(range(7))
ax.set_xlabel('β₁: exponent of z₁',fontsize=12); ax.set_ylabel('β₂: exponent of z₂',fontsize=12)
ax.set_title('Example of selected principal heads (G.4)\nz₁² and z₂³, assigned in this order',fontsize=13)
ax.text(.5,-.18,'Green: B = {(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)}\n'
        'All homogeneous indices and all base Taylor exponents remain allowed.\n'
        'The six elements are candidate generators; further relations may reduce them.',
        transform=ax.transAxes,ha='center',va='top',fontsize=10,linespacing=1.5)
bx.axis('off'); bx.set_xlim(0,1); bx.set_ylim(0,1)
def box(y,h,label,color):
    bx.add_patch(FancyBboxPatch((.03,y),.94,h,boxstyle='round,pad=.012',fc=color,ec='#42546a',lw=1.3))
    bx.text(.5,y+h/2,label,ha='center',va='center',fontsize=12,linespacing=1.45)
box(.76,.17,'Finite actual fibre (G.1–G.5)\nPrincipal relations Pᵢ = z^γᵢ eⱼᵢ + Aᵢ\nFinite remainder support B, including nilpotents','#eaf2fc')
box(.48,.19,'Convergent relative division (G.6–G.12)\n∥Aᵢ∥ < (1/8)cⱼᵢR_z^γᵢ,  ∥DE∥ ≤ 1/8\n(Q,S) = Σℓ≥0 (−DE)^ℓ DF\nActual common domain and factorial bounds','#f0f6e9')
box(.20,.19,'Whole-stalk realization (G.13–G.15)\nM₀ = Σ_(β,j)∈B A₀ z^β mⱼ;  M = Σ_(β,j)∈B A z^β mⱼ\nA₀: coefficients independent of z;  A=A₀[h⁻¹]\nNo singular-support section is discarded','#e6f5ec')
box(.015,.105,'Still open: bounded resolution, sectorial action,\ninfinite-order comparison and finite D-type embedding','#fff1dd')
for y1,y2 in [(.745,.69),(.465,.405),(.185,.13)]:
    bx.annotate('',xy=(.5,y2),xytext=(.5,y1),arrowprops=dict(arrowstyle='->',lw=1.8,color='#526579'))
fig.suptitle('Finite covector remainder support gives an actual coordinate-commuting-ring realization',fontsize=16,y=.99)
fig.subplots_adjust(bottom=.20,top=.88)
fig.text(.055,.04,'Exact proof locators: G.1–G.5. The input is the actual finite-lattice/finite-fibre premise (G.1), not a generic-stratum model.\n'
         'Human context: Kashiwara–Kawai, HolIII (1981), III.5.5, freely available author PDF. The full convergent argument is retained in the leaf.',fontsize=10,color='#465569')
fig.savefig(HERE/'finite-commuting-realization.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'finite-commuting-realization.svg',bbox_inches='tight')
(HERE/'finite-head-example.json').write_text(json.dumps({'heads':[[2,0],[0,3]],'assigned_order':[0,1],'finite_remainder':[[i,j] for j in range(3) for i in range(2)],'meaning':'Example of selected principal heads; the remainder list bounds candidate generators and does not assert a free rank-six module.','contractivity_bound':'1/8'},indent=2)+'\n',encoding='utf-8')
print('Rendered finite-commuting-realization.png and .svg')
