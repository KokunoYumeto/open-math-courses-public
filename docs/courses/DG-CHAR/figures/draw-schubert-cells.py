"""Original Schubert partition diagram. Run with Pillow; outputs beside source.

Written by GPT-6.1 Sol (OpenAI), at Ultra. CC0-1.0.
The mathematical data are the pivot/partition correspondence in Section1 of
Schubert cells and universal Grassmannian cohomology, and its six-cell example.
This is a partition-size diagram; it does not depict attaching-map incidences.
"""
from pathlib import Path
from itertools import combinations
from PIL import Image, ImageDraw, ImageFont
import json,hashlib,html

OUT=Path(__file__).resolve().parent
WIDTH,HEIGHT=780,1040
BG='#f7f7ef';INK='#203d3b';FILL='#36968b';GRID='#c4cec7'
FONT=Path('C:/Windows/Fonts/arial.ttf')
if not FONT.exists():
    import PIL
    FONT=Path(PIL.__file__).resolve().parent/'fonts/DejaVuSans.ttf'
def font(size):
    try:return ImageFont.truetype(str(FONT),size)
    except OSError:return ImageFont.truetype('DejaVuSans.ttf',size)
im=Image.new('RGB',(WIDTH,HEIGHT),BG);draw=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
     '<title>Six Schubert cells of the real Grassmannian of two-planes in four-space</title>',
     '<desc>Panels list pivots, dimension and partitions in a two-by-two rectangle. Shaded box counts are zero, one, two, two, three and four. This is a partition-size diagram, not an incidence diagram.</desc>',
     f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{BG}"/>']
def text(x,y,s,size=32,fill=INK):
    draw.text((x,y),s,font=font(size),fill=fill)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}">{html.escape(s)}</text>')
def rectangle(x,y,w,h,fill,stroke=None,thick=2):
    draw.rectangle((x,y,x+w,y+h),fill=fill,outline=stroke,width=thick)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{thick}"' if stroke else '')+'/>')
text(32,22,'Six cells of Gr_2(R^4)',38)
text(32,72,'Pivots, real dimension, partition',29)
data=[]
for k,sigma in enumerate(combinations(range(1,5),2)):
    lam=(sigma[1]-2,sigma[0]-1);dim=sum(lam)
    x=24+(k%2)*384;y=140+(k//2)*284
    rectangle(x,y,348,258,'#ffffff',GRID)
    text(x+18,y+13,f'{sigma[0]},{sigma[1]}   |   dimension {dim}',29)
    for row in range(2):
        for col in range(2):
            rectangle(x+36+col*62,y+76+row*62,62,62,FILL if col<lam[row] else BG,INK,2)
    text(x+192,y+92,f'({lam[0]}, {lam[1]})',31)
    data.append({'pivots':sigma,'partition':lam,'real_dimension':dim,'shaded_boxes':sum(lam)})
text(32,1002,'Boxes count parameters; no incidences are shown.',26)
svg.append('</svg>')
im.save(OUT/'schubert-cells.png',optimize=True)
(OUT/'schubert-cells.svg').write_text('\n'.join(svg),encoding='utf-8')
(OUT/'schubert-cells-data.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print('Original diagram:',WIDTH,'x',HEIGHT,';',len(data),'cells; SHA256',hashlib.sha256((OUT/'schubert-cells.png').read_bytes()).hexdigest())
