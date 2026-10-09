"""Clock-coordinate projections and sampled logarithmic commutant profiles."""
from pathlib import Path
import math,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="500" viewBox="0 0 1040 500"><rect width="1040" height="500" fill="#f8fafc"/><style>text{font-family:Arial,sans-serif;fill:#172c3e}.title{font-size:18px;font-weight:bold}.label{font-size:15px}.small{font-size:14px}</style>',
'<text x="24" y="29" class="title">One geometric neighborhood, different clocks and damping constants</text>',
'<text x="24" y="54" class="label">Left: boundary-symbol clock coordinates. Right: a commutant symbol, not a solution amplitude.</text>']
colors=['#007c91','#aa552d','#6f52a5']
for i,title in enumerate(['Changing operator: a = −1/4, 0, 1/4','Changing damping: A = 1, 4, 16']):
 left=24+i*516;px=left+54;bottom=338;width=408;height=208
 parts += [f'<rect x="{left}" y="78" width="496" height="327" rx="8" fill="white" stroke="#d2dde7"/>',f'<text x="{left+12}" y="104" class="title">{title}</text>']
 if i==0:
  parts.append(f'<path d="M {px} 126 V {bottom} H {px+width}" fill="none" stroke="#7b8d9e"/>')
  for value in [0,.5,1,1.5]:
   yy=bottom-height*value/1.8
   parts += [f'<path d="M {px} {yy:.3f} H {px+width}" stroke="#e1e9ef"/>',f'<text x="{px-31}" y="{yy+5:.3f}" class="small">{value:g}</text>']
  for j,a in enumerate([-.25,0,.25]):
   speed=2*(1+a)/math.sqrt(2+a)
   parts.append(f'<path d="M {px} {bottom} L {px+width} {bottom-height*speed/1.8:.6f}" fill="none" stroke="{colors[j]}" stroke-width="2.2"/>')
   parts.append(f'<text x="{left+20+j*149}" y="391" class="small" style="fill:{colors[j]}">a = {a:+.2f}</text>')
  parts += [f'<text x="{px+5}" y="125" class="label">z₁ / δ</text>',f'<text x="{px+width/2}" y="{bottom+35}" text-anchor="middle" class="label">Nₐ / δ</text>']
  ticks=[(0,'0'),(.5,'0.5'),(1,'1')]
 else:
  parts.append(f'<path d="M {px} 126 V {bottom} H {px+width}" fill="none" stroke="#7b8d9e"/>')
  for value in [0,-10,-20,-30,-40,-50]:
   yy=130-height*value/55
   parts += [f'<path d="M {px} {yy:.3f} H {px+width}" stroke="#e1e9ef"/>',f'<text x="{px-34}" y="{yy+5:.3f}" class="small">{value:g}</text>']
  for j,A in enumerate([1,4,16]):
   pts=[]
   for k in range(151):
    X=1.35*k/150;logq=-A/((1.5-X)*math.log(10))
    pts.append((px+width*X/1.5,130-height*logq/55))
   d='M '+' L '.join(f'{xx:.5f},{yy:.5f}' for xx,yy in pts)
   parts.append(f'<path d="{d}" fill="none" stroke="{colors[j]}" stroke-width="2.2"/>')
   parts.append(f'<text x="{left+20+j*149}" y="391" class="small" style="fill:{colors[j]}">A = {A}</text>')
  parts += [f'<path d="M {px+width} 126 V {bottom}" stroke="#172c3e" stroke-dasharray="4 4"/>',f'<text x="{px+5}" y="124" class="label">log₁₀ q</text>',f'<text x="{px+width/2}" y="{bottom+35}" text-anchor="middle" class="label">X = x / (εδ)</text>']
  ticks=[(0,'0'),(.5,'0.75'),(1,'1.5')]
 for frac,label in ticks:
  xx=px+width*frac
  parts.append(f'<text x="{xx-7}" y="{bottom+18}" class="small">{label}</text>')
parts += ['<text x="24" y="435" class="label">Clock speed: 2(1 + a) / √(2 + a). Every parameter uses the same clock interval 0 ≤ Nₐ / δ ≤ 1.</text>',
'<text x="24" y="461" class="label">log₁₀ q = −A / [(3/2 − X) log 10], sampled for 0 ≤ X ≤ 1.35. All supports end at X = 1.5.</text>',
'<text x="24" y="487" class="label">The full phase coordinates and the distinction between boundary-symbol flow and a full ray are stated in F0.</text></svg>']
svg=ROOT/'figures/uniform-glancing-supports.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(ROOT/'figure-check.json').write_text(json.dumps({'svg':svg.relative_to(ROOT).as_posix(),'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'left_parameters':[-.25,0,.25],'left_coordinates':'z1/delta versus N_a/delta on the boundary-symbol orbit; not a full p_a trajectory',
 'right_damping':[1,4,16],'right_coordinates':'log10 q versus X=x/(epsilon*delta)',
 'right_sample_interval':[0,1.35],'right_samples_per_curve':151,'common_positivity_interval':[0,1.5],
 'wave_amplitude_plotted':False,'actually_inspected':False},indent=2)+'\n','utf-8')
print('Wrote uniform clock and damping-support figure.')
