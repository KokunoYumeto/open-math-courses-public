"""Reproducible exact HV proof map; panel coordinates are schematic."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent.parent
asset_root=root/'assets'
W=900
heights=[430,450,740,490,610,450,550,650]
H=sum(heights)+215
fig=plt.figure(figsize=(W/100,H/100),dpi=100)
ax=fig.add_axes([0,0,1,1])
ax.set_xlim(0,W);ax.set_ylim(H,0);ax.axis('off')
fig.patch.set_facecolor('#f6f4ee')
labels=[]
def text(x,y,s,size=15,bold=False,color='#173448'):
    item=ax.text(x,y,s,fontsize=size,fontfamily='DejaVu Sans',
                 fontweight='bold' if bold else 'normal',va='top',ha='left',color=color)
    labels.append(item)
    return item
text(32,24,'A weaker fourth-invariant bound',27,True)
text(32,66,'Original integral models → full rings → exact indices and conductors',15)
text(32,91,'K / Q₂ finite; v(π)=1; e=v(2); κ is the receiving invariant parameter.',14)
cursor=130
def panel(number,title,locator,lines):
    global cursor
    top=cursor
    height=heights[number-1]
    ax.add_patch(FancyBboxPatch((24,top),852,height-15,boxstyle='round,pad=0,rounding_size=12',
                              linewidth=1,edgecolor='#9bb1bc',facecolor='#ffffff'))
    text(43,top+16,f'{number}. {title}',19,True)
    text(43,top+48,locator,12,color='#456b73')
    yy=top+79
    for line in lines:
        if isinstance(line,tuple):
            value,size=line
        else:value,size=line,15
        text(43,yy,value,size)
        yy+=31 if size>=15 else 28
    cursor+=height
    return top

panel(1,'The original equation and its integral inverse','HV1–HV7; earlier resolution / minimality / Euler providers',[
    'y² + a₁xy + a₃y = x³ + a₂x² + a₄x + a₆',
    'v(b₂)=2e+κ,  v(b₆)=2e+5,  v(b₄)>B=e+2μ',
    'κ≥2 even;  3κ<2e+5;  t=2e+κ+5;  μ=t/4;  n=2e−3κ+5',
    's=a₁/2 ∈ R,  r=a₃/2 ∈ R;  Y=y+sx+r;  y=Y−sx−r',
    'A₂=b₂/4,  A₄=b₄/2,  A₆=b₆/4',
    'Y²=x³+A₂x²+A₄x+A₆;  v(A₂)=κ,  v(A₄)>2μ,  v(A₆)=5',
    'R[x,y]=R[x,Y];  C[y]=C[Y];  dx/(2y+a₁x+a₃)=dx/(2Y)',
    'Both projective maps fix [0:1:0] and have integral determinant 1.',
    '1≤n≤2e−1 odd;  μ=κ+n/4;  μ≥9/4;  receiving M=9.'
])
panel(2,'Every changed minimum is strict','HV8–HV9; absent fourth terms have value infinity',[
    '4b₈=b₂b₆−b₄²;  2v(b₄)>4e+κ+5;  v(b₈)=t',
    'Δ=−b₂²b₈−8b₄³−27b₆²+9b₂b₄b₆;  d=4e+10',
    'Competitor gaps: 2e+3κ−5;  >2e+6μ−10;  >e+κ+2μ−5',
    'c₄=b₂²−24b₄;  fourth-term gap >n/2;  v(c₄)=4e+2κ',
    'q(X)=X⁴+(b₂/3)X³+b₄X²+b₆X+b₈/3',
    'Middle endpoint margins: 2e+κ−μ>0,  v(b₄)−2μ>e,  n/4>0',
    'Every root has v(x)=μ;  odd t gives degree / ramification / residue = 4 / 4 / 1.',
    'v(j)=8e+6κ−10≥10;  original quartic discriminant = −Δ²/27.'
])
panel(3,'Both entire quartic bases and all coefficients','HV10–HV13; vF=4v; F=K(x); every power class is distinct',[
    ('mⱼ=⌊jt/4⌋; C=R ⊕ R·x/π^(m₁) ⊕ R·x²/π^(m₂) ⊕ R·x³/π^(m₃)',14),
    'i₄=Σmⱼ=3(t−1)/2;  D₄=2d−2i₄=n+3',
    't=4a+1:  θ=x/πᵃ;  floors (a,2a,3a)',
    't=4a+3:  θ=πᵃ⁺¹/x;  floors (a,2a+1,3a+2)',
    'vF(θ)=1;  C=R[θ];  θ⁴+γ₃θ³+γ₂θ²+γ₁θ+γ₀=0',
    'Direct case (t=4a+1):',
    ('(γ₃,γ₂,γ₁,γ₀)=(b₂/(3πᵃ), b₄/π²ᵃ, b₆/π³ᵃ, b₈/(3π⁴ᵃ))',14),
    'Reciprocal case (t=4a+3):',
    ('(γ₃,γ₂,γ₁,γ₀)=(3b₆πᵃ⁺¹/b₈, 3b₄π²ᵃ⁺²/b₈,',14),
    ('                         b₂π³ᵃ⁺³/b₈, 3π⁴ᵃ⁺⁴/b₈)',14),
    'Constant term value 4;  sixth-invariant odd error value n+4.',
    'Other odd error gap: 4e+6κ−10>0',
    'Quadratic error value: 4v(b₄)−2t+4>4e+4>n+4',
    'u=−γ₀/π ∈ R×;  θ⁴=πu+ε;  vF(ε)=n+4',
    'ε=−γ₃θ³−γ₂θ²−γ₁θ; no coefficient has been discarded.'
])
panel(4,'Finite square precision for every base unit','HV14–HV15; no ramified square root of u₀ is introduced',[
    'J=⌊n/4⌋;  S₋₁=0;  Sⱼ=Σᵢ₌₀ʲ cᵢ²(πu)ⁱ',
    'Choose residues: c̄ⱼ²ūʲ = residue((u₀−Sⱼ₋₁)/πʲ)',
    'Finite residue-field squaring is bijective;  u₀−Sⱼ ∈ πʲ⁺¹R.',
    'w=Σⱼ₌₀ᴶ cⱼθ²ʲ is a unit.',
    'θ⁴ᵐ−(πu)ᵐ = ε Σᵢ₌₀ᵐ⁻¹ θ⁴⁽ᵐ⁻¹⁻ⁱ⁾(πu)ⁱ',
    'Diagonal error value ≥n+4m;  each cross error value ≥4e+2>n.',
    'Final base error value ≥4(J+1)>n.',
    'Therefore vF(w²−u₀)≥n+1, including the empty-sum case J=0.',
    'All induction lengths are allowed; later coefficients may be zero.'
])
panel(5,'Original point and its whole quadratic ring','HV16–HV19; L=F(η); vL=2vF; residue degree one',[
    'U=x³+(b₂/4)x²+(b₄/2)x+b₆/4;  Y²=U',
    'N=3x²+(b₂/2)x+b₄/2;  B₀=3x+b₂/4',
    'N²−4UB₀=−3q(x)=0;  v(N)=2μ;  v(U)=5',
    'u₀=b₂/(4π^κ) is a base unit.',
    'B*=B₀/π^κ=u₀+3x/π^κ;  vF(3x/π^κ)=n',
    'ζ=N/(2π^(κ/2)Y);  ζ²=B*;  D=N/(2π^(κ/2)B*);  vF(D)=10',
    'j=(n−1)/2;  η=(ζ−w)/θʲ;  y=Dζ−sx−r',
    'η²+aη+b=0;  a=2w/θʲ;  b=(w²−B*)/θ²ʲ',
    'vF(a)=4e−j>0;  vF(b)=1;  entire ring ℬ=C[η]',
    'Derivative values: 8e+1 and 8e−n+1; exact gap n.',
    'y=(Dw−sx−r)+Dθʲη;  original basis matrix:',
    '[ 1   Dw−sx−r ]',
    '[ 0      Dθʲ   ]    ℓ=vF(Dθʲ)=10+j=(n+19)/2',
    'D₈/₄=8e−n+1; no original-coordinate shift is omitted.'
])
panel(6,'All eight original columns, then the conductor','HV20–HV21; both full rings precede the Swan identity',[
    ('ωⱼ=xʲ/π^(mⱼ); H=diag(1,π^(m₁),π^(m₂),π^(m₃)); α=Dw−sx−r',14),
    'Whole basis (ω₀,ω₁,ω₂,ω₃,ηω₀,ηω₁,ηω₂,ηω₃); ω₀=1',
    'Original basis (1,x,x²,x³,y,xy,x²y,x³y)',
    'ℳ₈=[ H   MαH ;  0   M(Dθʲ)H ];  Mz=multiplication by z on C',
    'det ℳ₈=π^(2i₄) NormF/K(Dθʲ);  norm value = ℓ, retaining its unit',
    'D₈=2D₄+D₈/₄=8e+n+7;  i₈=2i₄+ℓ=7e+3κ/2+24',
    '6d−2i₈=D₈;  δ=(D₈−D₄−4)/2=4e;  f=4e+2',
    'ε₄=3, ε₈=7, ν=0; central wild −I gives zero inertia invariants.',
    'i₄+ℓ=d+8;  M−1+f=d with M=9.'
])
panel(7,'Every overorder containing the full quartic ring','HV22–HV23; all nonzero-trace and quartic derivative factors retained',[
    'C[y]=C+θˡCη;  Qs=C+θˢCη;  0≤s≤ℓ',
    'ξs=θˢη;  ξs²+aθˢξs+bθ²ˢ=0',
    'lengthR(ℬ/Qs)=s;  disc exponent=D₈+2s;  original index=i₈−s',
    'Order conductor (Qs:ℬ)=θˢℬ;  absolute length weight is 1.',
    'd₂=2η+a;  d₄=4θ³+3γ₃θ²+2γ₂θ+γ₁',
    'Relative dual = d₂⁻¹(θ⁻ˢC+Cη)',
    'Absolute dual = (d₄d₂)⁻¹(θ⁻ˢC+Cη)',
    'Conjugation η ↦ −a−η;  derivative ↦ −d₂',
    'Tr(1/d₂)=0,  Tr(η/d₂)=1,  Tr(η²/d₂)=−a',
    'Dual pairing [ 0  1 ; 1  −aθˢ ] has determinant −1.',
    'Conjugation preserves all Qs. Orders missing the full C are not classified.'
])
top=panel(8,'Precisely added integer levels and actual families','HV24–HV27; exact rational valuation scale below',[
    'Old β=2e+(μ+5)/2;  β−B=n/8',
    'Added m: B<m≤β;  count=⌊(n+4)/8⌋; none for n=1,3.',
    'Every level: Y²=x³+π^κ x²+π^(m−e)x+π⁵.',
    'e=10, κ=2:  μ=27/4, n=19, B=47/2, β=207/8.'
])
axis_y=top+237
def axis_x(value):return 66+float((Fraction(value)-23)/3)*748
ax.plot([axis_x(23),axis_x(26)],[axis_y,axis_y],color='#526a77',linewidth=1.5)
ax.plot([axis_x(Fraction(47,2)),axis_x(Fraction(207,8))],[axis_y,axis_y],color='#72b5a1',linewidth=6,alpha=.5)
for value,label in [(Fraction(47,2),'B = 47/2'),(Fraction(24),'m = 24'),(Fraction(25),'m = 25'),(Fraction(207,8),'β = 207/8')]:
    px=axis_x(value)
    ax.plot([px,px],[axis_y-6,axis_y+8],color='#173448',linewidth=1)
    if value.denominator==1:ax.plot(px,axis_y,'o',color='#177252',markersize=7)
    text(px-33,axis_y+20,label,12)
ax.plot(axis_x(Fraction(47,2)),axis_y,'o',color='#177252',markerfacecolor='white',markersize=7)
ax.plot(axis_x(Fraction(207,8)),axis_y,'o',color='#177252',markersize=7)
for yy,line in [
    (top+315,'At m=24: a₄=π¹⁴; b₈=4π⁷−π²⁸, with term values 27 and 28.'),
    (top+350,'(d,i₄,D₄,ℓ,D₈/₄,D₈,i₈,δ,f)=(50,39,22,19,62,106,97,40,42)'),
    (top+385,'Five residue choices c₀,…,c₄; j=9; twenty overorders Q₀,…,Q₁₉.'),
    (top+425,'Infinite added family: κ=2, e=4q+3, n=8q+5, m=2e+4, q≥0'),
    (top+460,'Its added-level count is q+1; its nine exact entries are:'),
    (top+495,'(16q+22, 12q+18, 8q+8, 4q+12, 24q+20,'),
    (top+530,' 40q+36, 28q+48, 16q+12, 16q+14).'),
    (top+570,'Twelve-point exercise and all four full solution parts accompany HV1–HV27.')
]:
    text(43,yy,line,14)
text(32,H-68,'Human source: J. S. Milne, free Algebraic Number Theory, 7.55 / 7.56.',12)
text(32,H-42,'All specialized claims have written programme proofs. Panel coordinates are schematic.',12)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
boxes=[]
for item in labels:
    box=item.get_window_extent(renderer)
    assert box.x0>=0 and box.x1<=W and box.y0>=0 and box.y1<=H,(item.get_text(),list(box.bounds))
    boxes.append({'label':item.get_text(),'bbox':list(map(float,box.bounds))})
for i,a in enumerate(boxes):
    ax0,ay0,aw,ah=a['bbox']
    for b in boxes[i+1:]:
        bx0,by0,bw,bh=b['bbox']
        assert min(ax0+aw,bx0+bw)-max(ax0,bx0)<=0 or min(ay0+ah,by0+bh)-max(ay0,by0)<=0,(a['label'],b['label'])
png=asset_root/'weaker-fourth-invariant-even-second-proof-map.png'
fig.savefig(png,dpi=100,facecolor=fig.get_facecolor(),metadata={'Title':'Weaker fourth-invariant bound: exact original maps and full normalization'})
plt.close(fig)
record={'dimensions':[W,H],'panels':8,'text_labels':len(boxes),'all_labels_in_bounds':True,
        'all_text_boxes_nonoverlapping':True,'axis_exact_values':['47/2','24','25','207/8'],
        'png_sha256':hashlib.sha256(png.read_bytes()).hexdigest(),'labels':boxes,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'actual_render_inspection_pending':True,'layout_positions_are_schematic':True}
print(json.dumps(record))
