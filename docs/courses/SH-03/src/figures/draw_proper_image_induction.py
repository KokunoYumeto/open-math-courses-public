from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Original diagram by OpenAI GPT-6 Astra, October 2026. CC0.
# Proof: https://github.com/KokunoYumeto/open-math-courses/blob/main/docs/courses/SH-03/src/weierstrass-parametrization-and-connected-regular-loci.md#proper-holomorphic-images
# Mathematical credits: Remmert; Demailly II §8.1–8.2; Shiffman removal via the linked course proof.
def font_file(preferred, fallback):
    try:
        ImageFont.truetype(preferred, 20)
        return preferred
    except OSError:
        ImageFont.truetype(fallback, 20)
        return fallback

W = Path(__file__).resolve().parent
im = Image.new('RGB', (1500, 1180), '#ffffff')
d = ImageDraw.Draw(im)
font_path = font_file('seguisym.ttf', 'DejaVuSans.ttf')
font = ImageFont.truetype(font_path, 23)
small = ImageFont.truetype(font_path, 20)
title = ImageFont.truetype(font_file('arialbd.ttf', 'DejaVuSans-Bold.ttf'), 31)

def box(rect, lines, fill='#eef5fb'):
    d.rounded_rectangle(rect, radius=14, fill=fill, outline='#214766', width=2)
    x0,y0,x1,y1=rect
    h=len(lines)*33
    for k,line in enumerate(lines):
        b=d.textbbox((0,0),line,font=font)
        d.text(((x0+x1-b[2])/2,(y0+y1-h)/2+k*33),line,font=font,fill='#14293b')

def arrow(points, label=None, labelpos=None):
    d.line(points, fill='#214766', width=4)
    x,y=points[-1];px,py=points[-2]
    if y>py: tri=[(x,y),(x-8,y-14),(x+8,y-14)]
    elif y<py: tri=[(x,y),(x-8,y+14),(x+8,y+14)]
    elif x>px: tri=[(x,y),(x-14,y-8),(x-14,y+8)]
    else: tri=[(x,y),(x+14,y-8),(x+14,y+8)]
    d.polygon(tri,fill='#214766')
    if label: d.text(labelpos,label,font=small,fill='#14293b')

d.text((70,35),'Proper-image proof: the smaller source closes the induction',font=title,fill='#14293b')
box((70,105,1430,210),['f : A → N proper; A irreducible, dimℂ A = d; generic rank = r',
                         'D = singular points ∪ regular rank-drop points; dimℂ D ≤ d − 1'])
arrow([(750,210),(750,266)],'restrict f to D',(790,225))
box((400,266,1100,355),['B = f(D) is closed analytic by induction'])
arrow([(1100,310),(1230,310),(1230,430)],'B = f(A)',(1250,355))
box((1080,430,1430,510),['Image already analytic'],fill='#e8f4ea')
arrow([(750,355),(750,430)],'B ≠ f(A)',(780,380))
box((70,430,1000,540),['T = A ∩ f⁻¹(B) is a proper analytic subset of A',
                       'Every fibre in T has real dimension ≥ 2(d − r)'])
arrow([(420,540),(420,604)],'finite chart fibre-dimension formula',(475,565))
box((70,604,750,704),['dimℝ B + 2(d − r) ≤ dimℝ T ≤ 2d − 2',
                      'Hence dimℝ B ≤ 2r − 2'])
box((805,604,1430,704),['f : A ∖ T → N ∖ B is proper, constant rank r',
                        'C = f(A) ∖ B is pure analytic; f(A) = closure(C)'])
arrow([(890,540),(1110,540),(1110,604)])
arrow([(410,704),(410,775),(750,775),(750,820)])
arrow([(1110,704),(1110,775),(750,775)])
box((160,820,1340,940),['For r ≥ 1: E = B ∪ (f(A) ∖ real-analytic regular locus)',
                        'E is closed subanalytic, dimℝ E ≤ 2r − 2; f(A) ∖ E = Creg is pure complex r',
                        'The pure-dimensional removal theorem makes f(A) analytic'],fill='#e8f4ea')
d.text((80,995),'r = 0: either B = f(A), or B is empty and proper constant rank gives a locally finite image.',font=small,fill='#14293b')
d.text((80,1040),'Fibre bound: local parametrization → analytic disc → compact analytic sets in a Euclidean chart are finite',font=small,fill='#14293b')
d.text((80,1072),'→ boundary-separated finite projection → upper semicontinuity → fibre dimension ≥ d − r.',font=small,fill='#14293b')
d.text((80,1110),'Proper-map induction: Demailly II §8.1–8.2. See proof §§1–6.',font=small,fill='#526273')
d.text((80,1142),'Removal: Complex conicity and analytic Lagrangian closures, “Proof of removal across a subanalytic exceptional set”.',font=small,fill='#526273')
im.save(W/'proper-image-induction.png')
