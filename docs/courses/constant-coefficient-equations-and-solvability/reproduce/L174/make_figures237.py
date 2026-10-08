"""Draw exact weight compensation and locally finite primitive diagrams."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os,json
OWN=Path(__file__).resolve().parent
def draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    out=OWN/"figures";out.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
        "axes.titlesize":14,"axes.labelsize":14,"xtick.labelsize":12,
        "ytick.labelsize":12,"legend.fontsize":12,"svg.fonttype":"none",
        "svg.hashsalt":"quotient-distribution-solvability",
        "axes.spines.top":False,"axes.spines.right":False})
    blue,orange,green,red="#165d9c","#ae5523","#26734d","#a12535"
    def save(fig,name):
        fig.savefig(out/(name+".png"),dpi=180,
                    metadata={"Creator":"Open Mathematics Courses"})
        fig.savefig(out/(name+".svg"),
                    metadata={"Creator":"Open Mathematics Courses","Date":None})
        plt.close(fig)
    j=np.arange(1,7)
    fig,axes=plt.subplots(2,1,figsize=(6.6,8.2),layout="constrained")
    a=axes[0]
    a.plot(j,j*j,"o-",color=orange,linewidth=1.6,
        label=r"$\log_2 w_j=j^2$")
    a.plot(j,-j*j-2*j-8,"s-",color=blue,linewidth=1.6,
        label=r"$\log_2\varepsilon_j=-j^2-2j-8$")
    a.axhline(0,color="#777777",linewidth=.8)
    a.set(xlim=(.7,6.3),xticks=j,ylim=(-62,43),
        yticks=[-56,-32,-12,0,16,36],xlabel="Index j",
        ylabel="Base-two logarithm",
        title="Growing masses and shrinking smoothing radii")
    a.legend(loc="upper left",frameon=False)
    a=axes[1]
    a.plot(j,-2*j-8,"o-",color=green,linewidth=1.7)
    a.text(3.5,-9.9,r"$w_j\varepsilon_j=2^{-2j-8}$",ha="center",
        fontsize=16,color=green)
    a.text(4.5,-13.3,r"$\sum_{j\geq1}w_j\varepsilon_j=\frac{1}{768}$",
        ha="center",fontsize=18,color=green)
    a.text(3.5,-21.2,"One derivative controls the entire global sum.",
        ha="center",fontsize=12)
    a.set(xlim=(.7,6.3),xticks=j,ylim=(-22,-9),yticks=[-10,-12,-16,-20],
        xlabel="Index j",ylabel=r"$\log_2(w_j\varepsilon_j)$",
        title="The compensated test errors are summable")
    save(fig,"large-masses-and-summable-smoothing-errors")
    fig,axes=plt.subplots(2,1,figsize=(6.6,8.2),layout="constrained")
    x=1-np.power(2.,-j)
    a=axes[0]
    a.plot(j,x,"o-",color=blue,linewidth=1.6)
    a.axhline(1,color=red,linestyle="--",linewidth=1.7)
    a.text(3.5,1.025,"Excluded boundary at x = 1",ha="center",
        color=red,fontsize=13)
    a.text(3.5,.63,r"$x_j=1-2^{-j}$",ha="center",color=blue,fontsize=18)
    a.set(xlim=(.7,6.3),xticks=j,ylim=(.43,1.07),
        yticks=[.5,.75,.875,1],xlabel="Index j",
        ylabel="Singular point coordinate",
        title="Both series have these isolated singular points")
    a=axes[1]
    a.plot(j,j,"o-",color=orange,linewidth=1.6,label="Datum order j")
    a.plot(j,j-1,"s-",color=blue,linewidth=1.6,label="Primitive order j − 1")
    a.text(4.5,1.1,r"$\partial_t u=f$",ha="center",fontsize=18)
    a.set(xlim=(.7,6.3),xticks=j,ylim=(-.3,6.7),
        yticks=range(7),xlabel="Index j",
        ylabel="Exact isolated-point derivative order",
        title="The solution lowers each order by one")
    a.legend(loc="upper left",frameon=False)
    save(fig,"increasing-orders-and-an-exact-primitive")
    geometry={"first_figure":{
        "domain":"(0,1)","point_formula":"x_j=1-2^(-j)",
        "mass_formula":"w_j=2^(j^2)",
        "radius_formula":"epsilon_j=2^(-j^2-2j-8)",
        "error_bound_formula":"w_j*epsilon_j=2^(-2j-8)",
        "infinite_sum_exact":"1/768",
        "sampled_indices":list(range(1,7)),
        "samples":[{"j":k,"log2_mass":k*k,
                    "log2_radius":-k*k-2*k-8,
                    "log2_error_bound":-2*k-8}for k in range(1,7)],
        "plots_are_not_Dirac_height_graphs":True,
        "proof_locators":["formal Lemma1.1","learner Example1",
                          "learner Exercise1"]},
        "second_figure":{
        "domain":"(0,1)","point_formula":"x_j=1-2^(-j)",
        "datum_formula":"sum partial^j delta_(x_j)",
        "primitive_formula":"sum partial^(j-1) delta_(x_j)",
        "equation":"partial_t u=f","excluded_endpoint":1,
        "samples":[{"j":k,"x_j":1-2**(-k),"datum_order":k,
                    "primitive_order":k-1}for k in range(1,7)],
        "orders_unbounded_in_both_complete_series":True,
        "proof_locators":["formal Theorem4.1","formal Theorem5.1",
                          "learner Example2","learner Exercises3–4"]}}
    (out/"geometry237.json").write_text(
        json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"figures":2,"PNG_SVG_pairs":2,
                     "temporary_font_cache_removed_on_exit":True}))
if __name__=="__main__":
    with TemporaryDirectory(prefix="an02-own237-mpl-") as cache:
        os.environ["MPLCONFIGDIR"]=cache
        draw()
