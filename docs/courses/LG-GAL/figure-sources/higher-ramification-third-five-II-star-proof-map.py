"""Reproducible original proof map of AI with exact public proof locators."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig = plt.figure(figsize=(9,27),dpi=100,facecolor='white')
ax = fig.add_axes([0,0,1,1]);ax.set_xlim(0,900);ax.set_ylim(0,2700);ax.axis('off')
ink='#172840';blue='#24577b';accent='#1f766a'
def text(x,y,s,size=13,color=ink,weight='normal'):
    ax.text(x,y,s,fontsize=size,color=color,fontweight=weight,va='top',ha='left',linespacing=1.55)
def panel(top,height,title,body,color='#edf4f8'):
    ax.add_patch(FancyBboxPatch((32,top-height),836,height,boxstyle='round,pad=0,rounding_size=12',facecolor=color,edgecolor='#cedde6',linewidth=1.2))
    text(56,top-20,title,16,blue,'bold');text(56,top-66,body,13)

text(35,2665,'II* at higher ramification: the full point ring',21,ink,'bold')
text(35,2610,'Exact first valuation 3; exact third valuation 5.  Sections 6.0AC.1–7',14,blue)
panel(2550,300,'1  Actual hypotheses and discriminant  |  HF1–HF6',
 'v(π)=1;  e=v(2)≥3.  These bounds concern the actual equation.\n'
 'v(a₁)=3;  v(a₂)≥2;  v(a₃)=5;  v(a₄)≥6;  v(a₆)=5.\n'
 'a₂ and a₄ may be zero (valuation +∞).  M=9 components.\n'
 'v(b₂)=6;  v(b₄)≥8;  v(b₆)=10;  v(b₈)=11.\n'
 'd=v(Δ)=20;  v(c₄)=12;  v(j)=16: potentially good.\n'
 'Every quartic root has v(x)=11/4;  [F:K]=4, residue degree 1.')
panel(2218,298,'2  The entire quartic lattice  |  HF7–HF8',
 'B₄ = R ⊕ R(x/π²) ⊕ R(x²/π⁵) ⊕ R(x³/π⁸).\n'
 'Values: 0, 3/4, 1/2, 1/4 — distinct fractional classes.\n'
 'A sum is integral exactly when each R-coefficient is integral.\n'
 'The determinant gives i₄=2+5+8=15, not just a bound.\n'
 'D₄=2d−2i₄=10.  τ=x³/π⁸ has v_F(τ)=1.\n'
 'The same distinct-class argument proves B₄=R[τ]; v_F=4v.')
panel(1888,360,'3  Second residue cancellation of the constant  |  HF9–HF13',
 'Choose a unit k so J₀=−k²b₈/(3π⁶)−a₆ has value ≥6.\n'
 'w₀=kx²/π³.  E(w₀)=J₃x³+J₂x²+J₁x+J₀.\n'
 'J-coefficient bounds: ≥0, ≥2, exactly 4, ≥6.\n'
 'If v(J₀)=6, its constant precedes the 27/4 linear term.\n'
 'Choose σ=π³u by ū²=−J₀/π⁶ modulo π; otherwise σ=0.\n'
 'Then v(σ)≥3 and v(J₀+σ²)≥7.  Put w=w₀+σ.\n'
 'Keep every cross term: E(w)=E(w₀)+σ(A+2w₀)+σ².\n'
 'A=a₁x+a₃;  G=x³+a₂x²+a₄x+a₆.\n'
 'E(w)=w²+Aw−G: this is the complete point error.')
panel(1496,330,'4  Unique minima after the actual shift  |  HF13–HF14',
 'E(w)=K₃x³+K₂x²+K₁x+K₀.\n'
 'K-coefficient bounds: ≥0, ≥2, exactly 4, ≥7.\n'
 'Term bounds: 33/4, 15/2, 27/4, 7.\n'
 'Only K₁x has least value:  v(E(w))=27/4.\n'
 'Trace terms a₁x, a₃, 2w₀, 2σ: 23/4, 5, ≥11/2, ≥6.\n'
 'Only a₃ is least: v(T(w))=5, where T(w)=A+2w.\n'
 'In F: error 27, trace 20; no leading term is discarded.')
panel(1134,340,'5  The entire point ring, not an integral suborder  |  HF15–HF16',
 'η=(y−kx²/π³−σ)/τ¹³.\n'
 'Its quadratic has constant valuation 1 and trace valuation 7.\n'
 'It is Eisenstein: [L:F]=2, ramification 2, residue degree 1.\n'
 'The two summand parities prove B₈=B₄[η] in full.\n'
 'Exact relative point index: 13, from the generator determinant.\n'
 'Upper derivative terms: 8e+1≥25 and 14.\n'
 'Relative different=14;  D₈=2D₄+14=34;  i₈=2i₄+13=43.')
panel(762,314,'6  Exact conductor and Euler identity  |  HF16–HF17',
 'ε₄=3;  ε₈=7;  ν=0.  The fields each give one inertia orbit.\n'
 'The even orbit forces a nontrivial wild action.\n'
 'Earlier quaternion/kernel proofs give zero cohomology invariants.\n'
 'Swan δ=2d−i₈+i₄−2=40−43+15−2=10.\n'
 'Conductor f=2+δ=12.  NF24: i₄+13=28=d+M−1.\n'
 'Euler/discriminant: M−1+f=9−1+12=20=d.', '#edf7f3')
text(36,406,'Exercise, six points  |  Section 6.0AC.6',15,blue,'bold')
text(36,366,'If J₀ has value 6, the uncorrected F-error has value 24.\n'
 'Denominator 12 makes its constant a unit; it does not prove fullness.\n'
 'The retained scalar correction gives error 27 and the full index 13.',12)
text(36,245,'Sources and boundaries',14,blue,'bold')
text(36,207,'Prerequisite results: Lesson 08, 6.0E/H/I.8–I.9/K.1–K.6/P.3/P.5;\nearlier programme local-field proofs, 0A–0G. Source:\nJ. S. Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56, pp.129–130.\nhttps://www.jmilne.org/math/CourseNotes/ANT.pdf\nScope is exactly HF1. Other II* parameters are outside this diagram.\nCoordinates specify the diagram layout.',10.5)
fig.savefig(Path(__file__).resolve().parents[1] / 'assets/higher-ramification-third-five-II-star-proof-map.png',dpi=100,facecolor='white')
plt.close(fig)
