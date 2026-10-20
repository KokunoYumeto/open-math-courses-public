'Reproduce the two full-ring mechanisms of the third-four II-star argument.'
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig,ax=plt.subplots(figsize=(9,34),dpi=100)
fig.patch.set_facecolor('white');ax.set(xlim=(0,9),ylim=(0,34));ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,33.45,'II*: higher first, third valuation four',ha='center',fontsize=21,fontweight='bold')
ax.text(4.5,32.98,'Two full quartic rings; the same discriminant 16 and conductor 8',ha='center',fontsize=12.5)
def box(y,height,title,body,locator,color,size=11.5):
    ax.add_patch(FancyBboxPatch((.52,y),7.96,height,boxstyle='round,pad=.02,rounding_size=.17',facecolor=color,edgecolor='#365675',linewidth=1.5))
    ax.text(4.5,y+height-.4,title,ha='center',fontsize=15.5,fontweight='bold')
    ax.text(4.5,y+height/2-.03,body,ha='center',va='center',fontsize=size,linespacing=1.55)
    ax.text(4.5,y+.17,locator,ha='center',fontsize=10.2,color='#365675')
box(28.98,3.3,'The actual original preparation and the two coordinate changes',
    'v(π) = 1; e = v(2) ≥ 2; v(a₁) ≥ 3; v(a₂) ≥ 2\n'
    'v(a₃) = 4; v(a₄) ≥ 4; v(a₆) = 5; M = 9\n'
    'Original first, second or fourth coefficients may vanish\n'
    'The actual earlier RO2–RO4 x-shift gives v(a₄) ≥ 5 and preserves v(a₃) = 4\n'
    's = a₄/a₃; y = y′ + sx; a′₁ = a₁ + 2s; a′₂ = a₂ − sa₁ − s²\n'
    'a′₃ = a₃; a′₄ = 0; a′₆ = a₆; all needed bounds and Δ are preserved',
    'TF1–TF3; tests below use the actual transformed equation','#edf4ff',10.95)
box(25.78,2.65,'The exhaustive invariant alternatives after preparation',
    'v(b₂) ≥ 6; v(b₄) ≥ 7; v(b₆) = 8; b₈ = a₆b₂ + a₂a₃²\n'
    'Transformed v(a₂) = 2 gives v(b₈) = 10; transformed v(a₂) ≥ 3 gives v(b₈) ≥ 11\n'
    'Infinite b₂ is allowed in either case; infinite a₂ belongs to the second\n'
    'Unique Δ leader −27b₆²: d = 16; v(c₄) ≥ 12; v(j) ≥ 20',
    'TF4–TF6; q(X) = X⁴ + (b₂/3)X³ + b₄X² + b₆X + b₈/3','#eaf7ef',11.0)
box(21.41,3.82,'Case 1: v(b₈) = 10 gives the entire quartic field ring',
    'c² = −3, v(c) = 0 after a finite unramified cube-root extension\n'
    'Every root v(x) = 5/2; choose v(r) = 1 with v(r² − a₂) ≥ 3\n'
    't = cx² + ra₃\n'
    't² = b₂x³ + (3b₄ + 2cra₃)x² + 3b₆x + a₆b₂ + (a₂ + r²)a₃²\n'
    'Unique leader 3b₆x: v(t) = 21/4 forces degree and ramification four\n'
    'Full basis: 1, x/π², t/π⁵, xt/π⁷; τ = t/π⁵; B₄ = R[τ]\n'
    'Distinct classes 0, 1/2, 1/4, 3/4; i₄ = 2 + 5 + 7 = 14; D₄ = 4',
    'TF7–TF10; full lattice and uniformizer, with unit basis determinant c²','#edf4ff',10.8)
box(16.81,4.04,'Case 1: the complete point shift and the whole point ring',
    'A = a₁x + a₃; G = x³ + a₂x² + a₆; y² + Ay − G = 0\n'
    'Choose unit k with v(k²ra₃/c + a₆) ≥ 6; w = kx\n'
    'E = w² + Aw − G = (k²/c)t − (k²ra₃/c + a₆) − x³\n'
    '                                      + (ka₁ − a₂)x² + ka₃x\n'
    'Unique error leader (k²/c)t: v_F(E) = 21; v_F(A + 2w) = 16\n'
    'η = (y − w)/τ¹⁰; normalized constant = 1; normalized trace = 6\n'
    'Full B₈ = B₄[η]; point index 10; exact relative different 12\n'
    'D₈ = 2·4 + 12 = 20; i₈ = 2·14 + 10 = 38',
    'TF11–TF15; v_F = 4v; no exact square-root assumption in the point shift','#fff5e6',10.9)
box(12.21,4.04,'Case 2: v(b₈) ≥ 11 gives a base factor and a full cubic ring',
    'q(π³T)/π¹¹ has integral coefficients and a linear reduction with unit derivative\n'
    'Hensel gives ρ ∈ π³R; q = (X − ρ)g; g = X³ + c₂X² + c₁X + c₀\n'
    'v(c₂) ≥ 3; v(c₁) ≥ 6; v(c₀) = 8; every cubic root v(x) = 8/3\n'
    'u = π³/x; u³ + (c₁π³/c₀)u² + (c₂π⁶/c₀)u + π⁹/c₀ = 0\n'
    'Eisenstein: full C = R[u], basis 1, x/π², x²/π⁵; cubic index 7; different 2\n'
    'g(ρ) = q′(ρ) has value 8; exact product cokernel R/(g(ρ))\n'
    'Full B₄ = R × C; i₄ = 8 + 7 = 15; D₄ = 32 − 30 = 2',
    'TF16–TF21; actual reciprocal uniformizer and complete cokernel proof','#eaf7ef',10.8)
box(7.85,3.81,'Case 2: both full quadratic point rings and their actual towers',
    'At x = ρ and at v(x) = 8/3: v(A) = 4 and v(G) = 5\n'
    'Base: η₀ = y/π²; normalized constant 1, trace 2; full R[η₀]\n'
    'Point index 2; different D₂ = 4 (2e + 1 ≥ 5 > 4)\n'
    'Cubic: η₃ = y/u⁷; cubic normalized constant 1, trace 5; full C[η₃]\n'
    'Point index 7; relative different 10 (6e + 1 ≥ 13 > 10)\n'
    'Full B₈ = R[η₀] × C[η₃]; D₆ = 2·2 + 10 = 14; D₈ = 4 + 14 = 18\n'
    'Both residue degrees one: weighted point index 2 + 7 = 9; i₈ = 39',
    'TF22–TF23; all lengths and towers come from constructed full rings','#edf4ff',10.8)
tb=ax.table(cellText=[['10','14','4','10','20','38','3 / 7'],['≥ 11','15','2','9','18','39','2 / 6']],
    colLabels=['v(b₈)','i₄','D₄','Σ fⱼℓⱼ','D₈','i₈','ε₄ / ε₈'],cellLoc='center',bbox=[.05,5.94/34,.9,1.33/34])
tb.auto_set_font_size(False);tb.set_fontsize(11.7)
for (row,col),cell in tb.get_celld().items():
    cell.set_edgecolor('#9cb0c7');cell.set_linewidth(.8);cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0:cell.get_text().set_fontweight('bold')
ax.text(4.5,5.36,'Both: ν = 0; δ = 32 − i₈ + i₄ − 2 = 6; f(E/K) = 2 + δ = 8',ha='center',fontsize=12)
ax.text(4.5,4.87,'i₄ + Σ fⱼℓⱼ = 24 = d + 8; −Art(X/R) = 9 − 1 + 8 = 16 = d',ha='center',fontsize=12)
ax.text(4.5,3.75,
    'Wild action: quartic transitivity in Case 1, degree-two base point orbit in Case 2.\n'
    'The actual earlier quaternion proof gives zero rank-two inertia invariants.\n'
    'Base valuations v(π) = 1; quartic v_F = 4v; cubic v_C = 3v.\n'
    'D values are base discriminant exponents; relative differents use upper point valuations.\n'
    'Order indices are R-lengths; point indices use factor rings; all residue degrees are one.',
    ha='center',va='center',fontsize=10.3,linespacing=1.55)
ax.text(4.5,1.64,
    'Full proof: Lesson 8, Sections 6.0AA.1–8, TF1–TF25.\nAll TF1 preparations under the displayed hypotheses.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.\nhttps://www.jmilne.org/math/CourseNotes/ANT.pdf',
    ha='center',va='center',fontsize=10.15,linespacing=1.55)
fig.canvas.draw();renderer=fig.canvas.get_renderer()
for label in ax.texts:
    bounds=label.get_window_extent(renderer)
    assert bounds.x0>=0 and bounds.x1<=900 and bounds.y0>=0 and bounds.y1<=3400,label.get_text()
dest=Path(__file__).resolve().parents[1]/'assets/third-four-II-star-proof-map.png'
fig.savefig(dest,dpi=100,metadata={'Title':'Higher-first II-star with third valuation four: both full-ring mechanisms'})
plt.close(fig);print(dest.name)
