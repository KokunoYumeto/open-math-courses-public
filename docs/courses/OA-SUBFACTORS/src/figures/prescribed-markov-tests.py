"""Exact expectation bars for Exercise 8.7; heights scale values by 180."""
from pathlib import Path
from fractions import Fraction as F
from html import escape

out = Path(__file__).with_suffix('.svg')
v = [F(1,6), F(1,2), F(1,3)]
assert (v[0]+v[1])/2 == v[2] == F(1,3)
s = ['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="650" viewBox="0 0 960 650">',
     '<rect width="960" height="650" fill="#f7f4ee"/>',
     '<style>text{font-family:Arial,sans-serif;fill:#192d38} .title{font-size:27px;font-weight:bold}.label{font-size:22px}.small{font-size:18px}</style>']
def text(x,y,t,cls='label'):
    s.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(t)}</text>')
def rect(x,y,w,h,color):
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
text(36,48,'A prescribed test can average unequal entries','title')
text(36,85,'A = diagonal algebra of B = M₃;  B₁ = M₃ ⊕ M₃ ⊕ M₃','label')
text(36,121,'Basic-trace weights: u = (1/18, 1/6, 1/9); Jones projection: (E₁₁, E₂₂, E₃₃)','small')
for row, values in enumerate([v,[F(1,3)]*3]):
    baseline = 290 + 235*row
    text(36,baseline-(123 if row==0 else 99),'E_B(e_A)' if row==0 else 'E_P(e_A)','label')
    for i,z in enumerate(values):
        x=260+210*i; h=180*z
        rect(x,baseline-float(h),180,float(h),'#277f8e' if row==0 else '#b37439')
        s.append(f'<path d="M{x} {baseline}h180" stroke="#192d38" stroke-width="2"/>')
        text(x+67,baseline-float(h)-14,str(z))
        text(x+58,baseline+31,['E₁₁','E₂₂','E₃₃'][i])
    if row==1:
        s.append('<path d="M260 571v9h390v-9 M680 571v9h180v-9" fill="none" stroke="#192d38" stroke-width="2"/>')
        text(346,609,'P cell: E₁₁ + E₂₂','small'); text(717,609,'P cell: E₃₃','small')
text(36,351,'First two entries average: (1/6 + 1/2)/2 = 1/3. Third entry stays 1/3.','label')
text(36,387,'Equal widths encode trace 1/3; heights encode expectation values.','small')
text(36,644,'Definition 8.10 · Lemma 8.7 · full solution in Exercise 8.7 · original reproducible figure','small')
s.append('</svg>')
out.write_text('\n'.join(s)+'\n',encoding='utf-8')
print(out)
