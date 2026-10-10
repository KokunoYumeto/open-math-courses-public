"""Exact series table and partial-sum plot for CRO:X1-X2."""
from pathlib import Path
from html import escape
out=Path(__file__).resolve().parent/'compact-ray-observation.svg'
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="570" viewBox="0 0 1040 570" role="img" aria-labelledby="title desc">',
 '<title id="title">Actual data columns and the limitation of dense tests</title>',
 '<desc id="desc">Left: exact entries j to the power n for j less than n, and two to the power minus j for j at least n. Right: exact partial sums J, minimum of J and 4, and minimum of J and 8.</desc>',
 '<rect width="1040" height="570" fill="#fff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#182a3b;font-size:16px}.head{font-size:20px;font-weight:bold}.small{font-size:14px}</style>']
def text(x,y,s,cls='',anchor='start'):
 svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def line(x1,y1,x2,y2,color='#435668',width=1.2):
 svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
def curve(points,color):
 svg.append('<polyline fill="none" stroke="'+color+'" stroke-width="3" points="'+' '.join(f'{x:.3f},{y:.3f}' for x,y in points)+'"/>')
text(30,32,'Every fixed data column has a finite square sum','head')
text(565,32,'Dense tests alone do not give the limit','head')
text(30,62,'a(j,n) = jⁿ for j < n;  a(j,n) = 2⁻ʲ for j ≥ n')
text(565,62,'Exact partial sums from the ℓ² example')
cx=70;cy=112;cw=65;ch=38
text(36,104,'j \\ n','small')
for n in range(1,7):text(cx+(n-.5)*cw,101,str(n),'','middle')
for j in range(1,9):
 text(50,cy+(j-.5)*ch+5,str(j),'','middle')
 for n in range(1,7):
  fill='#fff0d6' if j<n else '#d9eff1'
  svg.append(f'<rect x="{cx+(n-1)*cw}" y="{cy+(j-1)*ch}" width="{cw}" height="{ch}" fill="{fill}" stroke="#fff" stroke-width="2"/>')
  label=str(j**n) if j<n else '1/'+str(2**j)
  text(cx+(n-.5)*cw,cy+(j-.5)*ch+5,label,'small','middle')
svg.append('<rect x="70" y="442" width="16" height="16" fill="#fff0d6"/>')
text(94,455,'finite prefix for each column','small')
svg.append('<rect x="70" y="471" width="16" height="16" fill="#d9eff1"/>')
text(94,484,'square-summable dyadic tail','small')
plot=lambda J,S:(615+J*23,418-S*18)
for v in [0,4,8,12,16]:
 x,y=plot(0,v);x2,y2=plot(16,v);line(x,y,x2,y2,'#dce4e9');text(603,y+5,str(v),'small','end')
for J in [0,4,8,12,16]:
 x,y=plot(J,0);line(x,y,x,y+5);text(x,y+25,str(J),'small','middle')
line(*plot(0,0),*plot(16,0));line(*plot(0,0),*plot(0,17))
text(993,441,'J');text(598,94,'sum','small')
curve([plot(J,J) for J in range(1,17)],'#b64736')
curve([plot(J,min(J,8)) for J in range(1,17)],'#7759a6')
curve([plot(J,min(J,4)) for J in range(1,17)],'#087e8b')
text(894,113,'J','small');text(852,261,'min(J, 8)','small');text(852,334,'min(J, 4)','small')
text(565,484,'Finite truncations converge as tests,','small')
text(565,504,'but their series bounds need not pass to the limit.','small')
text(30,545,'CRO:X1–X2, equations CO22–CO23. Exact values and partial sums; these panels do not depict phase-space trajectories.','small')
svg.append('</svg>');out.write_text('\n'.join(svg)+'\n','utf-8');print(out)
