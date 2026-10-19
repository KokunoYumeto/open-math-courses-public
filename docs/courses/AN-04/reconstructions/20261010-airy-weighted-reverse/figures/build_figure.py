"""Draw exact input projections and the two weighted recovery mechanisms."""
from pathlib import Path
from html import escape
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="590" viewBox="0 0 1080 590">',
 '<rect width="1080" height="590" fill="#f3f7fa"/>',
 '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#18364d}.body{font-size:17px}.small{font-size:14px}</style>',
 '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0 0 L8 3 L0 6" fill="#47647a"/></marker></defs>']
def text(x,y,t,cls='body'):
 parts.append(f'<text x="{x}" y="{y}" class="{cls}">{escape(t)}</text>')
def box(x,y,w,h,col):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{col}" stroke="#8b9da9"/>')
def arrow(x1,y1,x2,y2):
 parts.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#47647a" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
parts.append('<text x="25" y="35" font-size="23" font-weight="bold">Recover both parts of the stable Airy norm</text>')
text(35,78,'Exact w₁ projection: a = μ/λ = 1/25')
xx=lambda w:255+400*w
parts.append(f'<rect x="{xx(-.4)}" y="105" width="320" height="242" fill="#e2efec" stroke="#81a498" stroke-dasharray="5 4"/>')
text(108,127,'Larger cutoff equals one here','small')
for lo,hi,y,col,label in [(-.1,.1,170,'#526d86','K'),(.1,.3,235,'#087d67','ε = +1'),(-.3,-.1,300,'#aa5524','ε = −1')]:
 parts.append(f'<path d="M{xx(lo)} {y} H{xx(hi)}" stroke="{col}" stroke-width="11"/>')
 text(xx(hi)+10,y+5,label,'small')
arrow(xx(0),183,xx(.2),221)
arrow(xx(0),183,xx(-.2),285)
parts.append('<path d="M35 362 H478" stroke="#7a8d9b"/>')
for v in [-.4,-.2,0,.2,.4]:
 parts.append(f'<path d="M{xx(v)} 358 V367" stroke="#7a8d9b"/>')
 text(xx(v)-12,386,f'{v:g}','small')
text(478,365,'w₁','small')
text(35,420,'w = z + ε(√a, 0, …, 0, −a^(3/2)/3)','small')
text(35,447,'Omitted last displacement: −ε/375','small')
text(35,474,'λ = 4096; b = −256/25 < −2','small')
text(35,501,'Smooth tails remain outside these intervals.','small')
text(35,528,'WR8–WR11 bound them in every Sobolev norm.','small')
box(555,95,475,94,'#e5edf5')
text(575,122,'Interior branch observations')
text(575,151,'recover α and Zεv in H^(5/6)   [WR14]')
text(575,174,'Cutoffs contain all displaced input supports.','small')
box(555,220,475,114,'#e2efec')
text(575,247,'Actual boundary trace and Pu control')
text(575,276,'recover Aα + v in H_L; subtract Aα')
text(575,307,'to recover v in H_L   [WR16–WR19]')
arrow(790,190,790,215)
box(555,380,475,99,'#f5eadb')
text(575,409,'Exact sum of the two weight contributions')
text(575,440,'‖v‖²_Hw = π⁻¹‖ℓ^(5/6)Zεv‖² + ‖v‖²_HL','small')
text(575,464,'Full pair recovery, with coarse errors   [WR20–WR22]','small')
arrow(790,335,790,375)
text(555,515,'Scope: fields constructed from the localized stable pair.','small')
text(555,540,'The estimate concerns the stated stable-pair construction.','small')
text(25,575,'Left: projected canonical input shift [WR23]. Right: the two estimates combine; neither replaces the other.','small')
parts.append('</svg>')
Path(__file__).with_name('airy-weighted-reverse.svg').write_text('\n'.join(parts),'utf-8')
print('Wrote exact input-shift and norm-recovery figure.')
