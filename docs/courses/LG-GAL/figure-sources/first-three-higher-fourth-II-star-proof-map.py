"""Reproducible public proof map; positions below are diagram layout coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

base=Path(__file__).resolve().parent
fig=plt.figure(figsize=(9,32),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(3200,0);ax.axis('off')
ink='#253858';blue='#15668a';fill='#edf6fc';border='#cbdff0'
ax.text(45,54,'II* with first valuation three and higher fourth valuation',
        color=ink,fontsize=14.5,fontweight='bold',fontfamily='DejaVu Sans')
ax.text(45,96,'Every e ≥ 3 | Whole quartic and point rings | HI1–HI14',
        color=blue,fontsize=11.5,fontfamily='DejaVu Sans')
ax.text(45,130,'v(a₁)=3; v(a₂)≥2; v(a₃),v(a₄)≥6 or ∞; v(a₆)=5.',
        color=ink,fontsize=10.5,fontfamily='DejaVu Sans')

def panel(y,title,lines):
    ax.add_patch(FancyBboxPatch((35,y),830,330,boxstyle='round,pad=0,rounding_size=10',
        linewidth=1.2,edgecolor=border,facecolor=fill))
    ax.text(57,y+37,title,color=blue,fontsize=11.5,fontweight='bold',fontfamily='DejaVu Sans')
    for j,line in enumerate(lines):
        ax.text(57,y+78+27*j,line,color=ink,fontsize=9.7,fontfamily='DejaVu Sans')

panel(170,'1  Integral preparation preserves both orders  |  HI1–HI2',[
    'If v(a₂)=2, choose r of value 1 cancelling its leading residue square; else r=0.',
    'y=Y+rx gives a₁′=a₁+2r; a₂′=a₂−a₁r−r²; a₃′=a₃;',
    'a₄′=a₄−a₃r; a₆′=a₆. The new second valuation is at least 3.',
    'Changes to first and fourth coefficients have values ≥4 and ≥7.',
    'The four b-invariants are unchanged by exact expansion.',
    'R[x,Y]=R[x,y]; the same equality holds over the full B₄.',
    'Nine-component II* resolution and earlier minimality apply: M=9.',
    'Finite unramified cube-root extension preserves full normalization and indices.'
])
panel(515,'2  The complete discriminant has a unique minimum  |  HI3–HI5',[
    'v(b₂)=6; v(b₄)≥9; v(b₈)=11. Zero b₄ is allowed.',
    'b₆=a₃²+4a₆: the finite competing values have opposite parity.',
    'Thus v(b₆)=11 for e=3; v(b₆)≥12 for e≥4.',
    'Δ=−b₂²b₈−8b₄³−27b₆²+9b₂b₄b₆.',
    'Term values/bounds: 23, ≥36, 22 or ≥24, ≥26.',
    'e=3: unique minimum 22.  e≥4: unique minimum 23.',
    'v(c₄)=12; v(j)=14 or 13>0. Potential good reduction is proved earlier.',
    'These discriminants are minimal by the actual regular-model/origin proof.'
])
panel(860,'3  Every quartic root; the entire power lattice  |  HI6–HI7',[
    'q=x⁴+(b₂/3)x³+b₄x²+b₆x+b₈/3. Every root has v(x)=11/4.',
    'Endpoints have value 11; middle bounds are 57/4,29/2,55/4, all larger.',
    'The denominator forces degree/ramification 4 and residue degree 1.',
    'B₄=R⊕R(x/π²)⊕R(x²/π⁵)⊕R(x³/π⁸), in full; i₄=15.',
    'Basis values 0,3/4,1/2,1/4: an integral sum has all coefficients in R.',
    'τ=x³/π⁸ has v_F(τ)=1 for v_F=4v.',
    'Its four power classes prove the whole ring B₄=R[τ].',
    'Full-ring discriminant D₄=2d−30: 14 for e=3; 16 for e≥4.'
])
panel(1205,'4  Every point-error coefficient and constant retained  |  HI8–HI10',[
    'c=1+2ζ; ζ²+ζ+1=0; c²=−3; v(c+3)=e. Set w=(cx²+a₄)/a₁.',
    'E(w)=w²+(a₁x+a₃)w−(x³+a₂x²+a₄x+a₆); v(w)=5/2.',
    'E(w)=J₃x³+J₂x²+J₁x+J₀, with no omitted remainder:',
    'J₃=c+4a₂/a₁²; J₂=(c+3)(a₃/a₁+2a₄/a₁²)−a₂;',
    'J₁=3b₆/a₁²; J₀=a₂b₆/a₁².',
    'Unrestricted identity: a₁²(E−ΣJⱼxʲ)=(c²+3)x⁴−3q(x).',
    'e=3 term bounds: 33/4, ≥17/2, 31/4, ≥8; the linear term is least.',
    'e≥4: 33/4, ≥17/2, ≥35/4, ≥9; the cubic term is least.'
])
panel(1550,'5  Full trace and the two point denominators  |  HI11–HI12',[
    'T(w)=a₁x+a₃+2w. Contribution values: 23/4, ≥6, e+5/2.',
    'e=3: doubled shift is uniquely least; v_F(T)=22.',
    'e≥4: first-times-root term is uniquely least; v_F(T)=23.',
    'Full error values v_F(E)=31 or 33; choose m=15 or 16 respectively.',
    'η=(y−w)/τᵐ satisfies η²+(T/τᵐ)η+E/τ²ᵐ=0.',
    'In both regimes: constant F-value 1 and trace F-value 7.',
    'This is Eisenstein; the point extension is a totally ramified quadratic.',
    'No scalar, residue or second-coordinate correction is needed.'
])
panel(1895,'6  Both whole point rings and one exact different  |  HI12–HI13',[
    'Upper basis parities 0 and 1 prove the full B₈=B₄[η].',
    'The generator-change determinant is τᵐ, giving relative point index m.',
    'For the original point coordinate use w+rx; the integral shear preserves its order.',
    'Derivative upper values: 8e+1 and 14; the latter is always uniquely least.',
    'Relative different D₈/₄=14; both residue degrees are 1.',
    '                       e=3                     e≥4',
    'd, i₄, D₄         22,15,14                 23,15,16',
    'ℓ, D₈, i₈         15,42,45                 16,46,46'
])
panel(2240,'7  Swan, conductor and the proved numerical comparisons  |  HI14',[
    'Both full algebras are totally ramified fields: ε₄=3, ε₈=7, ν=0.',
    'A degree-four inertia orbit forces wild action; the earlier quaternion proof',
    'gives zero cohomology invariants. Apply the written permutation comparison:',
    '                       e=3                     e≥4',
    'δ=2d−i₈+i₄−2        12                       13',
    'f=2+δ                14                       15',
    'i₄+ℓ=d+M−1           30                       31',
    'M−1+f=d              22                       23'
])
ax.text(45,2630,'Exercise, six points  |  Section6.0AG.7',color=blue,fontsize=11.5,fontweight='bold')
ax.text(45,2672,'Prove preparation and both discriminants; retain the full errors and traces;',
        color=ink,fontsize=9.7)
ax.text(45,2704,'prove both whole rings, their different and conductors, and the exact union of scopes.',
        color=ink,fontsize=9.7)
ax.text(45,2770,'Sources and exact boundaries',color=blue,fontsize=11.5,fontweight='bold')
for j,line in enumerate([
    'Prerequisite results: Lesson08 6E/H/I.8–I.9/K.2/K.6/P.5/AD.1; Lesson01 0A–0G.',
    'Source: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56,',
    'printed pp.129–130. https://www.jmilne.org/math/CourseNotes/ANT.pdf',
    'With6AC–6AF: all actual e≥3, first3, second≥2, third/fourth≥5, sixth5.',
    'Higher/infinite first values and other complements are outside these hypotheses.',
    'General conductor–index identity: JM30–JM32, Section6.0BI.',
    'Coordinates specify the diagram layout.'
]):ax.text(45,2812+32*j,line,color=ink,fontsize=9.2)
fig.savefig(base.parent/'assets/first-three-higher-fourth-II-star-proof-map.png',dpi=100,
            metadata={'Software':'Matplotlib','Author':'Galois representations course'})
plt.close(fig)
