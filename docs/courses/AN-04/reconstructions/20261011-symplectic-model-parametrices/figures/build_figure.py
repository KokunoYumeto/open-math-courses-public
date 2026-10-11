"""Exact corrected Gaussian forcing and signed inverse identities. CC0-1.0."""
from pathlib import Path
import math,json,hashlib
root=Path(__file__).resolve().parents[1]
p=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="620" viewBox="0 0 1100 620" role="img" aria-labelledby="title desc"><title id="title">Remove the cokernel component before inverting</title><desc id="desc">Exact Gaussian input, its rank-one projection and their difference. Positive frequency removes a source component; negative frequency removes a solution component.</desc><rect width="1100" height="620" fill="#f7fafb"/><g fill="#183344" font-family="sans-serif"><text x="30" y="40" font-size="25" font-weight="bold">The missing inverse is exactly a projection</text><text x="40" y="83" font-size="19">X1: k = 1, frequency λ = 1</text>''']
px=lambda r:285+72*r
py=lambda y:356-205*y
p.append('<path d="M69 130V397H501 M69 356H501" fill="none" stroke="#183344" stroke-width="2"/>')
profiles=[('f',lambda r:math.exp(-r*r),'#166e80'),('Pf',lambda r:math.sqrt(2/3)*math.exp(-r*r/2),'#b3592b'),('f-Pf',lambda r:math.exp(-r*r)-math.sqrt(2/3)*math.exp(-r*r/2),'#704495')]
for name,fn,color in profiles:
 pts=' '.join(f'{px(r):.3f},{py(fn(r)):.3f}' for r in [-3+j/100 for j in range(601)])
 p.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>')
for r in [-3,-2,-1,0,1,2,3]:p.append(f'<text x="{px(r)-7}" y="425" font-size="17">{r}</text>')
for y,label in [(0,'0'),(.5,'1/2'),(1,'1')]:p.append(f'<text x="30" y="{py(y)+6}" font-size="16">{label}</text>')
p.append('<text x="513" y="360" font-size="18">r</text><text x="72" y="462" font-size="18" fill="#166e80">f(r) = exp(−r²)</text><text x="72" y="490" font-size="18" fill="#b3592b">Pf(r) = √(2/3) exp(−r²/2)</text><text x="72" y="518" font-size="18" fill="#704495">Corrected forcing: f − Pf</text>')
p.append('''<rect x="590" y="119" width="470" height="160" rx="10" fill="#e0edf1"/><text x="614" y="155" font-size="21" font-weight="bold">Positive frequency</text><text x="614" y="197" font-size="22">L E = I − P     and     E L = I</text><text x="614" y="243" font-size="18">Remove the adjoint-kernel component.</text><rect x="590" y="315" width="470" height="160" rx="10" fill="#f3e9df"/><text x="614" y="351" font-size="21" font-weight="bold">Negative frequency</text><text x="614" y="393" font-size="22">L E = I     and     E L = I − P</text><text x="614" y="439" font-size="18">Choose the solution perpendicular to ker L.</text><text x="590" y="516" font-size="18">D1–K2: exact fiber identities for odd k.</text><text x="30" y="570" font-size="18">The corrected forcing has zero exp(−r²/2)-weighted integral. Its pointwise sign changes.</text><text x="30" y="602" font-size="17">The plotted profiles are exact analytic functions; the proof does not depend on numerical sampling.</text></g></svg>''')
out=root/'figures/projected-forcing-and-inverses.svg';out.write_text(''.join(p),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'exact_parameters':{'k':1,'lambda':1,'domain':[-3,3],'samples':601,'input':'exp(-r^2)','projected':'sqrt(2/3)*exp(-r^2/2)','corrected':'input-projected'},'proof_locators':['D1','K1','K2','X1','V0'],'actually_inspected':False,'exact_coordinate_review_complete':False}
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8');print(json.dumps(check))
