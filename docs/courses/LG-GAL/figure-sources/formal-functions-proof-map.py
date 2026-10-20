"""Reproduce the actual Rees base change, kernel square and formal-functions bounds."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def installed_font_path(filename):
    try:
        return Path(ImageFont.truetype(filename,12).path)
    except OSError:
        return Path(filename)

import math

W, H = 2600, 3460
OUT = Path(__file__).resolve().parent.parent / 'assets' / 'formal-functions-proof-map.png'
REG = [installed_font_path('segoeui.ttf'), installed_font_path('DejaVuSans.ttf')]
BOLD = [installed_font_path('segoeuib.ttf'), installed_font_path('DejaVuSans-Bold.ttf')]
regular = next(p for p in REG if p.is_file())
bold = next(p for p in BOLD if p.is_file())
im = Image.new('RGB', (W, H), '#f5f7fb')
draw = ImageDraw.Draw(im)
INK, BLUE, GREEN, MUTED = '#18243a', '#174e87', '#17644c', '#43546e'

def paragraph(text, box, size=32, color=INK, strong=False):
    x0, y0, x1, y1 = box
    font = ImageFont.truetype(str(bold if strong else regular), size)
    lines = []
    for source_line in text.split('\n'):
        current = ''
        for word in source_line.split():
            candidate = (current + ' ' + word).strip()
            if draw.textlength(candidate, font=font) <= x1 - x0:
                current = candidate
            else:
                assert current, ('Unbreakable label', word)
                lines.append(current)
                current = word
        lines.append(current)
    line_height = size + 12
    assert y0 + len(lines) * line_height <= y1, ('Text overflow', text[:100], len(lines), box)
    for i, line in enumerate(lines):
        draw.text((x0, y0 + i * line_height), line, font=font, fill=color)

def panel(top, bottom, title):
    draw.rounded_rectangle((70, top, 2530, bottom), radius=20, fill='white', outline='#c5d0df', width=3)
    paragraph(title, (100, top + 18, 2500, top + 84), 39, BLUE, True)

def node(box, text):
    draw.rounded_rectangle(box, radius=12, fill='#edf3fa', outline=BLUE, width=3)
    paragraph(text, (box[0] + 20, box[1] + 16, box[2] - 20, box[3] - 8), 30)

def arrow(start, end, color=BLUE):
    draw.line((start, end), fill=color, width=5)
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    base = (end[0] - 23 * ux, end[1] - 23 * uy)
    draw.polygon([end, (base[0] - 10 * uy, base[1] + 10 * ux), (base[0] + 10 * uy, base[1] - 10 * ux)], fill=color)

paragraph('Formal functions: products, kernels and limits', (80, 42, 2520, 136), 55, INK, True)
paragraph('A Noetherian; I an ideal; f: X -> Spec A proper; F coherent. Every nilpotent is retained.\n'
          'T = A[It]; M_(q,n) = H^q(X, I^n F). I^n F means the image product.',
          (80, 145, 2520, 247), 32, MUTED)

panel(270, 1080, '1. Finite graded cohomology on an actual proper base change')
node((120, 385, 1080, 505), 'X_T = X x_(Spec A) Spec T\nG is the constructed product sheaf')
node((1520, 385, 2480, 505), 'X\nF is the original coherent sheaf')
node((120, 700, 1080, 812), 'Spec T\nT = A[It], a Noetherian ring')
node((1520, 700, 2480, 812), 'Spec A\nThe original base')
arrow((1080, 445), (1520, 445))
paragraph('projection p', (1098, 398, 1500, 439), 27, BLUE)
arrow((600, 505), (600, 700))
paragraph('f_T is proper', (650, 582, 1450, 634), 29, BLUE)
arrow((2000, 505), (2000, 700))
paragraph('f is proper', (2050, 582, 2460, 634), 29, BLUE)
arrow((1080, 755), (1520, 755))
paragraph('base change', (1098, 708, 1500, 749), 27, BLUE)
paragraph('On U = Spec C: Q_U = direct_sum_(n >= 0) I^n M, for F|U associated to M.\n'
          'Degree-zero generators of M generate Q_U over C tensor_A T. Localization glues G.\n'
          'Finite affine Cech comparison gives H^q(X_T,G) = E_q = direct_sum_n M_(q,n).\n'
          'Proper coherence over T makes E_q finite. This constructs G; no nonflat cohomology base-change assertion is used.',
          (100, 848, 2500, 1060), 31, GREEN)

panel(1100, 2210, '2. A kernel generator is killed through the actual commuting square')
paragraph('Fix q; write M_n = M_(q,n). tau_(n,m) comes from I^n F included in I^m F.\n'
          'K_n = ker(M_n -> M_0). Homogeneous generators y have degrees e <= c. Take n >= c.',
          (100, 1193, 2500, 1305), 32)
node((120, 1410, 1080, 1525), 'I^(n-e) tensor_A M_e\na tensor y, with y in K_e')
node((1520, 1410, 2480, 1525), 'M_n\na y')
node((120, 1790, 1080, 1905), 'I^(n-e) tensor_A M_0\na tensor tau_(e,0)(y) = 0')
node((1520, 1790, 2480, 1905), 'M_(n-e)\nThe image of a y is 0')
arrow((1080, 1467), (1520, 1467))
paragraph('multiplication', (1098, 1413, 1510, 1460), 27, BLUE)
arrow((600, 1525), (600, 1790))
paragraph('1 tensor tau_(e,0)', (650, 1633, 1460, 1690), 29, BLUE)
arrow((2000, 1525), (2000, 1790))
paragraph('tau_(n,n-e)', (2050, 1633, 2480, 1690), 29, BLUE)
arrow((1080, 1847), (1520, 1847))
paragraph('multiplication', (1098, 1793, 1510, 1840), 27, BLUE)
paragraph('Since n-e >= n-c, the further transition to M_(n-c) also kills a y.\n'
          'A finite homogeneous list generates K = direct_sum K_n over T. It gives\n'
          'K_n = ker(M_n -> M_(n-c)) for n >= c; every K_(n+c) -> K_n is zero.\n'
          'The separate finite list for E_q gives M_n = image(I^(n-c) tensor_A M_c -> M_n).',
          (100, 1950, 2500, 2186), 32, GREEN)

panel(2230, 2895, '3. The error system disappears before the limits are identified')
paragraph('M = M_(q,0); U_n = image(M_(q,n) -> M). For n >= c:\n'
          'I^n M is included in U_n, and U_n is included in I^(n-c) M.\n'
          '0 -> M/U_n -> B_n = H^q(X,F/I^n F) -> K_(q+1,n) -> 0.\n'
          'Choose c for both degrees q and q+1. If r >= n+c, the error transition is zero.\n'
          'The image of B_r -> B_n is exactly M/U_n: representatives from M lift it.\n'
          'Every compatible B-family therefore lies in the image modules coordinate by coordinate.\n'
          'The two displayed filtrations are cofinal by a fixed shift. Their quotient maps identify\n'
          'completion_I M = inverse_limit_n B_n, with the actual limit topologies.\n'
          'No general exactness theorem for inverse limits is a premise. For a finite local module,\n'
          'zero completion implies zero residue quotient by successive lifts, then zero module by Nakayama.',
          (100, 2325, 2500, 2860), 32)

panel(2915, 3315, '4. Exercise 6.22: a tensor creates a spurious degree-one piece')
paragraph('A = k[eps]/(eps^2); I = (eps); F is associated to A/I.\n'
          'Image product I F = 0. But I tensor_A (A/I) = I/I^2 = k is nonzero.\n'
          'Multiplication sends eps tensor 1 to 0. The constructed sheaf uses the zero image.\n'
          'E_0 is k in degree zero only. All transition kernels and U_n (n >= 1) are zero.\n'
          'F/I^n F = F with identity transitions, so both limits in formal functions are k.',
          (100, 3010, 2500, 3290), 32)
paragraph('Exact proof: FFR1-FFR9; Exercise6.22 has an8-point full solution. All diagrams are schematic; eps means epsilon.\n'
          'Free human sources: Stacks project authors, Tags02O8/02OA/02OB/02OC. Local inputs: N1/N2, AS3-AS7, SC5/SC11-SC12, PF3, Theorem0.C.10.',
          (80, 3340, 2520, 3445), 27, MUTED)
im.save(OUT)
print(f'{OUT.resolve()} | {W}x{H} RGB')
