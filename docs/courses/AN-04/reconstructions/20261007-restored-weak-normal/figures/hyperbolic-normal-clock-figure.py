"""Original schematic for HN5/HN7/HN43/HN44; not a numerical trajectory."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import matplotlib

OUT = Path(__file__).resolve().parent
W, H = 1560, 970
im = Image.new("RGB", (W, H), "#ffffff")
d = ImageDraw.Draw(im)
font_path = Path(matplotlib.get_data_path()) / "fonts/ttf/DejaVuSans.ttf"
bold_path = Path(matplotlib.get_data_path()) / "fonts/ttf/DejaVuSans-Bold.ttf"
font = lambda size, bold=False: ImageFont.truetype(str(bold_path if bold else font_path), size)
ink, blue, orange, light = "#16324f", "#145ea8", "#bd5b19", "#e8f1fa"

def text(x, y, value, size=29, fill=ink, bold=False):
    d.text((x, y), value, font=font(size, bold), fill=fill)

def arrow(a, b, color, width=5):
    d.line([a, b], fill=color, width=width)
    theta = math.atan2(b[1]-a[1], b[0]-a[0])
    points = [b, (b[0]-19*math.cos(theta-.5), b[1]-19*math.sin(theta-.5)),
                 (b[0]-19*math.cos(theta+.5), b[1]-19*math.sin(theta+.5))]
    d.polygon(points, fill=color)

text(55, 28, "Weak hyperbolic reflection: the normal clock", 42, bold=True)
text(55, 88, "Smooth face; scalar wave principal symbol; arbitrary complex matrix lower form", 26)
d.rounded_rectangle((55, 150, 1505, 540), 18, fill=light)
face_y = 342
d.line((85, face_y, 1470, face_y), fill=ink, width=5)
text(85, 359, "x = 0", 29, bold=True)
text(89, 238, "Interior x > 0", 27)
text(579, 384, "Compression identifies", 29, bold=True)
text(579, 425, "the two boundary lifts", 29)
arrow((270, 223), (743, 342), blue)
arrow((768, 342), (1280, 223), orange)
d.ellipse((741, 330, 768, 357), fill=ink)
text(350, 171, "Incoming", 31, blue, True)
text(95, 280, "ξ+ > 0 ; η < 0", 28, blue)
text(990, 171, "Outgoing", 31, orange, True)
text(1180, 281, "ξ− < 0 ; η > 0", 28, orange)
text(306, 463, "ξ± = ± √[(τ² − ζᵀ B_b ζ) / a_b]", 31, bold=True)
text(928, 463, "H_p x = −2 a_b ξ±", 29)

text(65, 580, "Exact clock and positive boundary derivative", 28, bold=True)
text(65, 628, "σ = x ξ ;  λ = |τ| ;  η = −σ / λ", 32)
text(65, 678, "λ⁻¹ H_p η = 2 d_b > 0 at both lifts", 32, blue, True)
text(65, 726, "d_b = 1 − |τ|⁻² ζᵀ B_b ζ ≥ c₀ > 0", 29)

d.rounded_rectangle((860, 580, 1497, 865), 15, outline=ink, width=3)
text(887, 600, "Target energy index s", 31, bold=True)
for y, row in zip((650, 692, 734, 776, 818), (
    "Commutant A : order s + 1/2",
    "Positive L2 output B : order s + 1",
    "Lower solution : energy s − 1/2",
    "Incoming solution : energy s",
    "Forcing : natural-dual index s + 1",
)):
    text(887, y, row, 26)
text(65, 824, "One shared positive-cutoff neighborhood", 28, bold=True)
text(65, 866, "crosses η = 0 and persists at every order.", 27)
text(65, 927, "Schematic branches, not a computed Hamilton trajectory. Exact equations: HN5, HN7, HN43–HN44.", 22)
im.save(OUT / "hyperbolic-normal-clock.png")
print(str(OUT / "hyperbolic-normal-clock.png"))
