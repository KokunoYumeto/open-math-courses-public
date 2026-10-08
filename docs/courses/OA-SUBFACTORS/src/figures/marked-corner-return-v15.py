from pathlib import Path
from html import escape

owned = Path(__file__).resolve().parent
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1320" height="1080" viewBox="0 0 1320 1080">']
parts.append('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#43536a"/></marker></defs>')
parts.append('<title>Actual selected-cell approximate-return obstruction and exact whole-family correction</title>')
parts.append('<desc>The same physical diagonal algebra fixes the central expectation in every corner core. Weyl averaging obstructs every finite unital corner stage. The selected whole-stage family still completes exactly through its five-adic residual trace certificate. Proof locators MR.4–MR.32.</desc>')
parts.append('<rect width="1320" height="1080" fill="#f7f9fc"/>')
def box(x,y,w,h,fill="#ffffff",stroke="#cad3df"):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
def txt(x,y,text,size=24,fill="#162b45",weight="normal"):
    parts.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans, Arial, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}">{escape(text)}</text>')
def arrow(x1,y1,x2,y2,color="#43536a"):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3" marker-end="url(#arrow)"/>')

txt(40,48,"An actual good cell blocks every unital corner-stage return",29,weight="bold")
txt(40,84,"Index 25 lamplighter inclusion · all-smooth amenability · fixed physical targets",23)

box(40,112,1240,252)
txt(64,150,"1. The first physical commutant fixes the center data in every corner",25,weight="bold")
for i in range(5):
    x=64+240*i
    box(x,174,216,86,"#e6eefb")
    txt(x+14,203,f"d{i} = p q{i}",24)
    txt(x+14,229,"physical τp(di) = 1/5",15)
    txt(x+14,250,"dual τp(di) = 1/5",15)
txt(66,292,"Central contraction zT in every ordinary corner core:  E(pA0)(zT) = Σ vi di",23)
txt(66,332,"v0 = h− > 0,  v1 = −h− ;  τp(zT) = h+ ;  ||p z0 − h+ p||²₂,p ≥ 2 h−² / 5",22)

box(40,374,600,238)
txt(64,410,"2. Exact Weyl average",25,weight="bold")
txt(64,453,"Fp ≅ Mat5, with the same d0,…,d4",23)
txt(64,492,"W = {SᵃDᵇ : 0 ≤ a,b < 5}",23)
txt(64,534,"mean ||[u,zT]||²₂,p ≥ 4 h−² / 5",23)
txt(64,574,"Every finite corner stage L: max dist₂,p(u,L) ≥ c",20)
box(680,374,600,238)
txt(704,410,"3. Actual whole-stage selection",25,weight="bold")
txt(704,453,"76.2–76.3 select p ∈ Nk;  t = τ(p) > 0",23)
txt(704,494,"G = p (Nh′ ∩ M) p, after the given prefix",23)
txt(704,534,"Polar correction: δ = c/400",23)
txt(704,574,"Fixed yu = EG(u):  ||u − yu||₂,p < c/4",22)
arrow(640,490,678,490)

box(40,644,1240,166,"#fff1ec","#ddb6a9")
txt(64,682,"4. The proposed return fails with its original physical budget",25,weight="bold")
txt(64,724,"Any ordinary finite corner chain, at any length: max ||yu − EL(yu)||₂ > (3c/4) √t",23)
txt(64,765,"ε = c √t;  ε0 = ε/8;  old error = 0;  ε0 + max (Σ δi(y)²)½ > 7ε/8 > ε/2",23)
arrow(340,614,340,642)
arrow(980,614,980,642)

box(40,842,1240,173,"#e9f6f0","#9bbdac")
txt(64,880,"5. The full family still returns exactly in this actual model",25,weight="bold")
txt(64,923,"Retain p,G and every other good block; choose τ(f) < ε²/16.  Y ⊂ G ⊂ P0.",23)
txt(64,964,"τ(f) ∈ ℤ[1/5] gives a new finite origin for f.  P0 ⊂ P*;  EP*(y) = y.",23)
txt(64,998,"Both expectation rows, physical/dual trace restrictions and prescribed cup operators are preserved.",19)
txt(42,1049,"c = h−/√5 > 0.  Norms use τp = τ/t.  Boxes are schematic; no area denotes trace or capacity.",19)
parts.append('</svg>')
svg = owned/"marked-corner-return-v15.svg"
svg.write_text("\n".join(parts), encoding="utf-8")
try:
    import cairosvg
    cairosvg.svg2png(url=str(svg), write_to=str(owned/"marked-corner-return-v15.png"))
    print("SVG and PNG rendered")
except ImportError:
    import shutil, subprocess
    renderer = shutil.which("magick")
    if renderer:
        subprocess.run([renderer, str(svg), str(owned/"marked-corner-return-v15.png")], check=True, capture_output=True)
        print("SVG and PNG rendered with ImageMagick")
    else:
        print("SVG written; no PNG renderer available")
