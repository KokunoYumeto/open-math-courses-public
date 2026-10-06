"""Original reproducible diagram for 70.1–70.4; coordinates are schematic."""
from pathlib import Path
from html import escape
W,H=900,1200
items=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
'<rect width="900" height="1200" fill="#f6f8fb"/>',
'<style>text{font-family:Arial,sans-serif;font-size:20px;fill:#18364c}.title{font-size:27px;font-weight:bold}.head{font-size:23px;font-weight:bold}.math{font-family:Georgia,serif;font-size:25px}.small{font-size:18px}.edge{stroke:#315e78;stroke-width:2.5;fill:none}</style>']
def text(x,y,value,cls=''):
    items.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(value)}</text>')
def panel(y,h,title):
    items.append(f'<rect x="25" y="{y}" width="850" height="{h}" rx="14" fill="white" stroke="#a9bdcc"/>')
    text(47,y+37,title,'head')
def box(x,y,w,h,label):
    items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#e4eff7" stroke="#7795aa"/>')
    text(x+15,y+35,label,'math')
text(34,42,'Retain the projection in joint central transfer','title')
text(34,77,'General core estimates and an exact finite matrix example.','small')
panel(99,315,'1. Different densities have different roles  [70.1–70.6]')
box(50,159,355,63,'ζ = C_A(p)     smaller dimension')
box(445,159,380,63,'β = P₀ζ       larger dimension')
box(50,249,355,63,'γₚ :  τ(γₚt) = Tr(p x g)')
box(445,249,380,63,'ρₚ = γₚ / (dκ)     joint density')
text(51,350,'ζ ≤ γₚ ≤ b_d ζ       and       ‖ρₚ − β‖₁ ≤ εₚ Tr(p)','math')
text(51,387,'The estimate does not identify ρₚ with ζ. No joint g → h substitution.','small')
panel(435,300,'2. Central cuts split basis flow exactly  [70.7–70.14]')
box(50,496,775,65,'d Tr(p) ℬₚ(Z) = Fₚ(Z) + Λₚ(Z)')
text(54,603,'Fₚ:  sum ‖qᵣ aᵢ qⱼ‖₂² over r ≠ j  — internal mixing','math')
text(54,649,'Λₚ: sum ‖qᵣ aᵢ (1 − p) zⱼ‖₂²  — leakage','math')
text(54,697,'Λₚ ≤ sum ‖[p,aᵢ]‖₂². Small scalar boundary controls both terms.','small')
panel(756,330,'3. Exact example: A = Mat₂ ⊕ Mat₂ ⊂ Mat₄  [70.21]')
text(50,823,'Selected coordinates of p = diag(I₂,e₁₁); Tr = Tr₄/2.','small')
for x,label,sel in [(83,'1a',True),(255,'1b',True),(550,'2a',True),(722,'2b',False)]:
    items.append(f'<circle cx="{x}" cy="900" r="27" fill="{"#d9eaf5" if sel else "#fff"}" stroke="#315e78" stroke-width="2"/>')
    text(x-13,908,label,'small')
items.append('<path d="M83 873 Q316 807 550 873 M255 927 Q490 985 722 927" class="edge"/>')
text(240,864,'V swaps 1a ↔ 2a','small')
text(329,984,'V swaps 1b ↔ 2b','small')
text(52,1030,'c = 3/2;  ζ = (2,1);  β = 3/2;  γₚ = 2ζ','math')
text(52,1070,'ℬₚ = 1/2;  Fₚ = 1;  Λₚ = 1/2;  dcℬₚ = 3/2','math')
text(35,1127,'Schematic layout; this matrix model is not an asserted Jones core.','small')
text(35,1161,'Proof locators 70.1–70.21. Problem: Popa, Theorem 4.2.2, pp. 213–214.','small')
items.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(items)+'\n',encoding='utf-8')
