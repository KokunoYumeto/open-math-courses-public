"""Exact HW proof map. Layout is schematic; the two valuation axes are exact."""
from pathlib import Path
from fractions import Fraction
import argparse
import hashlib
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent.parent
asset=root/'assets/weaker-fourth-invariant-odd-second-proof-map.png'
heights=[380,380,530,590,420,450,590,650]
W=900
H=sum(heights)+215
fig=plt.figure(figsize=(W/100,H/100),dpi=100)
ax=fig.add_axes([0,0,1,1])
ax.set_xlim(0,W);ax.set_ylim(H,0);ax.axis('off')
fig.patch.set_facecolor('#f6f4ee')
labels=[]
def text(x,y,s,size=14,bold=False,color='#173448'):
    item=ax.text(x,y,s,fontsize=size,fontfamily='DejaVu Sans',
                 fontweight='bold' if bold else 'normal',va='top',ha='left',color=color)
    labels.append(item)
    return item
text(32,24,'The weaker bound for an odd second invariant',23,True)
text(32,61,'Original model → full factor rings → original indices → conductor',15)
text(32,91,'K / Q₂ finite; v(π)=1; k comes from v(b₂), not from the original a₂.',14)
cursor=130
def panel(number,title,locator,lines):
    global cursor
    top=cursor
    height=heights[number-1]
    ax.add_patch(FancyBboxPatch((24,top),852,height-15,
                 boxstyle='round,pad=0,rounding_size=12',linewidth=1,
                 edgecolor='#9bb1bc',facecolor='white'))
    text(43,top+16,f'{number}. {title}',18,True)
    text(43,top+48,locator,12,color='#456b73')
    yy=top+79
    for line in lines:
        value,size=line if isinstance(line,tuple) else (line,14)
        text(43,yy,value,size)
        yy+=30
    cursor+=height
    return top

panel(1,'Both integral model maps and their actual orders','HW1–HW3; earlier resolution, minimality and Euler proofs',[
    'k≥3 odd; n=2e−3k+5≥2 even; μ=k+n/4; t=4μ',
    'v(b₂)=2e+k; v(b₆)=2e+5; v(b₄)>B=e+2μ; b₄=0 allowed',
    's=a₁/2, r=a₃/2 ∈ R; Y=y+sx+r; y=Y−sx−r',
    'Y²=x³+A₂x²+A₄x+A₆; A₂=b₂/4, A₄=b₄/2, A₆=b₆/4',
    'Receiving values: k, >2μ, 5; first and third coefficients zero.',
    'Projective maps have determinant 1, fix infinity, and are inverse.',
    'R[x,y]=R[x,Y]; dx/(2y+a₁x+a₃)=dx/(2Y)',
    'e≥3, μ≥7/2; receiving type II*, M=9; original a₂ may be a unit.'
])
panel(2,'The original quartic and point maps retain every term','HW4–HW5; d=4e+10; v(c₄)=4e+2k; v(j)=8e+6k−10',[
    '4b₈=b₂b₆−b₄²; v(b₈)=t; every competing minimum is strict.',
    'q(X)=X⁴+(b₂/3)X³+b₄X²+b₆X+b₈/3; all roots have v(x)=μ.',
    'U=x³+(b₂/4)x²+(b₄/2)x+b₆/4; Y=y+(a₁x+a₃)/2',
    'N=3x²+(b₂/2)x+b₄/2; B₀=3x+b₂/4; N²−4UB₀=−3q(x)',
    's₀=π^((k−1)/2); u₀=b₂/(4πᵏ); B=πu₀+3π^(1−k)x',
    'ζ=N/(2s₀Y); ζ²=B; D=N/(2s₀B); y=Dζ−(a₁x+a₃)/2',
    'v(N)=2μ; v(U)=5; v(B)=1; v(D)=2; the half-shift is integral.',
    'D²B=U and ζ⁻¹=ζ/B give the inverse in the same original field.'
])
panel(3,'Every actual full quartic factor and both scaled cases','HW6–HW9; Cⱼ=Rⱼ[αⱼ]; vⱼ=Eⱼv; ΣEⱼfⱼ=4',[
    'm=⌊μ⌋=k+r; Z=x/πᵐ; Q=Z⁴+C₃Z³+C₂Z²+C₁Z+C₀',
    '(C₃,C₂,C₁,C₀)=(b₂/(3πᵐ),b₄/π²ᵐ,b₆/π³ᵐ,b₈/(3π⁴ᵐ))',
    '                         n=4r, r≥1             n=4r+2, r≥0',
    'v(Z), v(C₃)             0, 2e−r                1/2, 2e−r',
    'v(C₂), v(C₁), v(C₀)     >e, r, 0               >e+1, r+2, 2',
    'v(Q′), v(disc Q)        r, 4r                  r+2, 4r+8',
    'Nonmaximal trace dual gives dⱼ≤vⱼ(Q′(Zⱼ)); odd Eⱼ: dⱼ=Eⱼ−1.',
    'Even Eⱼ:               Eⱼ=2                  Eⱼ=4',
    'n=4r                   dⱼ≤2r                 dⱼ≤4r',
    'n=4r+2, r≥1            dⱼ≤2r                 dⱼ≤4r+2',
    'n=2                    cannot occur          dⱼ=4',
    'Even dⱼ; dⱼ≥Eⱼ; dⱼ+1<Eⱼe; Eⱼ(1+μ−k)−1>dⱼ.',
    'Mixed lattice (1,Z,W,ZW), W=(Z²−πc)/(πZ), has determinant −c/(πC₀).',
    'Split quadratics retain every other-factor derivative contribution.'
])
top=panel(4,'The full series and every maximizing square','HW10–HW11; complete earlier series proof: Section 6.0AM.4',[
    'F(α)=π; F=Aᴱ times a unit; vC(F′(α))=dC; T=vC(2)=Ee',
    'H(A)=F(A)u₀(F(A))+3F(A)^(1−k)X(A); H(α)=B',
    'H′=(u₀+πu₀′)F′ + 3π^(1−k)X′ + 3(1−k)π^(−k)xF′',
    'First derivative term uniquely least; vC(H′)=dC; vC(B)=E.',
    'Even E: maximum square error dC+1; all maximizers w+α^(dC/2+1)C.',
    'Odd E: maximum square error E; all maximizers α^((E+1)/2)C.',
    'Finite residue-square construction retains the odd unit at degree dC+1.',
    'Exact lemma illustration: E=4, dC=6, T=20; no curve is specified.'
])
axis_y=top+399
def sx(t):return 65+float(Fraction(t)/22)*750
ax.plot([sx(0),sx(22)],[axis_y,axis_y],color='#526a77',linewidth=1.5)
for value,label in [(0,'0'),(4,'E=4'),(6,'dC=6'),(7,'error=7'),(20,'T=20')]:
    x0=sx(value)
    ax.plot([x0,x0],[axis_y-5,axis_y+5],color='#526a77')
    if value==6:text(x0-25,axis_y+39,label,12)
    elif value==7:text(x0-5,axis_y+13,label,12)
    else:text(x0-14,axis_y+13,label,12)
ax.scatter([sx(7)],[axis_y],s=70,color='#b24a28',zorder=3)
text(43,top+493,'If vC(u)≤3, u² gives error ≤6; if vC(u)≥4, the old error 7 persists.',13)
text(43,top+525,'The exact cross term 2wu has higher value in both regimes.',13)

panel(5,'Every point polynomial gives the entire original ring','HW12; dⱼ even in every factor; aⱼ=dⱼ/2',[
    'Even Eⱼ: ηⱼ=(ζⱼ−wⱼ)/αⱼ^aⱼ; odd Eⱼ: wⱼ=0, ηⱼ=ζⱼ/αⱼ^aⱼ.',
    'ηⱼ²+Aⱼηⱼ+cⱼ=0; Aⱼ=2wⱼ/αⱼ^aⱼ; cⱼ=(wⱼ²−B)/αⱼ^(2aⱼ)',
    'vⱼ(cⱼ)=1; Aⱼ∈αⱼCⱼ (or Aⱼ=0); full ring Bⱼ=Cⱼ[ηⱼ].',
    'Even derivative values: 2Eⱼe+1 and 2Eⱼe+Eⱼ−dⱼ.',
    'Odd derivative: 2ηⱼ, value 2Eⱼe+1=2Eⱼe+Eⱼ−dⱼ.',
    'y=(Dwⱼ−A/2)+Dαⱼ^aⱼηⱼ; Lⱼ=vⱼ(Dαⱼ^aⱼ)=2Eⱼ+dⱼ/2.',
    'The integral original shift remains, even when its value is zero.',
    'Changing a maximizing approximant translates ηⱼ by an element of αⱼCⱼ.',
    'Both inverse translations preserve the full ring and the original y-order.'
])
panel(6,'All eight original columns precede the conductor','HW13–HW15; fⱼ are residue weights, not ramification weights',[
    'H = original quartic power basis in an actual full B₄ basis.',
    'c=(Dwⱼ−A/2)ⱼ; g=(Dαⱼ^aⱼ)ⱼ; Mz = multiplication by z on B₄.',
    'Original eight columns:  ℋ=[ H  McH ; 0  MgH ]',
    'Inverse: [ H⁻¹  −H⁻¹McMg⁻¹ ; 0  H⁻¹Mg⁻¹ ]',
    'det ℋ=(det H)² ∏NormFⱼ/K(Dαⱼ^aⱼ), retaining every norm unit.',
    'D₄=Σfⱼdⱼ; i₄=d−D₄/2; ℓ=ΣfⱼLⱼ=8+D₄/2.',
    'i₄+ℓ=d+8; i₈=2i₄+ℓ; D₈=D₄+8e+4=6d−2i₈.',
    'All point quadratics ramify; ν=0; ε₈−ε₄=4.',
    'Earlier central −1 proof gives tame conductor 2; δ=4e; f=4e+2.',
    'Both full rings and both original indices were established first.'
])
panel(7,'Full-base orders, complete duals and raw conductors','HW16–HW19; relative hⱼ=2ηⱼ+Aⱼ; actual base different δCⱼ',[
    'Oⱼ,s=Cⱼ ⊕ αⱼˢCⱼηⱼ; 0≤s≤Lⱼ; every full-base order is ∏Oⱼ,sⱼ.',
    'Number = ∏(Lⱼ+1); defect = Σfⱼsⱼ; original index = i₈−Σfⱼsⱼ.',
    'Discriminant exponent D₈+2Σfⱼsⱼ; (Oⱼ,s:Bⱼ)=αⱼˢBⱼ.',
    'Tr(1/hⱼ)=0; Tr(ηⱼ/hⱼ)=1; Tr(ηⱼ²/hⱼ)=−Aⱼ.',
    'Absolute dual = δCⱼ⁻¹ hⱼ⁻¹ (αⱼ^(−s)Cⱼ ⊕ Cⱼηⱼ).',
    'Relative pairing [ 0  1 ; 1  −αⱼˢAⱼ ] has determinant −1.',
    'Raw A₄=R[x], raw A₈=R[x,y]=R[x,Y]; q′=4U.',
    'Raw duals: q′⁻¹A₄ and (8UY)⁻¹A₈.',
    'Trace biduality proves (A₄:B₄)=q′B₄∨ and (A₈:B₈)=8UYB₈∨.',
    'Factor ideals: αⱼ^(Eⱼ(2e+5)−dⱼ)Cⱼ;',
    '              ηⱼ^(4Eⱼe+14Eⱼ−dⱼ)Bⱼ.',
    'Weighted exponent sums = 2i₄ and 2i₈.',
    'Derivative generators and their units are retained, including Aⱼ=0.',
    'Orders without the full quartic base are outside this classification.'
])
top=panel(8,'All added integer levels and an original unit witness','HW20–HW23; exact valuation axis below',[
    'Old β=2e+(μ+5)/2 = B+n/8; B=e+2μ is an integer.',
    'Added values v(b₄)=B+j, 1≤j≤⌊n/8⌋; none at n=2,4,6.',
    'Every level: a₁=a₃=0, a₂=uπᵏ, a₄=vπ^(2μ+j), a₆=wπ⁵.',
    'Actual Eisenstein field: πᵉ=2; arbitrary units u,v,w.',
    'k=3, e=4q+2, n=8q, q≥1: exactly q new levels.',
    'Witness π¹⁰=2: a₁=a₃=2, a₂=3π³−1, a₄=π¹⁵−2, a₆=π⁵−1.',
    'e=10, k=3, n=16, μ=7; B=24, β=26; two added levels.'
])
axis_y=top+354
def lx(t):return 85+float((Fraction(t)-23)/4)*710
ax.plot([lx(23),lx(27)],[axis_y,axis_y],color='#526a77',linewidth=1.5)
ax.plot([lx(24),lx(26)],[axis_y,axis_y],color='#16716c',linewidth=5)
for value in (23,24,25,26,27):
    x0=lx(value)
    ax.plot([x0,x0],[axis_y-7,axis_y+7],color='#526a77')
    text(x0-9,axis_y+16,str(value),13)
ax.scatter([lx(24)],[axis_y],s=85,facecolors='white',edgecolors='#16716c',zorder=4)
ax.scatter([lx(25),lx(26)],[axis_y,axis_y],s=70,color='#16716c',zorder=4)
text(lx(24)-25,axis_y-37,'B=24',12)
text(lx(26)-25,axis_y-37,'β=26',12)
text(43,top+423,'The witness has v(b₄)=25; both 25 and 26 satisfy the new bound.',13)
text(43,top+457,'(v(b₂),v(b₄),v(b₆),v(b₈))=(23,25,25,28); d=50; v(c₄)=46.',13)
text(43,top+491,'v(j)=88; Y=y+x+1; receiving (A₂,A₄,A₆)=(3π³,π¹⁵,π⁵).',13)
text(43,top+525,'Original a₂ and A/2=x+1 have value zero; the inverse preserves the order.',13)
text(43,top+559,'No witness factor decomposition is asserted without its actual calculation.',13)

text(32,H-62,'Proof: Lesson 08, Section 6.0AS, HW1–HW23; earlier full series lemma 6.0AM.4.',12)
text(32,H-38,'Local-field source: Milne, free Algebraic Number Theory author notes, as cited in 6.0AM.1.',11)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
boxes=[item.get_window_extent(renderer) for item in labels]
outside=[i for i,b in enumerate(boxes) if b.x0<0 or b.y0<0 or b.x1>W or b.y1>H]
overlaps=[]
for i,b in enumerate(boxes):
    for j in range(i+1,len(boxes)):
        if b.overlaps(boxes[j]): overlaps.append((i,j))
assert not outside,('outside labels',outside)
assert not overlaps,('overlapping labels',overlaps)
asset.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(asset,dpi=100,metadata={'Software':'Matplotlib; original Galois representations proof map.'})
plt.close(fig)
parser=argparse.ArgumentParser()
parser.add_argument('--check-path',type=Path)
args=parser.parse_args()
record={'width':W,'height':H,'panels':8,'labels':len(labels),'labels_outside':outside,
        'overlapping_labels':overlaps,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'render_sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),
        'render':str(asset),'layout_coordinates':'schematic',
        'exact_axes':{'square_lemma':{'E':4,'d_C':6,'T':20,'max_error':7},
                      'added_levels':{'B':24,'beta':26,'added':[25,26],'witness':25}}}
if args.check_path:
    args.check_path.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
