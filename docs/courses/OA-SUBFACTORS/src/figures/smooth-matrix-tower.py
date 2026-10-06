"""Original exact matrix/expectation diagram for M.5."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="630" viewBox="0 0 740 630"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs><rect width="740" height="630" fill="white"/>']
def text(x,y,s,size=17,bold=False):out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb'):out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')
def arrow(x,y,u,v):out.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#365c78" stroke-width="2" marker-end="url(#a)"/>')
text(26,40,'One finite matrix model extends the representation',24,True)
text(26,72,'Partial supports are retained: p = diag(fᵢ); λ = 1/d.',18)
rect(18,94,704,239)
rect(50,129,145,54,'white');text(112,165,'V',22)
rect(397,129,291,54,'white');text(423,165,'D = p Matₙ(U) p',21)
arrow(205,151,387,151);text(283,138,'L',22)
arrow(387,216,205,216);text(280,206,'E₁',21)
text(36,258,'L(v)ᵢⱼ = E(aᵢ* v aⱼ);  E₁(C) = λ Σᵢⱼ aᵢ Cᵢⱼ aⱼ*;  E₁ L = id_V.',17)
text(36,302,'Both maps are normal; L is faithful; E₁ is CP, unital and faithful.',17)
rect(18,352,704,165,'#eef8f4')
text(36,388,'e = ηη*,  ηᵢ = E(aᵢ*),  η*η = 1.   e v e = E(v)e.',18)
text(36,428,'D = span(V e V);   E₁(v e w) = λ v w.',19,True)
text(36,468,'bᵢ = √d aᵢ e;   E₁(bᵢ* bⱼ) = δᵢⱼ fᵢ;   Σᵢ bᵢ bᵢ* = d 1_D.',18)
text(26,555,'Iterate the same normal finite construction, with index d at every step.',17)
text(26,587,'Exact algebra maps and normalization; positions carry no metric geometry.',16)
text(26,617,'Proof: 61.2. Human source: Sorin Popa, DOI 10.1007/BF02392646, §2.2.',15)
out.append('</svg>')
(R/'smooth-matrix-tower.svg').write_text('\n'.join(out),encoding='utf-8')
