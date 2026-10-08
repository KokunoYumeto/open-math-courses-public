"""Reproduce exact mathematical diagrams using an automatically removed font cache."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, os
import numpy as np

def render():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import rcParams
    rcParams.update({"font.size":13, "axes.titlesize":16, "axes.labelsize":13,
                     "svg.hashsalt":"an02-hypoelliptic243", "font.family":"DejaVu Sans"})
    root=Path(__file__).resolve().parent
    out=root/"figures"
    out.mkdir(exist_ok=True)
    geometry={
        "fourier_convention":"F(z)=mu(exp(-i*x.z))",
        "finite_difference":{"kernel":{"points":[-.5,.5],"coefficients":[1,2]},
            "zeros":"z_j=(2*j+1)*pi-i*log(2), j integral",
            "displayed_indices":list(range(-3,4)),
            "displayed_real_center_window":"abs(eta)<=log(2+abs(xi))/3",
            "window_is_a_real_center_comparison_not_the_total_complex_norm_strip":True},
        "ratio_panel":{"indices":list(range(0,51)),
            "difference_ratio":"log(2)/log(sqrt(((2*q+1)*pi)^2+log(2)^2))",
            "elliptic_branch":"z=(t,i*sqrt(1+t^2)), t=q+1",
            "elliptic_symbol":"1+z1^2+z2^2",
            "elliptic_ratio":"sqrt(1+t^2)/log(sqrt(1+2*t^2))",
            "one_branch_not_an_all_zero_proof":True},
        "boundary_profiles":{"positive_center":"v(z)=Im(z)","negative_center":"v(z)=-Im(z)",
            "parametrix_profiles":"the negatives on the same centers",
            "kernel_and_parametrix_singular_sets":[-1,1],
            "convex_hull":[-1,1],"interior_is_smooth":True},
        "translated_example":{"a":.6,"kernel_singular_set":[.6],"inverse_singular_set":[-.6]},
        "proof_locators":["Formal Theorem2.1,Theorems3.4,4.1,5.1",
                          "Learner Examples1,2,4 and Exercise3"],
        "source_credit":"Original diagrams of the explicitly proved models; Hörmander convolution regularity theory is credited in both chapters."
    }
    (out/"geometry243.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
    fig,axes=plt.subplots(2,1,figsize=(8.6,8.1),layout="constrained")
    x=np.linspace(-23,23,700)
    band=np.log(2+abs(x))/3
    axes[0].fill_between(x,-band,band,color="#d7e8f6",alpha=.85)
    axes[0].plot(x,band,color="#5182a0",lw=1)
    axes[0].plot(x,-band,color="#5182a0",lw=1)
    indices=np.arange(-3,4)
    axes[0].scatter((2*indices+1)*np.pi,np.full(7,-np.log(2)),
                    marker="x",s=95,lw=2.4,color="#b53c32",label="Exact transform zeros")
    axes[0].axhline(0,color="#555",lw=.8)
    axes[0].set(xlim=(-23,23),ylim=(-1.8,1.8),xlabel="Real frequency ξ",
                ylabel="Imaginary frequency η",
                title="Fixed-height zeros remain in logarithmic windows")
    axes[0].legend(loc="upper right",fontsize=12)
    axes[0].text(-21,1.45,"Shaded window: |η| ≤ log(2+|ξ|)/3",fontsize=12)
    q=np.arange(0,51)
    difference=np.log(2)/np.log(np.sqrt(((2*q+1)*np.pi)**2+np.log(2)**2))
    t=q+1
    elliptic=np.sqrt(1+t*t)/np.log(np.sqrt(1+2*t*t))
    axes[1].plot(q,elliptic,color="#236a8d",lw=2.5,label="One exact elliptic zero branch: t=q+1")
    axes[1].plot(q,difference,color="#b53c32",lw=2.5,label="Difference-kernel zeros: j=q")
    axes[1].set(xlabel="Sample index q",ylabel="|Im ζ| / log|ζ|",
                title="Exact zero families have different retreat ratios",ylim=(0,None))
    axes[1].grid(alpha=.2)
    axes[1].legend(loc="upper left",fontsize=11.5)
    for suffix in ("png","svg"):
        fig.savefig(out/("zeros-and-logarithmic-retreat."+suffix),dpi=170,
                    metadata={"Date":None} if suffix=="svg" else {})
    plt.close(fig)
    fig,axes=plt.subplots(3,1,figsize=(8.6,10.1),layout="constrained")
    y=np.linspace(-2,2,300)
    axes[0].plot(y,y,color="#236a8d",lw=2.6,label="Positive real centers: v=η")
    axes[0].plot(y,-y,color="#b96b2b",lw=2.6,label="Negative real centers: v=−η")
    axes[0].axhline(0,color="#888",lw=.8);axes[0].axvline(0,color="#888",lw=.8)
    axes[0].set(xlabel="Parameter imaginary part η",ylabel="Exact limiting profile",
                title="Each frequency sign selects one singular point")
    axes[0].legend(fontsize=11.5)
    for row,label,color in ((1,"Compact kernel μ₀","#236a8d"),(0,"Compact parametrix ν₀","#b96b2b")):
        axes[1].scatter([-1,1],[row,row],s=115,color=color,zorder=4)
        axes[1].text(-1.65,row,label,ha="right",va="center",fontsize=13)
        axes[1].plot([-1,1],[row,row],color="#c9c9c9",lw=3,zorder=1)
    axes[1].text(0,.5,"Smooth between the two singular points",ha="center",fontsize=13)
    axes[1].set(xlim=(-3.25,1.8),ylim=(-.4,1.4),xlabel="Spatial coordinate x",
                title="The exact singular set is {−1,1}; the hull fills the interval")
    axes[1].set_yticks([]);axes[1].set_xticks([-1,0,1])
    axes[1].spines[["top","right","left"]].set_visible(False)
    axes[2].scatter([.6],[1],s=135,color="#236a8d",zorder=3)
    axes[2].scatter([-.6],[0],s=135,color="#b96b2b",zorder=3)
    axes[2].annotate("",xy=(-.6,.07),xytext=(.6,.93),
                     arrowprops={"arrowstyle":"->","lw":2,"color":"#505050"})
    axes[2].text(.68,1,"Kernel singularity a=3/5",va="center",fontsize=13)
    axes[2].text(-.68,0,"Inverse singularity −a=−3/5",ha="right",va="center",fontsize=13)
    axes[2].set(xlim=(-2.7,2.7),ylim=(-.4,1.4),xlabel="Spatial coordinate x",
                title="A translated elliptic kernel makes the reflection sign visible")
    axes[2].set_yticks([]);axes[2].set_xticks([-.6,0,.6],labels=["−3/5","0","3/5"])
    axes[2].spines[["top","right","left"]].set_visible(False)
    for suffix in ("png","svg"):
        fig.savefig(out/("affine-profiles-and-exact-reflected-singularities."+suffix),dpi=170,
                    metadata={"Date":None} if suffix=="svg" else {})
    plt.close(fig)
    print(json.dumps({"figures":2,"PNG_and_SVG":True,"exact_geometry":str(out/"geometry243.json"),
                      "private_font_cache_removed_on_exit":True}),flush=True)

if __name__=="__main__":
    with TemporaryDirectory(prefix="an02-own243-mpl-") as cache:
        os.environ["MPLCONFIGDIR"]=cache
        render()
