"""Reproduce both full-ring alternatives in the e1/d15 III-star proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax=plt.subplots(figsize=(9,29),dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0,9),ylim=(0,29));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,28.45,'III* at discriminant valuation fifteen',ha='center',fontsize=23,fontweight='bold')
ax.text(4.5,27.91,'Two exhaustive full-ring alternatives; one conductor',ha='center',fontsize=13)

def box(y,h,title,body,locator,color,size=13):
    ax.add_patch(FancyBboxPatch((.55,y),7.9,h,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
    ax.text(4.5,y+h-.44,title,ha='center',fontsize=17,fontweight='bold')
    ax.text(4.5,y+h/2-.08,body,ha='center',va='center',fontsize=size,linespacing=1.65)
    ax.text(4.5,y+.19,locator,ha='center',fontsize=10.3,color='#365675')

box(24.62,2.65,'Actual translated preparation',
    'e = v(2) = 1; v(a₁), v(a₂) ≥ 2; v(a₃) ≥ 4; v(a₄) = 3\n'
    'Apply Lemma 6.0D, raising v(a₆) to ≥ 6\n'
    'On translated coefficients: v(b₂) ≥ 5 ⇔ d = 15; M = 8',
    '6.0S.1: DF1–DF5; every higher or infinite allowed coefficient valuation','#edf4ff')
ax.add_patch(FancyArrowPatch((4.5,24.47),(4.5,23.99),arrowstyle='-|>',mutation_scale=20,linewidth=1.5,color='#365675'))
box(19.72,4.15,'Quartic shifts and the scalar branch test',
    'v(x) = 3/2; t = x² + a₄/c; s = t − uπ⁴; T = s − ρπ³x\n'
    'u and ρ use residue square roots only; v(s) ≥ 9/2\n'
    'U = uπ⁴ + a₄(1 − 1/c); v(U) = 4\n'
    'D = 2U + a₁a₃; v(D) = 5\n'
    'T² + JT + Bx + C = 0; v(J) = 5, v(B) ≥ 8, v(C) ≥ 10\n'
    'The scalars B and C are defined in DF13; c² = −3',
    '6.0S.2: DF6–DF14; the two cases below are alternatives','#edf4ff',12.5)

# Both arrows leave the common calculation; no arrow joins the alternatives.
ax.plot([.31,.31],[10.24,19.72],color='#365675',linewidth=1.5)
ax.plot([.31,4.5],[19.58,19.58],color='#365675',linewidth=1.5)
ax.plot([4.5,4.5],[19.58,19.72],color='#365675',linewidth=1.5)
for yy in (16.1,10.24):
    ax.add_patch(FancyArrowPatch((.31,yy),(.54,yy),arrowstyle='-|>',mutation_scale=17,linewidth=1.5,color='#365675'))

box(13.12,5.95,'Alternative A: v(B) = 8',
    'v(T) = 19/4 forces a totally ramified quartic field F\n'
    'Full B₄ basis: 1, x/π, T/π⁴, xT/π⁶\n'
    'v_F(π) = 4; τ = xT/π⁶; i₄ = 11; D₄ = 8\n'
    'w₁ = πλx; V = −B/π⁴; v(μ²V − U) ≥ 5; w₂ = μT/π²\n'
    'Second error has v_F = 23; second trace has v_F = 15\n'
    'η = (y − w₁ − w₂)/τ¹¹; full B₈ = B₄[η]\n'
    'Normalized constant 1, trace 4; upper relative different 8\n'
    'Point index ℓ = 11; D₈ = 24; i₈ = 33',
    '6.0S.3, 6.0S.5–6: DF15, DF21–DF28','#eaf7ef',12.7)

box(6.61,5.87,'Alternative B: v(B) ≥ 9',
    'v(T) ≥ 5; X = x/π; θ = T/π⁵\n'
    'Candidate order '+r'$\mathcal{C}_4$'+' has basis 1, X, θ, Xθ\n'
    'Residue X² = 0; the quadratic quotient in θ is separable\n'
    'Lift two idempotents after a finite unramified extension\n'
    'Full B₄ = O(F₁) × O(F₂); v_Fⱼ(π) = 2; X uniformizer\n'
    'Each quadratic factor has discriminant 3; i₄ = 12; D₄ = 6\n'
    'ηⱼ = (y − w₁)/X⁵; constant 1, trace ≥ 3; upper different 5\n'
    'Point indices ℓ₁ = ℓ₂ = 5; D₈ = 22; i₈ = 34',
    '6.0S.4–5, 6.0S.7: DF16–DF23, DF29–DF30','#fff5e6',12.7)

cols=['quartic','i₄','i₈','D₄','D₈','Σℓⱼ','ε₄','ε₈','δ','f']
rows=[['field','11','33','8','24','11','3','7','6','8'],
      ['two quadratics','12','34','6','22','5 + 5','2','6','6','8']]
table=ax.table(cellText=rows,colLabels=cols,colWidths=[.2]+[.078]*9,
    cellLoc='center',bbox=[.045,4.72/29,.91,1.38/29])
table.auto_set_font_size(False);table.set_fontsize(11.3)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8)
    cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,4.31,'Both: ν = 0; i₄ + Σℓⱼ = 22 = d + M − 1',ha='center',fontsize=13)
ax.text(4.5,3.84,'−Art(X/R) = M + 1 + δ = 15 = d',ha='center',fontsize=16,fontweight='bold')
ax.text(4.5,2.87,
    'Base valuations v(π) = 1; quartic valuations use v_F(π) = 4 or v_Fⱼ(π) = 2.\n'
    'Normalized quadratic constants and traces use their quartic field valuation.\n'
    'Relative different exponents use the upper point field valuation.\n'
    'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓⱼ are factor-ring lengths.\n'
    'Finite unramified extensions preserve all numbers and permit the displayed product.',
    ha='center',va='center',fontsize=10.6,linespacing=1.6)
ax.text(4.5,1.65,'This completes the e = 1 III* range together with Section 6.0R',ha='center',fontsize=13,fontweight='bold')
ax.text(4.5,.96,'Higher-e III* and every other residual family still require their full proofs.\n'
    'The universal NF24 identity and distinct reviews remain required.\n'
    'Exact conditions and proof locators: Lesson 8, Sections 6.0S.1–9.',
    ha='center',va='center',fontsize=11.3,linespacing=1.7)
dest=Path(__file__).resolve().parents[1]/'assets/III-star-d15-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Two full-ring alternatives for the discriminant-fifteen III-star proof'})
plt.close(fig)
print(dest.name)
