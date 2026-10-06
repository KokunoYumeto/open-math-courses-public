"""Leaf normalization, branching phase and one-copy fork flip. CC0."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="890" viewBox="0 0 540 890" role="img" aria-labelledby="title desc">',
 '<title id="title">One branching phase remains after tree gauge normalization</title>',
 '<desc id="desc">The root leaf matrix is normalized to one. An edge couples the two endpoint diagonal entries by C_u(v,v)=mu_v/mu_u times the conjugate of C_v(u,u). Four edge-copy phases give local row and column phases with inverse diagonal products at opposite endpoints. Degree-two matrices are forced as z,k;k,minus conjugate z. The triple-point block is X=-a P_u+alpha(1-P_u), with the real part of alpha fixed by delta and t0. Its two distinct conjugate unit-circle choices follow from the positive discriminant (4-delta squared)(delta-t0) squared. On D the phase is plus or minus i; flipping only the tip columns in one graph copy exchanges it. Simultaneously flipping rows and columns leaves the matrix unchanged. Lemmas36.1–36.3, Theorem36.4 and Proposition36.5.</desc>',
 '<rect width="540" height="890" fill="#fbfcff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']
def text(x,y,s,cls='label',anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def box(y,title,lines,height=116):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+29,title,'heading')
    for j,line in enumerate(lines):text(270,y+58+25*j,line,'label')
text(24,33,'Normalize the arms; keep the branch phase','title','start')
box(56,'Start at a leaf, then proceed along the tree',[
    'Root matrix = 1; edge diagonals remain coupled.',
    'Cᵤ(v,v) = (μᵥ/μᵤ) conjugate(Cᵥ(u,u))'])
box(191,'A degree-two vertex is forced',[
    'Cᵥ = [ z  k ; k  −conjugate(z) ],  k > 0',
    'First off-diagonal row/column entries positive.',
    'Parent fixes z.'])
box(326,'The triple point has one remaining unit phase',[
    'X = −a Pᵤ + α(1−Pᵤ);  |α| = 1',
    'Re(α) = (δ²−δt₀−2)/(2a),  a ≠ 0'])
box(461,'The two choices are distinct',[
    '4a² − (δ²−δt₀−2)² = (4−δ²)(δ−t₀)² > 0',
    'Thus α and conjugate(α) are two gauge classes.'])
text(270,616,'On D: equal tips force α = +i or −i','heading')
parts.append('<circle cx="130" cy="726" r="61" fill="none" stroke="#adbacb"/>')
parts.append('<path d="M51 726 H209 M130 649 V803" stroke="#7c9bbd" fill="none"/>')
for y,label in [(665,'+i'),(787,'−i')]:
    parts.append(f'<circle cx="130" cy="{y}" r="6" fill="#276a89"/>')
    text(158,y+6,label,'label')
text(190,753,'Re','small');text(152,648,'Im','small')
text(365,683,'Swap tip columns only:','heading')
text(365,713,'α ↦ −α = conjugate(α)')
text(365,752,'Swap rows and columns:','heading')
text(365,782,'α stays unchanged.')
text(270,844,'One graph-copy flip exchanges the two D classes.','heading')
text(270,874,'All maps preserve the traced grid and Jones cups.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
