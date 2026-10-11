"""Reproduce the projective foundation map with Python 3 and Pillow.

Coordinates in the middle diagram are cochain degrees and tuple bases.
All other boxes are proof mechanisms, not geometric scale models.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 2600, 3640
SCALE = 13/15
OUT = Path(__file__).resolve().parents[1] / 'assets/projective-foundation-proof-map.png'
REGULAR = [Path('C:/Windows/Fonts/seguisym.ttf'),
           Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
BOLD = [Path('C:/Windows/Fonts/segoeuib.ttf'),
        Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')]
reg = next((p for p in REGULAR if p.is_file()), None)
strong = next((p for p in BOLD if p.is_file()), None)
if reg is None or strong is None:
    raise RuntimeError('Segoe UI or DejaVu Sans regular and bold fonts required.')
im = Image.new('RGB', (W, H), '#f6f8fb')
native_draw = ImageDraw.Draw(im)


class LogicalDraw:
    """Draw at the native resolution from the common logical layout grid."""
    @staticmethod
    def xy(point):
        return tuple(round(v*SCALE) for v in point)

    def textlength(self, text, **kw):
        return native_draw.textlength(text, **kw)/SCALE

    def textbbox(self, point, text, **kw):
        return tuple(v/SCALE for v in native_draw.textbbox(self.xy(point), text, **kw))

    def text(self, point, text, **kw):
        native_draw.text(self.xy(point), text, **kw)

    def rounded_rectangle(self, box, radius, width, **kw):
        native_draw.rounded_rectangle(self.xy(box), radius=round(radius*SCALE),
                                      width=max(1, round(width*SCALE)), **kw)

    def line(self, points, width, **kw):
        coords = self.xy(points) if isinstance(points[0], (int, float)) else [self.xy(p) for p in points]
        native_draw.line(coords, width=max(1, round(width*SCALE)), **kw)

    def polygon(self, points, **kw):
        native_draw.polygon([self.xy(p) for p in points], **kw)


d = LogicalDraw()
INK, MUTED = '#172b45', '#43546b'
BLUE, TEAL, PURPLE, ORANGE = '#235c95', '#076b6c', '#654093', '#9b591d'


def font(size, bold=False):
    return ImageFont.truetype(str(strong if bold else reg), round(size*SCALE))


def para(text, box, size=38, color=INK, bold=False, gap=10):
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


def panel(box, title, body='', color=BLUE, fill='white', size=38):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=25, fill=fill, outline=color, width=4)
    yy = para(title, (x0+30, y0+18, x1-30, y0+145),
              44, color, True, gap=9)
    d.line((x0+30, yy+10, x1-30, yy+10), fill=color, width=2)
    if body:
        para(body, (x0+30, yy+28, x1-30, y1-28), size, gap=12)
    return yy+28


def arrow(start, end, color=BLUE, width=6, head=22):
    x0, y0 = start
    x1, y1 = end
    d.line((x0, y0, x1, y1), fill=color, width=width)
    theta = math.atan2(y1-y0, x1-x0)
    d.polygon([(x1, y1),
               (x1-head*math.cos(theta)+head*.5*math.sin(theta),
                y1-head*math.sin(theta)-head*.5*math.cos(theta)),
               (x1-head*math.cos(theta)-head*.5*math.sin(theta),
                y1-head*math.sin(theta)+head*.5*math.cos(theta))], fill=color)


para('Projective foundations: charts, signs and finiteness',
     (80, 45, 2920, 135), 64, INK, True)
para('Arbitrary scalar rings through PF7; Noetherian base for PF8–PF9.',
     (80, 145, 2920, 205), 40, MUTED)
para('Nilpotents and finite fields retained. PF1–PF9 are the written proof blocks in §0.C.0.',
     (80, 211, 2920, 265), 35, MUTED)

panel((80, 300, 1470, 900), 'PF1–PF2 | charts and all integer twists',
      'U_i = D_+(X_i) = Spec A[X_j/X_i : j ≠ i].\n'
      '(S localized at x_i) = B_i[t, t⁻¹],  t ↦ x_i.\n'
      'On U_i ∩ U_j invert x_j/x_i; triple overlaps use the same fractions.\n'
      'O(d) has frame e_i = x_i^d for every integer d.\n'
      'e_j = (x_j/x_i)^d e_i; frames multiply under tensor.\n'
      'Homogeneous quotient gives chart quotient rings.\n'
      'Charts, quotients and frames commute with every A → A′.',
      BLUE, '#edf4fd', size=37)

panel((1530, 300, 2920, 900), 'PF4 | Segre retains its defining ideal',
      'P¹_A × P¹_A → P³_A,  Z_kl ↦ X_k Y_l.\n'
      'At Z_00 ≠ 0: a = X_1/X_0, b = Y_1/Y_0.\n'
      'A[z_10,z_01,z_11]/(z_11 − z_10 z_01) ≅ A[a,b].\n'
      'The inverse sends a ↦ z_10 and b ↦ z_01.\n'
      'Frame Z_00 ↦ X_0 ⊗ Y_0 proves σ*O(1) = O(1,1).\n'
      'Over A = k[ε]/(ε²), the point (a,b,ab+ε) has determinant ε ≠ 0: only its residue lies on Segre.\n'
      'General pivot: z_kl = z_kj z_il. See (PF8)–(PF9).',
      TEAL, '#f0fbfa', size=37)

panel((80, 950, 1470, 1600), 'PF3 | empty fibres prove universal closedness',
      'After any scalar change to B, let T = B[X]/J.\n'
      'Each homogeneous T_D is finite over B.\n'
      'At a prime p, empty Proj(T ⊗ κ(p)) means X_i^e_i = 0 for every coordinate; choose each e_i ≥ 1.\n'
      'D = 1 + Σ_i(e_i − 1) gives T_D ⊗ κ(p) = 0.\n'
      'Conversely T_D ⊗ κ(p) = 0 (D > 0) kills all X_i^D.\n'
      'Nakayama and finite generators give b ∉ p with (T_D)_b = 0. Degree-one generation kills all higher components on D(b).\n'
      'Thus the missing-image locus is open after every base change. The explicit closed diagonal supplies separatedness.',
      BLUE, '#edf4fd', size=37)

panel((1530, 950, 2920, 1600), 'PF5–PF6 | which Laurent weights survive?',
      'Weight α ∈ Z^(n+1),  Σ α_i = d.\n'
      'N(α) = { i : α_i < 0 }. Tuple I contributes A X^α exactly when N(α) ⊆ I.\n'
      'N empty: augmented contraction leaves H⁰.\n'
      'N nonempty and proper: signed insertion contracts every degree; see the actual maps below.\n'
      'N full: only degree n survives.\n'
      'For n ≥ 1: H⁰ uses all α_i ≥ 0; Hⁿ uses all α_i < 0; all other degrees vanish. Both bases are finite.\n'
      'Exception n = 0: H⁰(P⁰_A,O(d)) = A X_0^d for ALL integers d; every positive group is zero.',
      PURPLE, '#f7f2fc', size=37)

y = panel((80, 1660, 2920, 2360), 'PF5 and PF10 | explicit differentials and signed homotopies',
          color=PURPLE, fill='#f7f2fc')
para('P²_A, d = −1, α = (−2,1,0), N = {0}, insertion vertex v = 1. Coefficients are over ANY A.',
     (115, y, 2885, y+100), 38)
centres = [370, 1500, 2630]
for cx, title, basis in zip(centres, ['C⁰ = A', 'C¹ = A²', 'C² = A'],
                           ['tuple 0', 'tuples 01, 02', 'tuple 012']):
    d.rounded_rectangle((cx-225, 1840, cx+225, 1980), radius=15,
                        fill='white', outline=PURPLE, width=3)
    para(title, (cx-200, 1853, cx+200, 1910), 44, PURPLE, True)
    para(basis, (cx-200, 1920, cx+200, 1975), 33)
arrow((610, 1880), (1250, 1880), PURPLE)
arrow((1750, 1880), (2390, 1880), PURPLE)
para('δ⁰(a) = (−a,−a)', (650, 1910, 1230, 1980), 39, PURPLE)
para('δ¹(b_01,b_02) = b_01 − b_02', (1775, 1910, 2370, 2030), 36, PURPLE)
arrow((1250, 2070), (610, 2070), TEAL)
arrow((2390, 2070), (1750, 2070), TEAL)
para('h¹(b_01,b_02) = −b_01', (630, 2100, 1250, 2205), 36, TEAL)
para('h²(c) = (0,−c)', (1800, 2100, 2360, 2205), 39, TEAL)
para('Degree 1: δ⁰h¹(b) + h²δ¹(b) = (b_01,b_01) + (0,b_02 − b_01) = b.  Degrees 0 and 2 also give identity.',
     (115, 2240, 2885, 2330), 37)

panel((80, 2420, 1470, 3190), 'PF7 | denominator clearing is only the first step',
      'Quasi-coherent F; local s ∈ Γ(W_i,F). On W_j put t_ij = X_i/X_j.\n'
      'Choose common N and a_j representing t_ij^N s on W_i ∩ W_j.\n'
      'On W_j ∩ W_k put u = X_k/X_j.\n'
      'Δ_jk = a_j − u^N a_k vanishes only after localizing at t_ij.\n'
      'Choose common K killing all Δ_jk in their actual overlap modules.\n'
      'a′_j = t_ij^K a_j; new twist is N+K.\n'
      'a′_j − u^(N+K) a′_k = t_ij^K Δ_jk = 0.\n'
      'Now glue. For finite-type F, repeating for finite chart generators yields ⊕ O(−a_λ) ↠ F.\n'
      'High twists are generated by the images of coordinate monomials. No equality is inferred merely on a dense open.',
      ORANGE, '#fff7ee', size=38)

panel((1530, 2420, 2920, 3190), 'PF8 | simultaneous induction for coherent F',
      'Noetherian A; n+1 affine charts give H^q(G) = 0 for q > n for every quasi-coherent G.\n'
      'Let E = ⊕ O(−a_λ) ↠ F and K = kernel. The kernel is coherent by AS7 and N1.\n'
      '0 → K(d) → E(d) → F(d) → 0 gives\n'
      'H^q(E(d)) → H^q(F(d)) → H^(q+1)(K(d)).\n'
      'LEFT: the finite twist bases above.\n'
      'RIGHT: the simultaneous induction hypothesis.\n'
      'The exact sequence is 0 → I → H^q(F(d)) → J → 0, with I a finite quotient of the left and J a finite submodule of the right.\n'
      'For q > 0, large d kills both outer terms.\n'
      'A new coherent kernel is allowed at each step. No finite resolution or base-dimension bound is assumed.',
      BLUE, '#edf4fd', size=38)

panel((80, 3250, 2920, 3910), 'PF9 | relative images and the same hyperplane bundle',
      'Closed immersion j : Y → Pⁿ_Z, with Z locally Noetherian; coherent F on Y, π : Y → Z and L = j*O(1).\n'
      'On V = Spec A ⊆ Z, PF8 proves that H^q(π⁻¹V,F) is a finite A-module.\n'
      'SC14 identifies its associated sheaf with (R^qπ_*F)|_V; AS7 makes it coherent.\n'
      'If Z is quasi-compact, a finite affine cover gives a single d_0 with R^qπ_*(F ⊗ L^d) = 0 for d ≥ d_0 and q > 0.\n'
      'For maps f : Y → X and h : Y → P^N_A, the graph map (f,h) : Y → P^N_X pulls back each coordinate frame to the same section as h. Hence h*O(1) ≅ (f,h)*O(1).\n'
      'SC15 supplies the separate vanishing-image collapse used later in the proper-coherence argument.\n'
      'Arbitrary scalar change of TWIST cohomology was proved above. Arbitrary coherent-cohomology base change requires its own proof.',
      TEAL, '#f0fbfa', size=39)

para('Proof locators: §0.C.0.1–0.C.0.10; equations (PF1)–(PF22); Exercises 6.18–6.19.',
     (80, 3960, 2920, 4020), 36, MUTED)
para('Free primary comparisons: Stacks 01M3 / 01NH / 01WD / 01XT / 01PW / 01YS. Full local proofs accompany the figure.',
     (80, 4030, 2920, 4140), 36, MUTED)

im.save(OUT)
print(str(OUT.resolve()))
