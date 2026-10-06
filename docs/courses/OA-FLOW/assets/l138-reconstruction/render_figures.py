"""CC0. Reproduce the exact Z/3 coefficient and shear illustration."""
from pathlib import Path
import html
import hashlib
import json
import math
import fitz

OWN = Path(__file__).resolve().parent
OUT = OWN / "figures"
OUT.mkdir(exist_ok=True)
W, H = 1800, 1240
svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<rect width="1800" height="1240" fill="#fcfcf9"/>',
    '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10Z" fill="#263f55"/></marker></defs>',
]
def text(x, y, content, size=27, colour="#152b3b", anchor="start", weight="normal"):
    svg.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{colour}" text-anchor="{anchor}">{html.escape(content)}</text>')

def line(x1, y1, x2, y2, arrow=False, colour="#263f55", width=3):
    svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{colour}" stroke-width="{width}" fill="none"/>')
    if arrow:
        dx, dy = x2-x1, y2-y1
        length = math.hypot(dx, dy)
        ux, uy = dx/length, dy/length
        bx, by = x2-20*ux, y2-20*uy
        points = f"{x2},{y2} {bx-8*uy},{by+8*ux} {bx+8*uy},{by-8*ux}"
        svg.append(f'<polygon points="{points}" fill="{colour}"/>')

def matrix(x, y, title, entries, selected, sub):
    text(x + 175, y, title, 30, anchor="middle", weight="bold")
    left, top, cell = x + 13, y + 45, 112
    for r in range(3):
        for c in range(3):
            fill = "#d0eee7" if (r, c) in selected else "#f0f2f3"
            svg.append(f'<rect x="{left+c*cell}" y="{top+r*cell}" width="{cell}" height="{cell}" fill="{fill}" stroke="#b9c6ce"/>')
            text(left+(c+.5)*cell, top+(r+.5)*cell+10, entries[r][c], 27, anchor="middle")
        text(left-17, top+(r+.5)*cell+9, str(r), 24, anchor="end")
    for c in range(3):
        text(left+(c+.5)*cell, top-12, str(c), 24, anchor="middle")
    text(x+175, top+3*cell+48, sub, 24, anchor="middle")

text(70, 63, "Two exact mechanisms in the order-three duality", 43, weight="bold")
text(70, 104, "Counting Haar on G; dual mass 1/3. Rows and columns are indexed 0, 1, 2.", 26)
matrix(75, 160, "A[α₁(b)]", [["α₁(b)","0","0"],["0","b","0"],["0","0","α₂(b)"]], {(1,1)}, "coefficient at row 1 is b")
text(470, 393, "×", 54, anchor="middle")
matrix(515, 160, "p₁ S₂ p₂ = E₁₂", [["0","0","0"],["0","0","1"],["0","0","0"]], {(1,2)}, "column 2 moves to row 1")
text(908, 393, "=", 54, anchor="middle")
matrix(955, 160, "b E₁₂", [["0","0","0"],["0","0","b"],["0","0","0"]], {(1,2)}, "α₋₁(α₁(b)) = b")
line(1338, 380, 1423, 380, True)
text(1380, 315, "s = 1", 25, anchor="middle")
matrix(1440, 160, "α₁(b) E₀₁", [["0","α₁(b)","0"],["0","0","0"],["0","0","0"]], {(0,1)}, "right translation subtracts 1")
text(70, 660, "(FC3): nonunital coefficients are allowed; the scalar matrices act as multipliers.", 25)
line(70, 698, 1730, 698, colour="#b9c6ce", width=2)
text(70, 746, "The shear makes the multiplicity coordinate stationary", 35, weight="bold")
text(70, 787, "(TC3)–(TC4), sampled exactly on G × G = (Z/3Z)²; every coordinate is modulo 3.", 25)

colours = ["#7452a5", "#007d76", "#c07317"]
def grid(x, top, horizontal, transform):
    cell = 115
    for k in range(3):
        line(x, top+k*cell, x+2*cell, top+k*cell, colour="#d1d9dc", width=2)
        line(x+k*cell, top, x+k*cell, top+2*cell, colour="#d1d9dc", width=2)
    for t in range(3):
        for k in range(3):
            xx, yy = x + k*cell, top + (2-t)*cell
            q = k if transform else (k-t)%3
            svg.append(f'<circle cx="{xx}" cy="{yy}" r="20" fill="{colours[q]}"/>')
            text(xx, yy+7, str(q), 20, "#fff", "middle", "bold")
    for k in range(3):
        text(x+k*cell, top+2*cell+42, str(k), 25, anchor="middle")
    for t in range(3):
        text(x-35, top+(2-t)*cell+8, str(t), 25, anchor="end")
    text(x+cell, top+2*cell+82, horizontal, 29, anchor="middle", weight="bold")
    text(x-78, top+cell+8, "t", 29, anchor="middle", weight="bold")
    return cell

grid(200, 858, "x", False)
grid(1100, 858, "q = x − t", True)
line(412, 964, 218, 867, True, width=5)
text(370, 835, "(2,1) → (0,2)", 24, anchor="middle")
line(1215, 953, 1215, 878, True, width=5)
text(1400, 835, "(1,1) → (1,2)", 24, anchor="middle")
line(570, 968, 925, 968, True, width=4)
text(748, 930, "Sζ(q,t) = ζ(q+t,t)", 29, anchor="middle")
text(748, 1009, "q stays fixed", 27, anchor="middle", weight="bold")
text(70, 1202, "Colours and point labels mark q = 0, 1, 2. Basis translation increments x,t; after the shear only t increments.", 24)
svg.append("</svg>")
source = "\n".join(svg) + "\n"
svg_path = OUT / "finite-clock-and-shear.svg"
svg_path.write_text(source, encoding="utf-8")
png_path = OUT / "finite-clock-and-shear.png"
document = fitz.open(stream=source.encode("utf-8"), filetype="svg")
pdf = fitz.open("pdf", document.convert_to_pdf())
pdf[0].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False).save(png_path)
receipt = {
    "mathematical_sample": "Exact Z/3Z matrices and coordinate shear, not general-group geometry.",
    "equation_locators": ["TC3", "TC4", "FC1", "FC2", "FC3", "61"],
    "dimensions": [W, H], "licence": "CC0-1.0 for original figure/code",
    "assets": [{"path": str(p), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in [svg_path, png_path]],
}
(OWN / "FIGURE_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
