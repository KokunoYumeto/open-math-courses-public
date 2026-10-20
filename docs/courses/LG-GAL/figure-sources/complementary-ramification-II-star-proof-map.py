"""Reproducible public proof map; positions are schematic layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,46),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(4600,0);ax.axis('off')
ink='#253858';blue='#15668a';fill='#edf6fc';border='#cbdff0'
ax.text(45,52,'II* with large or infinite first valuation',color=ink,
        fontsize=17,fontweight='bold',fontfamily='DejaVu Sans')
ax.text(45,96,'Every e ≥ 1 | Two full cubic normalizations | HK1–HK22',
        color=blue,fontsize=11.5,fontfamily='DejaVu Sans')
ax.text(45,134,'Exact product-order defect, all point rings and conductors.',
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

panel(1,'Actual preparation, including infinite first valuation  |  HK1',[
    'v(π)=1; e=v(2)≥1; r=2e+5; λ=r/3.',
    'h=v(a₁)>(8e+5)/6; k=v(a₂)>λ; z=v(a₃)≥e+3;',
    'l=v(a₄)>2λ; v(a₆)=5. Each of a₁,a₂,a₃,a₄ may vanish.',
    'No upper cutoff on e or the coefficient valuations.',
    'At finite h: 3h≥4e+3, equivalently 4e<3h−2.',
    'These are tests on actual coefficients after any coordinate preparation.',
    'Earlier 6E/I.8–I.9 prove the minimal nine-component II* model.',
    'Earlier K.2/K.6/P.5 prove trace duals, towers, order and inertia formulas.',
    'Earlier AD.1 proves full normalization and numerical invariance',
    'under a finite unramified extension; its point quadratics stay ramified.'
])
panel(2,'Every invariant contribution and the unique minimum  |  HK2–HK4',[
    'b₂=a₁²+4a₂; b₄=a₁a₃+2a₄; b₆=a₃²+4a₆;',
    'b₈=a₆b₂−a₁a₃a₄+a₂a₃²−a₄².',
    'v(b₂)>λ+2e; v(b₄)>2λ+e; v(b₆)=r; v(b₈)>4λ.',
    'The square in b₆ has value ≥r+1: its 4a₆ term is uniquely least.',
    'Eighth-term bounds: >4λ, >4λ+e+1/2, >4λ+1, >4λ.',
    'The eighth invariant may vanish; no nonzero value is assumed.',
    'Δ=−b₂²b₈−8b₄³−27b₆²+9b₂b₄b₆.',
    'Three higher bounds: >6λ+4e, >6λ+6e, >6λ+3e.',
    'The sixth-invariant square alone has value 6λ.',
    'd=v(Δ)=2r=4e+10; c₄=b₂²−24b₄ has value >2λ+4e.',
    'v(j)>12e, possibly infinite. Minimality and M=9 precede the conductor.'
])
panel(3,'Rational sign pair and its integral product defect  |  HK5–HK8',[
    'q=X⁴+(b₂/3)X³+b₄X²+b₆X+b₈/3; m=floor(λ)+1.',
    'F(T)=q(π^mT)/π^(r+m) has integral constant and unit linear coefficient;',
    'all higher coefficients have positive value. Its reduction is linear.',
    'Complete Newton iteration and unit divided differences give one root in R.',
    'ρ∈π^mR; v(ρ)>λ; ρ=0 when b₈=0.',
    'q=(X−ρ)g; g=X³+C₂X²+C₁X+C₀.',
    'C₂=b₂/3+ρ; C₁=b₄+(b₂/3)ρ+ρ²;',
    'C₀=b₆+b₄ρ+(b₂/3)ρ²+ρ³. Values: >λ, >2λ, r.',
    'All three cubic roots have value λ. g(ρ)=q′(ρ) has value r.',
    '0 → R[X]/q → R⊕R[X]/g → R/(g(ρ)) → 0.',
    'The last map is (a,B) ↦ a−B(ρ). Its exact quotient length is r.',
    'Generic product splitting alone would omit this required integral defect.'
])
panel(4,'The entire tame cubic field when 3 does not divide r  |  HK9–HK11',[
    'Slope denominator 3 forces [F₃:K]=e(F₃/K)=3 and f(F₃/K)=1.',
    'mⱼ=floor(jr/3); v₃=3v.',
    'C₃=R⊕R(x/π^m₁)⊕R(x²/π^m₂), in full.',
    'Distinct fractional classes in [0,1) prove coefficientwise integrality.',
    'The two denominator floors sum to r−1.',
    'For r=3a+1: θ=x/π^a. For r=3a+2: θ=π^(a+1)/x.',
    'Both exact transformed cubic equations are Eisenstein; v₃(θ)=1.',
    'Its first three power classes prove C₃=R[θ], in full.',
    'Derivative values: 2, ≥3e+4, ≥3. Thus the full-ring different D₃=2.',
    'B₄=R×C₃; i₄=r+(r−1)=d−1; D₄=2.',
    'Degree 3 and residue degree 1 must not be confused in weighting lengths.'
])
panel(5,'The entire unramified cubic algebra when 3 divides r  |  HK12',[
    'r=3a, equivalently e≡2 mod 3.',
    'G₃(T)=g(π^aT)/π^(3a) reduces to T³+ū with ū≠0.',
    'Its residue derivative is T². All three residue roots are simple.',
    'Earlier 0F.1–0F.2 supply their finite residue/unramified splitting field K′.',
    'Newton lifting stays in each simple-root class and lifts all three roots.',
    'Their unit differences give integral Lagrange coordinate idempotents.',
    'The entire cubic normalization is R′³; the full quartic ring is R′⁴.',
    'The basis (1,x,x²) in (1,T,T²) has determinant π^(3a).',
    'Cubic index r; product defect r; total i₄=2r=d; D₄=0.',
    'Over K there may be nontrivial unramified residue factors.',
    'Only the numerical invariants descend; no false splitting over K is asserted.'
])
panel(6,'All full point quadratics and their exact indices  |  HK13–HK15',[
    'A=a₁x+a₃; G=x³+a₂x²+a₄x+a₆; Y=y+A/2.',
    'For every factor: v(x)≥λ; v(A/2)≥3; Y²=G+A²/4=π⁵u, u a unit.',
    'Every non-sixth term has value >5; every square/cross term is retained.',
    'Rational or split factor: η₀=Y/π²; η₀²=πu.',
    'Upper basis parities prove the entire R[η₀]. Relative index ℓ₀=2;',
    'derivative upper value D₂=2e+1. It is a ramified quadratic field.',
    'Tame cubic factor: η₃=Y/(π²θ); η₃²=θ(π/θ³)u.',
    'π/θ³ is a unit. Upper parities prove the entire C₆=C₃[η₃].',
    'Relative C₃-module index ℓ₃=v₃(π²θ)=7, weighted by f(F₃/K)=1.',
    'Relative different D₆/₃=6e+1; absolute D₆=2·2+(6e+1)=6e+5.',
    'All shifts are integral; all order determinants use the full ring bases.'
])
panel(7,'Full columns, inertia and conductor  |  HK16–HK18',[
    '                             3 does not divide r          3 divides r',
    'B₄                           R×C₃                         R′⁴ after base change',
    'D₄, i₄                       2, d−1                       0, d',
    'k_pt = Σ fⱼℓⱼ                2+7=9                        4·2=8',
    'D₈                           8e+6                         8e+4',
    'i₈=2i₄+k_pt                  8e+27                        8e+28',
    'ε₄, ε₈, ν                    2, 6, 0                      0, 4, 0',
    'In each column i₈=(6d−D₈)/2 and ε₈−ε₄=4.',
    'The rational sign pair has a ramified point quadratic: wild action is nontrivial.',
    'Quaternion central −1 gives zero cohomology inertia invariants.',
    'δ=2d−i₄−k_pt−2=4e; f=4e+2=d−8;',
    'i₄+k_pt=d+8; M−1+f=d. These follow after all full ring calculations.'
])

def row(e):
    r=2*e+5; d=2*r; split=r%3==0
    i4=d if split else d-1; D4=0 if split else 2
    kpt=8 if split else 9; D8=8*e+4 if split else 8*e+6
    i8=2*i4+kpt; swan=2*d-i4-kpt-2
    assert i8==(6*d-D8)//2 and swan==4*e and i4+kpt==d+8
    return (d,i4,D4,kpt,D8,i8,swan,swan+2)
rows=[row(e) for e in (1,2,3)]
assert rows==[(14,13,2,9,14,35,4,6),(18,18,0,8,20,44,8,10),
             (22,21,2,9,30,51,12,14)]
assert row(4)==(26,25,2,9,38,59,16,18)
assert row(5)==(30,30,0,8,44,68,20,22)
panel(8,'Complete higher-first coverage and infinite first  |  HK19–HK22',[
    'All finite h≥4, k>(2h+5)/4, z≥h+1, l≥h+3, sixth value 5:',
    'If 4e≥3h−2, the preceding higher-first proof applies.',
    'If 4e<3h−2, integer values give 3h≥4e+3; HK1 follows.',
    'Old second threshold minus λ is (6h−8e−5)/12>0;',
    'h−e≥2 gives z≥e+3; 3(h+3)−(4e+10)≥2 gives l>2λ.',
    'Thus every e≥1 is covered on this entire finite higher-first preparation.',
    'Additional infinite first: a₁=0, k>λ, z≥e+3, l>2λ, sixth value 5.',
    'Example row order: d, i₄, D₄, k_pt, D₈, i₈, δ, f.',
    'e=1, h≥3,k≥3,z≥4,l≥5: '+', '.join(map(str,rows[0])),
    'e=2, h≥4,k≥4,z≥5,l≥7: '+', '.join(map(str,rows[1])),
    'e=3, h≥5,k≥4,z≥6,l≥8: '+', '.join(map(str,rows[2])),
    'Each example also permits a₁=0 and zero second, third or fourth coefficients.'
])
ax.text(45,3790,'Exercise, ten points  |  Section6.0AI.8',color=blue,fontsize=12,fontweight='bold')
for j,line in enumerate([
    '(a) All invariant bounds, exact discriminant and vanishing terms (2 points).',
    '(b) Rational root, integral product defect, both entire cubic rings (3 points).',
    '(c) All full point rings, indices, inertia and conductor columns (3 points).',
    '(d) Complete higher-first coverage and all three examples (2 points).',
    'The complete four-part solution is retained with the mathematical proof.'
]):ax.text(45,3832+30*j,line,color=ink,fontsize=10)
ax.text(45,4030,'Written sources and exact remaining scope',color=blue,
        fontsize=12,fontweight='bold')
for j,line in enumerate([
    'Actual providers: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5/AD.1; Lesson01 0A–0G.',
    'Free human context: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56,',
    'printed pp.129–130. https://www.jmilne.org/math/CourseNotes/ANT.pdf',
    'The higher-first preparation HK19 is now proved at every ramification index.',
    'Infinite first outside HK21 and lower coefficient bounds still remain.',
    'Other additive families are outside the hypotheses of this diagram.',
    'General conductor–index identity: JM30–JM32, Section6.0BI.',
    'The complete ring bases and valuation conventions are in the cited proof.',
    'K-value v(π)=1; cubic value v₃=3v; point-field values are 2v or 6v.',
    'All drawing positions are layout coordinates, not points sampled on the curve.'
]):ax.text(45,4072+33*j,line,color=ink,fontsize=9.5)
fig.savefig(base.parent/'assets/complementary-ramification-II-star-proof-map.png',dpi=100,
            metadata={'Software':'Matplotlib','Author':'Galois representations course'})
plt.close(fig)
