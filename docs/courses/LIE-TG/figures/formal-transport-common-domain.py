"""Sample the analytic jet-transport formulas of Example 4.29 into editable SVG."""
from pathlib import Path
from math import exp

def points(fun,ymin,ymax,top,height):
    result=[]
    for i in range(481):
        w=-1.2+2.4*i/480
        px=630+500*(w+1.2)/2.4
        py=top+height*(ymax-fun(w))/(ymax-ymin)
        result.append(f'{px:.5f},{py:.5f}')
    return ' '.join(result)

slope=points(lambda w:exp(-w*w),0,1.1,170,235)
second=points(lambda w:-2*w*exp(-2*w*w),-.7,.7,512,230)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="850" viewBox="0 0 1200 850" role="img" aria-labelledby="title desc">
<title id="title">Formal transport and one finite coefficient domain</title>
<desc id="desc">For H prime exp(u squared), source u=0 and slope p0=1 are transported to u=w, slope exp(-w squared), and second derivative f(w)=-2w exp(-2w squared). The plots sample w from -1.2 to 1.2 in 481 points. The formal series f has zero constant term and nonzero linear coefficient -2. The coefficient map therefore extends to a fraction field when p0 is nonzero.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>
<rect width="1200" height="850" fill="#f7f9fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
<text x="30" y="40" font-size="25" font-weight="650">Formal transport and a finite source-slope domain</text>
<text x="30" y="69" font-size="17">H′(u)=exp(u²),   H(U)=H(u)+H(w),   source a=(0,0).</text>
<rect x="25" y="92" width="530" height="720" rx="13" fill="white" stroke="#c5d0df"/>
<rect x="575" y="92" width="600" height="720" rx="13" fill="white" stroke="#c5d0df"/>
<text x="47" y="130" font-size="21" font-weight="600">Coefficient selection and transport back</text>
<rect x="48" y="155" width="480" height="100" rx="8" fill="#edf4f8"/>
<text x="67" y="189" font-size="19">u=0, slope p₀</text>
<text x="67" y="226" font-size="18">Fixed-fibre coordinate algebra Rₗ</text>
<path d="M288 265L288 304" stroke="#14757e" stroke-width="2.5" marker-end="url(#arrow)"/>
<text x="310" y="288" font-size="17">g<tspan baseline-shift="sub" font-size="12">w</tspan></text>
<rect x="48" y="319" width="480" height="118" rx="8" fill="#edf4f8"/>
<text x="67" y="351" font-size="19">u=w,   p=exp(−w²)p₀</text>
<text x="67" y="385" font-size="18">f(w,p₀)=−2w exp(−2w²)p₀²</text>
<text x="67" y="417" font-size="18">[w]f=−2p₀²  ≠ 0 on p₀ ≠ 0</text>
<path d="M288 447L288 487" stroke="#14757e" stroke-width="2.5" marker-end="url(#arrow)"/>
<text x="310" y="471" font-size="16">ordinary coefficient map</text>
<rect x="48" y="502" width="480" height="100" rx="8" fill="#eaf4ef"/>
<text x="67" y="537" font-size="19">A[f⁻¹]  →  Frac(L[[w]])</text>
<text x="67" y="574" font-size="17">Nonzero series are invertible in the field.</text>
<path d="M288 612L288 652" stroke="#14757e" stroke-width="2.5" marker-end="url(#arrow)"/>
<text x="310" y="636" font-size="17">g<tspan baseline-shift="sub" font-size="12">w</tspan>⁻¹ and field faithfulness</text>
<rect x="48" y="667" width="480" height="110" rx="8" fill="#edf4f8"/>
<text x="67" y="704" font-size="19">Ranks and symbol identities at the original jet</text>
<text x="67" y="741" font-size="17">One finite source-slope restriction: p₀ ≠ 0.</text>
<text x="600" y="128" font-size="21" font-weight="600">Analytic values when p₀=1</text>
<text x="630" y="157" font-size="18" fill="#14757e">p(w)=exp(−w²)</text>
<g stroke="#d7dfe8" stroke-width="1">
<path d="M630 405H1130 M630 298.18182H1130 M630 191.36364H1130"/>
<path d="M630 512H1130 M630 627H1130 M630 742H1130"/>
</g>
<g stroke="#8797ab" stroke-width="1.6" fill="none">
<path d="M630 170V405H1130"/>
<path d="M630 512V742H1130"/>
<path d="M630 627H1130"/>
</g>
<g stroke="#8797ab" stroke-dasharray="5 5"><path d="M880 170V405 M880 512V742"/></g>
<polyline points="{slope}" stroke="#14757e" stroke-width="3.5" fill="none"/>
<polyline points="{second}" stroke="#315dba" stroke-width="3.5" fill="none"/>
<circle cx="880" cy="627" r="5" fill="#c25430"/>
<g font-size="15" text-anchor="end"><text x="621" y="410">0</text><text x="621" y="303">0.5</text><text x="621" y="196">1</text><text x="621" y="518">0.7</text><text x="621" y="632">0</text><text x="621" y="747">−0.7</text></g>
<g font-size="15" text-anchor="middle"><text x="630" y="430">−1.2</text><text x="880" y="430">0</text><text x="1130" y="430">1.2</text><text x="630" y="768">−1.2</text><text x="880" y="768">0</text><text x="1130" y="768">1.2</text></g>
<text x="1143" y="430" font-size="16">w</text><text x="1143" y="768" font-size="16">w</text>
<text x="630" y="487" font-size="18" fill="#315dba">f(w,1)=−2w exp(−2w²)</text>
<text x="908" y="590" font-size="16" fill="#a34224">f(0,1)=0</text>
<text x="908" y="614" font-size="16" fill="#a34224">[w]f=−2</text>
<text x="630" y="796" font-size="14" fill="#52647a">481 samples of each displayed analytic formula.</text>
</g></svg>'''

if __name__=='__main__':
    Path(__file__).with_suffix('.svg').write_text(svg,encoding='utf-8',newline='\n')
