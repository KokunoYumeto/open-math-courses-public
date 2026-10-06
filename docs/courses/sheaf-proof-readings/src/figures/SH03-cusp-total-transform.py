#!/usr/bin/env python3
"""Create an exact native SVG of the three point blow-ups of y^2-x^3.

Original programme figure, exposition, and code: CC0 1.0.
Human mathematical context: Edward Bierstone and Pierre D. Milman,
Canonical desingularization in characteristic zero by blowing up the maximum
strata of a local invariant, author manuscript of 25 November 1996. Their
principal-ideal framework is the reference; these explicit chart computations
and this figure are independently expressed programme work.

Uses only the Python standard library. The parabola is one exact quadratic
Bezier curve, not a sampled approximation. All other divisor branches are
straight coordinate lines. Axis scales are affine and may differ.

Example after publication:
  python src/figures/SH03-cusp-total-transform.py \
      --output figures/SH03-cusp-total-transform.svg
The --check-only flag verifies polynomial identities over the integers,
including the Laurent-polynomial overlap identities, without creating an SVG.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape


class Poly:
    """Sparse integral Laurent polynomials in two named formal variables."""

    def __init__(self, terms=0):
        if isinstance(terms, Poly):
            terms = terms.terms
        elif isinstance(terms, int):
            terms = {(0, 0): terms}
        self.terms = {key: value for key, value in terms.items() if value}

    def __add__(self, other):
        result = dict(self.terms)
        for key, value in Poly(other).terms.items():
            result[key] = result.get(key, 0) + value
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) + (-self)

    def __mul__(self, other):
        result = {}
        for (i, j), left in self.terms.items():
            for (k, ell), right in Poly(other).terms.items():
                key = (i + k, j + ell)
                result[key] = result.get(key, 0) + left * right
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("Use an explicit Laurent monomial for an inverse.")
        result = Poly(1)
        for _ in range(exponent):
            result = result * self
        return result

    def at(self, first, second):
        if any(i < 0 or j < 0 for i, j in self.terms):
            raise ValueError("The substituted polynomial must have no negative powers.")
        return sum((value * first**i * second**j
                    for (i, j), value in self.terms.items()), Poly())

    def __eq__(self, other):
        return self.terms == Poly(other).terms


def check_identities():
    """Arithmetic checks supplement the complete chart/cover argument in text."""
    x, y = Poly({(1, 0): 1}), Poly({(0, 1): 1})
    xi, yi = Poly({(-1, 0): 1}), Poly({(0, -1): 1})
    cusp = y**2 - x**3
    first_u = x**2 * (y**2 - x)
    first_s = y**2 * (1 - x**3 * y)
    second_a = x**3 * y**2 * (x - y)
    second_c = x**3 * (x * y**2 - 1)
    third_p = x**6 * y**2 * (1 - y)
    third_t = x**6 * y**3 * (y - 1)
    rows = [
        ("first u-chart", cusp.at(x, x*y), first_u),
        ("first s-chart", cusp.at(x*y, y), first_s),
        ("first overlap u=rs, v=1/r", first_u.at(x*y, xi), first_s),
        ("second a-chart", first_u.at(x*y, x), second_a),
        ("second c-chart", first_u.at(x, x*y), second_c),
        ("second overlap a=cd, b=1/d", second_a.at(x*y, yi), second_c),
        ("third p-chart", second_a.at(x, x*y), third_p),
        ("third t-chart", second_a.at(x*y, x), third_t),
        ("third overlap p=tw, q=1/w", third_p.at(x*y, yi), third_t),
        ("final s/c overlap r=1/(cd), s=c²d", first_s.at(xi*yi, x**2*y), second_c),
        ("final s/p overlap r=1/p, s=p³q", first_s.at(xi, x**3*y), third_p),
        ("final s/t overlap r=1/(tw), s=t³w²", first_s.at(xi*yi, x**3*y**2), third_t),
        ("final c/p overlap c=p²q, d=1/(pq)", second_c.at(x**2*y, xi*yi), third_p),
        ("final c/t overlap c=t²w, d=1/t", second_c.at(x**2*y, xi), third_t),
        ("direct map from p-chart x=p²q, y=p³q", cusp.at(x**2*y, x**3*y), third_p),
        ("direct map from t-chart x=t²w, y=t³w²", cusp.at(x**2*y, x**3*y**2), third_t),
        ("direct map from c-chart x=c, y=c²d", cusp.at(x, x**2*y), second_c),
        ("third overlap agrees on original x", (x**2*y).at(x*y, yi), x**2*y),
        ("third overlap agrees on original y", (x**3*y).at(x*y, yi), x**3*y**2),
        ("Bezier u=v²: controls L², -L², L² with L=3/2",
         9*(1-x)**2 - 18*x*(1-x) + 9*x**2, (-3+6*x)**2),
    ]
    for name, left, right in rows:
        if left != right:
            raise AssertionError(name)
    exponents = {
        "E1 in first u-chart": min(i for i, j in first_u.terms),
        "E1 strict in second a-chart": min(j for i, j in second_a.terms),
        "E2 in second a-chart": min(i for i, j in second_a.terms),
        "E1 strict in third p-chart": min(j for i, j in third_p.terms),
        "E2 strict in third t-chart": min(j for i, j in third_t.terms),
        "E3 in third p-chart": min(i for i, j in third_p.terms),
        "E3 in third t-chart": min(i for i, j in third_t.terms),
    }
    expected = [2, 2, 3, 2, 3, 6, 6]
    if list(exponents.values()) != expected:
        raise AssertionError("Total component multiplicities")
    return {"identities": [name for name, _, _ in rows], "component_multiplicities": exponents}


INK, MUTED, BLUE, ORANGE = "#172b3d", "#4c6171", "#146aa5", "#bf4d16"
WIDTH, HEIGHT = 720, 2640
PROOF_URL = "../SH03-subanalytic-sets-and-limiting-tangent-directions.html#keeping-the-whole-function-through-a-resolution"
SOURCE_URL = "https://www.math.toronto.edu/bierston/inventionnes.ps"


class Figure:
    def __init__(self, proof_url):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
            f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">',
            '<title id="title">Three blow-ups of the cusp y² − x³: total multiplicities</title>',
            '<desc id="desc">Four vertically stacked affine-coordinate panels. The first '
            'shows tangency of u=v² to u=0. The second shows three concurrent lines '
            'a=0, b=0 and a=b. The last two show the two charts of the third blow-up, '
            'where the exceptional multiplicity is six and at most two branches meet '
            'transversely. The q=1 and w=1 intersections are the same point. '
            'The q=0 and w=0 old-divisor directions are different; neither is falsely '
            'included in the other affine chart.</desc>',
            '<metadata>Original programme figure and generator: CC0 1.0. '
            'Human framework reference: Edward Bierstone and Pierre D. Milman, '
            'Canonical desingularization in characteristic zero by blowing up the '
            'maximum strata of a local invariant; author manuscript, 25 November 1996. '
            'The displayed cusp chart computations are independently expressed. '
            'Proof locator: #keeping-the-whole-function-through-a-resolution, PF8–PF10. '
            'This example does not prove a general resolution theorem.</metadata>',
            '<style>text{font-family:Arial,"Segoe UI",sans-serif;font-style:normal;fill:#172b3d}'
            '.label{paint-order:stroke;stroke:#fff;stroke-width:5;stroke-linejoin:round}'
            'a text{text-decoration:underline} .grid{stroke:#e1e8ed;stroke-width:1}'
            '.axis{stroke:#a8b6c0;stroke-width:1.5;stroke-dasharray:5 5}</style>',
            '<rect width="720" height="2640" fill="#fff"/>',
        ]
        self.proof_url = proof_url

    def add(self, value):
        self.parts.append(value)

    def text(self, x, y, value, size=24, fill=INK, weight=None, anchor="start", label=False):
        attrs = f' x="{x:g}" y="{y:g}" font-size="{size:g}" text-anchor="{anchor}" style="fill:{fill}"'
        if weight:
            attrs += f' font-weight="{weight}"'
        if label:
            attrs += ' class="label"'
        self.add(f'<text{attrs}>{escape(value)}</text>')

    def line(self, x1, y1, x2, y2, color, width=4, css=None):
        attrs = f' class="{css}"' if css else ""
        self.add(f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" stroke-width="{width:g}"{attrs}/>')

    def point(self, x, y, centre=False):
        radius = 8 if centre else 5
        self.add(f'<circle cx="{x:g}" cy="{y:g}" r="{radius}" fill="white" stroke="{INK}" stroke-width="2.5"/>')

    def panel(self, top, title, chart, formula, limits, names):
        self.add(f'<rect x="24" y="{top}" width="672" height="500" rx="16" fill="#fafcfd" stroke="#cad8e1" stroke-width="1.5"/>')
        self.text(44, top+35, title, 26, weight="700")
        self.text(44, top+70, chart, 24, MUTED)
        self.text(44, top+111, formula, 30, weight="600")
        return Plot(self, 60, top+140, 600, 270, limits, names)

    def output(self):
        return "\n".join(self.parts + ["</svg>\n"])


class Plot:
    def __init__(self, figure, left, top, width, height, limits, names):
        self.figure, self.left, self.top = figure, left, top
        self.width, self.height = width, height
        self.xmin, self.xmax, self.ymin, self.ymax = limits
        figure.add(f'<rect x="{left}" y="{top}" width="{width}" height="{height}" fill="#fff" stroke="#d8e2e9"/>')
        for x in (-1, 0, 1, 2):
            if self.xmin < x < self.xmax:
                figure.line(self.X(x), top, self.X(x), top+height, "#e1e8ed", 1, "grid")
        for y in (-1, 0, 1):
            if self.ymin < y < self.ymax:
                figure.line(left, self.Y(y), left+width, self.Y(y), "#e1e8ed", 1, "grid")
        figure.line(left, self.Y(0), left+width, self.Y(0), "#a8b6c0", 1.5, "axis")
        figure.line(self.X(0), top, self.X(0), top+height, "#a8b6c0", 1.5, "axis")
        figure.text(left+width-8, self.Y(0)+29, names[0], 25, MUTED, anchor="end", label=True)
        figure.text(self.X(0)-13, top+25, names[1], 25, MUTED, anchor="end", label=True)

    def X(self, x):
        return self.left + (x-self.xmin)*self.width/(self.xmax-self.xmin)

    def Y(self, y):
        return self.top + (self.ymax-y)*self.height/(self.ymax-self.ymin)

    def horizontal(self, y, color=BLUE):
        self.figure.line(self.left, self.Y(y), self.left+self.width, self.Y(y), color, 4.5)

    def vertical(self, x, color=BLUE):
        self.figure.line(self.X(x), self.top, self.X(x), self.top+self.height, color, 4.5)

    def label(self, dx, dy, value, color=INK):
        self.figure.text(self.left+dx, self.top+dy, value, 25, color, label=True)


def make_svg(proof_url=PROOF_URL):
    f = Figure(proof_url)
    f.text(32, 48, "Three blow-ups of y² − x³", 35, weight="700")
    f.text(32, 84, "Keeping the total function and its multiplicities", 24, MUTED)
    f.line(34, 118, 72, 118, BLUE, 4.5)
    f.text(82, 126, "exceptional divisors", 23, BLUE)
    f.line(374, 118, 412, 118, ORANGE, 4.5)
    f.text(422, 126, "weak zero curve", 23, ORANGE)
    f.text(32, 158, "Numbers in parentheses are total multiplicities.", 23, MUTED)

    p = f.panel(184, "A · First blow-up: tangency remains", "x=u, y=uv", "f ∘ π₁ = u²(v² − u)", (-.5, 2.5, -1.5, 1.5), ("u", "v"))
    p.vertical(0)
    # Exact quadratic parametrization: v=-L+2Lt, u=v². With L=3/2,
    # the Bezier u-controls are L², -L², L² and v-controls -L,0,L.
    L = 1.5
    f.add(f'<path d="M {p.X(L*L):g},{p.Y(-L):g} Q {p.X(-L*L):g},{p.Y(0):g} {p.X(L*L):g},{p.Y(L):g}" fill="none" stroke="{ORANGE}" stroke-width="4.5"/>')
    p.label(118, 35, "E₁: u=0 (2)", BLUE)
    p.label(330, 64, "C₁: u=v² (1)", ORANGE)
    f.point(p.X(0), p.Y(0), centre=True)
    f.text(44, 630, "Blow up the marked point (u,v)=(0,0).", 24)
    f.text(44, 665, "The smooth weak curve is tangent to E₁.", 24, MUTED)

    p = f.panel(708, "B · Second blow-up: three lines meet", "u=ab, v=a", "f ∘ π₂ = a³b²(a − b)", (-1.5, 1.5, -1.5, 1.5), ("a", "b"))
    p.vertical(0)
    p.horizontal(0)
    f.line(p.X(-1.5), p.Y(-1.5), p.X(1.5), p.Y(1.5), ORANGE, 4.5)
    p.label(320, 33, "E₂: a=0 (3)", BLUE)
    p.label(329, 177, "E₁′: b=0 (2)", BLUE)
    p.label(20, 43, "C₂: a=b (1)", ORANGE)
    f.point(p.X(0), p.Y(0), centre=True)
    f.text(44, 1154, "Blow up the marked point (a,b)=(0,0).", 24)
    f.text(44, 1189, "Three branches on a surface are not SNC.", 24, MUTED)

    p = f.panel(1232, "C · Third blow-up: the (p,q)-chart", "a=p, b=pq", "f ∘ π₃ = p⁶q²(1 − q)", (-1.5, 1.5, -.5, 1.5), ("p", "q"))
    p.vertical(0)
    p.horizontal(0)
    p.horizontal(1, ORANGE)
    p.label(18, 32, "E₃: p=0 (6)", BLUE)
    p.label(376, 250, "E₁″: q=0 (2)", BLUE)
    p.label(387, 56, "C₃: q=1 (1)", ORANGE)
    f.point(p.X(0), p.Y(0))
    f.point(p.X(0), p.Y(1))
    f.text(44, 1678, "E₁″ and C₃ meet E₃ transversely.", 24)
    f.text(44, 1713, "The E₂′ direction is in the other chart.", 24, MUTED)

    p = f.panel(1756, "D · Third blow-up: the (t,w)-chart", "b=t, a=tw", "f ∘ π₃ = t⁶w³(w − 1)", (-1.5, 1.5, -.5, 1.5), ("t", "w"))
    p.vertical(0)
    p.horizontal(0)
    p.horizontal(1, ORANGE)
    p.label(18, 32, "E₃: t=0 (6)", BLUE)
    p.label(371, 250, "E₂′: w=0 (3)", BLUE)
    p.label(382, 56, "C₃: w=1 (1)", ORANGE)
    f.point(p.X(0), p.Y(0))
    f.point(p.X(0), p.Y(1))
    f.text(44, 2202, "E₂′ and C₃ meet E₃ transversely.", 24)
    f.text(44, 2237, "The E₁″ direction is in the other chart.", 24, MUTED)

    f.text(32, 2301, "Overlap: q ≠ 0, w ≠ 0;  t=pq, w=1/q.", 25, weight="600")
    f.text(32, 2340, "The q=1 and w=1 crossings are the same point.", 24)
    f.text(32, 2377, "The q=0 and w=0 directions are distinct.", 24)
    f.text(32, 2414, "New multiplicity: 6 = 1 + 2 + 3.", 25, weight="600")
    f.text(32, 2449, "Weak order + both old divisor multiplicities.", 24, MUTED)
    f.add(f'<a href="{escape(proof_url, {chr(34): "&quot;"})}">')
    f.text(32, 2500, "Proof: Keeping the whole function, PF8–PF10.", 23)
    f.add('</a>')
    f.add(f'<a href="{SOURCE_URL}">')
    f.text(32, 2535, "Framework: Bierstone–Milman, author ms. (1996).", 23)
    f.add('</a>')
    f.text(32, 2573, "Exact chart illustration; axis scales may differ.", 22, MUTED)
    f.text(32, 2608, "Original programme figure and generator · CC0 1.0", 22, MUTED)
    return f.output()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".svg"))
    parser.add_argument("--proof-url", default=PROOF_URL)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    report = check_identities()
    report["status"] = "passed"
    if not args.check_only:
        data = make_svg(args.proof_url).encode("utf-8")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(data)
        report["svg_sha256"] = hashlib.sha256(data).hexdigest()
        report["svg_path"] = str(args.output)
        report["canvas"] = [WIDTH, HEIGHT]
    if args.receipt:
        args.receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
