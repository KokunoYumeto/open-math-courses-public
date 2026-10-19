"""Exact opposite-sign modes and finite-contact gains. CC0-1.0."""
from pathlib import Path
import math,json,hashlib
root=Path(__file__).resolve().parents[1]
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="560" viewBox="0 0 1100 560" role="img" aria-labelledby="title desc"><title id="title">Opposite-sign null modes and exact finite-contact gains</title><desc id="desc">The left panel plots exp minus x squared over two and exp minus x fourth over four, for x from minus two to two. The right panel displays the gains one over k plus one for contact orders one through six.</desc><rect width="1100" height="560" fill="#f7fafb"/><g font-family="sans-serif" fill="#183344"><text x="32" y="42" font-size="25" font-weight="bold">The sign selects the null mode; contact fixes the gain</text><text x="40" y="87" font-size="19">E1, R0: actual decaying solutions</text><text x="612" y="87" font-size="19">F3, S0: exact gain for the order-one model</text>''']
px=lambda x:275+100*x
py=lambda y:360-230*y
parts.append('<path d="M75 120V360H475" fill="none" stroke="#183344" stroke-width="2"/><path d="M275 120V360" stroke="#b4c8d0" stroke-dasharray="5 5"/>')
for k,color in [(1,'#166e80'),(3,'#b3592b')]:
 points=' '.join(f'{px(x):.3f},{py(math.exp(-x**(k+1)/(k+1))):.3f}' for x in [-2+j/100 for j in range(401)])
 parts.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>')
for x in [-2,-1,0,1,2]:parts.append(f'<text x="{px(x)-7}" y="384" font-size="17">{x}</text>')
for y,label in [(0,'0'),(.5,'1/2'),(1,'1')]:parts.append(f'<text x="39" y="{py(y)+6}" font-size="17">{label}</text>')
parts.append('<text x="489" y="364" font-size="18">x</text><text x="76" y="416" font-size="18" fill="#166e80">k = 1: exp(−x²/2)</text><text x="76" y="445" font-size="18" fill="#b3592b">k = 3: exp(−x⁴/4)</text><text x="40" y="480" font-size="18">Both solve w′ + xᵏw = 0 and belong to L².</text>')
parts.append('<path d="M640 120V360H1060" fill="none" stroke="#183344" stroke-width="2"/>')
for k in range(1,7):
 x=654+(k-1)*68;h=420/(k+1)
 parts.append(f'<rect x="{x}" y="{360-h:.3f}" width="42" height="{h:.3f}" fill="#166e80"/><text x="{x+4}" y="{350-h:.3f}" font-size="17">1/{k+1}</text><text x="{x+16}" y="384" font-size="18">{k}</text>')
parts.append('<text x="677" y="425" font-size="18">contact order k</text><text x="613" y="463" font-size="18">Gain δ = 1/(k+1); loss = k/(k+1).</text><text x="32" y="531" font-size="17">For order m, add m−1 to the gain. Odd contact has an excluded negative-frequency direction.</text></g></svg>')
out=root/'figures/finite-contact-sign-and-gain.svg';out.write_text(''.join(parts),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'exact_parameters':{'profile_orders':[1,3],'profile_domain':[-2,2],'profile_samples':401,'gain_orders':[1,2,3,4,5,6],'gain_formula':'1/(k+1)','null_mode_equation':"w'+x^k w=0"},'proof_locators':['E1','F3','S0','R0','V0'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                         }
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8');print(json.dumps(check))
