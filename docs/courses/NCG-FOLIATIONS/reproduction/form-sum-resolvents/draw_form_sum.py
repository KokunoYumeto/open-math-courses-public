"""Original SD resolvent-domain figure, CC0. Python and Pillow."""
from pathlib import Path
from io import BytesIO
from fractions import Fraction
import argparse,base64,html,json,re
from PIL import Image,ImageDraw,ImageFont
HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,default=HERE/'out')
parser.add_argument('--resources',type=Path,default=HERE.parent/'labelled-geometric-kernel')
args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
W,H=1800,1150

def render():
    font=(args.resources/'fonts/DejaVuSans.ttf').read_bytes()
    notice=(args.resources/'FONT-NOTICE.txt').read_text(encoding='utf-8')
    colors=dict(bg="#f4f6fa",ink="#14233d",blue="#2057a0",green="#196542",red="#a23838",amber="#946014",grid="#ccd5e3",pale="#e9eef7")
    image=Image.new("RGB",(W,H),colors["bg"]);d=ImageDraw.Draw(image);fonts={}
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">',
     '<title>The actual resolvent proof of the completed form-domain Dirac sum</title>',
     '<desc>SD.1 to SD.14. The differentiable physical realization is an explicit prerequisite; the self-adjoint sum follows from onto resolvents.</desc>',
     f'<metadata id="font-notice">{html.escape(notice)}</metadata>',
     f'<style>@font-face{{font-family:SD;src:url(data:font/ttf;base64,{base64.b64encode(font).decode()})}}text{{font-family:SD,sans-serif}}</style>',
     f'<rect width="{W}" height="{H}" fill="{colors["bg"]}"/>']
    def text(x,y,s,size=25,color="ink"):
        if size not in fonts:fonts[size]=ImageFont.truetype(BytesIO(font),size)
        c=colors.get(color,color);d.text((x,y),s,font=fonts[size],fill=c)
        parts.append(f'<text x="{x}" y="{y+size}" font-size="{size}" fill="{c}">{html.escape(s)}</text>')
    def box(x,y,w,h,border="grid"):
        c=colors[border];d.rounded_rectangle((x,y,x+w,y+h),15,fill="white",outline=c,width=2)
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="white" stroke="{c}" stroke-width="2"/>')
    def arrow(x,y,x2,y2):
        d.line([(x,y),(x2,y2)],fill=colors["blue"],width=4)
        d.polygon([(x2,y2),(x2-12,y2-8),(x2-12,y2+8)],fill=colors["blue"])
        parts.append(f'<path d="M{x},{y}L{x2},{y2}" stroke="{colors["blue"]}" stroke-width="4"/>')
        parts.append(f'<polygon points="{x2},{y2} {x2-12},{y2-8} {x2-12},{y2+8}" fill="{colors["blue"]}"/>')
    text(48,27,"The actual odd Dirac sum: a completed resolvent-domain proof",35)
    text(48,80,"Specific expression S = C + Gamma D_N; Dom S = Dom C intersect Dom D_N. Full inverse normal factor retained.",23)
    box(43,138,1715,167,"amber")
    text(68,156,"SD.3  Required physical coefficient realization",28,"amber")
    text(68,207,"D_N self-adjoint on its maximal distributional domain; coefficient resolvents carry the actual normal derivation.",24)
    text(68,252,"[D_N, R_lambda] = -i sum c_j partial_j R_lambda, with the original grading and final right Clifford order.",24)
    box(43,335,790,282,"green")
    text(67,351,"SD.2  Actual CW oscillator",28,"blue")
    text(67,399,"C = D^3 + B(1 + Theta),  Theta = h^(-1)",25)
    text(67,442,"R_lambda = (C + i lambda)^(-1)",26)
    text(67,486,"||partial_j R_lambda|| <= a + K_a / lambda^2",25)
    text(67,532,"K = [D_N, R_lambda] has norm -> 0",27,"green")
    text(67,576,"Form estimate; no one-sided Theta derivative required.",22)
    arrow(841,474,915,474)
    box(932,335,826,282,"green")
    text(956,351,"SD.1 + SD.4  The symmetric product",28,"blue")
    text(956,399,"B = -i Gamma R_lambda is self-adjoint",25)
    text(956,442,"X = (B D_N + D_N B) / 2 is essentially self-adjoint",23)
    text(956,486,"T = Gamma D_N R_lambda = i X + Gamma K / 2",24)
    text(956,532,"||K|| / 2 < 1 => 1 + T is onto",27,"green")
    text(956,576,"Use the explicit self-adjoint product core and Neumann series.",21)
    box(43,648,1715,239,"green")
    text(67,666,"SD.13  Onto resolvents of the specified sum",28,"blue")
    text(67,713,"(S + i lambda) R_lambda = 1 + T,   and repeat with -lambda",31)
    text(67,765,"Symmetry gives injectivity of the natural closed T extension; its already-onto core closure is therefore maximal.",24)
    text(67,812,"S is self-adjoint and odd on exactly Dom C intersect Dom D_N.  R_lambda(core D_N) is a joint graph core.",25,"green")
    text(67,853,"This proves the actual first-order sum; it does not choose an unspecified square root of an energy operator.",22)
    box(43,920,1715,167)
    text(67,934,"Exact constant-coefficient check: c = 1, lambda = 2, normal momentum p = 3",26,"blue")
    text(67,978,"C = c sigma_x; Gamma = sigma_z; B^2 = I/5; ||(1 + i p B)^(-1)||^2 = 5/14; ||(S + 2i)^(-1)||^2 = 1/14.",23)
    text(67,1020,"Remaining: actual differentiable inverse-module passage, G phase compatibility, local compactness and original Bott +1.",23,"red")
    text(48,1103,"Proof: K-theory of the leaf space, Section 11AM, SD.1–SD.14. Human context: Connes (1982), end of Section 8. Original figure/source: CC0.",21)
    parts.append('</svg>')
    (args.output_dir/"form-sum-resolvents.svg").write_text('\n'.join(parts),encoding="utf-8")
    image.save(args.output_dir/"form-sum-resolvents.png")
    # Exact rational squares for the finite illustration.
    c,lam,p=Fraction(1),Fraction(2),Fraction(3);den=c*c+lam*lam
    b_square=1/den;onto_inv_square=1/(1+p*p/den);sum_inv_square=1/(c*c+p*p+lam*lam)
    assert b_square==Fraction(1,5) and onto_inv_square==Fraction(5,14) and sum_inv_square==Fraction(1,14)
    assert b_square*onto_inv_square==sum_inv_square
    checks=dict(exact_finite_model=True,B_square=str(b_square),onto_inverse_norm_square=str(onto_inv_square),
                sum_inverse_norm_square=str(sum_inv_square),finite_model_is_the_general_proof=False,
                dimensions=[W,H],proof="K-theory of the leaf space, Section11AM, SD.1–SD.14")
    (args.output_dir/"FORM-SUM-CHECKS.json").write_text(json.dumps(checks,indent=2)+'\n',encoding="utf-8")
    print(json.dumps(checks))
if __name__=="__main__":render()
