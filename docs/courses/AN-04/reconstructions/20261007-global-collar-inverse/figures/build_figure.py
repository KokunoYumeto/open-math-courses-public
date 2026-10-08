"""Exact support bounds for an illustrative chart and typed global patch. CC0."""
from pathlib import Path
import html
HERE=Path(__file__).resolve().parent
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="680" viewBox="0 0 1080 680" role="img" aria-labelledby="title desc">',
 '<title id="title">Nested local supports, one global inverse</title>',
 '<desc id="desc">The left panel shows allowed one-dimensional support bounds inside one chart, not graphs of the smooth cutoffs. The right panel shows the finite square-partition sum, its unchanged leading bundle inverse, and its two distinct errors.</desc>',
 '<rect width="1080" height="680" fill="white"/>',
 '<style>text{font-family:Arial,sans-serif;fill:#14283a}.title{font-size:27px;font-weight:bold}.head{font-size:22px;font-weight:bold}.body{font-size:19px}.small{font-size:16px}</style>']
def text(x,y,t,cls='body',anchor='start'):
    parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(t)}</text>')
text(540,42,'Nested local supports, one global inverse','title','middle')
text(264,92,'One possible coordinate nesting','head','middle')
cx,scale=264,51
rows=[(152,4,'support of ψ lies inside [−4, 4]','#dfe8ef'),
      (224,3,'ψ = 1 on [−3, 3]','#b9d0e1'),
      (296,2.8,'image of v lies inside [−2.8, 2.8]','#dce9c4'),
      (368,2.2,'v(y) = y on [−2.2, 2.2]','#a9c67c'),
      (440,2,'support of ρ lies inside [−2, 2]','#ead2ae'),
      (512,1,'support of ϑ lies inside [−1, 1]','#caa16a')]
for y,a,label,color in rows:
    parts.append(f'<rect x="{cx-scale*a}" y="{y}" width="{2*scale*a}" height="19" fill="{color}" stroke="#576c7d"/>')
    text(cx,y-10,label,'small','middle')
text(cx,556,'Take ρ = 1 on [−1.2, 1.2].','small','middle')
text(cx,582,'Smooth cutoff values are not plotted.','small','middle')
text(cx,608,'All these sets lie within the same chart.','small','middle')
parts.append('<path d="M532 82 V622" stroke="#c9d6df"/>')
text(796,92,'The actual finite sum','head','middle')
text(796,153,'Q = ∑ ϑᵢ Tᵢ ϑᵢ : F → E','head','middle')
text(796,190,'∑ ϑᵢ² = 1','body','middle')
text(796,245,'Leading coefficient: M⁻¹','head','middle')
text(796,279,'Complete right-cutoff products retained.','small','middle')
text(796,347,'QP_c = I_E + R_E','head','middle')
text(796,381,'P_c Q = I_F + R_F','head','middle')
text(796,424,'Both errors have paired degree −1.','body','middle')
text(796,490,'Finite correction gives Q_N','head','middle')
text(796,527,'and error degree −N on each space.','body','middle')
text(796,583,'GC13–GC21; no boundary condition','small','middle')
text(796,608,'is imposed by the cylinder inverse.','small','middle')
text(540,655,'Support equalities justify both exact local comparisons in GC15; all cutoff terms remain in GC17–GC18.','small','middle')
parts.append('</svg>')
(HERE/'global-collar-patching.svg').write_text('\n'.join(parts)+'\n',encoding='utf-8')
print('Wrote global-collar-patching.svg (1080 x 680).')
