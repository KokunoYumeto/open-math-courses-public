"""CC0. Generate Figure11BL and check its exact finite operator arithmetic.

The full-domain, topological and family claims use the written proofs FBC.1–9.
This program uses only the Python standard library; no fonts are bundled.
"""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path


def operator(grade, character, n):
    if character == 1:
        return (1-grade, character, n), n+1
    if grade == 0:
        return (1, character, n-1), n if n else 0
    return (0, character, n+1), n+1


def exact_checks():
    rows = []
    for grade in (0, 1):
        for character in (1, -1):
            for n in range(17):
                node = (grade, character, n)
                out, a = operator(*node)
                if a:
                    back, b = operator(*out)
                    assert back == node and a == b
                    assert a*character == a*out[1]
                    square = a*b
                else:
                    assert node == (0, -1, 0)
                    square = 0
                expected = (n+1)**2 if character == 1 or grade == 1 else n*n
                assert square == expected
                rows.append(dict(input=node, output=out if a else None,
                                 weight=a, squared_weight=square,
                                 deck_commutator_zero=True))
    rotations = []
    for a,b in [(Q(1),Q(0)),(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13))]:
        assert a*a+b*b == 1
        # U=(a,-b;b,a), U^T U=I and U(-u)(-w)=U(u)w.
        u = ((a,-b),(b,a))
        gram = [[sum(u[k][i]*u[k][j] for k in range(2))
                 for j in range(2)] for i in range(2)]
        assert gram == [[Q(1),Q(0)],[Q(0),Q(1)]]
        w=(Q(2,7),Q(-3,11))
        image=tuple(sum(u[i][j]*w[j] for j in range(2)) for i in range(2))
        antipodal=tuple(sum((-u[i][j])*(-w[j]) for j in range(2)) for i in range(2))
        assert image == antipodal
        rotations.append(dict(z1=str(a),z2=str(b),unitary=True,antipodal_quotient_respected=True))
    labels=(0,1,0)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                assert ((labels[i]-labels[j])+(labels[j]-labels[k]))%2 == (labels[i]-labels[k])%2
    return dict(schema='flat-label-family-finite-checks/v1',basis_inputs=len(rows),
                operator_rows=rows,rational_unitary_samples=rotations,
                local_label_cocycle_tests=27,positive_kernel_character=-1,
                finite_checks_prove_infinite_domain_or_topology=False,
                full_proof='Section11BL, FBC.1–9, Exercises289–290',
                whole_base_unit_inferred_from_rank=False,
                physical_graph_realization_proved=False)


SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">
<metadata>Original mathematical expression and generator: CC0 1.0, to the extent of rights held. System fonts are not embedded. Proof: Section11BL, FBC.1–9. Human context: Alain Connes, A survey of foliations and operator algebras, Section8. This schematic does not assert compact-frame descent or a physical normal sum.</metadata>
<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0L10 4L0 8Z" fill="#304b71"/></marker></defs>
<rect width="1200" height="900" fill="white"/>
<g font-family="sans-serif" fill="#142943">
<text x="36" y="42" font-size="29" font-weight="bold">Flat-label family index and transverse disk calibration</text>
<text x="36" y="74" font-size="19">A pointwise index records rank. Label transitions also determine the family class.</text>
<rect x="28" y="101" width="564" height="360" rx="15" fill="#f0f5fd" stroke="#aac2df"/>
<rect x="608" y="101" width="564" height="360" rx="15" fill="#f7f1fb" stroke="#cbb8de"/>
<text x="50" y="135" font-size="23" font-weight="bold">Double cover and associated index line</text>
<ellipse cx="208" cy="218" rx="147" ry="48" fill="white" stroke="#304b71" stroke-width="2"/>
<circle cx="155" cy="218" r="7" fill="#734292"/><circle cx="262" cy="218" r="7" fill="#734292"/>
<text x="125" y="208" font-size="20">u</text><text x="268" y="208" font-size="20">−u</text>
<text x="375" y="223" font-size="23">S³</text>
<path d="M155 232L208 302M262 232L208 302" stroke="#304b71" stroke-width="2" fill="none" marker-end="url(#arrow)"/>
<circle cx="208" cy="318" r="7" fill="#304b71"/>
<text x="230" y="324" font-size="22">[u] ∈ RP³</text>
<text x="350" y="278" font-size="19">π(u)=π(−u)</text>
<text x="52" y="371" font-size="21">L = (S³ × C) / ((u,z) ∼ (−u,−z))</text>
<text x="52" y="405" font-size="20">Kernel transport has sign −1.</text>
<text x="52" y="437" font-size="19">Cover schematic; the drawn arrows represent π.</text>
<text x="632" y="135" font-size="23" font-weight="bold">The exact regular auxiliary</text>
<text x="634" y="181" font-size="21">H⁺ = H⁻ = ℓ²(Z/2) ⊗ ℓ²(N₀)</text>
<text x="634" y="221" font-size="21">Trivial-character pair: eigenvalues ±(n+1)</text>
<text x="634" y="258" font-size="21">Sign pair n ≥ 1: eigenvalues ±n</text>
<rect x="632" y="284" width="510" height="69" rx="9" fill="white" stroke="#b25b64"/>
<text x="648" y="313" font-size="21" fill="#9c303d">Unmatched positive sign line: e₋,₀</text>
<text x="648" y="339" font-size="18">D⁺e₋,₀ = 0; the negative kernel is zero.</text>
<text x="634" y="392" font-size="21">Index at every unit: +1</text>
<text x="634" y="433" font-size="21">Whole-base index: [L], with [L] ≠ [1]</text>
<rect x="28" y="479" width="1144" height="163" rx="15" fill="#fff6e8" stroke="#dab87c"/>
<text x="50" y="515" font-size="23" font-weight="bold">The transition carries a nonzero order-two K⁰ class</text>
<text x="50" y="552" font-size="21">An odd f:S³→S¹ would lift to ψ:S³→R; ψ(−u)−ψ(u) cannot be an odd multiple of π.</text>
<text x="50" y="590" font-size="21">U(u) = [ z₁  −z̄₂ ; z₂  z̄₁ ],   U*U=I,   U(−u)=−U(u).</text>
<text x="50" y="622" font-size="20">[u,w] ↦ ([u],U(u)w) trivializes L ⊕ L. Thus 2([L]−[1])=0, but [L]−[1] ≠ 0.</text>
<rect x="28" y="661" width="1144" height="155" rx="15" fill="#eef8f3" stroke="#96c8b0"/>
<text x="50" y="697" font-size="23" font-weight="bold">On one complete flat disk U: the bounded perturbation homotopy proves the unit</text>
<text x="50" y="735" font-size="21">Dⱼ = DΛ + Kⱼ  →  DΛ, on the same full domain.   ε|U = 1C₀(U).</text>
<text x="50" y="775" font-size="23">bU = βU [j]   ⇒   bU ⊗ ε = bU; the supplied Bott degree d and Clifford order remain.</text>
<text x="36" y="846" font-size="18">Proofs: 11BL, FBC.1–9; Exercises289–290. Original CC0 argument and schematic.</text>
<text x="36" y="874" font-size="18">Context: Connes, survey §8. Compact-frame descent and the physical graph sum remain separate.</text>
</g></svg>'''


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args(); args.output_dir.mkdir(parents=True,exist_ok=True)
    checks=exact_checks()
    (args.output_dir/'whole-base-flat-label-class.svg').write_text(SVG+'\n',encoding='utf-8',newline='\n')
    (args.output_dir/'WHOLE-BASE-FLAT-LABEL-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'basis_inputs':checks['basis_inputs'],'rational_unitary_samples':3,'local_label_cocycle_tests':27}))


if __name__=='__main__':
    main()
