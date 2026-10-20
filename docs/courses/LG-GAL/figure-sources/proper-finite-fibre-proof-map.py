"""Render the Noetherian proper finite-fibre proof map.

Run this file with Python and Pillow. It writes only the PNG next to the source.
The diagram's arrows record proof dependencies, not a cohomology base-change
isomorphism at finite level. Proof locators refer to Section 0.F and its NF tags.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

def installed_font_path(filename):
    try:
        return Path(ImageFont.truetype(filename,12).path)
    except OSError:
        return Path(filename)


WIDTH, HEIGHT = 3200, 2780
BG = "#fbfcfe"
INK = "#132d45"
MUTED = "#3e5970"
EDGE = "#557188"
FONT_CANDIDATES = [
    (installed_font_path('segoeui.ttf'), installed_font_path('segoeuib.ttf')),
    (Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
     Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")),
]
for regular, bold in FONT_CANDIDATES:
    if regular.is_file() and bold.is_file():
        break
else:
    raise RuntimeError("A listed regular/bold Unicode font pair is required.")
image = Image.new("RGB", (WIDTH, HEIGHT), BG)
draw = ImageDraw.Draw(image)
fonts = {(size, weight): ImageFont.truetype(str(bold if weight else regular), size)
         for size in (30, 32, 34, 36, 38, 42, 46, 54, 76) for weight in (False, True)}
boxes = []

def wrap(text, font, width):
    lines = []
    for paragraph in text.split("\n"):
        line = ""
        for word in paragraph.split():
            candidate = word if not line else line + " " + word
            if draw.textlength(candidate, font=font) <= width:
                line = candidate
            else:
                if not line:
                    raise ValueError("Unbreakable label exceeds box width: " + word)
                lines.append(line)
                line = word
        lines.append(line)
    return lines

def put(text, x, y, font, fill=INK):
    draw.text((x, y), text, font=font, fill=fill)

def panel(rect, title, body, fill, title_size=42, body_size=38):
    x0, y0, x1, y1 = rect
    pad = 24
    draw.rounded_rectangle(rect, radius=24, fill=fill, outline="#aac0d1", width=3)
    title_font, body_font = fonts[(title_size, True)], fonts[(body_size, False)]
    title_lines = wrap(title, title_font, x1-x0-2*pad)
    body_lines = wrap(body, body_font, x1-x0-2*pad)
    title_pitch, body_pitch = title_size+12, body_size+11
    required = 2*pad + len(title_lines)*title_pitch + 15 + len(body_lines)*body_pitch
    if required > y1-y0:
        raise ValueError(f"Panel is too short by {required-(y1-y0)} pixels: {title}")
    y = y0 + pad
    for line in title_lines:
        put(line, x0+pad, y, title_font)
        y += title_pitch
    y += 15
    for line in body_lines:
        put(line, x0+pad, y, body_font, MUTED)
        y += body_pitch
    boxes.append((title, rect, required))

def arrow(points, width=6):
    draw.line(points, fill=EDGE, width=width, joint="curve")
    (ax, ay), (bx, by) = points[-2], points[-1]
    angle = math.atan2(by-ay, bx-ax)
    size = 21
    wings = [(bx-size*math.cos(angle-d), by-size*math.sin(angle-d))
             for d in (0.5, -0.5)]
    draw.polygon([(bx, by), *wings], fill=EDGE)

put("Proper finite fibres implies finite", 160, 55, fonts[(76, True)])
put("A proof over locally Noetherian bases, with nilpotents retained", 165, 160,
    fonts[(42, False)], MUTED)
panel((330, 245, 2870, 475), "Hypotheses [Theorem 0.F.1]",
      "f: X → S is proper; every geometric fibre has finitely many points.\n"
      "Work on a Noetherian affine base S = Spec A; F is any coherent sheaf.",
      "#eaf1f8", 46, 38)

panel((140, 550, 1490, 830), "Coherent finiteness [0.C.10–11; 0.F.2]",
      "M^q = H^q(X,F) is a finite A-module.\n"
      "Graded Rees cohomology Q^q is finite (NF3).",
      "#e8f1fc", 42, 38)
panel((1710, 550, 3060, 830), "Infinitesimal fibres [0.F.2]",
      "At s, X_r = X ×_S Spec(O_S,s / m_s^r).\n"
      "Its topology equals the finite discrete topology of X_s.\n"
      "All nilpotent stalk rings are kept.",
      "#e8f6f0", 42, 36)

panel((140, 870, 1490, 1145), "Formal functions [0.F.2; NF2–NF7]",
      "Kernel transitions are pro-zero (NF5).\n"
      "Image and I-adic filtrations are cofinal.\n"
      "Completed stalk = lim_r H^q(X_r,F_r).",
      "#e8f1fc", 42, 38)
panel((1710, 870, 3060, 1145), "Finite-topology cohomology [0.F.2; NF8]",
      "Global sections is an exact finite product.\n"
      "H^q(X_r,F_r) = 0 for q > 0.\n"
      "Reducedness and flatness are not hypotheses.",
      "#e8f6f0", 42, 38)

panel((620, 1250, 2580, 1520), "Zero completion implies Nakayama [0.F.2; NF9]",
      "Surjective quotient transitions lift every residue class.\n"
      "For a finite stalk M: completed M = 0 implies M / mM = 0 implies M = 0.\n"
      "Thus R^q f_*F = 0 for all coherent F and q > 0.",
      "#f0ecfb", 42, 36)
panel((620, 1600, 2580, 1870), "Ideal vanishing implies affineness [0.F.3; NF10–NF12]",
      "H^1(X,J) = 0 for every coherent ideal J.\n"
      "Lift affine principal neighborhoods, then a global relation Σ b_j a_j = 1.\n"
      "Localization glues X = Spec Γ(X,O_X).",
      "#fff3df", 42, 36)
panel((620, 1950, 2580, 2120), "Degree-zero coherence implies finiteness [0.F.3]",
      "Γ(X,O_X) is finite over A. Therefore f is finite.",
      "#e4f1f0", 42, 38)

arrow([(815,475),(815,550)])
arrow([(2385,475),(2385,550)])
arrow([(815,830),(815,870)])
arrow([(2385,830),(2385,870)])
arrow([(815,1145),(815,1195),(1180,1195),(1180,1250)])
arrow([(2385,1145),(2385,1195),(2020,1195),(2020,1250)])
arrow([(1600,1520),(1600,1600)])
arrow([(1600,1870),(1600,1950)])

put("Applications add smooth lifting, geometric fibre data and actual group identities",
    160, 2160, fonts[(34, False)], MUTED)
draw.line([(445,2235),(2755,2235)], fill=EDGE, width=6)
draw.line([(1600,2120),(1600,2235)], fill=EDGE, width=6)
for center in (445,1215,1985,2755):
    arrow([(center,2235),(center,2280)])

panel((100,2280,790,2570), "Proper étale [0.F.3]",
      "Finite étale and locally free.\n"
      "Arbitrary later base change\n"
      "keeps finiteness, étaleness\n"
      "and rank.",
      "#eaf1f8", 32, 32)
panel((870,2280,1560,2570), "Multiplication [0.F.5]",
      "Q-base; n ≠ 0.\n"
      "[n] and E[n] have rank n².\n"
      "Correct square-zero lifts\n"
      "by the inverse differential.",
      "#eaf1f8", 32, 32)
panel((1640,2280,2330,2570), "Embeddings [0.F.4]",
      "Fibre embeddings give finite D;\n"
      "D tensor κ(s) = 0 implies D = 0.\n"
      "Rank-one étale divisor:\n"
      "the graph of a section.",
      "#eaf1f8", 32, 32)
panel((2410,2280,3100,2570), "Dual degree [0.F.5]",
      "Q-base; q̂ q = [N], deg q = N > 0.\n"
      "q̂ finite étale; deg q̂ = N.\n"
      "A torsion marking satisfies\n"
      "[N]P = O on the entire base.",
      "#eaf1f8", 32, 32)

panel((140,2620,3060,2770), "Excluded n = 0",
      "For a nonempty base, [0] has the whole one-dimensional geometric elliptic fibre over O; it is not finite.",
      "#fff0e8", 32, 32)

target = Path(__file__).resolve().parents[1] / 'assets/proper-finite-fibre-proof-map.png'
image.save(target, format="PNG", optimize=False)
print(f"Rendered {WIDTH} × {HEIGHT} PNG to {target.name}.")
print(f"All {len(boxes)} mathematical panels passed measured text-fit checks.")

