from io import BytesIO
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def render():
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
        "svg.fonttype":"none","svg.hashsalt":"TC-20261007",
        "axes.spines.top":False,"axes.spines.right":False})
    fig,axes=plt.subplots(1,2,figsize=(12,5.6),dpi=160)
    fig.subplots_adjust(left=.075,right=.97,top=.76,bottom=.25,wspace=.29)
    ink="#193440";teal="#137e8a";purple="#8250b2"
    fig.suptitle("One reflected coordinate, two opposite scalings",x=.075,y=.97,
                 ha="left",fontsize=21,fontweight="bold",color=ink)
    fig.text(.075,.875,"The interval example plots real arguments divided by pi/3, before exponentiation.",
             color="#50636c",fontsize=12)
    q=np.linspace(-1.5,1.5,601)
    ax=axes[0]
    ax.plot(q,np.exp(q),color=teal,lw=2.5,label=r"$H=e^Q$")
    ax.plot(q,np.exp(-q),color=purple,lw=2.5,label=r"$h_{\tau_0}=e^{-Q}$")
    ax.set(xlim=(-1.5,1.5),ylim=(0,4.9),xlabel="reflected coordinate q",ylabel="positive multiplier value")
    ax.set_title("A  The density is fixed by its imaginary powers",loc="left",fontsize=12,pad=17,fontweight="bold")
    ax.legend(frameon=False,fontsize=12)
    ax.axvline(0,lw=.7,color="#c3cfd4",zorder=0)
    ax.grid(axis="y",lw=.5,color="#dce3e7")
    ax=axes[1]
    s=.25
    seg=[(-.75,-.25,0),(-.25,0,-1),(0,.75,0),(.75,1,1),(1,1.5,0)]
    for a,b,y in seg:ax.plot([a,b],[y,y],color=teal if y else ink,lw=2.5)
    for x,old,new in [(-.25,0,-1),(0,-1,0),(.75,0,1),(1,1,0)]:
        ax.plot(x,old,marker="o",ms=6,mfc="white",mec=teal if old else ink,mew=1.5)
        ax.plot(x,new,marker="o",ms=6,mfc=teal if new else ink,mec=teal if new else ink)
    ax.set(xlim=(-.75,1.5),ylim=(-1.48,1.48),xlabel="reflected coordinate q",
           ylabel=r"$\arg(c_{1/4})/(\pi/3)$")
    ax.set_xticks([-.25,0,.75,1],[r"$-1/4$","0",r"$3/4$","1"])
    ax.set_yticks([-1,0,1],[r"$-1\quad(\bar\zeta)$",r"$0\quad(1)$",r"$1\quad(\zeta)$"])
    ax.set_title("B  A discontinuous transfer on [0, 1)",loc="left",fontsize=12,pad=17,fontweight="bold")
    ax.grid(axis="y",lw=.5,color="#dce3e7")
    fig.text(.075,.135,r"$\lambda(t)=e^{-itQ};\quad \theta_s(h_{\tau_0})=e^{-s}h_{\tau_0},\quad \theta_s(H)=e^sH$",
             fontsize=13,color=ink)
    fig.text(.565,.135,r"$b(q)=\zeta^{1_{[0,1)}(q)},\quad c_s(q)=b(q)\overline{b(q+s)}$",
             fontsize=13,color=ink)
    fig.text(.075,.045,"Exact formulas: TC6, TC8, TC34–TC36. Original vector figure and renderer: CC0-1.0.",
             fontsize=10,color="#50636c")
    # Bounded sample checks test the implementation; the text proves all-time assertions.
    samples=np.array([-.5,-.25,-.1,0,.5,.75,.9,1,1.25])
    zeta=np.exp(1j*np.pi/3)
    b=lambda x:np.where((x>=0)&(x<1),zeta,1+0j)
    phase=np.where((samples>=-.25)&(samples<0),-1,
                  np.where((samples>=.75)&(samples<1),1,0))
    error=float(np.max(np.abs(b(samples)*np.conj(b(samples+s))-np.exp(1j*np.pi*phase/3))))
    assert error<1e-14
    assert abs(math.exp(1)*math.exp(-1)-1)<1e-14
    svg=BytesIO();png=BytesIO()
    fig.savefig(svg,format="svg",metadata={"Date":None,"Creator":"Original translation-cocycle figure"})
    fig.savefig(png,format="png",metadata={"Software":"Original translation-cocycle figure"})
    plt.close(fig)
    return svg.getvalue(),png.getvalue(),{"interval_phase_max_error":error,"s":"1/4",
        "negative_phase_interval":"[-1/4,0)","positive_phase_interval":"[3/4,1)",
        "matplotlib":matplotlib.__version__,"numpy":np.__version__,"png_pixels":[1920,896]}


if __name__ == '__main__':
    from pathlib import Path
    import json
    directory = Path(__file__).resolve().parent
    svg, png, checks = render()
    (directory / 'tcc-models.svg').write_bytes(svg)
    (directory / 'tcc-models.png').write_bytes(png)
    print(json.dumps(checks))
