"""Exact rational spectral multipliers for the solved compact-correction example. CC0."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
root=Path(__file__).resolve().parents[1]
p=['''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650" role="img" aria-labelledby="title desc"><title id="title">A compact correction leaves one compatibility condition</title><desc id="desc">Exact circle Fourier multipliers for T and I+T at modes zero to three. The constant mode of I+T is zero. Every nonconstant multiplier is at least one half. Negative modes are identical.</desc><rect width="1100" height="650" fill="#f7fafb"/><g font-family="sans-serif" fill="#183344"><text x="30" y="42" font-size="25" font-weight="bold">A compact correction leaves one compatibility condition</text><text x="30" y="79" font-size="18">X2 and V0: exact Fourier multipliers on the circle; negative modes have the same values.</text><text x="52" y="135" font-size="22" font-weight="bold">Correction T</text><text x="605" y="135" font-size="22" font-weight="bold">Identity plus correction I + T</text><text x="52" y="167" font-size="18">tₖ = −1 / (1 + k²)</text><text x="605" y="167" font-size="18">ℓₖ = k² / (1 + k²)</text>''']
for x1,x2,base in [(68,498,210),(620,1050,470)]:
 p.append(f'<line x1="{x1}" y1="{base}" x2="{x2}" y2="{base}" stroke="#183344" stroke-width="2"/>')
for y,label in [(210,'0'),(470,'−1')]:p.append(f'<text x="35" y="{y+6}" font-size="17">{label}</text>')
for y,label in [(210,'1'),(340,'1/2'),(470,'0')]:p.append(f'<text x="565" y="{y+6}" font-size="17">{label}</text>')
p.append('<line x1="620" y1="340" x2="1050" y2="340" stroke="#669e9d" stroke-width="2" stroke-dasharray="5 4"/>')
values=[]
for k in range(4):
 t=Fraction(-1,1+k*k);ell=1+t;values.append({'k':k,'T':str(t),'I_plus_T':str(ell)})
 x=106+105*k;height=float(-260*t)
 p.append(f'<rect x="{x-23}" y="210" width="46" height="{height}" fill="#946143"/><text x="{x-24}" y="{210+height+27}" font-size="18">{str(t).replace("-","−")}</text><text x="{x-6}" y="525" font-size="18">{k}</text>')
 x=660+105*k;height=float(260*ell)
 if k:p.append(f'<rect x="{x-23}" y="{470-height}" width="46" height="{height}" fill="#176f82"/>')
 else:p.append(f'<circle cx="{x}" cy="470" r="7" fill="#aa483b"/>')
 p.append(f'<text x="{x-18}" y="{470-height-16}" font-size="18">{ell}</text><text x="{x-6}" y="525" font-size="18">{k}</text>')
p.append('''<text x="254" y="562" font-size="17">mode k</text><text x="808" y="562" font-size="17">mode k</text><text x="30" y="605" font-size="19">Lost mode: constants. Exact solvability requires zero mean.</text><text x="30" y="633" font-size="17">The infinite-dimensional proof is X2 and F2. The dashed line is the proved lower bound 1/2 for k ≠ 0.</text></g></svg>''')
out=root/'figures/compact-correction-and-obstruction.svg';out.write_text(''.join(p),'utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+out.name,'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'exact_parameters':{'modes':values,'nonconstant_lower_bound':'1/2','kernel':'constant mode','range':'zero-mean functions'},'proof_locators':['F2','X2','V0'],'actually_inspected':False,'exact_coordinate_review_complete':False}
(root/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8');print(json.dumps(record))
