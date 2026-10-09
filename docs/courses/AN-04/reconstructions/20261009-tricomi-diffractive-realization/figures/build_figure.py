"""CC0: exact projections of one Tricomi characteristic; no sampled PDE solution."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="470" viewBox="0 0 1040 470"><rect width="1040" height="470" fill="#f8fafc"/><style>text{font-family:Arial,sans-serif;fill:#172c3e}.title{font-size:19px;font-weight:bold}.label{font-size:15px}.small{font-size:14px}.axis{stroke:#74889a;stroke-width:1.3}</style>',
'<text x="28" y="30" class="title">One ray, three projections</text><text x="28" y="56" class="label">p = ξ² − xη²; η = 1; y₀ = 0; −1 ≤ τ ≤ 1. Positive covector dilations are suppressed.</text>']
specs=[('Base (y, x)',lambda t:-2*t**3/3,0.8,'y','y = −⅔τ³'),('Ordinary normal phase (ξ, x)',lambda t:t,1.2,'ξ','ξ = τ'),('Compressed normal phase (ζ, x)',lambda t:t**3,1.2,'ζ = xξ','ζ = τ³')]
for i,(title,h,limit,label,formula) in enumerate(specs):
    left=24+i*340;cx=left+160;bottom=345;scale=210
    X=lambda t:cx+130*h(t)/limit
    Y=lambda t:bottom-scale*t*t
    parts += [f'<rect x="{left}" y="82" width="324" height="310" rx="8" fill="white" stroke="#d2dde7"/>',
     f'<text x="{left+12}" y="108" class="title">{title}</text>',
     f'<path d="M {left+20} {bottom} H {left+305} M {cx} {bottom+10} V 124" class="axis" fill="none"/>',
     f'<text x="{cx+7}" y="127" class="label">x</text><text x="{left+252}" y="{bottom+25}" class="label">{label}</text>',
     f'<path d="M {cx-4} {bottom-scale} H {cx+4}" class="axis"/><text x="{cx-18}" y="{bottom+19}" class="small">0</text><text x="{cx-18}" y="{bottom-scale+4}" class="small">1</text>']
    for a,b,color in [(-1,0,'#007c91'),(0,1,'#ba4b24')]:
        ts=[a+(b-a)*j/120 for j in range(121)]
        d='M '+' L '.join(f'{X(t):.4f} {Y(t):.4f}' for t in ts)
        parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3"/>')
        # Arrow is the exact projection tangent at a regular sample.
        t=(a+b)/2;eps=0.002;dx=X(t+eps)-X(t-eps);dy=Y(t+eps)-Y(t-eps)
        norm=(dx*dx+dy*dy)**0.5;dx/=norm;dy/=norm
        px=X(t);py=Y(t)
        pts=[(px+6*dx,py+6*dy),(px-5*dx+4*dy,py-5*dy-4*dx),(px-5*dx-4*dy,py-5*dy+4*dx)]
        parts.append('<polygon points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)+f'" fill="{color}"/>')
    parts += [f'<circle cx="{cx}" cy="{bottom}" r="4.5" fill="#172c3e"/>',
     f'<text x="{left+14}" y="380" class="label">x = τ²; {formula}</text>']
parts += ['<text x="28" y="419" class="label" style="fill:#007c91">τ &lt; 0: incoming leg</text><text x="288" y="419" class="label" style="fill:#ba4b24">τ &gt; 0: outgoing leg</text>',
'<text x="28" y="448" class="label">At τ = 0: base velocity = 0, but ordinary phase velocity has dξ/dτ = 1. The Hamilton flow continues.</text></svg>']
out=ROOT/'figures/tricomi-ray-projections.svg';out.write_text('\n'.join(parts)+'\n','utf-8')
(ROOT/'figure-check.json').write_text(json.dumps({'svg':out.relative_to(ROOT).as_posix(),'svg_sha256':sha(out),'generator_sha256':sha(Path(__file__)),'coordinates':{'x':'tau**2','y':'-2*tau**3/3','xi':'tau','zeta':'tau**3','eta':1},'parameter_interval':[-1,1],'wave_amplitude_plotted':False,'actually_inspected':False},indent=2)+'\n','utf-8')
print('Wrote exact three-projection figure.')
