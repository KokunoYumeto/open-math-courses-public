"""Reproducible public proof map. Positions are diagram layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,46),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(4600,0);ax.axis('off')
ink='#253858';blue='#15668a';fill='#edf6fc';border='#cbdff0'
ax.text(45,52,'II* at the quarter ramification boundary',color=ink,
        fontsize=17,fontweight='bold',fontfamily='DejaVu Sans')
ax.text(45,96,'All finite h ≥ 4 | Negative auxiliary values included | HJ1–HJ20',
        color=blue,fontsize=11.5,fontfamily='DejaVu Sans')
ax.text(45,134,'Full quartic and point rings, different, indices and conductors.',
        color=ink,fontsize=10.5,fontfamily='DejaVu Sans')

def panel(number,title,lines):
    y=180+445*(number-1)
    assert len(lines)<=12
    ax.add_patch(FancyBboxPatch((35,y),830,425,boxstyle='round,pad=0,rounding_size=10',
        linewidth=1.2,edgecolor=border,facecolor=fill))
    ax.text(57,y+37,f'{number}  {title}',color=blue,fontsize=11.6,
        fontweight='bold',fontfamily='DejaVu Sans')
    for j,line in enumerate(lines):
        ax.text(57,y+79+27*j,line,color=ink,fontsize=9.8,fontfamily='DejaVu Sans')

panel(1,'Actual preparation and a possibly negative parameter  |  HJ1–HJ2',[
    'v(π)=1; e=v(2); h=v(a₁)≥4 is finite; 4e≥3h−2.',
    'λ=(2h+5)/4; k=v(a₂)>λ; z=v(a₃)≥h+1;',
    'v(a₄)≥h+3; v(a₆)=5. The second, third and fourth coefficients may vanish.',
    't=min(2(z−h),2(e−h)+5) is a finite integer; it may be negative.',
    'Both candidates give t≥4−h/2, so λ+t≥21/4.',
    'The derivative margin 8e−6h+5 is at least 1.',
    'Low regime L: t≤h+2. High regime H: t≥h+3. These exhaust all integers.',
    'Earlier 6E/I.8–I.9 give the actual minimal nine-component II* model.',
    'Earlier AD.1 proves full normalization and numerical invariance under',
    'the finite unramified cube-root extension. Both ring computations descend.'
])
panel(2,'Every discriminant term is controlled  |  HJ3–HJ7',[
    'b₂=a₁²+4a₂; b₄=a₁a₃+2a₄; b₆=a₃²+4a₆;',
    'b₈=a₆b₂−a₁a₃a₄+a₂a₃²−a₄².',
    'v(b₂)=2h; v(b₆)=2h+t; v(b₈)=2h+5;',
    'v(b₄)≥min(2h+1,e+h+3). Opposite sixth-term parities exclude cancellation.',
    'Δ=−b₂²b₈−8b₄³−27b₆²+9b₂b₄b₆.',
    'The competing values are 6h+5 (odd) and 4h+2t (even).',
    'Each cross-term bound is above the minimum by ≥h−1 or ≥e+1.',
    'Cube-term bounds exceed 6h+5 by ≥3e−2 or ≥3h/2+1, both positive.',
    'd=v(Δ): 4h+2t in L; 6h+5 in H. Every minimum is unique.',
    'c₄=b₂²−24b₄ has value 4h; v(j)=12h−d≥6h−5>0.',
    'All subtracted c₄ terms are higher. The actual earlier model proves minimality.'
])
panel(3,'Every root and coefficientwise integrality  |  HJ8–HJ10',[
    'q=x⁴+(b₂/3)x³+b₄x²+b₆x+b₈/3. Every root has value λ.',
    'Endpoints have value 2h+5; middle margins are ≥2h−λ,',
    'min(h−3/2,e+1/2), and λ+t−5≥1/4, all positive.',
    'Any other root value has a unique least endpoint, which is impossible.',
    'Denominator 4 forces one field F of degree/ramification 4 and residue degree 1.',
    'r=2h+5; mⱼ=floor(jr/4); v_F=4v.',
    'B₄=R⊕R(x/π^m₁)⊕R(x²/π^m₂)⊕R(x³/π^m₃), in full.',
    'Four distinct fractional classes in [0,1): integrality forces every coefficient in R.',
    'i₄=m₁+m₂+m₃=3h+6. This is the exact lattice determinant.',
    'τ=x/π^m₁ for even h; τ=x³/π^m₃ for odd h. In each case v_F(τ)=1.',
    'The first four powers prove B₄=R[τ]. D₄=2h+4t−12≥4 in L; 6h−2 in H.'
])
panel(4,'The whole point error, including its constant  |  HJ11–HJ14',[
    'c=1+2ζ; ζ²+ζ+1=0; c²=−3; v(c+3)=e.',
    'w=(cx²+a₄)/a₁ has exact value 5/2 and belongs to the full B₄.',
    'E(w)=w²+(a₁x+a₃)w−(x³+a₂x²+a₄x+a₆).',
    'E(w)=J₃x³+J₂x²+J₁x+J₀, with every coefficient retained:',
    'J₃=c+4a₂/a₁²; J₂=(c+3)(a₃/a₁+2a₄/a₁²)−a₂;',
    'J₁=3b₆/a₁²; J₀=a₂b₆/a₁².',
    'Exact unrestricted identity: a₁²(E−ΣJⱼxʲ)=(c²+3)x⁴−3q(x).',
    'v(J₃)=0; v(J₂)>λ; v(J₁)=t; v(J₀)=k+t or ∞.',
    'L: the linear term is uniquely least. H: the cubic term is uniquely least.',
    'The quadratic is >3λ; the constant is >λ+t, and is also >3λ in H.',
    'v_F(E)=4t+2h+5 in L, 6h+15 in H. No correction term is omitted.'
])
panel(5,'Full trace and both normalized point equations  |  HJ14–HJ16',[
    'T(w)=a₁x+a₃+2w. Contribution values: h+λ, z, e+5/2.',
    'Their finite fractional classes are odd-quarter, integral and half-integral.',
    'min(z,e+5/2)=h+t/2. It is ≥1/4 below the first contribution in L;',
    'in H it is ≥1/4 above it. The full minimum cannot cancel.',
    'v_F(T)=4h+2t in L; 6h+5 in H.',
    'ℓ=2t+h+2≥10 in L; ℓ=3h+7 in H.',
    'η=(y−w)/τ^ℓ satisfies η²+(T/τ^ℓ)η+E/τ^(2ℓ)=0.',
    'In both regimes: constant F-value 1; trace F-value 3h−2>0.',
    'This is Eisenstein: one quadratic point field, ramification 2 and residue degree 1.',
    'The full trace calculation holds also for zero third coefficient and negative t.'
])
panel(6,'Entire point rings, different and exact indices  |  HJ16–HJ17',[
    'In the normalized upper point valuation, 1 and η have values 0 and 1.',
    'Coefficients from F have even values: integrality forces both into B₄.',
    'Thus the entire B₈=B₄[η]. The order basis (1,y) in (1,η)',
    'has determinant τ^ℓ, so its relative point index is exactly ℓ.',
    'Derivative upper values: 8e+1 and 6h−4; margin ≥1, so D₈/₄=6h−4.',
    'Residue degrees are 1. Full different tower: D₈=2D₄+6h−4.',
    '                           L                              H',
    'D₄                  2h+4t−12                        6h−2',
    'D₈                  10h+8t−28                       18h−8',
    'i₈=2i₄+ℓ            7h+2t+14                        9h+19',
    'Both exact indices also satisfy i₈=(6d−D₈)/2 by the proved order discriminant.'
])
panel(7,'The conductor follows after full normalization  |  HJ18',[
    'Both algebras are single totally ramified fields: ε₄=3, ε₈=7, ν=0.',
    'A four-point inertia orbit forces nontrivial wild action.',
    'The earlier quaternion proof supplies central −1 and zero cohomology invariants.',
    'Apply the proved Swan/permutation comparison to the full rings:',
    '                           L                              H',
    'δ=2d−i₈+i₄−2         4h+2t−10                        6h−5',
    'f=2+δ                4h+2t−8                         6h−3',
    'i₄+ℓ                 4h+2t+8                         6h+13',
    'Therefore f=d−8, i₄+ℓ=d+8, and M−1+f=d with M=9.',
    'The earlier Euler proof identifies the last sum with the discriminant–Artin equality.',
    'This proves NF24 on the whole preparation HJ1, not on every additive preparation.'
])

def row(h,e,z):
    t=min(2*(z-h),2*(e-h)+5)
    low=t<=h+2
    d=4*h+2*t if low else 6*h+5
    i4=3*h+6;D4=2*d-2*i4;ell=2*t+h+2 if low else 3*h+7
    diff=6*h-4;D8=2*D4+diff;i8=2*i4+ell;swan=2*d-i8+i4-2
    assert 4*e>=3*h-2 and swan+2==d-8 and i4+ell==d+8
    return (d,i4,D4,ell,diff,D8,i8,swan,swan+2)
rows=[row(6,4,7),row(10,7,11),row(4,5,8)]
assert rows==[(26,24,4,10,32,40,58,16,18),(38,36,4,10,56,64,82,28,30),
             (29,18,22,19,20,64,55,19,21)]
format_row=lambda r:', '.join(str(n) for n in r)
panel(8,'An infinite exact-boundary family and three exact examples  |  HJ19–HJ20',[
    'Every q≥2: h=4q−2; e=3q−2; k≥2q+1; z≥4q−1;',
    'v(a₄)≥4q+1; v(a₆)=5. Here 4e=3h−2 and t=5−2q.',
    'The auxiliary parameter is arbitrarily negative as q increases.',
    'd=12q+2; i₄=12q; D₄=4; ℓ=10; D₈/₄=24q−16;',
    'D₈=24q−8; i₈=24q+10; δ=12q−8; f=12q−6.',
    'At every boundary member: (8e+1)−(6h−4)=1 exactly.',
    'Exact row order: d, i₄, D₄, ℓ, D₈/₄, D₈, i₈, δ, f.',
    'q=2 (h=6,e=4,t=1):   '+format_row(rows[0]),
    'q=3 (h=10,e=7,t=−1): '+format_row(rows[1]),
    'H example: h=4,e=5,k≥4,z≥8,v(a₄)≥7,v(a₆)=5,t=7.',
    'Its row: '+format_row(rows[2]),
    'The numerical rows illustrate the written unbounded proof; they do not replace it.'
])
ax.text(45,3790,'Exercise, ten points  |  Section6.0AH.8',color=blue,fontsize=12,fontweight='bold')
for j,line in enumerate([
    '(a) Derive all auxiliary and strict invariant/discriminant bounds (3 points).',
    '(b) Prove both entire rings, full errors/traces, different and conductors (4 points).',
    '(c) Derive the infinite family and all three exact example rows (3 points).',
    'The complete three-part solution is retained with the written proof.'
]):ax.text(45,3832+30*j,line,color=ink,fontsize=10)
ax.text(45,3995,'Written sources and exact remaining scope',color=blue,
        fontsize=12,fontweight='bold')
for j,line in enumerate([
    'Actual providers: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5/AD.1; Lesson01 0A–0G.',
    'Free human context: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56,',
    'printed pp.129–130. https://www.jmilne.org/math/CourseNotes/ANT.pdf',
    'HJ1 contains the earlier 6Y range when the finite first valuation is at least four.',
    'Infinite first values, lower ramification and all complementary ranges remain.',
    'The coefficient hypotheses delimit this family-specific diagram.',
    'General conductor–index identity: JM30–JM32, Section6.0BI.',
    'All specialization bounds and mechanisms are proved in HJ1–HJ20 or earlier lessons.',
    'Quartic v_F=4v; upper point value is 8v.',
    'All drawing positions are layout coordinates, not points or samples on the curve.'
]):ax.text(45,4037+33*j,line,color=ink,fontsize=9.5)
fig.savefig(base.parent/'assets/quarter-ramification-higher-first-II-star-proof-map.png',dpi=100,
            metadata={'Software':'Matplotlib','Author':'Galois representations course'})
plt.close(fig)
