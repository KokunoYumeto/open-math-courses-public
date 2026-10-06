"""The positive-cone transport and two normalizations of Proposition 21.5. CC0."""
from pathlib import Path
from html import escape

parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="500" height="460" viewBox="0 0 500 460" role="img" aria-labelledby="title desc">',
         '<title id="title">The dual and the normalized expectation</title>',
         '<desc id="desc">The dual E-prime maps N-prime to M-prime, with identity value c and Jones-projection value one. Conjugation by J identifies their positive cones with M1 and M. The lower map E1 is one over c times that transport, with identity value one and Jones-projection value one over c.</desc>',
         '<rect width="500" height="460" fill="#fbfcff"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:19px;font-weight:bold}.algebra{font-size:23px;font-weight:bold}.label{font-size:16px}.small{font-size:14px}</style>',
         '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#426987"/></marker></defs>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def line(x1,y1,x2,y2,dashed=False):
    parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#426987" stroke-width="2" marker-end="url(#arrow)"'+(' stroke-dasharray="5 5"' if dashed else '')+'/>')
text(24,32,'Two maps, two normalizations','title')
text(24,60,'Assume c = E′(1) &lt; ∞.'.replace('&lt;','<'),'small')
text(80,118,'N′','algebra','middle');text(420,118,'M′','algebra','middle')
line(115,111,381,111);text(250,99,'E′','label','middle')
text(250,153,'E′(1) = c1     E′(e) = 1','label','middle')
line(80,257,80,141,True);line(420,257,420,141,True)
text(95,209,'J(·)J','small');text(360,209,'J(·)J','small')
text(80,285,'M₁','algebra','middle');text(420,285,'M','algebra','middle')
line(115,278,381,278);text(250,262,'E₁ = c⁻¹ Ê','label','middle')
text(250,322,'E₁(1) = 1     E₁(e) = c⁻¹1','label','middle')
parts.append('<line x1="24" y1="349" x2="476" y2="349" stroke="#a4b4c8"/>')
text(24,379,'Ê(x) = J E′(JxJ) J, for x ≥ 0.')
text(24,409,'Vertical arrows identify positive cones.','small')
text(24,437,'Theorem 21.3 and Proposition 21.5.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
