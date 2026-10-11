"""Reproduce the two new higher-star full-normalization calculations."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig,ax=plt.subplots(figsize=(9,24.5),dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0,9),ylim=(0,24.5));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,23.9,'Further higher-star proofs',ha='center',fontsize=25,fontweight='bold')
ax.text(4.5,23.35,'Exact quartic and point rings; every allowed higher coefficient',ha='center',fontsize=12)

def panel(y,title,conditions,quartic,point,locators,color):
    ax.add_patch(FancyBboxPatch((.55,y),7.9,6.85,boxstyle='round,pad=.02,rounding_size=.18',facecolor=color,edgecolor='#365675',linewidth=1.6))
    ax.text(4.5,y+6.35,title,ha='center',fontsize=19,fontweight='bold')
    ax.text(4.5,y+5.67,conditions,ha='center',va='center',fontsize=12,linespacing=1.5)
    ax.text(4.5,y+4.18,quartic,ha='center',va='center',fontsize=15,linespacing=1.65)
    ax.add_patch(FancyArrowPatch((4.5,y+3.15),(4.5,y+2.5),arrowstyle='-|>',mutation_scale=21,linewidth=1.6,color='#365675'))
    ax.text(4.5,y+1.62,point,ha='center',va='center',fontsize=14,linespacing=1.6)
    ax.text(4.5,y+.36,locators,ha='center',fontsize=10.5,color='#365675')

panel(15.9,'III* : high a₁, a₃ valuation three',
      'Every e = v(2) ≥ 1; v(a₁) ≥ 2, v(a₃) = 3\n'
      'Prepared v(a₂) ≥ 2, v(a₄) = 3; translate v(a₆) ≥ 5 to ≥ 6',
      'v(x) = 3/2; t = x² + a₄/c, v(t) = 15/4\n'
      'Full B₄ basis: 1, x/π, t/π³, xt/π⁵\n'
      'Uniformizer τ = xt/π⁵; i₄ = 9, D₄ = 6',
      'w = πλx; η = (y − w)/τ¹⁰\n'
      'Shifted error: v_F = 21; trace before division: 12\n'
      'Full B₈: constant valuation 1, trace valuation 2; different 4',
      '6.0Q.2: HS3–HS14; residue cancellation only; all e allowed','#edf4ff')

panel(8.5,'II* : a further range at e = 1',
      'v(a₁) ≥ 2, v(a₂) ≥ 2, v(a₃) ≥ 4\n'
      'v(a₄) ≥ 5, v(a₆) = 5 and v(b₂) = 4',
      'v(x) = 9/4\n'
      'Full B₄ basis: 1, x/π², x²/π⁴, x³/π⁶\n'
      'Uniformizer τ = x/π²; i₄ = 12, D₄ = 4',
      'w = λx²/π²; η = (y − w)/τ¹⁰\n'
      'Shifted error: v_F = 21; trace before division: 14\n'
      'Full B₈: constant valuation 1, trace valuation 4; different 8',
      '6.0Q.3: HS15–HS21; this panel includes exactly the stated range','#eaf7ef')

ax.text(4.5,7.72,'Complete index, orbit and conductor values',ha='center',fontsize=18,fontweight='bold')
columns=['range','d','M','D₄','D₈','i₄','i₈','δ','f']
rows=[['III* above','12','8','6','16','9','28','3','5'],
      ['II* above','14','9','4','16','12','34','4','6']]
table=ax.table(cellText=rows,colLabels=columns,colWidths=[.24]+[.075]*8,
               cellLoc='center',bbox=[.065,4.9/24.5,.87,2.25/24.5])
table.auto_set_font_size(False);table.set_fontsize(13)
for (r,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8)
    cell.set_facecolor('#e8f0fa' if r==0 else ('#f5f8fc' if r%2 else 'white'))
    if r==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,4.4,'Both: point index ℓ = 10, ε₄ = 3, ε₈ = 7 and ν = 0',ha='center',fontsize=13)
ax.text(4.5,3.95,'i₄ + ℓ = d + M − 1; d = M + 1 + δ = −Art(X/R)',ha='center',fontsize=14)
ax.text(4.5,3.15,'c = 1 + 2ζ, with ζ a primitive cube root; c² = −3.\n'
        'Base valuations v(π) = 1; quartic upper valuations v_F(π) = 4.\n'
        'Quadratic normalized constants/traces use v_F; differents use the upper point field.\n'
        'Dⱼ are base discriminant exponents; iⱼ are R-lengths, ℓ is a B₄-length.\n'
        'Calculations descend through the permitted finite unramified extension.',
        ha='center',va='center',fontsize=10.7,linespacing=1.5)
ax.text(4.5,1.85,'The universal remaining equality is still open',ha='center',fontsize=15,fontweight='bold')
ax.text(4.5,.96,'III* remains for v(a₁) ≥ 2 and v(a₃) ≥ 4.\n'
        'II* remains outside the second panel; all shorter even, II/III and I₀* ranges remain.\n'
        'The complete residual scope is stated in Section 6.0Q.4.',
        ha='center',va='center',fontsize=11.5,linespacing=1.65)
dest=Path(__file__).resolve().parents[1]/'assets/higher-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Further higher-star full normalization and conductor proofs'})
plt.close(fig)
print(dest.name)
