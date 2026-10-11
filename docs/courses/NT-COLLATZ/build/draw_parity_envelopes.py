"""Reproduce the exact reflection map at first visit to height two."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
original=[0,1,2,1,2,3,2,1,0]
reflected=[0,1,2,3,2,1,2,3,4]
assert reflected==original[:3]+[4-y for y in original[3:]]
def points(y):return ' '.join(f'{52+43*i},{258-43*v}' for i,v in enumerate(y))
s=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="365" viewBox="0 0 440 365" role="img" aria-labelledby="title desc">',
'<title id="title">Reflection after the first hit</title><desc id="desc">Original heights 0,1,2,1,2,3,2,1,0; reflected heights 0,1,2,3,2,1,2,3,4. First hit of height2 at time2.</desc>',
'<rect width="440" height="365" fill="#fff"/>',
'<g font-family="Arial,sans-serif" font-size="15" fill="#172c38">',
'<text x="24" y="27" font-size="18" font-weight="bold">Reflect the path after its first hit</text>']
for y in range(5):
    py=258-43*y
    s.append(f'<line x1="52" y1="{py}" x2="400" y2="{py}" stroke="#dce4e9"/><text x="30" y="{py+5}">{y}</text>')
for i in range(9):s.append(f'<text x="{48+43*i}" y="282">{i}</text>')
s+=['<text x="20" y="69">Y</text><text x="408" y="282">j</text>',
'<line x1="52" y1="172" x2="400" y2="172" stroke="#687c8a" stroke-dasharray="5 4"/>',
'<text x="322" y="163">a = 2</text>',
f'<polyline points="{points(original)}" fill="none" stroke="#196276" stroke-width="4"/>',
f'<polyline points="{points(reflected)}" fill="none" stroke="#b55b19" stroke-width="3" stroke-dasharray="7 4"/>',
'<circle cx="138" cy="172" r="6" fill="#fff" stroke="#172c38" stroke-width="2"/>',
'<text x="91" y="153">first hit</text>',
'<line x1="26" y1="312" x2="66" y2="312" stroke="#196276" stroke-width="4"/>',
'<text x="77" y="317">original ends at 0</text>',
'<line x1="26" y1="339" x2="66" y2="339" stroke="#b55b19" stroke-width="3" stroke-dasharray="7 4"/>',
'<text x="77" y="344">reflected ends at 4</text>',
'</g></svg>']
(R/'figures/parity-reflection.svg').write_text('\n'.join(s)+'\n',encoding='utf-8')
print('Exact reflection figure generated.')

