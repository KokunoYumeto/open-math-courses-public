"""Exact flat-boundary geometry and the positive derivative-energy ellipse."""
from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib
root=Path(__file__).resolve().parent
out=root/'figures/mixed-dirichlet-flux-and-energy.svg'
out.parent.mkdir(exist_ok=True)
rows=[];points=[]
for k in range(361):
    theta=2*math.pi*k/360
    ut=math.cos(theta)/math.sqrt(3)+math.sin(theta)
    ur=math.cos(theta)/math.sqrt(3)-math.sin(theta)
    energy=ut*ut+ur*ur+ut*ur
    assert abs(energy-1)<2e-14
    rows.append({'theta':theta,'u_t':ut,'u_r':ur,'energy':energy})
    points.append(f'{825+96*ut:.6f},{310-96*ur:.6f}')
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" role="img" aria-labelledby="title desc">
<title id="title">An inward timelike multiplier and a boundary wave</title>
<desc id="desc">Left: the flat physical half-space r greater than zero, with metric dt squared minus dr squared. F=(1/2,1) is inward timelike, and a boundary signal at a=1 travels on the null ray t=1+r. Right: the real derivative-component ellipse u_t squared plus u_r squared plus u_t u_r equals one, whose eigenvalues are 3/2 and 1/2.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>
<rect width="1100" height="680" rx="10" fill="#fffdf7"/>
<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#203946}.title{font-size:26px;font-weight:bold}.small{font-size:18px}.axis{stroke:#64727b;stroke-width:1.5;marker-end:url(#arrow)}.ray{stroke:#146b8d;stroke-width:4;marker-end:url(#arrow)}.inward{stroke:#ad4234;stroke-width:4;marker-end:url(#arrow)}.ellipse{stroke:#5b784b;stroke-width:3;fill:none}</style>
<text x="30" y="42" class="title">Why the boundary estimate needs an inward timelike vector</text>
<text x="30" y="77">Flat model: L = partial_t^2 - partial_r^2; kappa = 1/2</text>
<text x="60" y="126">Physical (r,t) plane</text>
<text x="633" y="126">Derivative-component (u_t,u_r) plane</text>
<rect x="100" y="155" width="350" height="275" fill="#eef4f8"/>
<path d="M100 450V158" stroke="#243946" stroke-width="4"/>
<path class="axis" d="M80 430H465M100 450V148"/>
<text x="447" y="458">r</text><text x="76" y="156">t</text>
<text x="320" y="420" class="small">r &gt; 0</text>
<path d="M100 430L330 200" stroke="#89969d" stroke-width="2" stroke-dasharray="7 5"/>
<text x="337" y="203" class="small">t = r</text>
<path class="ray" d="M100 330L250 180"/>
<circle cx="100" cy="330" r="4" fill="#146b8d"/>
<text x="16" y="319" class="small">b(a)</text><text x="18" y="344" class="small">a = 1</text>
<text x="262" y="178" class="small">t = a + r</text>
<path class="inward" d="M100 430L150 330"/>
<text x="205" y="390">F = (1/2,1)</text>
<text x="123" y="474" class="small">boundary: r = 0</text>
<path class="axis" d="M675 310H1025M825 455V155"/>
<text x="991" y="337">u_t</text><text x="845" y="175">u_r</text>
<polyline class="ellipse" points="ELLIPSE_POINTS"/>
<path class="ray" d="M825 310LPLUS_X PLUS_Y"/>
<path class="inward" d="M825 310L921 406"/>
<text x="877" y="235" class="small">lambda+ = 3/2</text>
<text x="929" y="429" class="small">lambda- = 1/2</text>
<text x="595" y="490">u_t^2 + u_r^2 + u_t u_r = 1</text>
<text x="30" y="526">g(F,F) = 3/4 &gt; 0; F^r = 1/2 &gt; 0</text>
<text x="30" y="562">Zero Dirichlet flux: -J^r = |u_r|^2 / 2</text>
<text x="595" y="531" class="small">Semiaxes: sqrt(2/3) along (1,1),</text>
<text x="595" y="562" class="small">sqrt(2) along (1,-1).</text>
<text x="30" y="609" class="small">The two panels use different coordinates. The right panel sets u = 0 and has no y-derivative.</text>
<text x="30" y="646" class="small">DC9, DC12 and Exercises 1-2. Exact rays and 361 ellipse samples. Original figure: CC0-1.0.</text>
</svg>
'''
svg=svg.replace('ELLIPSE_POINTS',' '.join(points)).replace('PLUS_X',f'{825+96/math.sqrt(3):.6f}').replace('PLUS_Y',f'{310-96/math.sqrt(3):.6f}')
out.write_text(svg,'utf-8')
record={'schema':'AN04-mixed-dirichlet-figure/v1','recorded_utc':datetime.now(timezone.utc).isoformat(),
    'figure':'figures/'+out.name,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'script':'build_figure.py','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'sample_count':len(rows),'samples':rows,'passed':True,
    'left_coordinates':{'origin_pixels':[100,430],'units_to_pixels':100,'axes':['r','t'],'time_pixel_sign':-1,
        'boundary_signal_time':1,'signal_ray':'t=1+r','multiplier_components':[0.5,1],'metric_square':0.75,'outward_dirichlet_flux_coefficient':0.5},
    'right_coordinates':{'origin_pixels':[825,310],'units_to_pixels':96,'axes':['u_t','u_r'],'second_pixel_sign':-1,
        'energy':'u_t^2+u_r^2+u_t*u_r','eigenvalues':[1.5,0.5],'semiaxis_lengths':[math.sqrt(2/3),math.sqrt(2)]},
    'scope':'Exact flat two-variable model and real derivative energy; no general curved-boundary ray claim.',
    'actual_reader_inspection_pending':True,'general_proof_certified_by_samples':False,'licence':'CC0-1.0'}
(root/'figure-samples.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'samples':len(rows),'passed':True,'figure':out.name}))
