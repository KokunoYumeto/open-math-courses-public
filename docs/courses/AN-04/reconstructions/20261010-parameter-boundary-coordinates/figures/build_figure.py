"""Reproducible base coordinate curves for PBC:X1-X2."""
from pathlib import Path
from html import escape
out=Path(__file__).resolve().parent/'parameter-boundary-coordinates.svg'
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="600" viewBox="0 0 1040 600" role="img" aria-labelledby="title desc">',
 '<title id="title">Two actual boundary collar coordinate maps</title>',
 '<desc id="desc">Horizontal original tangent coordinate y, vertical normal coordinate x=t. Images of z=-1,0,1 under the shear y=z+x/2 and exponential map y=2 to the x times z. These are coordinate curves, not characteristic rays.</desc>',
 '<rect width="1040" height="600" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b;font-size:16px}.head{font-size:21px;font-weight:bold}.small{font-size:14px}</style>']
def text(x,y,s,cls='',anchor='start'):
 svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#536577',width=1):
 svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
def curve(points,color):
 svg.append('<polyline fill="none" stroke="'+color+'" stroke-width="3" points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+'"/>')
colors={-1:'#7759a6',0:'#087e8b',1:'#b64736'}
for panel,start in enumerate([34,560]):
 text(start,33,'A sheared collar' if panel==0 else 'An expanding collar','head')
 text(start,64,'Φ(x,z) = (x, z + x/2)' if panel==0 else 'Φ(x,z) = (x, 2ˣz)')
 text(start,90,'Jacobian j = 1; density factor W = 1' if panel==0 else 'Jacobian j = 2ˣ; density factor W = 2ˣᐟ²')
 point=lambda y,x:(start+224+90*y,438-280*x)
 for y in [-2,-1,0,1,2]:
  line(*point(y,0),*point(y,1),'#e0e7eb')
  px,py=point(y,0);line(px,py,px,py+6);text(px,py+27,str(y),'small','middle')
 for x in [0,.5,1]:
  line(*point(-2.25,x),*point(2.25,x),'#e0e7eb')
  px,py=point(-2.25,x);text(px-8,py+5,str(x),'small','end')
 line(*point(-2.25,0),*point(2.25,0),'#182a3b',2)
 line(*point(-2.25,0),*point(-2.25,1.06))
 text(start+5,130,'x=t','small');text(start+439,463,'y','small')
 for z in [-1,0,1]:
  points=[point(z+x/2 if panel==0 else 2**x*z,x) for x in [j/100 for j in range(101)]]
  curve(points,colors[z])
  px,py=points[-1];text(px,py-12,f'z={z}','small','middle')
 text(start+224,493,'Boundary: x=0 and y=z','small','middle')
 text(start,525,'PC20: straight coordinate lines; determinant one.' if panel==0 else 'PC23–PC24: the density and gauge cancel,','small')
 if panel: text(start,547,'while the tangential lower-order term remains.','small')
text(34,580,'PBC:X1–X2,F0. Exact analytic coordinate curves sampled for display, 0 ≤ x ≤ 1. These are not characteristic rays.','small')
svg.append('</svg>');out.write_text('\n'.join(svg)+'\n','utf-8');print(out)
