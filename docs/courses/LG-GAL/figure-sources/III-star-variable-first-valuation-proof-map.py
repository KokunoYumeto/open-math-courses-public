"""Reproduce the complete locally proved variable-k III-star mechanism."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(9, 29), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 9), ylim=(0, 29)); ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.text(4.5, 28.45, 'III* with arbitrary first valuation k', ha='center',
        fontsize=21, fontweight='bold')
ax.text(4.5, 27.96, 'A base scalar approximation makes a finite residue induction possible',
        ha='center', fontsize=12.3)

def box(y, h, title, body, locator, color, size=12):
    ax.add_patch(FancyBboxPatch((.52, y), 7.96, h,
        boxstyle='round,pad=.02,rounding_size=.17', facecolor=color,
        edgecolor='#365675', linewidth=1.5))
    ax.text(4.5, y+h-.4, title, ha='center', fontsize=16, fontweight='bold')
    ax.text(4.5, y+h/2-.06, body, ha='center', va='center',
            fontsize=size, linespacing=1.65)
    ax.text(4.5, y+.17, locator, ha='center', fontsize=10.2, color='#365675')

box(24.08, 3.36, 'Exact post-translation hypotheses',
    'v(π) = 1; e = v(2); finite k = v(a₁) ≥ 4; z = v(a₃)\n'
    'v(a₂) ≥ 2; v(a₄) = 3; v(a₆) ≥ 6\n'
    'e ≥ k; 4e ≥ 5k − 8; z ≥ k + 2; 4z ≥ 5k + 4\n'
    'z = +∞ is allowed; test these bounds after Lemma 6.0D\n'
    'c² = −3; A₀ = a₄/c; t = x² + A₀; d = 4k + 6; M = 8',
    '6.0V.1–2: VK1–VK4; no arbitrary-translation preservation assumed', '#edf4ff')
box(20.19, 3.34, 'The entire quartic integer ring',
    'v(x) = 3/2; v(t) = k + 9/4; τ = t/π^(k+2)\n'
    'Full basis: 1, x/π, t/π^(k+2), xt/π^(k+3)\n'
    'Upper valuation classes: 0, 2, 1, 3\n'
    'i₄ = 1 + (k + 2) + (k + 3) = 2k + 6\n'
    'D₄ = 2d − 2i₄ = 4k; τ is a quartic uniformizer',
    '6.0V.2: VK5; distinct classes prove full integrality', '#eaf7ef')
box(14.57, 5.06, 'A scalar approximates every needed power',
    'C₂ = b₄ − 2A₀; C₀ = b₈ + a₄²; N = π^(2k+4)\n'
    'Q = b₂A₀/(3N); β = (C₂A₀ − C₀/3)/N\n'
    'τ² = Qx + β + R₀; v(Q) = −1; v(β) ≥ 1\n'
    'R₀ = (−b₂xt/3 − C₂t − b₆x)/N; v(R₀) ≥ (k − 1)/2\n'
    'The two last margins are (4z − 5k − 4)/2 and (4e − 5k + 8)/2\n'
    'σ = −Q²A₀ + β² ∈ R; v(σ) = 1\n'
    'τ⁴ − σ = Q²t + 2Qxβ + 2(Qx + β)R₀ + R₀²\n'
    'v(τ⁴ − σ) ≥ k − 1 ⇒ v(τ^(4n) − σⁿ) ≥ k + n − 2\n'
    'For every n ≥ 6, the approximation error is at least k + 4',
    '6.0V.3: VK6–VK10; exact identity and unrestricted telescoping', '#fff5e6', 11.6)
box(9.35, 4.66, 'Exactly k − 2 residue cancellations',
    'H₂ = π²λ² − a₂; v(H₂) ≥ 3; w₁ = πλx\n'
    'E₁ = −xt + K + R₁; K = −H₂A₀ − a₆ ∈ R; v(K) ≥ 6\n'
    'v(R₁) ≥ k + 4; v(α₁) = k + 3/2; α₁ = a₁x + a₃ + 2w₁\n'
    'K₆ = K; Kₙ₊₁ = Kₙ + κₙ²σⁿ; v(Kₙ₊₁) ≥ n + 1\n'
    'n = 6, …, k + 3; κₙ ∈ R is one residue square-root lift\n'
    'S = Σ κₙτ^(2n); v(S) ≥ 3\n'
    'E = E₁ + α₁S + S² = −xt + errors of value ≥ k + 4\n'
    'v(E) = k + 15/4; v(a₁x + a₃ + 2w₁ + 2S) = k + 3/2',
    '6.0V.4: VK11–VK14; scalar errors, cross terms and traces bounded', '#eaf7ef', 11.65)
box(6.2, 2.6, 'The entire point integer ring',
    'ℓ = 2k + 7; η = (y − w₁ − S)/τ^ℓ; full B₈ = B₄[η]\n'
    'Normalized constant: 4(k + 15/4) − 2ℓ = 1\n'
    'Normalized trace: 4(k + 3/2) − ℓ = 2k − 1\n'
    'Upper relative different: min(8e + 1, 4k − 2) = 4k − 2',
    '6.0V.5: VK15–VK16; Eisenstein ring and exact point index ℓ', '#edf4ff', 11.9)
box(2.74, 2.9, 'Different, indices, Swan and conductor',
    'D₈ = 2D₄ + (4k − 2) = 12k − 2\n'
    'i₈ = (6d − D₈)/2 = 6k + 19 = 2i₄ + ℓ\n'
    'ε₄ = 3; ε₈ = 7; ν = 0; δ = 4k − 3; f(E/K) = 4k − 1\n'
    '−Art(X/R) = 8 + 1 + (4k − 3) = 4k + 6 = d\n'
    'i₄ + ℓ = 4k + 13 = d + M − 1',
    '6.0V.5: VK16; wild quaternion proof establishes inertia invariants', '#edf4ff', 11.8)
ax.text(4.5, 1.94,
    'Base valuations: v(π) = 1. Quartic valuations: v_F(π) = 4.\n'
    'Point constants/traces use v_F; the relative different uses the upper valuation.\n'
    'Dⱼ are base discriminant exponents; iⱼ are R-lengths; ℓ is a B₄-length.',
    ha='center', va='center', fontsize=10.5, linespacing=1.65)
ax.text(4.5, .85,
    'Proofs: Lesson 8, Sections 6.0V.1–6, VK1–VK16; all stated k are covered.\nGeneral conductor–index identity: JM30–JM32, Section6.0BI.\nSource: Milne, Algebraic Number Theory, Prop. 7.55 / Rem. 7.56.',
    ha='center', va='center', fontsize=10.3, linespacing=1.65)
dest = Path(__file__).resolve().parents[1]/'assets/III-star-variable-first-valuation-proof-map.png'
fig.savefig(dest, dpi=100, metadata={'Title': 'Full-ring proof for the variable-first-valuation III-star family'})
plt.close(fig)
print(dest.name)
