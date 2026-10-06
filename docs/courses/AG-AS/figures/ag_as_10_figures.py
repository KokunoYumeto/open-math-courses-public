"""Reproduce the seven weighted stable genus-two graphs. CC0, October 2026.

Written by GPT-6.1 Sol (OpenAI) in Codex at Ultra.
Run with Python 3 to reproduce the SVG sources. With --render-png,
Playwright renders the same drawings for the course reader.
"""
from pathlib import Path
import argparse
import hashlib
import json
from xml.sax.saxutils import escape

GRAPHS = [
    ('I', 'A smooth genus-two component', [2], []),
    ('II', 'One elliptic component, one self-node', [1], [(0, 0)]),
    ('III', 'One rational component, two self-nodes', [0], [(0, 0), (0, 0)]),
    ('IV', 'Two elliptic components, one node', [1, 1], [(0, 1)]),
    ('V', 'An elliptic component and a rational loop', [1, 0], [(0, 1), (1, 1)]),
    ('VI', 'Two rational components, three nodes', [0, 0], [(0, 1), (0, 1), (0, 1)]),
    ('VII', 'Two rational loops, one joining node', [0, 0], [(0, 0), (0, 1), (1, 1)]),
]

def graph_svg(roman, title, weights, edges):
    n = len(weights)
    xs = [165] if n == 1 else [90, 240]
    y = 110
    valences = [0] * n
    for i, j in edges:
        valences[i] += 1
        valences[j] += 1
    degrees = [2 * g - 2 + d for g, d in zip(weights, valences)]
    genus = sum(weights) + len(edges) - n + 1
    assert genus == 2 and all(d > 0 for d in degrees)
    assert sum(degrees) == 2
    loop_counts = [sum(i == j == v for i, j in edges) for v in range(n)]
    joins = sum(i != j for i, j in edges)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="330" height="220" viewBox="0 0 330 220" role="img" aria-labelledby="title desc">',
        f'<title id="title">Graph {roman}: {escape(title)}</title>',
        '<desc id="desc">' + escape(f'Vertex genera {weights}; edges {edges}. A loop counts twice in vertex valence. Arithmetic genus {genus}; vertex canonical degrees {degrees}.') + '</desc>',
        '<rect x="1" y="1" width="328" height="218" rx="12" fill="#ffffff" stroke="#cbd5e1"/>',
        f'<text x="165" y="25" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#0f172a">Graph {roman}</text>',
        '<g fill="none" stroke="#1e40af" stroke-width="3.5" stroke-linecap="round">',
    ]
    if joins:
        parts.append(f'<path d="M {xs[0]} {y} L {xs[1]} {y}"/>')
    if joins == 3:
        parts += [
            f'<path d="M {xs[0]} {y} C 125 27 205 27 {xs[1]} {y}"/>',
            f'<path d="M {xs[0]} {y} C 125 193 205 193 {xs[1]} {y}"/>',
        ]
    for v, count in enumerate(loop_counts):
        x = xs[v]
        if n == 1 and count == 1:
            parts.append(f'<path d="M {x} {y} C 30 16 300 16 {x} {y}"/>')
        else:
            directions = [-1, 1] if count == 2 else [-1 if v == 0 else 1]
            for direction in directions[:count]:
                outer = x + direction * (115 if n == 1 else 95)
                parts.append(f'<path d="M {x} {y} C {outer} 12 {outer} 208 {x} {y}"/>')
    parts.append('</g>')
    for x, weight in zip(xs, weights):
        parts += [
            f'<circle cx="{x}" cy="{y}" r="19" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/>',
            f'<text x="{x}" y="{y + 7}" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="22" fill="#0f172a">{weight}</text>',
        ]
    parts += [
        '<text x="165" y="191" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#334155">Vertex label = normalization genus</text>',
        '<text x="165" y="208" text-anchor="middle" font-family="sans-serif" font-size="12" fill="#334155">Each edge is one node; a loop has two branches</text>',
        '</svg>',
    ]
    return '\n'.join(parts) + '\n', {'id': roman, 'title': title, 'weights': weights, 'edges': edges, 'valences': valences, 'canonical_degrees': degrees, 'arithmetic_genus': genus}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'src' / 'assets' / 'AG-AS-10')
    parser.add_argument('--render-png', action='store_true')
    parser.add_argument('--browser-executable', type=Path)
    args = parser.parse_args()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    records = []
    for roman, title, weights, edges in GRAPHS:
        svg, record = graph_svg(roman, title, weights, edges)
        path = out / f'genus-two-{roman}.svg'
        path.write_text(svg, encoding='utf-8', newline='\n')
        record.update(file=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest().upper())
        records.append(record)
    if args.render_png:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            options = {'headless': True}
            if args.browser_executable:
                options['executable_path'] = str(args.browser_executable)
            browser = p.chromium.launch(**options)
            page = browser.new_page(viewport={'width': 330, 'height': 220}, device_scale_factor=2)
            for record in records:
                svg = (out / record['file']).read_text(encoding='utf-8')
                page.set_content('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#fff}svg{display:block}</style></head><body>' + svg + '</body></html>')
                png = out / (Path(record['file']).stem + '.png')
                page.locator('svg').screenshot(path=str(png))
                record.update(png=png.name, png_sha256=hashlib.sha256(png.read_bytes()).hexdigest().upper(), png_width=660, png_height=440)
            browser.close()
    (out / 'graphs.json').write_text(json.dumps({'lesson': 'AG-AS-10', 'licence': 'CC0', 'meaning': 'Weighted dual graphs, not metric or geometric embeddings of curves.', 'graphs': records}, indent=2), encoding='utf-8', newline='\n')
    print(json.dumps({'graphs': len(records), 'all_genus_two': all(r['arithmetic_genus'] == 2 for r in records), 'all_stable': all(min(r['canonical_degrees']) > 0 for r in records)}))

if __name__ == '__main__':
    main()
