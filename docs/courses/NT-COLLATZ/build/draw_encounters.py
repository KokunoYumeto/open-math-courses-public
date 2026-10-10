"""Editable deterministic SVG source: common-row packing, schematic slope 2."""
from pathlib import Path
from html import escape

ROOT=Path(__file__).resolve().parents[1]
def main():
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="620" viewBox="0 0 900 620" role="img" aria-labelledby="title desc">',
         '<title id="title">Disjoint rows force separated left columns</title>',
         '<desc id="desc">Two lattice triangles of slope two have vertices (1,0),(1,8),(5,8) and (7,1),(7,9),(11,9). At height four their integer rows are 1,2,3 and 7,8. Their left columns cannot approach closer than a full row length without intersection. The drawing is a rational-slope schematic, not an arithmetic phase set.</desc>',
         '<rect width="900" height="620" fill="#fff"/>',
         '<g font-family="Arial, sans-serif" font-size="19" fill="#182c38">']
    def xy(x,y):return 90+59*x,500-42*y
    def line(x1,y1,x2,y2,stroke='#dfe6ea',width=1,dash=''):
        X,Y=xy(x1,y1); U,V=xy(x2,y2)
        out.append(f'<line x1="{X}" y1="{Y}" x2="{U}" y2="{V}" stroke="{stroke}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
    def text(x,y,s,anchor='start',size=19,colour='#182c38'):
        out.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{colour}">{escape(s)}</text>')
    text(40,35,'A shared height turns triangular geometry into interval packing',size=22)
    for x in range(13):line(x,0,x,10)
    for y in range(11):line(0,y,12,y)
    for left,bottom,top,colour in ((1,0,8,'#cfdeeb'),(7,1,9,'#dbebe1')):
        verts=[xy(left,bottom),xy(left,top),xy(left+(top-bottom)/2,top)]
        out.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in verts)+f'" fill="{colour}" stroke="#355c70" stroke-width="2"/>')
        for y in range(bottom,top+1):
            for x in range(left,left+(y-bottom)//2+1):
                X,Y=xy(x,y)
                out.append(f'<circle cx="{X}" cy="{Y}" r="3.2" fill="#355c70"/>')
    line(0,4,12,4,'#a53d29',2,'7 6')
    for lo,hi in ((1,3),(7,8.5)):
        line(lo,4,hi,4,'#a53d29',5)
        for x in range(lo,int(hi)+1):
            X,Y=xy(x,4);out.append(f'<circle cx="{X}" cy="{Y}" r="6" fill="#a53d29"/>')
    text(77,339,'t*',anchor='end',colour='#a53d29')
    text(184,279,'first row',size=18,colour='#a53d29')
    text(510,279,'second row',size=18,colour='#a53d29')
    text(192,137,'Δ′',size=24)
    text(540,93,'Δ″',size=24)
    line(0,0,12.25,0,'#182c38',2)
    line(0,0,0,10.2,'#182c38',2)
    text(834,506,'x')
    text(66,73,'y')
    for x in (0,1,3,5,7,8,11):
        X,Y=xy(x,0);text(X,Y+24,str(x),anchor='middle',size=16)
    for x,s in ((1,'u′'),(7,'u″')):
        X,Y=xy(x,0);text(X,Y+49,s,anchor='middle',size=21)
    text(450,588,'A common lattice point in these rows would belong to both triangles.',anchor='middle',size=19)
    out.append('</g></svg>')
    (ROOT/'figures/encounter-packing.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')

if __name__=='__main__':main()
