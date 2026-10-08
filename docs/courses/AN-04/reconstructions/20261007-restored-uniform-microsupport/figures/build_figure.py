"""Exact sample coordinates for the two frequency obstructions in U058."""
from pathlib import Path
import json,hashlib,math
root=Path(__file__).resolve().parents[1]
source=root/'uniform-microsupport-and-dual-sources.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="780" height="650" viewBox="0 0 780 650" role="img" aria-labelledby="title desc">',
'<title id="title">Uniform microsupport and the missing half order</title>',
'<desc id="desc">Four finite possible frequency bands N/2 to 2N with the exact mode N; four samples of the unbounded one-mode pairing (1+m squared) to the one-quarter power, compared with two unit weighted norms.</desc>',
'<rect width="780" height="650" fill="#ffffff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#182a3b;font-size:17px}.small{font-size:15px}.title{font-size:21px;font-weight:bold}.grid{stroke:#dde5ea}.axis{stroke:#475569;stroke-width:1.5}</style>',
'<text x="24" y="32" class="title">Finite rank in each row; no uniform frequency decay</text>',
'<text x="24" y="60">Bands contain the support. Dots mark b_N(N) = 1.</text>']
rows=[]
for i,N in enumerate([4,8,16,32]):
 y=100+35*i
 lo,center,hi=[100+9*v for v in [N/2,N,2*N]]
 parts.extend([f'<text x="25" y="{y+6}">N = {N}</text>',
 f'<line x1="{lo}" y1="{y}" x2="{hi}" y2="{y}" stroke="#b7dce5" stroke-width="12"/>',
 f'<circle cx="{lo}" cy="{y}" r="5" fill="white" stroke="#43808d"/>',
 f'<circle cx="{hi}" cy="{y}" r="5" fill="white" stroke="#43808d"/>',
 f'<circle cx="{center}" cy="{y}" r="6" fill="#075a70"/>'])
 rows.append({'N':N,'open_containing_band':[N/2,2*N],'central_mode':N,'multiplier_at_center':1})
parts.append('<line x1="100" y1="242" x2="714" y2="242" class="axis"/>')
for n in [0,16,32,48,64]:
 x=100+9*n
 parts.extend([f'<line x1="{x}" y1="237" x2="{x}" y2="248" class="axis"/>',f'<text x="{x}" y="272" text-anchor="middle">{n}</text>'])
parts.extend(['<text x="719" y="245">n</text>',
'<text x="24" y="315" class="title">One-mode source obstruction at s = 1</text>',
'<text x="24" y="343">Pairing = (1 + m²)¹/⁴; each proposed weighted norm = 1</text>',
'<text x="24" y="367" class="small">Exact formula samples; horizontal positions label the selected modes.</text>'])
def yy(v):return 583-11*v
for value in [0,4,8,12,16]:
 y=yy(value)
 parts.extend([f'<line x1="90" y1="{y}" x2="710" y2="{y}" class="grid"/>',f'<text x="75" y="{y+6}" text-anchor="end">{value}</text>'])
parts.append(f'<line x1="90" y1="{yy(1)}" x2="710" y2="{yy(1)}" stroke="#9d5100" stroke-width="2" stroke-dasharray="6 5"/>')
samples=[]
for i,m in enumerate([2,16,64,256]):
 value=(1+m*m)**.25;x=155+165*i;y=yy(value)
 assert math.isclose(value**4,1+m*m,rel_tol=1e-12)
 parts.extend([f'<circle cx="{x}" cy="{y:.8f}" r="6" fill="#075a70"/>',
 f'<text x="{x+12}" y="{y-12:.4f}" class="small">{value:.3f}</text>',
 f'<text x="{x}" y="614" text-anchor="middle">m = {m}</text>'])
 samples.append({'m':m,'pairing':value,'source_weighted_norm':1,'solution_weighted_norm':1})
parts.extend(['<text x="385" y="646" class="small">Proofs: Exercises 1–2, equations UM20–UM25.</text>','</svg>'])
asset=root/'figures/frequency-drift.svg';asset.write_text('\n'.join(parts)+'\n',encoding='utf-8')
record={'passed':True,'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'asset':'figures/frequency-drift.svg','sha256':sha(asset),'bands':rows,'pairing_samples':samples,
 'exact_coordinate_checks':['Every band has endpoints N/2 and 2N.','Open endpoints distinguish possible support from a filled multiplier profile.',
 'Every center is the integer mode N with exact multiplier one.','Every pairing value has fourth power 1+m squared.',
 'Both proposed weighted norms equal one for every sample.','The unit comparison line uses the same vertical scale as pairing samples.'],
 'actually_inspected':False,'general_unboundedness_proved_in_lesson_not_by_samples':True}
(root/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':record['asset'],'passed':True,'bands':len(rows),'samples':len(samples)}))
