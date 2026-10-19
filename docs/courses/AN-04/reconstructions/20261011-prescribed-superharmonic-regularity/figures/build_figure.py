"""Exact packet support widths and logarithmic growth shape. CC0-1.0."""
from pathlib import Path
import math,json,hashlib
root=Path(__file__).resolve().parents[1]
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="570" viewBox="0 0 1100 570" role="img" aria-labelledby="title desc"><title id="title">Frequency windows and the realization norm lower bound</title><desc id="desc">Support and plateau widths around eta/t equal to one at log t equal to four, eight and sixteen. The second panel plots r/4 minus three log r for r between sixteen and sixty-four.</desc><rect width="1100" height="570" fill="#f7fafb"/><g font-family="sans-serif" fill="#183344"><text x="35" y="44" font-size="25" font-weight="bold">A narrowing frequency window still carries growing energy</text><text x="35" y="87" font-size="18">W1: normalized normal frequency η/t, d = 1</text><text x="608" y="87" font-size="18">X3: logarithm of the lower-bound shape</text>''']
X=lambda v:270+4400*(v-1)
for j,lam in enumerate([4,8,16]):
 yy=170+j*85;a=1/(8*lam);b=1/(16*lam)
 parts.append(f'<text x="35" y="{yy-25}" font-size="17">log t = {lam}</text><path d="M70 {yy}H470" stroke="#98aeb8"/><rect x="{X(1-a):.3f}" y="{yy-12}" width="{8800*a:.3f}" height="24" fill="#c7e3e9"/><rect x="{X(1-b):.3f}" y="{yy-12}" width="{8800*b:.3f}" height="24" fill="#146575"/>')
parts.append('<path d="M270 130V376" stroke="#ad602e" stroke-dasharray="5 5"/><text x="265" y="400" font-size="18">1</text><text x="35" y="440" font-size="17">Pale: support within 1/(8 log t)</text><text x="35" y="471" font-size="17">Dark: unit plateau within 1/(16 log t)</text>')
px=lambda r:650+390*(r-16)/48
py=lambda value:400-250*(value+5)/9
points=' '.join(f'{px(r):.3f},{py(r/4-3*math.log(r)):.3f}' for r in [16+48*j/400 for j in range(401)])
parts.append(f'<path d="M650 140V400H1040" fill="none" stroke="#183344" stroke-width="2"/><path d="M650 {py(0):.3f}H1040" stroke="#bdcdd5" stroke-dasharray="5 5"/><polyline points="{points}" fill="none" stroke="#146575" stroke-width="3"/>')
for rr in [16,32,48,64]:parts.append(f'<text x="{px(rr)-9:.3f}" y="426" font-size="17">{rr}</text>')
for val in [-4,0,4]:parts.append(f'<text x="618" y="{py(val)+6:.3f}" font-size="17">{val}</text>')
parts.append('<text x="675" y="128" font-size="19">r/4 − 3 log r</text><text x="905" y="459" font-size="18">r = log t</text><text x="609" y="490" font-size="16">Increasing for r &gt; 12; unbounded as r grows.</text><text x="35" y="537" font-size="16">The norm bound has an unspecified positive factor C. Its logarithm adds a constant to the right-hand curve.</text></g></svg>')
out=root/'figures/prescribed-regularity-packets.svg';out.write_text(''.join(parts),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
check={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'exact_parameters':{'normal_dimension':1,'support_profile_radius':'1/8','plateau_profile_radius':'1/16','log_t_rows':[4,8,16],'growth_log_interval':[16,64],'growth_gap':'1/8','ambient_dimension':3,'growth_function':'r/4-3 log r','samples':401},'proof_locators':['W1','W3','X2','X3'],'scope':'The recorded calculations and diagrams concern the stated examples. The general analytic assertions use the written arguments.'                                         }
(root/'figure-check.json').write_text(json.dumps(check,indent=2)+'\n','utf-8');print(json.dumps(check))
