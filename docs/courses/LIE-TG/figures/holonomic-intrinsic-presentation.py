from pathlib import Path
from html import escape
OUT=Path(__file__).resolve().parent
def text(x,y,s,size=23,weight='normal',fill='#203c50'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(s)}</text>'
def rect(x,y,w,h,fill):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#c4d3dd"/>'
def arrow(x1,y1,x2,y2):return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="#315c95" stroke-width="2.5" marker-end="url(#arrow)"/>'
def indexed(x,y,base,index):return f'<text x="{x}" y="{y}" font-size="23" fill="#203c50">{escape(base)}<tspan baseline-shift="sub" font-size="16">{escape(index)}</tspan></text>'
def begin(title,desc,height):return ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="'+str(height)+'" viewBox="0 0 1200 '+str(height)+'" role="img" aria-labelledby="title desc">',
    '<title id="title">'+escape(title)+'</title><desc id="desc">'+escape(desc)+'</desc>',
    '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#315c95" stroke-width="1.5"/></marker></defs>',
    '<rect width="1200" height="'+str(height)+'" fill="#fbfcfe"/><g font-family="DejaVu Sans,Arial,sans-serif">']
parts=begin('A holonomic presentation has one exact order shift',
    'The fixed intrinsic base is N equals E q. The compatible holonomic maps identify E q plus L and E q plus L plus k with intrinsic S L and S L plus k. Derivative beta of v alpha equals u alpha plus beta. Both rational-low polynomial-high classes are relative to N, with cutoffs L and q plus L. The contact-map inset has curvature a mapped to minus one over a on a nonzero domain.',960)
parts += [text(30,43,'Holonomic presentation: one order shift, one fixed base',27,'bold'),
 rect(25,65,1150,340,'#edf3fb'),
 text(45,105,'N=Eᑫ is the specified intrinsic point manifold.',25,'bold'),
 text(100,174,'Eᑫ⁺ᴸ⁺ᵏ',26),text(810,174,'Sᴸ⁺ᵏ',26),arrow(290,166,755,166),indexed(455,149,'Ψ','L+k'),
 text(100,300,'Eᑫ⁺ᴸ',26),text(810,300,'Sᴸ',26),arrow(290,292,755,292),indexed(470,275,'Ψ','L'),
 arrow(160,190,160,257),arrow(855,190,855,257),text(180,229,'π',22),text(875,229,'π',22),
 text(45,360,'Dᵝv[α]=u[α+β],  |α|≤q, |β|≤k.  Brackets label original graph derivatives.',22),
 rect(25,425,1150,195,'#f1f8f5'),
 text(45,465,'Exact coefficient comparison · Proposition 4.46',24,'bold'),
 text(45,508,'Intrinsic cutoff L  ↔  original equation cutoff q+L, in both cases over N.',24),
 text(45,548,'Both coordinate changes are polynomial in higher variables with basic coefficients on N.',21),
 text(45,588,'An intrinsic determining k-jet acts through original equation order q+k.',23),
 rect(25,640,1150,225,'#fff6eb'),
 text(45,680,'A local map does not by itself specify a full regular fibre action',24,'bold'),
 text(45,725,'X=p, U=u−px, P=−x:   dU−P dX=du−p dx.',24),
 text(45,768,'a=uₓₓ,   DₓX=a,   U_XX=−1/a,   U_XXX=uₓₓₓ/a³,   a≠0.',23),
 text(45,808,'At a=0 the contact direction leaves the original graph chart.',23),
 text(45,844,'The regular finite-level action in Proposition 4.46 is actual presentation data. Example 4.47.',20),
 text(30,909,'Proof: Proposition 4.46 and Example 4.47, (4.121)–(4.126).  See Exercise 17 and Solution 17.',18),
 text(30,941,'Context: Kruglikov–Lychagin, arXiv:1111.5480v3 §0.1.  GPT-6.1 Sol (OpenAI). CC0 1.0.',16),'</g></svg>']
holonomic_svg='\n'.join(parts)+'\n'

svg=holonomic_svg
if __name__=='__main__':
    (OUT/'holonomic-intrinsic-presentation.svg').write_bytes(svg.encode('utf-8'))
