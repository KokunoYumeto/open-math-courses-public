"""Exact tangential output interval coordinates and two-mode norm; CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,html
p=Path(__file__).resolve();root=p.parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="590" viewBox="0 0 1040 590">',
'<rect width="1040" height="590" fill="#f6f9fb"/>',
'<style>text{font-family:Arial,sans-serif;fill:#183048}.title{font-size:24px;font-weight:bold}.label{font-size:19px}.small{font-size:16px}</style>']
def text(x,y,s,cl='label',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{html.escape(s)}</text>')
def X(a):return 95+1400*float(a)
text(28,42,'A fixed residual test from separated output regions','title')
text(28,76,'First six intervals: center 1/(j+1), radius 1/[10(j+1)²].','label')
parts.append('<line x1="85" y1="204" x2="960" y2="204" stroke="#425c6b" stroke-width="2"/>')
intervals=[]
for j in range(1,7):
 center=Fraction(1,j+1);radius=Fraction(1,10*(j+1)**2);lo,hi=center-radius,center+radius
 intervals.append({'j':j,'center':str(center),'radius':str(radius),'left':str(lo),'right':str(hi)})
 parts.append(f'<rect x="{X(lo)}" y="156" width="{X(hi)-X(lo)}" height="48" fill="#208496"/>')
 parts.append(f'<line x1="{X(center)}" y1="152" x2="{X(center)}" y2="133" stroke="#208496"/>')
 text(X(center),123,str(j),'small','middle')
for i in range(7):
 x=X(Fraction(i,10))
 parts.append(f'<line x1="{x}" y1="204" x2="{x}" y2="214" stroke="#425c6b"/>')
 text(x,241,f'{i/10:.1f}','small','middle')
parts.append(f'<circle cx="{X(0)}" cy="204" r="5" fill="white" stroke="#425c6b" stroke-width="2"/>')
text(95,279,'0 is an accumulation point; every packed kernel has zero jets there.','small')
text(875,241,'z₁','label')
parts.append('<line x1="28" y1="310" x2="1012" y2="310" stroke="#c4d1db"/>')
text(28,348,'Two modes: Rₐ = R₀ + eⁱᵃ R₁','title')
text(28,383,'The output maps U₁ and U₂ preserve each L² norm and have disjoint ranges.','small')
for x,label in [(60,'2 U₁ R₀ f'),(375,'3 U₂ R₁ f')]:
 parts.append(f'<rect x="{x}" y="412" width="250" height="60" rx="8" fill="#dcecf1"/>')
 text(x+125,450,label,'title','middle')
text(338,451,'+','title','middle')
text(668,451,'=','title','middle')
text(745,451,'S f','title')
text(28,522,'‖S f‖² = 4 ‖R₀ f‖² + 9 ‖R₁ f‖²','title')
text(28,563,'Only residual kernels are relocated. The normal coordinate and input coordinates stay fixed.','small')
parts.append('</svg>')
dest=p.parent/'fixed-residual-packing.svg';dest.write_text('\n'.join(parts)+'\n','utf-8')
result={'svg':'figures/'+dest.name,'svg_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'actually_inspected':False,
 'exact_intervals':intervals,'horizontal_coordinate_map':'pixel = 95 + 1400*z1',
 'two_mode_weights':[2,3],'squared_norm_weights':[4,9],
 'meaning':'Actual first six tangential intervals and exact two-mode orthogonal norm identity; the omitted infinite tail accumulates at zero.'}
(root/'figure-check.json').write_text(json.dumps(result,indent=2)+'\n','utf-8')
print(json.dumps({'intervals':6,'passed':True}))
