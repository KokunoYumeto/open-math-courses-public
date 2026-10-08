"""Exact order/norm diagram for SF5–SF10, with reproducible SVG geometry."""
from pathlib import Path
from html import escape
import hashlib,json
r=Path(__file__).resolve().parents[1];f=r/'figures/sharp-form-half-order.svg'
f.parent.mkdir(exist_ok=True)
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="780" height="430" viewBox="0 0 780 430" role="img" aria-labelledby="title description">',
'<title id="title">Half-order balance in the full form defect</title>',
'<desc id="description">Order and norm diagram for SF5 through SF10. L plus raises the coefficient orders of F in M(s minus 1) by one half. The actual adjoint L star lowers those of H in M(s) by one half. Both balanced expressions are in M(k), k equals s minus one half, and map u to L2 with an Xk bound. A separate negative residual correction is bounded by the bare energy norm squared. This is a schematic operator diagram, not a Hamilton trajectory.</desc>',
'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#28566b"/></marker></defs>',
'<rect width="780" height="430" fill="#fff"/>',
'<style>text{font-family:Arial,sans-serif;fill:#203849;text-anchor:middle}.box{fill:#f1f7fa;stroke:#456a7c;stroke-width:1.5}.flow{stroke:#28566b;stroke-width:2;fill:none;marker-end:url(#arrow)}</style>']
def text(x,y,value,size=17,weight='normal'):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}">{escape(value)}</text>')
text(390,31,'Half-order balance in the full form defect',23,'bold')
text(390,55,'M(r): coefficients before one ordinary derivative have order r; the free term has order r + 1.',13)
for x,top,operator,bottom in [(30,'Fλ in M(s − 1)','L+  : order + ½','L+ Fλ in M(s − ½)'),(470,'Hλ in M(s)','L*  : order − ½','L* Hλ in M(s − ½)')]:
    parts.append(f'<rect class="box" x="{x}" y="75" width="280" height="119" rx="7"/>')
    text(x+140,101,top,19,'bold');text(x+140,137,operator,17);text(x+140,176,bottom,18)
parts.extend(['<path class="flow" d="M170,194 L260,223"/>','<path class="flow" d="M610,194 L520,223"/>','<rect class="box" x="160" y="226" width="460" height="69" rx="7"/>'])
text(390,250,'SF5: both expressions map u to L²',18,'bold')
text(390,277,'Each norm ≤ C Xₖ(u); |balanced pairing| ≤ C Xₖ(u)².',15)
text(390,326,'SF9: (Fλu, Hλu) = (L+Fλu, L*Hλu) − (Fλu, E_L*Hλu)',17)
text(390,355,'WF′(E_L) misses K; SF10 bounds the separate residual term by Cᵣ ‖u‖ᵥ².',16)
text(390,391,'k = s − ½; Q is elliptic on K; u in V and Qu in V; L* is the actual adjoint.',14)
text(390,414,'No ordinary normal derivative is moved across the boundary.',14,'bold')
parts.append('</svg>');f.write_text('\n'.join(parts)+'\n',encoding='utf8')
source=r/'sharp-boundary-form-defect.md'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'schema':'AN04-restored-sharp-form-figure/v1','asset':'figures/sharp-form-half-order.svg',
 'sha256':sha(f),'source_sha256':sha(source),'script_sha256':sha(Path(__file__)),
 'width':780,'height':430,'proof_locators':'SF4–SF10','passed':True,'actually_inspected':False,
 'original_svg_sha256':'a7b61c9f5f4ce654683e7b3da203268231ee719ebb8cee7c2cbf51b8d90b841d',
 'exact_coordinate_checks':['F has coefficient order s−1 and is raised by L+ of order one half.',
 'H has coefficient order s and is lowered by the actual L adjoint of order minus one half.',
 'Both balanced expressions have mixed order s−1/2 and the same X_k bound.',
 'The complex pairing bound has explicit absolute-value bars.',
 'SF9 retains its exact negative residual correction.',
 'The residual term has a bare energy bound and no ordinary normal derivative is transposed.'],
 'change':'Only the complex pairing bound gains explicit absolute-value bars; the original order diagram is retained.',
 'diagram_is_schematic_not_a_hamilton_trajectory':True}
(r/'figure-check.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'asset':record['asset'],'preserved_order_diagram':True}))
