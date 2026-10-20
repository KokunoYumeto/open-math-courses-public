"""Reproducible public higher-third proof map; coordinates are diagram coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig = plt.figure(figsize=(9,40),dpi=100,facecolor='white')
ax = fig.add_axes([0,0,1,1])
ax.set_xlim(0,900)
ax.set_ylim(4000,0)
ax.axis('off')
ink='#23354f'
accent='#1f628b'
ax.text(58,68,'II* with higher third valuation and fourth five',fontsize=17,weight='bold',color=ink)
ax.text(58,118,'Full rings and the odd point error | Sections 6.0AE.1–7',fontsize=11,color=accent)
ax.text(58,147,'Exact scope: e≥4; v(a₁)=3; v(a₂)≥2; v(a₃)≥6 or ∞; v(a₄)=v(a₆)=5.',fontsize=10,color=ink)

panels=[
('1  Raise the second valuation by an integral shear  |  HG1–HG2',[
 'If v(a₂)=2, choose r of value 1 by a residue square; otherwise r=0.',
 'Substitute y=Y+rx:',
 'a₁′=a₁+2r,   a₂′=a₂−a₁r−r²,   a₃′=a₃,',
 'a₄′=a₄−a₃r,   a₆′=a₆.',
 'Then v(a₂′)≥3; all other exact coefficient tests are preserved.',
 'The four b-invariants are unchanged by direct expansion.',
 'R[x,Y]=R[x,y]; both directions are integral. Original orders retained.',
 'Rename the prepared coefficients below. Finite unramified splitting',
 'preserves full rings, indices, discriminants and conductor by 6.0AD.1.',
]),
('2  Invariants, slope and the residual coordinate  |  HG3–HG8',[
 'v(b₂)=6; v(b₄)≥9; v(b₆)≥12; v(b₈)=10.',
 'Discriminant term bounds: 22, 39, 24, 27.  Unique minimum: d=22.',
 'v(c₄)=12; v(j)=14>0: potentially good.  Minimal II* has M=9.',
 'Every quartic root has v(x)=5/2; the slope alone proves no full ring.',
 'c=1+2ζ; ζ²+ζ+1=0; c²=−3.  t=cx²+a₄.',
 'M₀=3b₄+2ca₄ has v≥9.  C₀=b₈+a₄² has exact v=11.',
 'Choose β of value 3: C=C₀−β²a₄/c has v≥12.  s=t−βx.',
 'P=b₂−2cβ has v=6; L=3b₆−2βa₄+β³/c has exact v=9.',
 's²=Px³+M₀x²+Lx+(β²/c)s+C; unique minimum forces v(s)=23/4.',
]),
('3  The entire quartic lattice and its uniformizer  |  HG9',[
 'Denominator 4 proves [F:K]=e(F/K)=4, residue degree 1; F=K(x).',
 'Unscaled mixed change determinant c² is a unit.',
 'Ordered basis: 1, x/π², s/π⁵, xs/π⁸.',
 'v(1)=0; v(x/π²)=1/2; v(s/π⁵)=3/4; v(xs/π⁸)=1/4.',
 'Distinct fractional classes preclude cancellation of a least term.',
 'A field-basis combination is integral exactly when each coefficient lies in R.',
 'B₄=R ⊕ R(x/π²) ⊕ R(s/π⁵) ⊕ R(xs/π⁸): the full ring.',
 'i₄=2+5+8=15; D₄=2d−2i₄=14.',
 'τ=xs/π⁸ has v_F(τ)=1. Its four power classes prove B₄=R[τ].',
]),
('4  Retain the entire initial error in mixed coordinates  |  HG10–HG13',[
 'A=a₁x+a₃; E(w)=w²+Aw−(x³+a₂x²+a₄x+a₆); T(w)=A+2w.',
 'w₀=(cx²+a₄)/a₁ has value 5/2.',
 'E(w₀)=J₃x³+J₂x²+J₁x+J₀; coefficient bounds 0, 3, 6, 9.',
 'Hₓₛ=J₃/c; Hₛ=(J₃β/c+J₂)/c;',
 'Hₓ=J₁−J₃a₄/c+βHₛ; H₀=J₀−a₄Hₛ.',
 'E(w₀)=Hₓₛxs+Hₛs+Hₓx+H₀. All signed terms retained.',
 'Coefficient values: v(Hₓₛ)=0, v(Hₛ)≥3, v(Hₓ)=5, v(H₀)≥8.',
 'Term bounds: 33/4, 35/4, 15/2, 8. Exact quartic error: 30.',
 'a₁x alone gives trace value 11/2; quartic trace: 22.',
]),
('5  Cancel the even error using the second coordinate  |  HG14–HG16',[
 'Lift a residue square root of the unit −π⁴Hₓ/L to λ∈R×.',
 'V=Hₓ+λ²L/π⁴ has v≥6.  ψ=λs/π² has v=15/4.',
 'Set w=w₀+ψ. Retain both ψ² and the cross term ψT(w₀).',
 'E(w)=(Hₛ+λ²β²/(cπ⁴))s+Hₓₛxs+Vx+H₀',
 '        +(λ²/π⁴)(Px³+M₀x²+C)+ψT(w₀).',
 'The s-coefficient has exact v=2 (bounds 3 versus exact 2).',
 'Its term alone has value 31/4.',
 'Other bounds: 33/4, 17/2, 8, 19/2, 10, 8, 37/4: all strictly greater.',
 'Thus v_F(E(w))=31; v_F(T(w))=22; v(w)=5/2.',
]),
('6  The full point ring and the different  |  HG17–HG18',[
 'η=(y−w)/τ¹⁵ satisfies η²+(T/τ¹⁵)η+E/τ³⁰=0.',
 'Constant valuation 1 and trace valuation 7: Eisenstein over B₄.',
 'The point field F₈/F has degree/ramification 2 and residue degree 1.',
 'Upper basis values 0 and 1 have opposite parity.',
 'Hence B₈=B₄[η] in full, not just an integral suborder.',
 'Exact generator determinant τ⁻¹⁵ proves point index 15.',
 'Derivative values 8e+1≥33 and 14 give exact relative different 14.',
 'D₈=2D₄+14=42; i₈=2i₄+15=45=(6d−D₈)/2.',
 'Return to the original y by adding rx to w; original orders agree.',
]),
('7  Swan, conductor and Euler identity  |  HG18–HG20',[
 'One inertia orbit in each totally ramified field: ε₄=3, ε₈=7.',
 'Even degree-four orbit forces nontrivial wild inertia.',
 'Potential good reduction and earlier quaternion/kernel proof give ν=0.',
 'Swan δ=2d−i₈+i₄−(ε₈−ε₄)/2=44−45+15−2=12.',
 'Conductor f=2+δ=14.',
 'NF24: i₄+15=30=d+M−1.',
 'Euler/discriminant: M−1+f=9−1+14=22=d.',
 'These are outputs of the full ring calculations, not assumed inputs.',
]),
]
for i,(title,lines) in enumerate(panels):
    top=192+i*485
    ax.add_patch(FancyBboxPatch((50,top),800,470,boxstyle='round,pad=0,rounding_size=11',facecolor='#eef6fc',edgecolor='#c9dfee',linewidth=1.1))
    ax.text(72,top+42,title,fontsize=11,weight='bold',color=accent)
    for j,line in enumerate(lines):
        ax.text(72,top+88+j*32,line,fontsize=10,color=ink)

ax.text(58,3680,'Exercise, six points  |  Section 6.0AE.6',fontsize=12,weight='bold',color=accent)
ax.text(58,3720,'Explain the integral shear and error 30; construct λ and the entire new error;',fontsize=10,color=ink)
ax.text(58,3748,'prove full point index 15, different 14, absolute discriminant 42 and conductor 14.',fontsize=10,color=ink)
ax.text(58,3810,'Sources and exact boundaries',fontsize=12,weight='bold',color=accent)
footer=[
 'Prerequisite results: Lesson08 6.0U/E/H/I.8–I.9/K.2/K.6/P.5/AD.1; Lesson01 0A–0G.',
 'Source: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56, pp.129–130.',
 'https://www.jmilne.org/math/CourseNotes/ANT.pdf',
 'e3 with higher third/fourth5, higher first and other families are outside these hypotheses.',
 'Coordinates specify the diagram layout.',
]
for j,line in enumerate(footer):
    ax.text(58,3854+j*23,line,fontsize=8.5,color=ink)
fig.savefig(Path(__file__).resolve().parents[1] / 'assets/higher-third-fourth-five-II-star-proof-map.png',dpi=100,facecolor='white')
plt.close(fig)
