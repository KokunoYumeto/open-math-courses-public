from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
im = Image.new('RGB', (1720, 1100), '#f8fafc')
draw = ImageDraw.Draw(im)
from matplotlib.font_manager import findfont, FontProperties
font_path = findfont(FontProperties(family='DejaVu Sans'))
bold_path = findfont(FontProperties(family='DejaVu Sans', weight='bold'))
def font(size, bold=False): return ImageFont.truetype(bold_path if bold else font_path, size)
def txt(x,y,s,size=27,fill='#17263b',bold=False):
    while draw.textbbox((0,0),s,font=font(size,bold))[2] > 1650-x and size>18:
        size-=1
    draw.text((x,y), s, font=font(size,bold), fill=fill)
def panel(box, title):
    draw.rounded_rectangle(box, 20, fill='white', outline='#bac8da', width=2)
    txt(box[0]+24,box[1]+18,title,31,bold=True)
def arrow(x1,y1,x2,y2,color='#355f94'):
    draw.line((x1,y1,x2,y2), fill=color, width=4)
    if x1==x2:
        draw.polygon([(x2,y2),(x2-8,y2-13),(x2+8,y2-13)],fill=color)
    else:
        draw.polygon([(x2,y2),(x2-14,y2-8),(x2-14,y2+8)],fill=color)

txt(42,23,'Regular holonomic duality: the actual maps and the boundary lattice',36,bold=True)
txt(42,75,'Any smooth separated complex algebraic X; every closed support; every finite rank and Jordan block.',25)
panel((35,130,1685,373),'1. Dual lattice at every point of every complete curve (5.7c-5.7h)')
txt(65,188,'L in V,  Theta L in L',29,bold=True)
arrow(432,214,538,214)
txt(570,188,'L^vee = Hom_R(L,R) in V^vee',29,bold=True)
txt(65,245,'R = C[[t]] or C{t}; L full and free',27)
txt(570,240,'Theta^vee(phi)(v) = theta(phi(v)) - phi(Theta(v))',27)
txt(570,285,'Theta^vee L^vee in L^vee;  residue A becomes -A^T',28,fill='#176547')
txt(65,330,'The minus sign comes from the pairing; regularity includes all points at infinity.',26)

panel((35,400,1685,768),'2. Canonical extension map, with j = open u after closed i (5.7l-5.7s)')
txt(78,476,'H^0(j_! E)',30,bold=True)
txt(666,476,'j_!* E = image(can)',30,bold=True)
txt(1325,476,'H^0(j_* E)',30,bold=True)
arrow(278,500,626,500)
arrow(1010,500,1275,500)
txt(79,577,'H^0(j_! E^vee)',30,bold=True)
txt(648,577,'j_!* E^vee = D(j_!* E)',30,bold=True)
txt(1293,577,'H^0(j_* E^vee)',30,bold=True)
arrow(329,601,608,601)
arrow(1072,601,1245,601)
txt(431,454,'canonical map for E',25,fill='#355f94')
txt(426,550,'transpose = canonical map for E^vee',25,fill='#176547')
txt(72,663,'Duality reverses the arrows and exchanges the outer terms; it preserves the image and support.',27)
txt(72,708,'No boundary subobject on the dual: it would dualize to a forbidden boundary quotient, and conversely.',25)

panel((35,795,1685,1045),'3. Every composition factor and every cohomological degree (5.7t-5.7v)')
txt(69,854,'Factors of M:  S_1, ..., S_l',28,bold=True)
arrow(526,878,625,878)
txt(665,854,'Factors of D(M):  D(S_l), ..., D(S_1)',28,bold=True)
txt(69,917,'Each S_a = j_a,!* E_a becomes j_a,!* E_a^vee using the same affine inclusion.',28)
txt(69,972,'Bounded complexes:  H^q(D K) = D H^(-q)(K);  degrees [a,b] become [-b,-a].',28,fill='#176547')
txt(43,1061,'Exact proof locators: regular-singularities.md, 5.7c-5.7v. Diagram is schematic, not a restriction on support.',23)
target = ROOT / 'regular-duality-mechanism.png'
im.save(target)
print('Rendered regular-duality-mechanism.png')
