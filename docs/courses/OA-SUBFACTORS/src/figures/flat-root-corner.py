"""Root-returning compression and the flat realization proof. CC0."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="700" viewBox="0 0 540 700" role="img" aria-labelledby="title desc">',
       '<title id="title">A returning path bounds the relative commutant</title>',
       '<desc id="desc">Compactness puts N prime intersection M_k inside A_(k+1,m0). A horizontal path xi of even length m0 returning to the root defines projection p with trace delta to minus m0. Compression is injective on the relative commutant because N is a factor. In horizontal-first path order the corner leaves exactly the vertical paths of length k+1 from the root, so its dimension is at most dim A_(k+1,0). Flatness includes that whole algebra in the commutant, forcing equality, the actual rooted principal graph Gamma and index delta squared.</desc>',
       '<rect width="540" height="700" fill="#fbfcff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,title,lines,height=111):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+28,title,'heading','middle')
    for i,line in enumerate(lines):text(270,y+57+25*i,line,'label' if i==0 else 'small','middle')
text(24,33,'Flat paths recover the principal graph','title')
box(56,'Compactness gives finite location',[
    'N′ ∩ Mₖ ⊂ Aₖ₊₁,ₘ₀',
    'Choose even m₀ with full path support.'])
parts.append('<rect x="24" y="185" width="492" height="157" rx="8" fill="#fff8e9" stroke="#b6a070"/>')
text(270,214,'Horizontal-first order: ξ followed by α','heading','middle')
for x,v in [(55,'*'),(132,'⋯'),(231,'*'),(327,'⋯'),(458,'a')]:text(x,258,v,'heading','middle')
parts.append('<path d="M71 253 H110 M151 253 H208 M254 253 H306 M350 253 H436" stroke="#426987" stroke-width="2"/>')
text(143,282,'ξ: m₀ horizontal steps','small','middle')
text(370,282,'α: k+1 vertical steps','small','middle')
text(270,318,'p = [ξ,ξ];  ξ returns to *;  τ(p) = δ⁻ᵐ⁰','label','middle')
box(360,'The corner leaves the root-based vertical paths',[
    'p Aₖ₊₁,ₘ₀ p ≅ Aₖ₊₁,₀',
    'Compression x ↦ pxp is injective on N′ ∩ Mₖ.'])
box(489,'Two dimension bounds become equality',[
    'dim(N′ ∩ Mₖ) ≤ dim Aₖ₊₁,₀',
    'Flatness: Aₖ₊₁,₀ ⊂ N′ ∩ Mₖ.'])
text(270,634,'N′ ∩ Mₖ = Aₖ₊₁,₀ in the actual tower.','heading','middle')
text(270,664,'Rooted graph Γ; index δ²; depth r.','label','middle')
text(24,694,'Lemma 33.1 and Theorem 33.2.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
