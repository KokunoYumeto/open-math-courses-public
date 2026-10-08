"""Actual invariant inverse phase and dense normal-compatible operator core: original CC0."""
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
    "<title>A parallel actual inverse phase and dense normal-compatible operator core</title>",
    "<desc>PNC.1 to PNC.18. The actual normalized inverse phase is flattened by an even genuine equivariant unitary. A compact normal-smooth inverse gives a self-adjoint regular operator in the same class and a dense normal-compatible operator core. The original zero-source copy remains; source-essential compression, unbounded source and arrow controls and the physical graph comparison remain unproved.</desc>",
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







text(45,25,"A parallel actual inverse phase gives a dense normal-compatible operator core",37)
text(45,90,"PNC.1–PNC.18. Actual class dX and source B; full new operator domain; the normalization's zero-source copy stays.",25)
box(45,155,1135,565);box(1240,155,1165,565)
text(78,185,"The ACTUAL exactly invariant normalized phase",29)
text(78,250,"Fhat=[ Fav sqrt(1−Fav²) ; sqrt(1−Fav²) −Fav ]",26,BLUE)
text(78,315,"Fhat²=1; genuine arrows commute with Fhat",27,GREEN)
text(78,380,"Source phihat=diag(phi0,0); proper centre is copied",24)
text(78,445,"Add the represented degenerate regular phase Δ",26)
text(78,510,"Z=Ktilde⊕Q; FZ=Fhat⊕Δ; [Z,Ψ,FZ]=dX",27,GREEN)
text(78,575,"Finite source: f=(3/5)σ1; sqrt(1−f²)=(4/5)I2",25)
text(78,640,"phihat(1)=diag(1,1,0,0): rank 2, not rank 4",25,RED)
text(1273,185,"An even genuinely equivariant phase flattening",29)
text(1273,250,"W+:Z+ → M by proper-source regular absorption",25,BLUE)
text(1273,315,"W−=W+ F+− : Z− → M, an onto unitary",26)
text(1273,380,"W=diag(W+,W−); W FZ W*=J=[ 0 I ; I 0 ]",25,GREEN)
text(1273,445,"Φ=W Ψ W*; arrows are diag(L,L)",27)
text(1273,510,"Two equal regular connections: ∇J=J∇",28,GREEN)
text(1273,575,"Both the phase and arrows are parallel on full domains",24)
text(1273,640,"No derivative of W+, F+− or W is assumed",25,GREEN)
box(45,785,1135,670);box(1240,785,1165,670)
text(78,815,"A NORMAL-SMOOTH compact inverse",29)
text(78,880,"h=Σ cj θηj,ηj >0; cj controls all normal word tails",24,BLUE)
text(78,940,"H0=diag(h,h); T=J H0⁻¹ on exactly Ran H0",26)
text(78,1000,"Rλ=H0(J+iλH0)⁻¹; δRλ=J Bλ⁻¹(δH0)Bλ⁻¹",24,GREEN)
text(78,1060,"Order matters: h(x)h′(x) generally differs from h′(x)h(x).",23,RED)
line([(180,1280),(1080,1280)],INK,2)
line([(630,1105),(630,1335)],INK,2)
for key,col in [("11",BLUE),("22",GREEN),("12",INK)]:
    pts=[]
    for n in range(-80,81):
        x=n/80
        value=(2+x)/32 if key=="11" else (3-x)/32 if key=="22" else x/128
        pts.append((630+400*x,1280-1400*value))
    line(pts,col,4)
text(205,1290,"−1",21);text(640,1290,"0",21);text(1020,1290,"1",21)
text(78,1360,"Blue h11=(2+x)/32; green h22=(3−x)/32; black h12=x/128.",22)
text(78,1420,"PNC.18: exact rational 8×8 realified inverse/derivative tests.",23)
text(1273,815,"The ACTUAL dense normal-compatible operator core",29)
text(1273,880,"Cλ=Rλ CN ⊂ Dom T ∩ Dom ∇",29,BLUE)
text(1273,940,"Every z∈Dom T: approximate (T+iλ)z by ξn∈CN",24)
text(1273,1000,"Rλ ξn → z; T Rλ ξn=(1−iλRλ)ξn → Tz",25,GREEN)
text(1273,1060,"This is a full T-graph core and a dense joint domain.",25,GREEN)
text(1273,1120,"FT=J(1+H0²)⁻¹/²; FT−J is module compact",26)
text(1273,1180,"The full source-typed bounded cycle still has class dX.",24,GREEN)
text(1273,1240,"Bounded arrow error = αg(FT−J)−(FT−J), compact",24)
text(1273,1300,"A core for T is not yet a core for the joint graph.",24,RED)
text(1273,1360,"The Φ-source and unbounded arrow tests remain.",25,RED)
text(1273,1420,"The zero-source submodule has not been compressed.",24,RED)
box(45,1510,2360,195)
text(78,1540,"Retain both proved representatives while completing the physical comparison",30)
text(78,1600,"The earlier essential inverse has nondegenerate B-source and full unbounded arrow domains; this one has the new normal core.",23)
text(78,1660,"Original C0(T) balance, z⁻¹ρ(s), exterior grading and final right Clifford block remain required.",25,RED)
text(45,1740,"Original CC0. Finite matrices check source rank, normalization and resolvent order; actual infinite class/core assertions are proved.",23)
assert not overflow,overflow

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q()) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(r) for r in zip(*a)]
def diag(v):return [[Q(x) if i==j else Q() for j in range(len(v))] for i,x in enumerate(v)]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r] for r in a]
def block(a,b):return [[a[i][j] if i<len(a) and j<len(a) else b[i-len(a)][j-len(a)] if i>=len(a) and j>=len(a) else Q() for j in range(len(a)+len(b))] for i in range(len(a)+len(b))]
def inv(a):
    n=len(a);b=[list(r)+[Q(int(i==j)) for j in range(n)] for i,r in enumerate(a)]
    for j in range(n):
        p=next(i for i in range(j,n) if b[i][j])
        b[p],b[j]=b[j],b[p]
        v=b[j][j];b[j]=[x/v for x in b[j]]
        for i in range(n):
            if i!=j:
                v=b[i][j];b[i]=[x-v*y for x,y in zip(b[i],b[j])]
    return [r[n:] for r in b]
def mat(a):return [[str(x) for x in r] for r in a]
I2=diag([1,1]);I4=diag([1]*4);I8=diag([1]*8);Z2=diag([0,0]);Z4=diag([0]*4)
f=[[Q(0),Q(3,5)],[Q(3,5),Q(0)]]
Fhat=[[f[i][j] if i<2 and j<2 else -f[i-2][j-2] if i>=2 and j>=2 else Q(4,5)*I2[i%2][j%2] for j in range(4)] for i in range(4)]
Ghat=diag([1,-1,-1,1])
Wm=[[Q(1),Q(0),Q(0),Q(0)],[Q(0),Q(0),Q(0),Q(1)],Fhat[0],Fhat[3]]
J=[[Q(int(i//2!=j//2 and i%2==j%2)) for j in range(4)] for i in range(4)]
assert tr(Fhat)==Fhat and mm(Fhat,Fhat)==I4 and add(mm(Fhat,Ghat),mm(Ghat,Fhat))==Z4
assert mm(Wm,tr(Wm))==I4 and mm(tr(Wm),Wm)==I4
assert mm(mm(Wm,Fhat),tr(Wm))==J and mm(mm(Wm,Ghat),tr(Wm))==diag([1,1,-1,-1])
source_identity=mm(mm(Wm,block(I2,Z2)),tr(Wm))
assert mm(source_identity,source_identity)==source_identity
assert sum(source_identity[i][i] for i in range(4))==2
samples=[[[Q(int(r==i and c==j)) for c in range(2)] for r in range(2)] for i in range(2) for j in range(2)]
def phi(b):return mm(mm(Wm,block(b,Z2)),tr(Wm))
products=[]
for i,b in enumerate(samples):
    for j,c in enumerate(samples):
        assert mm(phi(b),phi(c))==phi(mm(b,c))
        products.append(dict(left=i,right=j,exact_product=True))
resolvents=[]
dh=scale([[Q(1),Q(1,4)],[Q(1,4),Q(-1)]],Q(1,32))
D=block(dh,dh);DJ=block(J,J);DD=block(D,D)
noncommuting=[]
for x in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:
    h=scale([[2+x,x/4],[x/4,3-x]],Q(1,32))
    det=h[0][0]*h[1][1]-h[0][1]*h[1][0]
    assert det>=Q(63,16*32**2) and h[0][0]>0
    noncommuting.append(dict(x=str(x),commutator=mat(add(mm(h,dh),mm(dh,h),-1))))
    H0=block(h,h);HH=block(H0,H0)
    for lam in [1,2,4]:
        B=[[(J[i][j] if i<4 and j<4 else J[i-4][j-4] if i>=4 and j>=4 else -lam*H0[i][j-4] if i<4 else lam*H0[i-4][j]) for j in range(8)] for i in range(8)]
        dB=[[(Q(0) if i//4==j//4 else -lam*D[i][j-4] if i<4 else lam*D[i-4][j]) for j in range(8)] for i in range(8)]
        Bi=inv(B);assert mm(B,Bi)==I8 and mm(Bi,B)==I8
        direct=add(mm(DD,Bi),mm(mm(mm(HH,Bi),dB),Bi),-1)
        ordered=mm(mm(mm(DJ,Bi),DD),Bi)
        assert direct==ordered
        resolvents.append(dict(x=str(x),lambda_value=lam,exact_left_and_right_inverse=True,exact_derivative_order=True,determinant=str(det)))
assert any(any(any(x for x in r) for r in [[Q(x) for x in r] for r in v['commutator']]) for v in noncommuting)
checks=dict(schema="parallel-normal-inverse-checks/v1",field="Q",normalized_phase=mat(Fhat),normalization_unitary=mat(Wm),flattened_phase=mat(J),transformed_source_identity=mat(source_identity),source_identity_rank=2,total_dimension=4,zero_source_subspace_retained=True,exact_normalization_and_grading=True,source_products=products,normal_resolvent_tests=resolvents,noncommuting_h_derivative=noncommuting,all_fraction_checks=True,actual_entire_B_source_class_retained_by_proof=True,actual_invariant_phase_parallel_connection_proved=True,actual_completed_normal_resolvent_preservation_proved=True,dense_normal_compatible_full_operator_core_proved=True,joint_domain_dense_proved=True,source_nondegeneracy_restored=False,full_joint_graph_core_proved=False,full_unbounded_B_source_commutators_proved=False,full_unbounded_arrow_domain_preservation_proved=False,source_essential_normal_compression_proved=False,original_physical_graph_sum_proved=False,original_Bott_comparison_proved=False,finite_model_proves_original_inverse=False,canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"parallel-normal-inverse.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"parallel-normal-inverse.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"PARALLEL-NORMAL-INVERSE-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(source_products=len(products),exact_normal_resolvent_tests=len(resolvents),source_rank=2,overflows=overflow)))
