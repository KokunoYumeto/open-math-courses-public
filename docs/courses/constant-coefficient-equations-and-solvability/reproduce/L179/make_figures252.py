"""CC0. Reproduce the exact sphere geometry and labeled Fourier model samples."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, os

ROOT = Path(__file__).resolve().parent
with TemporaryDirectory(prefix="an02-own252-mpl-") as temporary:
    os.environ["MPLCONFIGDIR"] = temporary
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    import numpy as np
    import mpmath as mp
    mp.mp.dps = 70
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "svg.hashsalt": "radial-boundary-252",
        "axes.spines.top": False, "axes.spines.right": False
    })
    out = ROOT/"figures"
    out.mkdir(exist_ok=True)
    def save(fig, name):
        fig.savefig(out/(name+".png"), dpi=160, bbox_inches="tight",
                    pad_inches=.15, metadata={"Software": "Open Mathematics Courses"})
        fig.savefig(out/(name+".svg"), bbox_inches="tight", pad_inches=.15,
                    metadata={"Date": None, "Creator": "Open Mathematics Courses"})
        plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(13.8, 5.4), layout="constrained")
    center = np.array([1., -.5])
    theta = np.array([.6, .8])
    radius = 1.5
    point = center+radius*theta
    for ax, sign, title in zip(axes, [1, -1],
        ["Kernel: singular circle a + (3/2) S¹",
         "Compact parametrix: reflected circle −a + (3/2) S¹"]):
        c = sign*center
        p = sign*point
        direction = sign*theta
        ax.add_patch(Circle(c, radius, fill=False, lw=2.2, edgecolor="#205a98"))
        ax.plot([c[0], p[0]], [c[1], p[1]], "--", color="#79848a", lw=1.5)
        ax.scatter([c[0]], [c[1]], color="#79848a", s=35)
        ax.scatter([p[0]], [p[1]], color="#b44c2e", s=45, zorder=5)
        ax.annotate("", xy=p+.55*direction, xytext=p,
                    arrowprops={"arrowstyle": "->", "color": "#b44c2e", "lw": 1.7})
        ax.annotate("a = (1, −1/2)" if sign==1 else "−a = (−1, 1/2)",
                    xy=c, xytext=(c[0], c[1]-.5*sign), ha="center", fontsize=10)
        ax.annotate("p = (19/10, 7/10)" if sign==1 else "−p = (−19/10, −7/10)",
                    xy=p, xytext=(1.3*sign, 1.65*sign),
                    ha="center", fontsize=10)
        ax.text(*(c+.45*radius*direction+np.array([-.25,.1])),
                "radius 3/2", fontsize=10, rotation=53 if sign==1 else 53)
        ax.text(*(p+.82*direction+sign*np.array([.02,.12])),
                "θ" if sign==1 else "−θ", color="#b44c2e", fontsize=12)
        ax.axhline(0, lw=.65, color="#a1a7ad")
        ax.axvline(0, lw=.65, color="#a1a7ad")
        ax.set(xlim=(-3.2,3.2), ylim=(-2.7,2.7),
               xlabel="x₁", ylabel="x₂", title=title)
        ax.set_aspect("equal")
        ax.grid(alpha=.15)
    save(fig, "translated-sphere-and-reflected-parametrix")

    def g2(r):
        return 1j*mp.pi**2*mp.hankel2(0, r)
    C2 = 1j*mp.pi*mp.sqrt(2*mp.pi)*mp.exp(1j*mp.pi/4)
    real_samples = []
    for r_float in np.geomspace(1., 64., 65):
        r = mp.mpf(str(r_float))
        W2 = mp.exp(1j*r)*mp.sqrt(r)*g2(r)/C2
        scaled = 8*r*abs(W2-1)
        assert scaled <= 1+mp.mpf("1e-50")
        real_samples.append(dict(r=str(r), dimension2_scaled_error=str(scaled),
                                 dimension5_scaled_error="1",
                                 dimension3_relative_error="0"))
    profile_samples = []
    for R in [16, 256, 65536]:
        for tau_float in np.linspace(-2, 2, 81):
            tau = mp.mpf(str(tau_float))
            r = R+1j*tau*mp.log(R)
            value = mp.log(abs(g2(r)))/mp.log(R)
            profile_samples.append(dict(R=R, tau=str(tau), model_log_profile=str(value),
                                        proved_limit=str(tau-mp.mpf(".5"))))
    fig, axes = plt.subplots(1, 2, figsize=(13.8, 5.3), layout="constrained")
    xs = [float(x["r"]) for x in real_samples]
    ys = [float(x["dimension2_scaled_error"]) for x in real_samples]
    axes[0].plot(xs, ys, color="#205a98", lw=2,
                 label="n = 2: sampled 8r |W₂ − 1|")
    axes[0].axhline(1, color="#9d632c", ls="--", lw=1.6,
                   label="proved bound 1; n = 5: r |W₅ − 1| = 1")
    axes[0].set(xscale="log", xlabel="Positive real frequency r",
                ylabel="Scaled relative error", ylim=(.69,1.035),
                title="Gaussian bound and exact odd-dimensional error")
    axes[0].text(1.25,.72,"n = 3: W₃ − 1 = 0 exactly",fontsize=10)
    axes[0].legend(loc="lower right", fontsize=9)
    axes[0].grid(alpha=.18)
    for R, color in zip([16, 256, 65536], ["#a16836","#547b46","#205a98"]):
        items = [x for x in profile_samples if x["R"]==R]
        axes[1].plot([float(x["tau"]) for x in items],
                     [float(x["model_log_profile"]) for x in items],
                     color=color, label=f"global model samples, R = {R}")
    taus = np.linspace(-2,2,81)
    axes[1].plot(taus,taus-.5,"--",color="#46354e",lw=1.7,
                 label="proved compact limit: τ − 1/2")
    axes[1].set(xlabel="τ, with r = R + iτ log R",
                ylabel="log |G₂(r)| / log R",
                title="Direction θ = e₁: logarithmic profiles")
    axes[1].legend(loc="upper left", fontsize=9)
    axes[1].grid(alpha=.18)
    save(fig,"radial-phase-errors-and-logarithmic-profiles")
    geometry = dict(
        schema="AN02-radial-geometry252/v1",
        exact_sphere_geometry=dict(
            dimension=2, center=["1","-1/2"], radius="3/2",
            unit_direction=["3/5","4/5"], singular_point=["19/10","7/10"],
            reflected_center=["-1","1/2"], reflected_point=["-19/10","-7/10"],
            singular_sets_are_circles_not_filled_disks=True,
            higher_dimension_picture_is_section=True,
            proof="Proposition 10.1; exact reflection in equation (10.2)"),
        relative_error_definition="W_n=exp(ir)*r^((n-1)/2)*G_n/C_n",
        proved_bounds=dict(dimension2="8r*abs(W_2-1)<=1 for real r>0",
                           dimension3="W_3-1=0", dimension5="W_5-1=-i/r"),
        real_samples=real_samples,
        profile_samples=profile_samples,
        profiles_are_global_model_samples_not_cutoff_transform_samples=True,
        compact_limit_proof="Theorem 8.1 and Proposition 9.1",
        numerical_precision_decimal_digits=70
    )
    (out/"geometry252.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(figures=2,real_samples=len(real_samples),
                         profile_samples=len(profile_samples),
                         owned_MPL_temporary_directory_removed_on_exit=True)))
