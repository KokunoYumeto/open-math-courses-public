"""Reproducible diagram for NP8, NP19, NP23, and NP29.

The full proofs are in U048_NORMAL_PRODUCT_DERIVATION_261.md.
This diagram records actual map types and coefficients, without a spectral model.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parent
im = Image.new('RGB', (1700, 1160), '#f7f8fa')
draw = ImageDraw.Draw(im)
font_path = 'C:/Windows/Fonts/cambria.ttc'
def font(size):
    return ImageFont.truetype(font_path, size)
def label(x, y, text, size=32, color='#152438'):
    draw.text((x, y), text, font=font(size), fill=color)
def box(x, y, width, height, title, lines):
    draw.rounded_rectangle((x, y, x+width, y+height), radius=14,
                           fill='white', outline='#456c8b', width=3)
    label(x+24, y+18, title, 35)
    for i, line in enumerate(lines):
        label(x+24, y+76+i*44, line, 29)

label(48, 26, 'The actual finite collar product retains both error bundles', 42)
label(48, 82, 'Original P_c : E_Y → F_Y; original M : E_Y → F_Y remains invertible.', 30)
box(48, 145, 784, 210, 'NP8–NP16: the complete finite product', [
    'D = Q R_F = R_E Q : F_Y → E_Y',
    'Normal degree −m−1; complete tangential coefficients D_n.',
    'Separated normal remainder: |κ|^(−m−1−L−v).'])
box(868, 145, 784, 210, 'NP17–NP20: the corrected operator', [
    'Q_2 = Q − D : F_Y → E_Y',
    'P_c Q_2 = I_F − R_F² : F_Y → F_Y',
    'Q_2 P_c = I_E − R_E² : E_Y → E_Y'])
box(48, 397, 1604, 176, 'NP9: every coefficient keeps its ordered factors and normal derivatives', [
    'D_n = Σ_(h+k+ℓ=n) binom(−m−h, ℓ) Q_h δ^ℓ F_(k+1),    δ = −i∂_r',
    'Q_h : F_Y → E_Y;  F_(k+1) : F_Y → F_Y;  tangential order(D_n) ≤ n'])
box(48, 616, 1604, 176, 'NP23: the third coefficient records the first finite inverse defect', [
    'H_0 = C_0 = M⁻¹;    H_1 = C_1;    H_2 = C_2 − M⁻¹ F_1² = C_2 − E_1² M⁻¹',
    'C_n are the constructed full formal inverse coefficients; Q_2 is the actual finite operator.'])
box(48, 834, 1604, 220, 'NP26–NP29: the original boundary source and all measurement orders', [
    'W = Q_2 R_F² = R_E² Q_2 : F_Y → E_Y,    normal degree −m−2',
    'Every source derivative q remains:  r⁺ W C_P^[q] U ∈ H̄_(ν, σ+q+2−ν),    every real ν.',
    'Every original boundary row remains:  B_j r⁺ W C_P^[q] U ∈ H^(σ+q+2−m_j−1/2)(Y; G_j).'])
label(48, 1085, 'Exact proofs: NP1–NP29.', 26)
label(48, 1125, 'The diagram does not assign point values to boundary distributions or remove any finite error.', 25)
im.save(root / 'normal_product_261.png')
print(root / 'normal_product_261.png')
