"""Original AN-05 L054 Figure 1. CC0; GPT-6.1 Sol, Ultra, October 2026.

Exact formulas: Sections 4 and 6, (4.4)-(4.6), (6.2)-(6.3).
Historical context: Hormander IV, Definition 28.1.7, pp. 230-231.
Numerical samples illustrate proved root geometry and the null-profile mechanism.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.titlesize": 15, "axes.labelsize": 13,
    "svg.hashsalt": "AN05-admissibility044",
})
fig, axes = plt.subplots(1, 3, figsize=(15, 7), dpi=160)
fig.subplots_adjust(left=.055, right=.98, bottom=.28, top=.77, wspace=.30)
fig.suptitle("A double root needs derivative control; a weight needs a quantitative bound",
             fontsize=19, y=.95)
fig.text(.5, .875,
         "Exact root paths at transverse frequency 1; exact weighted null profiles near time 1/4",
         ha="center", fontsize=13)

t = np.linspace(-.25, .25, 401)
good1 = 1j+t
good2 = 1j-t
bad_shift = np.sqrt(t.astype(complex))
bad1 = 1j+bad_shift
bad2 = 1j-bad_shift

for ax in axes[:2]:
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-.6, .6); ax.set_ylim(.4, 1.6)
    ax.axvline(0, color="#ced4da", linewidth=1)
    ax.axhline(1, color="#ced4da", linewidth=1)
    ax.set_xlabel(r"Real part of $\sigma$")
    ax.set_ylabel(r"Imaginary part of $\sigma$")
    ax.grid(alpha=.2)

axes[0].plot(good1.real, good1.imag, color="#007f73", linewidth=5, label=r"$i+t$")
axes[0].plot(good2.real, good2.imag, color="#df8f00", linewidth=2.5, linestyle="--", label=r"$i-t$")
axes[0].scatter([0], [1], color="#212529", s=35, zorder=5)
axes[0].set_title(r"Allowed: $(\sigma-i)^2-t^2$")
axes[0].legend(loc="upper right", frameon=True)
axes[0].text(.5, -.24, r"$|dq|\leq C\sqrt{|q|}$"+"\n"+
             "Smooth roots cross at the double zero.", transform=axes[0].transAxes,
             ha="center", va="top", fontsize=12)

axes[1].plot(bad1.real, bad1.imag, color="#007f73", linewidth=3, label=r"$i+\sqrt{t}$")
axes[1].plot(bad2.real, bad2.imag, color="#df8f00", linewidth=3, linestyle="--", label=r"$i-\sqrt{t}$")
axes[1].scatter([0], [1], color="#b83346", s=45, zorder=5)
axes[1].set_title(r"Excluded: $(\sigma-i)^2-t$")
axes[1].legend(loc="upper right", frameon=True)
axes[1].text(.5, -.24, r"$H_\sigma=0,\ H_t=-1$ at $t=0$"+"\n"+
             "The full derivative condition fails.", transform=axes[1].transAxes,
             ha="center", va="top", fontsize=12)

t0=.25
times=np.linspace(.17,.33,700)
phase=lambda z:z+z*z/2-20*z*z*z/3
for tau,color in [(20,"#8092c7"),(80,"#576eac"),(320,"#263e80")]:
    profile=np.exp(tau*(phase(times)-phase(t0)))
    axes[2].plot(times,profile,color=color,linewidth=2.5,label=r"$\tau=$"+str(tau))
axes[2].axvline(t0,color="#b83346",linewidth=1.5,linestyle=":")
axes[2].set_title("A localized weighted null profile")
axes[2].set_xlabel(r"Time $t$");axes[2].set_ylabel(r"$e^{\tau(F(t)-F(1/4))}$")
axes[2].set_xlim(.17,.33);axes[2].set_ylim(0,1.08);axes[2].grid(alpha=.2)
axes[2].legend(loc="lower left",frameon=True)
axes[2].text(.5,-.24,r"$F(t)=t+t^2/2-20t^3/3$"+"\n"+
             r"$F'(1/4)=0,\ F''(1/4)=-9$",
             transform=axes[2].transAxes,ha="center",va="top",fontsize=12)
fig.text(.5,.025,
         "Proof locators: L054 Section 4 and Exercise 3; Section 6 and Exercise 6. "
         "Original numerical illustrations; CC0.",
         ha="center",fontsize=11,color="#333333")
target=Path(__file__).with_name("admissible-clusters-and-weight-loss.png")
fig.savefig(target,dpi=160,metadata={"Software":"AN-05 original figure; CC0"})
plt.close(fig)
