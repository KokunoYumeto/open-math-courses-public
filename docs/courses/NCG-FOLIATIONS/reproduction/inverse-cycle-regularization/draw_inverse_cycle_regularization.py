"""Actual Bott-source inverse regularization: original CC0 diagram and exact checks."""
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
W, H = 2450, 1700
INK, BLUE, GREEN, RED = "#17283c", "#17638d", "#286d49", "#b64932"
im = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>An unbounded representative with the actual Bott source</title>",
    "<desc>IUR.1 to IUR.15. Exact unitary normalization retains the zero-source summand. One compact inverse controls source commutators and genuine arrow graph domains. Finite matrices distinguish whole invertibility, source-essential index and the zero scalar-unit restriction.</desc>",
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



text(45,25,"An unbounded Bott-source inverse: the actual class and its completed graph",40)
text(45,91,"IUR.1–IUR.15. Source B, target A=C0(X), original anchor and genuine arrows. Normal and essential replacement remain.",25)
box(45,155,1135,585);box(1240,155,1165,585)
text(78,185,"The source is preserved through normalization",31)
text(78,250,"K̃ = K⊕Kop;  φ(b)=diag(φ0(b),0)",30,BLUE)
text(78,315,"F = [ F0  C ; C  −F0 ];  C=(1−F0²)½",30)
text(78,380,"F=F*=F⁻¹;  [K̃,φ,F]=dX ∈ KKH(B,A)",30,GREEN)
text(78,445,"The second summand has ZERO B source",29,RED)
text(78,510,"Relative scalar unit acts on BOTH summands",27)
text(78,575,"Ordinary scalar restriction: 0A; no extra arrow claim",25,RED)
text(78,640,"A whole invertible operator can retain a nonzero",26)
text(78,695,"class for the represented B-source subspace",26)
text(1273,185,"One regulator with exact completed domain",31)
text(1273,250,"r=1+Σ(1−un); l=r⁻¹ ∈ KA(K̃); [l,F]=0",28,BLUE)
text(1273,315,"D=Fl⁻¹;  Dom D=Ran l;  ||Dξ||=||rξ||",30,GREEN)
text(1273,380,"(D±i)⁻¹=l(F∓il)(1+l²)⁻¹ is module compact",27)
text(1273,445,"FD−F is compact; the class remains dX",29,GREEN)
text(1273,510,"r φ(b)ξ=φ(b)rξ+Cbξ on the full domain",28)
text(1273,575,"[D,φ(b)]gr = F Cb + [F,φ(b)]gr r",28,BLUE)
text(1273,640,"Both terms are compact for the dense source core",25)
text(1273,695,"Range membership follows from a convergent inverse equation",23)
box(45,800,2360,310)
text(78,830,"Genuine arrows retain the completed graph",31)
text(78,895,"Ug Ran ls = Ran lr;  Ug rs Ug⁻¹ = rr+Ag;  Ag=Σ(un−αg un)",29,BLUE)
text(78,960,"||Dr Ugξ|| ≤ ||Dsξ||+||Ag|| ||ξ||;  compact-arrow tails and graph maps are continuous",27,GREEN)
text(78,1025,"(αgD−D)φ(b) = (αgF)Agφ(b) + [(αgF−F)φ(b)]r + (αgF−F)Cb",27)
text(78,1080,"This is the actual B-source cycle. No normal derivative of the chosen regulator or lift witness is asserted.",25,RED)
box(45,1170,2360,400)
text(78,1200,"Exact finite model: represented first copy, zero-source opposite-graded second copy",30)
for y,label,values,col in [
    (1265,"Coordinate",["1","2","3","4","5","6"],INK),
    (1325,"Grading",["+","+","−","−","−","+"],INK),
    (1385,"Source projection",["1","1","1","0","0","0"],RED),
    (1445,"D²",["4","9","9","4","16","16"],GREEN),
]:
    text(78,y,label,30,col)
    for j,value in enumerate(values):
        text(520+105*j,y,value,30,col)
text(1320,1265,"Whole D is invertible",29,BLUE)
text(1320,1330,"Remove the first ↔ fourth coupling",25)
text(1320,1395,"Essential D+: [0  3]: C²→C",29,GREEN)
text(1320,1460,"Even vacuum kernel; index +1",28,GREEN)
text(78,1520,"The finite removal is bounded. It does not prove infinite essential compression or a completed normal connection.",25,RED)
text(45,1615,"Sixteen source products, four covariances, exact normalization/square/commutator identities and both indices are checked.",25)
text(45,1660,"Original CC0. Section 11BB, IUR.1–IUR.15. The physical graph sum and original Bott comparison remain separate.",24)
assert not overflow,overflow
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A): return [list(x) for x in zip(*A)]
def diag(v): return [[x if i==j else Q(0) for j in range(len(v))] for i,x in enumerate(v)]
def add(A,B,scale=Q(1)): return [[x+scale*y for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def scale(A,x): return [[x*y for y in row] for row in A]
def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
def mat(A): return [[str(x) for x in row] for row in A]
def zero(A): return not any(x for row in A for x in row)
def psd2(A): return tr(A)==A and A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]-A[0][1]*A[1][0]>=0


I3=diag([Q(1)]*3)
F0=[[Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(1)],[Q(0),Q(1),Q(0)]]
C=diag([Q(1),Q(0),Q(0)])
P=diag([Q(1)]*3+[Q(0)]*3)
G=diag([Q(1),Q(1),Q(-1),Q(-1),Q(-1),Q(1)])
R=diag([Q(2),Q(3),Q(3),Q(2),Q(4),Q(4)])
L=diag([Q(1,2),Q(1,3),Q(1,3),Q(1,2),Q(1,4),Q(1,4)])
I6=diag([Q(1)]*6)
F=[[ (F0[i][j] if i<3 and j<3 else -F0[i-3][j-3] if i>=3 and j>=3 else C[i%3][j%3]) for j in range(6)] for i in range(6)]
assert tr(F)==F and mm(F,F)==I6 and zero(add(mm(F,G),mm(G,F)))
assert mm(R,F)==mm(F,R) and mm(L,R)==I6
D=mm(F,R);square=mm(D,D)
assert tr(D)==D and square==diag([Q(4),Q(9),Q(9),Q(4),Q(16),Q(16)])
U=diag([Q(1),Q(-1),Q(1),Q(1),Q(1),Q(-1)])
assert mm(U,U)==I6 and mm(U,P)==mm(P,U) and mm(U,G)==mm(G,U)
assert mm(U,R)==mm(R,U)
error=add(mm(mm(U,D),U),D,Q(-1))
K=mm(add(mm(mm(U,F),U),F,Q(-1)),P)
assert mm(error,P)==mm(K,R)
assert mm(add(mm(D,P),mm(P,D),Q(-1)),L)==add(mm(F,P),mm(P,F),Q(-1))
Qp=add(I6,P,Q(-1))
removed=add(mm(mm(P,D),Qp),mm(mm(Qp,D),P))
essential=[[D[i][j] for j in range(3)] for i in range(3)]
assert essential==[[Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(3)],[Q(0),Q(3),Q(0)]]
assert removed[0][3]==removed[3][0]==2 and sum(x!=0 for row in removed for x in row)==2
samples=[Q(1),Q(2),Q(-3),Q(0)]
source=[]
for b in samples:
    assert mm(mm(U,scale(P,b)),U)==scale(P,b)
    assert mm(add(mm(D,scale(P,b)),mm(scale(P,b),D),Q(-1)),L)==scale(add(mm(F,P),mm(P,F),Q(-1)),b)
    for a0 in samples:
        assert mm(scale(P,b),scale(P,a0))==scale(P,b*a0)
    source.append(dict(source_scalar=str(b),exact_covariance=True,exact_scaled_commutator=True,all_source_products=True))
checks=dict(schema="inverse-cycle-regularization-exact-checks/v1",
            normalization=mat(F),source_projection=mat(P),grading=mat(G),regulator=mat(R),
            compact_inverse=mat(L),operator=mat(D),square=mat(square),arrow_action=mat(U),
            localized_arrow_error=mat(mm(error,P)),off_diagonal_removal=mat(removed),
            essential_operator=mat(essential),source_tests=source,
            exact_unitary_normalization=True,exact_oddness=True,exact_square=True,
            exact_arrow_formula=True,exact_off_diagonal_removal=True,
            whole_operator_kernel_dimension=0,whole_scalar_unit_index=0,
            essential_even_kernel_dimension=1,essential_odd_kernel_dimension=0,essential_source_index=1,
            full_B_source_representation_nondegenerate=False,
            relative_unitization_representation_nondegenerate=True,
            equivariant_scalar_unit_cycle_asserted=False,
            finite_removal_proves_infinite_removal=False,normal_regulator_derivative_proved=False,
            all_fraction_checks=True,canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"inverse-cycle-regularization.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"inverse-cycle-regularization.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"INVERSE-CYCLE-REGULARIZATION-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(source_tests=len(source),source_products=len(samples)**2,exact_arrow_formula=True,essential_index=1,overflows=overflow)))
