"""Reproduce the original JD/FQ domain and cross-form figure. CC0.

Reads the shared DejaVu font and notice without copying them. If the
shared font is absent, recovers their bytes from this figure's SVG.
Needs Python and Pillow; uses Decimal for the endpoint samples.
"""
from pathlib import Path
from decimal import Decimal, localcontext
from fractions import Fraction
from io import BytesIO
import argparse, base64, html, json, math, re
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=HERE/'out')
parser.add_argument('--resources',type=Path,default=HERE.parent/'labelled-geometric-kernel')
args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
FONT=args.resources/'fonts/DejaVuSans.ttf'
NOTICE=args.resources/'FONT-NOTICE.txt'
SVG=args.output_dir/'joint-domains-cross-form.svg'
PNG=args.output_dir/'joint-domains-cross-form.png'
W, H = 1840, 1500
COLORS = dict(bg="#f4f6fa", ink="#14233d", muted="#415571",
              blue="#2057a0", green="#196542", red="#a23838",
              panel="#ffffff", grid="#ccd5e3", pale="#e9eef7")

def read_font():
    return FONT.read_bytes(), NOTICE.read_text(encoding='utf-8')


def endpoint(n):
    with localcontext() as c:
        c.prec = 100
        e = Decimal(2) ** (-n**3)
        r = (1-e*e).sqrt()
        A = Decimal(3)/2-e*e/2+e**4/2
        B = r**3*e/2
        C = 2*e*e-e**4/2
        delta = (A*C-B*B).sqrt()
        ratio = (e*(A*A+delta*A-B*B)-r*B*(2*A+delta))/(delta*(A+C+2*delta).sqrt())
        return e, ratio

def exact_checks():
    checks=[]
    for n in range(1, 6):
        e=Fraction(1, 2**(n**3)); z=e*e
        A=Fraction(3,2)-z/2+z*z/2
        C=2*z-z*z/2
        B2=(1-z)**3*z/4
        det=A*C-B2
        assert A>0 and det>0
        # The exact finite block determinant has no irrational r.
        assert det == (11*z-4*z*z+2*z*z*z)/4
        ed, val=endpoint(n)
        checks.append(dict(n=n, epsilon=str(e), determinant=str(det),
                           sampled_preimage_en=float(val)))
    return checks

def render():
    font_bytes, notice = read_font()
    im=Image.new("RGB", (W,H), COLORS["bg"]); d=ImageDraw.Draw(im)
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
      '<title>Completed inverse-power domains and oscillator cross forms</title>',
      '<desc>Exact JD.1 to JD.23 and FQ.1 to FQ.8. The half-power failure is an auxiliary smooth C2 example, not a foliation counterexample.</desc>',
      f'<metadata id="font-notice">{html.escape(notice)}</metadata>',
      f'<style>@font-face{{font-family:JD;src:url(data:font/ttf;base64,{base64.b64encode(font_bytes).decode()})}}text{{font-family:JD,sans-serif}}</style>',
      f'<rect width="{W}" height="{H}" fill="{COLORS["bg"]}"/>']
    fonts={}
    def f(size):
        if size not in fonts: fonts[size]=ImageFont.truetype(BytesIO(font_bytes),size)
        return fonts[size]
    def text(x,y,s,size=25,color="ink"):
        color=COLORS.get(color,color)
        d.text((x,y),s,font=f(size),fill=color)
        parts.append(f'<text x="{x}" y="{y+size}" font-size="{size}" fill="{color}">{html.escape(s)}</text>')
    def rect(x,y,w,h,fill="panel",outline="grid",radius=16):
        fill=COLORS.get(fill,fill); outline=COLORS.get(outline,outline)
        d.rounded_rectangle((x,y,x+w,y+h),radius,fill=fill,outline=outline,width=2)
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{outline}" stroke-width="2"/>')
    def line(points,color="blue",width=3):
        color=COLORS.get(color,color); d.line(points,fill=color,width=width)
        parts.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    def arrow(x1,y1,x2,y2,color="blue"):
        line([(x1,y1),(x2,y2)],color,4)
        angle=math.atan2(y2-y1,x2-x1)
        pts=[(x2,y2),(x2-15*math.cos(angle-.45),y2-15*math.sin(angle-.45)),
             (x2-15*math.cos(angle+.45),y2-15*math.sin(angle+.45))]
        d.polygon(pts,fill=COLORS[color]); parts.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in pts)}" fill="{COLORS[color]}"/>')

    text(55,30,"Completed domains: the orbit compact and the normal cross form",36)
    text(55,82,"Actual IJ/CW coefficient field; original G/T/C0(T), full inverse Spin-c factor and final right Clifford order",23,"muted")
    rect(45,137,1750,416)
    text(70,158,"JD.1–JD.6  One real K-invariant smooth compact",29,"blue")
    rect(83,225,425,190,"pale")
    text(106,243,"h0: all normal jet columns",25)
    text(106,284,"Phi = sum a_i Phi_i,  sum a_i < 1",23)
    text(106,323,"Phi_i uses actual cutoff arrows",23)
    text(106,362,"h = sum Phi^n(h0) = S S*",25)
    arrow(520,317,664,317)
    rect(680,223,510,247,"panel","green")
    text(703,244,"0 < alpha < 1/2",29,"green")
    text(703,290,"Dom h^(-alpha) = Ran h^alpha",25)
    text(703,337,"actual G transport + displacement",24)
    text(703,380,"completed continuous graph sections",24)
    text(703,423,"Strict limits prove the range equality",22,"muted")
    line([(520,236),(550,210),(1296,210),(1310,244)],"blue",4)
    arrow(1310,244,1320,244)
    rect(1324,223,433,247,"panel","green")
    text(1343,244,"k = sqrt(h)",29,"green")
    text(1343,290,"partial k is compact",25)
    text(1343,337,"Theta = k^(-1)",25)
    text(1343,380,"infinitesimal normal form",24)
    text(1343,423,"Different inverse power!",23,"red")
    text(83,492,"Order comparison at alpha = 1/2 does not prove a completed module domain. Exact example below.",25,"red")

    rect(45,580,845,532)
    text(70,603,"JD.7  Smooth C2 endpoint example",29,"blue")
    text(70,650,"h = a + (1/2) P a P;  (1/2) h <= P h P <= 2 h",23)
    text(70,690,"u = h e0 is in Ran sqrt(h);  P u is not",25,"red")
    text(70,733,"Coefficient of e_n in the unique fibre preimage",22,"muted")
    # Graph shows samples; the analytic limit is proved in JD.23.
    left,top,right,bottom=134,795,823,1004
    line([(left,top),(left,bottom),(right,bottom)],"muted",2)
    for value in (.0,.2,.4,.6,.8):
        yy=bottom-value/.85*(bottom-top)
        line([(left,yy),(right,yy)],"grid",1); text(78,yy-15,f"{value:.1f}",19,"muted")
    lim=math.sqrt(3/22); yy=bottom-lim/.85*(bottom-top)
    line([(left,yy),(right,yy)],"green",3)
    text(345,yy-31,"proved limit sqrt(3/22) > 0",21,"green")
    points=[]
    for n in range(1,6):
        value=float(endpoint(n)[1]); xx=left+(n-1)*(right-left)/4
        yy=bottom-value/.85*(bottom-top); points.append((xx,yy))
        d.ellipse((xx-6,yy-6,xx+6,yy+6),fill=COLORS["blue"])
        parts.append(f'<circle cx="{xx}" cy="{yy}" r="6" fill="{COLORS["blue"]}"/>')
        text(xx-5,bottom+9,str(n),19,"muted")
    line(points,"blue",2)
    text(680,1038,"n (samples)",19,"muted")
    text(70,1070,"x_n -> 0, but the escaping e_n amplitude does not vanish.",22,"red")

    rect(922,580,873,532)
    text(949,603,"FQ.1–FQ.3  Completed oscillator derivative",29,"blue")
    text(949,653,"C = D^3 + B(1 + Theta),   M = -partial(Theta^(-1))",23)
    text(949,699,"Bosonic array A_Theta     Exterior array E_Theta",23)
    rect(973,744,795,114,"pale")
    text(995,762,"b_M = 2 sqrt(2) Re <E_Theta, M A_Theta>",24)
    text(995,808,"|b_M| <= (||M|| / sqrt(2)) ||C psi||^2",25)
    text(949,893,"M compact: split M = e M e + a small remainder",23)
    text(949,940,"|b_M| <= a ||C psi||^2 + K_a ||psi||^2",27,"green")
    text(949,987,"Uses both weighted contraction energies.",23,"muted")
    text(949,1034,"No one-sided derivative assertion enters this proof.",23,"muted")

    rect(45,1140,1750,250)
    text(70,1164,"FQ.4  What a full physical Dirac sum still must prove",29,"blue")
    text(70,1210,"Q = ||D_N psi||^2 + ||C psi||^2 - i sum <psi, Gamma_aux c_j B(S_j) psi>",26)
    text(70,1260,"Dense Dom D_N intersect Dom C + the cross estimate => a closed energy form and self-adjoint energy operator.",23,"green")
    text(70,1305,"A self-adjoint odd Dirac sum, localized compactness, inverse-module passage and original Bott +1 remain separate.",23,"red")
    text(70,1351,"JD.7 is an auxiliary coefficient example; it does not obstruct the eligible foliation theorem.",22,"muted")
    text(55,1417,"Proof locators: K-theory of the leaf space, Section 11AK; JD.1–JD.23 and FQ.1–FQ.8. Exact constants and domains in text.",22)
    text(55,1455,"Human context: Connes (1982), A survey of foliations and operator algebras, end of Section 8. Original figure and source: CC0.",20,"muted")
    parts.append('</svg>')
    SVG.write_text('\n'.join(parts),encoding="utf-8")
    im.save(PNG)
    checks=dict(schema="joint-domain-cross-form-checks/v1", exact_blocks=exact_checks(),
                proved_limit_square="3/22", numerical_samples_are_proof=False,
                figure_dimensions=[W,H], proof_locators=["JD.1–JD.23","FQ.1–FQ.8"])
    (args.output_dir/"JOINT-DOMAIN-CHECKS.json").write_text(json.dumps(checks,indent=2)+'\n',encoding="utf-8")
    print(json.dumps(dict(svg=str(SVG),png=str(PNG),exact_cases=5,limit_square="3/22")))

if __name__ == "__main__": render()
