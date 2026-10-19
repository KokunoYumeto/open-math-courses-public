"""Reproduce the exact implication and remainder diagram."""
from pathlib import Path
from html import escape
HERE=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="610" viewBox="0 0 1100 610" role="img" aria-labelledby="title desc">',
 '<title id="title">Normal-fiber bound and finite front jets</title>',
 '<desc id="desc">The top path splits a symbol at its front constant and obtains a two-marginal Fourier bound from two output derivatives. The bottom path retains N exact front jets and bounds only the weighted full residual error by the original Banach norm.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10Z" fill="#334155"/></marker></defs>',
 '<rect width="1100" height="610" fill="#f8fafc"/>',
 '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#172c43;font-size:20px}.title{font-size:26px;font-weight:600}.small{font-size:18px}.box{fill:white;stroke:#58768d;stroke-width:2}.line{stroke:#334155;stroke-width:2;marker-end:url(#arrow)}</style>']
def text(x,y,value,cls=''):
 out.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(value)}</text>')
def box(x,y,w,h,lines):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="box"/>')
 for i,line in enumerate(lines):text(x+16,y+32+30*i,line)
def arrow(x,y,xx,yy):out.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" class="line"/>')
text(30,40,'Output smoothness controls the normal-frequency operator','title')
box(30,65,305,110,['a(v, κ) = θ(v) C(0, κ) + F','F and ∂²ᵥF are integrable','Only two x-derivatives used'])
box(395,65,305,110,['‖F̂(η, κ)‖ ≤ 2L/(1 + η²)','η = ξ − κ','Both marginal integrals finite'])
box(760,65,310,110,['‖Op(a)g‖₂ ≤ C ‖g‖₂','Plancherel + Cauchy–Schwarz','No κ-derivatives required'])
arrow(338,120,390,120);arrow(703,120,755,120)
text(30,225,'Full residuals reduce to finitely many exact front jets','title')
box(30,250,305,110,['R = Rᵇ + F₀','F₀: smooth, flat input kernel','‖F₀ D u‖₂ ≤ C ‖u‖ℬ'])
box(395,250,305,110,['JₙR: jets j = 0, …, N − 1','Full normal-difference tails','Compact physical projections'])
box(760,250,310,110,['R − JₙR = F₀ + ρᴺ Eₙ','Eₙ: full residual kernel','Every term retained'])
arrow(338,305,390,305);arrow(703,305,755,305)
box(395,415,675,105,['M: flat-test order;  q: differential order;  N ≥ M + q + 2',
 'Input test bound: xᴺ⁻¹⁻ᴹ⁻ᑫ ≤ x for 0 < x ≤ 1',
 '‖(R − JₙR)D u‖₂ ≤ C ‖u‖ℬ'])
arrow(915,365,915,410)
text(30,565,'Exact proof locators: N1–N2, W0–W1, J0–J2, T0.  Angular scalar assembly uses a separate geometric construction.','small')
out.append('</svg>');(HERE/'normal-fiber-and-front-jets.svg').write_text('\n'.join(out)+'\n','utf-8')
print(HERE/'normal-fiber-and-front-jets.svg')
