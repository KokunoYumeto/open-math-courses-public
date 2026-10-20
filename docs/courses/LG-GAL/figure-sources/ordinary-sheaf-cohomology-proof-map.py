"""Reproduce the ordinary cohomology proof map; Python3 and Pillow.
The grid coordinates are Cech/resolution degrees. eps denotes epsilon.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

def installed_font_path(filename):
    try:
        return Path(ImageFont.truetype(filename,12).path)
    except OSError:
        return Path(filename)


W, H = 2600, 3500
OUT = Path(__file__).resolve().parents[1] / 'assets/ordinary-sheaf-cohomology-proof-map.png'
REGULAR = [installed_font_path('segoeui.ttf'),
           installed_font_path('DejaVuSans.ttf')]
BOLD = [installed_font_path('segoeuib.ttf'),
        installed_font_path('DejaVuSans-Bold.ttf')]
reg = next((p for p in REGULAR if p.is_file()), None)
strong = next((p for p in BOLD if p.is_file()), None)
if reg is None or strong is None:
    raise RuntimeError('A listed Segoe UI or DejaVu Sans font is required.')
im = Image.new('RGB', (W, H), '#f6f8fb')
d = ImageDraw.Draw(im)
INK, MUTED = '#172b45', '#43546b'
BLUE, TEAL, PURPLE, ORANGE = '#235c95', '#076b6c', '#654093', '#9b591d'


def font(size, bold=False):
    return ImageFont.truetype(str(strong if bold else reg), size)


def para(text, box, size=35, color=INK, bold=False, gap=9):
    x0, y0, x1, y1 = box
    f = font(size, bold)
    yy = y0
    for textline in text.split('\n'):
        rows, current = [], ''
        for word in textline.split():
            trial = (current + ' ' + word).strip()
            if current and d.textlength(trial, font=f) > x1-x0:
                rows.append(current)
                current = word
            else:
                current = trial
        rows.append(current)
        for row in rows:
            assert d.textlength(row, font=f) <= x1-x0, (row, box)
            bounds = d.textbbox((x0, yy), row, font=f)
            assert bounds[3] <= y1, (row, box, bounds)
            d.text((x0, yy), row, font=f, fill=color)
            yy += size + gap
    return yy


def panel(box, title, body, color=BLUE, fill='white', size=35):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=25, fill=fill, outline=color, width=4)
    yy = para(title, (x0+26, y0+18, x1-26, y0+126),
              40, color, True, gap=7)
    d.line((x0+26, yy+7, x1-26, yy+7), fill=color, width=2)
    para(body, (x0+26, yy+24, x1-26, y1-20), size, gap=9)


def arrow(start, end, color=BLUE, width=6, head=20):
    x0, y0 = start
    x1, y1 = end
    d.line((x0, y0, x1, y1), fill=color, width=width)
    theta = math.atan2(y1-y0, x1-x0)
    d.polygon([(x1, y1),
               (x1-head*math.cos(theta)+head*.5*math.sin(theta),
                y1-head*math.sin(theta)-head*.5*math.cos(theta)),
               (x1-head*math.cos(theta)-head*.5*math.sin(theta),
                y1-head*math.sin(theta)+head*.5*math.cos(theta))], fill=color)



para('Ordinary sheaf cohomology: the finite mechanisms',
     (80,45,2520,135),60,INK,True)
para('Arbitrary rings and modules; positive resolutions; nilpotents retained.',
     (80,150,2520,210),37,MUTED)
para('SC1-SC15 | affine acyclicity uses degree induction, not proper coherence.',
     (80,215,2520,270),33,MUTED)

panel((80,315,640,735),'SC1 | Q/Z',
      'Divisibility extends maps by Zorn.\n'
      'Nonzero cyclic elements give nonzero characters.\n'
      'Q/Z is an injective cogenerator.',BLUE,'#edf4fd',size=31)
panel((730,315,1290,735),'SC2 | module injectives',
      'J_A=Hom_Z(A,Q/Z).\n'
      'Hom_A(M,J_A)=Hom_Z(M,Q/Z).\n'
      'Characters embed M into a product of copies of J_A.',TEAL,'#f0fbfa',size=31)
panel((1380,315,1940,735),'SC3 | point sheaves',
      'Choose injective J_x with F_x subset J_x.\n'
      'Stalk adjunction makes S_x J_x injective.\n'
      'Kernel of F -> product_x S_x J_x is zero by the x-projection at each stalk.',PURPLE,'#f7f2fc',size=30)
panel((2030,315,2520,735),'SC4 | open j!',
      'Extension by zero is exact.\n'
      'Injectives restrict to injectives.\n'
      'Restrictions of an injective sheaf are onto: it is flasque.',BLUE,'#edf4fd',size=30)
for x0,x1 in [(647,719),(1297,1369),(1947,2019)]:arrow((x0,530),(x1,530),BLUE)

panel((80,845,1220,1375),'SC5-SC7 | ordinary resolutions',
      '0 -> F -> I^0 -> I^1 -> ...\n'
      'H^n is kernel / image. Comparison maps differ by d h + h d.\n'
      'A flasque kernel lets local lifts glue: Gamma(U,G) -> Gamma(U,H) is onto.\n'
      'If kernel and middle are flasque, so is the quotient. Flasque sheaves are acyclic.\n'
      'Exact resolutions by acyclic terms compute cohomology by dimension shifting.',TEAL,'#f0fbfa',size=34)
panel((1380,845,2520,1375),'SC8-SC9 | the finite total complex',
      'Cech degree 0<=p<=r-1; resolution degree q>=0.\n'
      'partial = delta + (-1)^p d; mixed terms cancel.\n'
      'Flasque row augmentations identify total cohomology with ordinary cohomology.\n'
      'When intersections are acyclic, column augmentations identify it with Cech cohomology.\n'
      'Both cone chases take finitely many steps in each degree.',PURPLE,'#f7f2fc',size=34)
arrow((650,742),(650,832),TEAL)
arrow((1950,742),(1950,832),PURPLE)

# Coordinates in this grid are precisely Cech and resolution degrees.
d.rounded_rectangle((80,1490,1220,2250),radius=25,fill='#edf4fd',outline=BLUE,width=4)
para('SC11 | illustrated class degree n=3',(106,1510,1194,1575),40,BLUE,True)
para('Affine QC class; first move uses local db_i=c; r>=4.',(106,1580,1194,1645),30,INK)
x0,y0,stepx,stepy=225,2075,240,120
for j in range(4):
    d.line((x0+j*stepx,y0-3*stepy,x0+j*stepx,y0),fill='#d2dce8',width=2)
    d.line((x0,y0-j*stepy,x0+3*stepx,y0-j*stepy),fill='#d2dce8',width=2)
    d.text((x0+j*stepx-9,y0+10),str(j),font=font(26),fill=INK)
    d.text((x0-38,y0-j*stepy-15),str(j),font=font(26),fill=INK)
arrow((x0,y0),(x0+3*stepx+32,y0),BLUE,width=4,head=14)
arrow((x0,y0),(x0,y0-3*stepy-20),BLUE,width=4,head=14)
para('q: resolution',(650,1660,1190,1708),28,INK)
para('p: Cech',(990,2050,1190,2100),28,INK)
points=[(j,3-j) for j in range(4)]
for (a,b),(c,e) in zip(points,points[1:]):
    arrow((x0+a*stepx+18,y0-b*stepy+9),
          (x0+c*stepx-18,y0-e*stepy-9),TEAL,width=7,head=18)
for a,b in points:
    xx,yy=x0+a*stepx,y0-b*stepy
    d.ellipse((xx-10,yy-10,xx+10,yy+10),fill=TEAL)
    para(f'({a},{b})',(xx+15,yy-52,1190,yy+2),29,TEAL,True)
para('For q>0, subtract partial b with db=(-1)^p z.',
     (106,2150,1194,2205),30,INK)
para('At q=0 use SC10. If Cech columns end earlier, the class is already killed.',
     (106,2200,1194,2248),27,MUTED)

panel((1380,1490,2520,2250),'SC10-SC11 | two finite-power steps',
      'Principal cover: f_1,...,f_r generate 1.\n'
      'Clear the extra f_j denominators: t_j lifts f_j^N c.\n'
      'Then kill each discrepancy delta t_j - f_j^N c by another common power.\n'
      'Now delta t_j=f_j^N c over the original modules.\n'
      'Choose 1=sum a_j f_j^N. Then b=sum a_j t_j has delta b=c.\n'
      'For affine cohomology, first lift the global cocycle locally to db_i=c.\n'
      'Move (p,q) to (p+1,q-1) using vanishing in strictly lower positive degree.\n'
      'The last q=0 component lies in F and is killed by the principal-cover primitive.',BLUE,'#edf4fd',size=33)
arrow((650,1382),(650,1477),BLUE)
arrow((1950,1382),(1950,1477),BLUE)

panel((80,2380,1220,2900),'SC12-SC14 | affine covers and localization',
      'QC F; f:X->Y qc separated. On affine V=Spec(A), set Z=f^-1(V).\n'
      'Z has a finite cover with affine intersections: H^n(Z,F)=H^n(C).\n'
      'For a in A, C_a=C(F on Z_a). Exact localization gives H^n(C)_a=H^n(C_a).\n'
      'R^q f_*F is sheafified local cohomology; the principal-basis calculation on V makes it QC.\n'
      'Principal and prime localization are the base changes proved here.',TEAL,'#f0fbfa',size=34)
panel((1380,2380,2520,2900),'SC15 | all positive images vanish',
      'pi:Y->Z; H a module sheaf on Y; G=pi_*H.\n'
      'Assume R^q pi_*H=0 for every q>0.\n'
      'Push an injective resolution H -> I^bullet. Its image is an exact flasque resolution of G.\n'
      'Gamma(Z,pi_*I^bullet)=Gamma(Y,I^bullet).\n'
      'Hence H^n(Z,G)=H^n(Y,H).\n'
      'For g:Z->S, g_*pi_*I^bullet also gives R^n g_*G = R^n(g pi)_*H.',PURPLE,'#f7f2fc',size=34)
arrow((650,2257),(650,2367),TEAL)
arrow((1950,2257),(1950,2367),PURPLE)

panel((80,3020,2520,3335),'SC16 | a nonzero nilpotent cocycle has an actual signed primitive',
      'k a field; A=k[eps,t]/(eps^2). Cover by D(t) and D(1-t), since t+(1-t)=1.\n'
      'c=eps/[t(1-t)]; b_1=-eps/t; b_2=eps/(1-t).\n'
      'The ordered differential is delta b=b_2-b_1=c. The sign also works in characteristic two.\n'
      'eps is nonzero in A=k[t] + eps k[t], and stays nonzero after this localization.',ORANGE,'#fff9f0',size=34)
para('Local proofs SC0-SC16; grading exercises 6.16 and 6.17. Grid coordinates are cochain degrees.',
     (80,3390,2520,3438),30,MUTED)
para('Free human sources: the Stacks project authors, Tags 01D8, 09SV, 01X9, 01XB, 01E4, 01XJ.',
     (80,3445,2520,3496),30,MUTED)
assert W*H<10_000_000
im.save(OUT,format='PNG',optimize=True)
print(f'{OUT.name}: {W} x {H}; RGB; saved')
