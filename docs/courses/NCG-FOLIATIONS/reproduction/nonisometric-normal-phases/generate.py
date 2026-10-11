from pathlib import Path
import html,json
base=Path(__file__).resolve().parent
d=json.loads((base/'data.json').read_text(encoding='utf-8'))
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="850" viewBox="0 0 1080 850">','<rect width="1080" height="850" fill="white"/>','<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0 0 L7 3 L0 6 Z" fill="context-stroke"/></marker></defs>','<g font-family="Arial, sans-serif" fill="#183345">']
def text(x,y,s,size=20,color='#183345',anchor='start'):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{html.escape(s)}</text>')
text(540,40,'Nonisometric K-orientation: positive class and exact phase limit',26,anchor='middle')
out.append('<rect x="35" y="70" width="1010" height="210" rx="12" fill="#edf6f1" stroke="#35634c"/>')
text(60,103,'Original q = 1: circle suspension h(theta) = theta + sin(theta)/2',23)
for y,s in [(139,'Fixed-point derivative 3/2: invariant metric would require m(0) = 9m(0)/4.'),(177,'Coherent derivative lift retains the full inverse line and actual fixed-point isotropy.'),(215,'Negative Fourier phase: compact kernel cancellation; actual reduced norm; disk +1.'),(253,'Full suspension graph: completed creation connections preserve the inverse normal symbol.')]:text(60,y,s,20)
out.append('<rect x="35" y="305" width="1010" height="410" rx="12" fill="#f0f4fa" stroke="#365578"/>')
text(60,342,'Original q = 2: psi(theta,y) = (h(theta),y)',23)
text(60,383,'At the fixed circle: Dpsi = diag(3/2, 1).',21)
text(60,424,'The usual flat Dirac phase fails compact covariance.',20)
text(60,464,'One pointwise unitary for all normalized directions',20)
text(60,495,'would require Dpsi = lambda O (conformality).',20)
text(60,543,'Source direction: (1,1)/sqrt(2)',20,color='#a15b20')
text(60,580,'Range direction: (3,2)/sqrt(13)',20,color='#216982')
text(60,620,'Exact gap: sqrt(2 - 10/sqrt(26))',20,color='#69479b')
text(60,660,'This excludes the tested phase; another graph class remains possible.',18)
ox,oy,scale=735,650,260
out.append(f'<path d="M{ox} {oy} L1020 {oy} M{ox} {oy} L{ox} 375" stroke="#a7b1bb"/>')
for name,color in [('source_direction','#a15b20'),('range_direction','#216982')]:
    x,y=d['q2'][name];out.append(f'<path d="M{ox} {oy} L{ox+scale*x:.8f} {oy-scale*y:.8f}" stroke="{color}" stroke-width="4" marker-end="url(#arrow)"/>')
u,v=d['q2']['source_direction'],d['q2']['range_direction']
out.append(f'<path d="M{ox+scale*u[0]:.8f} {oy-scale*u[1]:.8f} L{ox+scale*v[0]:.8f} {oy-scale*v[1]:.8f}" stroke="#69479b" stroke-width="3" stroke-dasharray="5 4"/>')
text(875,408,'Exact symbol vectors',18,anchor='middle')
out.append('<rect x="35" y="740" width="1010" height="80" rx="12" fill="#fff4e6" stroke="#ad7941"/>')
text(60,774,'NRA.1–NRA.10 and AP.1–AP.12: original degrees, actual arrows and exact signs retained.',20)
text(60,804,'General metric-bundle routes still need reduced descent and the original disk comparison.',19)
out+=['</g></svg>']
(base.parents[1]/'figures'/(d['slug']+'.svg')).write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n')
