"""Reproduce Figure52.1: actual tensor legs, traces and center localization."""
from pathlib import Path
from html import escape
OUT=Path(__file__).with_suffix('.svg')
parts=[
 '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="1120" viewBox="0 0 640 1120" role="img" aria-labelledby="title desc">',
 '<title id="title">The canonical trace multiplier and the center condition</title>',
 '<desc id="desc">The old left matrix algebra becomes all operators on its n-squared dimensional Hilbert space. Both canonical trace normalizations are shown. The smaller and larger centers remain separate. A spectral-piece example has vanishing total defect but two large piece defects.</desc>',
 '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#315b70"/></marker></defs>',
 '<rect width="640" height="1120" fill="#f9fcfe"/>']
def text(x,y,s,size=19,color='#163c50',weight='normal'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="middle" font-weight="{weight}">{escape(s)}</text>')
def line(x1,y1,x2,y2,arrow=False):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#315b70" stroke-width="2"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
def box(x,y,w,h,title,detail):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#eaf3f8" stroke="#6b96ad"/>')
 text(x+w/2,y+29,title,22,weight='bold');text(x+w/2,y+56,detail,17)
text(320,35,'One matrix factor; two operator traces',26,weight='bold')
text(320,67,'H = L²(M⁰) ⊗ L²(Mₙ);  dim L²(Mₙ) = n²',21)
box(35,96,255,82,'Old leg: L(Mₙ)','n copies of its defining action')
box(350,96,255,82,'New leg: M(n²)','All operators on L²(Mₙ)')
line(295,137,345,137,True)
text(163,207,'e_R = e₀ ⊗ I',22)
text(478,207,'e_R⁰ = e₀ ⊗ r',22)
text(320,239,'r projects onto 1_D;  rank(r) = Tr(r) = 1',19)
box(35,270,570,81,'A = A₀ ⊗ L(Mₙ) ⊂ Ã = A₀ ⊗ M(n²)','The same first leg A₀ = ⟨N⁰, e₀⟩')
box(35,370,570,81,'B = B₀ ⊗ L(Mₙ) ⊂ B̃ = B₀ ⊗ M(n²)','The same first leg B₀ = ⟨M⁰, e₀⟩')
text(320,483,'Old normalization: Tr₀ ⊗ trₙ',22)
text(320,516,'New normalization: Tr₀ ⊗ Tr on L²(Mₙ)',22)
text(320,553,'Tr(L_b) = n² trₙ(b) ⇒ C_new(q) = n² C_old(q)',20,weight='bold')
text(320,585,'Center measures agree; relative L² defects are unchanged.',18)
line(35,612,605,612)
text(320,647,'The centers agree within each row',24,weight='bold')
text(320,680,'Z(A) = Z(Ã) ↔ Z(S⁰)',21)
text(320,712,'Z(B) = Z(B̃) ↔ Z(R⁰)',21)
text(320,746,'Z(A) ∩ M′ ↔ Z(S) ∩ Z(R)',21,weight='bold')
text(320,777,'A block in Z(A) needs justification before localizing M defects.',17)
line(35,798,605,798)
text(320,832,'Spectral-piece warning · Example 52.7',24,'#713d26','bold')
box(50,856,220,75,'p z′₀: dim k+1','u sends it to support z′₁')
box(370,856,220,75,'p z′₁: dim k','u sends it to support z′₀')
line(280,888,360,888,True)
line(360,907,280,907,True)
text(320,966,'k = 4ᵗ/2;  Tr(p) = k + ½',21)
text(320,1000,'Total relative defect: 1/√(k+½) → 0',21)
text(320,1033,'Each spectral-piece relative defect: √2',21,'#713d26','bold')
text(320,1065,'An actual nondegenerate square; no core realization claimed.',17)
text(320,1097,'52.3: full trace multiplier · 52.5: verified block hypothesis',16)
parts.append('</svg>')
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(OUT)
