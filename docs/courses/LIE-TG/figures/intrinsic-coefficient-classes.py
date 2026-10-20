from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
def text(x,y,s,size=22,weight='normal',fill='#203c50'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(s)}</text>'
def rect(x,y,w,h,fill):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#c7d4de"/>'
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="920" viewBox="0 0 1200 920" role="img" aria-labelledby="title desc">',
 '<title id="title">Intrinsic fibre rationality depends on the base</title>',
 '<desc id="desc">The intrinsic presentation has invariant coordinates I j equals exp minus p times w j. The original derivative rational invariant field consists of the ratios w j over w 2. In the slice x equals u equals w equals p equals z equals zero, the exact points w 2,w 3 equals one,one and two,two have equal ratio but different intrinsic invariant coordinates and different H orbits.</desc>',
 '<rect width="1200" height="920" fill="#fbfcfe"/><g font-family="DejaVu Sans,Arial,sans-serif">',
 text(30,42,'An intrinsic action: the base fixes the rational coefficient class',26,'bold'),
 rect(25,65,1150,255,'#edf3fb'),
 text(45,105,'Equation uₓₓ=0; free function w(x).  Intrinsic base M′=E¹.',24,'bold'),
 text(45,146,'p=uₓ,  z=wₓ,  b=u−px.   On M′: bₓ=pₓ=0,  wₓ=z.',23),
 text(45,189,'x′=x+s,  b′=b+h,  p′=p+a,  z′=eᵃz+c,  w′=eᵃw+cx+d.',23),
 text(45,232,'Iⱼ=e⁻ᵖwⱼ (j≥2),   DIⱼ=Iⱼ₊₁.   All fixed-point jet groups are trivial.',23),
 text(45,278,'In (x,u,w), u′=u+ax+sp+as+h depends on the derivative p when s≠0.',22),
 rect(25,340,555,440,'#f2f8f5'),
 text(45,380,'Exact original third-order slice',24,'bold'),
 text(45,416,'x=u=w=p=z=0;  w₂≠0',21),
 '<path d="M90 720 L435 720 M90 720 L90 450" stroke="#355668" stroke-width="2" fill="none"/>',
 text(445,727,'w₂',23),text(62,455,'w₃',23),
 '<path d="M90 720 L340 470" stroke="#738b9a" stroke-width="2" stroke-dasharray="7 7"/>',
 text(310,505,'r₃=1',22),
 '<circle cx="180" cy="630" r="7" fill="#187e75"/><circle cx="270" cy="540" r="7" fill="#a44f2a"/>',
 '<path d="M180 720 L180 630 L90 630 M270 720 L270 540 L90 540" stroke="#b7c7d0" stroke-width="1" fill="none"/>',
 text(171,749,'1',19),text(261,749,'2',19),text(66,637,'1',19),text(66,547,'2',19),
 text(193,655,'P=(1,1)',20,fill='#187e75'),text(282,563,'Q=(2,2)',20,fill='#a44f2a'),
 rect(605,340,570,440,'#fff6eb'),
 text(627,380,'Two different invariant fields',24,'bold'),
 text(627,427,'Intrinsic S² over M′:',23,'bold'),
 text(627,464,'ℝ(I₂,I₃),   q₂(P)=(1,1),',23),
 text(627,501,'q₂(Q)=(2,2).  Full H-orbits differ.',23),
 text(627,555,'Original derivative-rational class:',23,'bold'),
 text(627,593,'ℝ(r₃),  r₃=w₃/w₂.  Both values are 1.',22),
 text(627,639,'δ=∂ₚ+t∂ₜ on ℝ(p,t,r₃),  t=w₂.',22),
 text(627,676,'Its rational constants are ℝ(r₃).',22),
 text(627,723,'The dashed ray is not one H-orbit.',22,'bold'),
 text(45,820,'Example 4.41: full normalization and affine quotient tower, (4.109)–(4.111).',22),
 text(45,856,'Lemma 4.42 and Proposition 4.43: the rational constant field and failure of orbit separation.',21),
 text(45,895,'Scope context: Kruglikov–Lychagin, arXiv:1111.5480v3 §0.1.  GPT-6.1 Sol (OpenAI). CC0 1.0.',17),
 '</g></svg>']
svg='\n'.join(parts)+'\n'
if __name__=='__main__':
    (OUT/'intrinsic-coefficient-classes.svg').write_bytes(svg.encode('utf-8'))
    print(str(OUT/'intrinsic-coefficient-classes.svg'))
