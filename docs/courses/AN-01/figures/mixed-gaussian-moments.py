"""Exact formula samples for polynomial Gaussian moments. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

out = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 12, "axes.titlesize": 14, "figure.facecolor": "white",
                     "axes.spines.top": False, "axes.spines.right": False,
                     "svg.hashsalt": "AN01-mixed-gaussian-moments"})
fig, axes = plt.subplots(1, 2, figsize=(12.4, 4.9), constrained_layout=True)
x = np.linspace(-1.5, 1.5, 501)
X, Y = np.meshgrid(x, x)
F = np.sqrt(3)/np.pi * X*Y * np.exp(-3*X**2 - 2*X*Y - 3*Y**2)
bound = np.max(np.abs(F))
im = axes[0].pcolormesh(X, Y, F, shading="auto", cmap="RdBu_r",
                       norm=TwoSlopeNorm(vmin=-bound, vcenter=0, vmax=bound),
                       rasterized=True)
axes[0].contour(X, Y, 3*X**2+2*X*Y+3*Y**2, levels=[1,2,4],
                colors="#333333", linewidths=.6, alpha=.55)
axes[0].axhline(0, color="#444444", lw=.6)
axes[0].axvline(0, color="#444444", lw=.6)
axes[0].set(xlabel=r"$x_1$", ylabel=r"$x_2$", aspect="equal",
            title="Signed integrand at t = 1")
fig.colorbar(im, ax=axes[0], fraction=.045, pad=.03, label="Exact formula values")
t = np.linspace(0, 1.5, 601)
M = -np.sqrt(3)*t/(2*((t+1)*(t+3))**1.5)
axes[1].plot(t, M, color="#116e7d", lw=2.5, label="Exact normalized moment")
small = np.linspace(0, .65, 160)
axes[1].plot(small, -small/6, "--", color="#aa4a16", lw=1.8,
             label=r"First-order expression $-t/6$")
value = -np.sqrt(6)/64
axes[1].scatter([1], [value], s=48, color="#116e7d", zorder=5)
axes[1].annotate(r"$(1,-\sqrt{6}/64)$", (1, value), xytext=(.8,-.078),
                 arrowprops={"arrowstyle":"->", "color":"#444444"}, fontsize=12)
axes[1].axhline(0, color="#777777", lw=.8)
axes[1].set(xlim=(0,1.5), ylim=(-.115,.008), xlabel=r"Scale $t$",
             ylabel=r"$M_t^B(x_1x_2e^{-|x|^2})$",
             title="A nonzero odd-coordinate moment")
axes[1].legend(loc="lower right", frameon=False, fontsize=10)
axes[1].grid(alpha=.2)
for extension in ["png", "svg"]:
    fig.savefig(out / ("mixed-gaussian-moments." + extension), dpi=170,
                metadata={"Date": None} if extension == "svg" else None)
svg = out / "mixed-gaussian-moments.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines()) + "\n",
               encoding="utf-8")
plt.close(fig)
