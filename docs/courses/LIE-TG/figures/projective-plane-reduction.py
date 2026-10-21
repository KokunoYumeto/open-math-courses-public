"""Complete projective-plane case division, Theorem 8.9. CC0-1.0."""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1480" viewBox="0 0 1280 1480" role="img" aria-labelledby="title desc">
<title id="title">Every complex projective-plane Lie algebra</title>
<desc id="desc">Irreducible matrix actions are the full sl3 algebra or the three-dimensional conic stabilizer. Reducible nonsolvable actions give six affine or block models. Every solvable action preserves a complete flag and lies in its five-dimensional stabilizer; projection onto the affine x-line and all vertical kernels give the complete covering list.</desc>
<rect width="1280" height="1480" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:31px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a='' if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color='#fff'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
def arrow(x,y,xx,yy):parts.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
text(40,48,'The complete projective-plane reduction','title')
text(40,85,'h ⊂ pgl₃(ℂ) ≅ sl₃(ℂ), acting on ℙ(ℂ³); ordinary projective conjugacy first.','math')
box(40,110,1200,87,'#e0f2fe')
text(640,147,'Does the matrix action preserve a proper nonzero subspace of ℂ³?','head','middle')
text(640,180,'A matrix line is a projective point; a matrix plane is a projective line.','small','middle')
arrow(330,197,330,230);arrow(950,197,950,230)
box(40,232,570,225,'#fef3c7')
text(65,273,'No: irreducible','head')
text(65,312,'Every solvable ideal acts by scalars, hence is zero.','small')
text(65,350,'A maximal toral algebra has dimension 1 or 2.','small')
text(65,391,'rank 1: C₃, the nonsingular conic stabilizer','math')
text(65,431,'rank 2: full sl₃, dimension 8','math')
box(640,232,600,225,'#dcfce7')
text(665,273,'Yes: reducible','head')
text(665,312,'A point or a line is invariant.','small')
text(665,350,'Point and line cases are exchanged by duality.','small')
text(665,391,'Separate nonsolvable and solvable actions.','head')
text(665,431,'Ordinary projective types remain distinct.','small')
box(40,488,1200,217,'#fff')
text(65,531,'Reducible and nonsolvable: six types','head')
text(65,572,'A preserved line gives affine matrices (L,b) ∈ gl₂ ⋉ ℂ².','math')
text(65,612,'The image is sl₂ or gl₂; its translation kernel is 0 or ℂ².','small')
text(65,652,'Full kernel: A₅, A₆ and their duals.   Zero kernel: L₃, L₄ (self-dual).','math')
text(65,686,'The zero-kernel graph is removed by the explicit equation β([L,K]) = Lβ(K) − Kβ(L).','small')
box(40,735,1200,354,'#e0f2fe')
text(65,778,'Solvable: an incident point / line flag is invariant','head')
text(65,819,'Choose the line at infinity and its vertical point:  b = ⟨p,q,R,A,B⟩, R = xq.','math')
text(65,861,'Projection onto the affine x-line:','head')
text(65,903,'image 0','math');text(420,903,'image ⟨p⟩ or ⟨A⟩','math');text(900,903,'image ⟨p,A⟩','math')
text(65,947,'The vertical kernel lies in k = ⟨q,R,B⟩. Its complete list is:','small')
text(65,988,'0;   ⟨q⟩, ⟨R⟩, ⟨B⟩;   ⟨q,R⟩, ⟨q,B⟩, ⟨R,B⟩;   k.','math')
text(65,1030,'A kernel with a nonconstant translation coefficient forces its root to be fixed by the image.','small')
text(65,1068,'Lemma 8.8 solves every lift and every residual bracket, including resonant coefficients.','small')
box(40,1119,1200,219,'#ecfdf5')
text(65,1162,'Changing the flag gives the final projective parameter relations','head')
text(65,1203,'F₄(a,c), K₂(a,c): [a:c] exact.    T₃(a,c): [a:c] ~ [c:a].','math')
text(65,1244,'W₃(a,c): [a:c] ~ [a:a−c].    One-dimensional distinct eigenvalues: six values.','math')
text(65,1285,'Nilpotent ranks, common kernels/images and Jordan parts separate all remaining types.','small')
text(65,1320,'No seven-dimensional algebra occurs; zero and the full algebra are included.','small')
text(40,1387,'Proof: Lemmas 8.6–8.8 and Theorem 8.9. Exact dual pairings: Corollary 8.10.','small')
text(40,1430,'The schematic concerns complex connected local projective actions and their matrix algebras.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
