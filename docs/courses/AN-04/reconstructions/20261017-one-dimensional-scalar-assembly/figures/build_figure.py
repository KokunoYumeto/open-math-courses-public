"""Exact support bounds on [0,4]; original diagram, CC0-1.0."""
from pathlib import Path
W,H=1100,620
X=lambda t:100+225*t
rows=[('Collar output bounds',110,[(0,1,'#146575'),(3,4,'#146575')]),
      ('Interior output buffer',230,[(1/4,15/4,'#c37a19')]),
      ('Deep cutoff supports',350,[(0,1/8,'#624d91'),(31/8,4,'#624d91')])]
s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Boundary and interior scalar test supports on the interval from zero to four">',
'<rect width="1100" height="620" fill="white"/>',
'<style>text{font-family:Arial,sans-serif;fill:#183246;font-size:20px}.small{font-size:18px}</style>',
'<text x="100" y="34" font-size="25">Join two collar tests to one positive interior test</text>',
'<text x="100" y="65" class="small">X = [0,4]; inward coordinates xL = t and xR = 4 − t</text>']
for title,y,segments in rows:
 s += [f'<text x="100" y="{y-12}">{title}</text>',f'<line x1="100" y1="{y+25}" x2="1000" y2="{y+25}" stroke="#becad2" stroke-width="2"/>']
 for a,b,c in segments:
  s += [f'<rect x="{X(a)}" y="{y+12}" width="{X(b)-X(a)}" height="26" fill="{c}" opacity="0.85"/>']
 for t,label in [(0,'0'),(4,'4')]:s += [f'<text x="{X(t)}" y="{y+68}" text-anchor="middle">{label}</text>']
 if y==110:
  for t,label in [(1,'1'),(3,'3')]:s += [f'<text x="{X(t)}" y="{y+68}" text-anchor="middle">{label}</text>']
 elif y==230:
  for t,label in [(1/4,'1/4'),(15/4,'15/4')]:s += [f'<circle cx="{X(t)}" cy="{y+25}" r="6" fill="white" stroke="#c37a19" stroke-width="2"/>',f'<text x="{X(t)}" y="{y+68}" text-anchor="middle">{label}</text>']
 else:
  for t,label,shift in [(1/8,'1/8',25),(31/8,'31/8',-25)]:s += [f'<circle cx="{X(t)}" cy="{y+25}" r="5" fill="white" stroke="#624d91" stroke-width="2"/>',f'<text x="{X(t)+shift}" y="{y+68}" text-anchor="middle">{label}</text>']
s += ['<text x="100" y="465">The interior test overlaps the collar tests. Positivity handles this overlap.</text>',
'<text x="100" y="500">Only the two separate endpoint output channels are disjoint.</text>',
'<text x="100" y="540" class="small">Ratio bound in each collar: 3y/4 ≤ x ≤ 4y/3, with input y ≤ 3/4.</text>',
'<text x="100" y="575" class="small">Allowed support bounds, not nonzero kernel values. See C1, A0, P0 and Exercise 1.</text>','</svg>']
Path(__file__).with_name('one-dimensional-scalar-assembly.svg').write_text('\n'.join(s)+'\n','utf-8')
