"""Reproduce the proof diagram without changing the original parameter."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
S=2
W,H=1480,1380
img=Image.new('RGB',(W*S,H*S),'#f7f9fc')
d=ImageDraw.Draw(img)
font_root=Path('C:/Windows/Fonts')
def font(size,bold=False):
    return ImageFont.truetype(str(font_root/('segoeuib.ttf' if bold else 'segoeui.ttf')),size*S)
def text(x,y,content,size=26,bold=False,color='#172b4d'):
    d.text((x*S,y*S),content,font=font(size,bold),fill=color)
def box(x,y,w,h,title,lines,color='#ffffff'):
    d.rounded_rectangle((x*S,y*S,(x+w)*S,(y+h)*S),radius=18*S,fill=color,outline='#a8b7cc',width=2*S)
    title_size=28
    while d.textlength(title,font=font(title_size,True))>(w-48)*S:
        title_size-=1
    assert title_size>=23
    text(x+24,y+18,title,title_size,True)
    yy=y+65
    for line in lines:
        line_size=25
        while d.textlength(line,font=font(line_size))>(w-48)*S:
            line_size-=1
        assert line_size>=21
        text(x+24,yy,line,line_size)
        yy+=40
def arrow(x,y,xx,yy):
    d.line((x*S,y*S,xx*S,yy*S),fill='#4176a4',width=4*S)
    if y!=yy:
        d.polygon([(xx*S,yy*S),((xx-9)*S,(yy-15)*S),((xx+9)*S,(yy-15)*S)],fill='#4176a4')

text(54,28,'Original finite logarithmic envelopes',42,True)
text(54,85,'λ = 1 + 2⁻³¹ 25⁻¹⁹⁸¹⁵³     d = (4 + λ)(4 + λ⁻¹)',28)
text(54,128,'Full H action, original five likelihoods, both normal phases and canonical traces',25)
box(54,180,1372,186,'Actual finite parity-balanced average — FM21.10a–d',[
    'φ = ξ ĀL, for every original center seed ξ, normal or singular',
    'φ β₁ = φ exactly;     φ(Q) ≤ d + e;     e = 3(d − 1)/(2L + 1)',
    'Central integer/parity retained; βz² = id on the center; physical χ(z²) = λ²'])
arrow(410,366,410,405)
arrow(1067,366,1067,405)
box(54,414,676,154,'Exact lamp logarithm — FL22.5,9',[
    'φ(log R₁) − φ(log R₀) = log λ',
    'Full bounded RN cocycle; no spatial invariance assumed'])
box(754,414,672,154,'Reciprocal and probability budgets — FL22.10',[
    'A = 1 + λ + Σ exp(ℓⱼ);   B = 1 + λ⁻¹ + Σ exp(−ℓⱼ)',
    'exp(c) A ≤ 1;   exp(−c) B ≤ d + e;   AB ≤ d + e'])
arrow(410,568,410,607)
arrow(1067,568,1067,607)
box(54,616,676,190,'Mean enclosure — FL22.4–5,11',[
    's = (ℓ₁ + ℓ₂ + ℓ₃)/3;   α = e/[3(1 + λ⁻¹)]',
    'z± = [1 + λ + α ± √((1 + λ + α)² − 4λ)]/2',
    'log z₋ ≤ s ≤ log z₊;   z₋ < 1 < λ < z₊ for e > 0'])
box(754,616,672,190,'Full spatial differences — FL22.6,12',[
    '3 Σ(ℓⱼ − s)² ≤ e + 3(1 + λ⁻¹)(z − 1)(λ − z)/z',
    'Σ(ℓⱼ − s)² ≤ e/3 + (1 + λ⁻¹)(√λ − 1)²',
    'Original bounded full log Dt₁, log Dt₂, log Dt₃'])
arrow(410,806,410,845)
arrow(1067,806,1067,845)
box(54,854,1372,154,'Each original spatial mean — FL22.7–8',[
    'D = d + e;   a = 1 + λ;   b = 1 + λ⁻¹;   T = D − 4√D + 3 − ab',
    'x± = [T ± √(T² − 4ab)]/(2b);   log x₋ ≤ ℓⱼ ≤ log x₊   (j = 1, 2, 3)'])
arrow(740,1008,740,1047)
box(54,1056,1372,194,'Invariant cluster and the remaining original selection gap',[
    'As L → ∞:  0 ≤ ℓ₁ + ℓ₂ + ℓ₃ ≤ 3 log λ',
    'These necessary envelopes allow both symmetric endpoint tuples.',
    'They do not establish max ω(R₁) = λ/(4 + λ) or a strict upper separation.'], '#fff7e9')
text(54,1262,'Proof: General tail supports and controlled tunnels, FL22.4–12. Areas are schematic.',22)
text(54,1297,'Fixed normal count depth precedes a potentially singular Følner limit (OM.15–21).',22)
text(54,1332,'Human context: Avraham-Re’em–Björklund (2026), compact RN models; no endpoint theorem imported.',21)
img.save(ROOT/'finite-logarithmic-envelope-v22.png')
print('FL22_FIGURE_CREATED exact_formulas=true schematic=true')
