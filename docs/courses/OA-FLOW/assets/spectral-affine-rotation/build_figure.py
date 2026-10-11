"""Draw the exact spectral maps and the finite Fourier-mode window in SAR."""
from pathlib import Path
from html import escape


def build_svg():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="690" viewBox="0 0 1200 690" role="img" aria-labelledby="title desc">',
             '<title id="title">Spectral transport and the tracial fixed mode</title>',
             '<desc id="desc">Function arguments and base points move in inverse directions. In a five-by-five window of integer Fourier indices, the two irrational conjugation tests intersect only at the origin.</desc>',
             '<rect width="1200" height="690" fill="#f8fafc"/>',
             '<style>text{font-family:DejaVu Sans,Arial,sans-serif;fill:#172033}.title{font-size:28px;font-weight:700}.head{font-size:22px;font-weight:700}.body{font-size:20px}.small{font-size:17px}.tiny{font-size:15px}</style>']

    def text(x, y, content, cls="body", anchor="start"):
        size = {"title": 28, "head": 22, "body": 20, "small": 17, "tiny": 15}[cls]
        weight = 700 if cls in {"title", "head"} else 400
        parts.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="#172033" text-anchor="{anchor}">{escape(content)}</text>')

    text(42, 50, "Spectral transport and the tracial fixed mode", "title")
    text(42, 82, "Exact formulas: Propositions 2 and 6, Theorems 4 and 7", "small")
    for x, width in [(30, 565), (615, 555)]:
        parts.append(f'<rect x="{x}" y="112" width="{width}" height="500" rx="14" fill="white" stroke="#cbd5e1"/>')
    text(54, 149, "A. Scalar argument and point motion", "head")
    text(54, 191, "Rotation: z(t) = exp(−2πit)", "body")
    text(70, 231, "Function:   f(t) ↦ f(t − θ)", "body")
    text(70, 266, "Base point: t ↦ t + θ", "body")
    text(70, 302, "u v u* = exp(2πiθ) v", "body")
    parts.append('<line x1="54" y1="329" x2="570" y2="329" stroke="#cbd5e1"/>')
    text(54, 366, "Affine: (a,b)(c,d) = (ac,b + ad)", "body")
    text(70, 407, "Function:   f(p) ↦ f(ap)", "body")
    text(70, 442, "Base point: p ↦ p/a", "body")
    text(70, 482, "Fibre arrow H(x) → H(x/a):", "body")
    text(90, 520, "exp(ibx/a) Cₐ(x/a)", "body")
    text(70, 569, "Global norm factor: √jₐ(p)", "body")

    text(639, 149, "B. Both conjugations fix only 1", "head")
    text(639, 185, "Basis vector: uᵐvⁿ    •    θ irrational", "body")
    ox, oy, step = 895, 382, 54
    parts.append(f'<line x1="{ox-136}" y1="{oy}" x2="{ox+150}" y2="{oy}" stroke="#64748b" stroke-width="1.5"/>')
    parts.append(f'<line x1="{ox}" y1="{oy+136}" x2="{ox}" y2="{oy-151}" stroke="#64748b" stroke-width="1.5"/>')
    text(ox+164, oy+7, "m", "small")
    text(ox+9, oy-151, "n", "small")
    for m in range(-2, 3):
        for n in range(-2, 3):
            color = "#7c3aed" if m == n == 0 else "#c2410c" if n == 0 else "#0f766e" if m == 0 else "#cbd5e1"
            radius = 10 if m == n == 0 else 6
            parts.append(f'<circle cx="{ox+step*m}" cy="{oy-step*n}" r="{radius}" fill="{color}"/>')
        if m:
            text(ox+step*m, oy+29, str(m), "tiny", "middle")
            text(ox-17, oy-step*m+5, str(m), "tiny", "end")
    text(ox+15, oy+27, "0", "tiny")
    text(641, 548, "Ad u: eigenvalue qⁿ = 1 exactly when n = 0", "small")
    text(641, 577, "Ad v: eigenvalue q⁻ᵐ = 1 exactly when m = 0", "small")
    text(42, 650, "The dots show −2 ≤ m,n ≤ 2. The proof applies to every (m,n) ∈ ℤ².", "small")
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    Path(__file__).with_name("spectral-affine-rotation.svg").write_text(build_svg(), encoding="utf-8", newline="\n")
