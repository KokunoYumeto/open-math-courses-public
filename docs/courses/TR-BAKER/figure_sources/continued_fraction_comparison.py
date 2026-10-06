"""Reproduce the certified two-logarithm comparison figure.

Original figure: GPT-6.1 Sol (OpenAI), in Codex, Ultra; October 2026.
CC0. Data are computed by the accompanying exact rational certificate.
Font glyphs retain their own notices in assets/notices.
"""
from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter

root = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/"verification"))
from continued_fraction_comparison import RESULT
rows = RESULT["rows"]
x = [r["index"] for r in rows]
actual = [-r["log_absolute_form_decimal_approximation"] for r in rows]
general = [-r["general_log_lower_bound_decimal_approximation"] for r in rows]
sharp = [-r["sharp_log_lower_bound_decimal_approximation"] for r in rows]

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12})
fig,ax = plt.subplots(figsize=(10.2,4.6))
fig.patch.set_facecolor("#fbfbf8");ax.set_facecolor("#fbfbf8")
ax.plot(x,general,color="#b86738",lw=2.1,label="Upper bound on cost: constant 21600")
ax.plot(x,sharp,color="#26736b",lw=2.1,label="Upper bound on cost: constant 25.2")
ax.plot(x,actual,color="#223e63",lw=2,marker="o",ms=4.5,label="Actual cost at the convergent")
ax.set_yscale("log")
ax.set_xlim(.6,16.4);ax.set_xticks([1,4,8,12,16])
ax.set_xlabel("Index of the convergent of log 3 / log 2")
ax.set_ylabel("Cost = −log |p log 2 − q log 3|\n(logarithmic axis)")
ax.set_title("Certified values and uniform lower bounds",loc="left",fontsize=16,pad=14)
ax.grid(axis="y",which="major",color="#d9dedb",lw=.7)
ax.yaxis.set_major_locator(LogLocator(base=10))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.spines[["top","right"]].set_visible(False)
ax.legend(loc="center right",frameon=True,facecolor="#fbfbf8",edgecolor="#cfd5d0",fontsize=10.5)
fig.tight_layout()
out=root/"figures"/"continued-fraction-comparison.png"
out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=180,bbox_inches="tight")
print(out)
