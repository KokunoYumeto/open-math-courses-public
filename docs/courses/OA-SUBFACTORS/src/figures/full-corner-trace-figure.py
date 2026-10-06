"""Reproduce an exact matrix example of finite-full-corner trace extension."""
from pathlib import Path
from xml.sax.saxutils import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="960" height="710" viewBox="0 0 960 710" role="img" aria-labelledby="title desc">',
 '<title id="title">One corner determines the trace of the whole algebra</title>',
 '<desc id="desc">For P equal to the three by three matrices and q equal to E11, the partial isometries E1j have orthogonal initial projections Ejj and the same final projection q. Each diagonal entry of a positive matrix is measured in qPq, and their sum is the ordinary matrix trace. The general extension is a net sum over an arbitrary family.</desc>',
 '<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8" fill="#145778"/></marker></defs>',
 '<rect width="960" height="710" fill="#fbfcff"/>']
def text(x,y,s,size=22,color='#172635',weight='normal',anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(s)}</text>')
def box(x,y,w,h):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#e8f1f6" stroke="#9eb8c5"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#145778" stroke-width="3" marker-end="url(#arrow)"/>')
text(40,48,'One full corner determines the trace',29,weight='bold')
text(40,87,'Matrix example: P = M₃(ℂ),  q = E₁₁,  t(cq) = c.',23)
text(40,126,'For a ≥ 0, choose vⱼ = E₁ⱼ,  fⱼ = vⱼ* vⱼ = Eⱼⱼ.',23)
text(40,165,'The fⱼ are orthogonal and sum to 1; all vⱼ vⱼ* = q.',23)
for j,(sub,yy) in enumerate([('₁',220),('₂',315),('₃',410)],1):
 box(45,yy,280,65);text(185,yy+41,f'f{sub} = E{sub}{sub}',25,anchor='middle')
 box(610,yy,305,65);text(762,yy+41,f't(v{sub} a v{sub}*) = a{sub}{sub}',25,anchor='middle')
 arrow(345,yy+33,590,yy+33);text(468,yy+19,f'v{sub} = E₁{sub}',22,anchor='middle')
text(480,517,'Each vⱼ a vⱼ* = aⱼⱼ q lies in the same corner qPq.',23,anchor='middle')
box(30,540,900,98)
text(480,576,'T(a) = a₁₁ + a₂₂ + a₃₃;   T(q) = 1;   T(1) = 3.',25,weight='bold',anchor='middle')
text(480,615,'General full-corner formula: T(a) = Σⱼ t(vⱼ a vⱼ*).',23,anchor='middle')
text(480,664,'General sums run over finite subsets of an arbitrary index set (Lemma 1.2a).',18,anchor='middle')
text(480,695,'Only initial projections are orthogonal; the final projections may overlap.',18,anchor='middle')
parts.append('</svg>')
out=Path(__file__).with_suffix('.svg');out.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(str(out))
