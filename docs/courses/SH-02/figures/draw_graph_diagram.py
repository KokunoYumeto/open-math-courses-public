from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent
DEST=HERE;DEST.mkdir(exist_ok=True)
def diagram(mobile):
 w,h=(360,390) if mobile else (940,380)
 x1,x2=(75,259) if mobile else (130,765)
 y1,y2=55,190
 def text(x,y,s,size=23):
  def sub(z):return f'<tspan baseline-shift="sub" font-size=".68em">{z}</tspan>'
  def sup(z):return f'<tspan baseline-shift="super" font-size=".68em">{z}</tspan>'
  s=s.replace('Δ_Y*','Δ'+sub('Y')+sup('*')).replace('Γ_f*','Γ'+sub('f')+sup('*')).replace('Γ_f','Γ'+sub('f')).replace('Δ_Y','Δ'+sub('Y')).replace('id_Y','id'+sub('Y')).replace('f_!','f'+sub('!')).replace(')_!',')'+sub('!'))
  return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}">{s}</text>'
 def arrow(xa,ya,xb,yb):return f'<path d="M{xa},{ya} L{xb},{yb}" fill="none" stroke="#245c75" stroke-width="2" marker-end="url(#arrow)"/>'
 a=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
 '<title id="title">The Cartesian graph square and its proper-support base-change map</title>',
 '<desc id="desc">X maps to X times Y by the graph of f. Its vertical map is f. The right vertical map is f times the identity of Y. The bottom map is the diagonal of Y. This square is Cartesian. Its base-change mate beta identifies diagonal pullback after direct image along f times the identity with direct image along f after graph pullback.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#245c75"/></marker></defs>',
 f'<rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="#f4f8fa"/>',
 '<g fill="#142b3a" font-family="Cambria, Georgia, serif">',text(x1,y1,'X'),text(x2,y1,'X × Y'),text(x1,y2,'Y'),text(x2,y2,'Y × Y'),
 arrow(x1+30,y1-8,x2-51,y1-8),text((x1+x2)/2,y1-20,'Γ_f',18),
 arrow(x1,y1+17,x1,y2-30),text(x1-25,(y1+y2)/2,'f',19),
 arrow(x2,y1+17,x2,y2-30),text(x2+45,(y1+y2)/2,'f × id_Y',14 if mobile else 18),
 arrow(x1+30,y2-8,x2-51,y2-8),text((x1+x2)/2,y2-20,'Δ_Y',18),
 text((x1+x2)/2,235,'Cartesian square (GBT.21)',16 if mobile else 21)]
 if mobile:
  a.extend([text(180,283,'Δ_Y* (f × id_Y)_! (F ⊠ G)',18),arrow(180,296,180,322),text(204,314,'β',18),text(180,354,'f_! Γ_f* (F ⊠ G)',20)])
 else:
  a.extend([text(262,322,'Δ_Y* (f × id_Y)_! (F ⊠ G)',23),arrow(501,315,553,315),text(529,299,'β',21),text(731,322,'f_! Γ_f* (F ⊠ G)',23)])
 a.append('</g></svg>')
 return '\n'.join(a)+'\n'
for mobile,name in [(False,'graph-projection.svg'),(True,'graph-projection-mobile.svg')]:
 (DEST/name).write_text(diagram(mobile),encoding='utf-8')
(DEST/'graph-projection-math.json').write_text(json.dumps({'proof':'SH02-GBT-8','square':'GBT.21','map':'GBT.22 beta for q=Delta_Y, p=f times id_Y, q_prime=Gamma_f, p_prime=f','objects':['X','X times Y','Y','Y times Y'],'hypotheses':['All spaces locally compact Hausdorff','f continuous','C and D stable bicomplete','coefficient target is A_(X times Y) tensor (C tensor D), without assuming C tensor D complete'],'interpretation':'Commutative diagram of actual maps; positions are schematic and assert no geometric scale. Both versions show the same Cartesian square and the same beta.','sources':['Lurie HTT 7.3.1.18','Volpe published 6.9,6.13,6.14'],'licence':'CC0 1.0'},indent=2)+'\n',encoding='utf-8')
