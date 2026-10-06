"""CC0. Reproduce the exact global-class/measure diagram in Figure 12.1."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
out=root/'public/assets/global-jet-measure.svg'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" role="img" aria-labelledby="title desc">
<title id="title">A global secondary class and the sign of its measured index</title>
<desc id="desc">The two-jet projection on Borel spaces is a homotopy equivalence with contractible two-dimensional principal fiber. The invariant forms omega and beta give the pullback of the normalized Godbillon-Vey class as beta wedge d beta, equal to minus Omega, where Omega is the positive volume two nu. For a geometric K zero cycle y over the two-jet space, its positive measure trace is minus the evaluation of its geometric character against Omega. The proof uses an added even m-plane, an odd base dimension d, even normal rank r equal to three plus m minus d, and the signs epsilon d epsilon r equal to epsilon three plus m equal to minus epsilon m. The remaining comparison with the inverse two-step Thom map is explicitly open.</desc>
<metadata>Original mathematical diagram, CC0. Proposition 12.2 and Theorem 12.4. Human source: Alain Connes, transverse fundamental class, Section 7, Lemma 7.8.</metadata>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#285e86"/></marker></defs>
<style>text{font-family:Georgia,"DejaVu Serif",serif;fill:#17324a}.head{font-size:28px;font-weight:bold}.math{font-size:28px}.label{font-size:24px}.small{font-size:21px}.arrow{fill:none;stroke:#285e86;stroke-width:3;marker-end:url(#arrow)}</style>
<rect width="1200" height="800" fill="white"/>
<text x="30" y="43" class="head">The global class and the measured geometric sign</text>
<rect x="25" y="80" width="455" height="210" rx="12" fill="#eef4fb"/>
<rect x="720" y="80" width="455" height="210" rx="12" fill="#edf7ef"/>
<text x="50" y="127" class="math">Y₂ = (J₂⁺(S¹))Γ</text>
<text x="50" y="172" class="label">dω = β ∧ ω,   Ω = 2ν &gt; 0</text>
<text x="50" y="218" class="label">[β ∧ dβ]Γ = −[Ω]Γ</text>
<text x="50" y="261" class="small">Invariant form → bar total cocycle</text>
<text x="745" y="127" class="math">Y = (S¹)Γ</text>
<text x="745" y="172" class="label">GVY = B*(h₁c₁)</text>
<text x="745" y="218" class="label">π*GVY = −[Ω]Γ</text>
<text x="745" y="261" class="small">h₁ ↦ β,   c₁ ↦ dβ</text>
<path d="M490 145 L707 145" class="arrow"/>
<text x="535" y="125" class="label">π</text>
<text x="498" y="192" class="small">G₂ ≅ ℝ² fiber</text>
<text x="498" y="229" class="small">homotopy equivalence</text>
<rect x="25" y="325" width="570" height="265" rx="12" fill="#fff3e7"/>
<text x="48" y="367" class="head">A geometric cycle over Y₂</text>
<text x="48" y="412" class="label">y ∈ 𝒢₀(Z, Γ),   Ω = 2dy ∧ dp ∧ dq/p³</text>
<text x="48" y="457" class="label">T₂*(μZ y) = −⟨CZ(y), [Ω]Γ⟩</text>
<text x="48" y="500" class="small">TZ has three positive real line quotients.</text>
<text x="48" y="540" class="small">Â(τZ) = Td(τZ,ℂ) = 1 on the Borel space.</text>
<text x="48" y="573" class="small">All discrete Γ; compact relative support.</text>
<rect x="625" y="325" width="550" height="265" rx="12" fill="#eef4fb"/>
<text x="648" y="367" class="head">The normal reduction</text>
<text x="648" y="412" class="label">d odd,   m even,   D = 3 + m</text>
<text x="648" y="457" class="label">r = D − d even,   εk = (−1)ᵏ⁽ᵏ⁻¹⁾/²</text>
<text x="648" y="500" class="label">εd εr = εD = −εm</text>
<text x="648" y="540" class="small">Outward normal: +c₁(L)/2 exponent.</text>
<text x="648" y="573" class="small">Positive even Bott trace factor: +1.</text>
<rect x="25" y="625" width="1150" height="110" rx="12" fill="#f3f4f6"/>
<text x="48" y="666" class="label">Still required: compare the lifted proper cycle with (m₀Φ₂)⁻¹μ(x).</text>
<text x="48" y="710" class="small">The two statements above do not alone prove the full cyclic/GV geometric pairing.</text>
<text x="30" y="777" class="small">Proof locators: Lemma 12.1; Proposition 12.2; Lemma 12.3; Theorem 12.4. Connes, §7.</text>
</svg>
''',encoding='utf-8')
print(out.resolve())
