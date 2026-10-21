"""The full normalizer action on the regular nilpotent plane. CC0-1.0."""
from pathlib import Path
from html import escape
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="1500" viewBox="0 0 1280 1500" role="img" aria-labelledby="title desc">
<title id="title">Three character orbits over a regular nilpotent plane</title>
<desc id="desc">E sends e3 to e1 to e2 to zero, E squared is q=E23, and E cubed is zero. The full normalizer sends E to aE+bq and q to a squared q. Its action on the character pair (u,v) has exactly three orbits, represented by (0,0), (1,0), and (0,1), with nilpotent sets of dimension two, a rank-one line, and a rank-two line. A separate coordinate exchange illustrates the discrete sign action on a diagonal-family scalar parameter.</desc>
<rect width="1280" height="1500" fill="#f8fafc"/>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="#475569"/></marker></defs>
<style>text{font-family:Arial,sans-serif;fill:#102238;font-size:22px}.title{font-size:31px;font-weight:bold}.head{font-size:25px;font-weight:bold}.small{font-size:19px}.math{font-family:Georgia,serif}</style>''']
def text(x,y,s,cls='',anchor=None):
    a=''if anchor is None else f' text-anchor="{anchor}"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{a}>{escape(s)}</text>')
def box(x,y,w,h,color='#fff'):parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#94a3b8"/>')
def arrow(x,y,xx,yy):parts.append(f'<path d="M{x} {y} L{xx} {yy}" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>')
text(40,49,'A normalizer shear removes a scalar coefficient','title')
text(40,87,'J₂ = ⟨E,q⟩,   E = E₁₃+E₂₁,   q = E² = E₂₃,   E³ = 0.','math')
box(40,115,1200,126,'#e0f2fe')
text(180,169,'e₃','head math','middle');text(485,169,'e₁','head math','middle');text(790,169,'e₂','head math','middle');text(1095,169,'0','head math','middle')
arrow(240,160,415,160);arrow(545,160,720,160);arrow(850,160,1025,160)
text(328,144,'E','small math','middle');text(633,144,'E','small math','middle');text(938,144,'E','small math','middle')
text(640,216,'The square q sends e₃ directly to e₂ and kills e₁,e₂.','small','middle')
box(40,272,1200,233,'#fff')
text(65,315,'Every normalizer action has this form, and every such action occurs','head')
text(65,356,'E ↦ aE+bq,   q ↦ a²q,   a ∈ ℂ*, b ∈ ℂ.','math')
text(65,397,'u = χ(E), v = χ(q)  ⇒  v′ = v/a²,   u′ = u/a − bv/a³.','math')
text(65,438,'v ≠ 0: choose a²=v and b=u to obtain (u′,v′)=(0,1).','small')
text(65,478,'v = 0, u ≠ 0: choose a=u to obtain (1,0); zero remains zero.','small')
cards=[(40,'(u,v) = (0,0)','⟨E,q⟩','Every matrix is nilpotent.','Nilpotent set: dimension 2.','#dcfce7'),
       (450,'(u,v) = (1,0)','⟨E+I,q⟩','Nilpotent set = ℂq.','Nonzero nilpotent rank: 1.','#fef3c7'),
       (860,'(u,v) = (0,1)','⟨E,q+I⟩','Nilpotent set = ℂE.','Nonzero nilpotent rank: 2.','#e0f2fe')]
for x,title,model,line,last,color in cards:
    box(x,536,380,240,color);text(x+190,580,title,'head math','middle');text(x+190,629,model,'head math','middle')
    text(x+20,682,line,'small');text(x+20,727,last,'small')
box(40,807,1200,204,'#fff')
text(65,850,'An explicit conjugation, with no residual parameter','head')
text(65,891,'P = I+uE₂₁  ⇒  P(E+uI)P⁻¹ = E+u(q+I),   P(q+I)P⁻¹ = q+I.','math')
text(65,932,'Thus ⟨E+uI,q+I⟩ is conjugate to ⟨E,q+I⟩ for every u ∈ ℂ.','math')
text(65,978,'The three cards are distinct by their nilpotent-set dimensions and ranks.','small')
box(40,1042,1200,245,'#ecfdf5')
text(65,1085,'A disconnected normalizer can change an exact-looking scalar value','head')
text(65,1126,'T₃(1,−1): exchanging e₁,e₂ sends D(1,−1) to −D(1,−1).','math')
text(65,1167,'The identity matrix is fixed, so the graph parameter satisfies t ~ −t.','small')
text(65,1208,'This is the full joint relation [1:−1:t] ~ [−1:1:t] = [1:−1:−t].','math')
text(65,1252,'For the diagonal plane, all S₃ permutations of (α,β,−α−β) must be retained.','small')
text(40,1340,'Proof: Theorem8.13, equations(8.39)–(8.40), Example8.14 and Solutions13–14.','small')
text(40,1385,'Human source: Lie–Engel III, §29 pp.112–116, on character spaces and full normalizers.','small')
text(40,1430,'All statements concern matrix conjugacy over ℂ; the complete arguments remain alongside the figure.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
