"""Reproduce the typed finite normal correction diagram. Original CC0."""
from pathlib import Path
import html
HERE=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="680" viewBox="0 0 1080 680" role="img" aria-labelledby="title desc">',
 '<title id="title">One finite corrected inverse, two error spaces</title>',
 '<desc id="desc">P maps E to F and Q maps F to E. The error R F acts on F; R E acts on E. Both finite correction formulas agree, while the two remainders act on different spaces.</desc>',
 '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10Z" fill="#246497"/></marker></defs>',
 '<rect width="1080" height="680" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#14283a}.title{font-size:27px;font-weight:bold}.head{font-size:23px;font-weight:bold}.body{font-size:20px}.small{font-size:17px}</style>']
def text(x,y,value,cls='body',anchor='middle'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(value)}</text>')
text(540,43,'One finite corrected inverse, two error spaces','title')
for x,label in [(110,'E'),(880,'F')]:
    parts.append(f'<rect x="{x}" y="125" width="90" height="85" rx="12" fill="#e4eff8" stroke="#246497"/>')
    text(x+45,180,label,'head')
parts.append('<path d="M220 146 H860" stroke="#246497" stroke-width="3" marker-end="url(#arrow)"/>')
parts.append('<path d="M860 202 H220" stroke="#246497" stroke-width="3" marker-end="url(#arrow)"/>')
text(540,126,'P : E → F       degree m')
text(540,242,'Q : F → E       degree −m')
text(210,294,'R_E = QP − I_E','head')
text(870,294,'R_F = PQ − I_F','head')
text(210,327,'acts on E; degree −1','small')
text(870,327,'acts on F; degree −1','small')
text(540,375,'R_E Q = Q R_F   (actual associativity)','body')
parts.append('<rect x="72" y="400" width="936" height="86" rx="10" fill="#f0f5e7" stroke="#748b48"/>')
text(540,435,'Q_N = Q ∑(−R_F)ʲ = ∑(−R_E)ʲ Q','head')
text(540,467,'Each sum is finite: j = 0, …, N − 1.   See PN18.','small')
text(270,542,'Q_N P = I_E − (−R_E)ᴺ','head')
text(810,542,'P Q_N = I_F − (−R_F)ᴺ','head')
text(270,576,'error on E has degree −N','small')
text(810,576,'error on F has degree −N','small')
text(540,622,'Both errors keep their complete signed-tail and separated-kernel estimates.','small')
text(540,651,'PN13, PN17–PN19. The seed Q is an actual operator; N is finite.','small')
parts.append('</svg>')
(HERE/'paired-normal-errors.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Wrote paired-normal-errors.svg (1080 x 680).')
