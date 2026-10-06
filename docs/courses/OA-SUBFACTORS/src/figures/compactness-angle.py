"""Uniformly transported finite angle in Ocneanu compactness. CC0."""
from pathlib import Path
from html import escape
from math import sqrt

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="730" viewBox="0 0 540 730" role="img" aria-labelledby="title desc">',
         '<title id="title">A finite angle survives every two-level shift</title>',
         '<desc id="desc">The shift Psi_r sends H0 and H1 to H_2r and H_(2r+1), and fixes their intersection L. Central transfer h_r is uniformly between eta and eta inverse. Squared norm bounds transport the finite angle constant K to K over eta. Martingale adjacency tends to zero, proving the relative commutant is L. The lower planar illustration has theta pi over six, K two; it is an angle schematic, not a commuting square.</desc>',
         '<rect width="540" height="730" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']

def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

def box(y,title,lines,height=116):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+28,title,'heading','middle')
    for i,line in enumerate(lines):
        text(270,y+58+26*i,line,'label' if i==0 else 'small','middle')

text(24,33,'A finite angle determines the commutant','title')
box(55,'A two-level shift preserves algebra structure',[
    'Ψᵣ(H₀) = H₂ᵣ;  Ψᵣ(H₁) = H₂ᵣ₊₁;  Ψᵣ(L) = L',
    'Hₖ = L²(Pₖ′ ∩ Qₖ);  L = P₁′ ∩ Q₀.'])
box(189,'The trace can change, with uniform bounds',[
    'τ(Ψᵣ(x)) = τ(xhᵣ);  η1 ≤ hᵣ ≤ η⁻¹1',
    'η‖x‖₂² ≤ ‖Ψᵣ(x)‖₂² ≤ η⁻¹‖x‖₂².'])
box(323,'One finite angle controls every level',[
    'dist(x₂ᵣ, L) ≤ (K/η) ‖x₂ᵣ − x₂ᵣ₊₁‖₂ → 0',
    'xₖ = E_Qₖ(x), for x ∈ N′ ∩ M.'])
text(270,474,'Therefore N′ ∩ M = P₁′ ∩ Q₀.','heading','middle')

# Planar theta=pi/6: origin (95,655), horizontal y=(295,655).
# Its orthogonal foot is exactly (245,655-50sqrt(3)).
ox,oy=95,655
foot=(245,655-50*sqrt(3))
parts.append('<rect x="24" y="501" width="492" height="208" rx="8" fill="#fff8e9" stroke="#b6a070"/>')
text(42,528,'Planar angle illustration: θ = π/6, K = 2','small')
parts.append(f'<path d="M65 {oy} H325" stroke="#426987" stroke-width="2.5"/>')
parts.append(f'<path d="M{ox} {oy} L320 {oy-225/sqrt(3)}" stroke="#488a70" stroke-width="2.5"/>')
parts.append(f'<path d="M295 {oy} L{foot[0]} {foot[1]}" stroke="#a66442" stroke-width="2" stroke-dasharray="5 4"/>')
parts.append(f'<circle cx="295" cy="{oy}" r="4" fill="#426987"/>')
text(306,678,'y ∈ H₀','small')
text(329,649,'H₀','small')
text(322,560,'H₁','small')
text(82,680,'L = {0}','small')
text(156,645,'θ','small')
text(361,601,'dist(y,H₁)','small')
text(361,627,'= ‖y‖/2','small')
text(42,698,'For η = 1/2, the transported constant K/η is 4.','small')
text(24,727,'Lemmas 31.1–31.3 and Theorem 31.4.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
