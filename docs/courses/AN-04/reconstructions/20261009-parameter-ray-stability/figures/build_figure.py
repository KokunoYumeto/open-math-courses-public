"""CC0: exact normal excursions of the stated homogeneous quadratic family."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="470" viewBox="0 0 1040 470"><rect width="1040" height="470" fill="#f8fafc"/><style>text{font-family:Arial,sans-serif;fill:#172c3e}.title{font-size:18px;font-weight:bold}.label{font-size:15px}.small{font-size:14px}</style>',
'<text x="26" y="30" class="title">Reflections accumulate; the compressed limit remains a gliding ray</text><text x="26" y="55" class="label">pε = ξ² + (1 + ε)xη² − 2τη; η = 1, τ = a²/2, t = −2s. These panels show only normal position x.</text>']
panels=[('Change the operator; keep a = 0.20',[(.2,-.25,'#007c91'),(.2,0,'#aa552d'),(.2,.25,'#6f52a5')]),('Approach gliding; keep ε = 0',[(.24,0,'#007c91'),(.12,0,'#aa552d'),(.06,0,'#6f52a5')])]
for i,(title,curves) in enumerate(panels):
 left=24+i*516;px=left+52;bottom=332;width=424;height=210;maxx=.065
 parts += [f'<rect x="{left}" y="78" width="498" height="314" rx="8" fill="white" stroke="#d2dde7"/>',f'<text x="{left+12}" y="104" class="title">{title}</text>',f'<path d="M {px} 119 V {bottom} H {px+width}" fill="none" stroke="#7b8d9e"/>']
 for value in [0,.02,.04,.06]:
  yy=bottom-height*value/maxx
  parts += [f'<path d="M {px-4} {yy:.3f} H {px+width}" stroke="#e3eaf0"/>',f'<text x="{px-42}" y="{yy+5:.3f}" class="small">{value:.2f}</text>']
 for s in [0,.25,.5,.75,1]:
  xx=px+width*s
  parts += [f'<path d="M {xx} {bottom} V {bottom+4}" stroke="#7b8d9e"/>',f'<text x="{xx-8}" y="{bottom+22}" class="small">{s:g}</text>']
 parts += [f'<text x="{px+5}" y="121" class="label">x</text>',f'<text x="{px+width+8}" y="{bottom+4}" class="label">s</text>']
 for j,(a,eps,color) in enumerate(curves):
  k=1+eps;L=2*a/k;arcs=[];n=0
  while n*L<1:
   lo=n*L;hi=min((n+1)*L,1);delta=hi-lo
   # A quadratic Bezier traces the exact parabola, including a partial last arc.
   start=(px+width*lo,bottom)
   control=(px+width*(lo+delta/2),bottom-height*a*delta/maxx)
   end=(px+width*hi,bottom-height*(2*a*delta-k*delta*delta)/maxx)
   arcs.append(f'M {start[0]:.6f},{start[1]:.6f} Q {control[0]:.6f},{control[1]:.6f} {end[0]:.6f},{end[1]:.6f}')
   n+=1
  path=' '.join(arcs)
  parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2.2"/>')
  label=f'ε = {eps:+.2f}' if i==0 else f'a = {a:.2f}'
  parts.append(f'<text x="{left+20+j*157}" y="379" class="small" style="fill:{color}">{label}</text>')
 parts.append(f'<path d="M {px} {bottom} H {px+width}" fill="none" stroke="#172c3e" stroke-width="1.5" stroke-dasharray="4 4"/>')
parts += ['<text x="26" y="421" class="label">Exact period: 2a/(1 + ε). Exact height: a²/(1 + ε). Dashed boundary: the a = 0 gliding limit.</text>','<text x="26" y="450" class="label">Normal momentum changes sign at each hit; xξ stays continuous. Every displayed ray reaches t = −1 at s = 1/2.</text></svg>']
svg=ROOT/'figures/reflections-and-parameter-stability.svg';svg.write_text('\n'.join(parts)+'\n','utf-8')
(ROOT/'figure-check.json').write_text(json.dumps({'svg':svg.relative_to(ROOT).as_posix(),'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),'normal_position':'2*a*sigma-(1+epsilon)*sigma**2','period':'2*a/(1+epsilon)','height':'a**2/(1+epsilon)','hamilton_parameter_interval':[0,1],'left_amplitude':.2,'left_parameters':[-.25,0,.25],'right_parameter':0,'right_amplitudes':[.24,.12,.06],'wave_amplitude_plotted':False,'actually_inspected':False},indent=2)+'\n','utf-8')
print('Wrote exact parameter and gliding-limit excursion figure.')
