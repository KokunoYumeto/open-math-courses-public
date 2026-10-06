"""Original reproducible atomic-path and exact localization-gap figure."""
from pathlib import Path
from html import escape
from fractions import Fraction as F
W,H=900,1160
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="900" height="1160" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#18364c}.title{font-size:27px;font-weight:bold}.head{font-size:23px;font-weight:bold}.math{font-family:Georgia,serif;font-size:25px}.small{font-size:18px}.edge{stroke:#315e78;stroke-width:2.5;fill:none}</style>']
def text(x,y,s,c=''):
    p.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')
def panel(y,h,title):
    p.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#a9bdcc"/>')
    text(47,y+37,title,'head')
def frac(x):return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
text(34,42,'Small stationarity defect can hide a joint gap','title')
text(34,77,'A fixed commutative model; no Jones-core realization asserted.','small')
panel(99,321,'1. Two labels per fiber; exact atom weights  [69.1–69.4]')
for j in range(4):
    x=70+240*j
    p.append(f'<circle cx="{x}" cy="187" r="25" fill="#d9eaf5" stroke="#315e78"/>')
    text(x-13,195,'s'+str(j),'math')
for j in range(3):
    x=190+240*j
    p.append(f'<circle cx="{x}" cy="311" r="25" fill="#f4e7c9" stroke="#95722c"/>')
    text(x-13,319,'r'+str(j),'math')
    for sx,weight,offset in [(70+240*j,F(1,3*2**j),-20),(310+240*j,F(1,3*2**(j+1)),6)]:
        p.append(f'<path class="edge" d="M{sx},212 L{x},286"/>')
        text((sx+x)/2+offset,246,frac(weight),'small')
p.append('<path class="edge" stroke-dasharray="7,5" d="M815,202 L853,273"/>')
text(837,299,'…','math')
text(47,370,'P₀ on r_j: probabilities 2/3, 1/3;  Q₀ on s_k (k ≥ 1): 1/2, 1/2.','small')
text(47,401,'κ = 1;    t ≤ 3 P₀(t),    t ≤ 2 Q₀(t);    overlap ≤ 2.','math')
panel(442,267,'2. Interior cancellation leaves only three defects  [69.7–69.9]')
text(47,518,'f_L(s_k) = 2ᵏ for 0 ≤ k < L, and 0 afterward; c_L = (2L − 1)/3.','small')
for x,label,cost in [(63,'s₀','1/9'),(336,'s_L−1','2/9'),(609,'s_L','1/9')]:
    p.append(f'<rect x="{x}" y="546" width="229" height="90" rx="9" fill="#e8f1f7" stroke="#789bae"/>')
    text(x+20,579,label,'math')
    text(x+20,613,'weighted defect: '+cost,'small')
text(47,681,'All interior differences vanish; total ‖f_L − T f_L‖₁ = 4/9.','math')
panel(731,307,'3. The best larger-center density stays separated  [69.10–69.13]')
cols=[48,128,359,608]
for x,s in zip(cols,['L','Stationarity / mass','Best joint / mass','To P₀ f_L / mass']):text(x,813,s,'small')
for i,L in enumerate([2,4,8,16]):
    y=851+37*i
    vals=[str(L),frac(F(4,3*(2*L-1))),frac(F(L,2*(2*L-1))),frac(F(2*L,3*(2*L-1)))]
    for x,s in zip(cols,vals):text(x,y,s,'math')
for x,s in zip(cols,['Limit','0','1/4','1/3']):text(x,1017,s,'math')
text(34,1080,'Each of L active larger fibers has optimal unnormalized cost 1/6.','small')
text(34,1114,'Proved: no modulus from stationarity alone, even for this one fixed model.','small')
text(34,1146,'Actual general core localization still requires projection information.','small')
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')
