"""Reproduce Figure53.1: canonical columns, central cut and right Gram inverse."""
from pathlib import Path
from html import escape
OUT=Path(__file__).with_suffix('.svg')
parts=[
 '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1260" viewBox="0 0 640 1260" role="img" aria-labelledby="title desc">',
 '<title id="title">Bounded frames preserve a central support</title>',
 '<desc id="desc">A rounded projection yields bounded canonical columns and L2 vectors. The central spectral cut of a finite-stage expectation yields an exact vector Gram matrix. After fixing the stage, bounded approximation and a right inverse square root preserve that same central support. Uniform column errors and finite-stage constants are used in their respective order.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
 '<rect width="640" height="1260" fill="#f9fcfe"/>']
def text(y,s,size=20,color='#163c50',weight='normal'):
 parts.append(f'<text x="320" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="middle" font-weight="{weight}">{escape(s)}</text>')
def box(y,h,title,lines,fill='#eaf3f8'):
 parts.append(f'<rect x="30" y="{y}" width="580" height="{h}" rx="8" fill="{fill}" stroke="#6b96ad"/>')
 text(y+31,title,23,weight='bold')
 for j,s in enumerate(lines):text(y+64+30*j,s,20)
def arrow(y1,y2):
 parts.append(f'<line x1="320" y1="{y1}" x2="320" y2="{y2}" stroke="#315b70" stroke-width="2" marker-end="url(#arrow)"/>')
text(36,'One support through all normalizations',26,weight='bold')
text(68,'Aₘ = Nₘ′ ∩ M;  Bₘ = Nₘ′ ∩ N',21)
box(92,150,'1 · Rounded projection in ⟨N, e_R⟩',[
 'p = Σᵢ vᵢvᵢ*;   vᵢ* vⱼ = δᵢⱼ e_R z',
 'z ∈ Z(S), z ≠ 0;   Tr(p) = k τ(z)',
 'ξᵢ = vᵢ 1̂ ∈ L²(N);  ‖vᵢ‖ = 1'])
arrow(248,280)
box(290,190,'2 · Central spectral cut at a finite stage',[
 'h = E_Bₘ(z) ∈ Z(Bₘ)',
 'f = 1_[1−δ,1](h) ∈ Z(Bₘ)',
 'r = f h^(−½), inverse only on f',
 'ζᵢ = ξᵢ r;   E_Aₘ(ζᵢ* ζⱼ) = δᵢⱼ f'])
text(515,'‖f − z‖₂ ≤ δ⁻¹ ‖h − z‖₂ → 0',21)
text(548,'Columns give errors uniform in m · (53.11), (53.27)',18)
arrow(564,596)
box(606,115,'3 · Choose δ, then m, then FIX m',[
 'Control support loss and all unitary energies.',
 'Only now use the finite constant C_Aₘ.'],'#e5f1e7')
arrow(727,760)
box(770,183,'4 · Bounded row and its right Gram inverse',[
 'Y = (y₁,…,yₖ),  yᵢ ∈ Nf',
 'G = (E_Aₘ(yᵢ* yⱼ)) ∈ Mₖ(fBₘf)',
 '‖G − Iₖf‖ < ½;   a = Y G^(−½)',
 'aᵢ ∈ Nf;   E_Aₘ(aᵢ* aⱼ) = δᵢⱼ f'])
text(990,'The central projection f stays EXACTLY the same.',21,weight='bold')
text(1023,'Finite-stage coefficient errors now tend to zero.',19)
parts.append('<line x1="30" y1="1050" x2="610" y2="1050" stroke="#6b96ad"/>')
text(1084,'Why preserving support matters',23,'#713d26','bold')
text(1119,'In M₁₀₀, 1 − E₁₁ has trace 0.99 but is noncentral.',18,'#713d26')
text(1150,'A large new support alone does not recover centrality.',18,'#713d26')
text(1194,'Input existence for general nonfactor cores remains separate.',17)
text(1230,'Proof: 53.3–53.5 · Popa, Corollary 4.2.3, pp. 215–216',17)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT)
