"""Draw the GDA7 closed-graph proof of weight uniqueness."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "svg.hashsalt": "oa-flow-gns-weight-uniqueness",
    "font.size": 12,
})
DATA = {
    "proof": "OA-FLOW-GDA, GDA7",
    "kind": "logical schematic; no numerical approximation",
    "hypotheses": [
        "Phi and Psi are faithful normal semifinite weights on N",
        "sigma(Phi) = sigma(Psi)",
        "C is a linear subspace of n(Phi)",
        "Lambda(Phi)(C) is dense in H(Phi)",
        "Psi(a*a) = Phi(a*a) for every a in C",
    ],
    "steps": [
        "Psi = Phi_h for a positive nonsingular central h",
        "B = pi(Phi)(h)^(1/2) is positive and closed; E = Lambda(Phi)(C)",
        "||B xi|| = ||xi|| on E",
        "xi_n -> xi implies B xi_n is Cauchy; closedness puts xi in D(B)",
        "D(B) = H(Phi) and B*B = I; positivity gives B = I",
        "Faithfulness gives h = I; hence Psi = Phi on the full positive cone",
    ],
    "domains": {
        "initial": "E is a linear dense subset of D(B)",
        "conclusion": "D(B) = H(Phi), with no Hilbert separability hypothesis",
    },
}
fig = plt.figure(figsize=(16, 6), dpi=160, facecolor="#f8fafc")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ax.text(.5, .92, "A dense quadratic test determines the weight",
        ha="center", va="center", fontsize=24, color="#173a4b", weight="bold")
ax.text(.5, .84,
        r"Faithful n.s.f. weights $\Phi,\Psi$ with $\sigma^\Phi=\sigma^\Psi$; "
        r"$\Lambda_\Phi(\mathcal{C})$ is dense and $\Psi(a^*a)=\Phi(a^*a)$ on linear $\mathcal{C}$.",
        ha="center", va="center", fontsize=13, color="#355366")
boxes = [
    ("1. Central density",
     [r"$\Psi=\Phi_h$", r"$h\geq0,\quad\ker h=\{0\}$",
      "$h$ is affiliated with the center",
      "MA4, BC4, NC4, RF5, CZ1–6"]),
    ("2. The GNS identity",
     [r"$B=\pi_\Phi(h)^{1/2}$", r"$\mathcal{E}=\Lambda_\Phi(\mathcal{C})\subset D(B)$",
      r"$\|B\xi\|=\|\xi\|\quad(\xi\in\mathcal{E})$",
      r"$B$ is positive and closed"]),
    ("3. Close the graph",
     [r"$\xi_n\in\mathcal{E},\quad\xi_n\longrightarrow\xi$",
      r"$B\xi_n$ is Cauchy",
      r"$(\xi_n,B\xi_n)\longrightarrow(\xi,B\xi)$",
      r"$D(B)=H_\Phi$"]),
    ("4. Positivity fixes it",
     [r"$B^*B=I,\qquad B\geq0$", r"$B=I$",
      r"$h=1$ by faithfulness",
      r"$\Psi=\Phi$ on all $N_+$"]),
]
left, width, gap = .025, .22, .0225
for j, (title, lines) in enumerate(boxes):
    x = left + j * (width + gap)
    ax.add_patch(FancyBboxPatch((x, .31), width, .4,
                  boxstyle="round,pad=0.009,rounding_size=0.012",
                  facecolor="white", edgecolor="#577e94", linewidth=1.8))
    ax.text(x + width/2, .659, title, ha="center", va="center",
            fontsize=15, weight="bold", color="#173a4b")
    for k, text in enumerate(lines):
        ax.text(x + width/2, .575 - .066*k, text, ha="center", va="center",
                fontsize=12.5 if j else 11.5, color="#264958")
    if j < 3:
        ax.annotate("", xy=(x + width + gap - .004, .51),
                    xytext=(x + width + .004, .51),
                    arrowprops={"arrowstyle": "->", "lw": 2, "color": "#227c78"})
ax.text(.5, .215,
        r"The exact Cauchy estimate:  $\|B\xi_n-B\xi_m\|=\|\xi_n-\xi_m\|$.",
        ha="center", fontsize=16, color="#227c78")
ax.text(.5, .14,
        "Closedness proves the full domain; positivity then excludes every nonidentity isometry.",
        ha="center", fontsize=13, color="#355366")
ax.text(.5, .075,
        "GDA7 · Arbitrary Hilbert dimension · Logical schematic of the proved argument",
        ha="center", fontsize=11.5, color="#5b7081")
fig.savefig(ROOT / "gns-weight-uniqueness.png", dpi=160,
            metadata={"Software": "OA-FLOW figure source"})
fig.savefig(ROOT / "gns-weight-uniqueness.svg",
            metadata={"Date": None, "Creator": "OA-FLOW figure source"})
svg = ROOT / "gns-weight-uniqueness.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
               encoding="utf-8", newline="\n")
plt.close(fig)
(ROOT / "data.json").write_text(json.dumps(DATA, ensure_ascii=False, indent=2) + "\n",
                               encoding="utf-8")
