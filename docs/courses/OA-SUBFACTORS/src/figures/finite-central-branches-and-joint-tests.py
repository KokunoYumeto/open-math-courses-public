"""Reproducible exact branch diagram; node positions are schematic."""
from pathlib import Path
from html import escape
out=Path(__file__).with_suffix('.svg')
a=['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1210" viewBox="0 0 900 1210">',
'<rect width="900" height="1210" fill="#f5f8fc"/>',
'<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#316b99"/></marker></defs>',
'<style>text{font-family:Arial,sans-serif;fill:#173b54}.title{font-size:27px;font-weight:700}.head{font-size:22px;font-weight:700}.body{font-size:19px}.math{font-family:Georgia,serif;font-size:23px}.small{font-size:17px}</style>']
def text(x,y,t,cls='body',anchor='start'):
    a.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(t)}</text>')
def box(y,h):
    a.append(f'<rect x="24" y="{y}" width="852" height="{h}" rx="14" fill="white" stroke="#a9c1d3"/>')
text(32,43,'A fixed finite branch system for the joint center','title')
text(32,77,'Exact weighted model; the final averaging hypothesis remains open.')
box(100,400)
text(44,137,'1. Five atoms over two base points [72.3, 72.16]','head')
text(70,181,'Base mass: 1/2','small')
cols=[400,570,740];colors=['#316b99','#267b63','#9b6429'];fills=['#e0eff9','#e0f3eb','#fcf0df']
for j,(x,col) in enumerate(zip(cols,colors),1):text(x,181,'branch q'+str(j),'body','middle')
for row,y in enumerate([245,390]):
    text(70,y,'base '+str(row),'body')
    text(70,y+30,'conditional weights →','small')
    values=['2/3','1/3',None] if row==0 else ['1/3']*3
    for j,(x,col,fill,w) in enumerate(zip(cols,colors,fills,values)):
        if w is None:
            a.append(f'<circle cx="{x}" cy="{y}" r="34" fill="none" stroke="#8b9cab" stroke-dasharray="5 5"/>')
            text(x,y+6,'absent','small','middle')
            text(x,y+57,'support = 0','small','middle')
        else:
            a.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{fill}" stroke="{col}" stroke-width="2"/>')
            text(x,y+7,w,'math','middle')
            mass='1/3' if row==0 and j==0 else '1/6'
            text(x,y+57,'atom mass '+mass,'small','middle')
text(44,482,'s₁ = s₂ = (1,1), s₃ = (0,1);  x ≤ 3 E(x).  Positions are schematic.','small')
box(530,280)
text(44,568,'2. The full norm is the sum of central norms [72.5, 72.17]','head')
text(54,615,'Branch errors: (2/3, −1/3), (−1/3, 1/3), (0, −1)','math')
text(54,665,'Each central coordinate has base mass 1/2.','body')
text(54,715,'‖γ − 3ζ‖₁ = 1/2 + 1/3 + 1/2 = 4/3','math')
text(54,766,'The norm uses inherited atom masses, never counting measure.','small')
box(835,275)
text(44,873,'3. A sufficient hypothesis for actual core operators [72.12–72.14]','head')
text(54,920,'Fixed Hⱼ = E_A(xⱼ g xⱼ);  corner mean aⱼ','math')
text(54,969,'N-unitary norm average → âⱼ','math')
text(515,969,'UNPROVED for the actual Hⱼ','small')
a.append('<path d="M65 935 V952" fill="none" stroke="#947b58" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#arrow)"/>')
a.append('<path d="M65 986 V1004" fill="none" stroke="#316b99" stroke-width="2" marker-end="url(#arrow)"/>')
text(54,1044,'Then finite prior tests control the entire joint L¹ error.','body')
text(54,1087,'Proved implication; finite branch count does not prove the hypothesis.','small')
text(32,1147,'Problem credit: Popa, Theorem 4.2.2, pp. 213–214. Original proofs 72.1–72.5.','small')
text(32,1178,'Finite model above is not asserted to be an actual Jones core.','small')
a.append('</svg>')
out.write_text('\n'.join(a)+'\n',encoding='utf-8')
