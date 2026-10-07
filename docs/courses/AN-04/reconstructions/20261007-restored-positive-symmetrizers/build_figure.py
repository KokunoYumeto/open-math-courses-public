"""Render the exact sheared component-energy circle and record its sampled model."""
from pathlib import Path
import datetime,hashlib,json,math
r=Path(__file__).resolve().parents[4];c=Path(__file__).resolve().parent
f=c/'figures/variable-symmetrizer-energy-ellipse.svg'
rows=[];circle=[];ellipse=[]
scale=112
for k in range(361):
    theta=2*math.pi*k/360
    v1,v2=math.cos(theta),math.sin(theta)
    u1,u2=v1+v2,v2
    metric=(u1-u2)**2+u2*u2
    assert abs(metric-1)<1e-14
    rows.append({'theta':theta,'v':[v1,v2],'u':[u1,u2],'S_norm_squared':metric})
    circle.append(f'{260+scale*v1:.6f},{350-scale*v2:.6f}')
    ellipse.append(f'{755+scale*u1:.6f},{350-scale*u2:.6f}')
svg=[
'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" role="img" aria-labelledby="title desc">',
'<title id="title">A positive metric for nonorthogonal polarization</title>',
'<desc id="desc">The shear T=(1,1;0,1) maps the unit circle to the component-energy ellipse (u1-u2)^2+u2^2=1. Images of the two coordinate vectors are (1,0) and (1,1); they are orthonormal for S=(1,-1;-1,2), rather than for the Euclidean metric.</desc>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>',
'<rect width="1100" height="680" rx="10" fill="#fffdf7"/>',
'<style>text{font-family:Arial,sans-serif;font-size:21px;fill:#243943}.title{font-size:27px;font-weight:bold}.small{font-size:19px}.axis{stroke:#586770;stroke-width:1.5;marker-end:url(#arrow)}.blue{stroke:#12698b;stroke-width:4;marker-end:url(#arrow)}.red{stroke:#aa3a36;stroke-width:4;marker-end:url(#arrow)}.curve{stroke:#5d7750;stroke-width:3;fill:none}.grid{stroke:#e2dfd2;stroke-width:1}</style>',
'<text x="36" y="43" class="title">Positive energy in a sheared component frame</text>',
'<text x="36" y="79">b = 1: u = T v = (v1 + v2, v2)</text>',
'<text x="88" y="135">v component plane</text>',
'<text x="610" y="135">u component plane</text>',
'<path class="grid" d="M80 238H438M80 462H438M148 172V525M372 172V525M550 238H982M550 462H982M643 172V525M867 172V525"/>',
'<path class="axis" d="M65 350H455M260 530V165M545 350H995M755 530V165"/>',
'<text x="433" y="382">v1</text><text x="278" y="180">v2</text>',
'<text x="965" y="382">u1</text><text x="773" y="180">u2</text>',
'<polyline class="curve" points="'+' '.join(circle)+'"/>',
'<polyline class="curve" points="'+' '.join(ellipse)+'"/>',
'<path class="blue" d="M260 350H372"/><path class="red" d="M260 350V238"/>',
'<path class="blue" d="M755 350H867"/><path class="red" d="M755 350L867 238"/>',
'<text x="354" y="329">e+</text><text x="277" y="238">e-</text>',
'<text x="871" y="333">(1,0)</text><text x="878" y="227">(1,1)</text>',
'<path class="axis" d="M450 295H556"/><text x="491" y="279">T</text>',
'<text x="75" y="575">v1^2 + v2^2 = 1</text>',
'<text x="610" y="575">(u1 - u2)^2 + u2^2 = 1</text>',
'<text x="610" y="610" class="small">S = (1,-1; -1,2); T^T S T = I</text>',
'<text x="36" y="650" class="small">Exercise 8.1 and SM9/SM13. 361 samples of the exact parameterization. Original figure: CC0-1.0.</text>',
'</svg>']
f.write_text('\n'.join(svg)+'\n',encoding='utf8')
record={'schema':'an04-variable-symmetrizer-energy-figure/v1',
    'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'figure':'figures/'+f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
    'sample_count':len(rows),'samples':rows,'passed':True,
    'model':'b=1; u=T v; S=T^(-T)T^(-1); component ellipse, not physical rays',
    'numerically_sampled_exact_parameterization':True,'general_proof_certified_by_samples':False,
    'actual_reader_inspection_pending':True,'original_content_licence':'CC0-1.0',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(c/'figure-samples.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figure_created':True,'samples':len(rows)}))
