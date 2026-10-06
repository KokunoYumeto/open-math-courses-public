"""Reproduce the supported-coordinate diagram; uses only Python's standard library."""
from pathlib import Path
from html import escape
import argparse
p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).with_suffix('.svg')));a=p.parse_args()
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="650" viewBox="0 0 960 650" role="img" aria-labelledby="title desc">',
 '<title id="title">Four full basis coordinates and one half-supported coordinate</title>',
 '<desc id="desc">The index nine-halves diagonal example has four coordinates supported by the identity of N and a fifth supported by p zero of N trace one-half. Right coefficients reconstruct x as the sum of u i c i. The geometric corner E eleven has M trace one-third and is a different projection.</desc>',
 '<rect width="960" height="650" rx="20" fill="#f8faf9"/>',
 '<style>text{font-family:DejaVu Sans,Arial,sans-serif;font-style:normal;fill:#172635}.head{font-size:26px;font-weight:700}.label{font-size:22px}.small{font-size:18px}.eq{font-size:24px}.box{fill:white;stroke:#bccbd0;stroke-width:2}</style>']
def text(x,y,s,cls='label',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
text(40,49,'A fractional coordinate is a projection corner','head')
text(40,83,'For the explicit diagonal inclusion N ⊂ M₃(T) with T ≅ M₂(T)','small')
for i in range(5):
 x=40+182*i
 parts.append(f'<rect x="{x}" y="113" width="152" height="152" rx="12" class="box"/>')
 parts.append(f'<rect x="{x+14}" y="173" width="124" height="23" rx="4" fill="#dce9e8"/>')
 parts.append(f'<rect x="{x+14}" y="173" width="{62 if i==4 else 124}" height="23" rx="4" fill="{"#c1753c" if i==4 else "#2c7779"}"/>')
 text(x+76,145,'c'+'₁₂₃₄₅'[i],anchor='middle')
 text(x+76,223,'c₅ ∈ p₀N' if i==4 else 'cᵢ ∈ N',cls='small',anchor='middle')
 text(x+76,249,'τN(p₀) = ½' if i==4 else 'τN(1) = 1',cls='small',anchor='middle')
text(480,287,'Right N-module coordinates','small','middle')
text(480,317,'L²(M) ≅ L²(N)⁴ ⊕ p₀L²(N)','eq','middle')
text(480,345,'Index = 1 + 1 + 1 + 1 + ½ = 9⁄2','eq','middle')
parts.append('<rect x="40" y="374" width="880" height="82" rx="12" class="box"/>')
text(480,406,'x = u₁c₁ + u₂c₂ + u₃c₃ + u₄c₄ + u₅c₅','eq','middle')
text(480,437,'cᵢ = E_N(uᵢ* x); coefficients multiply on the right','small','middle')
parts.append('<rect x="40" y="479" width="430" height="129" rx="12" fill="#e4eeed"/>')
parts.append('<rect x="490" y="479" width="430" height="129" rx="12" fill="#f3e8dd"/>')
text(61,513,'Basis support in N','label')
text(61,549,'p₀ = ι(r),  τN(p₀) = ½','eq')
text(61,583,'Supports the final right coordinate','small')
text(511,513,'Geometric corner in N′ ∩ M','label')
text(511,549,'q = E₁₁,  τM(q) = ⅓','eq')
text(511,583,'Selects the first diagonal block of M','small')
text(40,637,'Bars show projection traces, not spectra or a finite-dimensional model of T.','small')
parts.append('</svg>')
Path(a.output).write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(a.output)
