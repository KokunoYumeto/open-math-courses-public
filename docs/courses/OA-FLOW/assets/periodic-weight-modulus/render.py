def render(data):
    import io, math
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyArrowPatch
    with plt.rc_context({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
                         "font.size":14,"svg.fonttype":"none",
                         "svg.hashsalt":"periodic-modulus-v1"}):
        fig=plt.figure(figsize=(14,8.3),dpi=120,facecolor="#fcfcf8")
        ink="#173341";blue="#2478a8";orange="#c46b26";gray="#687c86"
        fig.text(.04,.95,data["title"],fontsize=23,weight="bold",color=ink)
        fig.text(.04,.90,r"$L=-\log\lambda,\quad P=2\pi/L,\quad z=u(P),\quad \theta_s(z)=e^{-iPs}z$",
                 fontsize=19,color=ink)
        fig.text(.05,.81,"Fundamental-period phase",fontsize=18,weight="bold",color=ink)
        fig.text(.05,.763,r"$L=1,\ \mu=e^{-1/3}:\quad \operatorname{mod}(\alpha)(z)=e^{-2\pi i/3}z$",
                 fontsize=15,color=ink)
        ax=fig.add_axes([.045,.24,.435,.48])
        ax.set_xlim(-1.65,1.7);ax.set_ylim(-1.48,1.55)
        ax.set_aspect("equal");ax.axis("off")
        t=np.linspace(0,2*np.pi,361)
        ax.plot(np.cos(t),np.sin(t),color="#b7c7ce",lw=2)
        ax.axhline(0,color="#e1e7ea",lw=.9);ax.axvline(0,color="#e1e7ea",lw=.9)
        end=-2*math.pi/3
        a=np.linspace(0,end,100)
        ax.plot(1.18*np.cos(a),1.18*np.sin(a),color=blue,lw=2.5)
        ax.annotate("",xy=(1.18*math.cos(end),1.18*math.sin(end)),
                    xytext=(1.18*math.cos(end+.13),1.18*math.sin(end+.13)),
                    arrowprops={"arrowstyle":"-|>","color":blue,"lw":2.5})
        ax.scatter([1,math.cos(end)],[0,math.sin(end)],s=80,c=[ink,blue],zorder=4)
        ax.text(1.1,.12,r"$1=z(0)$",fontsize=15,color=ink)
        ax.text(-1.25,-1.31,r"$e^{-2\pi i/3}$",fontsize=18,color=blue)
        ax.text(-1.57,.68,r"$-\frac{2\pi}{3}$",fontsize=23,color=blue)
        ax.text(-.05,1.34,"Values of the coordinate at q = 0",ha="center",fontsize=11,color=gray)
        fig.text(.05,.188,"The negative dual convention gives a clockwise phase.",fontsize=12,color=gray)
        fig.text(.05,.148,"This panel is conditional on the stated scaling automorphism.",fontsize=10.8,color=gray)
        fig.text(.05,.109,"PDM16–PDM21; PDM36",fontsize=11,color=gray)
        fig.text(.54,.81,"A higher period loses a root",fontsize=18,weight="bold",color=ink)
        fig.text(.54,.763,r"$L=2P,\quad w=u(L)=z^2$",fontsize=17,color=ink)
        bx=fig.add_axes([.54,.20,.415,.49])
        bx.set_xlim(-1.65,1.65);bx.set_ylim(-2.15,2.1);bx.set_aspect("equal");bx.axis("off")
        for cy in [1.05,-1.1]:
            bx.plot(.70*np.cos(t),cy+.70*np.sin(t),color="#b7c7ce",lw=2)
        bx.scatter([.7,-.7],[1.05,1.05],s=85,c=[blue,orange],zorder=4)
        bx.text(.86,1.04,r"$z=1$",va="center",fontsize=15,color=blue)
        bx.text(-1.62,1.04,r"$z=-1$",va="center",fontsize=15,color=orange)
        bx.text(0,1.94,"Full center coordinate",ha="center",fontsize=12,color=gray)
        bx.scatter([.7],[-1.1],s=90,c=[ink],zorder=4)
        bx.text(.86,-1.1,r"$w=1$",va="center",fontsize=15,color=ink)
        bx.text(0,-2.00,"The tested power identifies both values",ha="center",fontsize=11,color=gray)
        bx.add_patch(FancyArrowPatch((.71,.98),(.73,-1.02),
                    connectionstyle="arc3,rad=-.40",arrowstyle="-|>",mutation_scale=15,
                    lw=1.8,color=blue))
        bx.add_patch(FancyArrowPatch((-.68,.98),(.62,-1.08),
                    connectionstyle="arc3,rad=.16",arrowstyle="-|>",mutation_scale=15,
                    lw=1.8,color=orange))
        bx.text(-.18,-.03,r"$w=z^2$",ha="center",fontsize=18,color=ink,
                bbox={"facecolor":"#fcfcf8","edgecolor":"none","pad":2})
        fig.text(.54,.147,r"Inner example: actual $z\mapsto z$; false inference $z\mapsto-z$.",
                 fontsize=12,color=ink)
        fig.text(.54,.107,"Both fix w.  PDM27–PDM35",fontsize=11,color=gray)
        fig.text(.04,.035,"Circle coordinates and phases are exact; no operator-norm or spectral-distance interpretation is intended.",
                 fontsize=10.5,color=gray)
        outp=io.BytesIO();outs=io.BytesIO()
        fig.savefig(outp,format="png",dpi=120,facecolor=fig.get_facecolor(),
                    metadata={"Software":"Matplotlib; original mathematical drawing"})
        fig.savefig(outs,format="svg",facecolor=fig.get_facecolor(),
                    metadata={"Date":None,"Creator":"Original mathematical drawing"})
        plt.close(fig)
        return outp.getvalue(),outs.getvalue()

if __name__ == "__main__":
    import json
    from pathlib import Path
    p=Path(__file__).resolve().parent
    png,svg=render(json.loads((p/"data.json").read_text()))
    (p/"pdm-phases.png").write_bytes(png)
    (p/"pdm-phases.svg").write_bytes(svg)
