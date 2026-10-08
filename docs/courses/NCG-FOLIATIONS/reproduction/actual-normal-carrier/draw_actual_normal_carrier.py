"""Actual represented normal carrier and graded degenerate augmentation: original CC0 exact diagram."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, base64, html, io, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--output-dir", type=Path, default=HERE / "out")
p.add_argument("--resources", type=Path, default=HERE.parent / "labelled-geometric-kernel")
options = p.parse_args()
options.output_dir.mkdir(parents=True, exist_ok=True)
font = (options.resources / "fonts/DejaVuSans.ttf").read_bytes()
notice = (options.resources / "FONT-NOTICE.txt").read_text(encoding="utf-8")
W, H = 2450, 1780
INK, BLUE, GREEN, RED = "#17283c", "#17638d", "#286d49", "#b64932"
im = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>An actual source-essential normal carrier</title>",
    "<desc>ANC.1 to ANC.17. A nondegenerate regular source representation and exactly degenerate graded augmentation preserve the actual inverse class d_X. Its represented unit-index summand gives an ordinary standard carrier with a completed metric normal connection. Full source and operator derivatives remain unproved.</desc>",
    "<metadata>" + html.escape("Original CC0 figure.\n" + notice) + "</metadata>",
    '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'
    + base64.b64encode(font).decode() + ')}text{font-family:LocalSans}</style>',
    f'<rect width="{W}" height="{H}" fill="#f8fafc"/>',
]

def text(x, y, s, size=29, col=INK):
    if size not in fonts:
        fonts[size] = ImageFont.truetype(io.BytesIO(font), size, layout_engine=ImageFont.Layout.BASIC)
    b = d.textbbox((x, y), s, font=fonts[size], anchor="lt")
    if b[0] < 0 or b[1] < 0 or b[2] > W or b[3] > H:
        overflow.append([s, list(b)])
    d.text((x, y), s, font=fonts[size], fill=col, anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def box(x, y, w, h):
    d.rectangle((x, y, x+w, y+h), fill="white", outline="#c9d5e3", width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="white" stroke="#c9d5e3" stroke-width="3"/>')

def line(points, col=BLUE, width=4):
    d.line(points, fill=col, width=width)
    svg.append('<polyline points="' + " ".join(f"{x},{y}" for x,y in points) + f'" fill="none" stroke="{col}" stroke-width="{width}"/>')

def arrow(x, y, xx, yy, col=BLUE):
    line([(x,y),(xx,yy)], col)
    angle = math.atan2(yy-y, xx-x)
    points = [(xx,yy)] + [(xx-17*math.cos(angle+b), yy-17*math.sin(angle+b)) for b in [-.45,.45]]
    d.polygon(points, fill=col)
    svg.append('<polygon points="' + " ".join(f"{x:.4f},{y:.4f}" for x,y in points) + f'" fill="{col}"/>')

def circle(x, y, r, col):
    d.ellipse((x-r,y-r,x+r,y+r), fill="white", outline=col, width=4)
    svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="white" stroke="{col}" stroke-width="4"/>')





text(45,25,"A represented standard carrier retains the actual inverse class and its full arrow graph",37)
text(45,90,"ANC.1–ANC.17. Original source B, target A=C0(X), genuine arrows and class dX; a completed metric normal connection.",25)
box(45,155,1135,560);box(1240,155,1165,560)
text(78,185,"Genuine augmentation, with source on BOTH copies",30)
text(78,250,"M=regular induction of A⊗L; Π(B)M is dense",28,BLUE)
text(78,315,"Q=M⊕Mop; ψ(b)=diag(Π(b),Π(b))",29)
text(78,380,"ΓQ=diag(ΓM,−ΓM); Δ=[ 0 ΓM ; ΓM 0 ]",28)
text(78,445,"Δ²=1; Δ is odd; [Δ,ψ(b)]graded=0",28,GREEN)
text(78,510,"Even genuine arrows commute exactly with Δ",27,GREEN)
text(78,575,"[Q,ψ,Δ]=0 with nondegenerate source everywhere",25,GREEN)
text(78,640,"Dropping ΓM gives an odd-source commutator of norm 2",24,RED)
text(1273,185,"The ACTUAL inverse and full completed domains",30)
text(1273,250,"E=K⊕Q; Φ=φ0⊕ψ; [E,Φ,FE]=dX",29,BLUE)
text(1273,315,"TQ=Δ lQ⁻¹ on Ran lQ; lQ is dense-range compact",26)
text(1273,380,"DE=Sbar0⊕TQ; full graph domain is the direct sum",25)
text(1273,445,"Both summands have compact unbounded source errors",24,GREEN)
text(1273,510,"Full arrow-domain equality; unlocalized compact errors",24,GREEN)
text(1273,575,"The original inverse is retained; the augmentation adds 0",24)
text(1273,640,"No zero-source carrier or scalar replacement is added",25,GREEN)

box(45,785,2360,440)
text(78,815,"Ordinary absorption uses the represented unit-index summand",31)
text(78,880,"Unit coordinates in M: A⊗L ≅ Hhat_A, with both infinite parities; not an invariant unit submodule.",25,BLUE)
text(78,945,"E ≅ Hhat_A ⊕ (K⊕Q′)  →  Hhat_A  by the proved even ordinary stabilization unitary W.",27)
text(78,1010,"Φ′=WΦW*; D′=WDEW*; Dom D′=W Dom DE; U′g=Wr Ug Ws*.",29,GREEN)
text(78,1075,"The entire source, operator and genuine action are transported: [Hhat_A,Φ′,FD′]=dX.",27,GREEN)
text(78,1140,"W is A-linear and preserves the original R-balance; it is not asserted normal-smooth or equivariant.",24,RED)

box(45,1290,1135,330);box(1240,1290,1165,330)
text(78,1320,"Completed metric normal connection",30)
text(78,1385,"∇0(Σ aj ej)=Σ (δaj)ej; take the minimal closure",26,BLUE)
text(78,1450,"Graph core: finite scalar normal-core coordinates",26)
text(78,1515,"Dom ∇E=W* Dom ∇0; metric and scalar Leibniz rules",24,GREEN)
text(78,1580,"No derivative of the arbitrary W is assumed",25,GREEN)
text(1273,1320,"Exact two-arrow M2 illustration",30)
text(1273,1385,"Π(b)=diag(b,ΓbΓ); V swaps the arrow blocks",26,BLUE)
text(1273,1450,"ψ(1)=I8; all represented coordinates are essential",25,GREEN)
text(1273,1515,"16 products; 4 covariances; both source degree signs",25)
text(1273,1580,"Finite cycle is exactly degenerate, not an inverse index",23,RED)
text(45,1660,"Full Φ′(B), D′, resolvent and U′ normal derivatives, a completed joint graph core and the original physical sum remain.",24,RED)
text(45,1710,"Original CC0. The finite matrices illustrate the signs; the actual class, infinite absorption and closed connection have full proofs.",23)
text(45,1750,"ANC.1–ANC.17 retain the full inverse coefficient and ordered Clifford factors as requirements for the physical graph.",23)
assert not overflow,overflow

Z=Q
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z()) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(row) for row in zip(*A)]
def diag(v):return [[Z(x) if i==j else Z() for j in range(len(v))] for i,x in enumerate(v)]
def add(A,B,sign=1):return [[x+sign*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,c):return [[c*x for x in a] for a in A]
def block(A,B):return [[A[i][j] if i<len(A) and j<len(A) else B[i-len(A)][j-len(A)] if i>=len(A) and j>=len(A) else Z() for j in range(len(A)+len(B))] for i in range(len(A)+len(B))]
def off(A):return [[A[i%len(A)][j%len(A)] if i//len(A)!=j//len(A) else Z() for j in range(2*len(A))] for i in range(2*len(A))]
def mat(A):return [[str(x) for x in a] for a in A]
def unit(i,j):return [[Z(int(r==i and c==j)) for c in range(2)] for r in range(2)]
I2=diag([1,1]);I4=diag([1]*4);I8=diag([1]*8)
Gamma=diag([1,-1]);GM=block(Gamma,Gamma);GQ=block(GM,scale(GM,Z(-1)))
V=off(I2);U=block(V,V);Delta=off(GM);plain=off(I4)
def alpha(b):return mm(mm(Gamma,b),Gamma)
def Pi(b):return block(b,alpha(b))
def psi(b):return block(Pi(b),Pi(b))
assert tr(Delta)==Delta and mm(Delta,Delta)==I8 and add(mm(Delta,GQ),mm(GQ,Delta))==diag([0]*8)
assert mm(U,U)==I8 and mm(U,Delta)==mm(Delta,U) and psi(I2)==I8
products=[];covariances=[];graded=[]
samples=[unit(i,j) for i in range(2) for j in range(2)]
for j,b in enumerate(samples):
    assert mm(mm(U,psi(b)),U)==psi(alpha(b))
    covariances.append(dict(sample=j,exact_covariance=True))
    degree=int(j in [1,2])
    comm=add(mm(Delta,psi(b)),mm(psi(b),Delta),-(-1)**degree)
    assert comm==diag([0]*8)
    graded.append(dict(sample=j,degree=degree,exact_graded_commutator_zero=True))
    for k,c in enumerate(samples):
        assert mm(psi(b),psi(c))==psi(mm(b,c))
        products.append(dict(left=j,right=k,exact_product=True))
bad=add(mm(plain,psi(samples[1])),mm(psi(samples[1]),plain))
bad_square=mm(tr(bad),bad);bad_projection=scale(bad_square,Z(1,4))
assert mm(bad_projection,bad_projection)==bad_projection and any(any(x for x in r) for r in bad_projection)
assert bad==scale(mm(psi(samples[1]),plain),Z(2))
R=diag([2,3,2,3,2,3,2,3]);D=mm(Delta,R)
assert mm(R,Delta)==mm(Delta,R) and tr(D)==D and mm(D,D)==mm(R,R) and mm(U,D)==mm(D,U)
source_errors=[]
for j,b in enumerate(samples):
    degree=graded[j]['degree']
    error=add(mm(D,psi(b)),mm(psi(b),D),-(-1)**degree)
    assert error==mm(Delta,add(mm(R,psi(b)),mm(psi(b),R),-1))
    source_errors.append(dict(sample=j,exact_unbounded_source_formula=True))
order=[0,2,5,7,1,3,4,6]
Wm=[[Z(int(order[i]==j)) for j in range(8)] for i in range(8)]
assert mm(Wm,tr(Wm))==I8 and mm(tr(Wm),Wm)==I8
assert mm(mm(Wm,GQ),tr(Wm))==diag([1]*4+[-1]*4)
Dprime=mm(mm(Wm,D),tr(Wm));Uprime=mm(mm(Wm,U),tr(Wm))
transport=[]
for j,b in enumerate(samples):
    p=mm(mm(Wm,psi(b)),tr(Wm))
    assert mm(mm(Uprime,p),tr(Uprime))==mm(mm(Wm,psi(alpha(b))),tr(Wm))
    transport.append(dict(sample=j,exact_transported_covariance=True))
checks=dict(schema="actual-normal-carrier-checks/v1",field="Q",source_products=products,source_covariances=covariances,graded_source_tests=graded,unbounded_source_tests=source_errors,transported_covariances=transport,grading=mat(GQ),correct_degenerate_phase=mat(Delta),plain_wrong_phase=mat(plain),wrong_odd_source_error=mat(bad),wrong_error_squared_projection=mat(bad_projection),wrong_odd_source_error_norm="2",source_identity=mat(psi(I2)),reference=mat(R),unbounded_operator=mat(D),finite_even_reordering=mat(Wm),finite_transported_operator=mat(Dprime),exact_unitary_odd_degenerate_phase=True,exact_arrow_invariance=True,finite_source_everywhere_nondegenerate=True,actual_entire_class_retained_by_proof=True,actual_completed_metric_normal_connection_proved=True,ordinary_standard_absorption_proved_in_lesson=True,finite_model_proves_infinite_absorption=False,full_source_operator_arrow_normal_derivatives_proved=False,completed_joint_normal_operator_domain_proved=False,original_physical_graph_sum_proved=False,original_Bott_comparison_proved=False,all_fraction_checks=True,canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"actual-normal-carrier.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"actual-normal-carrier.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"ACTUAL-NORMAL-CARRIER-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(products=len(products),covariances=len(covariances),graded_tests=len(graded),source_tests=len(source_errors),wrong_error_norm=2,overflows=overflow)))
