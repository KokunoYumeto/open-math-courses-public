"""Positive-evaluation shift: original CC0 diagram and exact rational checks."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, base64, html, io, json, math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--output-dir", type=Path, default=HERE / "out")
p.add_argument("--resources", type=Path, default=HERE.parent / "labelled-geometric-kernel")
a = p.parse_args()
a.output_dir.mkdir(parents=True, exist_ok=True)
font = (a.resources / "fonts/DejaVuSans.ttf").read_bytes()
notice = (a.resources / "FONT-NOTICE.txt").read_text(encoding="utf-8")
W, H = 2450, 1720
INK, BLUE, GREEN, RED = "#17283c", "#17638d", "#286d49", "#b64932"
im = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>The graded positive-evaluation shift retains its source and both finite boundaries</title>",
    "<desc>PES.1 to PES.19. Genuine action, graded shift, whole-base homotopy and a bounded product with the proved Bott source lift. Exact rational tests retain both finite kernel and cokernel; the infinite coefficient-class multiplicity is proved in the lesson.</desc>",
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

text(45,25,"The positive-evaluation shift: grading, genuine action and both finite boundaries",40)
text(45,91,"PES.1–PES.19. The homotopy retains every x∈X; its row-zero contribution retains the full Fock coefficient class.",26)
box(45,155,1135,635)
box(1240,155,1165,635)
text(78,185,"An exact E-source cycle before taking the lift",31)
text(78,248,"ρt:E→KA(HA);  Ugt ρt(e) Ugt* = ρt(αg e)",29,BLUE)
text(78,312,"tn↓0;  tn(v)=v+(1−v)tn;  t0(v)=1",29)
text(78,376,"E+=ℓ²(N)⊗HA;  E−=E+ with opposite grading",27)
text(78,440,"F = [ 0   ΓS ; ΓS*   0 ];  grading = diag(Γ,−Γ)",28,BLUE)
text(78,504,"1−F² = diag(P0,0); adjacent differences are compact",26,GREEN)
text(78,568,"Γ changes odd-source sums into differences",28,GREEN)
text(78,632,"Π0(I) is compact, but generally Π0(I)≠0",28,RED)
text(78,696,"An E-representation does not become a B-representation",25,RED)
text(78,754,"At v=1: row zero is ρ1; its complement is degenerate",25)
text(1273,185,"The genuine bounded B-source product",31)
text(1273,248,"zB ∈ KKH(B,E),  zB[q]=1B  (proved proper-source lift)",26,BLUE)
text(1273,312,"D = Z ⊗E Eshift;  Φ(b)=φz(b)⊗1",29)
text(1273,376,"Fd = M¼ Sz M¼ + (1−M)¼ GF (1−M)¼",29,BLUE)
text(1273,440,"GF is a graded F-connection; M is an anchored separator",25)
text(1273,504,"[D,Φ,Fd] = zB [h1] mFock [ev0] = dX",29,GREEN)
text(1273,568,"Source B, target A, base X and arrow action are retained",25,GREEN)
text(1273,632,"The lift witness Z is part of this construction",27)
text(1273,696,"Normal derivative and graph-domain controls are",26,RED)
text(1273,754,"additional hypotheses for the physical operator sum",26,RED)
box(45,850,2360,255)
text(78,881,"Exact rational action: V(t)=(1+t²)⁻¹ [ 1−t²   2t ; 2t   t²−1 ];  V*=V, V²=1",30,BLUE)
text(78,945,"Toy sequence tn=1/(n+1); e(t)=diag(1+t,2−t); δn=1/((n+1)(n+2))",28)
text(78,1008,"Source difference norm = (1−v)δn; action norm ≤2δn; source-localized arrow norm ≤4δn",27,GREEN)
text(78,1060,"Six adjacent pairs × four rational homotopy parameters are checked without floating-point arithmetic.",25)
box(45,1165,2360,420)
text(78,1195,"Five-row square truncation of S*: retain both boundary carriers",31)
text(80,1270,"E+ rows",27)
text(80,1430,"E− rows",27)
for n in range(5):
    x=425+340*n
    circle(x,1290,37,RED if n==0 else BLUE)
    circle(x,1450,37,RED if n==4 else BLUE)
    text(x-9,1273,str(n),29,RED if n==0 else INK)
    text(x-9,1433,str(n),29,RED if n==4 else INK)
    if n>0:
        arrow(x-28,1324,x-340+28,1416,GREEN)
text(335,1345,"kernel",25,RED)
text(1700,1505,"terminal cokernel",25,RED)
text(78,1542,"Finite coefficient index: dim ker − dim coker = 2−2=0.  The completed infinite shift has no terminal row.",25)
text(45,1630,"Infinite result: coefficient-class multiplicity +1, proved by the endpoint decomposition; not a finite-matrix index certificate.",26)
text(45,1675,"Original CC0. Proof: Section 11AZ, PES.1–PES.19. The finite illustration does not supply normal graph-domain estimates.",24)
assert not overflow, overflow

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
I2=diag([Q(1)]*2)
Gamma=diag([Q(1),Q(-1)])
Odd=[[Q(0),Q(1)],[Q(1),Q(0)]]
def V(t): return scale([[1-t*t,2*t],[2*t,t*t-1]],1/(1+t*t))
def e(t): return diag([1+t,2-t])
adjacent=[]
for n in range(6):
    delta=Q(1,(n+1)*(n+2))
    for v in [Q(0),Q(1,3),Q(2,3),Q(1)]:
        t=v+(1-v)*Q(1,n+1)
        u=v+(1-v)*Q(1,n+2)
        vt,vu=V(t),V(u)
        assert mm(vt,vt)==mm(vu,vu)==I2 and tr(vt)==vt and tr(vu)==vu
        difference=add(vu,vt,Q(-1))
        assert add(e(u),e(t),Q(-1))==diag([-(1-v)*delta,(1-v)*delta])
        assert psd2(add(scale(I2,(2*delta)**2),mm(tr(difference),difference),Q(-1)))
        lower=mm(add(mm(vt,vu),I2,Q(-1)),e(u))
        upper=mm(add(mm(vu,vt),I2,Q(-1)),e(t))
        assert psd2(add(scale(I2,(4*delta)**2),mm(tr(lower),lower),Q(-1)))
        assert psd2(add(scale(I2,(4*delta)**2),mm(tr(upper),upper),Q(-1)))
        adjacent.append(dict(n=n,v=str(v),t=str(t),u=str(u),delta=str(delta),
                             exact_involutions=True,exact_source_difference=True,
                             exact_action_bound=True,exact_localized_arrow_bounds=True))
finite=[]
graded=[]
for N in [2,3,4,5]:
    backward=[[Q(int(j==i+1)) for j in range(N)] for i in range(N)]
    ident=diag([Q(1)]*N)
    kernel=add(ident,mm(tr(backward),backward),Q(-1))
    cokernel=add(ident,mm(backward,tr(backward)),Q(-1))
    assert kernel==diag([Q(int(n==0)) for n in range(N)])
    assert cokernel==diag([Q(int(n==N-1)) for n in range(N)])
    assert sum(kernel[i][i] for i in range(N))==sum(cokernel[i][i] for i in range(N))==1
    finite.append(dict(rows=N,row_zero_kernel=mat(kernel),terminal_cokernel=mat(cokernel),
                       coefficient_dimension=2,kernel_dimension=2,cokernel_dimension=2,finite_index=0))
    gs=kron(backward,Gamma)
    plain=kron(backward,I2)
    constant=kron(ident,Odd)
    assert zero(add(mm(gs,constant),mm(constant,gs)))
    assert not zero(add(mm(plain,constant),mm(constant,plain)))
    source=[[Q(0)]*(2*N) for i in range(2*N)]
    for n in range(N):
        for i in range(2):
            for j in range(2): source[2*n+i][2*n+j]=Q(1,n+1)*Odd[i][j]
    lhs=add(mm(gs,source),mm(source,gs))
    gamma_all=kron(ident,Gamma)
    rhs=mm(gamma_all,add(mm(plain,source),mm(source,plain),Q(-1)))
    assert lhs==rhs
    graded.append(dict(rows=N,exact_graded_difference_identity=True,
                       constant_odd_commutator_with_Gamma_zero=True,
                       constant_odd_commutator_without_Gamma_nonzero=True))
checks=dict(schema="positive-evaluation-shift-exact-checks/v1",
            adjacent_rational_tests=adjacent,finite_boundary_tests=finite,
            graded_commutator_tests=graded,all_fraction_checks=True,
            infinite_coefficient_multiplicity_proved_by_lesson=1,
            finite_matrix_certifies_infinite_index=False,
            compact_ideal_action_identified_with_zero=False,
            E_source_relabelled_B=False,completed_normal_domains_supplied=False,
            canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(a.output_dir/"positive-evaluation-shift.png",format="PNG",optimize=False,compress_level=9)
(a.output_dir/"positive-evaluation-shift.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(a.output_dir/"POSITIVE-EVALUATION-SHIFT-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(rational_tests=len(adjacent),finite_boundary_tests=len(finite),
                     graded_tests=len(graded),overflows=overflow)))
