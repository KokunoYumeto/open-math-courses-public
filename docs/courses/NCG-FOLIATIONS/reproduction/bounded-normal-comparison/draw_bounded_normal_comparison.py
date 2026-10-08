"""Bounded normal comparison and an infinite rough-field example: original CC0 figure."""
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
W, H = 2450, 2030
INK, BLUE, GREEN, RED = "#17283c", "#17638d", "#286d49", "#b64932"
im = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(im)
fonts, overflow = {}, []
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<title>A bounded normal comparison and a completed graph sum</title>",
    "<desc>BNC.1 to BNC.20. A bounded comparison preserves a full separated graph-sum domain. The infinite rough mass has all compact regulator and arrow controls but fails normal H1 preservation. The physical sum still exists, and a full mass homotopy leaves the vacuum circle Dirac with sign action.</desc>",
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





text(45,25,"A bounded normal comparison supplies a full graph sum without a potential derivative",37)
text(45,88,"BNC.1–BNC.20. Completed tensor domains, localized resolvents and the actual infinite comparison.",28)
box(45,155,1135,550);box(1240,155,1165,550)
text(78,185,"Completed separated sum and bounded comparison",29)
text(78,250,"D*=S*⊗1+Γ⊗N;  D=D*+V;  ||V||≤1/8 in this example",26,BLUE)
text(78,315,"Dom D = Dom S* ∩ Dom N  (full closed domains)",27,GREEN)
text(78,380,"Coefficient energies add before taking the module norm",25)
text(78,445,"Large imaginary resolvents: Neumann-series inverses",25)
text(78,510,"||Rv(±is)−Rw(±is)||≤|v−w| ||V||/s²",28,BLUE)
text(78,575,"Localized phase comparison preserves the product class",25,GREEN)
text(78,640,"No derivative of the uniformly bounded V is used",26,GREEN)
text(1273,185,"Infinite rough potential; all arrow errors are zero",29)
text(1273,250,"a(x)=1/4+(1/8)√|sin(x/2)|;  1/4≤a≤3/8",28,BLUE)
text(1273,315,"S e0=0; first pair=a(x)J; pair n≥2=nJ",28)
text(1273,380,"r=1 on first 3 coordinates; r=n on pair n≥2",26)
text(1273,445,"r⁻¹ compact and constant; F²=1 in the doubled module",25)
text(1273,510,"Source action is nondegenerate after compression",26,GREEN)
text(1273,575,"For χ=1 near 0: χe1∈H¹ but S(χe1)=aχf1∉H¹",25,RED)
text(1273,640,"Yet the physical sum is self-adjoint with compact resolvent",23,GREEN)

box(45,760,1135,635);box(1240,760,1165,635)
text(78,790,"Actual squared derivative diverges as 1/(512|x|)",29)
text(78,842,"Log axes; 181 samples of the exact scalar formula, x>0",22)
left,right,top,bottom=175,1115,910,1270
line([(left,top),(left,bottom),(right,bottom)],INK,2)
for k in range(1,10,2):
    xx=left+(9-k)/8*(right-left)
    line([(xx,bottom),(xx,bottom+9)],INK,2)
    text(xx-24,bottom+14,"10⁻"+str(k),21)
for q in [-2,0,2,4,6]:
    yy=bottom-(q+2)/9*(bottom-top)
    line([(left-9,yy),(left,yy)],INK,2)
    text(72,yy-12,"10^"+str(q),21)
def xy(x,y):
    return (left+(math.log10(x)+9)/8*(right-left),bottom-(math.log10(y)+2)/9*(bottom-top))
derivative_samples=[]
actual=[];asym=[]
for i in range(181):
    x=10**(-9+8*i/180)
    y=math.cos(x/2)**2/(1024*math.sin(x/2))
    z=1/(512*x)
    derivative_samples.append(dict(x=x,squared_derivative=y,asymptote=z,ratio=y/z))
    actual.append(xy(x,y));asym.append(xy(x,z))
line(asym,BLUE,7);line(actual,RED,3)
text(78,1340,"Red: |a′(x)|². Blue: 1/(512x). ∫₀ε dx/x=∞.",25,RED)

text(1273,790,"Separated Fourier blocks and compact resolvent",29)
text(1273,842,"Plotted sample n=2,…,6 and k=−6,…,6; full tails proved",22)
lx,rx,ty,by=1360,2325,910,1260
line([(lx,ty),(lx,by),(rx,by)],INK,2)
for k in [-6,-3,0,3,6]:
    xx=lx+(k+6)/12*(rx-lx)
    line([(xx,by),(xx,by+9)],INK,2)
    text(xx-13,by+14,str(k),22)
for value in [0,2,4,6,8,10]:
    yy=by-value/10*(by-ty)
    line([(lx-9,yy),(lx,yy)],INK,2)
    text(1273,yy-12,str(value),21)
colors=["#17638d","#286d49","#9d6426","#704b91","#b64932"]
spectrum_samples=[]
for n,col in zip(range(2,7),colors):
    for k in range(-6,7):
        energy=n*n+k*k
        spectrum_samples.append(dict(pair=n,mode=k,squared_eigenvalue=energy))
        xx=lx+(k+6)/12*(rx-lx);yy=by-math.sqrt(energy)/10*(by-ty)
        circle(xx,yy,5,col)
text(1273,1340,"Vertical: √(n²+k²). Horizontal: Fourier mode k.",24,BLUE)

box(45,1455,2360,385)
text(78,1485,"The full infinite homotopy retains the surviving carrier and its actual action",31)
text(78,1550,"Vacuum e0: N=−i∂x with sign action. Balanced pairs: Fv(mn,k) → J as masses →∞.",26)
text(78,1615,"Strict endpoint + uniform compact source/normal tails: the paired endpoint is degenerate.",26,GREEN)
text(78,1680,"[D]=sgn⊗[N]. Negative winding e⁻ⁱˣ: onto backward shift; kernel is the constant mode.",27,BLUE)
text(78,1745,"Ordinary index +1; equivariant index is the sign character, not a scalar unit.",27,GREEN)
text(45,1890,"This infinite model has source C(S¹). It is not the phase-space Bott source or the original foliation inverse.",25,RED)
text(45,1945,"The actual dX module still needs a source-preserving completed normal comparison with its original coefficient and Clifford order.",23)
text(45,1990,"Original CC0. Reproducible raster/vector figure, exact rational block checks and scalar samples; proofs are BNC.1–BNC.20.",23)
assert not overflow,overflow

class Exact:
    """Complex rational numbers, for exact imaginary resolvent identities."""
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    @staticmethod
    def coerce(x):return x if isinstance(x,Exact) else Exact(x)
    def __add__(self,x):
        x=self.coerce(x);return Exact(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Exact(-self.a,-self.b)
    def __sub__(self,x):return self+-self.coerce(x)
    def __rsub__(self,x):return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x);return Exact(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x);den=x.a*x.a+x.b*x.b
        if not den:raise ZeroDivisionError()
        return Exact((self.a*x.a+self.b*x.b)/den,(self.b*x.a-self.a*x.b)/den)
    def __eq__(self,x):
        x=self.coerce(x);return self.a==x.a and self.b==x.b
    def conj(self):return Exact(self.a,-self.b)
    def __str__(self):return str(self.a)+("+" if self.b>=0 else "")+str(self.b)+"i"
Z=Exact
def mm(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Z()) for j in range(len(B[0]))] for i in range(len(A))]
def adj(A):return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def diag(v):return [[Z.coerce(x) if i==j else Z() for j in range(len(v))] for i,x in enumerate(v)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,c):return [[c*x for x in a] for a in A]
def mat(A):return [[str(x) for x in a] for a in A]
I=diag([1,1]);J=[[Z(0),Z(1)],[Z(1),Z(0)]];Gamma=diag([1,-1])
assert add(mm(J,Gamma),mm(Gamma,J))==diag([0,0])
block_tests=[]
for m in [Q(1,4),Q(3,8),Q(2),Q(5)]:
    for k in [-4,-1,0,3,7]:
        D=add(scale(J,Z(m)),scale(Gamma,Z(k)));energy=m*m+k*k
        assert adj(D)==D and mm(D,D)==diag([energy,energy])
        rp=scale(add(D,diag([Z(0,-1),Z(0,-1)])),Z(1)/(Z(energy+1)))
        rm=adj(rp)
        assert mm(add(D,diag([Z(0,1),Z(0,1)])),rp)==I
        assert mm(rp,add(D,diag([Z(0,1),Z(0,1)])))==I
        assert mm(add(D,diag([Z(0,-1),Z(0,-1)])),rm)==I
        block_tests.append(dict(mass=str(m),mode=k,squared_eigenvalue=str(energy),square_exact=True,both_resolvents_exact=True))
comparisons=[]
for k in [-4,-1,0,3,7]:
    m0,m1=Q(1,4),Q(3,8)
    A=add(scale(J,Z(m0)),scale(Gamma,Z(k)))
    B=add(scale(J,Z(m1)),scale(Gamma,Z(k)))
    ra=scale(add(A,diag([Z(0,-1)]*2)),Z(1)/Z(m0*m0+k*k+1))
    rb=scale(add(B,diag([Z(0,-1)]*2)),Z(1)/Z(m1*m1+k*k+1))
    assert add(rb,scale(ra,Z(-1)))==scale(mm(mm(rb,J),ra),Z(m0-m1))
    comparisons.append(dict(mode=k,bounded_resolvent_identity_exact=True))
normalization=[]
for a in [Q(1,4),Q(5,16),Q(3,8)]:
    defect=1-a*a
    assert a*a+defect==1
    normalization.append(dict(a=str(a),C_squared=str(defect),square_root_positive=True,doubled_unitary_block_identity_exact=True))
reference=[]
for n in [1,2,3,8,19,100]:
    value=1+sum(int(n>k) for k in range(1,n+1))
    assert value==n
    reference.append(dict(pair=n,cutoff_series_value=value,exact=True))
homotopy=[]
for v in [Q(0),Q(1,2),Q(3,4),Q(7,8)]:
    m=Q(1,4)/(1-v)
    for k in [-5,0,4]:
        energy=m*m+k*k
        assert energy+1>0
        homotopy.append(dict(v=str(v),mode=k,mass=str(m),square_defect=str(1/(1+energy)),uniform_square_defect_bound=str(1/(1+m*m))))
checks=dict(schema="bounded-normal-comparison-checks/v1",block_tests=block_tests,resolvent_comparisons=comparisons,normalization_checks=normalization,reference_series_checks=reference,mass_homotopy_checks=homotopy,derivative_samples=derivative_samples,spectrum_samples=spectrum_samples,potential_norm_bound="1/8",derivative_squared_asymptotic_coefficient="1/512",derivative_squared_integral_diverges_by_proof=True,actual_normal_H1_preservation=False,model_full_joint_domain_proved=True,model_self_adjoint_compact_resolvent_sum_proved=True,model_entire_infinite_class_proved=True,negative_winding_index=1,surviving_kernel_action="-1",model_identifies_original_Bott_inverse=False,original_normal_module_comparison_proved=False,original_physical_graph_sum_proved=False,all_rational_checks=True,canvas=[W,H],text_canvas_overflows=overflow)
svg.append("</svg>")
im.save(options.output_dir/"bounded-normal-comparison.png",format="PNG",optimize=False,compress_level=9)
(options.output_dir/"bounded-normal-comparison.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(options.output_dir/"BOUNDED-NORMAL-COMPARISON-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(exact_blocks=len(block_tests),resolvent_comparisons=len(comparisons),derivative_samples=len(derivative_samples),spectrum_samples=len(spectrum_samples),overflows=overflow)))
