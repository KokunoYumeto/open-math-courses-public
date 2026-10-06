"""Exact central arithmetic and proved flag implications; schematic coordinates."""
from pathlib import Path
from fractions import Fraction
from html import escape
a=['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="1310" viewBox="0 0 900 1310">',
 '<rect width="900" height="1310" fill="#f5f8fc"/>',
 '<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#316b99"/></marker></defs>',
 '<style>text{font-family:Arial,sans-serif;fill:#173b54}.title{font-size:27px;font-weight:700}.head{font-size:22px;font-weight:700}.body{font-size:20px}.math{font-family:Georgia,serif;font-size:24px}.small{font-size:18px}</style>']
def text(x,y,t,cls='body',anchor='start'):
 a.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(t)}</text>')
def box(y,h):a.append(f'<rect x="24" y="{y}" width="852" height="{h}" rx="14" fill="white" stroke="#a9c1d3"/>')
text(32,43,'Round the whole projection, retain a central flag','title')
text(32,78,'Exact three-atom arithmetic; no common support is inferred.')
box(100,540);text(44,137,'1. Square amplification by 4, then take the floor [73.26]','head')
text(50,183,'Vertical unit = one dimension; fractional caps are removed.','small')
xs=[180,430,680];dims=[Fraction(5),Fraction(28,3),Fraction(52,5)]
cols=['#316b99','#267b63','#9b6429'];fills=['#e0eff9','#e0f3eb','#fcf0df'];base=546;scale=28
for x,d,col,fill,w,floorv in zip(xs,dims,cols,fills,['1/2','1/3','1/6'],[5,9,10]):
 top=base-float(d)*scale;floor_top=base-floorv*scale
 a.append(f'<rect x="{x-55}" y="{floor_top}" width="110" height="{floorv*scale}" fill="{fill}" stroke="{col}" stroke-width="2"/>')
 for i in range(1,floorv):a.append(f'<path d="M{x-55} {base-i*scale} H{x+55}" stroke="{col}" stroke-width="0.7"/>')
 if d!=floorv:a.append(f'<rect x="{x-55}" y="{top}" width="110" height="{float(d-floorv)*scale}" fill="#f9d6d6" stroke="#a05050" stroke-dasharray="3 3"/>')
 text(x,219,'f = '+str(d),'math','middle')
 text(x,579,'floor = '+str(floorv),'math','middle')
 text(x,611,'base mass '+w,'small','middle')
text(760,312,'2/5 cap','small')
text(510,281,'1/3 cap','small')
box(661,224);text(44,699,'2. Exact loss and nested supports [73.12, 73.26]','head')
text(52,741,'z₁,…,z₅ = (1,1,1);  z₆,…,z₉ = (0,1,1)','math')
text(52,779,'z₁₀ = (0,0,1);   ∑ ν(zᵢ) = 43/6','math')
text(52,822,'Original mass = 661/90; loss = 8/45; relative loss = 16/661','body')
text(52,862,'The retained dimensions 5, 9, 10 have one support and three values.','small')
box(905,292);text(44,943,'3. Proved whole-projection and flag consequences','head')
text(62,986,'Global floor + prescription → small perturbation [73.1–73.2]')
a.append('<path d="M72 1000 V1020" stroke="#316b99" stroke-width="2" marker-end="url(#arrow)"/>')
text(62,1053,'Nested columns → bounded finite-stage flag [73.3–73.5]')
a.append('<path d="M72 1067 V1087" stroke="#947b58" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#arrow)"/>')
text(62,1120,'One common support / general local approximation','body')
text(62,1161,'Further implication remains open; dashed arrow is not a theorem.','small')
text(32,1241,'Problem credit: Popa, Theorem 4.2.2, pp. 213–214. Original proofs 73.1–73.5.','small')
text(32,1280,'This diagram shows central arithmetic, not an actual Jones-core example.','small')
a.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(a)+'\n',encoding='utf-8')
