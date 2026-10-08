"""Reproduce the exact scalar curves and the reconstruction diagram."""
from pathlib import Path
from math import exp
from html import escape
W,H=1120,480
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">Exact boundary cancellation and volume reconstruction</title>',
 '<desc id="desc">For a=1 and forcing exp(-2r), the volume inverse plus its negative boundary correction gives the Dirichlet solution. The second panel displays the exact parametrix and its retained left error.</desc>',
 '<rect width="1120" height="480" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b;font-size:17px}.title{font-size:21px;font-weight:bold}.small{font-size:15px}</style>']
def text(x,y,t,cls='',color=None):
 out.append(f'<text x="{x}" y="{y}"'+(f' class="{cls}"' if cls else '')+(f' style="fill:{color}"' if color else '')+'>'+escape(t)+'</text>')
def line(x,y,xx,yy,col='#becad0',width=1):out.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="{col}" stroke-width="{width}" fill="none"/>')
text(35,35,'Exact normal model (VB25–VB27)','title')
text(35,63,'a = 1, f(r) = exp(−2r), g = 0')
left,right,top,bottom=72,520,92,356
xx=lambda r:left+(right-left)*r/4
yy=lambda v:bottom-(bottom-top)*(v+.18)/.41
for v in [-.15,0,.1,.2]:
 line(left,yy(v),right,yy(v));text(24,yy(v)+5,str(v),'small')
for r in range(5):
 line(xx(r),top,xx(r),bottom);text(xx(r)-5,bottom+24,str(r),'small')
line(left,yy(0),right,yy(0),'#5e6b74',2)
for f,col in [(lambda r:exp(-r)/2-exp(-2*r)/3,'#2364b1'),(lambda r:-exp(-r)/6,'#b65a18'),(lambda r:(exp(-r)-exp(-2*r))/3,'#087c65')]:
 pts=[(xx(4*j/400),yy(f(4*j/400))) for j in range(401)]
 d='M'+' L'.join(f'{x:.3f} {y:.3f}' for x,y in pts)
 out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3"/>')
text(535,bottom+24,'r')
text(42,408,'Vf = ½ exp(−r) − ⅓ exp(−2r)',color='#2364b1')
text(42,436,'Correction = −⅙ exp(−r)',color='#b65a18')
text(42,464,'Sum u = ⅓ [exp(−r) − exp(−2r)]',color='#087c65')
line(570,20,570,466,'#d2dce2')
text(603,35,'Actual reconstruction (VB14–VB19)','title')
for y,height in [(70,124),(217,97),(338,102)]:
 out.append(f'<rect x="600" y="{y}" width="489" height="{height}" rx="8" fill="#f2f6f8" stroke="#bbccd5"/>')
text(619,99,'Forcing f and measurement g')
text(619,132,'L(f,g) = Vf + K S″ γVf + K Sg')
text(619,168,'K uses the full original boundary source.','small')
text(619,247,'u = L(Pu, Bu) + 𝒦u')
text(619,282,'𝒦 = −E − K S″ γE + K R₁ γ')
text(619,369,'The left error gains one derivative.')
text(619,401,'C γV = γEV − γVF gains N derivatives.')
text(619,428,'Every trace is taken above its proved threshold.','small')
out.append('</svg>')
(Path(__file__).parent/'volume-boundary-parametrix.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
