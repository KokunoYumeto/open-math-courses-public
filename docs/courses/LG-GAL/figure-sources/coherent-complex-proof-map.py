"""Reproduce the finite-complex proof map in the accompanying assets; Python 3 + Pillow.

ASCII labels are notation for the exact TeX in FC1--FC11 of the accompanying
proof. Horizontal arrows in the top row are labelled construction steps;
the explicit chain map and tensor maps are written in the theorem band.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

def installed_font_path(filename):
    try:
        return Path(ImageFont.truetype(filename,12).path)
    except OSError:
        return Path(filename)


W, H = 2600, 3260
OUT = Path(__file__).resolve().parents[1] / 'assets/coherent-complex-proof-map.png'
REGULAR = [installed_font_path('segoeui.ttf'),
           installed_font_path('DejaVuSans.ttf')]
BOLD = [installed_font_path('segoeuib.ttf'),
        installed_font_path('DejaVuSans-Bold.ttf')]
regular = next((p for p in REGULAR if p.is_file()), None)
bold = next((p for p in BOLD if p.is_file()), None)
if regular is None or bold is None:
    raise RuntimeError('A listed Segoe UI or DejaVu Sans font is required.')
im = Image.new('RGB', (W, H), '#f6f8fb')
draw = ImageDraw.Draw(im)
INK, MUTED = '#172b45', '#43546b'
BLUE, TEAL, PURPLE, ORANGE = '#235c95', '#076b6c', '#654093', '#9b591d'


def font(size, strong=False):
    return ImageFont.truetype(str(bold if strong else regular), size)


def paragraph(text, box, size=34, color=INK, strong=False, gap=9):
    x0, y0, x1, y1 = box
    f = font(size, strong)
    yy = y0
    for para in text.split('\n'):
        rows, current = [], ''
        for word in para.split():
            test = (current + ' ' + word).strip()
            if current and draw.textlength(test, font=f) > x1-x0:
                rows.append(current)
                current = word
            else:
                current = test
        rows.append(current)
        for row in rows:
            assert draw.textlength(row, font=f) <= x1-x0, (row, box)
            bbox = draw.textbbox((x0, yy), row, font=f)
            assert bbox[3] <= y1, (row, box, bbox)
            draw.text((x0, yy), row, fill=color, font=f)
            yy += size + gap
    return yy


def panel(box, title, body, color=BLUE, fill='white', size=34):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=26, fill=fill, outline=color, width=4)
    yy = paragraph(title, (x0+26, y0+18, x1-26, y0+125),
                   38, color, True, gap=7)
    draw.line((x0+26, yy+8, x1-26, yy+8), fill=color, width=2)
    paragraph(body, (x0+26, yy+25, x1-26, y1-20), size, gap=9)


def arrow(start, end, color=BLUE, width=6, head=20):
    x0, y0 = start
    x1, y1 = end
    draw.line((x0, y0, x1, y1), fill=color, width=width)
    theta = math.atan2(y1-y0, x1-x0)
    draw.polygon([(x1, y1),
                  (x1-head*math.cos(theta)+head*.5*math.sin(theta),
                   y1-head*math.sin(theta)-head*.5*math.cos(theta)),
                  (x1-head*math.cos(theta)-head*.5*math.sin(theta),
                   y1-head*math.sin(theta)+head*.5*math.cos(theta))],
                 fill=color)


paragraph('Finite cohomology complexes and base change',
          (80, 45, 2520, 125), 60, INK, True)
paragraph('A Noetherian; f: X -> Spec(A) proper; F coherent and flat over A.',
          (80, 140, 2520, 200), 36, MUTED)
paragraph('Choose m affine charts; n=m-1. Nilpotents and arbitrary new base rings are allowed.',
          (80, 200, 2520, 260), 34, MUTED)

panel((80, 345, 820, 965), 'FC5 | finite affine Cech',
      'C^p = sum Gamma(U_I,F)\n'
      'for increasing |I|=p+1.\n'
      'Degrees 0 <= p <= n.\n'
      'Each C^p is A-flat; it need not be finite.\n'
      'Proper coherence makes H^q(C) finite.\n'
      'C tensor A\' is the pulled-back affine-cover complex.',
      BLUE, '#edf4fd', size=35)
panel((960, 345, 1670, 965), 'FC2-FC3 | finite free K',
      'Cone^i = C^i + K^(i+1)\n'
      'd(c,k) = (dc+f(k), -dk).\n'
      'For a cycle (c,k), attach e:\n'
      'd_K(e)=-k; f(e)=c.\n'
      'Then d_Cone(0,e)=(c,k).\n'
      'Finite generators kill one cohomology degree at a time.\n'
      'K^i finite free; K^i=0 for i>n.',
      TEAL, '#f0fbfa', size=33)
panel((1810, 345, 2520, 965), 'FC4 | projective cutoff',
      'Q = coker(K^-2 -> K^-1).\n'
      'For every A-module M:\n'
      'Q tensor M -> K^0 tensor M is injective.\n'
      'P = coker(K^-1 -> K^0)\n'
      'is flat and finitely presented, hence finite projective.\n'
      'E^0=P; E^i=K^i for 1<=i<=n.',
      PURPLE, '#f7f2fc', size=33)
arrow((827, 650), (950, 650), TEAL)
paragraph('attach', (835, 591, 950, 638), 28, TEAL, True)
arrow((1677, 650), (1800, 650), PURPLE)
paragraph('truncate', (1678, 591, 1808, 638), 27, PURPLE, True)

panel((80, 1060, 2520, 1310), 'FC4-FC5 | actual chain map, then every tensor specialization',
      'g: E -> C is a quasi-isomorphism. Its bounded flat cone stays acyclic after every tensor.\n'
      'For every A-algebra A\':  H^q(X_A\',F_A\') = H^q(E tensor_A A\').\n'
      'The degree-zero comparison sends actual sections to their pulled-back sections.',
      BLUE, '#edf4fd', size=33)
arrow((2165, 972), (2165, 1050), PURPLE)

panel((80, 1390, 2520, 1705), 'FC6 | remove actual unit entries near a base prime p',
      'Row and column operations give d^i = diag(1,D). The equations d^2=0 split off\n'
      'Ae --1--> Av in degrees i and i+1; h(v)=e contracts this summand after every tensor.\n'
      'Repeat finitely many times. Remaining differential entries lie in p at the chosen point.\n'
      'Their residue matrices are zero: rank(P^i) = dim H^i(E tensor kappa(p)).',
      TEAL, '#f0fbfa', size=34)
arrow((650, 1712), (650, 1832), BLUE)
arrow((1950, 1712), (1950, 1832), PURPLE)
paragraph('Add higher vanishing', (210, 1750, 1100, 1810), 32, BLUE, True)
paragraph('Add actual marked cycles', (1510, 1750, 2390, 1810), 32, PURPLE, True)

panel((80, 1845, 1220, 2280), 'FC7 | higher fibre H^q=0 for all q>0',
      'Then P^i=0 for i>0.\n'
      'If fibre h^0=r, P^0 is free of rank r.\n'
      'H^0 after every A\' is (A\')^r.\n'
      'Higher cohomology vanishes on this neighborhood and after every base change.\n'
      'No regularity or finite Krull dimension is assumed.',
      BLUE, '#edf4fd', size=34)
panel((1380, 1845, 2520, 2280), 'FC8 | marked sections span fibre H^0',
      'Lift actual sections to cycles v_j in P^0.\n'
      'Their column matrix V is invertible after localizing at det(V) not in p.\n'
      'd^0 V=0 forces d^0=0 over the ring.\n'
      'Thus H^0 after every A\' has that basis.\n'
      'Fibre H^1 may be nonzero.',
      PURPLE, '#f7f2fc', size=34)

panel((80, 2410, 1220, 2965), 'FC9 | field values do not kill nilpotents',
      'A=k[eps]/(eps^2), with k a field.\n'
      'D: A --eps--> A, degrees 0 and 1.\n'
      'H^0(D)=(eps); H^1(D)=k.\n'
      'The residue differential is zero; both fibre dimensions are 1.\n'
      'H^0(D) tensor_A k -> H^0(D tensor_A k)\n'
      'is the ZERO map: eps maps to 0.\n'
      'No actual cycle reduces to the fibre basis 1. This is an algebraic example.',
      ORANGE, '#fff9f0', size=34)
panel((1380, 2410, 2520, 2965), 'FC10-FC11 | two geometric uses',
      'Proper flat f; every geometric fibre nonempty and integral:\n'
      'the actual unit 1 spans fibre H^0.\n'
      'FC8 gives O_S = f_*O_X universally, with no higher-vanishing hypothesis.\n'
      'For a line bundle, higher vanishing plus fibre generation gives\n'
      'f^*(f_*L) ->> L after shrinking, by Nakayama and proper support.\n'
      'Closed immersion needs its separate proof.',
      TEAL, '#f0fbfa', size=33)

paragraph('Exact local proofs: FC1-FC11; equations FC1-FC21; graded exercises FC-E1 and FC-E2.',
          (80, 3050, 2520, 3115), 33, MUTED)
paragraph('Free human sources: the Stacks project authors, Tags 07VJ, 064U, 0653, 0656, 01XL, 01XM.',
          (80, 3120, 2520, 3190), 32, MUTED)
paragraph('eps means epsilon; tensor means tensor product over A; the proof fixes every domain and degree.',
          (80, 3190, 2520, 3250), 29, MUTED)
assert W * H < 10_000_000
im.save(OUT, format='PNG', optimize=True)
print(f'{OUT.name}: {W} x {H}; RGB; saved')
