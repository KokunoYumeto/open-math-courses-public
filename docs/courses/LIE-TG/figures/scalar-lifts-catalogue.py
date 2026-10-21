"""Every scalar lift of a projective matrix algebra, Theorem8.13. CC0-1.0."""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1490" viewBox="0 0 1280 1490" role="img" aria-labelledby="title desc">
<title id="title">All three-variable linear algebras from their traceless images</title>
<desc id="desc">The traceless projection has scalar kernel. A subalgebra either contains the full scalar line and is a direct scalar extension, or is the graph of a character on its traceless image. Character means vanishing on every commutator. The complete character normalizer tables and joint homogeneous parameters classify the graphs, including zero-weight boundary characters and disconnected normalizer actions.</desc>
<rect width="1280" height="1490" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:31px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a=''if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color='#fff'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
def arrow(x,y,xx,yy):parts.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
text(40,49,'From every projective type to every linear lift','title')
text(40,87,'h ⊂ gl₃(ℂ),   π(M) = M − ⅓ tr(M)I,   k = π(h) ⊂ sl₃(ℂ).','math')
box(40,115,1200,86,'#e0f2fe');text(640,153,'The scalar intersection h ∩ ℂI is either ℂI or zero.','head','middle')
text(640,185,'Matrix conjugation preserves that intersection and the traceless image.','small','middle')
arrow(330,201,330,237);arrow(950,201,950,237)
box(40,239,570,210,'#dcfce7');box(640,239,600,210,'#fef3c7')
text(65,281,'Full scalar kernel','head');text(665,281,'Zero scalar kernel','head')
text(65,326,'h⁺(k) = k ⊕ ℂI','head math');text(665,326,'h(k,χ) = {X+χ(X)I : X ∈ k}','head math')
text(65,367,'Subtract the scalar part of every lift.','small');text(665,367,'χ is linear and χ([k,k]) = 0.','math')
text(65,409,'Conjugacy is exactly conjugacy of k.','small');text(665,409,'Conjugacy transports the actual character.','small')
box(40,480,1200,185,'#fff')
text(65,523,'Every graph parameter is classified under the full matrix normalizer','head')
text(65,564,'P k P⁻¹ = k′,   χ′(PXP⁻¹) = χ(X),   for every X ∈ k.','math')
text(65,606,'Perfect k: only χ=0.   Matrix lines: complete eigenvalue / Jordan-block classification.','small')
text(65,642,'Every higher-dimensional projective type is included in the two tables of Theorem 8.13.','small')
box(40,696,1200,282,'#e0f2fe')
text(65,738,'Four diagonal families use a joint homogeneous triple [a:c:t]','head')
text(65,778,'χ(D(a,c)) = t;   (a,c) ≠ (0,0);   scale a,c,t together.','math')
text(65,819,'F₄, K₂: exact triple.   T₃: [a:c:t] ~ [c:a:t].','math')
text(65,860,'W₃: [a:c:t] ~ [a:a−c:−t].','math')
text(65,901,'A zero root weight permits one extra nilpotent character ε ∈ {0,1}.','small')
text(65,941,'The ordered flag fixes the F₄/K₂ parameters; quotient eigenline exchanges give T₃/W₃.','small')
box(40,1009,1200,266,'#ecfdf5')
text(65,1051,'The remaining normalizer actions are explicit','head')
text(65,1092,'Two diagonal generators: an exact pair, an exchange, a reflection, or S₃ on a triple.','small')
text(65,1133,'Heisenberg n: four binary character types.   U and U′: zero / nonzero character.','small')
text(65,1174,'The regular nilpotent plane ⟨E,E²⟩: exactly (0,0), (1,0), (0,1).','math')
text(65,1215,'Mixed Jordan, regular affine and nonsolvable scalar parameters have the stated exact values.','small')
text(65,1252,'All exceptional zero-weight and repeated-eigenvalue cases are retained.','small')
text(40,1330,'Proof: Proposition8.11, Lemma8.12 and Theorem8.13; full projective images: Theorem8.9.','small')
text(40,1375,'Human source: Lie–Engel III, Chapter6 §§29–31, pp.109–121 (freely accessible original scan).','small')
text(40,1420,'The figure concerns complex matrix algebras under GL₃ conjugacy and connected local subgroup germs.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
