"""Reproducible proof diagram; exact local hypotheses and full fibre rings."""
from pathlib import Path
import hashlib
import json
import sysconfig
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

OUT = Path(__file__).resolve().parent.parent / 'assets' / 'proper-curve-and-embedding-proof-map.png'
SIZE = (2600, 3400)
FONT = Path(sysconfig.get_paths()['purelib']) / 'matplotlib/mpl-data/fonts/ttf/DejaVuSans.ttf'
BOLD = FONT.with_name('DejaVuSans-Bold.ttf')
assert FONT.is_file() and BOLD.is_file()
glyphs = {False: set(TTFont(FONT).getBestCmap()),
          True: set(TTFont(BOLD).getBestCmap())}
im = Image.new('RGB', SIZE, '#f5f8fb')
d = ImageDraw.Draw(im)
fonts = {s: ImageFont.truetype(str(FONT), s) for s in (32, 34, 37, 42, 62)}
bold = {s: ImageFont.truetype(str(BOLD), s) for s in (37, 42, 62)}

def line(text, xy, size=34, fill='#172c40', strong=False):
    font = bold[size] if strong else fonts[size]
    assert all(ord(c) in glyphs[strong] for c in text), text
    assert d.textbbox((0, 0), text, font=font)[2] < 2340, text
    d.text(xy, text, font=font, fill=fill)

def box(y, title, lines, color):
    assert len(lines) <= 6
    d.rounded_rectangle((100, y, 2500, y+370), radius=25,
                        fill='white', outline=color, width=5)
    d.rectangle((100, y+25, 114, y+345), fill=color)
    line(title, (145, y+25), 42, color, True)
    for j, text in enumerate(lines):
        line(text, (145, y+98+j*42), 34)

def arrow(y, color):
    d.line((1300, y, 1300, y+40), fill=color, width=6)
    d.polygon([(1287, y+25), (1313, y+25), (1300, y+45)], fill=color)

line('Local poles, finite maps and closed immersions', (100, 65), 62, strong=True)
line('Proof implications with the actual rings, residual degrees and hypotheses', (100, 155), 37)
line('A. Regular integral proper curve C over an arbitrary field k; dim C = 1',
     (100, 240), 37, '#245b83', True)

box(315, 'Local valuation ring — DFR1–DFR7', [
    'R Noetherian local; dim R = dimκ(m/m²) = 1. Nakayama gives m = (π).',
    'Rees modules ⇒ Artin–Rees ⇒ intersection of all mⁿ is zero.',
    'Dimension one forces π to be nonnilpotent; every nonzero a is uπᵛ, u a unit.',
    'This proves the domain property, every nonzero ideal (πⁿ), the valuation and normality.'
], '#245b83')
arrow(688, '#245b83')
box(745, 'A point ideal and a genuine pole — PCF1–PCF7', [
    'Choose a closed point x; ℓ = [κ(x):k] is finite and positive.',
    'Iₓ is invertible. Lₙ = Iₓ⁻ⁿ; H⁰(Lₙ/O) has k-dimension nℓ.',
    'Proper coherent finiteness: g = dim H¹(C,O) is finite.',
    'h⁰(Lₙ) ≥ h⁰(O) + nℓ − g; choose nℓ > g to obtain an actual pole.',
    'The section u is regular off x, has pole order m at x, and is transcendental over k.'
], '#245b83')
arrow(1118, '#245b83')
box(1175, 'The whole finite map and its degree — PCF8–PCF12', [
    'Glue [1:u] off x and [u⁻¹:1] near x to obtain t : C → P¹ₖ.',
    'Properness and finite geometric fibres, including the generic fibre, give finiteness.',
    'The infinity fibre has ring O_C,x/(πᵐ); its k-dimension is mℓ.',
    'DVR module bases prove t finite locally free of rank [K(C):k(u)] = mℓ.',
    't*O(1) = O(m[x]); explicit finite-cover coordinates in 0.F.4A prove projectivity.'
], '#245b83')

line('B. A map f with its own embedding hypotheses; Y locally Noetherian',
     (100, 1645), 37, '#386d48', True)
box(1720, 'Full geometric fibre criterion — EF1 and CIE1', [
    'Assume f proper and each full geometric fibre is empty or Spec K.',
    'Theorem 0.F.1 gives f finite. On a target chart: B → C, C a finite B-module.',
    'Q = coker(B → C) is finite. Q ⊗B K = 0 at every geometric target point.',
    'Faithful field extension gives Qₚ/pQₚ = 0; finite Nakayama gives Qₚ = 0.',
    'Thus B → C is onto: the source is the actual quotient by its kernel.'
], '#386d48')
arrow(2093, '#386d48')
box(2150, 'How point and tangent separation supply that hypothesis — CIE2', [
    'Require both injections for every algebraically closed extension K/k.',
    'EF1 gives a common algebraically closed overfield for two hypothetical fibre points.',
    'Point injectivity makes the fibre empty or a one-point finite-type K-scheme.',
    'B1 gives a local Artin fibre ring R with residue K.',
    'Its tangent space is Hom_K(m/m²,K). Tangent injectivity makes it zero.',
    'Finite Nakayama gives m = 0, so the full ring R equals K.'
], '#386d48')
arrow(2523, '#386d48')
box(2580, 'Relative coordinates retain the entire base — EF2 and CIE3', [
    'S Noetherian, X proper/S, i : X → Pʳ_S; each geometric base fibre map is a closed immersion.',
    'For a target geometric point with field K, EF2 embeds the chosen closure of κ(s) in K.',
    'A closed immersion stays a quotient map after every base change.',
    'Its full fibre is a quotient of K: empty or Spec K. Apply CIE1 to i.',
    'The whole relative map is a closed immersion, with all base nilpotents retained.'
], '#386d48')

line('Rank-one conclusion — CIE4', (100, 3040), 37, '#172c40', True)
line('For any ring A, a finite locally free rank-one unital A-algebra is A: its unit is a local basis.',
     (100, 3100), 34)
line('A residual divisor is a graph once its finite locally free rank-one hypothesis is proved.',
     (100, 3150), 34)
line('Exact proof locators: Lesson 3, 0.F.4.1–0.F.4.4; the diagram displays implication chains.',
     (100, 3240), 32)
line('No fibre is replaced by its reduction; point counts are distinct from lengths and degrees.',
     (100, 3290), 32)
im.save(OUT, format='PNG', optimize=True)
print(json.dumps({'path': str(OUT.resolve()), 'size': SIZE,
                  'bytes': OUT.stat().st_size,
                  'sha256': hashlib.sha256(OUT.read_bytes()).hexdigest()}))
