"""Coordinate and bound plots for the amplitude proof; CC0-1.0."""
from pathlib import Path
import hashlib,json,math,html
root=Path(__file__).resolve().parent
p=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="490" viewBox="0 0 1040 490">','<rect width="1040" height="490" fill="#f4f8fb"/>','<style>text{font:16px Arial,sans-serif;fill:#183b4b}.title{font-size:19px;font-weight:bold}.small{font-size:14px}.axis{stroke:#7c919c;stroke-width:1.5}.curve{stroke:#087d8b;stroke-width:3;fill:none}</style>']
def tx(x,y,t,c=''):p.append(f'<text x="{x}" y="{y}" class="{c}">{html.escape(t)}</text>')
def ln(x,y,X,Y,c='axis'):p.append(f'<line x1="{x}" y1="{y}" x2="{X}" y2="{Y}" class="{c}"/>')
def xy1(u,q):return 58+240*u,329-240*q
for x in [12,356,700]:p.append(f'<rect x="{x}" y="12" width="328" height="466" rx="12" fill="white" stroke="#d8e4eb"/>')
tx(29,44,'Support on the elliptic side','title');tx(373,44,'Normal block determinant','title');tx(717,44,'Flatness gains frequency decay','title')
points=[xy1(0,0),xy1(1,0),xy1(1,1)];p.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in points)+'" fill="#d9eff1"/>')
pts=[xy1(0,0),xy1(1,0),xy1(1,.25)];p.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in pts)+'" fill="#edc796"/>')
ln(*xy1(0,0),*xy1(1.05,0));ln(*xy1(0,0),*xy1(0,1.05));ln(*xy1(0,0),*xy1(1,1),'curve')
tx(36,345,'0','small');tx(296,350,'1','small');tx(34,93,'1','small');tx(290,374,'u = −v','small');tx(30,71,'q')
tx(155,142,'q = u','small');tx(182,262,'ζ > 0','small');tx(29,410,'Shaded triangle: 0 ≤ q < u.','small');tx(29,437,'Orange: q < u/4.','small');tx(29,462,'The caustic is preserved.','small')
def xy2(u,d):return 403+240*u,329-60*d
ln(*xy2(0,0),*xy2(1.05,0));ln(*xy2(0,0),*xy2(0,4.15));ln(*xy2(0,0),*xy2(1,4),'curve')
tx(380,350,'0','small');tx(640,350,'1','small');tx(382,93,'4','small');tx(650,374,'u','small');tx(380,72,'det J','small')
tx(496,156,'det J = 4u','small');tx(373,410,'J = [ 0  −2u ; 2  0 ]','small');tx(373,437,'Invertible for every u > 0.','small');tx(373,462,'Inverse powers meet flat errors.','small')
def xy3(z,f):return 747+12*z,329-9*f
ln(*xy3(0,0),*xy3(20.4,0));ln(*xy3(0,0),*xy3(0,26.5))
points=[xy3(j/20,(j/20)**4*math.exp(-2*(j/20)/3)) for j in range(401)]
p.append('<polyline points="'+' '.join(f'{a:.3f},{b:.3f}' for a,b in points)+'" class="curve"/>')
peak=(6/math.e)**4;xx,yy=xy3(6,peak);p.append(f'<circle cx="{xx}" cy="{yy}" r="5" fill="#b96820"/>')
ln(xx,yy,xx,329);tx(xx-5,350,'6','small');tx(978,350,'20','small');tx(726,350,'0','small');tx(975,374,'z','small');tx(757,83,'peak = (6/e)⁴','small')
tx(717,410,'z = λ q √u','small');tx(717,437,'Curve: z⁴ exp(−2z/3).','small');tx(717,462,'The error bound gains λ⁻⁴.','small')
p.append('</svg>');out=root/'airy-amplitude-errors.svg';out.write_text('\n'.join(p),'utf-8');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root.parent/'figure-check.json').write_text(json.dumps({'svg':'figures/airy-amplitude-errors.svg','svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),
 'coordinate_scope':'A13, the exact affine unattained wedge, CA14 determinant, and the CA23 bound with L=4, K=2, c=2/3.',
 'peak_coordinate':[6,peak],'licence':'CC0-1.0','external_artwork':False,'actually_inspected':False},indent=2)+'\n','utf-8')
print('Built three exact coordinate/bound panels.')
