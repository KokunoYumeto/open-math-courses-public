"""Original CC0 diagram and exact finite algebra for ENC.1–ENC.20."""
from pathlib import Path
from fractions import Fraction as Q
from PIL import Image, ImageDraw, ImageFont
import argparse, base64, html, io, json, math

HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser()
p.add_argument("--resources",type=Path,default=HERE.parent/"labelled-geometric-kernel")
p.add_argument("--output-dir",type=Path,default=HERE/"generated")
opts=p.parse_args()
opts.output_dir.mkdir(parents=True,exist_ok=True)
font=(opts.resources/"fonts/DejaVuSans.ttf").read_bytes()
notice=(opts.resources/"FONT-NOTICE.txt").read_text(encoding="utf-8")
W,H=1800,1140
im=Image.new("RGB",(W,H),"#f7fafc"); d=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<metadata>'+html.escape(notice)+'</metadata>',
 '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+base64.b64encode(font).decode()+
 ')}text{font-family:LocalSans}</style>',
 f'<rect width="{W}" height="{H}" fill="#f7fafc"/>']
fonts={}; overflow=[]
def text(x,y,s,size=24,col="#17334d"):
    if size not in fonts:
        fonts[size]=ImageFont.truetype(io.BytesIO(font),size,layout_engine=ImageFont.Layout.BASIC)
    box=d.textbbox((x,y),s,font=fonts[size],anchor="lt")
    if box[0]<0 or box[1]<0 or box[2]>W-12 or box[3]>H-12: overflow.append(s)
    d.text((x,y),s,font=fonts[size],fill=col,anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')
def rect(x,y,w,h,col="#ffffff",edge="#c7d7e2"):
    d.rectangle((x,y,x+w,y+h),fill=col,outline=edge,width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" stroke="{edge}" stroke-width="2"/>')
def line(points,col="#4c6c83",width=3):
    d.line(points,fill=col,width=width)
    svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')
def arrow(x,y):
    line([(x,y),(x,y+28)])
    pts=[(x,y+28),(x-8,y+16),(x+8,y+16)]
    d.polygon(pts,fill="#4c6c83")
    svg.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in pts)+'" fill="#4c6c83"/>')
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[Q(0) for _ in range(n)] for _ in range(n)]
def diag(vals): return [[vals[i] if i==j else Q(0) for j in range(len(vals))] for i in range(len(vals))]
def add(a,b): return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def neg(a): return scale(a,-1)
def scale(a,q): return [[q*x for x in row] for row in a]
def mul(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))] for i in range(len(a))]
def comm(a,b): return add(mul(a,b),neg(mul(b,a)))
def blocks(a,b,c,e): return [u+v for u,v in zip(a,b)]+[u+v for u,v in zip(c,e)]
def corner(a,i,j,n=4): return [row[j:j+n] for row in a[i:i+n]]
def transpose(a): return [list(v) for v in zip(*a)]
def det(a):
    a=[row[:] for row in a]; val=Q(1)
    for i in range(len(a)):
        j=next((j for j in range(i,len(a)) if a[j][i]),None)
        if j is None: return Q(0)
        if j!=i: a[i],a[j]=a[j],a[i];val=-val
        q=a[i][i];val*=q
        for j in range(i+1,len(a)):
            t=a[j][i]/q
            a[j]=[x-t*y for x,y in zip(a[j],a[i])]
    return val

I4,I8=eye(4),eye(8); Z4,Z8=zero(4),zero(8)
sx=[[Q(0),Q(1)],[Q(1),Q(0)]]
f=scale(blocks(sx,zero(2),zero(2),sx),Q(3,5))
c=scale(I4,Q(4,5))
F=blocks(f,c,c,neg(f))
gamma=diag([Q(1),Q(-1),Q(1),Q(-1)])
grading=blocks(gamma,Z4,Z4,neg(gamma))
P=blocks(I4,Z4,Z4,Z4); R=add(I8,neg(P))
U4=blocks(zero(2),eye(2),eye(2),zero(2)); U=blocks(U4,Z4,Z4,U4)
assert mul(F,F)==I8 and transpose(F)==F and add(mul(grading,F),mul(F,grading))==Z8
assert comm(U,F)==Z8 and comm(U,P)==Z8
tests=[]
for x in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:
    hs=[(2+x)/32,(3-x)/32,(4+x)/32,(5-x)/32]
    rs=diag([1/h for h in hs])
    ref=blocks(rs,Z4,Z4,rs)
    C_F=comm(ref,F); B_F=scale(mul(F,C_F),Q(1,2))
    r=scale(add(ref,mul(mul(F,ref),F)),Q(1,2))
    assert r==add(ref,B_F) and transpose(r)==r and comm(r,F)==Z8
    assert comm(ref,P)==Z8 and comm(r,P)==comm(B_F,P)
    r0=corner(r,0,0);T0=mul(c,corner(r,4,0));S0=corner(mul(F,r),0,0)
    assert r0==add(rs,corner(B_F,0,0))
    assert S0==add(mul(f,r0),T0) and transpose(S0)==S0
    assert comm(r0,f)==add(neg(mul(corner(r,0,4),c)),mul(c,corner(r,4,0)))
    Aref=add(mul(mul(U,ref),U),neg(ref))
    A=add(mul(mul(U,r),U),neg(r))
    assert A==scale(add(Aref,mul(mul(F,Aref),F)),Q(1,2))
    assert comm(S0,U4)==neg(mul(corner(mul(mul(mul(P,F),A),P),0,0),U4))
    for k in range(1,9):
        assert det([row[:k] for row in add(r,neg(I8))[:k]])>0
    assert all(h>=Q(1,32) for h in hs)
    tests.append(dict(x=str(x),positive_seed_entries=[str(v) for v in hs],
        exact_phase_commutation=True,exact_bounded_perturbation=True,
        exact_reference_projection_commutation=True,exact_essential_reference_perturbation=True,
        exact_compression_formula=True,exact_reference_commutator=True,
        exact_full_arrow_error=True,positive_regulator_minus_identity=True,
        averaged_projection_commutator_zero=(comm(r,P)==Z8),
        essential_operator=[[str(v) for v in row] for row in S0]))
units=[]
for i in range(2):
    for j in range(2):
        a=[[Q(u==i and v==j) for v in range(2)] for u in range(2)]
        units.append((i,j,blocks(a,zero(2),zero(2),a)))
products=[]
for i,j,a in units:
    for k,l,b in units:
        expected=next(v for u,w,v in units if u==i and w==l) if j==k else Z4
        assert mul(a,b)==expected
        products.append(dict(left=[i,j],right=[k,l],exact_product=True))
assert len(products)==16
at_zero=next(t for t in tests if t["x"]=="0")
assert at_zero["essential_operator"]==[[str(v) for v in row] for row in
    blocks(scale(sx,Q(8)),zero(2),zero(2),scale(sx,Q(108,25)))]

text(42,34,"The actual essential inverse: one normal-compatible operator graph core",38)
text(42,94,"ENC.1–ENC.23  |  nondegenerate B source  |  original class d_X  |  full arrow graph domains",25)
rect(40,160,548,560);rect(608,160,582,560);rect(1210,160,550,560)
text(61,184,"1. Smooth diagonal cutoffs",28)
text(61,230,"h*(g,n) > 0 on each coordinate",23)
text(61,270,"Positive floor on finite compact supports",21)
text(61,310,"v_m = finite convex sums of χ_k(h*)",22)
px,py,pw,ph=90,400,435,160
line([(px,py),(px,py+ph),(px+pw,py+ph)],width=2)
def smooth(t):
    if t<=0:return 0
    if t>=1:return 1
    a=math.exp(-1/t);b=math.exp(-1/(1-t));return a/(a+b)
for k,col in [(1,"#c05621"),(2,"#2b6cb0"),(3,"#2f855a")]:
    a=2**(-2*k-2);b=2**(-2*k-1)
    pts=[]
    for j in range(401):
        lam=j*.16/400
        pts.append((px+pw*j/400,py+ph*(1-smooth((lam-a)/(b-a)))))
    line(pts,col,3)
    text(86+145*(k-1),578,"χ"+str(k),20,col)
text(52,548,"0",18);text(496,548,"0.16",18)
text(61,618,"Each normal derivative is bounded.",21)
text(61,662,"No uniform bound along the sequence.",21)
text(628,184,"2. Average after core construction",26)
rect(637,233,523,79,"#edf5ff")
text(654,252,"r* = 1 + Σ(1 − v_n)",25)
text(654,288,"Core E = span(v_m C_reg) ⊂ Dom ∇",21)
arrow(898,322)
rect(637,366,523,89,"#eaf7ed")
text(654,384,"r = (r* + F r* F)/2 = r* + B_F",23)
text(654,420,"B_F = ½F[r*,F] is bounded compact",21)
arrow(898,467)
rect(637,511,523,100,"#fff3e5")
text(654,530,"Same full reference domain and core",22)
text(654,570,"[r,F] = 0 exactly; [r,P] is compact",22)
text(631,644,"P is parallel for the copied connection.",21)
text(631,682,"No normal derivative of F is assumed.",21)
text(1230,184,"3. Close the essential compression",25)
text(1230,246,"S_N = closure of P F r P",26)
text(1230,298,"B acts nondegenerately on M.",23)
text(1230,347,"P E is a core for the full S_N graph",22)
text(1230,390,"and lies in the completed normal domain.",21)
rect(1230,443,510,126,"#edf5ff")
text(1245,461,"Dom S_N ∩ Dom ∇ is",26)
text(1245,507,"dense, complete and arrow invariant.",23)
text(1230,604,"Normal-preserving w_m approximate",21)
text(1230,640,"the full S_N graph:  [S_N,w_m] → 0.",21)
text(1230,680,"Joint limit still needs (D_N w_m) ξ → 0.",20)
rect(40,746,1720,284)
text(61,770,"Exact finite calibration: opposite-graded 8 × 8 normalization, essential 4 × 4 compression",27)
text(61,819,"f = (3/5) diag(σ_x, σ_x),   C = (4/5) I_4,   Φ(b) = diag(b,b),   P = diag(I_4,0)",25)
text(61,863,"h*(x) = diag(2+x, 3−x, 4+x, 5−x)/32,    −1 ≤ x ≤ 1.    Arrow U swaps the two rows.",24)
text(61,909,"At x = 0:   S_0 = diag(8 σ_x, (108/25) σ_x).    The essential source identity is I_4.",24)
text(61,954,"5 rational samples: exact phase, regulator, compression and full arrow-error formulas; 16 source products.",23)
text(61,995,"Finite matrices illustrate the algebra; they do not prove the infinite inverse class.",21)
text(42,1054,"Still required: a joint graph core, normal-source and mixed estimates, the physical sum and original Bott +1 pairing.",23)
text(42,1096,"The proof keeps the original R balance, inverse coefficient, grading and final right Clifford order.",22)
assert not overflow,overflow
svg.append("</svg>")
im.save(opts.output_dir/"essential-normal-core.png",optimize=False)
(opts.output_dir/"essential-normal-core.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
checks=dict(schema="essential-normal-core-finite-calibration/v1",
    exact_normalization_and_grading=True,exact_invariant_phase=True,
    normalized_dimension=8,essential_dimension=4,essential_source_identity_rank=4,
    essential_source_nondegenerate=True,source_products=products,symmetrization_tests=tests,
    all_fraction_checks=True,text_canvas_overflows=overflow,
    finite_model_proves_original_inverse=False,finite_model_proves_physical_sum=False,
    proof_scope="ENC.1–20 retain the actual B-source inverse class, source/arrow controls and a dense normal-compatible full operator graph core. A full joint graph core, normal source/operator resolvent controls and original physical sum/Bott pairing remain unproved.")
(opts.output_dir/"ESSENTIAL-NORMAL-CORE-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(exact_symmetrization_samples=len(tests),exact_source_products=len(products),essential_source_identity_rank=4,overflows=len(overflow))))
