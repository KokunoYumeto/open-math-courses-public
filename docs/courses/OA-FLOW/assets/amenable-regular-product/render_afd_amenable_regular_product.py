"""Original deterministic SVG and exact convention checks; CC0-1.0.

Run Python -B. Default writes only the adjacent SVG. --check writes
nothing and compares the complete SVG bytes. No source/font copies or caches.
The finite arithmetic models check identities, not the infinite theorem.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def convention_checks():
    modulus = 11
    q = (0, 1, 4, 2)

    def mu(n, m):
        return (q[n] + q[m] - q[(n + m) % 4]) % modulus

    def omega(z, y, x):
        return mu((z - y) % 4, (y - x) % 4)

    for n in range(4):
        assert mu(0, n) == mu(n, 0) == 0
        for m in range(4):
            for l in range(4):
                assert (mu(n, m) + mu((n + m) % 4, l)
                        - mu(n, (m + l) % 4) - mu(m, l)) % modulus == 0

    h1 = lambda y, x: y // 2 == x // 2
    r1 = lambda x: 2 * (x // 2)
    c1 = {(y, x): omega(y, x, r1(x))
          for y in range(4) for x in range(4) if h1(y, x)}
    c2 = {(y, x): omega(y, x, 0) for y in range(4) for x in range(4)}
    a = {y: (c1[y, r1(y)] - c2[y, r1(y)]) % modulus for y in range(4)}
    b2 = {(y, x): (c2[y, x] + a[y] - a[x]) % modulus
          for y in range(4) for x in range(4)}
    assert any(c2[pair] != val for pair, val in c1.items())
    assert all(b2[pair] == val for pair, val in c1.items())
    for z in range(4):
        for y in range(4):
            for x in range(4):
                assert (b2[z, y] + b2[y, x] - b2[z, x]
                        - omega(z, y, x)) % modulus == 0
                assert (b2[z, x] + omega(z, y, x) - b2[y, x]
                        - b2[z, y]) % modulus == 0
    inverse_phase_fails = any(
        (-b2[z, x] + omega(z, y, x) + b2[y, x] - b2[z, y]) % modulus
        for z in range(4) for y in range(4) for x in range(4))
    assert inverse_phase_fails

    # Four-sheet exact example: the old relation has pairs {0,1}, {2,3}.
    old_matrix_units = {}
    for a_rank in range(2):
        for b_rank in range(2):
            arrows = {(2 * c + a_rank, 2 * c + b_rank) for c in range(2)}
            old_matrix_units[a_rank, b_rank] = arrows
            assert arrows == {(a_rank, b_rank), (2 + a_rank, 2 + b_rank)}
    for a_rank in range(2):
        for b_rank in range(2):
            assert {(x, y) for y, x in old_matrix_units[a_rank, b_rank]} == old_matrix_units[b_rank, a_rank]
            for c_rank in range(2):
                for d_rank in range(2):
                    composition = {(z, x)
                        for z, y in old_matrix_units[a_rank, b_rank]
                        for yy, x in old_matrix_units[c_rank, d_rank] if y == yy}
                    assert composition == (old_matrix_units[a_rank, d_rank]
                                           if b_rank == c_rank else set())

    # Finite-site semidirect sample checks only the action/product formula.
    def shift(bits, n):
        return tuple(bits[(i - n) % 3] for i in range(3))

    def plus(x, y):
        return tuple(a_bit ^ b_bit for a_bit, b_bit in zip(x, y))

    flips = [tuple((k >> i) & 1 for i in range(3)) for k in range(8)]
    elements = [(f, n) for f in flips for n in range(3)]

    def multiply(h, k):
        return (plus(h[0], shift(k[0], h[1])), (h[1] + k[1]) % 3)

    def act(h, x):
        return plus(h[0], shift(x, h[1]))

    for h in elements:
        for k in elements:
            for x in flips:
                assert act(multiply(h, k), x) == act(h, act(k, x))
            for l in elements:
                assert multiply(multiply(h, k), l) == multiply(h, multiply(k, l))

    return {
        "normalized_scalar_cocycle_mod_11": "pass",
        "independent_primitives_actually_disagree": "pass",
        "compatible_primitive_extension": "pass",
        "primitive_identity_all_64_triples": "pass",
        "multiplication_by_b_intertwiner_all_64_triples": "pass",
        "inverse_phase_detected_as_wrong": "pass",
        "four_sheet_exact_old_matrix_units": "pass",
        "finite_semidirect_action_and_associativity": "pass",
        "infinite_freeness_amenability_and_exhaustion": "proved_in_markdown_not_inferred_from_sample",
    }


def svg_bytes():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1090" viewBox="0 0 1440 1090" role="img" aria-labelledby="title desc">',
        '<title id="title">Amenable normal-subgroup regular product: actual sites, compatible primitive, and finite-pattern exhaustion</title>',
        '<desc id="desc">Three proof panels for equations A10, A13, A28 to A34, and A38 to A41. Site pairs are independent coordinates for n not equal to e outside finite flip support. The compatible cocycle primitive uses multiplication by b. Four sheets illustrate an exact matrix-unit inclusion; general finite patterns give increasing unital finite-dimensional algebras.</desc>',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 Z" fill="#425569"/></marker></defs>',
        '<rect width="1440" height="1090" fill="#f8fafc"/>',
        '<g font-family="sans-serif" fill="#172b43">']

    def rect(x, y, w, h, fill="white", stroke="#c7d2e0", radius=12):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

    def text(x, y, value, size=23, fill="#172b43", weight="normal", anchor="start"):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(value)}</text>')

    def line(x1, y1, x2, y2, arrow=False, stroke="#425569", dash=False):
        suffix = ' marker-end="url(#arrow)"' if arrow else ''
        if dash:
            suffix += ' stroke-dasharray="8 6"'
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="2.5"{suffix}/>')

    text(40, 48, 'The actual regular product is AFD when N is amenable', 32, weight="bold")
    text(40, 82, 'Countable G arbitrary  •  I = G × ℕ  •  every compatible (λ, μ)  •  proof locators below', 23)

    rect(28, 105, 1384, 279, "#eef5fc")
    text(52, 144, '1  Diagonal + finite-support flips; a free amenable action', 27, weight="bold")
    text(52, 183, 'X = {0,1}ᴵ with fair p;  F = ⊕ᴵ ℤ/2;  Γ = F ⋊ N', 25)
    text(52, 217, '(f,n) · x = f + n · x;  (f,n)(k,m) = (f + n·k, nm)', 23)
    text(52, 254, 'u₍f,n₎ = s_f L_n;   μ̃((f,n),(k,m)) = μ(n,m)', 23)
    text(52, 290, 'Trace: τμ(d u₍f,n₎) = 1₍f=0,n=e₎ ∫ d dp', 23)
    text(52, 338, 'Amenable Γ ⇒ R = ⋃ Hₖ on one invariant conull E.  [A10–A23; §5]', 22)
    text(917, 177, 'n ≠ e; j outside flipped levels', 21, weight="bold")
    for row, j in enumerate(['j₁', 'j₂', 'j₃']):
        yy = 201 + 43 * row
        rect(935, yy, 126, 33, "white", radius=6)
        rect(1166, yy, 196, 33, "white", radius=6)
        text(998, yy + 24, f'(e,{j})', 19, anchor="middle")
        text(1264, yy + 24, f'(n⁻¹,{j})', 19, anchor="middle")
        line(1073, yy + 17, 1153, yy + 17)
        text(1112, yy + 10, '=', 18, anchor="middle")
    text(917, 354, 'r independent equalities: p ≤ 2⁻ʳ → 0  [A13]', 18)

    rect(28, 404, 1384, 309, "#f3f0fc")
    text(52, 444, '2  Compatible finite-stage primitives remove the scalar twist', 27, weight="bold")
    rect(54, 474, 335, 126)
    text(72, 507, 'On Hₖ: δbₖ = ω', 24, weight="bold")
    text(72, 543, 'On Hₖ₊₁: δcₖ₊₁ = ω', 22)
    text(72, 578, 'cₖ₊₁(y,x) = ω(y,x,rₖ₊₁(x))', 20)
    rect(463, 474, 428, 126)
    text(484, 507, 'On Hₖ: dₖ = bₖ / cₖ₊₁', 23, weight="bold")
    text(484, 542, 'dₖ(y,x) = aₖ(y) / aₖ(x)', 22)
    text(484, 578, 'aₖ(y) = dₖ(y,rₖ(y))', 22)
    rect(965, 474, 421, 126)
    text(985, 507, 'bₖ₊₁(y,x) = cₖ₊₁(y,x)', 22, weight="bold")
    text(1050, 540, '× aₖ(y) / aₖ(x)', 23)
    text(985, 578, 'bₖ₊₁|Hₖ = bₖ  ⇒  b = ⋃ bₖ', 22)
    line(401, 534, 448, 534, arrow=True)
    line(903, 534, 950, 534, arrow=True)
    text(55, 641, 'ω(z,y,x) = b(z,y)b(y,x)/b(z,x);   (Bξ)(y,x) = b(y,x)ξ(y,x)', 25)
    text(55, 682, 'B Λω(a) B* = Λ₁(a b);   BUₕωB* = Mᵦₕ Vₕ.  Exact trace preserved.  [A28–A34]', 23)

    rect(28, 734, 1384, 287, "#eff8f3")
    text(52, 774, '3  Finite patterns give nested finite-dimensional algebras', 27, weight="bold")
    text(53, 814, 'Exact example: H₁ pairs; H₂ four sheets', 21)
    for index in range(4):
        x = 91 + 113 * index
        rect(x, 836, 70, 55, "white", radius=8)
        text(x + 35, 872, str(index), 25, weight="bold", anchor="middle")
    line(75, 907, 276, 907)
    line(301, 907, 502, 907)
    text(174, 934, '{0,1}', 20, anchor="middle")
    text(400, 934, '{2,3}', 20, anchor="middle")
    text(72, 982, 'e₀₁(old) = E₀₁ + E₂₃  inside M₄', 23)
    line(546, 881, 605, 881, arrow=True)
    text(635, 815, 'At stage k, class size d ≤ Kₖ:', 23, weight="bold")
    text(635, 853, 'record finitely many diagonal memberships,', 23)
    text(635, 887, 'generator targets, and every old matrix-unit map.', 23)
    text(635, 928, 'Aₖ = ⊕₍d, finite patterns C₎ M_d;   Aₖ₋₁ ⊂ Aₖ', 25, weight="bold")
    text(635, 975, 'Vₕ 1Dₕ,ₖ → Vₕ strongly;   Q = (⋃ Aₖ)″.  [A38–A41]', 23)

    text(40, 1048, 'Original proof schematic. Finite example is exact; it does not model every orbit.', 16)
    text(40, 1068, 'Human source question: Takesaki III, XVII.3 Exercise 5; relation input: current OA-ERGODIC Corollary 6.2.', 16)
    text(40, 1086, 'No classification or general crossed-product AFD theorem is used.', 16)
    parts.extend(['</g>', '</svg>'])
    result = ('\n'.join(parts) + '\n').encode('utf-8')
    root = ET.fromstring(result)
    assert root.attrib['viewBox'] == '0 0 1440 1090'
    assert 'A38–A41' in result.decode('utf-8')
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    checks = convention_checks()
    output = Path(__file__).resolve().with_name('afd-amenable-regular-product.svg')
    drawing = svg_bytes()
    if args.check:
        assert output.read_bytes() == drawing, 'SVG differs from deterministic source'
    else:
        output.write_bytes(drawing)
    print(json.dumps({'mode': 'check' if args.check else 'write',
                      'svg_bytes': len(drawing),
                      'svg_sha256': hashlib.sha256(drawing).hexdigest(),
                      'checks': checks}, ensure_ascii=False))


if __name__ == '__main__':
    main()
