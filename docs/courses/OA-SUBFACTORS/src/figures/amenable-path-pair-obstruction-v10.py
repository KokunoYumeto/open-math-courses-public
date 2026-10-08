"""CC0-1.0. Actual same-grade endpoint-pair invariant; exact sizes and traces."""
from pathlib import Path
from html import escape
own=Path(__file__).resolve().parent
W,H=1600,1060
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<rect width="100%" height="100%" fill="#f8faff"/>']
def text(x,y,s,size=29,bold=False,color='#192744'):
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{escape(s)}</text>')
def box(x,y,w,h,color='#ffffff'):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{color}" stroke="#c5d0e3" stroke-width="2"/>')
def line(x1,y1,x2,y2,label,lx,ly):
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#395fb4" stroke-width="4"/>')
    text(lx,ly,label,27,True,'#395fb4')
text(60,30,'An amenable actual tower can fail every inherited pair map',40,True)
text(60,89,'G = S3 × Z;  A = (12), B = (23);  original index 10;  blocked index 100',29)
text(60,133,'At every endpoint: n = m − i + 1 ≥ 2;  grade r = n − 1 is preserved by the physical trace',28)
box(60,205,710,440);box(830,205,710,440)
text(85,225,'Lower pair: append H on the right',31,True)
text(855,225,'Upper pair: prepend H on the left',31,True)
text(85,275,'n = 2, selected small block t = A',27)
text(855,275,'n = 2, every small top block u = A or BA',26)
box(300,335,230,85,'#edf3ff');text(330,355,'G: Mat1(A)',31,True)
box(1070,335,230,85,'#edf3ff');text(1100,355,'V: Mat1(u)',31,True)
line(365,420,250,495,'3',290,443);line(465,420,595,495,'2',530,443)
line(1135,420,1020,495,'3',1060,443);line(1235,420,1365,495,'2',1300,443)
box(110,500,290,95,'#eaf5ee');text(132,520,'F: Mat8(A)',31,True)
box(470,500,250,95,'#fff1e8');text(491,520,'F: Mat2(AB)',30,True)
box(880,500,290,95,'#eaf5ee');text(903,520,'U: Mat8(u)',31,True)
box(1240,500,250,95,'#eaf5ee');text(1261,520,'U: Mat8(Bu)',29,True)
text(85,609,'Distinct neighbour sizes: 8 and 2',27,True)
text(855,609,'Equal neighbour sizes: 8 and 8',27,True)
box(60,685,1480,130,'#edf3ff')
text(85,704,'All depths: L_n = (5n − 2)K^r + 2K^rB;  B L_n = L_n',30,True)
text(85,754,'Right selected size gap = 5n − 4 > 0; every left maximal-grade row has zero gap',29)
box(60,850,750,147)
text(85,866,'Two finite traces on a minimal charge projection',26,True)
text(85,908,'Physical: 2^(−r)/10^n;  normalized dual: 2^r/10^n',26)
text(85,948,'At n = 2, r = 1: 1/200 and 1/50, respectively',26)
box(840,850,700,147)
text(865,866,'Actual cup normalizations and amenability hold',26,True)
text(865,908,'Q and modified g: trace and expectation = 1/100',25)
text(865,948,'Generating core: factor centers; joint defect = 0',26)
text(60,1018,'PG1–PG26: finite-shifted-comparisons-without-coherence.md. Only same-grade edges shown; a trace-preserving image of the selected row has this grade.',21)
svg.append('</svg>')
(own/'amenable-path-pair-obstruction-v10.svg').write_text('\n'.join(svg),encoding='utf-8')
