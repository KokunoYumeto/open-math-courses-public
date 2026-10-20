"""Reproducible public proof map; exact values, schematic layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(9,48),dpi=100)
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set_xlim(0,900);ax.set_ylim(4800,0);ax.axis('off')
ink='#243653';blue='#0e668f';fill='#eef6fc';edge='#bbd9ee'
def text(x,y,value,size=9.1,color=ink,weight='normal'):
    ax.text(x,y,value,fontsize=size,color=color,fontweight=weight,va='top')
def panel(y,title,lines):
    ax.add_patch(FancyBboxPatch((34,y),832,440,boxstyle='round,pad=0,rounding_size=10',
                              facecolor=fill,edgecolor=edge,linewidth=1.2))
    text(56,y+23,title,11.7,blue,'bold')
    for j,line in enumerate(lines):text(56,y+67+26*j,line)
text(44,34,'II* on the complete next odd second boundary: n = 6',16,ink,'bold')
text(44,75,'Every unit | Three actual decomposition types | Full rings and original-order indices',10.6,blue)
text(44,110,'Exact conductor 4e+2 | HN1–HN33 | Complete proof and full exercise solution accompany this map',9.7)

panel(160,'1  Whole preparation, invariants and actual point radical | HN1–HN6',[
 'v(π)=1; k=v(a₂)≥3 odd; 2e=3k+1; e≥5; m=k+1; μ=k+3/2.',
 'h>e+μ/2; z>e+(μ+5−k)/2; l>e+(μ+5)/2; v(a₆)=5.',
 'First/third/fourth may vanish; second/sixth units are unrestricted.',
 'All terms retained: v(b₂)=2e+k; v(b₄)>2e+(μ+5)/2;',
 'v(b₆)=2e+5; v(b₈)=4μ; sixth-square alone gives d=4e+10.',
 'The minimal nine-component model is proved before its conductor.',
 'All x-roots have value μ; Z=x/π^m has value 1/2.',
 'Q=Z⁴+C₃Z³+C₂Z²+C₁Z+C₀; coefficient values (2e−1, ≥e+2, 3, 2).',
 'u=−C₀/π² and r=C₁/π³ are units.',
 'N²−4Upt B₀=−3q(x); s=π^((k−1)/2); ζ=N/(2sY).',
 'ζ²=B=πu₀+3π²Z; u₀=b₂/(4π^k) is a base unit.',
 'y=Dζ−A/2; v(D)=2; v(A/2)≥3. B has value1 and is not a unit.',
 'Same point algebra and inverse change of generators are proved exactly.'
])
panel(625,'2  Mixed generator, exact elimination and exhaustive unit test | HN7–HN13',[
 'Choose c̄²=ū; W=(Z²−πc)/(πZ) is integral.',
 'Full relations: Z²−πWZ−πc=0 and P(W)Z+T(W)=0.',
 'P=W³+p₂W²+p₁W+p₀; T=cW²+cp₂W+b.',
 'v(p₂)=2e−2; v(p₁)=e−1; p₀≡r; b≡(c²−u)/π.',
 'If v(u−c²)≥2 (including infinity), choose a=0.',
 'If v(u−c²)=1, choose ā²=(u−c²)/(πc) modulo π; a is a unit.',
 'W̄=ā; T(a)∈πR. Test P(a): unit gives F; divisible by π gives Q.',
 'Q can occur only in the value-one defect case, with ā³+r̄=0.',
 'H=T²+πWTP−πcP² has exact cancellations in degrees6 and5.',
 'For φ=W−a, H(a+φ)/h₄=φ⁴+γ₃φ³+γ₂φ²+γ₁φ+γ₀.',
 'v(γ₃)=1; v(γ₂)≥1; v(γ₁)≥2.',
 'F: v(γ₀)=1.  Q: v(γ₀)≥2 and v(γ₂)=1.',
 'Every coefficient and residue cancellation is written in HN11–HN13.'
])
panel(1090,'3  F: full ramified quartic and actual denominator basis | HN14',[
 'P(W) is a unit; Z=−T(W)/P(W). The shifted quartic is Eisenstein.',
 'F=K(Z)=K(φ), degree4, ramification4, residue degree1; v(φ)=1/4.',
 'C=R[φ] in full; also C=R⊕RZ⊕Rφ⊕RZφ.',
 'The four mixed classes shown below prove coefficientwise integrality.',
 'Degree-three coefficient of φ is c/C₀; degree-two coefficient of Zφ is 1/π.',
 'Their determinant value is −3; restoring x=π^mZ contributes 6m.',
 'i₄=6m+3=d−3. Full derivative minimum6 gives D₄=6 independently.'
])
# This axis encodes exact base-valuation classes, rather than drawing distances in a field.
plot_y=1090+319
ax.plot([100,800],[plot_y,plot_y],color=blue,linewidth=1)
for value,label in [(0,'1'),(.25,'φ'),(.5,'Z'),(.75,'Zφ')]:
    xp=100+700*value/.75
    ax.plot([xp,xp],[plot_y-10,plot_y+10],color=blue,linewidth=1)
    ax.scatter([xp],[plot_y],s=36,color=blue)
    text(xp-14,plot_y-43,label,10.6,blue,'bold')
    text(xp-17,plot_y+21,('0','1/4','1/2','3/4')[round(value*4)],9.8)
text(90,plot_y+60,'Exact fractional v-classes modulo integers; layout has no geometric metric on the field.',8.8)

panel(1555,'4  Complete power-series DVR lemma, including its different | HN15',[
 'R′/R is unramified; V(T)∈R′[[T]]; a,c are units.',
 'F*(T)=(1−πV(T))T²−πaT−πc, retaining the complete series.',
 'F*=T²+πL. Divide by T², substitute its π-error, and repeat.',
 'Corrections at step j are divisible by π^j: the entire division converges.',
 'Reduce any zero-remainder relation modulo π repeatedly to prove uniqueness.',
 'C′=R′[[T]]/(F*) is free with basis (1,T), not just an order in a field.',
 'Modulo π: k′[T]/T². The unique maximal ideal (π,T) equals (T).',
 'T²=π·unit; separation implies every nonzero element is T^j·unit.',
 'Thus C′ is the entire complete DVR, with ramification2 and residue k′.',
 'Its actual monic quadratic g is F* times a unit.',
 'Derivative term values: ≥2e+1, exactly2, ≥2e+3, ≥4.',
 'The unique value2 term is −πa, so the full different over R′ is2.',
 'No approximate polynomial or imported preparation theorem replaces this proof.'
])
panel(2020,'5  Q: both residue types and the whole quadratic-factor algebra | HN16–HN20',[
 'All shifted roots satisfy v(φ)≥1/2; J=φ/Z is integral.',
 'J=1/π−a/Z−c/Z²; τ=1−πJ is a unit.',
 'Full relation τZ²−πaZ−πc=0; the full implicit equation E(J,Z)=0 is in HN17.',
 'Its residue polynomial is Pcal(S)=c²S²+3ca²S+T(a)/π.',
 'Derivative 3ca² is a unit: two simple roots or one irreducible quadratic.',
 'For each residue factor, R → Rj (unramified fj) → Cj (ramification2).',
 'Newton constructs the constant root; a unit partial derivative constructs Vj(T).',
 'Apply HN15 to obtain each entire Cj; J=Vj(Z) and x=π^mZ satisfy original q.',
 'Two linear residues: B₄=C₁×C₂, each (degree,ramification,residue)=(2,2,1).',
 'Irreducible residue quadratic: B₄=C, with (degree,ramification,residue)=(4,2,2).',
 'In both cases Σfj=2; whole base lattice is R⊕RJ⊕RZ⊕RZJ.',
 'The coefficient determinant is c²/C₀², value−4: i₄=6m+4=d−2.',
 'Each full factor different2, weighted by fj, gives D₄=4.'
])
panel(2485,'6  F: the two residue corrections and entire degree-eight point field | HN21–HN24',[
 'Full relation φ⁴=πv₀−γ₃φ³−γ₂φ²−γ₁φ, with v₀=−γ₀/π a base unit.',
 'Choose b̄₀²v̄₀=ū₀ and b̄₁²v̄₀=(b₀²γ₂/π) modulo π.',
 'w=b₀φ²+b₁φ³ has full-ring value2; the second residue coefficient may be zero.',
 'The nine full square-error bounds, in order, are:',
 '8, 10, exactly7, 9, 9, 8, 11, 4e+5, 10.',
 'The uniquely least term is −b₀²γ₃φ³. Hence vF(w²−B)=7.',
 'η=(ζ−w)/φ³ has normalized quadratic constant value1 and trace value4e−1.',
 'Upper parities prove B₈=C[η] in full, degree8/ramification8/residue1 over K.',
 'Derivative upper values8e+1 and8e−2 give relative different8e−2, gap3.',
 'Original y-shift Dw−A/2 is integral; determinant is Dφ³.',
 'Its C-length is vF(Dφ³)=8+3=11; residue weight1.',
 'D₈=2·6+(8e−2)=8e+10; i₈=2i₄+11=8e+25.',
 'No conductor formula was used to construct either full ring.'
])
panel(2950,'7  Q: all entire point factors and exact residue weights | HN25–HN26',[
 'Choose b̄²c̄=ū₀ in the base residue field; w=bZ.',
 'w²−B=π(b²c−u₀)+πb²aZ+πb²JZ²−3π²Z.',
 'The four Cj-values are ≥4, exactly3, ≥4, 5; a is the proved unit.',
 'ηj=(ζ−w)/Z has constant Cj-value1 and trace Cj-value2e.',
 'Each B₈,j=Cj[ηj] is the entire Eisenstein quadratic, with upper parity basis.',
 'Derivative upper values4e+1 and4e give relative different4e, gap1.',
 'y=(Dw−A/2)+DZηj; original determinant Cj-value is4+1=5.',
 'Weight by residue degrees: Σfj·5=10, never by ramification indices.',
 'Split residue case: two point fields, each degree4/ramification4/residue1.',
 'Irreducible residue case: one point field, degree8/ramification4/residue2.',
 'Each point factor has absolute different4+4e.',
 'Thus D₈=Σfj(4+4e)=8e+8; i₈=2i₄+10=8e+26.',
 'Both possible residue types have been constructed over their full rings.'
])
panel(3415,'8  All conductors, infinite boundaries and actual realizations | HN27–HN33',[
 'Column order F,Q: i₄=d−3,d−2; D₄=6,4; point length11,10.',
 'D₈=8e+10,8e+8; i₈=8e+25,8e+26; inertia codimensions (3,7),(2,6).',
 'Quartic ramification4 or2 forces wild action; earlier central−1 kills H¹ invariants.',
 'All point quadratics are ramified: ν=0. Then Swan δ=4e and f=4e+2=d−8.',
 'Normalization i₄+ℓ=d+8; Euler M−1+f=d with minimal M=9.',
 'Every q≥1: k=2q+1; e=3q+2; μ=2q+5/2;',
 'h≥4q+4; z≥3q+6; l≥4q+6; sixth value5; zero lower coefficients allowed.',
 'Over every allowed field take a₁=a₃=a₄=0, a₆=−π^(3k+6)/4, a₂=3π^k u.',
 'u=1 gives the entire totally ramified quartic F.',
 'u=1+π+π²t gives Q, with residue polynomial S²+S+t̄.',
 't=0 gives two ramified quadratics; absolute trace(t̄)=1 gives the residue-degree2 quartic.',
 'Trace-one residues exist in every finite characteristic-two residue field, proved locally.',
 'Exact unbounded proof precedes all four numerical rows and these realizations.'
])
text(48,3935,'Exercise, ten points | Section6.0AL.8 | Complete four-part solution stays with the proof',11.5,blue,'bold')
for j,line in enumerate([
 '(a) Full invariants, same-point radical and complete elimination polynomial (2 points).',
 '(b) Both full quartic algebras, formal division/lifting and actual determinants (3 points).',
 '(c) All full point rings, different towers, residue weights and conductors (3 points).',
 '(d) Infinite preparations, every row and all three actual decomposition types (2 points).',
 'q=1 rows d,i₄,D₄,ℓ,D₈,i₈,δ,f:',
 'F: 30,27,6,11,50,65,20,22.   Q: 30,28,4,10,48,66,20,22.',
 'q=2: F: 42,39,6,11,74,89,32,34.   Q: 42,40,4,10,72,90,32,34.'
]):text(48,3980+29*j,line,9.2)
text(48,4250,'Written sources and exact remaining scope',11.5,blue,'bold')
for j,line in enumerate([
 'Earlier written proofs: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5; Lesson01 0A–0G.',
 'Free human context: J. S. Milne, Algebraic Number Theory, Prop2.43 and Prop7.55/Rem7.56.',
 'https://www.jmilne.org/math/CourseNotes/ANT.pdf',
 'Every specialized result, power-series lemma and residue-field trace test is proved locally.',
 'The n=6 boundary includes every permitted unit and higher coefficient under HM1.',
 'Deeper odd n≥8, lower coefficient bounds and other additive preparations lie outside HM1.',
 'The coefficient hypotheses delimit this family-specific diagram.',
 'General conductor–index identity: JM30–JM32, Section6.0BI.',
 'Positions are schematic layout coordinates.',
 'Panel positions are schematic layout coordinates. The valuation-class axis is exact.',
 'Full arguments, domains, bases, signs, constants and length weights accompany this map.'
]):text(48,4297+29*j,line,9.2)
fig.savefig(base.parent/'assets/odd-second-six-II-star-proof-map.png',dpi=100,
            metadata={'Description':'Original HN proof map: whole n6 boundary, every unit and residue branch; full written proof and exact remaining scope accompany it.'})
plt.close(fig)
