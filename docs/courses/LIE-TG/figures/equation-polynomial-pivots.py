"""Exact order-three affine fibre and symbol pivots of Example 4.33.

GPT-6.1 Sol (OpenAI), CC0 1.0.
"""
from pathlib import Path
from html import escape

parts=[]
def text(x,y,value,size=19,**attrs):
    extra=' '.join(f'{k.replace("_","-")}="{escape(str(v),quote=True)}"' for k,v in attrs.items())
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" {extra}>{escape(value)}</text>')
def box(x,y,w,h,color='#ffffff'):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" stroke="#c4cfdd"/>')

parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="850" viewBox="0 0 1200 850" role="img" aria-labelledby="title desc">
<title id="title">Actual equation coordinates from monic symbol pivots</title>
<desc id="desc">Fix a lower jet of (1+p squared)u_xx=u_xy with f=1+p squared nonzero and q=u_xy. At order three the free variables are a=u_xyy and b=u_yyy. The solved pivots are c=u_xxy=a/f minus 2p q squared/f squared, and d=u_xxx=a/f squared minus 4p q squared/f cubed. The entire affine equation fibre is the plane (d,c,a,b) parametrized by (a,b), with inverse projection to its last two coordinates. All denominators depend only on p. The monic symbol row is t_x squared minus t_x t_y/f; standard degree-three monomials are t_y cubed and t_x t_y squared.</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker></defs>
<rect width="1200" height="850" fill="#f6f8fc"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#17283d">
''')
text(30,39,'Actual equation coordinates from monic symbol pivots',26,font_weight=650)
text(30,74,'(1+p²)uₓₓ = uₓᵧ;   fixed lower jet: p=uₓ, q=uₓᵧ, f=1+p² ≠ 0.',21)
box(25,103,1150,241)
text(47,141,'Degree-three symbol: tₓ² − f⁻¹tₓtᵧ, with tₓ > tᵧ',23,font_weight=600)
nodes=[(65,'tᵧ³','b = uᵧᵧᵧ','free'),(342,'tₓtᵧ²','a = uₓᵧᵧ','free'),
       (619,'tₓ²tᵧ','c = uₓₓᵧ','pivot'),(896,'tₓ³','d = uₓₓₓ','pivot')]
for x,monomial,coordinate,kind in nodes:
    box(x,169,238,120,'#eaf4ed' if kind=='free' else '#edf2fc')
    text(x+119,200,monomial,23,text_anchor='middle')
    text(x+119,233,coordinate,21,text_anchor='middle')
    text(x+119,269,kind,18,text_anchor='middle',fill='#2c6547' if kind=='free' else '#265ba8')
for left,right in [(580,619),(857,896)]:
    parts.append(f'<path d="M{left} 231H{right-7}" stroke="#265ba8" stroke-width="2" marker-end="url(#arrow)"/>')
text(48,321,'Increasing pivot order: solve c from a, then d from c; b remains arbitrary.',20)
box(25,366,1150,286)
text(47,405,'The entire highest equation fibre is an affine plane in four coordinates',23,font_weight=600)
box(54,433,239,161,'#eaf4ed')
text(173,474,'(a,b) ∈ A²',26,text_anchor='middle')
text(173,512,'a = uₓᵧᵧ',21,text_anchor='middle')
text(173,548,'b = uᵧᵧᵧ',21,text_anchor='middle')
parts.append('<path d="M309 490H406" stroke="#265ba8" stroke-width="2" marker-end="url(#arrow)"/>')
text(357,470,'Φ',23,text_anchor='middle',fill='#265ba8')
parts.append('<path d="M406 554H309" stroke="#2c6547" stroke-width="2" marker-end="url(#arrow)"/>')
text(357,582,'π',21,text_anchor='middle',fill='#2c6547')
box(424,433,710,161,'#edf2fc')
text(447,472,'Φ(a,b) = (d,c,a,b)',25)
text(447,512,'c = f⁻¹a − 2p f⁻²q²',24)
text(447,552,'d = f⁻²a − 4p f⁻³q²',24)
text(49,630,'π(d,c,a,b)=(a,b);  π ∘ Φ=id.  Every a,b is allowed; rank dΦ=2.',21,fill='#2c6547')
box(25,674,1150,151)
text(48,710,'One denominator collection at every order',23,font_weight=600)
text(48,746,'Dᵢ(f⁻ʳ) = −r f⁻ʳ⁻¹Dᵢf.  Only powers of f are inverted; f has order one.',22)
text(48,786,'Theorem 4.32: actual raw equations + monic division + whole affine fibres.',21)
parts.append('</g></svg>')
svg='\n'.join(parts)+'\n'

if __name__=='__main__':
    Path(__file__).with_suffix('.svg').write_text(svg,encoding='utf-8',newline='\n')
