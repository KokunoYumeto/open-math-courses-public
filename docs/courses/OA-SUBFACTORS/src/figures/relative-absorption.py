"""Reproduce Figure50.1: simultaneous relative tensor decomposition.

All rates are exact proof bounds, not fitted numerical convergence.
"""
from pathlib import Path
from html import escape
from fractions import Fraction

OUT=Path(__file__).with_suffix('.svg')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1000" viewBox="0 0 640 1000" role="img" aria-labelledby="title desc">',
 '<title id="title">Two algebras share one infinite binary tensor factor</title>',
 '<desc id="desc">Commuting matrix factors in the smaller algebra, decreasing complements, and exact coefficient and error bounds.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
 '<rect width="640" height="1000" fill="#f9fcfe"/>']
def text(x,y,s,size=19,color='#163c50',anchor='middle',weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>')
def line(x1,y1,x2,y2,arrow=False):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#315b70" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def box(x,y,w,h,title,detail):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#eaf3f8" stroke="#6b96ad"/>')
    text(x+w/2,y+29,title,23,weight='bold')
    if detail:text(x+w/2,y+56,detail,17)

text(320,37,'A common factor for A ⊂ B',27,weight='bold')
text(320,68,'Finite type II algebras; centers may be nontrivial',19)
box(45,91,550,82,'Q₁, Q₂, … ⊂ A','Each Qₖ ≅ M₂; different Qₖ commute exactly')
line(320,174,320,212,True)
box(45,220,550,82,'Dₖ = Q₁ ⊗ ··· ⊗ Qₖ ≅ M(2ᵏ)','Lemma 50.3 repairs the next factor inside Dₖ′ ∩ A')
line(320,303,320,344,True)
box(45,351,245,85,'Pₖᴬ = Dₖ′ ∩ A','Pₖ₊₁ᴬ ⊂ Pₖᴬ')
box(350,351,245,85,'Pₖᴮ = Dₖ′ ∩ B','Pₖ₊₁ᴮ ⊂ Pₖᴮ')
text(320,399,'⊂',27)
text(320,472,'Coefficients lie in the appropriate complement',20)
text(320,503,'4ᵏ coefficients × tail error < 3·8⁻ᵏ',20)
text(320,536,'Reconstruction error < 3·2⁻ᵏ → 0',23,weight='bold')
line(320,550,320,587,True)
box(45,596,550,80,'ℛ₀ = (⋃ Dₖ)″ ⊂ A','Pᴬ = ℛ₀′ ∩ A; Pᴮ = ℛ₀′ ∩ B; Pᴬ ⊂ Pᴮ')
line(320,677,320,710,True)
text(320,742,'A ≅ Pᴬ ⊗ ℛ₀',27,weight='bold')
text(320,778,'B ≅ Pᴮ ⊗ ℛ₀',27,weight='bold')
text(320,813,'Both maps are multiplication with the same ℛ₀.',19)
text(320,845,'Traces factorize; maps are normal and injective.',19)
line(35,867,605,867)
text(320,901,'Exact upper bounds at k = 1, 2, 3',20,weight='bold')
for i,k in enumerate([1,2,3]):
    text(115+i*205,936,f'k={k}: 3/2ᵏ = {Fraction(3,2**k)}',18)
text(320,974,'Theorem 50.4 · equations 50.11–50.14 · complements need not be factors',15)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT)
