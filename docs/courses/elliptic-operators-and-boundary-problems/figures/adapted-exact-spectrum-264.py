"""Original U043 frequency lattice and exact counting bound, AE15--AE16.

CC0. This is a two-dimensional frequency section and a finite numerical
sample of a proved counting inequality. The torus period remains 2*pi;
the actual Fourier indices are integers and p=1+k**2+ell**4 throughout.
Run with Python, matplotlib, numpy and mpmath; writes PNG and SVG beside
this source. No external mathematical source is used by this diagram.
"""
from pathlib import Path
from math import isqrt
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
mp.mp.dps = 45
constant = 4 * mp.quad(lambda v: (1-v**2)**mp.mpf('0.25'), [0, 1])


def count_original(lam):
    """Exact integer enumeration independent of the quadrant formula."""
    if lam < 1:
        return 0
    s = lam-1
    return sum(1 for k in range(-isqrt(s), isqrt(s)+1)
               for ell in range(-isqrt(isqrt(s)), isqrt(isqrt(s))+1)
               if 1+k*k+ell**4 <= lam)


def formula_count(lam):
    if lam < 1:
        return 0
    s = lam-1
    k = isqrt(s)
    u = isqrt(isqrt(s))
    return 4*sum(isqrt(isqrt(s-j*j)) for j in range(1, k+1))+2*k+2*u+1


plt.rcParams.update({"font.size": 13, "axes.titlesize": 16,
                     "axes.labelsize": 14, "mathtext.fontset": "dejavusans",
                     "text.usetex": False,
                     "svg.hashsalt": "AN03-U043-adapted-exact-spectrum-264"})
fig, (left, right) = plt.subplots(1, 2, figsize=(15.2, 7.7))
fig.patch.set_facecolor("#fffdf8")
fig.suptitle("The full inverse retains every frequency and every lattice multiplicity",
             fontsize=20, y=.973)

lam = 17
for k in range(-5, 6):
    for ell in range(-3, 4):
        value = 1+k*k+ell**4
        if value <= lam:
            if k == ell == 0:
                color, marker, size = "#bd6320", "*", 200
            elif k == 0 or ell == 0:
                color, marker, size = "#356f9b", "s", 64
            else:
                color, marker, size = "#39835a", "o", 64
            left.scatter(k, ell, c=color, marker=marker, s=size, zorder=4)
        else:
            left.scatter(k, ell, c="#cccccc", s=20, zorder=1)
ys = np.linspace(-2, 2, 1601)
xs = np.sqrt(np.maximum(0, 16-ys**4))
left.plot(xs, ys, color="#444444", lw=1.7)
left.plot(-xs, ys, color="#444444", lw=1.7)
left.axhline(0, color="#aaaaaa", lw=.8)
left.axvline(0, color="#aaaaaa", lw=.8)
left.set(xlim=(-5.1, 5.1), ylim=(-3.15, 3.15), xlabel=r"$k\in\mathbb{Z}$",
         ylabel=r"$\ell\in\mathbb{Z}$", title=r"Actual frequencies: $1+k^2+\ell^4\leq17$")
left.set_aspect("equal")
left.set_xticks(range(-5, 6))
left.set_yticks(range(-3, 4))
left.grid(alpha=.19)
left.text(.02, .03, "12 quadrant points + 8 horizontal-axis points\n"
          "+ 4 vertical-axis points + 1 origin = 25", transform=left.transAxes,
          fontsize=11.8, va="bottom", bbox={"facecolor":"#fffdf8", "alpha":.95,
                                         "edgecolor":"#dddddd", "pad":5})

lams = np.arange(1, 258)
s = lams-1
counts = np.array([count_original(int(v)) for v in lams])
assert all(count_original(int(v)) == formula_count(int(v)) for v in lams)
lead = float(constant)*s.astype(float)**.75
bound = np.array([2*isqrt(int(v))+2*float(mp.mpf(int(v))**mp.mpf('.25'))+1
                  for v in s])
assert np.all(np.abs(counts-lead) <= bound+1e-11)
right.fill_between(lams, lead-bound, lead+bound, color="#cee3f0", alpha=.6,
                   label="AE16: error bound at sampled cutoffs")
right.plot(lams, lead+bound, color="#769db7", lw=1, ls=":")
right.plot(lams, lead-bound, color="#769db7", lw=1, ls=":")
right.plot(lams, lead, color="#a65b2f", lw=2,
           label=r"$C_{1,2}(\Lambda-1)^{3/4}$")
right.step(lams, counts, where="post", color="#245b81", lw=1.4,
           label=r"Exact $N_{1,2}(\Lambda)$, lattice enumeration")
right.set(xlim=(1, 257), xlabel=r"$\Lambda$ (the original eigenvalue cutoff)",
          ylabel="Number of eigenvalues, including multiplicity",
          title="The shift 1 and the complete floor error remain")
right.grid(alpha=.2)
right.legend(loc="upper left", fontsize=11, framealpha=.96)
right.text(.98, .03,
           r"$C_{1,2}=4\int_0^1(1-v^2)^{1/4}\,dv$"+"\n"+
           r"$E(\Lambda)=2\lfloor\sqrt{\Lambda-1}\rfloor$"+"\n"+
           r"$\qquad+2(\Lambda-1)^{1/4}+1$",
           ha="right", va="bottom", transform=right.transAxes, fontsize=12.5,
           bbox={"facecolor":"#fffdf8", "alpha":.96, "edgecolor":"#dddddd", "pad":5})
fig.text(.5, .055,
         "Continuous boundary on the left; integer Fourier points and exact counts. "
         "Right: a finite sample, not the proof.", ha="center", fontsize=12.1)
fig.text(.5, .025,
         "Proof: Nonelliptic Fredholm operators on their exact adapted spaces, "
         "editorial E3 and E5, AE11 and AE15-AE19. Original programme figure, CC0.",
         ha="center", fontsize=11.3)
fig.subplots_adjust(top=.865, bottom=.155, left=.061, right=.985, wspace=.21)
fig.savefig(OUT/'adapted-exact-spectrum-264.png', dpi=160, facecolor=fig.get_facecolor())
fig.savefig(OUT/'adapted-exact-spectrum-264.svg', facecolor=fig.get_facecolor(),
            metadata={"Date":None,"Creator":"Original AN03-U043 programme diagram, CC0"})
plt.close(fig)
print(json.dumps({"r":1,"m":2,"cutoff":17,"exact_count":count_original(17),
                  "counting_constant_integral":str(constant),
                  "sample_cutoffs":[1,257],"sample_size":257,
                  "all_exact_counts_match_quadrant_formula":True,
                  "all_sampled_counts_inside_proved_full_error":True}))
