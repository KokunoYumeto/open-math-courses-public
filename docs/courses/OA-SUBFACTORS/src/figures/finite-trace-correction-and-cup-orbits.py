"""Original reproducible diagram: exact finite data, cup orbit and obstruction."""
from pathlib import Path
from html import escape
W,H=900,1660
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365b75"/></marker></defs>',
f'<rect width="{W}" height="{H}" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:19px;fill:#182e43}.title{font-size:28px;font-weight:bold}.head{font-size:22px;font-weight:bold}.math{font-family:Georgia,serif;font-size:23px}.small{font-size:17px}.note{fill:#774914}.arrow{fill:none;stroke:#365b75;stroke-width:2.4;marker-end:url(#arrow)}</style>']
def text(x,y,s,cls=''):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>')
def panel(y,h,title):
    parts.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#b8ccd9"/>')
    text(47,y+35,title,'head')
def box(x,y,w,h,lines):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#eaf2f9" stroke="#92acbd"/>')
    for j,s in enumerate(lines):text(x+14,y+29+28*j,s,'math' if j==0 else '')
def arrow(x,y,xx,yy):
    parts.append(f'<path d="M{x},{y} L{xx},{yy}" class="arrow"/>')
text(34,42,'Finite traces do not determine the orbit of a cup','title')
text(34,75,'Exact finite certificates; their general tower satisfaction remains unproved.','small')
panel(97,285,'1. Match all weighted inclusion data  [67.1]')
box(48,158,328,106,['G = ⊕ᵦ Mat(mᵦ) ⊂ F','nₐ = Σᵦ mᵦ Lᵦₐ','minimal weight tₐ'])
box(519,158,328,106,['V = ⊕𝒹 Mat(M𝒹) ⊂ U','N𝒸 = Σ𝒹 M𝒹 K𝒹𝒸','minimal weight s𝒸'])
arrow(388,208,507,208)
text(400,186,'α₀, anti','small')
text(48,304,'nₐ = Nσ(a),  mᵦ = Mπ(b),  Lᵦₐ = Kπ(b),σ(a),  tₐ = sσ(a).','math')
text(48,344,'All four tests are necessary and sufficient; zero multiplicities count.','small')
panel(403,298,'2. Fix the labels, then solve the marked orbit  [67.2–67.3]')
text(48,478,'p = α₀(g),   H = V′ ∩ U,   α = Ad(vw) α₀.','math')
box(48,501,357,82,['v ∈ U(V),  w ∈ U(H)','vw = wv;  α(G) = V'])
box(479,501,368,82,['vwpw* v* = q','ordinary traces in each U-block'])
arrow(418,541,466,541)
text(48,625,'For block size n, compare every word of length ≤ 2n² − 1.','math')
text(48,664,'A candidate v passing those moments constructs the required w.','small')
panel(723,496,'3. Marginals can agree while the cup image fails  [67.25–67.27]')
text(48,798,'U = Mat₄,  V = diagonal algebra,  H = V,  τ = Tr / 4.','math')
text(48,836,'Both projections: rank 2, trace 1/2, E_V(p) = E_H(p) = 1/2 · I.','small')
def graph(x,y,edges,title):
    text(x,y-33,title,'head')
    pts={1:(x+20,y),2:(x+20,y+142),3:(x+223,y),4:(x+223,y+142)}
    for a,b,label in edges:
        ax,ay=pts[a];bx,by=pts[b]
        parts.append(f'<path d="M{ax},{ay} L{bx},{by}" stroke="#365b75" stroke-width="3"/>')
        label_dy=25 if (a,b)==(1,4) else -35 if (a,b)==(2,3) else -8
        text((ax+bx)/2+3,(ay+by)/2+label_dy,label,'small')
    for a,(xx,yy) in pts.items():
        parts.append(f'<circle cx="{xx}" cy="{yy}" r="18" fill="#eaf2f9" stroke="#365b75"/>')
        text(xx-5,yy+6,str(a),'small')
graph(99,910,[(1,3,'1/2'),(2,4,'1/2')],'p: 2 off-diagonal edges')
graph(528,910,[(1,3,'3/10'),(1,4,'2/5'),(2,3,'−2/5'),(2,4,'3/10')],'q: 4 off-diagonal edges')
text(48,1093,'Diagonal phases preserve magnitudes; permutations preserve edge count.','small')
text(48,1133,'τ(E₁₁ p E₃₃ p) = 1/16;    τ(E₁₁ q E₃₃ q) = 9/400.','math')
text(48,1174,'Best squared distance: fixed labels 1/5; all pair maps 1/10.','math')
panel(1241,263,'4. The actual first blocked endpoints  [67.22–67.24]')
box(48,1305,353,80,['M₋₆′ ∩ M₋₂ ⊂ M₋₆′ ∩ M₀','g₁ᵇˡᵏ = d r₋₂ r₋₃ r₋₁ r₋₂'])
box(488,1305,353,80,['M₂′ ∩ M₆ ⊂ M₀′ ∩ M₆','q₁ = Q₀ = d e₂ e₁ e₃ e₂'])
text(48,1424,'τ(g₁ᵇˡᵏ) = τ(q₁) = d⁻²;   lower cup in M₀, target in M₄.','math')
text(48,1464,'Needed for general generation: liminfₘ Δₘ,ᵢ = 0 for every fixed i.','note')
text(34,1553,'Complete finite proofs: 67.1–67.5; six solutions and the exact obstruction.','small')
text(34,1590,'Human source context: Popa, Classification, §4.5.1, printed pp.223–224.','small')
text(34,1627,'Analytic theorem:65.1–65.6. Actual canonical blocked cup:66.4.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
