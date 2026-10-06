"""Two-root reflection, exact split weights and the fixed-grid proof. CC0."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="850" viewBox="0 0 540 850" role="img" aria-labelledby="title desc">',
 '<title id="title">Folding two path roots into a fork</title>',
 '<desc id="desc">The example r=4 folds the reflection of A9, vertices zero through eight, into D6 with chain zero through three and tips plus and minus. The middle vertex four splits into the two reflection characters. General weights are nu_j=mu_j and nu_plus=nu_minus=mu_r/2. The parent starting roots each have trace one half. The fixed grid has an actual hyperfinite factor inclusion of index delta squared. Terminal commutation makes the root-return corner dimension bound an equality, yielding principal graph D_(r+2) and depth r. All assertions refer to Propositions34.1,34.3 and Theorems34.2,34.4.</desc>',
 '<rect width="540" height="850" fill="#fbfcff"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}.edge{stroke:#426987;stroke-width:2}</style>']
def text(x,y,s,cls='label',anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(s)}</text>')
def node(x,y,label,color='#edf3fb'):
    parts.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{color}" stroke="#426987"/>')
    text(x,y+5,label,'small')
def box(y,title,lines,height=110):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+27,title,'heading')
    for j,line in enumerate(lines):text(270,y+54+24*j,line,'small')
text(24,32,'Two roots fold into one fork','title','start')
text(270,66,'Example r = 4: the parent A₉','heading')
parts.append('<path d="M54 110 H486" class="edge"/>')
for j in range(9):node(54+54*j,110,str(j),'#fff1cc' if j==4 else '#e3eef9')
text(54,147,'root L','small');text(486,147,'root R','small')
text(270,177,'σ(j) = 2r − j;  τ(p₀) = τ(p₂ᵣ) = ½')
parts.append('<path d="M264 190 V213 L258 205 M264 213 L270 205" class="edge" fill="none"/>')
text(270,244,'The fixed graph D₆','heading')
parts.append('<path d="M60 321 H330 L445 278 M330 321 L445 366" class="edge" fill="none"/>')
for j in range(4):node(60+90*j,321,str(j))
node(445,278,'+','#fff1cc');node(445,366,'−','#fff1cc')
text(60,359,'root','small')
text(175,399,'chain weight νⱼ = μⱼ','small')
text(420,399,'each tip: μᵣ/2','small')
box(420,'Middle characters are two rank-one directions',[
    'ξ± = (ξL ± ξR)/√2;  ρ± = [ξ±, ξ±]',
    'Trace of each tip projection: μᵣ/(2δʳ).'])
box(547,'The fixed squares construct the factor pair',[
    'Fixed pair: N^σ ⊂ M^σ',
    'Common Jones cups; index δ²; δ = 2 cos(π/(2r+2)).'])
box(674,'Terminal commutation recovers the graph',[
    '[ρᵥ, ρₕ] = 0 ⇒ fixed axes commute',
    'Root-return q: τ(q) = δ⁻ᵐ⁰; qFₖ₊₁,ₘ₀q ≅ Fₖ₊₁,₀',
    'Injective compression + flatness gives equality.'],height=132)
text(270,834,'Principal graph Dᵣ₊₂; depth r.  Theorems 34.2, 34.4.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
