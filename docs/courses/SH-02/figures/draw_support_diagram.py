"""Reproducible exact support/colimit diagrams; no geometric scale is asserted."""
from pathlib import Path
import argparse,json,hashlib
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'figures');args=parser.parse_args()
args.output.mkdir(parents=True,exist_ok=True)
def text(x,y,s,size=25,fill='#23354b'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="middle">{s}</text>'
def arrow(x1,y1,x2,y2,color='#516b87'):
 return f'<path d="M {x1} {y1} L {x2} {y2}" fill="none" stroke="{color}" stroke-width="2.4" marker-end="url(#arrow)"/>'
def frame(width,height,title):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">For compact K inside relatively compact open U and compact L containing the closure of U, Q equals L minus U. The pointwise cofiber sequence A_F(Q) to A_F(L) to F(U) maps by its colimit cone to Gamma_c(X minus K;F) to Gamma_c(X;F) to F[K]. Both rows, or both columns in the portrait diagram, are cofiber sequences. See SH02-SXM-4.</desc><defs><marker id="arrow" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#516b87"/></marker></defs><rect width="100%" height="100%" rx="18" fill="#f7f9fc"/><g font-family="Georgia,serif">'
af=lambda s:'A<tspan baseline-shift="sub" font-size="17">F</tspan>('+s+')'
gc=lambda s:'Γ<tspan baseline-shift="sub" font-size="17">c</tspan>('+s+'; F)'
top=[af('Q'),af('L'),'F(U)'];bottom=[gc('X ∖ K'),gc('X'),'F[K]']
wide=frame(1060,390,'Compact support cofiber sequence and its filtered colimit')
wide+=text(530,38,'The complement triangle',29)+text(530,70,'Q = L ∖ U;   K ⊂ U,   closure(U) ⊂ L',20)
xs=[180,530,880]
for x,a,b in zip(xs,top,bottom):
 wide+=text(x,141,a)+text(x,280,b)+arrow(x,157,x,243)+text(x+72,204,'colimit',17)
for y in [132,272]:
 wide+=arrow(278,y,424,y)+arrow(632,y,795,y)
wide+=text(530,340,'Both rows are cofiber sequences. Vertical maps are the same diagram’s colimit cones.',19)+text(530,371,'Proof: SH02-SXM-4, equations (SXM.8)–(SXM.9).',17)+'</g></svg>'
portrait=frame(590,675,'Compact support cofiber sequence and its filtered colimit, portrait')
portrait+=text(295,39,'The complement triangle',27)+text(295,74,'Q = L ∖ U;  closure(U) ⊂ L',20)+text(295,105,'K ⊂ U; both columns read downward',19)
ys=[202,350,498]
for y,a,b in zip(ys,top,bottom):
 portrait+=text(135,y,a,25)+text(435,y,b,24)+arrow(228,y-8,322,y-8)+text(277,y-26,'colimit',15)
for x in [135,435]:
 portrait+=arrow(x,224,x,315)+arrow(x,372,x,463)
portrait+=text(295,579,'Vertical arrows form cofiber sequences.',19)+text(295,610,'Horizontal arrows are colimit cones.',19)+text(295,644,'Proof: SH02-SXM-4, (SXM.8)–(SXM.9).',17)+'</g></svg>'
rows=[]
for name,body in [('covariant-verdier-support.svg',wide),('covariant-verdier-support-mobile.svg',portrait)]:
 p=args.output/name;p.write_text(body+'\n',encoding='utf-8');rows.append({'name':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
math={'proof_locator':'SH02-SXM-4','interpretation':'Exact commuting diagram of support fibres and filtered colimit cones; a schematic of morphisms, not a geometric projection or sampled set.','hypotheses':'K compact, U relatively compact open neighborhood of K, L compact containing closure(U), Q=L minus U.','upper_sequence':'A_F(Q) -> A_F(L) -> F(U)','lower_sequence':'Gamma_c(X minus K;F) -> Gamma_c(X;F) -> F[K]','vertical_maps_wide':'Compact-support inclusions and the neighborhood-colimit map F(U)->F[K].','portrait':'Transpose of the same diagram: cofiber sequences downward, colimit-cone maps to the right.','files':rows}
(args.output/'FIGURE_MATH.json').write_text(json.dumps(math,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows))
