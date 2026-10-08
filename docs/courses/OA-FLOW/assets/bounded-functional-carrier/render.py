def render(data):
    """Return reproducible PNG and SVG bytes; no filesystem writes."""
    import io
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    with plt.rc_context({"font.family":"DejaVu Sans","font.size":14,
                         "mathtext.fontset":"dejavusans","svg.fonttype":"none",
                         "svg.hashsalt":"bounded-functional-carrier-v1"}):
        fig=plt.figure(figsize=(14,8.4),dpi=120,facecolor="#fbfbf8")
        fig.text(.05,.952,data["title"],fontsize=24,weight="bold",color="#162c38")
        fig.text(.05,.910,r"$M=B(\ell^2(\mathbb{N}))$   |   rank-one $p_1\perp p_2$   |   $\mu_{\omega_{t,p}}=t\,\delta_{z_t}$",
                 fontsize=16,color="#304d5e")
        colors=["#2878a8","#da8534","#398464"]
        rows=[(.50,.865),(.085,.45)]
        for j,(panel,(bottom,top)) in enumerate(zip(data["panels"],rows)):
            fig.text(.05,top,panel["name"],fontsize=18,weight="bold",color="#162c38")
            fig.text(.05,top-.045,panel["formula"],fontsize=18,color="#162c38")
            ax=fig.add_axes([.06,bottom+.075,.23,.185],facecolor="#fbfbf8")
            ax.set_xlim(-.18,2.35);ax.set_ylim(-.36,2.3)
            ax.set_aspect("equal");ax.axis("off")
            for r in range(2):
                for c in range(2):
                    val=panel["density"][r] if r==c else 0
                    fill=(colors[r] if j==0 else colors[2]) if val else "#e7edef"
                    rect=Rectangle((c,1-r),1,1,facecolor=fill,edgecolor="#567180",lw=1.4)
                    ax.add_patch(rect)
                    ax.text(c+.5,1-r+.5,str(val),ha="center",va="center",fontsize=23,
                            color="white" if val else "#5b6d74",weight="bold" if val else "normal")
            ax.text(.5,2.12,r"$p_1$",ha="center",fontsize=14)
            ax.text(1.5,2.12,r"$p_2$",ha="center",fontsize=14)
            ax.text(2.11,1.5,r"$p_1$",va="center",fontsize=14)
            ax.text(2.11,.5,r"$p_2$",va="center",fontsize=14)
            fig.text(.065,bottom+.035,"Density on two rank-one directions",fontsize=11,color="#304d5e")
            fig.text(.315,bottom+.195,panel["support"],fontsize=18,color="#304d5e",ha="center")
            fig.text(.315,bottom+.13,r"$\longmapsto$",fontsize=29,color="#304d5e",ha="center")
            bx=fig.add_axes([.455,bottom+.082,.475,.213],facecolor="#fbfbf8")
            bx.set_ylim(0,3.5);bx.set_xlim(.45,3.55)
            bx.set_yticks([0,1,2,3]);bx.set_xticks([1,2,3],[r"$z_1$",r"$z_2$",r"$z_3$"],fontsize=16)
            bx.set_ylabel(r"$\mu_\omega(z_t)$",labelpad=11,fontsize=15)
            bx.spines[["top","right"]].set_visible(False)
            bx.spines[["left","bottom"]].set_color("#81939c")
            bx.grid(axis="y",color="#dbe2e4",linewidth=.8,zorder=0)
            bx.tick_params(length=0,pad=5)
            for k,value in enumerate(panel["measure"]):
                bx.bar(k+1,value,width=.42,color=colors[k],zorder=3)
                if value==0:
                    bx.plot([k+.8,k+1.2],[0,0],color="#81939c",lw=3,zorder=4)
                bx.text(k+1,value+.10,str(value),ha="center",va="bottom",fontsize=16,
                        color=colors[k] if value else "#5b6d74",weight="bold")
            fig.text(.455,bottom+.020,panel["result"],fontsize=18,color="#162c38")
            fig.text(.932,bottom+.020,panel["proof"],fontsize=11,color="#304d5e",ha="right")
        fig.text(.05,.020,"Central atoms are categories, not positions in a metric space. All omitted density entries are zero.",
                 fontsize=10.5,color="#526a76")
        png=io.BytesIO();svg=io.BytesIO()
        fig.savefig(png,format="png",dpi=120,facecolor=fig.get_facecolor(),
                    metadata={"Software":"Matplotlib; original mathematical drawing"})
        fig.savefig(svg,format="svg",facecolor=fig.get_facecolor(),
                    metadata={"Date":None,"Creator":"Original mathematical drawing"})
        plt.close(fig)
        return png.getvalue(),svg.getvalue()

if __name__ == '__main__':
    from pathlib import Path
    import json
    directory=Path(__file__).resolve().parent
    png,svg=render(json.loads((directory/'data.json').read_text(encoding='utf-8')))
    (directory/'bfc-measures.png').write_bytes(png)
    (directory/'bfc-measures.svg').write_bytes(svg)
