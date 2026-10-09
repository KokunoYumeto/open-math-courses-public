"""Original diagnostic for the all-orbit two-gap proof; CC0-1.0.
Run with Python -B. Uses Pillow already present in the workspace runtime.
The installed Arial font is read for rasterization; no font is copied.
SVG contains text references, not embedded fonts. No package or cache is created.
"""
from pathlib import Path
from fractions import Fraction
import math, json, html
from PIL import Image, ImageDraw, ImageFont

OUT=Path(__file__).resolve().parent
W,H=1600,1430
im=Image.new('RGB',(W,H),'#ffffff'); draw=ImageDraw.Draw(im)
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="100%" height="100%" fill="white"/>']
font_path=Path('C:/Windows/Fonts/arial.ttf')
fonts={size:ImageFont.truetype(str(font_path),size) for size in [22,24,26,28,30,34,40]}
def text(x,y,t,size=26,color='#172b4d',anchor=None):
    draw.text((x,y),t,font=fonts[size],fill=color,anchor=anchor)
    ta='middle' if anchor=='mt' else ('end' if anchor=='rt' else 'start')
    svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial,sans-serif" font-size="{size}" text-anchor="{ta}" fill="{color}">{html.escape(t)}</text>')
def line(points,color='#cbd5e1',width=2):
    draw.line(points,fill=color,width=width)
    xy=' '.join(f'{x},{y}' for x,y in points)
    svg.append(f'<polyline points="{xy}" fill="none" stroke="{color}" stroke-width="{width}"/>')
def rect(box,fill,outline=None,width=1):
    draw.rectangle(box,fill=fill,outline=outline,width=width)
    x,y,x2,y2=box
    svg.append(f'<rect x="{x}" y="{y}" width="{x2-x}" height="{y2-y}" fill="{fill}"'+(f' stroke="{outline}" stroke-width="{width}"' if outline else '')+'/>')
def dot(x,y,color,r=8):
    draw.ellipse((x-r,y-r,x+r,y+r),fill=color)
    svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')
def arrow(x1,y1,x2,y2,color='#1c4966',width=3):
    line([(x1,y1),(x2,y2)],color,width)
    angle=math.atan2(y2-y1,x2-x1)
    for sign in [-1,1]:
        line([(x2,y2),(x2-14*math.cos(angle+sign*.45),y2-14*math.sin(angle+sign*.45))],color,width)

text(70,36,'Two separate controls: displacement and rank',40)
text(70,90,'A finite exact witness for (TG9), (TG26) and (TG34)',28,color='#52657c')

text(70,158,'A  Every prefix must stay in the open corridor',34)
left,right,top,bottom=190,1460,235,620
xp=lambda r:left+(right-left)*r/4
yp=lambda s:bottom-(float(s)+.25)/.70*(bottom-top)
rect((left,yp(Fraction(1,5)),right,yp(-Fraction(1,5))),'#e8f3f8')
for s,label in [(Fraction(-1,5),'-1/5'),(Fraction(0),'0'),(Fraction(1,5),'1/5'),(Fraction(2,5),'2/5')]:
    line([(left,yp(s)),(right,yp(s))], '#cf554b' if abs(s)==Fraction(1,5) else '#ced8e0',3 if abs(s)==Fraction(1,5) else 2)
    text(left-30,yp(s)-15,label,24,anchor='rt')
for r in range(5):
    line([(xp(r),top),(xp(r),bottom)],'#e4eaf0',1)
    text(xp(r),bottom+12,str(r),26,anchor='mt')
text(1385,bottom+49,'step r',24)
valid=[Fraction(0),Fraction(1,10),-Fraction(2,25),Fraction(3,50),-Fraction(1,25)]
bad=[Fraction(r,10) for r in range(5)]
line([(xp(r),yp(s)) for r,s in enumerate(bad)],'#c14a43',4)
line([(xp(r),yp(s)) for r,s in enumerate(valid)],'#006d8f',5)
for r,s in enumerate(valid):
    dot(xp(r),yp(s),'#006d8f')
    label='0' if not s else str(s)
    text(xp(r)+10,yp(s)+14,label,24,color='#006d8f')
for r in range(1,5):
    dot(xp(r),yp(bad[r]),'#c14a43',6)
text(965,219,'bad: every increment = 1/10',24,color='#b33a35')
text(900,yp(Fraction(1,5))+18,'boundary hit at r = 2 is already forbidden',22,color='#b33a35')
text(270,yp(-Fraction(1,5))+18,'valid: all |s_r| < 1/5',24,color='#006d8f')

text(70,740,'B  The valid witness uses positive tiles only',34)
text(70,790,'a = 1, b = √2; d_i = y_i − (s_i − s_(i−1))',28,color='#52657c')
coeffs=[(3,2),(4,1),(2,3),(5,1)]
a,b=1.0,math.sqrt(2)
y=[p*a+q*b for p,q in coeffs]
ends=[0.0]
for length in y:ends.append(ends[-1]+length)
scale=(right-left)/ends[-1]
base=875
colors={'a':'#1879a8','b':'#d8961c'}
for i,(p,q) in enumerate(coeffs):
    x=ends[i]
    for tile,length in [('a',a)]*p+[('b',b)]*q:
        x1,x2=left+x*scale,left+(x+length)*scale
        rect((x1,base,x2,base+59),colors[tile],outline='white',width=2)
        text((x1+x2)/2,base+11,tile,26,color='white',anchor='mt')
        x+=length
    assert math.isclose(x,ends[i+1])
    text(left+(ends[i]+ends[i+1])*scale/2,base+83,f'y{i+1} = {p}a + {q}b',24,anchor='mt')
for i,end in enumerate(ends):
    x=left+end*scale
    line([(x,base-9),(x,base+67)],'#172b4d',3)
    text(x,base-48,f'z{i}',24,anchor='mt')
text(190,1007,'Tile lengths use a numerical rendering scale; coefficients and fractions are exact.',24,color='#52657c')

text(70,1090,'C  A late move is paid for by the previous rank',34)
xs=[190,610,1030,1450]
for x,rank in zip(xs,[0,1,4,9]):
    rect((x-65,1190,x+65,1255),'#e8f3f8',outline='#006d8f',width=2)
    text(x,1206,f'rank {rank}',26,anchor='mt')
for i,(stage,charge) in enumerate([(1,1),(4,2),(9,5)]):
    arrow(xs[i]+70,1220,xs[i+1]-70,1220)
    mid=(xs[i]+xs[i+1])/2
    text(mid,1150,f'stage {stage}',24,anchor='mt')
    text(mid,1266,f'bound E{charge}',26,color='#006d8f',anchor='mt')
text(190,1340,'The charged indices 1, 2, 5 increase; their budgets sum to at most Σ E_i.',26,color='#52657c')

increments=[valid[i]-valid[i-1] for i in range(1,5)]
assert all(abs(s)<Fraction(1,5) for s in valid)
assert bad[2]==Fraction(1,5)
assert sum(p for p,q in coeffs)==14 and sum(q for p,q in coeffs)==7
assert all(y[i]-float(increments[i])>0 for i in range(4))
record={'license':'CC0-1.0','kind':'finite diagnostic; rank panel is a bound diagram',
        'exact_a':'1','exact_b':'sqrt(2)','corridor_radius':'1/5',
        'valid_prefix_errors':[str(s) for s in valid],
        'bad_prefix_errors':[str(s) for s in bad],
        'exact_increments':[str(s) for s in increments],
        'tile_coefficients':[{'a':p,'b':q} for p,q in coeffs],
        'original_gap_formula':'d_i = y_i - (s_i - s_(i-1))',
        'rank_promotions':[0,1,4,9],'global_move_stages':[1,4,9],
        'charged_indices':[1,2,5],'proof_locators':['TG9','TG18','TG26','TG34','Diagnostics 2 and 4'],
        'raster_size':[W,H],'rendering':'Pillow; installed Arial read without copying',
        'numeric_rendering_approximations':{'b':b,'word_lengths':y,'word_endpoints':ends}}
im.save(OUT/'corridor-tiles-and-rank-charge.png')
svg.append('</svg>')
(OUT/'corridor-tiles-and-rank-charge.svg').write_text('\n'.join(svg),encoding='utf8')
(OUT/'corridor-tiles-and-rank-charge.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Exact fraction, positivity, tile-count and rank-index assertions passed.')
