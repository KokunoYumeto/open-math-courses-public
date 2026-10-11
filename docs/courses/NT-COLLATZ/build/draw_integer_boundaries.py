"""Draw exact affine and endpoint intervals; floats only position SVG marks."""
from fractions import Fraction as F
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    bits=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="625" viewBox="0 0 440 625" role="img" aria-labelledby="title desc">',
          '<title id="title">Exact affine shifts and separated boundary intervals</title>',
          '<desc id="desc">The true start11 lies in10 through11, while104/9 does not. Four exact dyadic-triadic boundary intervals for M400 and R2 appear on a common endpoint axis.</desc>',
          '<rect width="440" height="625" fill="white"/>',
          '<style>text{font-family:Arial,sans-serif;fill:#14354b;font-size:14px}.small{font-size:12px}.line{stroke:#536d7d;stroke-width:1}</style>']
    def text(x,y,t,anchor='middle',small=False):
        bits.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}"'+(' class="small"' if small else '')+'>'+escape(str(t))+'</text>')
    def line(x1,y1,x2,y2,colour='#536d7d',width=1):
        bits.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" stroke-width="{width}"/>')
    text(220,27,'Dropping an offset can move a boundary point')
    text(220,51,'Word (1,2); endpoint M = 13')
    def tx(v): return 55+float(F(v)-10)*160
    bits.append(f'<rect x="{tx(10)}" y="91" width="{tx(11)-tx(10)}" height="32" fill="#daf0e8"/>')
    line(tx(10),118,tx(12),118)
    for v in (10,11,12):
        line(tx(v),113,tx(v),126)
        text(tx(v),146,str(v))
    for v,c in [(F(11),'#087c70'),(F(104,9),'#b85411')]:
        bits.append(f'<circle cx="{tx(v)}" cy="118" r="4" fill="{c}"/>')
        line(tx(v),82,tx(v),110,c)
    text(tx(11)-6,78,'N = 11','end')
    text(tx(F(104,9)),78,'N⁰ = 104/9')
    text(220,177,'Closed window [10,11]; shift = 5/9')
    text(220,204,'11 → 17 → 13 is the actual odd-return path')
    line(25,231,415,231,'#c8d7df')
    text(220,260,'Separated intervals in the endpoint coordinate v')
    text(220,284,'R = 2, M = 400 > 4 · 3⁴ = 324')
    def vx(v): return 55+float(F(v)-250)*F(355,500)
    pairs=[(1,1),(2,3),(1,2),(2,4)]
    for j,(r,s) in enumerate(pairs):
        lo=F((400-3**r)*2**s,3**r)
        hi=F(400*2**s,3**r)
        yy=342+j*65
        line(55,yy,410,yy,'#d9e2e8')
        line(vx(lo),yy,vx(hi),yy,'#087c70',6)
        for xx in (vx(lo),vx(hi)):
            line(xx,yy-7,xx,yy+7,'#087c70',1)
        text(55,yy-19,f'(r,s) = ({r},{s})     [{lo}, {hi}]','start',True)
    yy=562
    line(55,yy,410,yy)
    for v in (250,500,750):
        line(vx(v),yy-4,vx(v),yy+5)
        text(vx(v),yy+22,v,small=True)
    text(220,614,'Common linear scale; exact rational endpoints shown',small=True)
    bits.append('</svg>')
    (ROOT/'figures/integer-boundaries.svg').write_text('\n'.join(bits)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()

