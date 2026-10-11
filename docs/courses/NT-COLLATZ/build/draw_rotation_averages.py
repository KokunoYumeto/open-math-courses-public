"""Original reproducible rational-grid pairing diagram; positions are numerical."""
from pathlib import Path
from math import sqrt
ROOT=Path(__file__).resolve().parents[1]
def main():
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 352" role="img" aria-labelledby="title desc">',
    '<title id="title">A rotation block paired with a rational grid</title>',
    '<desc id="desc">Five points for square root of two and the seven-fifths grid, both starting at one tenth. The interval from 0.32 to 0.52 contains one grid point and two actual points. Index three crosses the lower boundary.</desc>',
    '<rect width="880" height="352" fill="#fff"/>',
    '<g font-family="Arial,sans-serif" fill="#142d3a">',
    '<text x="36" y="34" font-size="22">One boundary crossing in a complete five-point block</text>',
    '<text x="36" y="61" font-size="15">α = √2, p/q = 7/5, u = 1/10; pairs retain their orbit index i</text>']
    X=lambda t:65+750*t
    parts+= [f'<rect x="{X(.32)}" y="93" width="{750*.2}" height="163" fill="#e4effb"/>']
    for t in [.32,.52]:
        parts.append(f'<line x1="{X(t)}" x2="{X(t)}" y1="90" y2="261" stroke="#265d99" stroke-dasharray="5 4"/>')
        parts.append(f'<text x="{X(t)}" y="281" text-anchor="middle" font-size="15">{t:.2f}</text>')
    for y in [124,225]:
        parts.append(f'<line x1="65" x2="815" y1="{y}" y2="{y}" stroke="#88969e"/>')
    for i in range(5):
        grid=(.1+7*i/5)%1
        actual=(.1+i*sqrt(2))%1
        color="#b04b1e" if i==3 else "#486877"
        parts.append(f'<line x1="{X(grid):.3f}" y1="124" x2="{X(actual):.3f}" y2="225" stroke="{color}" stroke-width="2"/>')
        for t,y in [(grid,124),(actual,225)]:
            parts.append(f'<circle cx="{X(t):.3f}" cy="{y}" r="5" fill="{color}"/>')
            parts.append(f'<text x="{X(t):.3f}" y="{y-14}" text-anchor="middle" font-size="15">i={i}</text>')
    parts+=['<text x="36" y="91" font-size="16">Rational grid</text>',
            '<text x="36" y="198" font-size="16">Actual rotation</text>',
            '<text x="36" y="319" font-size="16">[0.32, 0.52): one grid point, two actual points. Only i=3 changes membership.</text>',
            '</g></svg>']
    (ROOT/'figures/rotation-grid.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
if __name__=='__main__': main()

