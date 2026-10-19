"""Plot the exact stable weight; numerical sampling illustrates the proved bounds."""
from pathlib import Path
import math
import mpmath as mp
mp.mp.dps=45
lam=4096
rows=[]
for j in range(361):
 b=-30+j/6
 f=1/(mp.pi*(mp.airyai(b)**2+mp.airybi(b)**2))
 E=mp.mpf(lam)**(mp.mpf(5)/3)*f
 L=mp.mpf(lam)**(mp.mpf(4)/3)*(1+mp.mpf(b)**2)**(-mp.mpf(1)/4)
 rows.append((b,float(mp.log10(E)),float(mp.log10(L)),float(mp.log10(E+L))))
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="600" viewBox="0 0 1080 600">',
 '<rect width="1080" height="600" fill="#f3f7fa"/>',
 '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#18364d} .small{font-size:14px} .body{font-size:17px}</style>',
 '<text x="28" y="34" font-size="23" font-weight="bold">Stable coefficients permit spatial localization</text>',
 '<text x="54" y="76" class="body">Exact Airy weight, λ = 4096</text>',
 '<text x="590" y="76" class="body">One decaying mode + one normalized mode</text>']
x=lambda b:70+(b+30)*7
y=lambda a:425-(a-3.5)*95
for a in [4,5,6,7]:
 parts.append(f'<path d="M70 {y(a):.2f} H490" stroke="#d5dfe7"/><text x="35" y="{y(a)+5:.2f}" class="small">10^{a}</text>')
for b in [-30,-15,0,15,30]:
 parts.append(f'<path d="M{x(b):.2f} 425 v6" stroke="#879caa"/><text x="{x(b)-10:.2f}" y="450" class="small">{b}</text>')
parts+=['<path d="M70 100 V425 H505" fill="none" stroke="#879caa"/>',
 '<text x="502" y="450" class="body">b</text>',
 '<defs><clipPath id="plot"><rect x="70" y="100" width="420" height="325"/></clipPath></defs>']
for idx,col,width,dash in [(1,'#ca7021',2,'5 4'),(2,'#7650a2',2,'4 3'),(3,'#06718e',3,'')]:
 pts=' '.join(f'{x(r[0]):.2f},{y(r[idx]):.2f}' for r in rows)
 parts.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{width}" stroke-dasharray="{dash}" clip-path="url(#plot)"/>')
for yy,col,dash,label in [(120,'#06718e','','w = E + L'),(148,'#ca7021','5 4','E = λ^(5/3) / |F(b)|²'),(176,'#7650a2','4 3','L = λ^(4/3) / ⟨b⟩^(1/2)')]:
 parts.append(f'<path d="M290 {yy} h32" stroke="{col}" stroke-width="3" stroke-dasharray="{dash}"/><text x="332" y="{yy+5}" class="small">{label}</text>')
parts+=['<text x="73" y="488" class="small">Negative b: oscillatory coefficient cost</text>',
 '<text x="73" y="511" class="small">Positive b: exponential term fades; L remains</text>',
 '<text x="590" y="132" class="body">Fε = cε (Ai − iε Bi),   ε = ±1</text>',
 '<text x="590" y="184" class="body">a = α̂ + (cε / Fε(b)) v̂</text>',
 '<text x="590" y="220" class="body">β = −iε (cε / Fε(b)) v̂</text>',
 '<path d="M800 246 v42 m-7 -9 l7 9 7 -9" fill="none" stroke="#06718e" stroke-width="2"/>',
 '<text x="590" y="326" class="body">α in H^(5/6),   v in H_w</text>',
 '<text x="590" y="370" class="body">Smooth spatial cutoffs are bounded.</text>',
 '<text x="590" y="407" class="body">Ordinary order-zero operators are bounded.</text>',
 '<text x="590" y="451" class="small">Raw growing coefficients are recovered after localization.</text>',
 '<text x="590" y="480" class="small">No arbitrary canonical invariance of w is asserted.</text>',
 '<text x="28" y="553" class="small">SL3: exact plotted weight. SL17–SL20: weighted coefficient isomorphism. SL11–SL15: localization proof.</text>',
 '<text x="28" y="577" class="small">The plot is a finite numerical illustration; it does not prove the all-frequency bounds or a general solution representation.</text>',
 '</svg>']
Path(__file__).with_name('stable-airy-localization.svg').write_text('\n'.join(parts),'utf-8')
print('Wrote exact-weight illustration at 361 sample arguments.')
