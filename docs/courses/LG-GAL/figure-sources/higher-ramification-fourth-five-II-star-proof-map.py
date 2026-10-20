"""Reproducible public fourth-five proof map; source coordinates are diagram coordinates."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig=plt.figure(figsize=(9,36),dpi=100,facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#21334c';blue='#225c82';fill='#edf5fa';border='#c5dbe8'
ax.text(.065,.984,'II* at higher ramification: the fourth-five case',fontsize=18,
        color=ink,weight='bold',va='top')
ax.text(.065,.968,'The full mixed quartic ring and both point corrections  |  Sections 6.0AD.1–8',
        fontsize=12,color=blue,va='top')

panels=[
 ('1  Actual coefficients and invariants  |  FF1–FF5',[
  'v(π)=1;  e=v(2)≥3.  These are tests on the actual equation.',
  'v(a₁)=3;  v(a₂)≥2;  v(a₃)=v(a₄)=v(a₆)=5.  a₂ may be zero.',
  'v(b₂)=6;  v(b₄)≥8;  v(b₆)=10;  v(b₈)=10.',
  'Cancellation in b₄ at e=3 is allowed.  No exact b₄ value is used.',
  'v(Δ)=20;  v(c₄)=12;  v(j)=16: potentially good.  M=9.',
  'Every root of q has v(x)=5/2; this alone proves no full ring.',
  'Optional finite unramified splitting preserves indices and conductor.',
 ]),
 ('2  A second quartic coordinate  |  FF6–FF10',[
  'c=1+2ζ;  ζ²+ζ+1=0;  c²=−3;  v(c+3)=e.',
  't=cx²+a₄;  C₀=a₆b₂−a₁a₃a₄+a₂a₃² has value 11.',
  'Residue squaring: v(β)=3; C=C₀−β²a₄/c; v(C)≥12.',
  's=t−βx;  P=b₂−2cβ;  M₀=3b₄+2ca₄;',
  'L=3b₆−2βa₄+β³/c has exact value 9.',
  's²=Px³+M₀x²+Lx+(β²/c)s+C.  v(P)≥6;  v(M₀)=8.',
  'Four polynomial-term bounds: 27/2, 13, 23/2, 12.',
  'Unique-minimum arguments force v(s)=23/4.',
  'Denominator four proves [F:K]=e(F/K)=4; residue degree 1.',
 ]),
 ('3  The entire quartic lattice  |  FF11',[
  'F=K(x);  v_F=4v.  The unscaled mixed change has determinant c².',
  'Ordered basis: 1, x/π², s/π⁵, xs/π⁸.',
  'v(1)=0; v(x/π²)=1/2; v(s/π⁵)=3/4; v(xs/π⁸)=1/4.',
  'Distinct fractional classes prevent cancellation of the least term.',
  'A combination is integral exactly when every coefficient lies in R.',
  'B₄=R ⊕ R(x/π²) ⊕ R(s/π⁵) ⊕ R(xs/π⁸), the full ring.',
  'i₄=2+5+8=15;  D₄=2d−2i₄=10.',
  'τ=xs/π⁸ has v_F(τ)=1.  Its power classes prove B₄=R[τ].',
 ]),
 ('4  The complete first error and scalar correction  |  FF12–FF14',[
  'A=a₁x+a₃;  E(w)=w²+Aw−(x³+a₂x²+a₄x+a₆);  T(w)=A+2w.',
  't=s+βx has value 11/2;  w₀=t/a₁ has value 5/2.',
  'E(w₀)=J₃x³+J₂x²+J₁x+J₀;  coefficient bounds 0, ≥2, 4, ≥6.',
  'J₁=3b₆/a₁²;  J₀=a₂b₆/a₁².  All signed terms are in FF13.',
  'If v(J₀)=6, choose σ=π³u by a residue square; otherwise σ=0.',
  'Then v(J₀+σ²)≥7.  Put w₁=w₀+σ.',
  'E(w₁)=J₁x+R₁, with every term of R₁ of value ≥7.',
  'v_F(E(w₁))=26;  v_F(T(w₁))=20.',
  'The even error 26 leaves a unit constant after denominator 13.',
 ]),
 ('5  The uniformizer residue correction  |  FF15–FF17',[
  'Choose unit λ by the residue square of cπ¹⁰J₁/(La₄).',
  'C₁=J₁−λ²La₄/(cπ¹⁰) has value ≥5;  L and a₄ are nonzero.',
  'ψ=λxs/π⁵=λπ³τ has value 13/4.',
  'Its whole square, with the exact five-term remainder in FF16, is',
  'ψ²=−λ²La₄x/(cπ¹⁰)−λ²β²a₄s/(c²π¹⁰)+λ²R₀/π¹⁰.',
  'The five bounds for R₀/π¹⁰ are 17/2, 8, 7, 15/2, 29/4.',
  'Put w=w₁+ψ.  Retain the cross term ψT(w₁), of value 33/4.',
  'E(w)=−λ²β²a₄s/(c²π¹⁰)+C₁x+R₁+λ²R₀/π¹⁰+ψT(w₁).',
  'The s coefficient has exact value 1: its term alone has value 27/4.',
 ]),
 ('6  The full point field and its different  |  FF18–FF20',[
  'The other four error bounds are 15/2, 7, 7, 33/4.',
  'w=(cx²+a₄)/a₁+σ+λπ³τ;  v(w)=5/2;  v(T(w))=5.',
  'In F: exact error 27, trace 20; normalized v_F(τ)=1.',
  'η=(y−w)/τ¹³ satisfies η²+(T/τ¹³)η+E/τ²⁶=0.',
  'Constant valuation 1, trace valuation 7: Eisenstein.',
  'F₈/F has degree and ramification 2, residue degree 1.',
  'Opposite basis parities prove B₈=B₄[η] in full.',
  'Exact relative point index 13 comes from the generator determinant.',
  'Upper derivative values 8e+1≥25 and 14 give different 14.',
 ]),
 ('7  Exact indices, conductor and Euler identity  |  FF20–FF21',[
  'D₈=2D₄+14=34;  i₈=2i₄+13=43=(6d−D₈)/2.',
  'Each totally ramified field gives one inertia orbit: ε₄=3; ε₈=7.',
  'The even sign-pair orbit forces a nontrivial wild image; ν=0.',
  'Earlier quaternion/kernel proofs give zero cohomology invariants.',
  'Swan δ=2d−i₈+i₄−(ε₈−ε₄)/2=40−43+15−2=10.',
  'Conductor f=2+δ=12.  NF24: i₄+13=28=d+M−1.',
  'Euler/discriminant: M−1+f=9−1+12=20=d.',
  'Together with6.0AC, this covers actual first3/third5/fourth≥5.',
 ])
]
top=.944; height=.112; gap=.010
text_artists=[]
for title,lines in panels:
    bottom=top-height
    patch=FancyBboxPatch((.06,bottom),.88,height,boxstyle='round,pad=0.004,rounding_size=0.008',
                         facecolor=fill,edgecolor=border,linewidth=1)
    ax.add_patch(patch)
    text_artists.append((ax.text(.080,top-.010,title,fontsize=12.0,weight='bold',color=blue,va='top'),bottom,top))
    for i,line in enumerate(lines):
        text_artists.append((ax.text(.080,top-.024-i*.0088,line,fontsize=10.9,color=ink,va='top'),bottom,top))
    top=bottom-gap

ax.text(.065,.077,'Exercise, six points  |  Section 6.0AD.7',fontsize=12.0,color=blue,weight='bold',va='top')
ax.text(.065,.066,'Before ψ, error 26 gives a unit constant. Construct λ, retain both cross and square terms,\n'
        'and prove the corrected full index 13, different 14, absolute discriminant 34 and conductor 12.',
        fontsize=10.2,color=ink,va='top',linespacing=1.5)
ax.text(.065,.045,'Sources and boundaries',fontsize=12.0,color=blue,weight='bold',va='top')
ax.text(.065,.034,'Prerequisite results: Lesson08, 6.0U/E/H/I.8–I.9/K.2/K.6/P.5/AB.7/AC; earlier local-field proofs,0A–0G.\nSource: J. S. Milne, Algebraic Number Theory, Prop.7.55/Rem.7.56, pp.129–130.\nhttps://www.jmilne.org/math/CourseNotes/ANT.pdf\nScope is exactly FF1; raised/infinite third and other families are outside this diagram.\nCoordinates specify the diagram layout.',
        fontsize=9.2,color=ink,va='top',linespacing=1.4)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
for artist,bottom,top in text_artists:
    box=artist.get_window_extent(renderer).transformed(ax.transAxes.inverted())
    assert .06<=box.x0 and box.x1<=.94 and bottom<=box.y0 and box.y1<=top,(artist.get_text(),box.bounds)
fig.savefig(Path(__file__).resolve().parents[1] / 'assets/higher-ramification-fourth-five-II-star-proof-map.png',dpi=100,facecolor='white')
plt.close(fig)
