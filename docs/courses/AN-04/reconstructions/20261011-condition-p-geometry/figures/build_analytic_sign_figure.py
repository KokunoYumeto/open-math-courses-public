"""Exact simple-root and analytic sign-factor examples."""
from pathlib import Path
from fractions import Fraction
from math import sqrt,cos,sin,pi
from html import escape

W,H=1080,570
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">Simple real roots and a time-independent sign factor</title>',
 '<desc id="desc">A marked fiber through w squared minus z cubed, and the common sign carrier x times x squared plus y squared with its nonnegative quotients.</desc>',
 '<rect width="1080" height="570" fill="#f8fafc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#17243b;font-size:17px}.small{font-size:14px}.head{font-size:20px;font-weight:bold}.axis{stroke:#52627a;stroke-width:1.3}.curve{fill:none;stroke:#1d4ed8;stroke-width:3}</style>']

def text(x,y,s,cls=''):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#52627a',width=1.3,dash=''):
 parts.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')
def curve(points,color='#1d4ed8',width=3):
 value=' '.join(f'{x:.3f},{y:.3f}' for x,y in points)
 parts.append(f'<polyline points="{value}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def dot(x,y):parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="5" fill="#17243b"/>')

text(36,38,'Simple roots expose an odd multiplicity','head')
text(36,67,'P(z,w) = w² − z³')
left=lambda z,w:(110+700*z,280-420*w)
line(*left(-.08,0),*left(.49,0));line(*left(0,-.40),*left(0,.40))
text(455,304,'z');text(86,111,'w')
for sign in [1,-1]:curve([left(z,sign*z**1.5) for z in [j*.48/200 for j in range(201)]])
z=Fraction(1,4);r=Fraction(1,8)
assert r*r-z*z*z==0 and 2*r==Fraction(1,4)
line(*left(float(z),-.38),*left(float(z),.38),'#7c3aed',2,'6 5')
dot(*left(float(z),float(r)));dot(*left(float(z),-float(r)))
text(180,205,'w = 1/8','small');text(180,374,'w = −1/8','small')
line(250,208,279,223,'#52627a',1);line(250,355,279,337,'#52627a',1)
text(313,117,'+');text(313,265,'−');text(313,427,'+')
text(288,458,'z = 1/4','small')
text(36,495,'At the roots: ∂P/∂w = ±1/4.')
text(36,524,'Avoiding the other zero sets isolates the parity test.','small')

text(577,38,'One sign carrier, varying nonnegative quotient','head')
text(577,67,'G(x,y) = x(x²+y²)')
right=lambda x,y:(810+150*x,280-150*y)
parts.append('<rect x="615" y="100" width="195" height="360" fill="#fee2e2"/><rect x="810" y="100" width="195" height="360" fill="#dbeafe"/>')
line(*right(-1.3,0),*right(1.3,0));line(*right(0,-1.2),*right(0,1.2),'#17243b',3)
text(651,123,'G < 0');text(896,123,'G > 0');text(813,484,'G = 0','small')
for t,color in [(0,'#047857'),(1,'#b45309')]:
 curve([right(cos(2*pi*j/240)/sqrt(1+t*t),sin(2*pi*j/240)) for j in range(241)],color)
dot(*right(0,0));text(817,269,'Hₜ = 0','small')
text(1015,286,'x');text(817,92,'y')
line(585,498,618,498,'#047857',3);text(627,504,'H₀ = x²+y² = 1','small')
line(585,526,618,526,'#b45309',3);text(627,532,'H₁ = 2x²+y² = 1','small')
text(882,504,'Fₜ = G Hₜ','small');text(882,532,'Hₜ ≥ 0','small')
parts.append('</svg>')
output=Path(__file__).with_name('analytic-sign-factorization.svg')
output.write_text('\n'.join(parts)+'\n','utf-8')
print({'output':output.name,'exact_marked_fiber':str(z),'exact_marked_roots':[str(-r),str(r)],'curve_samples_are_illustrative':True})
