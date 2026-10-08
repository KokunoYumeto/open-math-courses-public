"""Reproduce two mathematical figures; remove the private font cache on exit."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, os

ROOT = Path(__file__).resolve().parent

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import mpmath as mp
    mp.mp.dps = 65
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":12,
                         "axes.titlesize":15, "axes.labelsize":13,
                         "svg.hashsalt":"AN02-own-finite-order240",
                         "savefig.facecolor":"white"})
    colors = ["#235baf", "#ad4b19", "#197759", "#8436a0"]
    y = np.linspace(.003, 1, 650)
    fig, ax = plt.subplots(figsize=(10.8, 6.4), constrained_layout=True)
    samples = []
    for index, power in enumerate([2,4,6]):
        ell = mp.log(mp.pi * 10 ** power)
        values = np.array([float(mp.log(2*mp.sinh(ell*mp.mpf(str(t))))/ell) for t in y])
        ax.plot(y, values, color=colors[index], lw=2.1,
                label=rf"$c=\pi\,10^{power}$")
        ax.plot(-y[::-1], values[::-1], color=colors[index], lw=2.1)
        for t in [mp.mpf("0.01"),mp.mpf("0.1"),mp.mpf("0.5"),mp.mpf("1")]:
            samples.append(dict(center_exact=f"pi*10^{power}", y_exact=str(t),
                                value_65_digits=mp.nstr(mp.log(2*mp.sinh(ell*t))/ell,65)))
    ax.plot(np.r_[-y[::-1],0,y], np.r_[y[::-1],0,y], color="#20272c",
            ls="--", lw=2.3, label=r"Canonical limit $|y|$")
    ax.axhline(0,color="#a4adb3",lw=.8)
    ax.axvline(0,color="#bac2c8",lw=.9,ls=":")
    ax.set(xlim=(-1.04,1.04),ylim=(-.75,1.07),
           xlabel=r"Imaginary parameter $y$ in $z=iy$",
           ylabel=r"$\log(2\sinh(|y|\log c))/\log c$",
           title="Real zeros and the limiting logarithmic profile")
    ax.text(.08,-.65,r"At $y=0$: each finite-center logarithm is $-\infty$",
            fontsize=10.5, bbox=dict(facecolor="white",edgecolor="#cbd2d6",pad=6))
    ax.legend(loc="lower left",framealpha=.96,fontsize=11)
    ax.grid(alpha=.19)
    for ext in ["png","svg"]:
        metadata={"Creator":"GPT-6.1 Sol; original mathematics and rendering"}
        if ext=="svg": metadata["Date"]=None
        fig.savefig(out/f"real-zeros-and-logarithmic-profiles.{ext}",dpi=180,
                    metadata=metadata)
    plt.close(fig)

    x = np.linspace(-6,6,1201)
    weights = [np.ones_like(x)]
    for j in range(1,6):
        b = np.ones_like(x) if j==1 else np.minimum(1,np.maximum(0,np.abs(x)-j+1))
        weights.append((1+2.0**(-j))*weights[-1]+2.0**j*b)
    fig, axes = plt.subplots(1,2,figsize=(12,5.5),constrained_layout=True,
                             gridspec_kw={"width_ratios":[1.5,1]})
    for index, stage in enumerate([1,2,4,6]):
        axes[0].plot(x,weights[stage-1],lw=2,color=colors[index],label=rf"$a_{stage}$")
    axes[0].set(xlabel=r"Position $t$",ylabel=r"Finite-stage weight $a_j(t)$",
                xlim=(-6,6),title="Additive changes leave each fixed compact")
    axes[0].legend(loc="upper center",ncol=2,fontsize=11)
    axes[0].grid(alpha=.2)
    stages=np.arange(1,7)
    axes[1].bar(stages,np.full(6,5),color="#235baf",width=.65)
    axes[1].set(xticks=stages,xlabel="Weight stage",ylabel="Derivative order",
                ylim=(0,6.8),title="One derivative order throughout")
    axes[1].text(3.5,5.8,r"$R_0=k+r+1=5$",ha="center",fontsize=14)
    axes[1].grid(axis="y",alpha=.2)
    for ext in ["png","svg"]:
        metadata={"Creator":"GPT-6.1 Sol; original mathematics and rendering"}
        if ext=="svg": metadata["Date"]=None
        fig.savefig(out/f"growing-weights-and-a-fixed-derivative-order.{ext}",dpi=180,
                    metadata=metadata)
    plt.close(fig)
    geometry = dict(schema="AN02-finite-order-figures240/v1",
                    profile=dict(centers_exact=["pi*10^2","pi*10^4","pi*10^6"],
                        formula="log(2*sinh(abs(y)*log(c)))/log(c)",
                        finite_center_value_at_y0="-infinity; omitted, not plotted as a finite height",
                        canonical_limit="abs(y)", plotted_abs_y_min=.003, plotted_abs_y_max=1,
                        samples=samples, numeric_precision_decimal_digits=65),
                    weights=dict(initial="a1(t)=1", e_j="2^(-j)", N_j="2^j",
                        b1="1", b_j="min(1,max(0,abs(t)-j+1)) for j>=2",
                        recurrence="a_(j+1)=(1+2^(-j))*a_j+2^j*b_j",
                        plotted_stages=[1,2,4,6], domain=[-6,6],
                        fixed_order=dict(n=1,M=0,A=0,k=2,r=2,R0=5),
                        model_weights_not_asserted_to_solve_unspecified_forcing=True,
                        exact_samples_at_t_5_over_2={"a2":"7/2","a3":"67/8","a4":"859/64"}))
    (out/"geometry240.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(figures=2,public_png_svg_pairs=2,
                          temporary_font_cache_removed_on_exit=True)))

if __name__=="__main__":
    with TemporaryDirectory(prefix="an02-own240-mpl-") as cache:
        os.environ["MPLCONFIGDIR"]=cache
        main()
