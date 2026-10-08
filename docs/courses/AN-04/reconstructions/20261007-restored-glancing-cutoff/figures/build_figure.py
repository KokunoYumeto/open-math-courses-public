"""Exact coordinate plots of GS9 and the sharp scalar example after GS13."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="920" height="480" viewBox="0 0 920 480" role="img" aria-labelledby="title desc">
<title id="title">The same scale ratio controls the derivative and mixed error</title>
<desc id="desc">For theta equal to delta divided by epsilon between zero and one quarter, the left exact curve is one minus twice square root theta, and the right is square root theta. At theta one sixteenth they equal one half and one quarter respectively. Zero is a limiting ratio. Both curves use exact quadratic parametrizations, and the vertical scales differ.</desc>
<rect width="920" height="480" fill="white"/>
<g font-family="Arial,sans-serif" fill="#263c48">
<text x="25" y="33" font-size="23" font-weight="700">One ratio: θ = δ/ε</text>
<text x="25" y="61" font-size="16">Exact characteristic model and exact scalar mixed error · GS9 and GS13</text>
<text x="55" y="103" font-size="19" font-weight="700">Hamilton derivative: 1 − 2√θ</text>
<text x="510" y="103" font-size="19" font-weight="700">Mixed error: √θ</text>
<path d="M100 125 V360 H400 M560 125 V360 H860" fill="none" stroke="#849ba5" stroke-width="1.5"/>
<path d="M100 247.5 H380 M170 247.5 V360 M560 247.5 H840 M630 247.5 V360" fill="none" stroke="#99adb8" stroke-width="1.3" stroke-dasharray="5 4"/>
<path d="M100 135 Q100 247.5 380 360" fill="none" stroke="#236985" stroke-width="3.5"/>
<path d="M560 360 Q560 247.5 840 135" fill="none" stroke="#925a31" stroke-width="3.5"/>
<circle cx="170" cy="247.5" r="4.5" fill="#236985"/><circle cx="630" cy="247.5" r="4.5" fill="#925a31"/>
<text x="75" y="140" font-size="16">1</text><text x="55" y="253" font-size="16">1/2</text><text x="76" y="382" font-size="16">0</text>
<text x="513" y="140" font-size="16">1/2</text><text x="513" y="253" font-size="16">1/4</text><text x="535" y="382" font-size="16">0</text>
<text x="153" y="384" font-size="16">1/16</text><text x="365" y="384" font-size="16">1/4</text><text x="406" y="366" font-size="18">θ</text>
<text x="613" y="384" font-size="16">1/16</text><text x="825" y="384" font-size="16">1/4</text><text x="866" y="366" font-size="18">θ</text>
<text x="55" y="425" font-size="16">Vφ ≥ 1/2 exactly when θ ≤ 1/16 in this model.</text>
<text x="510" y="425" font-size="16">The error tends to zero when δ/ε tends to zero.</text>
<text x="25" y="459" font-size="15">Same horizontal scale; different vertical scales. θ = 0 is a limit. General sufficient constants are in GS5.</text>
</g></svg>'''
ET.fromstring(svg)
asset=ROOT/'figures/two-scale-derivative-and-error.svg';asset.write_text(svg,encoding='utf-8')
points=[]
for i in range(41):
    u=F(i,80);v=2*u;theta=u*u
    x=100*(1-v)**2+200*(1-v)*v+380*v*v
    left=135*(1-v)**2+495*(1-v)*v+360*v*v
    right=360*(1-v)**2+495*(1-v)*v+135*v*v
    assert x==100+1120*theta
    assert left==360-225*(1-2*u) and right==360-450*u
    points.append({'u':str(u),'theta':str(theta),'left_value':str(1-2*u),'right_value':str(u)})
assert F(1,4)**2==F(1,16) and 1-2*F(1,4)==F(1,2)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'AN04-glancing-cutoff-figure/v1','asset':'figures/'+asset.name,
 'sha256':sha(asset),'source_sha256':sha(ROOT/'glancing-cutoff-scales-preparation.md'),
 'script_sha256':sha(Path(__file__)),'proof_locators':['GS9','sharp example following GS13'],
 'exact_coordinate_checks':points,'parameter':'u=sqrt(theta), 0<=u<=1/2',
 'pixel_maps':'left x=100+1120theta, y=360-225(1-2u); right x=560+1120theta, y=360-450u',
 'sampled_plot':False,'exact_quadratic_bezier_curves':True,'different_vertical_scales_labelled':True,
 'original_licence':'CC0-1.0','actually_inspected':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print({'exact_rational_coordinate_checks':len(points),'visual_inspection_pending':True})
