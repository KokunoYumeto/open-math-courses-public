"""Reproducible SVG of two exact characteristic-function moduli.
Curves are sampled drawings; labelled endpoint/centre values are exact.
"""
from pathlib import Path
from math import cos,pi

ROOT=Path(__file__).resolve().parents[1]


def panel(x0,title,subtitle,kind):
    left=x0+50
    top=100
    width=300
    height=180
    pts=[]
    for j in range(241):
        t=-pi+2*pi*j/240
        val=abs(cos(t/2)) if kind==1 else abs(cos(t))
        pts.append(f'{left+width*j/240:.3f},{top+height*(1-val):.3f}')
    out=[f'<text x="{x0+200}" y="35" text-anchor="middle" class="title">{title}</text>',
         f'<text x="{x0+200}" y="64" text-anchor="middle" class="sub">{subtitle}</text>',
         f'<path d="M {left} {top} V {top+height} H {left+width}" class="axis"/>',
         f'<path d="M {left} {top} H {left+width}" class="grid"/>',
         f'<polyline points="{" ".join(pts)}" class="curve"/>']
    for j,label in [(0,'−π'),(1,'0'),(2,'π')]:
        x=left+width*j/2
        val=1 if (kind==2 or j==1) else 0
        y=top+height*(1-val)
        out.extend([f'<circle cx="{x}" cy="{y}" r="4" class="dot"/>',
                    f'<text x="{x}" y="{top+height+28}" text-anchor="middle">{label}</text>'])
    out.extend([f'<text x="{left-18}" y="{top+6}" text-anchor="middle">1</text>',
                f'<text x="{left-18}" y="{top+height+5}" text-anchor="middle">0</text>'])
    return '\n'.join(out)


def main():
    svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 390" role="img" aria-labelledby="title desc">
<title id="title">Support restrictions leave extra Fourier peaks</title>
<desc id="desc">The modulus for a fair increment on zero and one is absolute cosine t over two; only the centre reaches one. For minus one and one it is absolute cosine t; both endpoints also reach one, recording the parity restriction.</desc>
<style>text{font:19px Georgia,serif;fill:#172c38}.title{font-size:23px;font-weight:600}.sub{font-size:18px}.axis{fill:none;stroke:#425565;stroke-width:1.5}.grid{fill:none;stroke:#ccd7de;stroke-dasharray:5 5}.curve{fill:none;stroke:#125567;stroke-width:3}.dot{fill:#ac5c19}</style>
<rect width="800" height="390" fill="white"/>
'''+panel(0,'Support {0, 1}','|φ(t)| = |cos(t/2)|',1)+panel(400,'Support {−1, 1}','|φ(t)| = |cos t|',2)+'''
<text x="200" y="350" text-anchor="middle">Difference group: ℤ</text>
<text x="600" y="350" text-anchor="middle">Difference group: 2ℤ</text>
<text x="400" y="382" text-anchor="middle" class="sub">Local probabilities for lattice sums · Lemma 2</text>
</svg>
'''
    target=ROOT/'figures/lattice-frequencies.svg'
    target.write_text(svg,encoding='utf-8',newline='\n')


if __name__=='__main__':
    main()
