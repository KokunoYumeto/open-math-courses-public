"""Reproduce Figure 80.1 from exact operator and vector frequencies."""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "80-spectral-sum-kernel-data.json").read_text(encoding="utf-8"))
assert data["schema"] == "oa-flow-figure80/v1"
E, F = data["operator_frequencies"], data["vector_frequencies"]
pairs = sorted((p, e + p) for p in F for e in E)
assert [list(pair) for pair in pairs] == sorted(data["pairs_p_q"])
assert sorted(set(q for _, q in pairs)) == data["output_frequencies"]
assert data["excluded_test_frequency"] not in data["output_frequencies"]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13})
fig, (ax, lower) = plt.subplots(2, 1, figsize=(13, 9), dpi=125,
                               gridspec_kw={"height_ratios": [3, 1]})
fig.patch.set_facecolor("#fbfcfd")
ax.set_facecolor("#fbfcfd")
ax.set_xlim(-.75, 3.85)
ax.set_ylim(-1.9, 6.2)
ax.set_xticks(F, [str(p) for p in F])
ax.set_yticks([-1, 2, 4, 5], ["-1", "2", "4", "5"])
ax.set_xlabel("vector frequency p", color="#173447", labelpad=8)
ax.set_ylabel("output frequency q", color="#173447", labelpad=8)
ax.set_title("The product h(q) g(q-p) f(p)", fontsize=20,
             weight="bold", color="#173447", pad=18)
ax.grid(True, color="#d9e2e7", linewidth=1)
for p, q in pairs:
    ax.scatter(p, q, s=470, color="#1b7897", edgecolor="white", linewidth=2,
               zorder=4)
    ax.annotate(f"q-p = {q-p}", (p, q), xytext=(10, 10), textcoords="offset points",
                color="#173447", fontsize=12, weight="bold")
ax.axhline(data["excluded_test_frequency"], color="#ae5b51",
           linestyle="--", linewidth=2.5)
ax.text(1.5, 4.18, "h near q=4: no matching pair", ha="center",
        color="#ae5b51", fontsize=14, weight="bold")
ax.text(1.5, 5.58, "Filled points: p in F and q-p in E", ha="center",
        color="#1b7897", fontsize=14)
for spine in ax.spines.values():
    spine.set_color("#a8bac4")

lower.axis("off")
lower.set_facecolor("#fbfcfd")
lower.text(.02, .8, "Exact Minkowski sum", fontsize=18, weight="bold",
           color="#173447", transform=lower.transAxes)
lower.text(.02, .45, "E = {-1, 2}     F = {0, 3}     E + F = {-1, 2, 5}",
           fontsize=17, color="#1b7897", transform=lower.transAxes)
lower.text(.02, .12, "Frequency 2 has two routes: -1 + 3 and 2 + 0.",
           fontsize=14, color="#597284", transform=lower.transAxes)
fig.tight_layout(pad=2.2)
fig.savefig(HERE / "80-spectral-sum-kernel.png", dpi=125,
            facecolor=fig.get_facecolor(), metadata={"Software": "OA-FLOW Figure 80.1"})
plt.close(fig)
