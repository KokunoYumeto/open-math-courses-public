"""Reproduce the exact cyclic Takai diagram as SVG and optionally PNG.

Original expression dedicated under CC0-1.0. This is an illustration of the
specified matrix identities, not a numerical or formal proof.

Run: python render-takai-cyclic-n3.py
For PNG, install playwright and Edge, then add --png. SVG is runtime independent;
PNG font rasterization may vary across browsers and operating systems.
"""
from pathlib import Path
import html
import argparse
svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="900" height="700" viewBox="0 0 900 700" role="img" aria-labelledby="title desc">',
       '<title id="title">Recovering one entry in the cyclic Takai model</title>',
       '<desc id="desc">Indices modulo three. A diagonal with alpha-one of b, b, alpha-two of b times E-one-two gives b E-one-two. Bidual time one sends it to alpha-one of b E-zero-one.</desc>',
       '<rect width="900" height="700" fill="#ffffff"/>',
       '<style>text{font-family:Georgia,serif;fill:#14202d;font-size:22px} .title{font-size:27px;font-weight:bold} .small{font-size:19px} .matrix{font-size:25px} .idx{font:18px Arial,sans-serif;fill:#475569}</style>']

def text(x, y, value, cls='', anchor='start'):
    svg.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{html.escape(value)}</text>')

def matrix(x, y, entries, active=None, cell=74):
    for r in range(3):
        text(x-19, y+r*cell+44, str(r), 'idx', 'middle')
        text(x+r*cell+cell/2, y-16, str(r), 'idx', 'middle')
        for c in range(3):
            fill = '#d6e8f8' if (r,c)==active else '#f5f7fa'
            svg.append(f'<rect x="{x+c*cell}" y="{y+r*cell}" width="{cell}" height="{cell}" fill="{fill}" stroke="#94a3b8"/>')
            text(x+c*cell+cell/2, y+r*cell+45, entries[r][c], 'matrix', 'middle')

text(38, 44, 'Recovering the coefficient: G = ℤ/3ℤ', 'title')
text(38, 80, 'Rows and columns are labelled 0, 1, 2; every index is modulo 3.', 'small')
text(135, 122, 'Aα₁(b)', anchor='middle')
text(434, 122, 'E₁₂ = p₁ S₂ p₂', anchor='middle')
text(735, 122, 'b E₁₂', anchor='middle')
matrix(35, 162, [['α₁(b)','0','0'],['0','b','0'],['0','0','α₂(b)']], (1,1))
matrix(335, 162, [['0','0','0'],['0','0','1'],['0','0','0']], (1,2))
matrix(635, 162, [['0','0','0'],['0','0','b'],['0','0','0']], (1,2))
text(294, 283, '×', anchor='middle')
text(594, 283, '=', anchor='middle')
text(38, 424, 'The selected row has α₋₁(α₁(b)) = b.  This is (FC3).', 'small')
text(38, 484, 'Bidual time s = 1:', 'title')
text(38, 528, 'b E₁₂  ↦  α₁(b) E₀₁')
text(38, 568, 'Right translation shifts both indices down by one.', 'small')
text(38, 602, 'The coefficient receives the original action α₁.', 'small')
matrix(635, 452, [['0','α₁(b)','0'],['0','0','0'],['0','0','0']], (0,1), cell=65)
text(38, 663, 'Scalar E, S, p may be multipliers; the products shown have entries in A.', 'small')
svg.append('</svg>')
target = Path(__file__).resolve().with_name('takai-cyclic-n3.svg')
target.write_text('\n'.join(svg)+'\n', encoding='utf-8', newline='\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--png', action='store_true')
    args = parser.parse_args()
    if args.png:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(channel='msedge', headless=True)
            page = browser.new_page(viewport={'width':900,'height':700}, device_scale_factor=2)
            page.set_content('<html><body style="margin:0">'+target.read_text(encoding='utf-8')+'</body></html>')
            page.locator('svg').screenshot(path=str(target.with_suffix('.png')))
            browser.close()
    print(target.name)
