from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html, math, base64

out = Path(__file__).resolve().parent.parent / 'figures'
W, H = 2520, 2100
im = Image.new('RGB', (W, H), '#f5f7fb')
d = ImageDraw.Draw(im)
fontroot = Path(__file__).resolve().parent / 'fonts'
regular = fontroot / 'DejaVuSansCondensed.ttf'
bold = fontroot / 'DejaVuSansCondensed-Bold.ttf'
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="100%" height="100%" fill="#f5f7fb"/>']

# Cross-platform SVG font binding; retain the complete embedded-font licence.
fontcss=[]
for fontname,weight in [('DejaVuSansCondensed.ttf','400'),('DejaVuSansCondensed-Bold.ttf','700')]:
    fontdata=base64.b64encode((Path(__file__).resolve().parent/'fonts'/fontname).read_bytes()).decode('ascii')
    fontcss.append("@font-face{font-family:'NCG-DejaVu-Condensed';font-style:normal;font-weight:"+weight+";src:url(data:font/ttf;base64,"+fontdata+") format('truetype')}")
svg.insert(1,'<defs><style>'+''.join(fontcss)+'</style></defs>')
svg.insert(1,'<metadata>'+html.escape((Path(__file__).resolve().parent/'fonts/LICENSE_DEJAVU.txt').read_text(encoding='utf-8'))+'</metadata>')


def text(x, y, value, size=34, color='#18273d', weight=False):
    font = ImageFont.truetype(str(bold if weight else regular), size)
    d.text((x, y), value, font=font, fill=color)
    svg.append(f'<text x="{x}" y="{y+size}" font-family="NCG-DejaVu-Condensed" font-size="{size}" font-weight="{"bold" if weight else "normal"}" fill="{color}">{html.escape(value)}</text>')

def box(x, y, w, h, title, lines, accent='#246f94', size=31):
    d.rounded_rectangle((x,y,x+w,y+h), radius=18, fill='white', outline=accent, width=3)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="white" stroke="{accent}" stroke-width="3"/>')
    text(x+25, y+18, title, 36, accent, True)
    for i, line in enumerate(lines): text(x+25, y+77+i*47, line, size)

def arrow(x1,y1,x2,y2):
    d.line((x1,y1,x2,y2), fill='#246f94', width=6)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2),(x2-22*math.cos(a-.5),y2-22*math.sin(a-.5)),(x2-22*math.cos(a+.5),y2-22*math.sin(a+.5))]
    d.polygon(pts,fill='#246f94')
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#246f94" stroke-width="6"/>')
    svg.append('<polygon points="'+ ' '.join(f'{x},{y}' for x,y in pts)+'" fill="#246f94"/>')

text(65,35,'The compact-subgroup product and restriction projector',49,weight=True)
text(65,110,'G = SU(1,1), K = U(1), X = G/K with curvature −1; full exterior parity throughout',32)

box(65,180,2390,205,'A checked failed connection formula is excluded',[
    'Sₓ = Θₓ + (1−Θₓ²)¹⁄⁴ F_H (1−Θₓ²)¹⁄⁴ fails the F_H creation connection.',
    'No current proof step uses this failed formula; the full negative Witten product is used below.'
],accent='#9b3e4a')

box(65,435,1140,280,'1. Exact rank-two covector rotation',[
    'P = C₀(X, Cl⁺(T*X)); η(y) = c₊(r dr / √(1+r²)).',
    'ηₜ = c₊(cos(πt) ξ + sin(πt) Jξ), 0 ≤ t ≤ 1.',
    'J is the invariant oriented cotangent rotation.',
    'η₀ = η, η₁ = −η; ηₜ² = r²/(1+r²).'
])
box(1315,435,1140,280,'2. Complete hyperbolic Hodge space',[
    'H = L²(X, Λ*), D = d+d*, Q = D−c₊(d(r²/2)).',
    'Q has its actual closed compact-core domain.',
    'Q² ≥ ∇*∇ + r²/2 − 4; whole resolvents compact.',
    'ker Q = ℂ e^(−r²/2) vol, even and K-fixed.'
])
arrow(1208,573,1309,573)

box(65,765,1140,350,'3. Full graded Hodge creation connection',[
    'ε = (−1)^|p|, p ∈ C∞c(X,Cl⁺), Kₚ = Qρ(p)−ερ(p)D.',
    'Kₚ is bounded; compact support controls the potential.',
    'R_Q(z)ρ(p)−ερ(p)R_D(εz)',
    '                 = −ε R_Q(z) Kₚ R_D(εz).',
    'Error norm ≤ ‖Kₚ‖/λ² for z = ±iλ.',
    'Two-pole integration: full compact connection.'
],size=29)
box(1315,765,1140,350,'4. Positivity in the whole compact quotient',[
    'a = −η, C = {a,Q} = 2r²/√(1+r²) + B, ‖B‖ ≤ 2.',
    'R± = (Q±iλ)⁻¹, λ = √(1+t²).',
    '{a, Q(Q²+λ²)⁻¹} = ½(R₊CR₋ + R₋CR₊).',
    'Replace C by C+2 ≥ 0: both sandwiches positive.',
    'Compact correction 2(Q²+λ²)⁻¹ has norm ≤ 2/λ².',
    'Positive strong limit + norm-compact correction.'
],size=29)

box(65,1165,2390,250,'5. The actual K-product is the scalar unit',[
    'r(η) ⊗ₚ r(d) is represented by the complete Q bounded transform (or its compactly differing phase).',
    'The nonzero phase summand is exactly K-degenerate. The even Gaussian is the trivial K-module.',
    'Thus r(γ)=1, γ=η⊗ₚd. This uses the full product criterion and full represented splitting.'
])

box(65,1465,1140,295,'6. Actual induction and Cartan paths',[
    'Iₚ(x): Eₓ = Γ₀(G×ₖE), then Eₓ ⊗C₀(X) P.',
    'L(x) = (1_A ⊗ η) ⊗ Iₚ(x) ⊗ d.',
    'Cartan path sₜ(z)=exp(tY_z) moves the A action.',
    'Transported F′z=U(s(z))FU(s(z))* moves to F.',
    'All P-localized errors are whole-interval compacts.'
],size=29)
box(1315,1465,1140,295,'7. Projector and the actual native difference',[
    'rL(x)=x ⊗ r(γ)=x; Lr(y)=γy. Hence γ²=γ.',
    'Boundary factorization gives z=q*w.',
    'Parabolic contraction/induction: σ_Q(γ)=1_Q.',
    'So z=γz=Lrz=0, since the full K-comparison gives rz=0.',
    'Finite-center descent and holonomy transport finish.'
],size=28)

text(65,1820,'Section 11B proof locators: WP.1–WP.42; RP.0–RP.8;',30,weight=True)
text(65,1868,'HF.1–HF.7; RR.2–RR.3 and RR.6–RR.8. Entire exterior parity and all compact ideals retained.',29)
text(65,1916,'Human sources: Kasparov (1988), equivariant products and induction; Skandalis (1985), Stinespring construction.',29)
text(65,1964,'This is an exact proof map. Arrows denote represented constructions or KK products, with the displayed types.',29)
text(65,2012,'Literal same-spin class remains δ_S = −δ_inv[D], D = det S = LH²; Tδ_S = −[D].',30)

im.save(out/'kt-hyperbolic-restriction-projector.png')
svg.append('</svg>')
(out/'kt-hyperbolic-restriction-projector.svg').write_text('\n'.join(svg)+'\n',encoding='utf-8')
print('Rendered exact repaired projector proof map: kt-hyperbolic-restriction-projector.png/svg')
