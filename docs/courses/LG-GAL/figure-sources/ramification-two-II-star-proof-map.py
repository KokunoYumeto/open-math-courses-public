"""Reproduce the complete e=2 II-star proof mechanisms, with exact public proof locators."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9,46),dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0,9),ylim=(0,46)); ax.axis('off')
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.text(4.5,45.42,'II*: all remaining ramification-index-two cases',ha='center',fontsize=18.5,fontweight='bold')
ax.text(4.5,44.92,'Four exhaustive cases; three full quartic rings; discriminant 18 and conductor 10',ha='center',fontsize=11.8)

def box(y,height,title,body,locator,color,size=11.2):
    ax.add_patch(FancyBboxPatch((.48,y),8.04,height,boxstyle='round,pad=.02,rounding_size=.15',facecolor=color,edgecolor='#365675',linewidth=1.4))
    ax.text(4.5,y+height-.38,title,ha='center',fontsize=14.2,fontweight='bold')
    ax.text(4.5,y+height/2-.04,body,ha='center',va='center',fontsize=size,linespacing=1.48)
    ax.text(4.5,y+.16,locator,ha='center',fontsize=10,color='#365675')

box(40.93,3.36,'Actual original preparation and fourth-coefficient normalization',
    'v(π) = 1; e = v(2) = 2; v(a₁) ≥ 3; v(a₂) ≥ 2\n'
    'v(a₃) ≥ 5; v(a₄) ≥ 4; v(a₆) = 5; all four lower-bound coefficients may vanish\n'
    'Actual RO2–RO4 shift: x = x′ + rₓ, v(rₓ) ≥ 2; a₃ changes by a₁rₓ\n'
    'Transformed bounds persist and v(a₄) ≥ 5; all tests use these actual coefficients\n'
    'v(b₂) ≥ 6, v(b₄) ≥ 7, v(b₆) = 9, v(b₈) ≥ 10; M = 9\n'
    'Unique Δ leader −27b₆²: d = 18; v(c₄) ≥ 12; v(j) ≥ 18',
    'RT1–RT4; actual earlier model/minimality/Euler/local-field providers in Section 6.0AB.1','#edf4ff',10.95)
box(37.50,2.93,'The four exhaustive cases and the actual torsion quartic',
    'A: v(a₄) = 5, v(b₂) ≥ 7          B: v(a₄) ≥ 6, v(b₂) = 6\n'
    'C: v(a₄) ≥ 6, v(b₂) ≥ 7          D: v(a₄) = 5, v(b₂) = 6\n'
    'Infinite a₄ or b₂ belongs to its indicated lower-bound case\n'
    'q(X) = X⁴ + (b₂/3)X³ + b₄X² + b₆X + b₈/3\n'
    'After a finite unramified extension: c = 1 + 2ζ, c² = −3, v(c) = 0, v(c + 3) = 2',
    'RT5–RT8; A(x) = a₁x + a₃, G(x) = x³ + a₂x² + a₄x + a₆','#eaf7ef',11)
box(33.44,3.56,'Case A: the whole mixed quartic lattice',
    'v(b₈) = 10; every v(x) = 5/2; t = cx² + a₄\n'
    'M₀ = 3b₄ + 2ca₄ = 3a₁a₃ + 2(c + 3)a₄, v(M₀) ≥ 8\n'
    'C₀ = b₈ + a₄² = a₆b₂ − a₁a₃a₄ + a₂a₃², v(C₀) ≥ 12\n'
    't² = b₂x³ + M₀x² + 3b₆x + C₀; unique leader 3b₆x\n'
    'v(t) = 23/4 forces degree and ramification four\n'
    'Full basis: 1, x/π², t/π⁵, xt/π⁸; τ = xt/π⁸; B₄ = R[τ]\n'
    'Distinct fractions 0, 1/2, 3/4, 1/4; i₄ = 15, D₄ = 6',
    'RT9–RT11; coefficient M₀ is distinct from the component count M = 9','#edf4ff',10.95)
box(29.37,3.56,'Case A: full point error, trace and Eisenstein ring',
    'Choose unit k with v(k²a₄/c + a₆) ≥ 6; w = kx\n'
    'E = w² + A(x)w − G(x) = (k²/c)t − (k²a₄/c + a₆) − x³\n'
    '                                      + (ka₁ − a₂)x² + (ka₃ − a₄)x\n'
    'Unique t leader: v(E) = 23/4; v(A(x) + 2w) = 9/2\n'
    'v_F = 4v; η = (y − w)/τ¹¹; normalized constant 1, trace 7\n'
    'Full B₈ = B₄[η]; point index 11; relative different min(17,14) = 14\n'
    'D₈ = 2·6 + 14 = 26; i₈ = 2·15 + 11 = 41',
    'RT12–RT14; residue cancellation is a unit lift, never an assumed exact square root','#fff5e6',10.95)
box(25.78,3.08,'Case B: the full power lattice and actual quadratic point shift',
    'v(b₈) = 11; every v(x) = 11/4 forces a totally ramified quartic field\n'
    'Full basis: 1, x/π², x²/π⁵, x³/π⁸; τ = x³/π⁸; i₄ = 15, D₄ = 6\n'
    'Choose unit k with v(k²b₈/(3π⁶) + a₆) ≥ 6; w = kx²/π³\n'
    'Full reduced E = J₃x³ + J₂x² + J₁x + J₀\n'
    'v(J₃) ≥ 0, v(J₂) ≥ 2, v(J₁) = 3, v(J₀) ≥ 6; unique J₁x leader\n'
    'v(E) = 23/4, trace 9/2; full point index 11/different 14; D₈ = 26, i₈ = 41',
    'RT15–RT16 give all four signed J coefficients, including the complete constant','#edf4ff',10.95)
box(22.00,3.28,'Case C: four actual Hensel factors and four full point rings',
    'q(π³U)/π¹² reduces to U⁴ + αU + γ with α ≠ 0: derivative α is a unit\n'
    'Finite unramified splitting and Hensel give xⱼ = π³Uⱼ, v(xⱼ) ≥ 3\n'
    'Every pair difference has value 3; a zero root is permitted\n'
    'Full B₄ = R⁴; exact Vandermonde index 6·3 = 18; D₄ = 0\n'
    'At each xⱼ: v(G) = 5, v(A) ≥ 5; ηⱼ = yⱼ/π²\n'
    'Four full Eisenstein point rings, constant 1/trace ≥ 3; index 2/different 5 each\n'
    'Full B₈ = ∏ R[ηⱼ]; weighted point index 8; D₈ = 20, i₈ = 44',
    'RT17–RT19; pairwise unit residue differences establish the full product index','#eaf7ef',10.9)
box(18.24,3.26,'Case D: the exact residual equation and its two alternatives',
    'Every v(x) = 5/2; t = cx² + a₄; v(C₀) = 11, v(M₀) ≥ 8\n'
    'Choose v(β) = 3 with C = C₀ − β²a₄/c of value ≥ 12; s = t − βx\n'
    'P = b₂ − 2cβ has value 5; L = 3b₆ − 2βa₄ + β³/c has value ≥ 9\n'
    'Complete relation: s² = Px³ + M₀x² + Lx + (β²/c)s + C\n'
    'A unique-minimum contradiction proves v(s) > 11/2\n'
    'D1: v(L) = 9 gives v(s) = 23/4          D2: v(L) ≥ 10 gives v(s) ≥ 6',
    'RT20; every coefficient and constant retained; L = 0 belongs to D2','#fff5e6',10.95)
box(14.53,3.20,'Case D1: the necessary second point cancellation',
    'Full quartic basis: 1, x/π², s/π⁵, xs/π⁸; τ = xs/π⁸; i₄ = 15, D₄ = 6\n'
    'The first error E(kx) has value 11/2: its even value is not a full-ring proof\n'
    'Choose unit λ with v(λ²L/π⁶ + k²β/c) ≥ 4; w = kx + λs/π³\n'
    'E(w) = E(kx) + 2kxλs/π³ + A(x)λs/π³ + λ²s²/π⁶\n'
    'Final s coefficient (k² + λ²β²/π⁶)/c is a unit:\n'
    'cL − β³ = 3cb₆ − 2cβa₄ has exact value 9\n'
    'v(E(w)) = 23/4, trace 9/2; full point index 11/different 14; D₈ = 26, i₈ = 41',
    'RT21–RT24; all competing terms and both cross terms are strictly higher','#edf4ff',10.85)
box(10.43,3.59,'Case D2: construct the whole rank-four order before splitting it',
    'ξ = x/π², S = s/π⁶; O = R1 ⊕ Rξ ⊕ RS ⊕ RξS\n'
    'Exact relations: ξ² = aξ + b + d₀S; S² = US + V + Wξ + HSξ\n'
    'v(a) = v(b) = v(H) = 1, v(d₀) = 2; U is a unit, V,W integral\n'
    'Full multiplication by ξ and S preserves every basis vector: O is an order\n'
    'Unit triangular determinant c², denominators π²,π⁶,π⁸: index 16\n'
    'Residue: ξ̄² = 0; Z = S̄ + (W̄/Ū)ξ̄; Z² − ŪZ − V̄ = 0 is separable\n'
    'After finite unramified splitting: O/πO = k[ξ̄]/(ξ̄²) × k[ξ̄]/(ξ̄²)',
    'RT25–RT31 give complete signed U₀,V₀,W₀ and normalized coefficients, plus closure','#eaf7ef',10.85)
box(6.50,3.42,'Case D2: lift idempotents, prove DVRs, then construct both point rings',
    'F(z) = z² − z; zₙ₊₁ = zₙ − (2zₙ − 1)⁻¹F(zₙ); errors square\n'
    'Completeness gives O = O₁ × O₂, each rank two; ξᵢ² = π·unit\n'
    'Local maximal ideal (ξᵢ), regular ξᵢ and zero intersection of powers prove DVRs\n'
    'Full B₄ = O; Oᵢ = R[ξᵢ]; each Eisenstein trace 1/constant 1/different 2\n'
    'Each w = kxᵢ: vᵢ(E) = 11, vᵢ(trace) = 9; ηᵢ = (yᵢ − kxᵢ)/ξᵢ⁵\n'
    'Full point index 5, constant 1/trace 4, relative different 8 each\n'
    'Absolute D₄,ᵢ = 2·2 + 8 = 12; D₈ = 24; i₈ = 2·16 + 5 + 5 = 42',
    'RT32–RT36; DVR proof establishes full normalization before any different is used','#edf4ff',10.85)

table = ax.table(cellText=[['A / B / D1','15','6','11','26','41','3 / 7'],['C','18','0','8','20','44','0 / 4'],['D2','16','4','10','24','42','2 / 6']],
    colLabels=['case','i₄','D₄','Σ fⱼℓⱼ','D₈','i₈','ε₄ / ε₈'],cellLoc='center',bbox=[.055,4.68/46,.89,1.30/46])
table.auto_set_font_size(False); table.set_fontsize(11.3)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor('#9cb0c7'); cell.set_linewidth(.8)
    cell.set_facecolor('#e8f0fa' if row==0 else '#f5f8fc')
    if row==0: cell.get_text().set_fontweight('bold')
ax.text(4.5,4.20,'All: ν = 0; δ = 36 − i₈ + i₄ − 2 = 8; f(E/K) = 2 + δ = 10',ha='center',fontsize=11.9)
ax.text(4.5,3.73,'i₄ + Σ fⱼℓⱼ = 26 = d + 8; −Art(X/R) = 9 − 1 + 10 = 18 = d',ha='center',fontsize=11.9)
ax.text(4.5,2.75,
    'RT37–RT38: actual even inertia orbits force wild action; the earlier quaternion proof\n'
    'gives zero cohomology invariants. Base discriminants D₄,D₈ are R-exponents;\n'
    'relative point differents use the upper point valuation; indices are module lengths.\n'
    'All residue degrees in the constructed split edition are one; v_F = 4v, vᵢ = 2v.',
    ha='center',va='center',fontsize=10.75,linespacing=1.4)
ax.text(4.5,1.46,
    'This proof and the actual earlier first/third/first-two/third-four proofs cover all e = 2 II*.\nHigher-ramification complements and other additive cases are outside these hypotheses.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.',
    ha='center',va='center',fontsize=10.75,linespacing=1.4)
ax.text(4.5,.52,
    'Source: J. S. Milne, free Algebraic Number Theory notes, Prop. 7.55 / Rem. 7.56.\nThe specialized arguments are in Sections 6.0AB.1–10.',
    ha='center',va='center',fontsize=10.1,color='#365675',linespacing=1.4)

fig.savefig(Path(__file__).resolve().parents[1] / 'assets/ramification-two-II-star-proof-map.png',dpi=100,facecolor='white')
plt.close(fig)
