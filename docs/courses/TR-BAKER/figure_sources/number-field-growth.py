"""Reproduce Figure 16.1 from exact Gaussian cyclotomic values."""
from pathlib import Path
import importlib.util
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "primitive_check", HERE.parent/"verification"/"number-field-primitive-check.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
rows = check.gaussian_norm_data()
n = [r["n"] for r in rows]
y = [math.log(r["norm"]) for r in rows]
fig, ax = plt.subplots(figsize=(9.3, 4.5), layout="constrained")
ax.plot(n, y, color="#236c9e", linewidth=1, alpha=.45)
ax.scatter(n, y, color="#236c9e", s=16,
           label=r"Computed $\log N\mathfrak{C}_n$ for $\gamma=1+i$")
ax.plot(n, [2*math.log(k) for k in n], color="#ad4b30",
        linestyle="--", linewidth=2,
        label=r"Nonprimitive upper bound $2\log n$ (for $n>36$)")
ax.set(xlabel=r"Index $n$", ylabel="Natural logarithm of ideal norm",
       title="A cyclotomic ideal must acquire a new prime ideal")
ax.set_xlim(39, 101)
ax.set_ylim(0, max(y)*1.12)
ax.grid(alpha=.18)
ax.legend(loc="upper left", frameon=True, fontsize=9)
fig.savefig(HERE.parent/"figures"/"number-field-growth.png", dpi=160)
plt.close(fig)
