"""Reproduce the full ramification-one II-star exhaustion and its new order calculation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(9, 31), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 9), ylim=(0, 31)); ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.text(4.5, 30.48, 'Every II* preparation at e = 1', ha='center', fontsize=22, fontweight='bold')
ax.text(4.5, 29.98, 'Coordinate preparation, full rings, exact indices and conductor', ha='center', fontsize=12.8)

def box(y, height, title, body, locator, color, size=11.5, x=.52, width=7.96):
    ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=.02,rounding_size=.17',
        facecolor=color,edgecolor='#365675',linewidth=1.5))
    center=x+width/2
    ax.text(center,y+height-.39,title,ha='center',fontsize=15.5 if width>5 else 13.5,fontweight='bold')
    ax.text(center,y+height/2-.05,body,ha='center',va='center',fontsize=size,linespacing=1.55)
    ax.text(center,y+.17,locator,ha='center',fontsize=10.0 if width>5 else 9.6,color='#365675')

box(26.0,3.27,'The actual preparation and its integral normalization',
    'v(π) = 1; e = v(2) ≥ 1; v(a₁) ≥ 1; v(a₂) ≥ 2\n'
    'v(a₃) ≥ 3; v(a₄) ≥ 4; v(a₆) = 5; M = 9\n'
    'If v(a₄) = 4, choose r = π²λ with a₄/π⁴ + 3λ² = 0 in the residue field\n'
    'Otherwise r = 0. Set x = x′ + r, y = y′\n'
    'a′₁ = a₁; a′₂ = a₂ + 3r; a′₃ = a₃ + a₁r\n'
    'a′₄ = a₄ + 2a₂r + 3r²; a′₆ = a₆ + a₄r + a₂r² + r³',
    '6.0Z.1–2: RO1–RO4; finite residue-field squaring and every added term','#edf4ff',10.9)
box(22.5,2.95,'At e = 1: the new normalized range',
    'First valuation ≥ 2, third ≥ 4, fourth ≥ 5, sixth = 5\n'
    'Normalized b₂ has value ≥ 5, including infinity\n'
    'v(b₄) ≥ 6; v(b₆) = 7; v(b₈) ≥ 10\n'
    'Unique Δ leader −27b₆²: d = 14; v(c₄) ≥ 9; v(j) ≥ 13\n'
    'Quartic q(X) = X⁴ + (b₂/3)X³ + b₄X² + b₆X + b₈/3\n'
    'A = a₁x + a₃; G = x³ + a₂x² + a₄x + a₆; y² + Ay − G = 0',
    '6.0Z.3: RO5–RO7; infinite permitted coefficients included','#eaf7ef',11.4)
box(18.17,3.8,'A base root and the entire cubic integer ring',
    'q(π³T)/π¹⁰ reduces to a linear polynomial with unit derivative\n'
    'Hensel gives ρ ∈ π³R; q = (X − ρ)g, g = X³ + c₂X² + c₁X + c₀\n'
    'v(c₂) ≥ 3; v(c₁) ≥ 6; v(c₀) = 7; every cubic root v(x) = 7/3\n'
    'u = x/π²; the u-polynomial is Eisenstein\n'
    'Entire cubic ring C = R[u]; residue degree one; cubic order index 2 + 4 = 6\n'
    'Cubic derivative values 2, ≥ 7, ≥ 6: different and base discriminant = 2\n'
    'Full quartic normalization B₄ = R × C; D₄ = 2',
    '6.0Z.4: RO8–RO11; coefficientwise valuation classes prove the full ring','#edf4ff',10.9)
box(14.62,3.0,'The exact quartic product-order cokernel',
    'g(ρ) = q′(ρ) = 4ρ³ + b₂ρ² + 2b₄ρ + b₆ has value 7\n'
    'Quartic order → R ⊕ R[X]/g → R/(g(ρ)) → 0\n'
    'The last map is (a,b) ↦ a − b(ρ); interpolation proves its kernel\n'
    'Product-order index 7 + cubic normalization index 6 = i₄ = 13\n'
    'Discriminant check: 2d − 2i₄ = 28 − 26 = D₄ = 2',
    '6.0Z.5: RO12–RO13; injectivity, exact cokernel and normalization proved','#fff5e6',11.1)
box(10.56,3.5,'Base factor: degree 1 → 2',
    'x = ρ; v(A) ≥ 4; v(G) = 5\n'
    'η₀ = y/π²\n'
    'Normalized constant = 1\n'
    'Normalized trace ≥ 2\n'
    'Full point ring R[η₀]\n'
    'Point index ℓ₀ = 2\n'
    'Different = D₂ = 3',
    '6.0Z.6: RO14–RO15','#edf4ff',11.05,x=.52,width=3.79)
box(10.56,3.5,'Cubic factor: degree 3 → 6',
    'v(x) = 7/3; v(A) ≥ 4; v(G) = 5\n'
    'η₃ = y/u⁷; u is the cubic uniformizer\n'
    'Cubic normalized constant = 1\n'
    'Cubic normalized trace ≥ 5\n'
    'Full point ring C[η₃]\n'
    'Point index ℓ₃ = 7\n'
    'Relative different = 7; D₆ = 11',
    '6.0Z.6: RO14–RO15','#eaf7ef',10.65,x=4.69,width=3.79)
for start in (2.42,6.58):
    ax.add_patch(FancyArrowPatch((start,10.47),(4.5,10.02),arrowstyle='-|>',mutation_scale=14,color='#365675',linewidth=1.4))
box(6.82,2.99,'Full point product and conductor',
    'B₈ = R[η₀] × C[η₃]; D₈ = 3 + 11 = 14\n'
    'Both residue degrees = 1: weighted point index 2 + 7 = 9\n'
    'i₈ = 2i₄ + 9 = 35; ε₄ = 2; ε₈ = 6; ν = 0\n'
    'δ = 28 − 35 + 13 − 2 = 4; f(E/K) = 2 + δ = 6\n'
    'i₄ + 9 = 22 = d + 8; −Art(X/R) = 9 − 1 + 6 = 14 = d',
    '6.0Z.6–7: RO15–RO16; the degree-two orbit forces wild action','#edf4ff',11.5)
ax.text(4.5,6.36,'The full exhaustion tests the original first and third coefficients',ha='center',fontsize=12.0,fontweight='bold')
table=ax.table(cellText=[
    ['v(a₁) = 1','11','3','6.0O.5'],
    ['v(a₁) ≥ 2, v(a₃) = 3','12','4','6.0O.6'],
    ['v(a₁) ≥ 2, v(a₃) ≥ 4','14','6','6.0Q.3 or 6.0Z.3–7']],
    colLabels=['Original e = 1 preparation','d','f','Full written proof'],
    colWidths=[.40,.09,.09,.42],cellLoc='center',bbox=[.05,4.27/31,.9,1.55/31])
table.auto_set_font_size(False);table.set_fontsize(10.7)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8);cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0: cell.get_text().set_fontweight('bold')
ax.text(4.5,3.58,
    'Final row: normalize first; test the new b₂. Value 4 uses 6.0Q.3; ≥ 5 uses this proof.\n'
    'Infinite first/third valuations follow the same original-coefficient alternatives.\n'
    'Higher e ≥ 2, original v(a₁) = 2 and v(a₃) ≥ 4: the shift gives every FT1 hypothesis.\n'
    'The two FT1 conductor tests use the transformed third coefficient.',
    ha='center',va='center',fontsize=10.5,linespacing=1.55)
ax.text(4.5,2.1,
    'Base valuations v(π) = 1; cubic valuations v_C(π) = 3.\n'
    'D₂, D₄, D₆, D₈ are base discriminant exponents; relative differents use point valuations.\n'
    'i₄, i₈ are R-lengths; ℓ₀, ℓ₃ use the factor integer rings. Both residue degrees are one.',
    ha='center',va='center',fontsize=10.15,linespacing=1.6)
ax.text(4.5,.81,
    'Full proof: Lesson 8, Sections 6.0Z.1–8, RO1–RO17. The displayed family-specific hypotheses apply.\nHigher-e complementary II* ranges and other additive cases are outside these hypotheses.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
    ha='center',va='center',fontsize=10.1,linespacing=1.6)
fig.canvas.draw();renderer=fig.canvas.get_renderer()
for label in ax.texts:
    bounds=label.get_window_extent(renderer)
    assert bounds.x0>=0 and bounds.x1<=900 and bounds.y0>=0 and bounds.y1<=3100,label.get_text()
dest=Path(__file__).resolve().parents[1]/'assets/ramification-one-II-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Every II-star preparation at ramification one: full rings and exhaustion'})
plt.close(fig);print(dest.name)
