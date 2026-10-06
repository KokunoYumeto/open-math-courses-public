"""Original reproducible block schematic, with exact dimension and trace labels."""
from pathlib import Path
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="1350" viewBox="0 0 740 1350">',
'<rect width="740" height="1350" fill="#f7fafc"/>',
'<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#365d75"/></marker></defs>']
def text(x,y,s,size=20,bold=False):
 parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="#133c53">{escape(s)}</text>')
def box(x,y,w,h,color):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#9bb8c9"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#365d75" stroke-width="3" marker-end="url(#arrow)"/>')
text(370,37,'Full support from a factorial larger core',27,True)
text(370,72,'The smaller canonical center may move under M.',20)
box(20,96,700,228,'#eaf3f8')
text(370,131,'1 · Transfer through the common cup-factor basis',23,True)
text(200,177,'z ∈ Z(A)',24,True)
text(543,177,'I(z) = d ν(z) · 1 ∈ Z(B)',20,True)
arrow(282,172,385,172)
text(370,218,'I(z) = Σ aᵢ z aᵢ*;  B is a factor because R is a factor.',19)
text(370,258,'e A e = S e;  e B e = R e;  ν(z) = Tr(e z).',20)
text(370,294,'This scalar identity does not assert that Z(A) commutes with M.',17)
box(20,345,700,245,'#e8f4ed')
text(370,382,'2 · Balance the central dimension with a finite test set',22,True)
text(370,426,'h = n · 1 + f;  τ(f) = d − n.',23,True)
text(370,470,'Average h with powers of v ∈ K₁:  ‖h̄ − d · 1‖ ≤ 1/L.',20)
text(370,512,'Include the basis unitaries and v powers in the Følner test set.',18)
text(370,554,'ζ = C_A(p), c = Tr(p):  ‖ζ − c · 1‖₁ &lt; σ c.',22,True)
box(20,612,700,448,'#fdf0e6')
text(370,650,'3 · Exact example: trim excess and fill deficits',23,True)
text(370,686,'Center weights 1/2, 1/2 · fourfold dimension scaling',19)
box(65,709,270,100,'#e6b69b');box(405,709,270,100,'#9ec5d6')
text(200,745,'Left dimension: 36',23,True);text(540,745,'Right dimension: 32',23,True)
text(200,780,'Delete dimension 2',20);text(540,780,'Add dimension 2',20)
arrow(200,814,200,865);arrow(540,814,540,865)
box(65,873,270,72,'#b1d4bd');box(405,873,270,72,'#b1d4bd')
text(200,918,'Target dimension: 34',22,True)
text(540,918,'Target dimension: 34',22,True)
text(370,984,'Deleted scalar trace 1 + added scalar trace 1 = 2.',20)
text(370,1025,'C_A(q) = 34 · 1;  Tr(q) = 34;  ‖p − q‖₂² / 34 = 1/17.',19,True)
box(20,1080,700,179,'#eeeff9')
text(370,1117,'4 · Integer rounding retains the entire Jones support',22,True)
text(370,1160,'C(q) = k · 1 ⇒ q = sum of k pieces, each equivalent to e_R₀.',19)
text(370,1200,'Defect / √k &lt; (√2 + 1) ε₀ / 4 &lt; ε.',23,True)
text(370,1238,'This supplies BF₁, then both local forms and the every-core converse.',17)
text(370,1294,'Proof: 58.1–58.7. Lower panel: exact support arithmetic, Example 58.9.',17)
text(370,1325,'Block schematic; no spatial or small-error instance asserted. Original · CC0.',16)
parts.append('</svg>')
# Escape handles literal comparison characters once; these labels need actual characters.
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts).replace('&amp;lt;','&lt;')+'\n',encoding='utf-8')
