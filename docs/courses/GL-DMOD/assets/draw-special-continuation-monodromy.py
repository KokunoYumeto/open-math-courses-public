"""Reproducible fibre meridians, anchor extension and function-envelope diagram."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":18,
                           "svg.hashsalt":"special-continuation-monodromy"})
blue,red,grey="#145da0","#a12b3a","#687587"
fig,axes=plt.subplots(3,1,figsize=(7.4,18.2),
                     gridspec_kw={"height_ratios":[1.1,1.1,1]})
fig.subplots_adjust(left=.16,right=.95,top=.935,bottom=.025,hspace=.64)

a=axes[0];a.set_aspect("equal")
a.add_patch(Circle((0,0),1,facecolor="#f2f6fa",edgecolor=grey,lw=1.5))
a.plot([-.5,-.25], [0,0], color=blue,lw=2)
a.scatter([-.5],[0],s=40,color=blue,zorder=4)
a.text(-.91,-.48,r"$A_r=-1/2$",color=blue,fontsize=17)
theta=np.linspace(np.pi,3*np.pi,401)
for sign in [-1,1]:
    h=sign/4
    a.plot([-.25,-.25,-1/8],[0,h,h],color=blue,lw=1.7)
    a.plot(np.cos(theta)/8,h+np.sin(theta)/8,color=blue,lw=2.2)
    a.annotate("",xy=(0,h-1/8),xytext=(-.05,h-.114),
               arrowprops={"arrowstyle":"->","color":blue,"lw":2})
    a.scatter([0],[h],s=32,color=red,zorder=5)
    a.plot([0,np.sqrt(1-h*h)],[h,h],"--",color=grey,lw=1.2)
    a.annotate(r"$+i/4$"if sign==1 else r"$-i/4$",
               xy=(0,h),xytext=(.22,sign*.49),
               arrowprops={"arrowstyle":"-","color":red},
               color=red,fontsize=17)
a.text(-.82,.75,r"$\zeta=16t,\quad x_*=-1/16$",fontsize=17)
a.text(-.82,-.81,"Two fibre meridians",fontsize=15.5)
a.set(xlim=(-1.04,1.04),ylim=(-1.04,1.04),xlabel=r"$\operatorname{Re}\zeta$",
      ylabel=r"$\operatorname{Im}\zeta$")
a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1])
a.set_title("A. A smaller disc contains every root\nMC.A: fibre generators map onto "+r"$\Gamma$",
            fontsize=18.5,pad=15)

a=axes[1];a.set_aspect("equal")
a.add_patch(Circle((0,0),.5,facecolor="#e7f0f9",edgecolor=blue,lw=2))
a.add_patch(Circle((0,0),.4,fill=False,edgecolor=grey,ls="--",lw=1.3))
a.scatter([0],[0],s=55,color=red,zorder=5)
a.annotate(r"$H=\{z=0\}$",xy=(0,0),xytext=(.11,-.19),
           arrowprops={"arrowstyle":"-","color":red},color=red,fontsize=17)
a.annotate("",xy=(.5,0),xytext=(.495,-.075),
           arrowprops={"arrowstyle":"->","color":blue,"lw":2.3})
a.text(-.45,.60,r"$|\zeta|=1/2$",fontsize=18,color=blue)
a.text(-.51,-.64,r"$g(A',z)=h(A',z)$",fontsize=19)
a.text(-.51,-.76,"Time identity extends the formula",fontsize=15)
a.set(xlim=(-.63,.63),ylim=(-.82,.7),xlabel=r"$\operatorname{Re}z$",
      ylabel=r"$\operatorname{Im}z$")
a.set_xticks([-.5,0,.5]);a.set_yticks([-.5,0,.5])
a.set_title("B. The anchor removes the cylinder error\nMC.D–MC.E: full time disc, smaller base",
            fontsize=18.5,pad=17)

a=axes[2];a.axis("off")
a.set_title("C. Actual solution monodromy\nand finite function determination",fontsize=18.5,pad=13)
lines=[
 r"$\rho:\Gamma\longrightarrow\mathrm{GL}(V)$",
 r"$\Downarrow$",
 r"$\mathfrak{c}=\ker(\mathbf{C}[\Gamma]\longrightarrow\mathrm{End}(V))$",
 r"$\Downarrow\quad\mathfrak{a}=I\mathfrak{c}$",
 r"$(\gamma-1)c f_{ai}=0$",
 r"$\Downarrow$",
 r"$\dim\mathbf{C}[\Gamma]/\mathfrak{a}\leq 1+dq^2$"]
for y,t in zip(np.linspace(.94,.03,len(lines)),lines):
    a.text(.5,y,t,ha="center",va="center",fontsize=18,transform=a.transAxes)
for ax in axes[:2]:
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(r/"special-continuation-monodromy.png",dpi=160,
            metadata={"Software":"Matplotlib"})
fig.savefig(r/"special-continuation-monodromy.svg",
            metadata={"Date":None,"Creator":"Open mathematics course figures"})
plt.close(fig)
data={
 "panel_A":{"curve":"t^2=x^3","x_star":"-1/16","time_roots":["i/64","-i/64"],
            "display_coordinate":"zeta=16t","display_disc_radius":"1",
            "display_roots":["i/4","-i/4"],"display_anchor":"-1/2",
            "display_meridian_radius":"1/8","cuts":"horizontal to right disc boundary",
            "proof":"MC.A and MC.6"},
 "panel_B":{"base_hypersurface":"H={z=0}","cauchy_radius":"1/2",
            "dashed_inner_circle":"|z|=2/5, contained in extension domain",
            "anchor_hypothesis":"g=h near t=A' for the whole base",
            "extension":"Cauchy contour in z, then the identity theorem in t",
            "proof":"MC.15, MC.17--MC.19"},
 "panel_C":{"q":"dim_C V","d":"number of group generators, d<=m",
            "c":"ker(C[Gamma]->End_C(V))","a":"I c",
            "function_annihilation":"(gamma-1)c f_ai=0",
            "bound":"dim_C C[Gamma]/a<=1+d q^2","proof":"MC.21--MC.27"},
 "source_context":"https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf"}
(r/"special-continuation-monodromy-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
