"""CC0 original exact finite examples for Sections 9 and 10 of L25."""
from pathlib import Path
from fractions import Fraction
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OWN = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "svg.fonttype": "none", "svg.hashsalt": "OA-FLOW-L25-original-20261004"})
P = np.array([1, 2, 0, -1, 1], dtype=int)
Q = np.array([1, 0, 1, 1, -1], dtype=int)
numerator_K = np.outer(P, Q)
numerator_F = np.array([[P[x]*Q[(x+s) % 5] for s in range(5)] for x in range(5)])
K = numerator_K/(2*np.sqrt(7))
F = numerator_F/(2*np.sqrt(7))

def kernel(f):
    return np.array([[f[x, (y-x) % 5] for y in range(5)] for x in range(5)])

def convolution(f, h):
    return np.array([[sum(f[x, r]*h[(x+r) % 5, (t-r) % 5]
                         for r in range(5)) for t in range(5)] for x in range(5)])

def involution(f):
    return np.array([[np.conjugate(f[(x+s) % 5, (-s) % 5])
                      for s in range(5)] for x in range(5)])

units = {}
for i in range(5):
    for j in range(5):
        f = np.zeros((5, 5), dtype=int)
        f[i, (j-i) % 5] = 1
        units[i, j] = f
        expected = np.zeros((5, 5), dtype=int)
        expected[i, j] = 1
        assert np.array_equal(kernel(f), expected)
for (i, j), f in units.items():
    assert np.array_equal(involution(f), units[j, i])
    for (k, ell), h in units.items():
        expected = units[i, ell] if j == k else np.zeros((5, 5), dtype=int)
        assert np.array_equal(convolution(f, h), expected)
        assert np.array_equal(kernel(convolution(f, h)), kernel(f)@kernel(h))
assert np.allclose(kernel(F), K, rtol=0, atol=1e-15)
assert np.linalg.matrix_rank(K) == 1
assert np.isclose(np.linalg.norm(K, 2), 1)
assert np.allclose(kernel(involution(F)), K.conj().T, rtol=0, atol=1e-15)

t = Fraction(7, 20)
probabilities = [t/3]*3+[(1-t)/2]*2
assert sum(probabilities) == 1
xi = np.sqrt(np.array([float(p) for p in probabilities]))
U = np.zeros((5, 5))
for i, j in [(0, 1), (1, 2), (2, 0), (3, 4), (4, 3)]:
    U[j, i] = 1
assert np.allclose(U@xi, xi)
projection = np.diag([1, 1, 1, 0, 0])
assert np.array_equal(projection@U, U@projection)
assert np.isclose(xi@projection@xi, float(t))
assert np.linalg.matrix_rank(U-np.eye(5)) == 3
for indices in [[0, 1, 2], [3, 4]]:
    block = U[np.ix_(indices, indices)]
    assert len(indices)-np.linalg.matrix_rank(block-np.eye(len(indices))) == 1

fig, axes = plt.subplots(1, 3, figsize=(16, 6), gridspec_kw={"width_ratios": [1, 1, 1.16]})
fig.subplots_adjust(left=.045, right=.98, top=.81, bottom=.30, wspace=.40)
fig.suptitle("Exact finite models: a crossed-product kernel and an invariant state",
             fontsize=20, fontweight="bold", y=.975)
fig.text(.5, .905, "C₅ right translation: K(x,y) = F(y−x)(x), with all indices modulo 5",
         ha="center", fontsize=15)

for ax, data, title, xlabel in [
    (axes[0], numerator_F, "Coefficient array F(s)(x)", "s"),
    (axes[1], numerator_K, "Kernel K(x,y) = p(x)q(y)", "y"),
]:
    ax.imshow(data, vmin=-2, vmax=2, cmap="RdBu_r", interpolation="nearest")
    ax.set_xticks(range(5)); ax.set_yticks(range(5))
    ax.set_xlabel(xlabel); ax.set_ylabel("x")
    ax.set_title(title, fontsize=14, pad=16)
    for x in range(5):
        for y in range(5):
            ax.text(y, x, str(data[x, y]), ha="center", va="center",
                    color="white" if abs(data[x, y]) == 2 else "#1b1b1b",
                    fontsize=15, fontweight="bold")
    ax.set_xticks(np.arange(-.5, 5, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 5, 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=.7)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.text(.5, -.20, "Every displayed entry is divided by 2√7",
            transform=ax.transAxes, ha="center", fontsize=11)

axes[1].text(.5, -.30, "p = (1,2,0,−1,1)/√7;  q = (1,0,1,1,−1)/2\n"
            "rank K = 1;  ‖K‖ = ‖p‖ ‖q‖ = 1",
            transform=axes[1].transAxes, ha="center", fontsize=11)
ax = axes[2]
colors = ["#246794"]*3+["#ba5a30"]*2
ax.bar(range(5), [float(p) for p in probabilities], color=colors, width=.67)
ax.set_xticks(range(5), ["a₀", "a₁", "a₂", "b₀", "b₁"])
ax.set_ylim(0, .39); ax.set_yticks([0, .1, .2, .3])
ax.set_ylabel("coordinate probability")
ax.set_title("C₆ action on a 3-cycle and a 2-cycle", fontsize=13, pad=16)
ax.spines[["top", "right"]].set_visible(False)
for i, p in enumerate(probabilities):
    ax.text(i, float(p)+.012, str(p), ha="center", fontsize=12)
ax.text(.5, -.20, "t = 7/20;  mass(O₃) = 7/20;  mass(O₂) = 13/20",
        transform=ax.transAxes, ha="center", fontsize=11)
ax.text(.5, -.31, "The joint commutant is ℂ ⊕ ℂ.\n"
        "At t = 0 or 1, discard the zero-weight orbit: it becomes ℂ.",
        transform=ax.transAxes, ha="center", fontsize=11)
fig.text(.5, .025, "Original CC0 illustration. Discrete matrix entries and probabilities are exact; "
         "Sections 9–10 and Exercises 11.2–11.3 prove the claims.", ha="center", fontsize=11)
for ext in ["png", "svg"]:
    fig.savefig(OWN/f"L25-original-finite-models.{ext}", dpi=160,
                metadata={"Date": "2026-10-04"})
plt.close(fig)

def file_record(p):
    b=p.read_bytes()
    return {"path":p.as_posix(), "sha256":hashlib.sha256(b).hexdigest(), "bytes":len(b)}
receipt = {
    "licence": "CC0",
    "scope": "Exact finite arithmetic supporting the illustrated examples, not a substitute for the proofs",
    "coefficient_numerator_rows_x_columns_s": numerator_F.tolist(),
    "kernel_numerator_rows_x_columns_y": numerator_K.tolist(),
    "common_denominator": "2*sqrt(7)",
    "matrix_unit_product_checks": 625,
    "matrix_unit_adjoint_checks": 25,
    "rank_one_kernel_norm": 1,
    "probabilities": [str(p) for p in probabilities],
    "invariant_state_parameter": str(t),
    "joint_commutant_dimensions": {"interior": 2, "endpoint_3cycle": 1, "endpoint_2cycle": 1},
    "proof_locators": ["Section 9", "Theorem 10.1", "equation (10.8)", "Exercises 11.2–11.3"],
    "checks_passed": True,
    "visual_qa": "Native PNG must be inspected separately before handoff",
    "files": [file_record(OWN/f"L25-original-finite-models.{ext}") for ext in ["svg", "png"]],
}
(OWN/"L25_FIGURE_AND_ARITHMETIC_CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"passed":True, "matrix_unit_products":625, "figure_files":receipt["files"]},indent=2))
