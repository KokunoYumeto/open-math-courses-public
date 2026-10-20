"""Reproducible public proof map; all positions are schematic layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,48),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,900); ax.set_ylim(4800,0); ax.axis('off')
ink='#253858'; blue='#15668a'; fill='#edf6fc'; border='#cbdff0'
ax.text(45,53,'II* at the adjacent odd second boundaries',color=ink,fontsize=16.5,fontweight='bold')
ax.text(45,95,'Every unit | Both cancellation cases | Whole rings and original-order indices',
        color=blue,fontsize=10.8)
ax.text(45,132,'n=2 or4; three normalization mechanisms; exact conductor 4e+2 | HM1–HM28',
        color=ink,fontsize=10.2)

def panel(number,title,lines):
    y=180+455*(number-1)
    assert len(lines)<=12
    ax.add_patch(FancyBboxPatch((35,y),830,435,boxstyle='round,pad=0,rounding_size=10',
        linewidth=1.2,edgecolor=border,facecolor=fill))
    ax.text(57,y+37,f'{number}  {title}',color=blue,fontsize=11.1,fontweight='bold')
    for j,line in enumerate(lines):ax.text(57,y+79+27*j,line,color=ink,fontsize=9.5)

panel(1,'Actual preparation and complete invariant bounds | HM1–HM7',[
 'v(π)=1; k=v(a₂)≥3 odd; n=2e−3k+5 is2 or4; μ=(2e+k+5)/4.',
 'h=v(a₁)>e+μ/2; z=v(a₃)>e+(μ+5−k)/2;',
 'l=v(a₄)>e+(μ+5)/2; v(a₆)=5. First/third/fourth may vanish.',
 'Second and sixth units arbitrary. All actual ramification values are included.',
 'β=2e+(μ+5)/2. b₂ value2e+k; b₄>β; b₆ value2e+5; b₈ value4μ.',
 'All terms retained. Sixth-invariant square alone gives d=4e+10.',
 'v(c₄)=4e+2k; subtracted-term margin>5n/8; v(j)>0.',
 'Every sign-pair quartic root x has value μ; its ring is proved below.',
 'Earlier6E/I.8–I.9 give the minimal9-component II* model before conductors.',
 'N²−4UB₀=−3q(x); ζ=N/(2π^((k−1)/2)Y); ζ²=B; y=Dζ−A/2.',
 'B=πu₀+3x/π^(k−1), v(B)=1; v(D)=2; v(A/2)≥3.',
 'The radical has positive value; B is not being called a unit.'
])
panel(2,'n=2: a mixed basis proves the entire quartic ring | HM8–HM10',[
 '2e=3k−3; μ=k+1/2; Z=x/π^k has value1/2.',
 'Z⁴+C₃Z³+C₂Z²+C₁Z+C₀=0, with all original terms retained.',
 'v(C₃)=2e; v(C₂)>3k/2−1/4; v(C₁)=v(C₀)=2.',
 'u=−C₀/π²∈R×. Choose c̄²=ū in the finite base residue field.',
 'θ=(Z²−πc)/π; its full squared numerator has least term −C₁Z.',
 'That term has value5/2; base-square error≥3; every cross/other term higher.',
 'Hence v(θ)=1/4: degree/ramification4, residue degree1.',
 'C=R⊕RZ⊕Rθ⊕RZθ=R[θ] in full; basis classes0,1/2,1/4,3/4.',
 'θ=x²/π^(2k+1)−c; Zθ=x³/π^(3k+1)−cx/π^k.',
 'Exact denominator sum i₄=6k+2=d−2; normal discriminant D₄=4.',
 'Distinct fractional classes prove coefficientwise integrality, not just integrality.'
])
panel(3,'n=4: the actual shifted quartic and its two cases | HM11–HM13',[
 '2e=3k−1; μ=k+1; T=x/π^μ. Choose c̄⁴=−C̄₀ in the base residue field.',
 'f(c+X)=X⁴+d₃X³+d₂X²+d₁X+d₀. All shifted coefficients exact:',
 'd₃=C₃+4c; d₂=C₂+3cC₃+6c²;',
 'd₁=C₁+2cC₂+3c²C₃+4c³; d₀=f(c).',
 'v(d₃)=2e−1; v(d₂)=e; v(d₁)=1; v(d₀)≥1.',
 'A: v(d₀)=1 → Eisenstein quartic θ=T−c; v(θ)=1/4.',
 'Entire C=R[θ]; x=π^μ(c+θ); triangular original index i₄=6μ=d−2.',
 'θ⁴=πu+ε, u=−d₀/π∈R×; ε=−d₁θ−d₂θ²−d₃θ³.',
 'v(ε)=5/4 from the uniquely least linear term; normal discriminant4.',
 'B: v(d₀)≥2, including d₀=0 → rational-plus-cubic normalization below.',
 'The cancellation is tested on the complete f(c), not on selected unit terms.'
])
panel(4,'n=4 B: complete rational/cubic ring and product defect | HM14–HM16',[
 'π⁻²f(c+πS)=π²S⁴+πd₃S³+d₂S²+(d₁/π)S+d₀/π².',
 'Unit linear reduction; full Newton correction constructs the unique ρ∈πR.',
 'F(X)=(X−ρ)g(X); g=X³+g₂X²+g₁X+g₀;',
 'g₂=d₃+ρ; g₁=d₂+ρd₃+ρ²; g₀=d₁+ρd₂+ρ²d₃+ρ³.',
 'v(g₂)≥1; v(g₁)≥2; v(g₀)=1. Cubic Eisenstein; v(α)=1/3.',
 'C₃=R[α] in full by basis classes0,1/3,2/3; cubic different2.',
 'Full B₄=R×C₃. g(ρ)=F′(ρ) has exact value1.',
 'Evaluation difference quotient is R/(g(ρ)); compatible pairs have',
 'the explicit polynomial preimage a+(X−ρ)c(X). Product defect length1.',
 'Original scaling contributes6μ; total i₄=6μ+1=d−1; D₄=2.',
 'Discarding the product defect changes the exact original-order index.'
])
panel(5,'Whole point field above either quartic field | HM17–HM19',[
 'n=2: choose ā²c̄=ū₀ and w=aZ.',
 'w²−B=π(a²c−u₀)+πa²θ−3πZ, with values≥2,5/4,3/2.',
 'n=4 A: v₀=u₀+3πc; choose ā²ū=v̄₀ and w=aθ².',
 'w²−B=π(a²u−v₀)+a²ε−3π²θ, with values≥2,5/4,9/4.',
 'Both: v(w)=1/2 and v_F(w²−B)=5 exactly; v_F=4v.',
 'η=(ζ−w)/θ² satisfies the full normalized quadratic.',
 'Its constant F-value1 and trace F-value4e prove Eisenstein irreducibility.',
 'Upper basis parities0/1 prove entire B₈=C[η], point degree/ramification2.',
 'Derivative upper values8e+1 and8e: exact positive gap1; relative different8e.',
 'y=(Dw−A/2)+Dθ²η; integral shift; original determinant Dθ².',
 'Exact point index ℓ=8+2=10; residue weight1.',
 'Full D₈=8e+8; i₈=8e+26.'
])
panel(6,'Both whole point fields above the product | HM20–HM22',[
 'Rational: B=πV₂, V₂=u₀+3π(c+ρ)∈R×.',
 'Entire B₂=R[ζ], ζ²=πV₂, Eisenstein; degree/ramification2, residue1.',
 'Different2e+1; y=Dζ−A/2; exact original-order length2.',
 'Cubic: B=πV₃, V₃=u₀+3π(c+α)∈C₃×.',
 'η=ζ/α; η²=πV₃/α² has cubic constant value1.',
 'Upper basis parities prove entire B₆=C₃[η]; degree/ramification6, residue1.',
 'Relative different6e+1; absolute different6e+5 by the full tower.',
 'y=Dαη−A/2; exact cubic determinant value6+1=7.',
 'Full B₈=B₂×B₆; total point length2+7=9.',
 'D₈=(2e+1)+(6e+5)=8e+6; i₈=8e+27.',
 'Both length weights are residue degree1, not ramification2 or3.'
])
panel(7,'All indices, inertia counts and conductor | HM23–HM24',[
 'Column order: n=2; n=4 A; n=4 B. All have d=4e+10.',
 'i₄: d−2,d−2,d−1.  D₄:4,4,2.  Point length:10,10,9.',
 'D₈:8e+8,8e+8,8e+6.  i₈:8e+26,8e+26,8e+27.',
 'Each also satisfies the point-order check i₈=(6d−D₈)/2.',
 'Inertia codimensions (ε₄,ε₈): (3,7),(3,7),(2,6); difference4.',
 'A quartet orbit, or the rational pair’s quadratic orbit, forces wild action.',
 'Earlier quaternion proof gives central −1 and zero cohomology invariants.',
 'Every point quadratic is proved ramified; ν=0.',
 'Apply the written permutation/Swan comparison only after full normalization:',
 'δ=2d−i₈+i₄−2=4e; f=4e+2=d−8;',
 'i₄+ℓ=d+8; M−1+f=d with minimal M=9.',
 'Different ring/index columns give the same conductor; no conductor used to find them.'
])
panel(8,'Infinite boundaries and actual realization of both branches | HM25–HM28',[
 'Every q≥1: k=2q+1. n=2: e=3q,h≥4q+1,z≥3q+3,l≥4q+4;',
 'n=4: e=3q+1,h≥4q+3,z≥3q+5,l≥4q+5; sixth value5.',
 'Second/sixth units arbitrary; first/third/fourth values may be infinite.',
 'Both n=4 cases exist over every allowed field: set a₁=a₃=a₄=0.',
 'Choose any a₆ of value5; μ=k+1; C₁=4a₆/π^(3μ) has value1.',
 'L=4(π^(3μ)+a₆)/(3π^(4μ)) is nonzero of value−k.',
 'a₂ᴮ=−(1+C₁)/L; a₂ᴬ=(1+π)a₂ᴮ; both have exact valuek.',
 'For B: f(1)=0 and x=π^μ is an actual rational quartic root.',
 'For A: f(1)=−π(1+C₁) has exact value1: shifted Eisenstein quartic.',
 'q=1 rows d,i₄,D₄,ℓ,D₈,i₈,δ,f:',
 'n=2:22,20,4,10,32,50,12,14; A:26,24,4,10,40,58,16,18;',
 'B:26,25,2,9,38,59,16,18. Written unbounded proof precedes these examples.'
])
ax.text(45,3890,'Exercise, ten points | Section6.0AK.8',color=blue,fontsize=12,fontweight='bold')
for j,line in enumerate([
 '(a) All invariant/root bounds and the same-point generator change (2 points).',
 '(b) All whole quartic rings, both cancellations and exact product defect (3 points).',
 '(c) All full point rings, original lengths, different towers and conductors (3 points).',
 '(d) Infinite boundaries, exact rows and both actual branch realizations (2 points).',
 'The complete four-part solution remains with the complete mathematical proof.'
]):ax.text(45,3932+31*j,line,color=ink,fontsize=10)
ax.text(45,4140,'Written sources and exact remaining scope',color=blue,fontsize=12,fontweight='bold')
for j,line in enumerate([
 'Prerequisite results: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5; Lesson01 0A–0G.',
 'Free human context: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56,',
 'printed129–130. https://www.jmilne.org/math/CourseNotes/ANT.pdf',
 'Both whole adjacent odd second boundaries n=2,4 are proved, with all units.',
 'Deeper odd n≥6 and lower coefficient bounds outside HM1 remain.',
 'Other additive families are outside the hypotheses of this diagram.',
 'General conductor–index identity: JM30–JM32, Section6.0BI.',
 'Positions are schematic layout coordinates.',
 'All positions are layout coordinates; exact valuation classes are printed explicitly.',
 'Full sources, bases, determinant weights and arguments accompany every arrow.'
]):ax.text(45,4182+33*j,line,color=ink,fontsize=9.5)
fig.savefig(base.parent/'assets/adjacent-odd-second-II-star-proof-map.png',dpi=100,
            metadata={'Software':'Matplotlib','Author':'Galois representations course'})
plt.close(fig)
