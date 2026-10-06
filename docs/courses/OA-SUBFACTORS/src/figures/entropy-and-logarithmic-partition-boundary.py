"""Original reproducible finite-coupling and log-boundary diagram."""
from pathlib import Path
from html import escape
W,H=900,1110
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="900" height="1110" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#18364c}.title{font-size:27px;font-weight:bold}.head{font-size:23px;font-weight:bold}.math{font-family:Georgia,serif;font-size:25px}.small{font-size:18px}.edge{stroke:#315e78;stroke-width:2.5;fill:none;marker-end:url(#arrow)}</style>',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="#315e78"/></marker></defs>']
def text(x,y,s,c=''):p.append(f'<text x="{x}" y="{y}" class="{c}">{escape(s)}</text>')
def panel(y,h,s):
    p.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#a9bdcc"/>')
    text(47,y+37,s,'head')
text(34,42,'Weighted stationarity controls a bounded-band boundary','title')
text(34,77,'Exact finite-partition proof; controlled spread remains required.','small')
panel(99,305,'1. An exact two-label coupling  [71.1–71.4; Example 71.1]')
for x,a in [(190,2),(680,1)]:
    p.append(f'<circle cx="{x}" cy="239" r="43" fill="#d9eaf5" stroke="#315e78" stroke-width="2"/>')
    text(x-27,247,'ζ = '+str(a),'math')
p.append('<path d="M228 213 Q435 150 642 213" class="edge"/>')
p.append('<path d="M642 265 Q435 330 228 265" class="edge"/>')
p.append('<path d="M156 214 C95 160 95 316 156 264" class="edge"/>')
p.append('<path d="M714 264 C785 316 785 160 714 214" class="edge"/>')
text(356,173,'each direction: 1/4','small')
text(370,334,'each loop: 1/4','small')
text(50,379,'c = 3/2;  K = 1;  H = 2. Positions and edges are schematic.','small')
panel(424,260,'2. Entropy and absolute log cost  [71.5–71.12]')
text(52,508,'D(2 | 1) = 2 log 2 − 1;   D(1 | 2) = 1 − log 2','math')
text(52,558,'D* = (log 2)/4;    J = 3 log 2 / 4','math')
text(52,610,'a |log(a/b)| ≤ D(a | b) + √(2a D(a | b))','math')
text(52,654,'Both marginals cancel the inside linear term; no symmetry needed.','small')
panel(704,265,'3. Random log cuts and the general estimate  [71.8; 71.13]')
text(52,789,'Width w = 1: separation probability = log 2','math')
text(52,837,'Exact average normalized boundary = (log 2)/2','math')
text(52,889,'General: average ℬ ≤ σ + (A + √(2A))/w','math')
text(52,937,'A = (1 + log(H/K)) σ;   σ = ‖ζ − Tζ‖₁ / c','math')
text(35,1014,'A fixed band plus sufficiently small stationarity supplies the boundary.','small')
text(35,1050,'Unrestricted Følner must still supply simultaneous control of the band.','small')
text(35,1086,'Problem credit: Popa, Theorem 4.2.2, pp. 213–214. Original proof 71.1–71.14.','small')
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')
