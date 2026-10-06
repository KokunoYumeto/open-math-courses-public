"""Reproducible exact 2D support/rank diagram for Lesson78. No spatial model."""
from pathlib import Path
from html import escape
W,H=1000,1490
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
   '<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9" fill="#426580"/></marker></defs>',
   f'<rect width="{W}" height="{H}" fill="#f2f6fb"/>']
def text(x,y,s,size=22,color='#18334b',bold=False):
 p.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def box(x,y,w,h,color='#fff'):
 p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#b9ccdc"/>')
def arrow(x,y,xx,yy):
 p.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#426580" stroke-width="2.5" marker-end="url(#arr)"/>')
def panel(y,h,title):
 box(25,y,950,h);text(48,y+38,title,24,bold=True)
text(30,44,'Exact trace certificates close the residual',31,bold=True)
text(30,78,'Actual weights • finite full partition • primitive promotion • precise scope',21)

panel(103,296,'1. A physical support needs an exact finite trace certificate')
box(48,162,415,112,'#eaf2fc');box(538,162,415,112,'#eaf7f1')
text(65,194,'Bⱼ = ⊕ℓ Mat_(nⱼℓ)',24)
text(65,227,'ranks: 0 ≤ hℓ ≤ nⱼℓ, hℓ integer',21)
text(65,258,'minimal weights: ωⱼℓ = τ(eℓ)',21)
arrow(478,216,522,216)
text(555,194,'Σℓ ωⱼℓ hℓ = τ(f) exactly',24)
text(555,228,'g ∈ Bⱼ with τ(g) = τ(f)',22)
text(555,261,'u ∈ N and ugu* = f',22)
text(49,316,'Conjugate only the new tunnel:  f ∈ uBⱼu* ⊂ uAⱼu*.',23)
text(49,351,'Finite alignment makes the trace set independent of the tunnel choice.',20)
text(49,382,'Proof: 78.1–78.3; Theorems 78.2–78.3',18)

panel(420,277,'2. Keep the old square and enlarge its retained corner')
text(49,497,'Selected whole-stage blocks',21,bold=True);text(671,497,'Retained residual',21,bold=True)
box(49,517,205,55,'#eaf2fc');box(270,517,205,55,'#eaf2fc');box(491,517,153,55,'#eaf2fc');box(662,517,292,55,'#fff1df')
text(67,552,'P₁ / Q₁',23);text(288,552,'P₂ / Q₂',23);text(539,552,'…',27);text(679,552,'fA₀ / ℂf',23)
arrow(808,584,808,618)
text(49,615,'r₁ + ··· + r_q + f = 1 exactly',23)
text(49,647,'P₀ ⊂ P*;   all old blocks and targets stay fixed',21)
text(49,678,'78.4–78.9; EN EP* = EQ*',19)
text(669,645,'f(uAⱼu*)f / f(uBⱼu*)f',21)
text(669,674,'contains fA₀ / ℂf',19)

panel(719,322,'3. Primitive example: the scalar trace becomes valid ranks')
text(49,794,'C = [[2, 1], [1, 2]],  ρ = 3,  v = (−1, 2),  τ(v) = 1/2',23)
box(48,821,280,131,'#fff1df');box(360,821,280,131,'#eaf7f1');box(672,821,280,131,'#eaf7f1')
text(65,853,'level 0',22,bold=True);text(377,853,'level 1',22,bold=True);text(689,853,'level 2',22,bold=True)
text(65,885,'ranks (−1, 2)',23);text(377,885,'ranks (0, 3)',23);text(689,885,'ranks (3, 6)',23)
text(65,916,'capacities (1, 1)',21);text(377,916,'capacities (3, 3)',21);text(689,916,'capacities (9, 9)',21)
text(65,943,'weights (1/2, 1/2)',18);text(377,943,'weights (1/6, 1/6)',18);text(689,943,'weights (1/18, 1/18)',18)
arrow(333,887,352,887);arrow(646,887,665,887)
text(49,990,'Cᵏv ≥ 0 and Cᵏ(n − v) ≥ 0 eventually; the trace remains exactly 1/2.',22)
text(49,1023,'Primitive proof: 78.10–78.17; worked system: Example 78.8',18)

panel(1063,316,'4. Reducible diagnostic: scalar subtraction does not suffice')
text(49,1138,'α = √2/2,   Fₖ = Mat_(2ᵏ) ⊕ Mat_(2ᵏ),   C = 2I₂',24)
text(49,1177,'Two disjoint physical conjugates of (0, 1): each trace = 1 − α.',22)
text(49,1216,'Residual trace: 1 − 2(1 − α) = √2 − 1 ∈ (0, 1).',24)
box(49,1240,901,71,'#fff1df')
text(67,1271,'Formal canonical ranks: (1, −1) → (2, −2) → (4, −4) → ···',23)
text(67,1301,'Negative second rank at every stage: no finite certificate.',21)
text(49,1345,'Abstract system only; no actual Jones-core or subfactor counterexample.',21)
text(49,1369,'78.18–78.21; Example 78.7; Exercise 78.4',18)

text(30,1420,'Finite depth supplies a primitive tail with the actual reflected trace (78.6).',21,bold=True)
text(30,1449,'Human source: S. Popa, Classification of amenable subfactors of type II (1994),',18)
text(30,1475,'Theorem 4.4.1(1), printed p.222. General exact partition and generating routes remain assigned.',18)
p.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(p)+'\n',encoding='utf-8')
