"""Original CC0 geometry and exact auxiliary checks for MGS.1–MGS.16."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import argparse, base64, html, io, json

HERE = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument("--resources", type=Path, default=HERE.parent / "labelled-geometric-kernel")
p.add_argument("--output-dir", type=Path, default=HERE / "generated")
opts = p.parse_args()
opts.output_dir.mkdir(parents=True, exist_ok=True)
font = (opts.resources / "fonts/DejaVuSans.ttf").read_bytes()
notice = (opts.resources / "FONT-NOTICE.txt").read_text(encoding="utf-8")
W,H = 1800,1310
im = Image.new("RGB",(W,H),"#f7fafc")
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
       '<metadata>'+html.escape(notice)+'</metadata>',
       '<style>@font-face{font-family:LocalSans;src:url(data:font/ttf;base64,'+
       base64.b64encode(font).decode()+')}text{font-family:LocalSans}</style>',
       f'<rect width="{W}" height="{H}" fill="#f7fafc"/>']
fonts = {}
overflow = []

def text(x,y,s,size=24,col="#17334d"):
    if size not in fonts:
        fonts[size]=ImageFont.truetype(io.BytesIO(font),size,layout_engine=ImageFont.Layout.BASIC)
    box=d.textbbox((x,y),s,font=fonts[size],anchor="lt")
    if box[0]<0 or box[1]<0 or box[2]>W-12 or box[3]>H-12:
        overflow.append(s)
    d.text((x,y),s,font=fonts[size],fill=col,anchor="lt")
    svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" dominant-baseline="text-before-edge">{html.escape(s)}</text>')

def rect(x,y,w,h,fill="#fff",edge="#c7d7e2"):
    d.rectangle((x,y,x+w,y+h),fill=fill,outline=edge,width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{edge}" stroke-width="2"/>')

def line(points,col="#527489",width=3):
    d.line(points,fill=col,width=width)
    svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{col}" stroke-width="{width}"/>')

def ellipse(x,y,rx,ry,fill="none",col="#527489",width=3):
    d.ellipse((x-rx,y-ry,x+rx,y+ry),fill=None if fill=="none" else fill,outline=col,width=width)
    svg.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{col}" stroke-width="{width}"/>')

text(40,28,"Physical normal Dirac on actual matrix-group suspension columns",34)
text(40,83,"MGS.1–MGS.16  |  original inverse, scalar compactness and source-oriented Bott +1",25)
rect(40,139,1720,179)
text(62,159,"G = (Lhat × Lhat × N) / Γ     →     G|T = Γ ⋉ N     →     G|sT = Lhat × N",29)
text(62,208,"Chart label t and normal point n_i:  (y,n) = (t⁻¹ z_i(x), t⁻¹ n_i)",26)
text(62,254,"Overlap (t,n_i) ↦ (ht,hn_i) leaves the actual source column unchanged.",25)
rect(40,340,820,438,"#eaf4fa")
rect(890,340,870,438,"#eaf7ed")
text(62,360,"Irrational sphere rotation: fixed poles retain germs",27)
ellipse(234,575,140,140)
ellipse(234,575,140,40)
line([(234,418),(234,732)],"#91a4b2",2)
ellipse(234,435,7,7,"#bf4b52","#bf4b52")
ellipse(234,715,7,7,"#bf4b52","#bf4b52")
text(252,421,"north",20)
text(252,706,"south",20)
text(403,430,"θ = 2πα,   α ∉ Q",26)
text(403,482,"k fixes each pole.",25)
text(403,531,"Its derivative rotates",24)
text(403,570,"by kθ; k ≠ 0 gives",24)
text(403,609,"a nonidentity germ.",24)
text(403,666,"Pole isotropy: Z",25)
text(403,708,"Holonomy cover: R",25)
text(912,360,"Regular auxiliary with one positive root",27)
text(912,406,"D⁺ e_n = −n e_n (n<0);   n e_(n−1) (n>0)",23)
coords={n:980+110*(n+3) for n in range(-3,4)}
for n,x in coords.items():
    ellipse(x,490,9,9,"#bf4b52" if n==0 else "#347a6c",
            "#bf4b52" if n==0 else "#347a6c")
    text(x-26,452,f"e{n}⁺",20)
for n in range(-3,3):
    x=coords[n]
    ellipse(x,642,9,9,"#347a6c","#347a6c")
    text(x-26,669,f"e{n}⁻",20)
for n in [-3,-2,-1,1,2,3]:
    source=coords[n];target=coords[n if n<0 else n-1]
    line([(source,505),(target,627)],"#347a6c")
    text((source+target)//2+7,552,str(abs(n)),21)
text(912,720,"Unpaired e0⁺: index +1;   ||[D,V]|| = √2",25)
rect(40,805,1720,395,"#fff7e9")
text(62,825,"The entire original normal inverse stays in the physical operator",28)
text(62,877,"Π^(q(q−1)/2) C_q   |   full lift z⁻¹ ρ_t(s)   |   dual determinant   |   right C_q last",26)
text(62,930,"D_B = D_K ⊗ 1 + γ_K ⊗ D_N;     D_G = P D₀ P on P Dom(D₀)",27)
text(62,984,"Dom(D_B) = Dom(D_K ⊗ 1) ∩ Dom(1 ⊗ D_N);     σ_⊥² = |ξ|²",26)
text(62,1037,"Leaf convolution × normal/auxiliary resolvent is an ordinary scalar compact.",25)
text(62,1090,"Actual normalized bump:   E* ≅ pA;    restriction = [D_N];    (i_* b_U) z_G = 1",25)
text(62,1143,"All return labels, point stabilizers, complete domains and inverse phases are retained.",25)
text(42,1231,"A global compact suspension is proved here. Compatible physical operators for arbitrary holonomy still remain.",23)
text(42,1271,"Sphere schematic; exact auxiliary pairing. Infinite proofs and full domain arguments are in Section 11BI.",22)
assert not overflow,overflow

def plus(n):
    return {} if n==0 else {n if n<0 else n-1:abs(n)}
def minus(m):
    return {m if m<0 else m+1:-m if m<0 else m+1}
def shifted(v):
    return {i+1:a for i,a in v.items()}
def sub(a,b):
    keys=set(a)|set(b)
    return {i:a.get(i,0)-b.get(i,0) for i in sorted(keys) if a.get(i,0)!=b.get(i,0)}

samples=[]
for n in range(-6,7):
    cp=sub(plus(n+1),shifted(plus(n)))
    cm=sub(minus(n+1),shifted(minus(n)))
    expected_p={n+1:-1} if n<=-2 else ({0:-1} if n==-1 else ({0:1} if n==0 else {n:1}))
    expected_m={n+1:-1} if n<=-2 else ({0:-1,1:1} if n==-1 else {n+2:1})
    assert cp==expected_p and cm==expected_m
    samples.append(dict(input=n,positive_commutator=cp,negative_commutator=cm,
                        positive_image=plus(n),negative_image=minus(n)))
checks=dict(schema="matrix-suspension-exact-checks/v1",
            mathematical_locators=[f"MGS.{i}" for i in range(1,17)],
            figure_dimensions=[W,H],bounded_text_overflow=[],
            exact_commutator_samples=samples,
            exceptional_positive_gram=[[1,-1],[-1,1]],
            exceptional_gram_trace=2,exceptional_gram_determinant=0,
            exceptional_negative_column_norm_squared=2,
            commutator_norm_squared=2,
            auxiliary_kernel_positive=["e0"],auxiliary_kernel_negative=[],
            scalar_index=1,
            finite_checks_prove_infinite_selfadjointness=False,
            finite_checks_prove_irrational_germ_faithfulness=False,
            finite_checks_prove_general_holonomy=False,
            complete_proof="K-theory of the leaf space, Section 11BI and Exercises 282–283",
            sphere_geometry="Schematic of the rotation action; no numerical Dirac spectrum claimed",
            original_expression_license="CC0-1.0",
            font_notice="Exact retained DejaVu notice from the shared reproduction resources")
im.save(opts.output_dir/"matrix-suspension-dirac.png",optimize=True)
svg.append("</svg>")
(opts.output_dir/"matrix-suspension-dirac.svg").write_text("\n".join(svg)+"\n",encoding="utf-8",newline="\n")
(opts.output_dir/"MATRIX-SUSPENSION-CHECKS.json").write_text(json.dumps(checks,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
