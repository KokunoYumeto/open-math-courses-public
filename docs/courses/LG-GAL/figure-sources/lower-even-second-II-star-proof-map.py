"""Reproducible public proof map; all positions are schematic layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,46),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(4600,0);ax.axis('off')
ink='#253858';blue='#15668a';fill='#edf6fc';border='#cbdff0'
ax.text(45,52,'II* with lower even second valuation',color=ink,
        fontsize=17,fontweight='bold',fontfamily='DejaVu Sans')
ax.text(45,96,'Arbitrary units | Finite full-ring square construction | HL1–HL23',
        color=blue,fontsize=11.5,fontfamily='DejaVu Sans')
ax.text(45,134,'Complete quartic and point rings, exact indices/different/conductor.',
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

panel(1,'Actual preparation and all unit choices  |  HL1–HL2',[
    'v(π)=1; e=v(2)≥1; k=v(a₂)≥2 is even; 3k<2e+5.',
    't=2e+k+5; μ=t/4; h=v(a₁)>e+μ/2;',
    'z=v(a₃)>e+(μ+5−k)/2; l=v(a₄)>e+(μ+5)/2; v(a₆)=5.',
    'The first, third and fourth coefficients may vanish.',
    'Second and sixth coefficient units are arbitrary; no square condition.',
    'All e and coefficient values satisfying these actual tests are included.',
    'n=2e−3k+5=t−4k is odd, 1≤n≤2e−1; μ>k; μ≥9/4.',
    'Earlier 6E/I.8–I.9 prove the minimal nine-component II* model.',
    'K.2/K.6/P.5 supply actual trace-dual, tower, order and inertia proofs.',
    'The unit construction below takes place in the entire quartic ring.'
])
panel(2,'Every invariant, discriminant and quartic root  |  HL3–HL6',[
    'b₂=a₁²+4a₂; b₄=a₁a₃+2a₄; b₆=a₃²+4a₆;',
    'b₈=a₆b₂−a₁a₃a₄+a₂a₃²−a₄².',
    'β=2e+(μ+5)/2. Values: b₂=2e+k, b₄>β, b₆=2e+5, b₈=t.',
    'Other eighth-term margins: >e+3(μ−k)/2, >μ−k, >μ−k.',
    'In Δ, the sixth-invariant square alone has value d=4e+10.',
    'Other margins: 2e+3k−5; >5e+3μ/2−5/2; >2e+k+μ/2−5/2.',
    'v(c₄)=4e+2k; its subtracted term is higher by >5n/8.',
    'v(j)=8e+6k−10≥10. Model minimality precedes the conductor.',
    'q=X⁴+(b₂/3)X³+b₄X²+b₆X+b₈/3.',
    'All middle endpoint margins are positive, including the linear margin n/4.',
    'Every root has value μ. Odd numerator forces degree/ramification 4, residue 1.'
])
panel(3,'Entire quartic ring and two exact uniformizer equations  |  HL7–HL9',[
    'F=K(x); v_F=4v; mⱼ=floor(jt/4).',
    'C=B₄=R⊕R(x/π^m₁)⊕R(x²/π^m₂)⊕R(x³/π^m₃), in full.',
    'Four distinct fractional classes in [0,1) prove coefficientwise integrality.',
    'i₄=3(t−1)/2=3e+3k/2+6; D₄=2d−2i₄=n+3.',
    'For t=4a+1: θ=x/π^a. For t=4a+3: θ=π^(a+1)/x.',
    'In both cases v_F(θ)=1 and the first four powers prove C=R[θ].',
    'Its exact quartic equation retains every coefficient (see HL8).',
    'The constant F-value is 4. The sixth-invariant odd term has value n+4.',
    'The other odd-degree term is higher by 4e+6k−10>0.',
    'The quadratic term is higher by >3e+3k/2−5/2>0.',
    'Both full uniformizer equations are Eisenstein, not pure fourth-power substitutes.'
])
panel(4,'The full-ring relation and finite residue recursion  |  HL10–HL13',[
    'θ⁴=πu+ε with u∈R× and v_F(ε)=n+4, from the complete quartic.',
    'For every m≥1: θ^(4m)−(πu)^m',
    ' = ε·Σᵢ₌₀^(m−1) θ^(4(m−1−i))(πu)^i, of value ≥n+4m.',
    'For any base unit u₀∈R× set M₀=floor(n/4), S₋₁=0.',
    'Choose c̄_m²·ū^m = ((u₀−S_(m−1))/π^m)̄, for 0≤m≤M₀.',
    'S_m=Σᵢ₌₀^m cᵢ²(πu)^i; each next base error lies in π^(m+1)R.',
    'Finite characteristic-two residue squaring is bijective; all choices exist.',
    'w=Σₘ₌₀^M₀ c_m θ^(2m) is a unit of the entire C.',
    'Every diagonal error has value ≥n+4m; every cross term has value ≥4e+2.',
    'Final base error has value ≥4(M₀+1)>n. All cross terms exceed n too.',
    'Therefore v_F(w²−u₀)≥n+1, for arbitrary units at all permitted n.',
    'One residue lift alone gives only value 4 and is insufficient when n>3.'
])
panel(5,'The unrestricted point-radical identity  |  HL14–HL15',[
    'A=a₁x+a₃; G=x³+a₂x²+a₄x+a₆; Y=y+A/2; U=G+A²/4.',
    'B₀=3x+b₂/4; N=3x²+(b₂/2)x+b₄/2.',
    'Exact polynomial identity: N²−4UB₀=−3q(x). Every coefficient retained.',
    'u₀=b₂/(4π^k)∈R×; B=B₀/π^k=u₀+3x/π^k∈C×.',
    'v_F(3x/π^k)=n odd. No exact square root of u₀ in K is assumed.',
    'The first term in N alone has value 2μ; the other margins are ≥3/4 and >n/8.',
    'v(U)=5; v(A/2)≥3. All completed-square terms remain in the calculation.',
    'ζ=N/(2π^(k/2)Y) satisfies ζ²=B.',
    'D=N/(2π^(k/2)B) has value v_F(D)=10 and belongs to the entire C.',
    'y=Dζ−A/2. These relations identify the same actual point algebra.'
])
panel(6,'Whole point ring, exact order determinant and different  |  HL16–HL18',[
    'Apply the full residue recursion to this actual u₀. Its square error is ≥n+1.',
    'Thus v_F(w²−B)=n exactly. Put j=(n−1)/2 and η=(ζ−w)/θ^j.',
    'η²+(2w/θ^j)η+(w²−B)/θ^(2j)=0.',
    'Full constant F-value 1; trace F-value 4e−j>0: Eisenstein.',
    'Upper basis parities 0/1, against even F-coefficient values,',
    'prove the entire B₈=C[η]; point ramification 2 and residue degree 1.',
    'Derivative upper values 8e+1 and 8e−n+1 have exact positive gap n.',
    'D₈/₄=8e−n+1=6e+3k−4, from the full-ring trace dual.',
    'y=(Dw−A/2)+Dθ^jη with integral shift. Exact determinant Dθ^j.',
    'Relative index ℓ=10+j=(n+19)/2=e−3k/2+12≥10.',
    'This C-module length is weighted by residue degree 1, not ramification 4.'
])
panel(7,'Full discriminant/index columns and conductor  |  HL19–HL20',[
    'd=4e+10; D₄=n+3=2e−3k+8; i₄=3e+3k/2+6;',
    'ℓ=(n+19)/2; relative different D₈/₄=8e−n+1;',
    'D₈=2D₄+D₈/₄=8e+n+7=10e−3k+12;',
    'i₈=2i₄+ℓ=7e+3k/2+24. Also i₈=(6d−D₈)/2.',
    'Both full fields have one inertia orbit: ε₄=3, ε₈=7, ν=0.',
    'The four-pair inertia orbit forces a nontrivial wild image.',
    'The earlier quaternion proof supplies central −1 and zero cohomology invariants.',
    'Apply the proved Swan/permutation comparison after the full normalizations:',
    'δ=2d−i₈+i₄−2=4e; f=4e+2=d−8;',
    'i₄+ℓ=d+8 and M−1+f=d, with M=9.',
    'These prove NF24 on HL1; the universal assertion remains open.'
])

def row(e,k):
    assert k>=2 and k%2==0 and 3*k<2*e+5
    n=2*e-3*k+5;d=4*e+10;i4=3*e+3*k//2+6
    D4=n+3;ell=(n+19)//2;diff=8*e-n+1;D8=2*D4+diff;i8=2*i4+ell
    swan=2*d-i8+i4-2
    assert swan==4*e and i4+ell==d+8 and i8==(6*d-D8)//2
    return (d,i4,D4,ell,diff,D8,i8,swan,swan+2)
rows=[row(1,2),row(4,4),row(10,2)]
assert rows==[(14,12,4,10,8,16,34,4,6),(26,24,4,10,32,40,58,16,18),
             (50,39,22,19,62,106,97,40,42)]
assert row(7,6)==(38,36,4,10,56,64,82,28,30)
panel(8,'Infinite exact boundary and a longer unit recursion  |  HL21–HL23',[
    'Every q≥1: e=3q−2; k=2q; h≥4q−1; z≥3q+1; l≥4q+1; sixth value 5.',
    'The second unit is arbitrary; first/third/fourth values may be infinite.',
    'μ=2q+1/4; n=1; M₀=j=0. Derivative gap is exactly one.',
    'd=12q+2; i₄=12q; D₄=4; ℓ=10; D₈/₄=24q−16;',
    'D₈=24q−8; i₈=24q+10; δ=12q−8; f=12q−6.',
    'Exact row order: d, i₄, D₄, ℓ, D₈/₄, D₈, i₈, δ, f.',
    'q=1, e=1,k=2,h≥3,z≥4,l≥5: '+', '.join(map(str,rows[0])),
    'q=2, e=4,k=4,h≥7,z≥7,l≥9: '+', '.join(map(str,rows[1])),
    'e=10,k=2,h≥14,z≥15,l≥16: '+', '.join(map(str,rows[2])),
    'The last case has μ=27/4,n=19,M₀=4,j=9: coefficients c₀ through c₄.',
    'No nonzero condition on later residue coefficients; every unit is included.',
    'Numerical rows illustrate the written unbounded proof, not its justification.'
])
ax.text(45,3790,'Exercise, ten points  |  Section6.0AJ.8',color=blue,fontsize=12,fontweight='bold')
for j,line in enumerate([
    '(a) Every invariant/discriminant/root bound and all vanishing terms (2 points).',
    '(b) Entire quartic ring, both uniformizers, full finite unit recursion (3 points).',
    '(c) Exact torsion identity, whole point ring, index/different/conductor (3 points).',
    '(d) Infinite boundary and every exact example, including the longer recursion (2 points).',
    'The complete four-part solution is retained with the mathematical proof.'
]):ax.text(45,3832+30*j,line,color=ink,fontsize=10)
ax.text(45,4030,'Written sources and exact remaining scope',color=blue,
        fontsize=12,fontweight='bold')
for j,line in enumerate([
    'Actual providers: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5; Lesson01 0A–0G.',
    'Free human context: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56,',
    'printed pp.129–130. https://www.jmilne.org/math/CourseNotes/ANT.pdf',
    'Arbitrary-unit lower even-second preparation HL1 is proved in full.',
    'Odd second and lower first/third/fourth coefficient bounds remain.',
    'Other additive families are outside the hypotheses of this diagram.',
    'General conductor–index identity: JM30–JM32, Section6.0BI.',
    'The complete ring bases and valuation conventions are in the cited proof.',
    'Base v(π)=1; quartic value v_F=4v; upper point-field value is 8v.',
    'All drawing positions are layout coordinates, not points sampled on the curve.'
]):ax.text(45,4072+33*j,line,color=ink,fontsize=9.5)
fig.savefig(base.parent/'assets/lower-even-second-II-star-proof-map.png',dpi=100,
            metadata={'Software':'Matplotlib','Author':'Galois representations course'})
plt.close(fig)
