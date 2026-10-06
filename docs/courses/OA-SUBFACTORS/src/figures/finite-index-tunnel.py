"""Three exact replacements for finite depth in lesson 29. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="680" viewBox="0 0 540 680" role="img" aria-labelledby="title desc">',
         '<title id="title">A finite-index tunnel gives a generating tunnel</title>',
         '<desc id="desc">Assume the downward relative-commutant closure R is a II1 factor and [M:R]=D is finite. At odd k=2h-1, a skipped Jones projection p makes pRp isomorphic to S_k=R intersection N_k. For the finite relative commutants C_l, the projection onto blocks of size less than q decreases to zero and the sum of minimal weights is at most its trace plus 1/q. Coherent rotations w_(k+1)=w_k v_k, with v_k in N_k, agree on D_k and preserve the factor closure. Prefix approximation and basis transport then prove orbital detection and force the new closure T to equal M.</desc>',
         '<rect width="540" height="680" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,title,lines,height=125):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+29,title,'heading','middle')
    for i,line in enumerate(lines):
        text(270,y+59+25*i,line,'label' if i==0 else 'small','middle')
text(24,34,'A finite-index tunnel is enough','title')
text(24,65,'Hypotheses: R is a II₁ factor; [M : R] = D < ∞.','label')
box(91,'Odd skipped corners give factors',[
    'k = 2h − 1;   Nₖ ⊂ Q = M₋ₕ ⊂ M',
    'p ∈ Dₖ ⊂ R;   pRp = Sₖp;   Sₖ = R ∩ Nₖ',
    'Coefficient recovery: a = dʰ E_Q(pxp).'])
box(237,'Small blocks lose all their trace',[
    'τ(zₗ⁽q⁾) → 0;   Σⱼ tₗ(j) ≤ τ(zₗ⁽q⁾) + 1/q',
    'zₗ⁽q⁾ selects Cₗ blocks with size < q.',
    'First fix q; then let l → ∞; finally let q → ∞.'])
box(383,'Coherent rotations preserve the closure',[
    'wₖ₊₁ = wₖvₖ;   vₖ ∈ Nₖ;   [vₖ, Dₖ] = 0',
    'Ad(wₖ₊₁) and Ad(wₖ) agree on Dₖ.',
    'The induced trace isomorphism makes T a factor.'])
parts.append('<path d="M270 521 V548 M260 538 L270 548 L280 538" fill="none" stroke="#426987" stroke-width="2.5"/>')
box(559,'Basis transport + orbital detection ⇒ T = M',[
    'Lemmas 29.1–29.3; Proposition 29.4; Theorem 29.6.'],height=86)
text(24,671,'No finite-depth hypothesis; all closures use the trace of M.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
