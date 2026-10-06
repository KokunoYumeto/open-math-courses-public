"""The two unitary matrices and cup slide in lesson 32. CC0."""
from pathlib import Path
from html import escape

parts=['<svg xmlns="http://www.w3.org/2000/svg" width="540" height="730" viewBox="0 0 540 730" role="img" aria-labelledby="title desc">',
       '<title id="title">Two unitary cell matrices build a path grid</title>',
       '<desc id="desc">An elementary square has a and d on one graph parity, b and c on the other. Fixing a,d gives U with row b and column c. Fixing b,c gives R with row a and column d, the conjugate coefficient times square root mu(a)mu(d) over mu(b)mu(c). The first changes path order; the second proves commuting expectations. Full support makes the square nondegenerate. Moving a normalized vertical cup across a horizontal edge leaves that edge followed by the normalized cup at its endpoint. The factor inclusion has index delta squared, while its graph still requires flatness.</desc>',
       '<rect width="540" height="730" fill="#fbfcff"/>',
       '<style>text{font-family:Arial,sans-serif;fill:#172c45}.title{font-size:20px;font-weight:bold}.heading{font-size:18px;font-weight:bold}.label{font-size:17px}.small{font-size:16px}</style>']
def text(x,y,value,cls='label',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')
def box(y,title,lines,height=106):
    parts.append(f'<rect x="24" y="{y}" width="492" height="{height}" rx="8" fill="#edf3fb" stroke="#7c9bbd"/>')
    text(270,y+28,title,'heading','middle')
    for i,line in enumerate(lines):text(270,y+57+24*i,line,'label' if i==0 else 'small','middle')
text(24,33,'Two unitary matrices build a path grid','title')
for x,y,v in [(55,85,'a'),(187,85,'b'),(55,163,'c'),(187,163,'d')]:
    text(x,y,v,'heading','middle')
parts.append('<path d="M70 79 H166 M70 157 H166 M55 99 V140 M187 99 V140" stroke="#426987" stroke-width="2" fill="none"/>')
text(117,72,'h','small','middle');text(117,183,'h','small','middle')
text(36,123,'v','small','middle');text(208,123,'v','small','middle')
text(256,87,'a,d: one parity','small')
text(256,117,'b,c: the other parity','small')
text(256,153,'Each side is a graph edge.','small')
box(211,'Fix a,d: rows b, columns c',[
    'Uᵃ˒ᵈ_b,c = w(a,b,c,d)',
    'The unitary U changes v h to h v.'])
box(335,'Fix b,c: rows a, columns d',[
    'Rᵇ˒ᶜ_a,d = √[μ(a)μ(d)/μ(b)μ(c)] · w̅',
    'The weighted unitary R gives commuting expectations.'])
box(459,'A normalized cup passes through a cell',[
    'cupₐ followed by (a → d) ↦ (a → d) then cup_d',
    'Output coefficient: 1_{c=d} √[μ(b)/(δ μ(d))].'])
box(583,'Full path support gives the actual factor tower',[
    'Full support ⇒ nondegenerate square;  [M : N] = δ²',
    'The principal graph also requires flatness.'],height=112)
text(24,722,'Proposition 32.2, Lemma 32.3 and Theorem 32.4.','small')
parts.append('</svg>')
Path(__file__).with_suffix('.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
