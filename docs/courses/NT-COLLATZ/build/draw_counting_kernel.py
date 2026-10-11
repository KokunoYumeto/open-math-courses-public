"""Draw exact finite kernel terms and two residue-population examples.
Fraction arithmetic determines every kernel value; floats place SVG coordinates.
"""
from pathlib import Path
from fractions import Fraction as F
from math import log2
from check_counting_kernel import kernel_term

ROOT=Path(__file__).resolve().parents[1]
out=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="665" viewBox="0 0 440 665" role="img" aria-labelledby="title desc">',
     '<title id="title">A binomial counting kernel and unequal residue weights</title>',
     '<desc id="desc">Exact normalized kernel terms for lengths10 through110, and two populations of90 points whose weighted errors are2 and9.</desc>',
     '<rect width="440" height="665" fill="white"/>',
     '<g font-family="Arial,sans-serif" fill="#16364b">']

def text(x,y,t,size=14,anchor='middle'):
    out.append(f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-size="{size}">{t}</text>')

def line(x1,y1,x2,y2,color='#6d8793',dash=''):
    out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{color}" {dash}/>')

text(220,24,'A sharp cutoff leaves a concentrated kernel',15)
text(220,48,'Y = 2¹², U = 2²⁴, M = 1')
text(220,70,'Exact summands divided by 2²⁴',13)
terms=[(r,kernel_term(r,F(1),F(2**12),F(2**24))/2**24) for r in range(10,111)]
peak=max(v for _,v in terms)
x=lambda r:48+(r-10)*3.4
y=lambda v:235-135*float(v/peak)
for r,v in terms:
    out.append(f'<rect x="{x(r):.2f}" y="{y(v):.2f}" width="2.6" height="{235-y(v):.2f}" fill="#167e81"/>')
line(45,235,393,235)
for r in (10,30,50,70,90,110):
    line(x(r),235,x(r),240)
    text(x(r),258,str(r),12)
text(410,240,'r',13)
centre=24/(2-log2(3))
line(x(centre),92,x(centre),235,'#bb5e16','stroke-dasharray="4 3"')
text(x(centre)+6,90,'centre ≈ 57.83',12,'start')
text(220,286,'Integer cutoffs are not replaced by real ones',13)
line(24,307,416,307,'#d4e0e7')
text(220,334,'The same error can receive different weights',15)
text(220,358,'h = (1/10, −1/10, 0, …),   ‖h‖₁ = 1/5')
for baseline,pop,title,result in [(462,[10]*9,'Ten points in each residue','Weighted sum = 2'),
                                  (603,[90]+[0]*8,'Ninety points in residue zero','Weighted sum = 9')]:
    text(220,baseline-72,title,14)
    for z,n in enumerate(pop):
        xx=54+z*40
        height=46*n/90
        out.append(f'<rect x="{xx-12}" y="{baseline-height:.2f}" width="24" height="{height:.2f}" fill="#167e81"/>')
        if n:
            text(xx,baseline-height-5,str(n),12)
        text(xx,baseline+18,str(z),12)
    line(36,baseline,392,baseline)
    text(411,baseline+18,'z',12)
    text(220,baseline+43,result,14)
out.append('</g></svg>')
(ROOT/'figures/counting-kernel.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('figures/counting-kernel.svg')


