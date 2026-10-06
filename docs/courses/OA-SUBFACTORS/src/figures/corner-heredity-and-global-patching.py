"""Original exact trace/support schematic; proof locators (59.1)–(59.8), (59.13)–(59.18)."""
from pathlib import Path
from html import escape
from math import sqrt
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="1470" viewBox="0 0 740 1470"><rect width="740" height="1470" fill="white"/>']
def text(x,y,s,size=17,color='#17324a',bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill,stroke='#9eb3c5',radius=0):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
text(26,40,'Retain a projection; patch the whole inclusion',25,bold=True)
text(26,70,'Exact trace coordinates and orthogonal operator blocks',18)
rect(18,94,704,368,'#eff5fb',radius=10)
text(36,128,'1. An irrational trace fits in one shrinking residual cell',20,bold=True)
text(36,157,'t = √2/2.  Filled binary cells are retained at every later level.',17)
left,width=145,530
for j,b,y in [(1,1,192),(2,2,265),(3,5,338)]:
 n=2**j;cell=width/n
 text(36,y+26,f'j = {j}',18)
 for i in range(n):rect(left+i*cell,y,cell,36,'#3a749b' if i<b else '#fff')
 rect(left+b*cell,y,(sqrt(2)/2-b/n)*width,36,'#dd9f43')
 out.append(f'<rect x="{left+b*cell}" y="{y}" width="{cell}" height="36" fill="none" stroke="#bb7326" stroke-width="3"/>')
 text(left,y+59,f'τ(pⱼ) = {b}/{n};   residual cell trace = 1/{n}',17)
text(36,421,'Blue: full cells. Gold: residual trace. Border: its containing cell.',16)
text(36,447,'Trace-coordinate schematic; p − pⱼ is a projection, ||p − pⱼ||₂² ≤ 2⁻ʲ.',16)
rect(18,481,704,451,'#eef8f4',radius=10)
text(36,516,'2. Left and right compression give two normalizations',20,bold=True)
text(36,548,'H = L²(M₆); rank(p) = 3; t = 1/2. Operator prototype only.',17)
size=37;gx,gy=46,594
for i in range(6):
 for j in range(6):
  rect(gx+j*size,gy+i*size,size,size,'#509f90' if i<3 and j<3 else '#fff')
  if i==j:
   out.append(f'<circle cx="{gx+j*size+size/2}" cy="{gy+i*size+size/2}" r="5" fill="#b26527"/>')
text(334,602,'q = Lₚ ρ(p): 9 of 36 cells',18,bold=True)
text(334,639,'normalized Hilbert trace(q) = 1/4',17)
text(334,676,'q e q has eigenvalue 1/2',18)
text(334,713,'eₚ = 2 q e q is a projection',18)
text(334,750,'ordinary Hilbert trace(eₚ) = 1',17)
text(334,787,'e projects onto the identity vector.',16)
text(36,852,'General corner: φ₁(q) = t²;  eₚ = t⁻¹ q e q;  canonical Tr(eₚ) = 1.',17)
text(36,886,'The green square is qH. Brown diagonal dots support the identity vector.',16)
text(36,913,'The finite prototype illustrates the formulas; it is not a proper II₁ pair.',16)
rect(18,951,704,432,'#fff7ea',radius=10)
text(36,987,'3. A new local block adds an orthogonal error',20,bold=True)
bs=65;px,py=63,1055
for i in range(3):
 for j in range(3):
  color='#729bbb' if i==0 or j==0 else '#69aa97' if i==1 or j==1 else '#fff'
  rect(px+j*bs,py+i*bs,bs,bs,color)
for i,label in enumerate(['S','s','f−s']):text(px+i*bs+16,py-15,label,18);text(24,py+i*bs+39,label,16)
text(302,1068,'Blue: F(S), with zero f–f block',17)
text(302,1103,'Green: G(s), supported inside f',17)
text(302,1138,'White: remaining (f−s)–(f−s) block',16)
text(302,1180,'⟨F(S), G(s)⟩₂ = 0',20,bold=True)
text(36,1284,'||Gₛ||₂² = ||sys − a||₂² + ||[fyf,s]||₂² < 2δ²τ(s).',18)
text(36,1322,'Maximality fills the unit; a finite selection leaves a small trace tail.',17)
text(36,1358,'Both row and column labels are exact projections; sizes are schematic.',16)
text(26,1416,'Proof locators: (59.1)–(59.8), (59.13)–(59.18). Reproducible SVG source retained.',15)
text(26,1447,'Human source: Sorin Popa, DOI 10.1007/BF02392646, §§3.2.4(ii), 4.4.',15)
out.append('</svg>')
(R/'corner-heredity-and-global-patching.svg').write_text('\n'.join(out),encoding='utf-8')
