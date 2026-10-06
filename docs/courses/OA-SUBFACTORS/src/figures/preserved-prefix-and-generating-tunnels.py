"""Original map/index diagram. Locators (60.9)–(60.15); no spatial geometry."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parent
out=['<svg xmlns="http://www.w3.org/2000/svg" width="740" height="1180" viewBox="0 0 740 1180"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#365c78"/></marker></defs><rect width="740" height="1180" fill="white"/>']
def text(x,y,s,size=17,color='#17324a',bold=False):
 out.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" font-weight="{"bold" if bold else "normal"}">{escape(s)}</text>')
def rect(x,y,w,h,fill='#eff5fb',stroke='#9eb3c5',radius=8):
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
def arrow(x,y,x2,y2):
 out.append(f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="#365c78" stroke-width="2" marker-end="url(#arrow)"/>')
text(26,39,'Keep the prefix; generate both factors',26,bold=True)
text(26,70,'Exact algebra maps, skipped indices and error bounds',18)
rect(18,94,704,322)
text(36,127,'1. Full compatibility comes from a finite common basis',20,bold=True)
rect(75,163,170,54,'white');text(126,198,'B = ⟨M,e⟩',19)
rect(489,163,170,54,'white');text(563,198,'M',21)
rect(75,293,170,54,'white');text(120,328,'Aₖ = ⟨Nₖ,e⟩',19)
rect(489,293,170,54,'white');text(559,328,'Nₖ',21)
arrow(255,190,479,190);text(359,181,'Φ',22)
arrow(255,320,479,320);text(359,311,'Φ',22)
arrow(160,226,160,283);text(181,259,'Eₖ',20)
arrow(574,226,574,283);text(595,259,'E_Nₖ',18)
text(36,377,'E_Nₖ Φ = Φ Eₖ.  Φ may be nonnormal; all coefficient sums are finite.',17)
text(36,400,'T = Σᵢ aᵢ Eₖ(aᵢ* T), with aᵢ in R. Proof: (60.6)–(60.9).',17)
rect(18,435,704,363,'#eef8f4')
text(36,469,'2. k = 2: the higher step has index a = d³',20,bold=True)
xs=[55,230,405,580]
for x,label in zip(xs,['M = L₋₁','N₂ = L₀','N₅ = L₁','N₈ = L₂']):
 rect(x,500,115,49,'white');text(x+12,532,label,18)
for x in xs[:-1]:
 arrow(x+124,525,x+164,525);text(x+125,491,'⊃',20);text(x+120,575,'index d³',15)
text(36,616,'N₅ ⊂ N₂ ⊂ M is a basic triple. Its Jones projection has E_N₂(g) = d⁻³1.',16)
text(36,650,'Ordinary prefix retained exactly:',18,bold=True)
for x,label in [(55,'N₀'),(145,'N₁'),(235,'N₂')]:
 rect(x,674,65,45,'#d9eee5');text(x+19,703,label,19)
for x in [120,210]:arrow(x+5,697,x+20,697)
arrow(310,697,491,697);text(331,685,'ordinary continuation',15)
rect(505,674,170,45,'white');text(536,703,'last level = U₂',18)
text(36,755,'u ∈ N₂ fixes g₀,g₁ and aligns the final N₈ with U₂. Targets stay fixed.',17)
text(36,781,'The arrows order algebras; their spacing represents no metric geometry.',16)
rect(18,817,704,267,'#fff7ea')
text(36,851,'3. One nested tunnel for a countable dense sequence',20,bold=True)
for y,i,bound,k in [(887,1,'1/2',5),(934,2,'1/4',11),(981,3,'1/8',23)]:
 rect(38,y,64,34,'white');text(53,y+24,f'i = {i}',17)
 targets=['x₁','x₁,x₂','x₁,x₂,x₃'][i-1]
 text(122,y+24,f'retain prior prefix; kᵢ ≥ {k}; test {targets}; error < {bound}',17)
text(36,1044,'Starting at k₀ = 2: kᵢ ≥ 3·2ⁱ − 1. Actual stages may be later.',17)
text(26,1118,'All i ≥ j approximate xⱼ within 2⁻ⁱ; distance to the final closure is zero.',17)
text(26,1150,'Human source: Sorin Popa, DOI 10.1007/BF02392646, §§3.2.4(i), 4.4.',15)
out.append('</svg>')
(R/'preserved-prefix-and-generating-tunnels.svg').write_text('\n'.join(out),encoding='utf-8')
