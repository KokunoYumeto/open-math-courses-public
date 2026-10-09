"""CC0 original diagram; exact formula plus labelled numerical samples.

Uses only the Python standard library. SVG text uses installed viewer fonts;
no font bytes or glyph outlines are embedded.
"""
import argparse
import html
import json
import math
from pathlib import Path


def sample(x):
    r = 1/x + 1/(1-x)
    derivative = -1/x**2 + 1/(1-x)**2
    alpha = 1/math.sqrt(1+derivative**2)
    return dict(x=x, r=r, derivative=derivative, alpha=alpha)


def generate():
    samples = [sample(i/500) for i in range(1,500)]
    assert sample(.5)['alpha'] == 1
    assert all(0 < p['alpha'] <= 1 for p in samples)
    assert max(abs(sample(i/500)['alpha']-sample(1-i/500)['alpha']) for i in range(1,500)) < 1e-13
    points = ' '.join(f"{80+600*p['x']:.4f},{335-128*p['alpha']:.4f}" for p in samples)
    parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="1000" viewBox="0 0 760 1000">
<metadata>Original mathematical expression and generator: CC0 1.0 to the extent of rights held. Exact example: T=(0,1), g=dx^2, r=1/x+1/(1-x), alpha=(1+(r')^2)^(-1/2). Curve points are numerical samples, not a proof. Proof: Theorem11BM.1, WN.1-11, WB.1-6, Exercises291-293. Historical context: Connes, A survey of foliations and operator algebras, Section8. Full inverse coefficient: Theorem7.17. System fonts are not embedded.</metadata>
<rect width="760" height="1000" fill="white"/>
<g font-family="sans-serif" fill="#132a43">
<text x="30" y="40" font-size="27" font-weight="bold">Complete metric, unchanged normal phase</text>
<text x="30" y="73" font-size="22">A positive weight on the original normal Hilbert space</text>
<rect x="25" y="98" width="710" height="332" rx="14" fill="#edf6f7" stroke="#b1cfd4"/>
<text x="45" y="132" font-size="24" font-weight="bold">1. Exact incomplete interval example</text>
<text x="45" y="164" font-size="22">T = (0,1), g = dx²; original total length is 1</text>
<line x1="80" y1="188" x2="680" y2="188" stroke="#556b7f" stroke-width="3"/>
<circle cx="80" cy="188" r="6" fill="white" stroke="#556b7f" stroke-width="2"/>
<circle cx="680" cy="188" r="6" fill="white" stroke="#556b7f" stroke-width="2"/>
<line x1="80" y1="335" x2="680" y2="335" stroke="#8295a6"/>
<line x1="80" y1="207" x2="80" y2="335" stroke="#8295a6"/>
<text x="57" y="215" font-size="20">1</text>
<text x="58" y="339" font-size="20">0</text>
<text x="77" y="360" font-size="20">0</text>
<text x="353" y="360" font-size="20">1/2</text>
<text x="674" y="360" font-size="20">1</text>
<text x="100" y="233" font-size="22" fill="#086574">α(x): numerical samples</text>
''', f'<polyline points="{points}" fill="none" stroke="#087c89" stroke-width="3"/>', '''
<text x="45" y="397" font-size="22">r = 1/x + 1/(1−x),   α = 1 / √(1 + (r′)²)</text>
<rect x="25" y="451" width="710" height="205" rx="14" fill="#f5f1fa" stroke="#cabbda"/>
<text x="45" y="486" font-size="24" font-weight="bold">2. Both omitted endpoints become infinitely far</text>
<text x="45" y="526" font-size="23">gα = α⁻² dx²,   α⁻¹ ≥ |r′|</text>
<text x="45" y="565" font-size="22">Endpoint length diverges because r → ∞.</text>
<text x="45" y="603" font-size="22">ηn = ζ(r/n),   ‖[A,ηn]‖ ≤ ‖ζ′‖∞ / n</text>
<text x="45" y="634" font-size="21">Compact cutoffs converge in the full maximal graph norm.</text>
<rect x="25" y="677" width="710" height="265" rx="14" fill="#fff7ea" stroke="#decda9"/>
<text x="45" y="712" font-size="24" font-weight="bold">3. The positive factor cancels from the phase</text>
<text x="45" y="753" font-size="23">A = α½ N α½,   symbol(A) = α c_inv(ξ)</text>
<text x="45" y="793" font-size="23">α c_inv(ξ) / (α |ξ|) = c_inv(ξ) / |ξ|</text>
<text x="45" y="832" font-size="21">Original q, inverse line and final Clifford block are retained.</text>
<text x="45" y="870" font-size="22">Original positive disk Bott class × local inverse = +1</text>
<text x="45" y="910" font-size="21">Domain: u ∈ L², u ∈ H¹_loc, Au ∈ L².</text>
<text x="30" y="974" font-size="20">Maximal normal cycle; no reduced physical graph claim.</text>
</g></svg>''']
    data = dict(schema='weighted-normal-figure/v1', interval=[0,1], endpoints_included=False,
                original_metric='dx^2', exhaustion='1/x+1/(1-x)',
                derivative='-1/x^2+1/(1-x)^2', alpha='(1+derivative^2)^(-1/2)',
                sample_role='Numerical evaluation of exact formula; not a proof', samples=samples,
                retained_degree='original q', reduced_graph_claimed=False,
                proof='Theorem11BM.1, WN.1-11, WB.1-6, Exercises291-293')
    return ''.join(parts), data


if __name__ == '__main__':
    p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path('generated'));a=p.parse_args()
    a.output_dir.mkdir(parents=True,exist_ok=True)
    svg,data=generate()
    (a.output_dir/'weighted-normal-cycle.svg').write_text(svg,encoding='utf-8',newline='\n')
    (a.output_dir/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'samples':len(data['samples']),'symmetry_checked':True,'infinite_domain_claimed_by_samples':False}))
