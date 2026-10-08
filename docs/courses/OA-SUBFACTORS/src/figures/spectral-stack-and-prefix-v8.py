"""Reproduce Figure V8.1; independent CC0-1.0 operator-coordinate diagram."""
from pathlib import Path
from html import escape

W,H=1460,1090
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
       '<title id="title">An actual spectral stack with prefix and test preservation</title>',
       '<desc id="desc">The finite Jones density gives a right-coordinate projection. A coordinate trace scales by n; the old algebra scales by n squared. A fixed prefix and an approximately preserved common basis retain the physical tests. Small joint defect remains a separate input.</desc>',
       '<rect width="100%" height="100%" fill="#f5f7fb"/>',
       '<style>text{font-family:Arial,"DejaVu Sans",sans-serif;fill:#172236}.title{font-size:31px;font-weight:700}.head{font-size:23px;font-weight:700}.line{font-size:20px}.small{font-size:18px}</style>']

def text(x,y,label,cls='line'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(label)}</text>')

def card(x,y,w,h,title,lines,color='#e5efff',stroke='#3266a1'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="{stroke}" stroke-width="2"/>')
    text(x+18,y+35,title,'head')
    for i,line in enumerate(lines):text(x+18,y+74+32*i,line)

def arrow(x1,x2,y):
    parts.append(f'<path d="M{x1},{y} H{x2}" stroke="#3266a1" stroke-width="4"/>')
    parts.append(f'<path d="M{x2},{y} l-10,-7 v14 z" fill="#3266a1"/>')

text(30,46,'One realized projection; both canonical traces','title')
text(30,80,'Same physical inclusion N ⊂ M.  Proofs: FC.3–FC.24 and V8.1–V8.33.','small')
card(30,112,430,250,'Finite Jones columns',[
    'h = Σ aᵢ e aᵢ*,   Σ aᵢ aᵢ* = 1',
    '0 ≤ h ≤ 1,   Tr(h) = 1',
    'ψₕ|M = τ;   ψₕ E_A = ψₕ',
    'q = supp(h),   1 ≤ Tr(q) ≤ L',
    'L is finite for this density.'
])
card(515,112,430,250,'Actual matrix complement',[
    'D ≅ Mₙ ⊂ Tₖ ⊂ S ∩ Nₖ',
    'New core: S⁰ = D′∩S ⊂ R⁰ = D′∩R',
    'Ã = A⁰ ⊗ B(L²(D))',
    'rⱼ = right(Eⱼⱼ),   Σ rⱼ = 1',
    'rⱼ commutes with old B and M.'
])
card(1000,112,430,250,'The projection and traces',[
    'tⱼ = (j + θ)/n,   pₜ = 1₍ₜ,∞₎(h)',
    'P = Σ pₜⱼ rⱼ ∈ Ã,   P² = P',
    'Tr̃(T rⱼ) = n Tr(T)',
    'Tr̃(T) = n² Tr(T) for old T',
    'Both center measures are retained.'
])
arrow(465,505,237);arrow(950,990,237)
card(30,394,685,253,'Mesh and one simultaneous shift',[
    'H = (1/n)Σ pₜⱼ,   η = Tr(q)/n < 1',
    '‖H − h‖₁ ≤ η;   Tr̃(P) = n² Tr(H)',
    'joint(P)/Tr̃(P) ≤ (Jₕ + 2η)/(1 − η)',
    'One θ: Σᵤ ‖[u,P]‖₂²/Tr̃(P) ≤ 2Σᵤ √εᵤ/(1 − η)',
    'εᵤ = ‖u h u* − h‖₁;   choose n after this L.'
])
card(745,394,685,253,'Prefix retention and later physical tests',[
    'F = Nₖ′∩M; the absorption map fixes F pointwise.',
    'Fixed marked cups recover the entire old prefix.',
    'It need not fix Nₖ pointwise by the tensor map.',
    'Two deletions: ‖bᵢ⁰⁰ − bᵢ‖₂,τ < 4δ.',
    'New test defect ≤ old defect + 4√(4δ² + χd).'
],color='#e6f3e9',stroke='#37834d')
card(30,679,685,234,'Four right-coordinate cuts (scalar sample)',[
    'Eigenvalues: 1/4 and 3/4;   n = 4,   θ = 1/2.',
    'Thresholds: 1/8, 3/8, 5/8, 7/8.',
    'Ranks of the four cuts: 2, 1, 1, 0.',
    'Their average H equals h in this example.'
])
for j,rows in enumerate([[1,1],[0,1],[0,1],[0,0]]):
    for i,occupied in enumerate(rows):
        x=499+45*j;y=820+32*i
        parts.append(f'<rect x="{x}" y="{y}" width="25" height="25" fill="{chr(35)+"3266a1" if occupied else "white"}" stroke="#3266a1"/>')
card(745,679,685,234,'The charged band and the remaining input',[
    'Lost relative trace r gives χ ≤ 2η/(1 − η) + 2r.',
    'The positive band is [a, n²L]; further deletion',
    'scales dimensions by b² and retains the prefix.',
    'A larger matrix does not erase a positive Jₕ.',
    'General joint balance and the full partition remain open.'
],color='#fff0e8',stroke='#a4492e')
text(30,958,'Boxes and areas are schematic. The scalar sample is not an asserted ordinary Jones core.','small')
text(30,991,'Both rows use their inherited full-corner traces; the smaller and larger centers remain distinct.','small')
text(30,1024,'Human context: S. Popa, Classification of amenable subfactors of type II (1994), §§4.2 and4.4.','small')
text(30,1057,'Independent exposition and reproducible figure: GPT-6.1 Sol (OpenAI), October 2026; CC0 1.0.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
