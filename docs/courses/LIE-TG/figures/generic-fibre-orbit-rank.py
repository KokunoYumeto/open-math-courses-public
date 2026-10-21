"""Reproduce the finite generic-fibre argument of Theorem 4.35."""
from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
W,H=520,1000
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
 '<title id="title">Generic fibre and orbit rank</title>',
 '<desc id="desc">Theorem 4.35. Over an algebraically closed field of characteristic zero, a finite full orbit quotient has generic fibre dimension r equal to m minus d. Finite normalization and field extension compute this dimension. The entire geometric generic fibre is one full orbit. Separability and translation give generic orbit rank r, so invariant differentials of rank d span the orbit annihilator on the invariant regular rank locus.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="none" stroke="#305b57" stroke-width="1.5"/></marker></defs>',
 '<rect width="520" height="1000" fill="#f7f6ed"/>']
def text(x,y,s,size=19,bold=False,anchor='start',color='#173c3a'):
 parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, DejaVu Sans, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(s)}</text>')
def box(y,h,title,lines):
 parts.append(f'<rect x="24" y="{y}" width="472" height="{h}" rx="10" fill="#ffffff" stroke="#9eb6af" stroke-width="1.5"/>')
 text(42,y+30,title,21,True)
 for i,line in enumerate(lines):text(42,y+61+27*i,line)
def arrow(y1,y2):
 parts.append(f'<path d="M260 {y1} V{y2}" fill="none" stroke="#305b57" stroke-width="2" marker-end="url(#arrow)"/>')
text(260,34,'Generic fibre and orbit rank',25,True,'middle')
text(260,61,'Theorem 4.35 · characteristic zero',17,False,'middle')
box(82,144,'The quotient fields',[
 'k ⊂ F = k(Y) ⊂ K = k(X) ⊂ Ω',
 'm = trdegₖ K, d = trdegₖ F',
 'Ω algebraically closed, r = m − d'])
arrow(232,258)
box(271,145,'The generic fibre Uη over F',[
 'On every nonempty affine chart:',
 'F[t₁, …, tᵣ] ↪ B is finite',
 'Frac B = K, trdegꜰ K = r'])
arrow(422,448)
box(461,145,'Extend to Z = Uη ×ꜰ Ω',[
 'Ω[t₁, …, tᵣ] ↪ B ⊗ꜰ Ω is finite',
 'dim Z = r, allowing nilpotents',
 'and multiple components'])
arrow(612,638)
box(651,145,'The full geometric fibre is an orbit',[
 'Zred = GΩ · xΩ',
 'xΩ comes from the generic point of X',
 'dim(GΩ · xΩ) = r'])
arrow(802,828)
box(841,135,'Invariant regular rank loci',[
 'rank Δ = r, rank(df₁, …, dfₛ) = d',
 'span{df₁, …, dfₛ} = Ann Δ'])
parts.append('</svg>')
(OUT/'generic-fibre-orbit-rank.svg').write_bytes(('\n'.join(parts)+'\n').encode())
