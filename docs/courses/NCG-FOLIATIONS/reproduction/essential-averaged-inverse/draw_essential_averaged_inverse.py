"""Proper-source average and essential unbounded inverse: original CC0 exact diagram."""
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
    "<title>A proper-source average and a completed essential inverse</title>",
    "<desc>EAI.1 to EAI.24. A proper-source cutoff column makes the actual bounded phase exactly invariant. A controlled reference and full regularity/resolvent comparison discard the zero-source normalization summand. Full arrow graph domains and class d_X are retained; normal derivatives and physical sum remain.</desc>",
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




text(45,25,"Proper-source averaging removes the zero-source summand on the full closed graph",38)
text(45,91,"EAI.1–EAI.24. Actual nondegenerate source B, target A=C0(X), original anchor, class dX and genuine arrows.",26)
box(45,155,1135,565);box(1240,155,1165,565)
text(78,185,"Average on the ACTUAL source representation",31)
text(78,250,"C0(W)→L_A(K) is nondegenerate; W is proper",27,BLUE)
text(78,315,"Vξ(g)=Cg ξ;  Cg²=c(g⁻¹·);  V*V=1",30)
text(78,380,"T(g)=Ug F0,s Ug⁻¹;  Fbar=V* T V",29,BLUE)
text(78,445,"αg Fbar=Fbar EXACTLY; (Fbar−F0)φ0(b) is compact",25,GREEN)
text(78,510,"The centre is used on K, not lifted into EB",27)
text(78,575,"Source class dX and the actual representation remain",26,GREEN)
text(78,640,"A proper probability anchor alone would not suffice",25,RED)
text(1273,185,"Reference control and closed compression",31)
text(1273,250,"P is invariant; [r,P]=CP is bounded compact",27,BLUE)
text(1273,315,"rdiag=r−CP(2P−1)≥1;  ri=Pi r Pi",29)
text(1273,380,"Si=Pi D Pi=Fi ri+Ti; Ki=[ri,Fi] is bounded",27)
text(1273,445,"vε=(1+εri)⁻¹ maps into the reference core",27)
text(1273,510,"[Si,vε] is uniformly bounded and strongly zero",26,GREEN)
text(1273,575,"State-local deficiency test → self-adjoint regular closure",24,GREEN)
text(1273,640,"The full closure domain can exceed the reference domain",24,RED)
box(45,785,2360,375)
text(78,815,"Essential operator: source-local compactness, exact inverse class and full arrow domains",31)
text(78,880,"Localized resolvent difference ≤ Cb/s²; its phase difference integral is compact",28,BLUE)
text(78,945,"[K,φ0,Sbar0(1+Sbar0²)⁻½]=dX; φ0(B)K is dense; the zero-source block is discarded",27,GREEN)
text(78,1010,"Ug Dom Sbar0,s = Dom Sbar0,r;  Sbar0,r Ug−Ug Sbar0,s = −P F Ag P Ug",27,GREEN)
text(78,1075,"Ag=αg r−r is a continuous compact-arrow section; the graph bound holds on the FULL closure",25)
text(78,1130,"Normal derivatives of the lift, cutoff, averaged phase and regulator still require proofs.",26,RED)
box(45,1220,2360,425)
text(78,1250,"Exact Z/2 example: U swaps the two even coordinates; cutoff c=1/2",31)
text(78,1315,"F0=[ 0 0 0 ; 0 0 1 ; 0 1 0 ]",30,BLUE)
text(1273,1315,"Fbar=[ 0 0 1/2 ; 0 0 1/2 ; 1/2 1/2 0 ]",28,GREEN)
arrow(1045,1343,1235,1343,GREEN)
text(78,1380,"r=2I+P+FPF≥2; r commutes with F and U, but not P",27)
text(78,1445,"Essential S0=4Fbar; positive-to-negative block (2,2)",28,GREEN)
text(1273,1445,"Kernel (1,−1); U acts by −1; ordinary index +1",25,GREEN)
text(78,1510,"Removed reference block norm 1/2; removed D block norm 3",28,BLUE)
text(78,1575,"All averaging, normalization, source, covariance and compression identities are exact in Q(√2).",25)
text(45,1690,"The finite example illustrates the proof; completed regularity and full-domain invariance are established in the lesson.",25)
text(45,1735,"Original CC0. Section 11BC, EAI.1–EAI.24. The normal connection, physical graph sum and original Bott comparison remain.",24)
assert not overflow,overflow

class Quad:
    """Exact field Q(sqrt(2)); coefficients are fractions."""
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    @staticmethod
    def coerce(x): return x if isinstance(x,Quad) else Quad(x)
    def __add__(self,x):
        x=self.coerce(x);return Quad(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Quad(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x);return Quad(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x);den=x.a*x.a-2*x.b*x.b
        if not den:raise ZeroDivisionError()
        return Quad((self.a*x.a-2*self.b*x.b)/den,(self.b*x.a-self.a*x.b)/den)
    def __eq__(self,x):
        x=self.coerce(x);return self.a==x.a and self.b==x.b
    def __bool__(self):return bool(self.a or self.b)
    def __str__(self):
        if not self.b:return str(self.a)
        if not self.a:return str(self.b)+"*sqrt(2)"
        return str(self.a)+("+" if self.b>0 else "")+str(self.b)+"*sqrt(2)"
Z=Quad
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z()) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(row) for row in zip(*A)]
def diag(v):return [[Z(x) if i==j else Z() for j in range(len(v))] for i,x in enumerate(v)]
def add(A,B,sign=1):return [[x+sign*y for x,y in zip(ar,br)] for ar,br in zip(A,B)]
def scale(A,c):return [[c*x for x in row] for row in A]
def mat(A):return [[str(x) for x in row] for row in A]
def zero(A):return not any(x for row in A for x in row)
def inverse(A):
    n=len(A);aug=[row[:]+diag([1]*n)[i] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[pivot]=aug[pivot],aug[j]
        value=aug[j][j];aug[j]=[x/value for x in aug[j]]
        for i in range(n):
            if i!=j:
                value=aug[i][j];aug[i]=[x-value*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]
I3=diag([1]*3);I6=diag([1]*6)
F0=[[Z(0),Z(0),Z(0)],[Z(0),Z(0),Z(1)],[Z(0),Z(1),Z(0)]]
U=[[Z(0),Z(1),Z(0)],[Z(1),Z(0),Z(0)],[Z(0),Z(0),Z(1)]]
Fbar=scale(add(F0,mm(mm(U,F0),U)),Z(Q(1,2)))
assert Fbar==[[Z(0),Z(0),Z(Q(1,2))],[Z(0),Z(0),Z(Q(1,2))],[Z(Q(1,2)),Z(Q(1,2)),Z(0)]]
assert mm(U,U)==I3 and mm(mm(U,Fbar),U)==Fbar
Pk=scale([[Z(1),Z(-1),Z(0)],[Z(-1),Z(1),Z(0)],[Z(0),Z(0),Z(0)]],Z(Q(1,2)))
assert mm(Pk,Pk)==Pk and zero(mm(Fbar,Pk))
C=add(Pk,scale(add(I3,Pk,-1),Z(0,Q(1,2))))
assert tr(C)==C and mm(C,C)==add(I3,mm(Fbar,Fbar),-1) and mm(Fbar,C)==mm(C,Fbar)
F=[[Fbar[i][j] if i<3 and j<3 else -Fbar[i-3][j-3] if i>=3 and j>=3 else C[i%3][j%3] for j in range(6)] for i in range(6)]
P=diag([1,1,1,0,0,0]);Qp=add(I6,P,-1)
G=diag([1,1,-1,-1,-1,1])
U6=[[U[i%3][j%3] if i//3==j//3 else Z() for j in range(6)] for i in range(6)]
assert tr(F)==F and mm(F,F)==I6 and zero(add(mm(F,G),mm(G,F)))
assert mm(U6,F)==mm(F,U6) and mm(U6,P)==mm(P,U6)
R=add(scale(I6,Z(2)),add(P,mm(mm(F,P),F)))
assert mm(R,F)==mm(F,R) and mm(U6,R)==mm(R,U6) and tr(R)==R
L=inverse(R);assert mm(R,L)==I6 and mm(L,R)==I6
D=mm(F,R);assert tr(D)==D and mm(D,D)==mm(R,R)
assert mm(D,inverse(D))==I6
Br=add(mm(mm(P,R),Qp),mm(mm(Qp,R),P))
Bo=add(mm(mm(P,D),Qp),mm(mm(Qp,D),P))
projection=scale(mm(Br,Br),Z(4));assert mm(projection,projection)==projection and not zero(projection)
assert mm(Bo,Bo)==[[Z(9)*mm(C,C)[i%3][j%3] if i//3==j//3 else Z() for j in range(6)] for i in range(6)]
assert mm(C,Pk)==Pk
S0=[[D[i][j] for j in range(3)] for i in range(3)]
assert S0==scale(Fbar,Z(4)) and mm(U,S0)==mm(S0,U)
assert [S0[2][i] for i in range(2)]==[Z(2),Z(2)]
kernel=[[Z(1)],[Z(-1)],[Z(0)]]
assert zero(mm(S0,kernel)) and mm(U,kernel)==scale(kernel,Z(-1))
def pi(b):return [[b[i][j] if i<3 and j<3 else Z() for j in range(6)] for i in range(6)]
def unit(i,j):return [[Z(int(r==i and c==j)) for c in range(3)] for r in range(3)]
samples=[I3,unit(0,0),unit(0,2),unit(2,0)]
products=[];covariances=[]
for i,b in enumerate(samples):
    assert mm(mm(U6,pi(b)),U6)==pi(mm(mm(U,b),U))
    covariances.append(dict(sample=i,exact_covariance=True))
    for j,e in enumerate(samples):
        assert mm(pi(b),pi(e))==pi(mm(b,e))
        products.append(dict(left=i,right=j,exact_product=True))
checks=dict(schema="essential-averaged-inverse-exact-checks/v1",
            field="Q(sqrt(2))",initial_phase=mat(F0),source_action=mat(U),
            averaged_phase=mat(Fbar),normalized_unitary=mat(F),grading=mat(G),
            source_projection=mat(P),regulator=mat(R),inverse_regulator=mat(L),
            full_operator=mat(D),removed_reference_block=mat(Br),removed_operator_block=mat(Bo),
            essential_operator=mat(S0),even_kernel=mat(kernel),
            source_products=products,source_covariances=covariances,
            exact_average=True,exact_invariance=True,exact_normalization=True,
            exact_regulator_commutation=True,exact_operator_square=True,
            exact_essential_compression=True,reference_off_diagonal_norm="1/2",
            operator_off_diagonal_norm="3",essential_source_index=1,
            full_source_nondegenerate_after_compression=True,
            full_closed_arrow_domains_proved_by_lesson=True,
            even_kernel_action="-1",
            ordinary_index_identifies_equivariant_scalar_unit=False,
            finite_model_supplies_regular_closure=False,normal_derivatives_proved=False,
            physical_graph_sum_proved=False,all_field_checks=True,
            canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"essential-averaged-inverse.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"essential-averaged-inverse.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"ESSENTIAL-AVERAGED-INVERSE-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(products=len(products),covariances=len(covariances),exact_field="Q(sqrt(2))",index=1,overflows=overflow)))
