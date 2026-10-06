"""Exact conditional map diagram for 61.1/61.6/61.7."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="920" viewBox="0 0 740 920"><defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs><rect width="740" height="920" fill="white"/>']
def text(x,y,s,size=17,bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="#17324a" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb'):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#9eb3c5"/>')
def arrow(x,y,u,v):
 out.append(f'<line x1="{x}" y1="{y}" x2="{u}" y2="{v}" stroke="#365c78" stroke-width="2" marker-end="url(#a)"/>')
text(26,40,'Compress first, then use the tracial tower',25,True)
text(26,72,'Conditional hypotheses: T injective; (M′ ∩ T)′ ∩ T = M.',18)
rect(18,94,704,333)
text(36,130,'1. Keep the original tracial GNS space explicit',20,True)
rect(45,167,100,56,'white');text(87,201,'V',22)
rect(279,167,184,56,'white');text(307,201,'B(L²(T))',21)
rect(593,167,100,56,'white');text(631,201,'T',22)
arrow(155,195,269,195);text(177,176,'p π(·) p',18)
arrow(473,195,583,195);text(518,176,'Θ',22)
text(36,267,'H₀ = closure of π(⋃ⱼ Mⱼ)ξ = L²(T).  p commutes with every Mⱼ.',17)
text(36,303,'F(v) = Θ(pπ(v)p) lies in T and commutes with M′ ∩ T.',17)
text(36,339,'The assumed bicommutant identity gives F(V) ⊂ M.',18)
text(36,375,'Smoothness gives [F(U),e₀] = 0; Markov faithfulness gives F(U) ⊂ N.',17)
text(36,409,'Θ and F may be singular. No normal map of an infinite represented tower.',16)
rect(18,446,704,191,'#eef8f4')
text(36,481,'2. Finite row formula gives full expectation compatibility',20,True)
text(36,521,'T₀ = Σᵢ aᵢ bᵢ,   bᵢ = E(aᵢ* T₀),   cᵢ = E_N(aᵢ).',18)
text(36,558,'E(T₀) = Σᵢ cᵢ bᵢ;   E_N F(T₀) = Σᵢ cᵢ F(bᵢ) = F(E(T₀)).',18)
text(36,605,'The state τF is M-central and E-compatible. Proof: 61.1, 61.6.',17)
rect(18,656,704,179,'#fff7ea')
text(36,691,'3. The cluster point fixes every tracial tower element',20,True)
text(36,731,'qⱼ projects L²(T) onto L²(Mⱼ); βⱼ projects B(L²(Mⱼ)) onto Mⱼ.',17)
text(36,769,'Θⱼ(X) = βⱼ(qⱼ X qⱼ);   Θⱼ(x) = E_Mⱼ(x) → x for every x ∈ T.',17)
text(36,807,'Take a point-ultraweak cluster only after this exact identity. Proof: 61.7.',17)
text(26,870,'Conditional proof only: full nonextremal bicommutant input remains unproved.',16)
text(26,901,'Human source: Sorin Popa, DOI 10.1007/BF02392646, §4.5, pp. 223–225.',15)
out.append('</svg>')
(R/'smooth-representations-and-tower-compression.svg').write_text('\n'.join(out),encoding='utf-8')
