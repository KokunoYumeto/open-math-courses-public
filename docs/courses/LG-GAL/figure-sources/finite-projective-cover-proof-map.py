"""Reproduce the finite-cover coordinate proof map; Python3 + Pillow.

ASCII variables denote the exact TeX and domains in Section0.F.4A/FP1-FP5.
The drawn square is local to D+(Z_ii); its right projection is defined there.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def installed_font_path(filename):
    try:
        return Path(ImageFont.truetype(filename,12).path)
    except OSError:
        return Path(filename)

import math

W, H = 2600, 3120
OUT = Path(__file__).resolve().parents[1] / 'assets/finite-projective-cover-proof-map.png'
REGULAR = [installed_font_path('segoeui.ttf'), installed_font_path('DejaVuSans.ttf')]
BOLD = [installed_font_path('segoeuib.ttf'), installed_font_path('DejaVuSans-Bold.ttf')]
regular = next((p for p in REGULAR if p.is_file()), None)
bold = next((p for p in BOLD if p.is_file()), None)
if regular is None or bold is None:
    raise RuntimeError('A listed Segoe UI or DejaVu Sans font is required.')
im = Image.new('RGB', (W, H), '#f5f7fb')
draw = ImageDraw.Draw(im)
INK, MUTED, BLUE, GREEN = '#18243a', '#43546e', '#174e87', '#17644c'


def font(size, strong=False):
    return ImageFont.truetype(str(bold if strong else regular), size)


def paragraph(text, box, size=32, color=INK, strong=False):
    x0, y0, x1, y1 = box
    f = font(size, strong)
    lines = []
    for source_line in text.split('\n'):
        current = ''
        for word in source_line.split():
            trial = (current + ' ' + word).strip()
            if draw.textlength(trial, font=f) <= x1-x0:
                current = trial
            else:
                assert current, ('Unbreakable label too wide', word)
                lines.append(current)
                current = word
        lines.append(current)
    line_height = size + 12
    assert y0 + len(lines)*line_height <= y1, ('Text overflow', text[:90], len(lines), box)
    for index, line in enumerate(lines):
        draw.text((x0, y0+index*line_height), line, font=f, fill=color)


def panel(top, bottom, title):
    draw.rounded_rectangle((70, top, 2530, bottom), radius=20, fill='white', outline='#c5d0df', width=3)
    paragraph(title, (100, top+18, 2500, top+82), 40, BLUE, True)


def node(box, text):
    draw.rounded_rectangle(box, radius=14, fill='#edf3fa', outline=BLUE, width=3)
    paragraph(text, (box[0]+22, box[1]+18, box[2]-22, box[3]-8), 30)


def arrow(start, end, color=BLUE):
    draw.line((start, end), fill=color, width=5)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    length, width = 22, 10
    back = (end[0]-length*math.cos(angle), end[1]-length*math.sin(angle))
    pts = [end, (back[0]+width*math.sin(angle), back[1]-width*math.cos(angle)),
           (back[0]-width*math.sin(angle), back[1]+width*math.cos(angle))]
    draw.polygon(pts, fill=color)


paragraph('Finite covers give projective coordinates', (80, 42, 2520, 126), 57, INK, True)
paragraph('Theorem0.F.7: R Noetherian, n >= 0, t: X -> P_R^n finite. Nilpotents are retained.\nThe chosen embedding survives arbitrary R -> R\' after it is constructed.',
          (80, 137, 2520, 245), 32, MUTED)

panel(260, 620, '1. Finite maps are proper: the algebra calculation')
paragraph('On an affine target, B is a finite A-module. Its generators generate the algebra; the diagonal is the quotient B tensor_A B -> B.\nIntegrality + lying over give image Spec(B/J) = V(J intersect A). Every base-changed algebra remains finite, so closedness is universal.\nFinite type + closed diagonal + universal closedness prove properness (FP1).',
          (100, 340, 2500, 600), 32)

panel(640, 1100, '2. A finite pushforward supplies the missing coordinates')
paragraph('U_i = D+(X_i) = Spec A_i; A_i = R[X_j/X_i : j != i].\nt inverse(U_i) = Spec B_i, with B_i finite over A_i.\nF = t_* O_X is coherent. PF7 gives d >= 1 and r global generators of F(d).\nTheir pulled-back functions b_ai generate B_i as an A_i-module (FP3).\nAdd e_ij = t^*(X_i^(d-1) X_j), including e_i = e_ii, and sections s_a.\nThe list generates L^d, with L = t^* O(1), and defines Phi into P_R^N.\nN + 1 = (n + 1)^2 + r. Repeated coordinates are allowed.',
          (100, 720, 2500, 1080), 32)

panel(1120, 1960, '3. The actual chart square commutes')
paragraph('Phi inverse(D+(Z_ii)) = t inverse(U_i). Set u_j = Z_ij/Z_ii and v_a = H_a/Z_ii; w_l denotes the remaining target ratios.',
          (100, 1200, 2500, 1305), 31)
node((120, 1340, 1120, 1460), 'X_i = Spec B_i\nsource chart')
node((1480, 1340, 2480, 1460), 'D+(Z_ii) = Spec R[u_j,v_a,w_l]\ntarget chart')
node((120, 1660, 1120, 1770), 'U_i = Spec R[X_j/X_i : j != i]')
node((1480, 1660, 2480, 1770), 'U_i = Spec R[X_j/X_i : j != i]')
arrow((1120, 1400), (1480, 1400))
paragraph('Phi_i: closed immersion', (1120, 1308, 1480, 1344), 22, BLUE, True)
arrow((620, 1460), (620, 1660))
paragraph('t_i', (680, 1535, 1100, 1590), 30, BLUE)
arrow((1980, 1460), (1980, 1660))
paragraph('projection pi_i', (2040, 1520, 2460, 1580), 30, BLUE)
arrow((1120, 1710), (1480, 1710))
paragraph('identity', (1225, 1655, 1480, 1700), 27, BLUE)
paragraph('FP5: R[u_j,v_a,w_l] -> B_i; u_j -> t^*(X_j/X_i), v_a -> b_ai.\nIt is surjective: coefficients are polynomials in u_j, and every B_i element is their linear combination of the b_ai. No free basis is assumed.',
          (100, 1820, 2500, 1940), 31, GREEN)

panel(1980, 2360, '4. Local quotient maps give the whole projective closed image')
paragraph('Every source point lies above Omega = union_i D+(Z_ii).\nX is proper over R; the target is separated; the graph makes Phi proper.\nIts image is closed. Omega together with P_R^N minus Phi(X) covers the target.\nOn each selected chart Phi is the quotient by ker(FP5); on the complement its inverse image is empty. The quotient ideals glue.\nActual frames identify Phi^* O(1) with L^d. Quotient maps and frames pull back under every base change.',
          (100, 2060, 2500, 2340), 31)

panel(2380, 2960, '5. The target chart at infinity matters: Exercise6.21')
paragraph('R = k[eps]/(eps^2); B = R[z]/(z^2 - eps). The R-basis is 1,z.\nThe embedding is [U:V] = [1:z], with homogeneous ideal (V^2 - eps U^2).\nOn D+(U): R[v]/(v^2 - eps) = B, where v = V/U.\nOn D+(V): R[u]/(1 - eps u^2) = 0, where u = U/V,\nbecause (1 - eps u^2)(1 + eps u^2) = 1.\nThe geometric fibre has one point and length2; the total k-dimension is4.\nThe nonzero elements z, z^2 = eps, z^3 = eps z are lost on reduction.\nFor n = 0 in the theorem, A_0 = R and there are no u_j variables.',
          (100, 2460, 2500, 2940), 32)

paragraph('Exact proof: Section0.F.4A, FP1-FP5. All diagrams are schematic; eps means epsilon.',
          (80, 2980, 2520, 3030), 28, MUTED)
paragraph('Free human comparison: Stacks project authors, Tags0B3I and01W7; local prerequisites PF3, PF4, PF7, I1/I4, AS5-AS7.',
          (80, 3035, 2520, 3100), 27, MUTED)
assert W*H < 10_000_000
im.save(OUT, format='PNG', optimize=True)
print(f'{OUT.name}: {W} x {H}; RGB; saved')
