"""Exact reproducible trace-order diagram. No sampled numerical geometry."""
from pathlib import Path
from html import escape
W,H=1000,1490
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
 '<title>Finite trace order and the remaining support</title>',
 '<desc>Nested trace simplexes test finite integer ranks. The changing two-block vector promotes at level two. Critical path weights allow a kernel correction; a transcendental parameter forbids it. The unrestricted actual amenable-inclusion partition remains open.</desc>',
 '<defs><marker id="arr" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0 L9 4.5 L0 9" fill="#416682"/></marker></defs>',
 f'<rect width="{W}" height="{H}" fill="#f2f6fb"/>']
def text(x,y,s,size=22,bold=False,color='#16344d'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" fill="{color}" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def box(x,y,w,h,fill='#fff'):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#b9cdda"/>')
def panel(y,h,title):
 box(25,y,950,h);text(47,y+38,title,24,True)
def arrow(x,y,xx,yy):
 parts.append(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}" stroke="#416682" stroke-width="2.5" marker-end="url(#arr)"/>')
text(30,45,'Finite trace order and the remaining support',31,True)
text(30,79,'Exact finite ranks • all norm traces • critical-path repair • precise boundary',21)
panel(103,280,'1. All compatible norm traces control promotion')
text(48,178,'Kⱼ,ⱼ ⊃ Kⱼ,ⱼ₊₁ ⊃ Kⱼ,ⱼ₊₂ ⊃ ···',25)
text(48,216,'aₖ = minℓ(vₖℓ / nₖℓ) ↗ minσ σ(v)',23)
text(48,254,'bₖ = maxℓ(vₖℓ / nₖℓ) ↘ maxσ σ(v)',23)
box(48,274,900,58,'#e9f6ef')
text(66,312,'If every σ has 0 < σ(v) < 1, then 0 ≤ vₖ ≤ nₖ at a finite level.',23)
text(48,361,'Weights are minimal-projection weights; σ ranges over all norm traces. 79.1–79.6',18)
panel(403,247,'2. A changing two-block system: Dⱼ = [[j + 2, 1], [1, j + 2]]')
for x,k,v,n,weight in [(48,0,'(−2, 3)','(1, 1)','(1/2, 1/2)'),(360,1,'(−1, 4)','(3, 3)','(1/6, 1/6)'),(672,2,'(1, 11)','(12, 12)','(1/24, 1/24)')]:
 box(x,465,280,129,'#eaf2fc' if k<2 else '#e9f6ef')
 text(x+17,494,'level '+str(k),21,True)
 text(x+17,526,'ranks '+v,23)
 text(x+17,558,'capacities '+n,21)
 text(x+17,583,'weights '+weight,18)
arrow(333,528,351,528);arrow(645,528,664,528)
text(48,628,'Exact trace = 1/2; the first valid promotion is level 2. Example 79.4',20)
panel(670,266,'3. Critical path trace: a kernel correction gives the certificate')
text(48,743,'δ = 2, t = 1/4. Level 4 capacities (2, 3, 1); weights (1, 3, 5)/16.',22)
box(48,765,423,100,'#fff1df');box(529,765,423,100,'#e9f6ef')
text(65,797,'signed ranks (2, 3, −1)',24)
text(65,831,'trace 3/8; character −1',22)
arrow(481,814,519,814)
text(546,797,'valid ranks (0, 2, 0)',24)
text(546,831,'trace 3/8; character 0',22)
text(48,901,'Difference polynomial = 1 − 4t: it vanishes at t = 1/4. 79.18',21)
text(48,925,'Bounded integer coins prove every dyadic trace is available. Theorem 79.6',18)
panel(956,295,'4. Transcendental noncritical trace: no alternative certificate')
text(48,1031,'Choose transcendental t ∈ (1/5, 1/4), δ = 1/√t > 2.',24)
text(48,1072,'Outermost level-4 p: τ(p) = 1 − 3t + t² < 11/25 < 1/2.',23)
text(48,1112,'Two disjoint physical conjugates: residual R(t) = −1 + 6t − 2t² > 0.',22)
box(48,1132,901,62,'#fff1df')
text(65,1171,'Any finite q with τ(q) = R(t) would have χ(q) = R(0) = −1.',23)
text(48,1227,'Impossible for a projection. The path GNS algebra is still a II₁ factor. Proposition 79.7',19)
panel(1271,138,'5. Actual inclusion: the unrestricted proof still needs additional input')
text(48,1345,'Use actual norm-trace uniqueness or an actual critical-path trace identification.',21)
text(48,1378,'Factoriality alone supplies neither; no amenable-subfactor counterexample is inferred.',20)
text(30,1445,'Proof locators: 79.1–79.18. Human source endpoint: S. Popa (1994),',19)
text(30,1474,'Classification of amenable subfactors of type II, Theorem 4.4.1(1), printed p.222.',19)
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_bytes(('\n'.join(parts)+'\n').encode('utf-8'))
