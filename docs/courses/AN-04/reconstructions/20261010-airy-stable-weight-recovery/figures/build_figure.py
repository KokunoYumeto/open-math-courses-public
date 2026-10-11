"""Exact phase displacement curve and separately labelled one-dimensional supports."""
from pathlib import Path
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="650" viewBox="0 0 1080 650">',
 '<rect width="1080" height="650" fill="#f8fafc"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b}.title{font-size:23px;font-weight:bold}.label{font-size:17px}.small{font-size:15px}.box{fill:white;stroke:#c6d3dc;stroke-width:2}</style>']
def text(x,y,t,cl='label'):
    parts.append(f'<text x="{x}" y="{y}" class="{cl}">{t}</text>')
text(28,36,'Stable Airy weight: phase displacement and cutoff reserve','title')
text(30,72,'Exact displacement curve; axes have different scales.')
text(570,72,'One-dimensional translation example (SW23).')
sx=lambda u:90+1320*u
sy=lambda v:145-36000*v
parts+=['<path d="M75 145 H445 M90 130 V380" stroke="#6c8192" fill="none"/>']
pts=[(sx(i/400),sy(-(i/400)**3/3)) for i in range(101)]
parts.append('<polyline stroke="#086e8c" stroke-width="3" fill="none" points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in pts)+'"/>')
parts.append(f'<circle cx="{sx(.25)}" cy="{sy(-1/192)}" r="5" fill="#086e8c"/>')
text(438,134,'dμ');text(36,123,'dλ')
text(67,168,'0','small');text(72,352,'−1/192','small')
text(390,125,'1/4','small')
text(150,384,'(dμ,dλ) = (s, −s³/3), 0 ≤ s ≤ 1/4','small')
text(30,418,'Endpoint: (1/4, −1/192); norm √2305/192 &lt; 13/50','small')
text(30,445,'SWR:D0, X3, V0. Both coordinate shifts are retained.','small')
tx=lambda x:810+135*x
for y,lo,hi,color,label in [
    (160,-1,1,'#086e8c','input cutoff support [−1,1]'),
    (240,-1.25,1.25,'#ba5935','all translates, |d| ≤ 1/4'),
    (320,-1.5,1.5,'#47805c','observation plateau [−3/2,3/2]')]:
    text(568,y-22,label)
    parts.append(f'<path d="M{tx(lo)} {y} H{tx(hi)}" stroke="{color}" stroke-width="7"/>')
    for x in [lo,hi]:parts.append(f'<path d="M{tx(x)} {y-7} V{y+7}" stroke="{color}" stroke-width="2"/>')
    text(tx(lo)-15,y+28,str(lo),'small');text(tx(hi)-12,y+28,str(hi),'small')
text(566,384,'E_d χ E_d⁻¹ = multiplication by χ(x−d)','small')
text(566,416,'This interval diagram is not a Euclidean norm bound.','small')
text(566,445,'SWR:D1–D3, X2, V0: keep the full spatial reserve.','small')
parts.append('<rect x="28" y="483" width="1024" height="139" rx="9" class="box"/>')
text(46,512,'The three controlled terms in the exact identity SW13','label')
text(46,543,'Observed phase term: unitary multipliers + smooth cutoff (D2).')
text(46,570,'Unobserved phase tail: full off-displacement kernel bound (D1).')
text(46,597,'Amplitude commutator: H_L → H⁵ᐟ⁶ by the weighted Fourier difference estimate (A1).')
parts.append('</svg>')
out=Path(__file__).with_name('airy-stable-weight-recovery.svg')
out.write_text('\n'.join(parts)+'\n','utf-8')
print(out)
