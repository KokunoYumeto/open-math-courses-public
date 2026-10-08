"""Draw the exact normal support relation and the proved source/error indices."""
from pathlib import Path
from html import escape

OUT=Path(__file__).with_name('halfspace-support.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="610" viewBox="0 0 1120 610" role="img" aria-labelledby="title desc">',
 '<title id="title">Model support and complete source gains</title>',
 '<desc id="desc">The model kernel is supported where output normal r is at most input normal s. A source at s zero has no positive output. A source part with q coefficient derivatives gains q tangential orders; either finite inverse error layer adds N.</desc>',
 '<rect width="1120" height="610" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#142b45}.title{font-size:23px;font-weight:700}.label{font-size:18px}.small{font-size:16px}.box{fill:#f2f6fc;stroke:#315b88;stroke-width:1.6}</style>']
def text(x,y,s,cls='label',anchor='start',fill=None):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}"'+(f' style="fill:{fill}"' if fill else '')+'>'+escape(s)+'</text>')
def line(x1,y1,x2,y2,stroke='#142b45',dash=None,width=1.5):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
def px(s):return 80+(s+1)*320/3
def py(r):return 420-(r+1)*320/3
text(65,42,'Where the model can send an input','title')
parts.append('<polygon points="80,420 400,420 400,100" fill="#d6eadd"/>')
for z in [-1,0,1,2]:
 line(px(z),100,px(z),420,'#dbe1e8');line(80,py(z),400,py(z),'#dbe1e8')
 text(px(z),447,str(z),'small','middle');text(61,py(z)+5,str(z),'small','end')
parts.append('<rect x="80" y="100" width="320" height="320" fill="none" stroke="#142b45"/>')
line(80,420,400,100,'#278150',None,2.5)
line(px(0),100,px(0),py(0),'#b23b32','6 5',3)
line(px(0),py(0),px(0),420,'#278150',None,3)
text(95,82,'output r','label');text(240,478,'input s','label','middle')
text(286,342,'allowed: r ≤ s','label','middle')
text(98,136,'r > s','label');text(98,160,'zero kernel','small')
text(191,283,'s = 0','small');text(194,307,'r = 0','small')
text(68,516,'Dashed red: a boundary source has','small')
text(68,539,'no positive output under this model.','small')
text(68,572,'Exact support bound: HM18–HM19.','small')
text(555,42,'Every source derivative and error gain','title')
boxes=[(85,68,['Original jets: Uₐ ∈ H^(σ−a−½)','0 ≤ a < m']),
 (185,72,['q-th source part C_P^(q) U','H_(−m, σ+q), supported at r = 0']),
 (290,92,['Either E_N Q_N or Q_N F_N, restricted to r > 0','H_(ν, σ+q+N−ν), every real ν','Full source: q = 0,…,m−1']),
 (420,83,['Trace k, then boundary row of order mⱼ−k','H^(σ+q+N−mⱼ−½)','Choose ν > k+½ before taking the trace'])]
for y,h,labels in boxes:
 parts.append(f'<rect x="550" y="{y}" width="520" height="{h}" rx="9" class="box"/>')
 for i,label in enumerate(labels):text(810,y+27+i*24,label,'small','middle')
for y1,y2 in [(153,185),(257,290),(382,420)]:
 line(810,y1,810,y2-5,'#315b88',None,2)
 parts.append(f'<path d="M 805 {y2-12} L 810 {y2-5} L 815 {y2-12}" fill="none" stroke="#315b88" stroke-width="2"/>')
text(555,548,'The two errors act on their respective bundles.','small')
text(555,572,'Exact maps: HM11, HM14, HM24–HM27.','small')
parts.append('</svg>');OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT.name)
