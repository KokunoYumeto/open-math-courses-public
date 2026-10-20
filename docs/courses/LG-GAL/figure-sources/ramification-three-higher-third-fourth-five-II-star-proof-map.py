"""Reproducible public ramification-three proof map; all coordinates are diagram coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig=plt.figure(figsize=(9,44),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(4400,0);ax.axis('off')
ink='#23354f';accent='#1f628b'
ax.text(58,67,'II* at ramification three: both cancellation branches',fontsize=16,weight='bold',color=ink)
ax.text(58,114,'Whole mixed quartic and point rings | Sections6.0AF.1–9, HH1–HH22',fontsize=11,color=accent)
ax.text(58,148,'v(2)=v(a₁)=3; v(a₂)≥2; v(a₃)≥6 or ∞; v(a₄)=v(a₆)=5.',fontsize=10,color=ink)
panels=[
 ('1  Integral preparation and the discriminant test  |  HH1–HH7',[
  'If v(a₂)=2, choose r of value 1 by a residue square; otherwise r=0.',
  'y=Y+rx raises v(a₂′)≥3; all other exact coefficient tests are retained.',
  'All four b-invariants are unchanged. R[x,Y]=R[x,y], also over B₄.',
  'Rename the prepared coefficients: v(b₂,b₄,b₆,b₈)=(6,8,11,10).',
  'D=a₁²a₄−12a₆ has value at least 11; D=0 is allowed.',
  'Exact congruence: Δ−(D²−b₂³a₆) ∈ π²⁴R; v(b₂³a₆)=23.',
  'Branch A: v(D)=11 ⇒ d=22.  Branch B: v(D)≥12 or D=0 ⇒ d=23.',
  'v(c₄)=12; v(j)=14 or 13>0. Earlier minimal II* resolution gives M=9.',
 ]),
 ('2  One residual coordinate and one full quartic ring  |  HH8–HH11',[
  'Every quartic root has v(x)=5/2. Set c=1+2ζ, ζ²+ζ+1=0; c²=−3.',
  't=cx²+a₄; M₀=3b₄+2ca₄ has v≥9; C₀=b₈+a₄² has v=11.',
  'Choose β of value 3 with C=C₀−β²a₄/c of value at least 12.',
  's=t−βx; P=b₂−2cβ has v≥6 (may vanish).',
  'L=3b₆−2βa₄+β³/c has exact v=9.',
  's²=Px³+M₀x²+Lx+(β²/c)s+C ⇒ exact v(s)=23/4.',
  'F=K(x): degree/ramification 4, residue degree 1. Set v_F=4v.',
  'B₄=R⊕R(x/π²)⊕R(s/π⁵)⊕R(xs/π⁸), in full. i₄=15.',
  'Basis values 0,1/2,3/4,1/4: an integral sum has all coefficients in R.',
  'τ=xs/π⁸ has v_F(τ)=1; its four power classes prove B₄=R[τ].',
 ]),
 ('3  The entire mixed point error  |  HH12–HH14',[
  'E(w)=w²+(a₁x+a₃)w−(x³+a₂x²+a₄x+a₆); T(w)=a₁x+a₃+2w.',
  'w₀=t/a₁=(s+βx)/a₁ has v=5/2.',
  'E(w₀)=J₃x³+J₂x²+J₁x+J₀; coefficient values/bounds: 0, ≥3, 5, ≥8.',
  'J₃=c+4a₂/a₁²; J₂=(c+3)(a₃/a₁+2a₄/a₁²)−a₂;',
  'J₁=3b₆/a₁²; J₀=a₂b₆/a₁².',
  'Hₓₛ=J₃/c; Hₛ=(J₃β/c+J₂)/c;',
  'Hₓ=J₁−J₃a₄/c+βHₛ; H₀=J₀−a₄Hₛ.',
  'E(w₀)=Hₓₛxs+Hₛs+Hₓx+H₀: every term retained.',
  'v(Hₓₛ)=0; v(Hₛ)≥3; v(H₀)≥8; Hₓ+D/a₁² ∈ π⁶R.',
  'Thus v(Hₓ)=5 in A, and v(Hₓ)≥6 in B.',
 ]),
 ('4  The same test controls the cancelled trace  |  HH15',[
  'Z=a₁²+2β; U=Z/a₁.',
  'Whole trace: T(w₀)=Ux+(2/a₁)s+a₃.',
  'β²a₄/c−a₆a₁² has v≥12; retain this full residue error.',
  'Z²−(a₁²/a₄)D = (4c/a₄)(β²a₄/c−a₆a₁²)',
  '                        +4a₁²β+4a₆a₁²(c+3)/a₄.',
  'The three bounds are 13,15,15: the remainder lies in π¹³R.',
  'A: Z has v=6; U has v=3; Ux alone gives trace v=11/2 (F-value22).',
  'B: Z has v≥7; U has v≥4; (2/a₁)s alone gives v=23/4 (F-value23).',
  'The integer valuation of Z is essential when its square has v≥13.',
 ]),
 ('5  Branch A: correction with the second coordinate  |  HH16–HH18',[
  'v(D)=11; initial error v=15/2, or normalized30.',
  'Choose λ∈R× by λ²≡−π⁴Hₓ/L in the residue field.',
  'V=Hₓ+λ²L/π⁴ has v≥6; ψ=λs/π² has v=15/4; w_A=w₀+ψ.',
  'E(w_A)=(Hₛ+λ²β²/(cπ⁴))s+Hₓₛxs+Vx+H₀',
  '            +(λ²/π⁴)(Px³+M₀x²+C)+ψT(w₀).',
  'The s-coefficient has exact v=2; its term alone gives v=31/4.',
  'Seven other bounds: 33/4,17/2,8,19/2,10,8,37/4, all larger.',
  'Full trace correction 2ψ has v=27/4>11/2.',
  'Result: v_F(E)=31, v_F(T)=22; v(w_A)=5/2.',
 ]),
 ('6  Branch B: scalar cancellation of the constant  |  HH19',[
  'v(D)≥12 or D=0; v(Hₓ)≥6. If v(H₀)≥9, choose σ=0.',
  'Otherwise v(H₀)=8: choose σ of v=4 with H₀+σ² of v≥9.',
  'w_B=w₀+σ. Retain the entire scalar square and trace cross term:',
  'E(w_B)=Hₓₛxs+Hₛs+Hₓx+(H₀+σ²)+σT(w₀).',
  'Five bounds: 33/4,35/4,17/2,9,39/4.',
  'The first is exact and uniquely least: v_F(E)=33.',
  '2σ has v≥7>23/4, so v_F(T)=23 is retained.',
  'v(w_B)=5/2. Zero coefficient/test cases obey the same proof.',
 ]),
 ('7  Two whole point rings; one relative different  |  HH20–HH21',[
  'A: (w,m)=(w_A,15).  B: (w,m)=(w_B,16).',
  'η=(y−w)/τᵐ; η²+(T/τᵐ)η+E/τ²ᵐ=0.',
  'Both branches: constant F-value1, trace F-value7. Eisenstein.',
  'Upper basis parities 0 and1 prove the entire B₈=B₄[η].',
  'Relative point index is m. Derivative upper values25 and14 give different14.',
  '                            A                  B',
  'd, i₄, D₄              22,15,14          23,15,16',
  'point index ℓ                15                 16',
  'D₈=2D₄+14                  42                 46',
  'i₈=2i₄+ℓ                   45                 46',
 ]),
 ('8  Swan, conductor and the proved comparisons  |  HH22',[
  'Both full algebras are totally ramified fields: ε₄=3, ε₈=7, ν=0.',
  'Degree-four inertia orbit forces wild action; earlier quaternion proof gives',
  'zero cohomology invariants. Apply the actual earlier Swan comparison:',
  '                            A                  B',
  'δ=2d−i₈+i₄−2               12                 13',
  'f=2+δ                       14                 15',
  'i₄+ℓ=d+M−1                 30                 31',
  'M−1+f=d                    22                 23',
  'These equalities follow from full rings; none is an input to their construction.',
 ]),
]
for i,(title,lines) in enumerate(panels):
    top=188+i*480
    ax.add_patch(FancyBboxPatch((50,top),800,465,boxstyle='round,pad=0,rounding_size=11',facecolor='#eef6fc',edgecolor='#c9dfee',linewidth=1.1))
    ax.text(72,top+42,title,fontsize=11,weight='bold',color=accent)
    for j,line in enumerate(lines):ax.text(72,top+85+j*32,line,fontsize=9.5,color=ink)
ax.text(58,4070,'Exercise, eight points  |  Section6.0AF.8',fontsize=12,weight='bold',color=accent)
ax.text(58,4107,'Prove both discriminants and the trace test; show the full quartic basis;',fontsize=10,color=ink)
ax.text(58,4135,'retain every corrected error term; prove both full point rings and conductors.',fontsize=10,color=ink)
ax.text(58,4190,'Sources and exact boundaries',fontsize=12,weight='bold',color=accent)
footer=[
 'Prerequisite results: Lesson08 6.0E/H/I.8–I.9/K.2/K.6/P.5/AD.1; Lesson01 0A–0G.',
 'Source: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56, pp.129–130.',
 'https://www.jmilne.org/math/CourseNotes/ANT.pdf',
 'Actual first3/fourth5/third≥5 preparation covered for all e≥3 with6AD/6AE.',
 'e3/fourth≥6, higher first and other families are outside these hypotheses.',
 'Coordinates specify the diagram layout.',
]
for j,line in enumerate(footer):ax.text(58,4231+j*23,line,fontsize=8.5,color=ink)
fig.savefig(Path(__file__).resolve().parents[1]/'assets/ramification-three-higher-third-fourth-five-II-star-proof-map.png',dpi=100,facecolor='white');plt.close(fig)
