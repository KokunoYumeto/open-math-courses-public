"""Completed quantum-positive shift: original CC0 diagram and exact rational checks."""
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
W, H = 2450, 1720
INK, BLUE, GREEN, RED = "#17283c", "#17638d", "#286d49", "#b64932"
im = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>A completed paired positive operator with compact resolvents</title>",
    "<desc>QPS.1 to QPS.19. Matched oscillator scales cancel the mixed terms, yielding actual completed domains, source-local compact arrow errors and parallel ordinary normal resolvents. Exact finite matrices retain both vacuum boundaries.</desc>",
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


text(45,25,"A completed positive operator: matched pairs, graph domains and compact tails",40)
text(45,91,"QPS.1–QPS.19. Source E, target A=C0(X), actual grading and genuine arrow action. The B-source lift is separate.",26)
box(45,155,1135,640); box(1240,155,1165,640)
text(78,185,"Pair positive row n with negative row n−1",31)
text(78,250,"Dn = [ an Q   wn Γ ; wn Γ   an Q ]",32,BLUE)
text(78,315,"QΓ=−ΓQ; use the SAME an on both rows",28,RED)
text(78,380,"Dn² = diag(an² Q²+wn², an² Q²+wn²)",29,GREEN)
text(78,445,"wn→∞; an>0 and an≤2⁻ⁿ√tn",29)
text(78,510,"an Mn≤2⁻ⁿ; wn·adjacent source/arrow error→0",26)
text(78,575,"Every finite pair has a compact Fock resolvent",27,GREEN)
text(78,640,"Tail norm ≤ supn>N (1+wn²)⁻½ →0",29,GREEN)
text(78,705,"f(D±i)⁻¹ is A-module compact for f∈C0(X)",28)
text(78,763,"Global compactness on noncompact X is not inferred",25,RED)
text(1273,185,"Completed domains and actual arrows",31)
text(1273,250,"Graph energy is an A-valued SUM of inner products",26)
text(1273,315,"Take the norm of that A-valued sum, then its square root",25,BLUE)
text(1273,380,"Pointwise summability is insufficient for the module",26,RED)
text(1273,445,"Ug Dom D = Dom D; graph maps are continuous",28,GREEN)
text(1273,510,"(Ug D Ug*−D)Π(e) has compact continuous tails",26)
text(1273,575,"Constant-column connection: ∇(D±i)⁻¹=(D±i)⁻¹∇",26,GREEN)
text(1273,640,"Transport BOTH the connection and its completed domain",25)
text(1273,705,"The transported connection need not equal the original",25,RED)
text(1273,763,"No unlocalized bounded arrow difference is asserted",25,RED)
box(45,850,2360,255)
text(78,880,"Exact finite oscillator: Γ=diag(1,1,−1); Q=[ 0 0 0 ; 0 0 2 ; 0 2 0 ]; vacuum=e0",29,BLUE)
text(78,945,"For w1=1, a1=1/2: D1²=diag(1,2,2,1,2,2); its resolvent norm is 1/√2",29,GREEN)
text(78,1008,"These toy scales verify block identities; the general source controls choose their own wn and an.",25)
text(78,1060,"Example of the module norm: ||x²+(1−x)²||C([0,1])=1, while ||x||²+||1−x||²=2.",26)
box(45,1165,2360,420)
text(78,1195,"Vacuum sector of a four-row square truncation: both zero-energy carriers remain",30)
text(80,1270,"positive rows",26); text(80,1430,"negative rows",26)
for n in range(4):
    x=525+410*n
    circle(x,1290,37,RED if n==0 else BLUE)
    circle(x,1450,37,RED if n==3 else BLUE)
    text(x-9,1273,str(n),29,RED if n==0 else INK)
    text(x-9,1433,str(n),29,RED if n==3 else INK)
    if n>0:
        arrow(x-28,1324,x-410+28,1416,GREEN)
        arrow(x-410+28,1416,x-28,1324,GREEN)
        text(x-255,1328,"w"+str(n),25,GREEN)
text(420,1345,"even vacuum",24,RED)
text(1640,1505,"odd terminal vacuum",24,RED)
text(78,1542,"Finite index: 1−1=0. Infinite calibration: only row-zero vacuum; every paired complement is invertible.",25)
text(45,1630,"The bounded transform has the genuine positive-evaluation class; its ordinary scalar calibration is 1A over the whole base.",25)
text(45,1675,"Original CC0. Section 11BA, QPS.1–QPS.19. This E-source operator does not supply normal domains for the B-source lift.",24)
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

Gamma=diag([Q(1),Q(1),Q(-1)])
Fock=[[Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(2)],[Q(0),Q(2),Q(0)]]
I3=diag([Q(1)]*3)
assert tr(Fock)==Fock and zero(add(mm(Fock,Gamma),mm(Gamma,Fock)))
def pair(n,other_scale=None):
    a=Q(1,n+1); b=a if other_scale is None else other_scale; w=Q(n)
    return [[(a*Fock[i][j] if i<3 and j<3 else
              b*Fock[i-3][j-3] if i>=3 and j>=3 else
              w*Gamma[i%3][j%3]) for j in range(6)] for i in range(6)]
pairs=[]
for n in range(1,5):
    a=Q(1,n+1); w=Q(n); D=pair(n)
    target=kron(diag([Q(1),Q(1)]),add(scale(mm(Fock,Fock),a*a),scale(I3,w*w)))
    assert tr(D)==D and mm(D,D)==target
    total=diag([Q(1),Q(1),Q(-1),Q(-1),Q(-1),Q(1)])
    assert zero(add(mm(total,D),mm(D,total)))
    assert all(target[i][i]>=w*w for i in range(6))
    pairs.append(dict(n=n,a=str(a),w=str(w),operator=mat(D),square=mat(target),
                      exact_square=True,exact_oddness=True,positive_pair_gap=True))
bad=pair(1,Q(1,3));bad_square=mm(bad,bad)
assert any(bad_square[i][j] for i in range(3) for j in range(3,6))
def rank(A):
    B=[row[:] for row in A]; r=0
    for j in range(len(B[0])):
        pivot=next((i for i in range(r,len(B)) if B[i][j]),None)
        if pivot is None: continue
        B[r],B[pivot]=B[pivot],B[r]
        value=B[r][j];B[r]=[x/value for x in B[r]]
        for i in range(len(B)):
            if i!=r:
                value=B[i][j]
                B[i]=[x-value*y for x,y in zip(B[i],B[r])]
        r+=1
        if r==len(B):break
    return r
finite=[]
for N in range(2,6):
    size=6*N;D=[[Q(0)]*size for _ in range(size)]
    for row in range(N):
        for i in range(3):
            for j in range(3):
                D[3*row+i][3*row+j]=Q(1,row+1)*Fock[i][j]
                D[3*N+3*row+i][3*N+3*row+j]=Q(1,row+2)*Fock[i][j]
        if row:
            for i in range(3):
                for j in range(3):
                    D[3*row+i][3*N+3*(row-1)+j]=Q(row)*Gamma[i][j]
                    D[3*N+3*(row-1)+j][3*row+i]=Q(row)*Gamma[i][j]
    grading=diag([Q(1),Q(1),Q(-1)]*N+[Q(-1),Q(-1),Q(1)]*N)
    assert tr(D)==D and zero(add(mm(D,grading),mm(grading,D)))
    even=0;odd=6*N-3
    assert all(D[i][even]==D[i][odd]==0 for i in range(size))
    assert grading[even][even]==1 and grading[odd][odd]==-1 and rank(D)==size-2
    finite.append(dict(square_rows=N,dimension=size,rank=size-2,even_vacuum_index=even,
                       odd_terminal_vacuum_index=odd,finite_index=0,exact_rank_and_grading=True))
for x in [Q(0),Q(1,2),Q(1)]:
    assert x*x+(1-x)*(1-x)<=1
checks=dict(schema="quantum-positive-shift-exact-checks/v1",paired_block_tests=pairs,
            square_boundary_tests=finite,unequal_scales_have_nonzero_cross_terms=True,
            module_norm_example=dict(norm_of_sum=1,sum_of_separate_norm_squares=2),
            all_fraction_checks=True,finite_square_index=0,infinite_calibration_from_lesson=1,
            proper_anchor_identified_with_proper_action=False,
            unlocalized_arrow_difference_asserted_bounded=False,
            transported_normal_connection_identified_with_original=False,
            source_E_relabelled_B=False,normal_lift_module_domains_proved=False,
            canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"quantum-positive-shift.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"quantum-positive-shift.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"QUANTUM-POSITIVE-SHIFT-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(paired_blocks=len(pairs),square_boundaries=len(finite),
                     mismatched_scales_detected=True,overflows=overflow)))
