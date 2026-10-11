from pathlib import Path
import html,json
base=Path(__file__).resolve().parent
d=json.loads((base/'data.json').read_text(encoding='utf-8'))
w,h=d['dimensions_px']['width'],d['dimensions_px']['height']
out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">','<rect width="100%" height="100%" fill="#fff"/>','<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#31596d"/></marker></defs>','<g font-family="Arial, sans-serif" fill="#182f3c">','<text x="450" y="42" text-anchor="middle" font-size="26">Whole Killing-jet compact weighting</text>','<text x="450" y="72" text-anchor="middle" font-size="17">Section 11BV: exact modules, domains, bounds and limited obstruction</text>']
for i,lines in enumerate(d['boxes']):
    y=100+156*i
    fill='#fff0e8' if i>=9 else '#edf5f9'
    out.append(f'<rect x="50" y="{y}" width="800" height="132" rx="12" fill="{fill}" stroke="#31596d"/>')
    for j,line in enumerate(lines):
        size=21 if j==0 else 17
        out.append(f'<text x="450" y="{y+28+27*j}" text-anchor="middle" font-size="{size}">{html.escape(line)}</text>')
    if i<len(d['boxes'])-1:
        out.append(f'<path d="M450 {y+133} L450 {y+153}" stroke="#31596d" stroke-width="2" marker-end="url(#arrow)"/>')
out+=['<text x="450" y="1841" text-anchor="middle" font-size="16">Original mathematical expression CC0-1.0; tensor arity r and normal degree q are distinct.</text>','</g></svg>']
target=base.parents[1]/'figures'/(d['slug']+'.svg')
target.write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n')
