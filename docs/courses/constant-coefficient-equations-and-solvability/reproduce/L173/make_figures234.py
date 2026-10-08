"""Draw exact carrier-domain geometry and regular convex tangent planes."""
from pathlib import Path
from tempfile import TemporaryDirectory
import os, json

OWN = Path(__file__).resolve().parent

def draw():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    import numpy as np

    out=OWN/"figures"; out.mkdir(exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
        "axes.titlesize":14,"axes.labelsize":14,"xtick.labelsize":12,
        "ytick.labelsize":12,"legend.fontsize":11,"svg.fonttype":"none",
        "svg.hashsalt":"singular-profile-domain-geometry",
        "axes.spines.top":False,"axes.spines.right":False})
    blue, orange, red, green="#165d9c","#ae5523","#a12535","#26734d"
    def save(fig,name):
        fig.savefig(out/(name+".png"),dpi=180,
                    metadata={"Creator":"Open Mathematics Courses"})
        fig.savefig(out/(name+".svg"),
                    metadata={"Creator":"Open Mathematics Courses","Date":None})
        plt.close(fig)

    fig,axes=plt.subplots(2,1,figsize=(6.6,9.5),layout="constrained",
                          gridspec_kw={"height_ratios":[1,1.7]})
    a=axes[0]
    a.plot([0,0],[0,3],color=blue,linewidth=6,solid_capstyle="round")
    a.scatter([0],[0],s=100,color=red,zorder=4)
    a.annotate(r"Known carrier $K_0=\{(0,0)\}$",(0,0),(.18,.45),
        fontsize=13,color=red,arrowprops={"arrowstyle":"-","color":red})
    a.text(.18,2.2,r"Hull $S=\{0\}\times[0,3]$",fontsize=13,color=blue)
    a.text(.18,1.45,"Every carrier is inside S.\nTheir family is not a singleton.",
        fontsize=12)
    a.set(xlim=(-.3,1.55),ylim=(-.25,3.45),xticks=[0],yticks=[0,1,2,3],
        xlabel="First coordinate",ylabel="Second coordinate",
        title="A nontrivial hull and an actual point carrier")

    a=axes[1]
    a.add_patch(Rectangle((-2,-4),4,5,facecolor="#dceaf4",
        edgecolor=blue,linestyle="--",linewidth=2))
    a.add_patch(Rectangle((-2,-1),4,2,facecolor="#f5e3d5",
        edgecolor=orange,linestyle="--",linewidth=2))
    a.plot([0,0],[-1,0],color="#303030",linewidth=3,zorder=3)
    js=np.arange(1,6); points=-1-np.zeros(5)+np.power(2.,-js)
    a.scatter(np.zeros(5),points,color=green,s=32,zorder=5)
    a.scatter([0],[-1],facecolors="white",edgecolors=red,
        linewidths=1.8,s=75,zorder=6)
    a.scatter([0],[-2],color=red,marker="x",s=80,linewidths=2,zorder=6)
    a.annotate("Allowed by K₀,\noutside X₂",(0,-2),(.6,-2.45),
        fontsize=12,color=red,arrowprops={"arrowstyle":"-","color":red})
    a.annotate("Witnesses approach\nexcluded boundary",(0,-1),(-.8,-1.55),
        ha="center",fontsize=11,color=green,
        arrowprops={"arrowstyle":"->","color":green})
    a.annotate("Compact image\nbound C",(0,-.1),(-1.8,.2),
        fontsize=11,arrowprops={"arrowstyle":"-","color":"#303030"})
    a.text(.8,.45,r"$X_2=E_S(X_1)$",ha="center",fontsize=13,color=orange)
    a.text(0,-3.35,r"$X_1=E_{K_0}(X_1)$",ha="center",fontsize=14,color=blue)
    a.text(0,-4.45,"Dashed rectangle edges are excluded.",
        ha="center",fontsize=11)
    a.set(xlim=(-2.6,2.6),ylim=(-4.65,1.4),xticks=[-2,0,2],
        yticks=[-4,-2,-1,0,1],xlabel="First coordinate",
        ylabel="Second coordinate",
        title="Each carrier gives its own translation domain")
    a.set_aspect("equal",adjustable="box")
    save(fig,"profile-family-and-an-escaping-boundary")

    fig,axes=plt.subplots(2,1,figsize=(6.6,10.2),layout="constrained",
                          gridspec_kw={"height_ratios":[1.7,1]})
    a=axes[0]; t=np.linspace(-1.3,1.3,801); f=np.abs(t)+t*t
    a.fill_between(t,f,3.5,color="#dceaf4",alpha=.95)
    a.plot(t,f,color="#222222",linewidth=2.6,label=r"Boundary $s=|t|+t^2$")
    params=[-1.,-.5,.5,1.]
    colors=[orange,blue,blue,orange]
    for p,c in zip(params,colors):
        slope=np.sign(p)+2*p
        a.plot(t,slope*t-p*p,color=c,linestyle="--",linewidth=1.3)
        a.scatter([p],[abs(p)+p*p],color=c,s=35,zorder=4)
    for p in [-.5,.5]:
        slope=np.sign(p)+2*p; norm=np.sqrt(1+slope*slope)
        a.annotate("",(p+.45*slope/norm,abs(p)+p*p-.45/norm),
            (p,abs(p)+p*p),arrowprops={"arrowstyle":"->","color":blue,
                                     "linewidth":1.8})
    a.scatter([0],[0],facecolors="white",edgecolors=red,
              linewidths=2,s=85,zorder=6)
    a.annotate("Excluded corner\n(0, 0)",(0,0),(.53,.15),fontsize=12,
        color=red,arrowprops={"arrowstyle":"-","color":red})
    a.text(0,2.65,r"Open domain $s>|t|+t^2$",ha="center",fontsize=12)
    a.text(.02,.02,"Arrows show outward\nnormal directions.",
        transform=a.transAxes,fontsize=10,
        bbox={"facecolor":"white","alpha":.9,"edgecolor":"none"})
    a.set(xlim=(-1.5,1.5),ylim=(-1.05,3.2),xticks=[-1,-.5,0,.5,1],
        yticks=[-1,0,1,2,3],xlabel="Horizontal coordinate t",
        ylabel="Vertical coordinate s",
        title="Regular tangents at a = −1, −½, ½, 1")
    a.set_aspect("equal",adjustable="box")
    a.legend(loc="upper left",frameon=False,fontsize=10)
    a=axes[1]
    for values in [np.linspace(-1.15,-.001,400),
                   np.linspace(.001,1.15,400)]:
        a.plot(values,values**2,color=blue,linewidth=2)
    for p,c in zip(params,colors):
        a.scatter([p],[p*p],color=c,s=55,zorder=4)
    a.scatter([0],[0],facecolors="white",edgecolors=red,
              linewidths=2,s=85,zorder=6)
    a.text(0,1.2,r"At the corner, every regular tangent has gap $a^2>0$.",
        ha="center",fontsize=11)
    a.set(xlim=(-1.2,1.2),ylim=(-.08,1.4),xticks=[-1,-.5,0,.5,1],
        yticks=[0,.25,1],xlabel="Regular tangency coordinate a ≠ 0",
        ylabel="Corner height − tangent height",
        title="All strict inequalities still include the corner")
    save(fig,"regular-tangents-and-the-missing-interior")
    geometry={
        "first_figure":{
            "kernel":"delta_(0,0)+(1/5) delta_0 tensor g; g positive on(2,3)",
            "hull_segment":[[0,0],[0,3]],"known_point_carrier":[0,0],
            "hull_itself_not_claimed_to_be_an_actual_carrier":True,
            "X1_open_rectangle":[[-2,2],[-4,1]],
            "X2_open_rectangle":[[-2,2],[-1,1]],
            "point_carrier_translation_domain":"X1",
            "hull_translation_domain":"X2",
            "compact_image_bound":[[0,-1],[0,0]],
            "outside_equation_point":[0,-2],
            "sampled_witnesses":[{"j":j,"point":[0,-1+2**(-j)]}
                                  for j in range(1,6)],
            "excluded_equation_boundary":[0,-1],
            "lower_outward_normal":[0,-1],
            "reflected_normal":[0,1],
            "reflected_support_values":{"point_carrier":0,"hull":3},
            "proof_locators":["formal Theorem4.1","formal Theorem6.1",
                              "learner Example2","learner Exercise5"]},
        "second_figure":{
            "boundary_formula":"s=abs(t)+t^2",
            "open_domain_formula":"s>abs(t)+t^2",
            "regular_tangent_parameters":params,
            "tangent_formula":"s=(sign(a)+2a)t-a^2; a!=0",
            "corner":[0,0],"corner_excluded":True,
            "corner_tangent_gap_formula":"a^2>0",
            "normal_formula":"(sign(a)+2a,-1)/sqrt(1+(sign(a)+2a)^2)",
            "normal_arrow_parameters":[-.5,.5],"normal_arrow_length":.45,
            "normal_plane_axes_have_equal_Euclidean_scale":True,
            "all_regular_tangents_strict_at_corner":True,
            "closed_halfspace_intersection":"s>=abs(t)+t^2",
            "interior_required_to_recover_open_domain":True,
            "proof_locators":["formal Lemma3.1","formal Lemma3.2",
                              "formal Theorem7.1","learner Example4",
                              "learner Exercise7"]}}
    (out/"geometry234.json").write_text(
        json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"figures":2,"PNG_SVG_pairs":2,
                      "temporary_font_cache_removed_on_exit":True}))

if __name__=="__main__":
    with TemporaryDirectory(prefix="an02-own234-mpl-") as cache:
        os.environ["MPLCONFIGDIR"]=cache
        draw()
