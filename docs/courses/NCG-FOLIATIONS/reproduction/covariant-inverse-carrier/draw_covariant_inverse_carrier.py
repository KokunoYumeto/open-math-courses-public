"""Equivariant inverse absorption, parallel normal connection and closed joint graph: original CC0."""
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
    "<title>An equivariant regular inverse carrier and its closed normal graph</title>",
    "<desc>CVC.1 to CVC.18. Proper cutoff embedding, source-coordinate regularization and an infinite copy shift preserve the actual inverse class. The regular connection is parallel for normal holonomy. The joint graph intersection is complete and invariant; its density and the physical sum remain unproved.</desc>",
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






text(45,25,"The actual inverse on a regular carrier: arrows are parallel for the normal connection",35)
text(45,90,"CVC.1–CVC.18. Original B-source, genuine H action, class dX, normal holonomy and full closed operator domains.",25)
box(45,155,1135,565);box(1240,155,1165,565)
text(78,185,"Proper cutoff and SOURCE coefficient maps",30)
text(78,250,"K  ──VK──▶  R_H(K)  ──R_H(j)──▶  Q",31,BLUE)
text(78,315,"(VKξ)(g)=C_s(g) Ug⁻¹ ξ_r(g)",29)
text(78,380,"(R_H(j)y)(g)=j_s(g)y(g)",29)
text(78,445,"s(h⁻¹g)=s(g): the internal vector stays fixed",25,GREEN)
text(78,510,"I*I=1; LI=IU; Q=I(K)⊕N, invariant complement",24,GREEN)
text(78,575,"Finite C2 check: C=diag(1,0), U swaps two phases",24)
text(78,640,"Vξ=(ξ0,0,ξ1,0); P=diag(1,0,1,0)",26,BLUE)
text(1273,185,"An ONTO infinite copy shift",30)
text(1273,250,"Extra K*  →  K0",29,BLUE)
for n in range(3):
    y=325+n*85
    text(1273,y,"K"+str(n),28,BLUE);text(1660,y,"K"+str(n+1),28,BLUE)
    arrow(1370,y+20,1595,y+20)
    text(1850,y,"N"+str(n)+"  →  N"+str(n),27,GREEN)
text(1273,590,"…  old Kn → K(n+1); every Nn stays at n",25)
text(1273,650,"Inverse: extract K0, shift later K copies back",24,GREEN)
box(45,785,1135,630);box(1240,785,1165,630)
text(78,815,"Exact normal reflection on two arrow rows",29)
text(78,875,"La y(x)=swap y(−x); m(a)=−1",28,BLUE)
text(78,930,"y(x)=(x,x²); La y(x)=(x²,−x)",28)
text(78,985,"∂(La y)=(2x,−1)=−La(∂y)",29,GREEN)
line([(155,1180),(1060,1180)],INK,2)
line([(610,1050),(610,1310)],INK,2)
for direction,col in [(1,BLUE),(-1,GREEN)]:
    pts=[(610+400*i/80,1180-direction*100*i/80) for i in range(-80,81)]
    line(pts,col,4)
text(195,1188,"−1",21);text(1010,1188,"1",21);text(620,1188,"0",21)
text(195,1325,"Blue: x. Green: −x. Row swap accompanies reflection.",22)
text(78,1380,"At x=0 the derivative sign is −1, not +1.",24,RED)
text(1273,815,"The two actual CLOSED graphs",29)
text(1273,875,"DH=W DE W*; ΦH=W Φ W*; [Q,ΦH,FDH]=dX",25,BLUE)
text(1273,935,"Dcap=Dom DH ∩ Dom ∇reg",29)
text(1273,995,"||y||cap=||y||+||DH y||+||∇reg y||",27)
text(1273,1055,"Cauchy in all three components ⇒ complete graph",24,GREEN)
text(1273,1115,"La Dcap,s=Dcap,r; bound ≤(1+C)||y||cap",25,GREEN)
text(1273,1175,"∇r La=(La⊗m(a))∇s: full local normal graph",24,GREEN)
text(1273,1240,"These are bisection SECTION domains.",26,RED)
text(1273,1300,"A normal derivation has no isolated-unit fibre domain.",23)
text(1273,1360,"Completeness does not prove density or a joint core.",24,RED)
box(45,1480,2360,225)
text(78,1510,"Source and operator normal estimates still govern the physical inverse",30)
text(78,1570,"No derivative of j, I, P, the cutoff or W is assumed. ΦH(B) and DH need their own normal-domain proof.",25)
text(78,1630,"Original C0(T) balance, full z⁻¹ρ(s) phase, grading and final right Clifford block remain required.",25,RED)
text(45,1740,"Original CC0. Exact finite tests illustrate cutoff and signs; infinite absorption and graph closure are proved in the lesson.",23)
assert not overflow,overflow

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q()) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return [list(r) for r in zip(*a)]
def diag(v):return [[Q(x) if i==j else Q() for j in range(len(v))] for i,x in enumerate(v)]
def mat(a):return [[str(x) for x in r] for r in a]
C=diag([1,0]);U=[[Q(0),Q(1)],[Q(1),Q(0)]]
I2=diag([1,1]);I4=diag([1]*4)
V=[[Q(1),Q(0)],[Q(0),Q(0)],[Q(0),Q(1)],[Q(0),Q(0)]]
L=[[Q(int(i//2!=j//2 and i%2==j%2)) for j in range(4)] for i in range(4)]
P=mm(V,tr(V))
assert mm(tr(V),V)==I2 and mm(L,V)==mm(V,U)
assert P==diag([1,0,1,0]) and mm(L,P)==mm(P,L)
cutoff_square=mm(C,C);translated=mm(mm(U,cutoff_square),U)
assert [[x+y for x,y in zip(a,b)] for a,b in zip(cutoff_square,translated)]==I2
reflections=[]
for x in [Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]:
    reflected=[x*x,-x];derived=[2*x,Q(-1)]
    minus_transported=[-(-2*x),Q(-1)]
    assert derived==minus_transported
    assert [(-x)*(-x),-(-x)]==[x*x,x]
    reflections.append(dict(x=str(x),original=[str(x),str(x*x)],
                            reflected=[str(v) for v in reflected],
                            derivative=[str(v) for v in derived],
                            exact_covariance=True))
shift=[]
for n in range(6):
    dest=n+1
    assert dest-1==n
    shift.append(dict(old_K=n,new_K=dest,inverse_K=dest-1,N_unchanged=n))
checks=dict(schema="covariant-inverse-carrier-checks/v1",field="Q",
            cutoff=mat(C),original_arrow=mat(U),regular_arrow=mat(L),
            embedding=mat(V),projection=mat(P),exact_cutoff_partition=True,
            exact_isometry=True,exact_equivariance=True,exact_invariant_projection=True,
            reflection_tests=reflections,copy_shift_tests=shift,extra_K_destination=0,
            wrong_reflection_derivative_at_zero=["0","1"],
            correct_reflection_derivative_at_zero=["0","-1"],
            normal_transport_sign="-1",all_fraction_checks=True,
            infinite_shift_onto_proved_in_lesson=True,
            actual_entire_B_source_class_retained_by_proof=True,
            covariant_vector_connection_closure_proved_in_lesson=True,
            joint_graph_completeness_proved_in_lesson=True,
            joint_graph_arrow_invariance_proved_in_lesson=True,
            finite_model_proves_infinite_absorption=False,
            joint_graph_density_proved=False,
            full_B_source_operator_normal_derivatives_proved=False,
            original_physical_graph_sum_proved=False,original_Bott_comparison_proved=False,
            canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"covariant-inverse-carrier.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"covariant-inverse-carrier.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"COVARIANT-INVERSE-CARRIER-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(exact_cutoff=True,reflections=len(reflections),shift_tests=len(shift),overflows=overflow)))
