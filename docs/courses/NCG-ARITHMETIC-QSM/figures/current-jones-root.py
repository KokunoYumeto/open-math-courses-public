"""Reproduce Figure19.1. Original CC0 diagram, GPT-6.1 Sol, Ultra."""
from pathlib import Path
from html import escape
from math import sqrt
phi=(1+sqrt(5))/2
out=['<svg xmlns="http://www.w3.org/2000/svg" width="820" height="1040" viewBox="0 0 820 1040" role="img" aria-labelledby="title desc">',
 '<title id="title">The rooted Jones window and its thermal factor</title>',
 '<desc id="desc">A4 with base1 and root0; faithful finite compression, canonical endpoint Gibbs masses with lower bound phi to the minus3, and bounded strong lifts identifying the Jones closure with a type II infinity graph factor.</desc>',
 '<rect width="820" height="1040" fill="#fff"/>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#17657b"/></marker></defs>',
 '<style>text{font-family:Arial,sans-serif;fill:#182124}.heading{font-size:24px;font-weight:700}.label{font-size:22px}.small{font-size:19px}.box{fill:#f3f7f8;stroke:#cad8dd;stroke-width:1.5}.line{stroke:#17657b;stroke-width:2.5;fill:none}</style>']
def text(x,y,s,kind='label',anchor='start'):
    out.append(f'<text x="{x}" y="{y}" class="{kind}" text-anchor="{anchor}">{escape(s)}</text>')
def panel(y,h):
    out.append(f'<rect x="20" y="{y}" width="780" height="{h}" rx="12" class="box"/>')
def line(x,y,u,v,arrow=False):
    marker=' marker-end="url(#arrow)"' if arrow else ''
    out.append(f'<path d="M{x},{y} L{u},{v}" class="line"{marker}/>')

panel(20,225);text(42,58,'1. A line graph with endpoint root 0','heading')
xs=[120,310,500,690]
for x,u in zip(xs,xs[1:]):line(x,119,u,119)
for i,x in enumerate(xs):
    fill='#17657b' if i%2==0 else '#fff'
    out.append(f'<circle cx="{x}" cy="119" r="17" fill="{fill}" stroke="#17657b" stroke-width="2"/>')
    text(x,90,str(i),'label','middle')
    text(x,159,'odd' if i%2==0 else 'even','small','middle')
text(120,194,'root','small','middle');text(310,194,'base','small','middle')
text(42,229,'δ = φ, λ = φ, v₂/v₀ = φ;   B = [[0, 1], [1, 1]]','small')

panel(263,238);text(42,301,'2. The local isomorphism — Lemma 19.1','heading')
out.append('<rect x="52" y="330" width="240" height="66" fill="#fff" stroke="#cad8dd"/>')
out.append('<rect x="436" y="330" width="312" height="66" fill="#fff" stroke="#cad8dd"/>')
text(172,371,'J_N','label','middle');text(592,371,'q_N⁰ A_N q_N⁰','label','middle')
line(306,363,419,363,True);text(362,343,'ρ_N','label','middle')
text(42,431,'ρ_N(x) = q_N⁰ x;  rooted path length = 4N + 2','label')
text(42,468,'x_N = ρ_N⁻¹(q_N⁰a),   ‖x_N‖ ≤ ‖a‖     (19.9)','label')

panel(519,275);text(42,557,'3. Canonical Gibbs block masses','heading')
text(42,595,'w_m(b) = Q_m(0, b)     (19.4)','label')
barx=220;barwidth=510
for endpoint,mass,exact,y in [(0,phi**-2,'φ⁻²',632),(2,phi**-1,'φ⁻¹',688)]:
    text(42,y+22,f'm=0, b={endpoint}','small')
    out.append(f'<rect x="{barx}" y="{y}" width="{barwidth}" height="28" fill="#e5ecef"/>')
    out.append(f'<rect x="{barx}" y="{y}" width="{barwidth*mass:.4f}" height="28" fill="#17657b"/>')
    text(barx+barwidth*mass+10,y+22,exact,'label')
bound=barx+barwidth*phi**-3
out.append(f'<path d="M{bound:.4f},624 L{bound:.4f},724" stroke="#b46324" stroke-width="3" stroke-dasharray="6 4"/>')
text(42,754,'Every w_m(b) ≥ φ⁻³;  Jones KMS χ ≤ φ³ ω_can','label')
text(42,783,'m=0: C ⊕ C;   m=1: M₅ ⊕ M₈     (rooted A₄)','small')

panel(813,200);text(42,851,'4. Recover the thermal factor — Theorem 19.2','heading')
text(42,892,'q_N⁰ → 1 strongly in the root-0 graph sector','label')
text(42,930,'‖(x_N − a)ξ‖ ≤ 2‖a‖ ‖(1 − q_N⁰)ξ‖ → 0','label')
text(42,971,'Jones closure M_J = M₀, of type II∞ at index φ²','label')
text(42,999,'Theorem 19.2 also proves uniqueness for every β > 0.','small')
out.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(out)+'\n',encoding='utf-8')
