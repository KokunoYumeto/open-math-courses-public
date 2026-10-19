"""CC0 exact schematic for SA.1--SA.7; SVG is dependency-free.

Run python strong-amenability-transfer-v25.py to create SVG and PNG. PNG rendering uses Pillow.
Run python strong-amenability-transfer-v25.py --svg-only for the portable standard-library SVG route.
Coordinates are display coordinates, not algebraic metric/area data.
"""
from pathlib import Path
from html import escape
import sys

HERE=Path(__file__).resolve().parent
W,H=1500,1080
BG='#f7f9fc'; INK='#172c42'; BLUE='#215e87'; GREEN='#267858'
commands=[]
def rect(x,y,w,h,fill,outline=INK): commands.append(('rect',(x,y,w,h,fill,outline)))
def text(x,y,t,size=25,color=INK): commands.append(('text',(x,y,t,size,color)))
def line(x1,y1,x2,y2,color=INK,width=3): commands.append(('line',(x1,y1,x2,y2,color,width)))
def arrow(x1,y1,x2,y2,color=INK):
    line(x1,y1,x2,y2,color)
    if x1==x2:
        line(x2,y2,x2-8,y2-13,color); line(x2,y2,x2+8,y2-13,color)
    else:
        line(x2,y2,x2-13,y2-8,color); line(x2,y2,x2-13,y2+8,color)
def node(x,y,w,h,title,sub,color='#ffffff'):
    rect(x,y,w,h,color)
    text(x+18,y+18,title,27)
    text(x+18,y+59,sub,21)

text(45,28,'Original amenability -> actual core admission and generation',34)
text(45,83,'SA.3--SA.5 require no factoriality; the physical trace and cups are retained.',24)
rect(35,133,1430,450,'#eaf1f8')
text(60,151,'Original inherited-trace core and canonical expected representation',27,BLUE)
node(70,210,365,110,'S = R intersect N  subset R','R and S may have centers here')
arrow(440,262,535,262,BLUE)
node(550,210,570,110,'A = <N,p>  subset_E_A  B = <M,p>','p = e_R^M on L2(M);  Tr(p) = 1')
text(1135,235,'SA.4',24,BLUE)
text(1135,277,'E_A|M = E_N',22)
text(70,347,'Finite level j:',25,BLUE)
text(70,395,"R_j = closure of union (N_l' intersect M_j)",25)
text(70,441,"x in N' intersect M_j  ->  x in R_j  ->  [x,p_j] = 0",25)
text(70,487,'p_j = e_R_j^M_j;  [x,N] = 0  ->  x commutes with the represented A.',24)
text(70,538,'The original upward cups e_j are unchanged;  tau(e_j) = 1/d.',24)

arrow(1410,594,1410,645,GREEN)
text(70,607,'All smooth representations -> compatible M-central state (singular allowed)',24,GREEN)
rect(35,660,1430,233,'#edf5ee')
text(60,677,'SA.6: add ergodic core (R factor); retain every prescribed finite prefix',27,GREEN)
text(60,720,'Every finite Y and tolerance; k = 2, r = 2: index a = d^3, endpoint m = 8.',24)
node(75,772,255,97,'U_0 = N_2','earlier g_0, g_1 fixed')
arrow(340,817,475,817,GREEN)
node(490,772,255,97,'U_1 <-> N_5','skipped ordinary level')
arrow(755,817,890,817,GREEN)
node(905,772,255,97,'U_2 <-> N_8','single aligner u in N_2')
text(1190,796,'SA.13',24,GREEN)
text(1190,835,'m = 3(3)-1',23)

arrow(1410,905,1410,958,GREEN)
text(70,921,'SA.7: separable predual supplies a dense countable sequence.',24,GREEN)
rect(35,973,1430,82,'#ffffff')
text(60,985,"One retained-prefix tunnel: closure of union (N_l' intersect M) = M",27)
text(60,1021,'The smaller closure is N. The general bicommutant implication remains unresolved (SA.8).',22)

svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Exact strong-amenability transfer, SA.1 through SA.7</title>',
 '<desc>Algebra boxes are schematic. The core projection has canonical trace one; physical cups have normalized trace one over d. The countable generating conclusion requires separable predual.</desc>',
 f'<rect width="{W}" height="{H}" fill="{BG}"/>']
for typ,arg in commands:
    if typ=='rect':
        x,y,w,h,fill,outline=arg
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{outline}" stroke-width="2"/>')
    elif typ=='line':
        x1,y1,x2,y2,color,width=arg
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"/>')
    else:
        x,y,t,size,color=arg
        svg.append(f'<text x="{x}" y="{y+size}" font-family="Arial,DejaVu Sans,sans-serif" font-size="{size}" fill="{color}">{escape(t)}</text>')
svg.append('</svg>')
(HERE/'strong-amenability-transfer-v25.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
if '--svg-only' in sys.argv:
    print('SVG created; PNG deliberately skipped.'); raise SystemExit
from PIL import Image,ImageDraw,ImageFont
fonts=['C:/Windows/Fonts/arial.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
def font(size):
    for f in fonts:
        if Path(f).exists(): return ImageFont.truetype(f,size)
    try: return ImageFont.truetype('DejaVuSans.ttf',size)
    except OSError: return ImageFont.load_default(size=size)
im=Image.new('RGB',(W,H),BG); draw=ImageDraw.Draw(im)
for typ,arg in commands:
    if typ=='rect':
        x,y,w,h,fill,outline=arg
        draw.rounded_rectangle((x,y,x+w,y+h),radius=9,fill=fill,outline=outline,width=2)
    elif typ=='line':
        x1,y1,x2,y2,color,width=arg
        draw.line((x1,y1,x2,y2),fill=color,width=width)
    else:
        x,y,t,size,color=arg
        draw.text((x,y),t,font=font(size),fill=color)
im.save(HERE/'strong-amenability-transfer-v25.png')
print('SVG and PNG created: SA.1--SA.7, 1500 x 1080.')
