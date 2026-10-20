"""Reproduce the Section 0.B proof map with explicit AS10/AS13 hypotheses.
Write only the PNG in the course assets directory.
Requires Python 3 and Pillow. Labels use ASCII mathematical notation to avoid
font-dependent substitution. Exact proofs and conventional TeX are in the
accompanying section. eps denotes epsilon, QC means quasi-coherent.
"""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 3300, 3700
OUT = Path(__file__).resolve().parents[1] / 'assets/affine-sheaf-proof-map.png'
FONT_DIR = Path('.')
REGULAR = FONT_DIR / "segoeui.ttf"
BOLD = FONT_DIR / "segoeuib.ttf"
im = Image.new("RGB", (WIDTH, HEIGHT), "#f7f8fb")
d = ImageDraw.Draw(im)
INK, MUTED, BLUE = "#172b45", "#41546b", "#235c95"
TEAL, PURPLE, ORANGE = "#076b6c", "#654093", "#9b591d"

def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else REGULAR), size)

def lines_for(text, f, width):
    """Wrap at words; assert every line has its actual measured width."""
    result = []
    for para in text.split("\n"):
        current = ""
        for word in para.split():
            candidate = (current + " " + word).strip()
            if current and d.textlength(candidate, font=f) > width:
                result.append(current)
                current = word
            else:
                current = candidate
        result.append(current)
    for line in result:
        assert d.textlength(line, font=f) <= width, (line, width)
    return result

def paragraph(text, box, size=35, color=INK, bold=False, gap=10):
    x0, y0, x1, y1 = box
    f = font(size, bold)
    yy = y0
    step = size + gap
    for line in lines_for(text, f, x1-x0):
        assert yy + size + 8 <= y1, (text, box, yy)
        d.text((x0, yy), line, fill=color, font=f)
        yy += step
    return yy

def panel(box, title, body, color=BLUE, fill="#ffffff",
          title_size=38, body_size=35):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=28, fill=fill, outline=color, width=4)
    yy = paragraph(title, (x0+28, y0+20, x1-28, y0+120),
                   title_size, color, True, gap=6)
    d.line((x0+28, yy+9, x1-28, yy+9), fill=color, width=2)
    paragraph(body, (x0+28, yy+27, x1-28, y1-18),
              body_size, INK, gap=9)

def arrow(start, end, color=BLUE, width=7, head=22):
    x0, y0 = start
    x1, y1 = end
    d.line((x0,y0,x1,y1), fill=color, width=width)
    theta = math.atan2(y1-y0, x1-x0)
    p1=(x1-head*math.cos(theta)+head*.55*math.sin(theta),
        y1-head*math.sin(theta)-head*.55*math.cos(theta))
    p2=(x1-head*math.cos(theta)-head*.55*math.sin(theta),
        y1-head*math.sin(theta)+head*.55*math.cos(theta))
    d.polygon([(x1,y1), p1, p2], fill=color)

def centered(text, box, size=32, color=MUTED, bold=False):
    x0,y0,x1,y1=box
    f=font(size,bold)
    assert d.textlength(text,font=f) <= x1-x0, (text, box)
    xx=(x0+x1-d.textlength(text,font=f))/2
    d.text((xx,y0),text,fill=color,font=f)
    assert y0+size+8 <= y1

paragraph("Affine modules, sheaves and finite denominators",
          (90,55,3210,145),64,INK,True)
paragraph("Section 0.B: arbitrary rings and nilpotents; Noetherianity only where stated",
          (90,155,3210,215),37,MUTED)

panel((90,260,1050,600), "0.B.1-0.B.2 | AS1-AS3",
      "Germs give exact sheaf operations.\n"
      "A finite principal cover gives the unit-ideal gluing formula AS1.\n"
      "M becomes the sheaf with sections M_a on D(a) (AS2).")
panel((1170,260,2130,600), "0.B.3 | AS4-AS5",
      "Clear chart denominators, then kill overlap differences.\n"
      "Recover M = Gamma(X,F).\n"
      "Modules and QC sheaves on Spec(A) are equivalent; both functors are exact.")
panel((2250,260,3210,600), "0.B.4 | AS6-AS7",
      "Kernels, quotients, tensors and ambient extensions stay QC.\n"
      "If the ring is Noetherian, finite modules and their submodules give coherent sheaves.")
arrow((1055,430),(1160,430))
arrow((2135,430),(2240,430))

panel((90,720,1570,1140), "0.B.5 | AS8: the module M is finite",
      "For Ann(M), use finitely many module generators.\n"
      "One product of denominator multipliers kills a times every generator.\n"
      "(Ann_A M)_S = Ann_(A_S)(M_S).\n"
      "This bound need not exist for an infinite module.",
      TEAL, "#f0fbfa", body_size=36)
panel((1730,720,3210,1140), "0.B.5 | AS9: the ideal J is finite",
      "For M[J], the module M may be arbitrary.\n"
      "Use finitely many ideal generators to obtain one killing multiplier.\n"
      "(M[J])_S = M_S[J_S].\n"
      "This is a different finite list from AS8.",
      PURPLE, "#f7f2fc", body_size=36)

d.rounded_rectangle((90,1260,3210,1770), radius=28,
                    fill="#edf4fd", outline=BLUE, width=4)
paragraph("0.B.6 | AS10: qcqs localization is proved before QC direct image",
          (120,1282,3180,1350),41,BLUE,True)
paragraph("X qcqs; F quasi-coherent; s in Gamma(X,O_X).",
          (125,1340,3175,1388),30,BLUE)
panel((125,1390,1000,1650), "1. Finite affine charts",
      "Choose U_i covering X.\n"
      "One exponent a extends a section from every U_i intersect X_s.",
      BLUE, title_size=34, body_size=33)
panel((1140,1390,2070,1650), "2. Finite overlap charts",
      "Cover every U_i intersect U_j by finitely many W_ijk.\n"
      "One exponent b kills every overlap difference.",
      BLUE, title_size=34, body_size=33)
panel((2210,1390,3175,1650), "3. Localize the equalizer",
      "Use finite products of chart and overlap sections (formula AS8).\n"
      "Exact localization identifies its kernel with Gamma(X_s,F).",
      BLUE, title_size=34, body_size=33)
arrow((1005,1520),(1128,1520))
arrow((2075,1520),(2198,1520))
centered("The corrected sections s^b u_i glue; dividing by s^(a+b) gives the original section.",
         (120,1695,3180,1755),35,BLUE)

arrow((570,1775),(570,1885))
paragraph("AS10 supplies\nlocalization",
          (610,1790,1030,1890),31,BLUE,gap=7)
panel((90,1900,1060,2270), "0.B.7 | AS11: QC direct image",
      "For qcqs f, take Z=f^-1(Spec(A)).\n"
      "M=Gamma(Z,F); on D(a), sections are M_a by AS10.\n"
      "Thus f_*F is QC. A qc separated map satisfies these hypotheses.",
      BLUE, body_size=34)
panel((1180,1900,2120,2270), "0.B.7 | AS12: separate zero test",
      "For qc f, its schematic ideal is ker(A -> product B_i).\n"
      "Finite source charts suffice; no overlap equalizer or quasi-separatedness is needed.",
      TEAL, body_size=34)
panel((2240,1900,3210,2270), "0.B.8 | AS13: extend finite data",
      "X qcqs; U quasi-compact open; F QC.\n"
      "Use AS11 and AS6 to form the kernel/graph on X.\n"
      "Choose finite numerator generators on the open, then glue across finitely many charts.",
      PURPLE, body_size=34)

d.rounded_rectangle((90,2380,3210,3540), radius=28,
                    fill="#fff9f0", outline=ORANGE, width=4)
paragraph("0.B.9 | AS14: the quotient/localization square, with nilpotents retained",
          (120,2400,3180,2480),40,ORANGE,True)
paragraph("k is a field; eps denotes epsilon. Division makes k[t] a PID; A is free of rank two over k[t].",
          (135,2490,3170,2550),32,INK)
paragraph("AS7 then makes every A-ideal finite: A is Noetherian.",
          (135,2545,3170,2600),32,INK)

panel((180,2660,1270,2820), "Ring A = k[eps,t]/(eps^2)",
      "J = (eps); eps is nonzero.", ORANGE,
      title_size=35, body_size=32)
panel((2030,2660,3120,2820), "Ring A_t = k[t,t^-1][eps]/(eps^2)",
      "The nilpotent eps is still nonzero.", ORANGE,
      title_size=33, body_size=32)
arrow((1280,2740),(2015,2740),ORANGE)
centered("localize at t: injective",
         (1300,2672,1995,2730),31,ORANGE,True)
panel((180,3020,1270,3180), "Module M = A/J = k[t]",
      "Ann_A(M) = J.", ORANGE, title_size=35, body_size=32)
panel((2030,3020,3120,3180), "Module M_t = k[t,t^-1]",
      "M_t = A_t/J_t.", ORANGE, title_size=35, body_size=32)
arrow((1280,3100),(2015,3100),ORANGE)
centered("localize at t",
         (1300,3032,1995,3090),31,ORANGE,True)
arrow((725,2830),(725,3005),ORANGE)
paragraph("quotient by J", (755,2880,1260,2940),31,ORANGE,True)
arrow((2575,2830),(2575,3005),ORANGE)
paragraph("quotient by J_t", (2605,2880,3110,2940),31,ORANGE,True)

paragraph("The square commutes. Since ker(A -> A_t)=0, the schematic closure of D(t) is the full X (AS12).",
          (135,3210,3170,3270),32,INK)
paragraph("Dotted vertical arrows apply the associated-sheaf functor (AS3, AS5, AS6):",
          (135,3265,3170,3320),31,INK)
sequence = "0 -> J~ -> O_X -> M~ = i_*O_Z -> 0"
sf = font(37, True)
base_x = (WIDTH - d.textlength(sequence, font=sf))/2
o_x = base_x + d.textlength("0 -> J~ -> ",font=sf) + d.textlength("O_X",font=sf)/2
m_x = base_x + d.textlength("0 -> J~ -> O_X -> ",font=sf) + d.textlength("M~",font=sf)/2
centered("A", (o_x-60,3335,o_x+60,3400),35,ORANGE,True)
centered("M", (m_x-60,3335,m_x+60,3400),35,ORANGE,True)
for xx in (o_x,m_x):
    for yy in range(3380,3420,12):
        d.line((xx,yy,xx,min(yy+6,3418)),fill=ORANGE,width=4)
    arrow((xx,3418),(xx,3427),ORANGE,width=4,head=10)
centered(sequence, (135,3435,3170,3495),37,ORANGE,True)

paragraph("Free human source: the Stacks project authors, Tags 01HV, 01IB, 01P7, 01LC, 01PO.",
          (90,3590,3210,3650),30,MUTED)
paragraph("Full local proofs: Sections 0.B.1-0.B.10, AS1-AS14; exercises 6.10 and 6.11.",
          (90,3640,3210,3695),30,MUTED)
# The final native raster stays below ten million pixels, so the whole
# image can be inspected at original detail without display downscaling.
FINAL_WIDTH, FINAL_HEIGHT = 2960, 3319
im = im.resize((FINAL_WIDTH, FINAL_HEIGHT), Image.Resampling.LANCZOS)
im.save(OUT, format="PNG", optimize=True)
print(f"{OUT.name}: {FINAL_WIDTH} x {FINAL_HEIGHT}; RGB; saved")

