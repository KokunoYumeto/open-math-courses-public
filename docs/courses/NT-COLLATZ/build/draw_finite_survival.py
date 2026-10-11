"""Draw the exact three-block proof decomposition; no sampled path is plotted."""
from pathlib import Path
from xml.sax.saxutils import escape
R=Path(__file__).resolve().parents[1]
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="440" height="790" viewBox="0 0 440 790" role="img" aria-labelledby="title desc">',
'<title id="title">Three estimates for one surviving word</title>',
'<desc id="desc">For m=16 the exact word split has lengths 4,8,4. Two independent necessary outer conditions each supply an inverse square root. A conditional endpoint bound for the middle supplies the third. The resulting bound is for each terminal bin, then summed with exponential weights.</desc>',
'<rect width="440" height="790" fill="#ffffff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#183a46}.head{font-size:20px;font-weight:bold}.body{font-size:16px}.small{font-size:15px}.math{font-size:19px}.label{font-size:17px;font-weight:bold}</style>']
def text(x,y,value,cls='body',anchor=None):
    attr='' if anchor is None else ' text-anchor="'+anchor+'"'
    parts.append(f'<text x="{x}" y="{y}" class="{cls}"{attr}>{escape(value)}</text>')
def box(y,h,color):
    parts.append(f'<rect x="18" y="{y}" width="404" height="{h}" rx="8" fill="{color}" stroke="#b9cbd1"/>')
text(20,32,'One word, three separate estimates','head')
text(20,60,'Example: m = 16, a = 4, b = 8.')
for x,width,color,label in [(20,100,'#dceeea','first 4'),(120,200,'#e7edf8','middle 8'),(320,100,'#dceeea','last 4')]:
    parts.append(f'<rect x="{x}" y="78" width="{width}" height="46" fill="{color}" stroke="#56727e"/>')
    text(x+width/2,107,label,'label','middle')
text(20,155,'Fix a terminal bin: Zₘ + B ∈ [q, q + 1).')
box(175,130,'#eff7f3')
text(34,204,'First outer block','label')
text(34,233,'Every prefix has Zⱼ > −B.')
text(34,264,'Probability ≤ 2(B + 1) / √(va)','math')
text(34,289,'Only these first a letters are used.','small')
box(325,153,'#eff7f3')
text(34,354,'Last outer block, read backwards','label')
text(34,383,'Negate its increments, not its bits.')
text(34,410,'Zₘ₋ⱼ − Zₘ > −(q + 1)')
text(34,441,'Probability ≤ 2(q + 2) / √(va)','math')
text(34,465,'These letters are disjoint from the first.','small')
box(498,131,'#f0f3fa')
text(34,527,'Middle block, with both ends fixed','label')
text(34,556,'A unit bin contains at most one atom.')
text(34,587,'Conditional probability ≤ Cₚ / √b','math')
text(34,614,'This bound is uniform in the fixed ends.','small')
text(20,662,'Multiply the two outer probabilities.')
text(20,687,'Then apply the conditional middle bound.')
text(220,724,'4Cₚ(B + 1)(q + 2) / (va√b)','math','middle')
text(20,759,'Finally sum bins with weights e⁻ᶿᑫ.','body')
parts.append('</svg>')
(R/'figures/three-block-survival.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')

