"""Reproduce the original predual-smoothing diagram with no external library."""
from pathlib import Path
import sys
SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="960" height="930" viewBox="0 0 960 930" role="img" aria-labelledby="title desc">
<title id="title">From quasi-equivalence to a continuous normal action</title>
<desc id="desc">For a nondegenerate representation on separable H, bounded sequential density makes scalar normal orbits Borel. Haar averages are normal by a faithful-state reduction from increasing nets to sequences. Left translation makes each average orbit norm continuous. Countably many separating tests on one finite-measure open set prove that the averages span a norm-dense subspace of the predual, which gives continuity for all normal functionals.</desc>
<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0 0L8 3L0 6Z" fill="#275866"/></marker></defs>
<rect width="960" height="930" fill="#faf9f5"/>
<g font-family="Georgia,serif" fill="#152e38">
<text x="40" y="48" font-size="28" font-weight="bold">Continuity comes from the whole predual</text>
<text x="40" y="76" font-size="18">Point-norm action α on A; nondegenerate π on a separable Hilbert space H.</text>
<text x="40" y="99" font-size="18">G arbitrary LCH; π ∘ αₛ is quasi-equivalent to π for every s ∈ G.</text>
<rect x="35" y="108" width="890" height="143" rx="12" fill="#e4eff0" stroke="#72949d"/>
<text x="58" y="143" font-size="23" font-weight="bold">QI1 · Bounded sequences give scalar measurability</text>
<text x="58" y="178" font-size="21">π(aₙ) → x strongly*, with ‖π(aₙ)‖ ≤ ‖x‖</text>
<text x="58" y="209" font-size="21">ω(βₜ(x)) = limₙ ω(π(αₜ(aₙ)))</text>
<text x="58" y="237" font-size="18">Each approximating scalar orbit is continuous; the limit is Borel.</text>
<path d="M480 257V283" stroke="#275866" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="35" y="292" width="890" height="153" rx="12" fill="#eef0e3" stroke="#8d9874"/>
<text x="58" y="327" font-size="23" font-weight="bold">QI2 · The Haar averages are normal</text>
<text x="58" y="361" font-size="21">Ω(f,ω)(x) = ∫ f(t) ω(βₜ⁻¹(x)) dt          Tₛω = ω ∘ βₛ⁻¹</text>
<text x="58" y="393" font-size="19">A faithful normal state selects xᵢₙ ↑ x from every bounded xᵢ ↑ x.</text>
<text x="58" y="423" font-size="19">Scalar monotone convergence + NF1–4 ⇒ Ω(f,ω) belongs to P<tspan baseline-shift="sub" font-size="14">∗</tspan>.</text>
<path d="M480 451V477" stroke="#275866" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="35" y="486" width="890" height="139" rx="12" fill="#e4eff0" stroke="#72949d"/>
<text x="58" y="521" font-size="23" font-weight="bold">QI2 · Left translation gives norm continuity</text>
<text x="58" y="556" font-size="21">Tₛ Ω(f,ω) = Ω(Lₛf,ω)          Lₛf(t) = f(s⁻¹t)</text>
<text x="58" y="590" font-size="21">‖Tₛ Ω(f,ω) − Ω(f,ω)‖ ≤ ‖Lₛf − f‖₁ ‖ω‖ → 0</text>
<text x="58" y="614" font-size="17">Left Haar measure is used throughout; no modular factor is omitted.</text>
<path d="M480 631V657" stroke="#275866" stroke-width="3" marker-end="url(#arrow)"/>
<rect x="35" y="666" width="890" height="178" rx="12" fill="#eef0e3" stroke="#8d9874"/>
<text x="58" y="701" font-size="23" font-weight="bold">QI3 · The averages span a norm-dense subspace of P<tspan baseline-shift="sub" font-size="14">∗</tspan></text>
<text x="58" y="735" font-size="19">An annihilator x gives countably many scalar tests hₙ = 0 a.e.</text>
<text x="58" y="766" font-size="19">Use one open V with 0 &lt; Haar(V) &lt; ∞ to choose a common parameter.</text>
<text x="58" y="797" font-size="19">All normal tests then kill βₜ⁻¹(x), hence x = 0.</text>
<text x="58" y="827" font-size="20">‖Tₛω − ω‖ ≤ 2‖ω − η‖ + ‖Tₛη − η‖   for averaged η</text>
<text x="40" y="879" font-size="18">P = π(A)″; P<tspan baseline-shift="sub" font-size="14">∗</tspan> is the predual. Arrows are proved implications.</text>
<text x="40" y="908" font-size="16">Mathematical antecedent: M. Takesaki, Theory of Operator Algebras II, X.3.1.</text>
</g></svg>
"""
def main():
    target=Path(__file__).with_name("predual-smoothing.svg")
    data=SVG.encode("utf-8")
    if "--check" in sys.argv:
        if target.read_bytes()!=data: raise SystemExit("SVG differs from its reproducible source.")
        print("Exact SVG reproduction verified.")
    else:
        target.write_bytes(data)
        print(target.name)
if __name__=="__main__": main()
