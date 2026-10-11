"""Draw the exact centered paths used in the lesson. No plotting dependency."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
def main():
    X=lambda k:70+50*k
    Y=lambda u:218-36*u
    out=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 500" role="img" aria-labelledby="t d">',
         '<title id="t">Equal totals do not determine prefix excursions</title>',
         '<desc id="d">The word 3,3,3,1,1,1 has deviations 0,1,2,3,2,1,0 and reaches the excluded boundary 3. The word 3,1,3,1,3,1 has deviations 0,1,0,1,0,1,0 and remains in the strict strip.</desc>',
         '<rect width="440" height="500" fill="#fff"/>',
         '<g font-family="system-ui,sans-serif" fill="#183046">',
         '<text x="220" y="34" text-anchor="middle" font-size="20">Same total, different earlier paths</text>',
         '<rect x="70" y="110" width="300" height="216" fill="#edf5f5"/>']
    for u in range(-3,4):
        dash=' stroke-dasharray="7 5"' if abs(u)==3 else ''
        color='#a03f35' if abs(u)==3 else '#c7d5df'
        out.append(f'<path d="M70 {Y(u)} H370" stroke="{color}"{dash}/>')
        out.append(f'<text x="57" y="{Y(u)+5}" text-anchor="end" font-size="15">{u}</text>')
    for k in range(7):
        out.append(f'<text x="{X(k)}" y="352" text-anchor="middle" font-size="15">{k}</text>')
    for values,color,dashed in [([0,1,2,3,2,1,0],'#a64532',False),([0,1,0,1,0,1,0],'#126d8a',True)]:
        pts=' '.join(f'{X(k)},{Y(u)}' for k,u in enumerate(values))
        dash=' stroke-dasharray="6 4"' if dashed else ''
        out.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3.5"{dash}/>')
        for k,u in enumerate(values):
            out.append(f'<circle cx="{X(k)}" cy="{Y(u)}" r="4" fill="{color}"/>')
    out += ['<circle cx="220" cy="110" r="10" fill="none" stroke="#a64532" stroke-width="2"/>',
            '<text x="220" y="86" text-anchor="middle" font-size="16">Boundary reached at k = 3</text>',
            '<text x="220" y="380" text-anchor="middle" font-size="17">Prefix length k</text>',
            '<text x="24" y="218" transform="rotate(-90 24 218)" text-anchor="middle" font-size="16">Valuation sum minus 2k</text>',
            '<text x="80" y="412" fill="#a64532" font-size="17">3, 3, 3, 1, 1, 1</text>',
            '<text x="80" y="440" fill="#126d8a" font-size="17">3, 1, 3, 1, 3, 1</text>',
            '<text x="220" y="478" text-anchor="middle" font-size="16">Both dashed boundaries are excluded.</text>',
            '</g></svg>']
    p=ROOT/'figures/prefix-passage.svg';p.write_text('\n'.join(out)+'\n',encoding='utf-8')
    print(p)
if __name__=='__main__': main()
