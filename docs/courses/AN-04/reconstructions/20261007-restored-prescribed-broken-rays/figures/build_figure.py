"""Draw the exact finite strip ray and its quadratic compressed normal component."""
from pathlib import Path
import hashlib, json, xml.etree.ElementTree as ET
r = Path(__file__).resolve().parents[1]
dest = r / 'figures/prescribed-broken-ray-geometry.svg'
dest.parent.mkdir(parents=True, exist_ok=True)
x = lambda t: 100 + 200*t
y = lambda z: 530 - 180*z
pieces = [(0,.5,-1,0,.25),(.5,1.5,1,-2,.75),
          (1.5,2.5,-1,4,-3.75),(2.5,3,1,-6,8.75)]
# Each tuple records zeta = -(A t^2+B t+C), keeping exact quarter constants.
quadratics = [(1,0,-.25),(-1,2,-.75),(1,-4,3.75),(-1,6,-8.75)]
curves = []
checks = []
for (lo,hi,*_), (aa,bb,cc) in zip(pieces, quadratics):
    f = lambda t: aa*t*t+bb*t+cc
    dt = hi-lo
    z0,z1 = f(lo),f(hi)
    control = z0 + (2*aa*lo+bb)*dt/2
    curves.append(f'<path d="M{x(lo):g},{y(z0):g} Q{x((lo+hi)/2):g},{y(control):g} {x(hi):g},{y(z1):g}" fill="none" stroke="#236985" stroke-width="3.5"/>')
    for j in range(21):
        u = j/20
        t = lo + dt*u
        bezier = (1-u)**2*z0 + 2*(1-u)*u*control + u*u*z1
        assert abs(bezier-f(t)) < 1e-12
        checks.append({'t':t, 'zeta':f(t), 'bezier':bezier})
poly = [(0,.5),(.5,1),(1.5,0),(2.5,1),(3,.5)]
base = ' '.join(f'{x(t):g},{315-180*rr:g}' for t,rr in poly)
arrows = []
for (t0,r0),(t1,r1) in zip(poly, poly[1:]):
    pts = []
    for u in [.42,.60]:
        pts.append((x(t0+(t1-t0)*u),315-180*(r0+(r1-r0)*u)))
    arrows.append(f'<path d="M{pts[0][0]:g},{pts[0][1]:g} L{pts[1][0]:g},{pts[1][1]:g}" stroke="#236985" stroke-width="3.5" marker-end="url(#blueArrow)"/>')
svg = """<svg xmlns="http://www.w3.org/2000/svg" width="780" height="710" viewBox="0 0 780 710" role="img" aria-labelledby="title desc">
<title id="title">A finite reflected strip ray and its endpoint forcing</title>
<desc id="desc">The exact four base segments from time zero to three reflect at the upper, lower and upper walls. Only the two interior endpoints carry forcing singularities. The lower panel plots zeta equals r times one minus r times rho, which is zero at both walls.</desc>
<defs>
<marker id="blueArrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="#236985"/></marker>
<marker id="grayArrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0 L7 3.5 L0 7 Z" fill="#70818a"/></marker>
</defs>
<rect x="16" y="16" width="748" height="370" rx="16" fill="#f6f8fa"/>
<rect x="16" y="400" width="748" height="290" rx="16" fill="#f6f8fa"/>
<g font-family="Arial,sans-serif" fill="#263c48">
<text x="38" y="50" font-size="22" font-weight="700">A finite strip ray, τ = 1</text>
<text x="38" y="80" font-size="17">Blue: solution singularities. Red: endpoint forcing.</text>
<path d="M80 336 V115 M80 336 H728" fill="none" stroke="#83939b" stroke-width="1.6" marker-end="url(#grayArrow)"/>
<text x="59" y="113" font-size="18">r</text><text x="738" y="341" font-size="18">t</text>
<path d="M100 135 H715 M100 315 H715" stroke="#b2bec5" stroke-width="1.4"/>
<text x="61" y="141" font-size="16">1</text><text x="62" y="321" font-size="16">0</text>
""" + f'<polyline points="{base}" fill="none" stroke="#236985" stroke-width="3.5"/>' + """
""" + ''.join(arrows) + """
<circle cx="100" cy="225" r="6" fill="#b84d36"/><circle cx="700" cy="225" r="6" fill="#b84d36"/>
<circle cx="200" cy="135" r="4" fill="#236985"/><circle cx="400" cy="315" r="4" fill="#236985"/><circle cx="600" cy="135" r="4" fill="#236985"/>
<text x="107" y="120" font-size="17">ρ = −1</text>
<text x="291" y="190" font-size="17">ρ = 1</text>
<text x="489" y="190" font-size="17">ρ = −1</text>
<text x="633" y="156" font-size="17">ρ = 1</text>
<text x="95" y="362" font-size="16">0</text><text x="187" y="362" font-size="16">1/2</text><text x="387" y="362" font-size="16">3/2</text><text x="587" y="362" font-size="16">5/2</text><text x="695" y="362" font-size="16">3</text>
<text x="38" y="433" font-size="22" font-weight="700">Compressed normal component ζ = r(1−r)ρ</text>
<text x="38" y="460" font-size="16">The two walls remain different base points; both have ζ = 0.</text>
<path d="M100 592 V473 M100 592 H728" fill="none" stroke="#83939b" stroke-width="1.6" marker-end="url(#grayArrow)"/>
<text x="90" y="475" font-size="18">ζ</text><text x="738" y="598" font-size="18">t</text>
<path d="M100 530 H720" stroke="#b2bec5" stroke-width="1"/>
<text x="61" y="490" font-size="16">1/4</text><text x="78" y="536" font-size="16">0</text><text x="51" y="581" font-size="16">−1/4</text>
""" + ''.join(curves) + """
<circle cx="100" cy="575" r="5" fill="#b84d36"/><circle cx="700" cy="485" r="5" fill="#b84d36"/>
<text x="95" y="618" font-size="16">0</text><text x="187" y="618" font-size="16">1/2</text><text x="387" y="618" font-size="16">3/2</text><text x="587" y="618" font-size="16">5/2</text><text x="695" y="618" font-size="16">3</text>
<text x="38" y="657" font-size="16">Arrows use physical time; s = −t/2 gives Hamilton orientation.</text>
</g></svg>
"""
ET.fromstring(svg)
dest.write_text(svg, encoding='utf8')
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
record = {
    'schema':'an04-prescribed-broken-ray-figure/v1',
    'asset':str(dest.relative_to(r)).replace('\\','/'), 'sha256':sha(dest),
    'coordinate_section':'tau=1; four rho branches -1,+1,-1,+1',
    'base_map':'(t,r)->(100+200t,315-180r)',
    'compressed_map':'(t,zeta)->(100+200t,530-180zeta)',
    'zeta_definition':'r(1-r)rho, pairing with a global compressed normal frame',
    'quadratic_coefficients':quadratics, 'exact_bezier_checks':checks,
    'proof_locators':['BG3-BG4','BG31-BG32'], 'exact_coordinate_sections':True,
    'schematic':False, 'original_licence':'CC0-1.0', 'script_sha256':sha(Path(__file__))}
(r/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figure_written':True,'exact_quadratic_checks':len(checks)}))
