from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.hashsalt": "AN01-U163"})
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8), layout="constrained")
ax = axes[0]
t = np.linspace(-1, 1, 401)
ax.fill_betweenx(t, -np.abs(t), np.abs(t), color="#c7e2f2", alpha=.8)
ax.plot(np.abs(t), t, color="#236991")
ax.plot(-np.abs(t), t, color="#236991")
ax.axhline(0, color="#333333", linewidth=.8)
ax.axvline(0, color="#888888", linewidth=.6)
for s in [-.5, .5]:
    ax.plot([-.5, .5], [s, s], color="#ae4c25", linewidth=3)
    ax.scatter([-.5, .5], [s, s], color="#ae4c25", s=22, zorder=5)
ax.text(.1, .76, r"$|a|\leq |t|$", fontsize=12)
ax.text(.58, .48, r"$t=1/2$", color="#ae4c25")
ax.text(.58, -.54, r"$t=-1/2$", color="#ae4c25")
ax.set(xlim=(-1.15, 1.15), ylim=(-1.08, 1.08),
       xlabel="tangential input a, with output x = 0", ylabel="normal scale t",
       title="Both sides use a shrinking input interval")
ax.set_aspect("equal")
ax = axes[1]
for r in range(1, 7):
    e = 2.**(-r)
    ax.plot([-e, e], [r, r], color="#236991", linewidth=6, solid_capstyle="butt")
    ax.scatter([-e, e], [r, r], color="#236991", s=24)
    ax.text(e + .025, r, rf"$\varepsilon_{r}=2^{{-{r}}}$", va="center", fontsize=10)
ax.axvline(0, color="#888888", linewidth=.8, linestyle="--")
ax.set(xlim=(-.56, .82), ylim=(6.6, .35), yticks=range(1, 7),
       xlabel="normal variable t", ylabel="degree r",
       title="Illustrative cutoff supports")
ax.text(-.53, 6.47, "Actual widths also depend on the data.", fontsize=9, color="#4a4a4a")
for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
fig.savefig(out / "normal-jet-scales.png", dpi=160, metadata={"Software": "Matplotlib; GPT-6 Astra (OpenAI)"})
svg = out / "normal-jet-scales.svg"
fig.savefig(svg, metadata={"Date": None, "Creator": "GPT-6 Astra (OpenAI)"})
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n", encoding="utf-8", newline="\n")
