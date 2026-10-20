"""Original reproducible geometry of full-section identity and cap detection."""
from pathlib import Path
from fractions import Fraction as Q
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

root=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":18,
                           "svg.hashsalt":"singular-directional-separation"})
blue,red,grey="#145da0","#a12b3a","#687587"
fig,axes=plt.subplots(3,1,figsize=(7.4,17.6),
    gridspec_kw={"height_ratios":[1.1,1.35,1.1]})
fig.subplots_adjust(left=.16,right=.95,top=.965,bottom=.025,hspace=.65)
a=axes[0];a.set_aspect("equal")
a.add_patch(Circle((0,0),1,facecolor="#f2f6fa",edgecolor=grey,lw=1.6))
a.add_patch(Circle((-.5,0),.125,facecolor="#f3cf6b",edgecolor="#a97d00",lw=1.6))
a.scatter([0],[0],s=65,color=red,zorder=4)
u=np.linspace(np.pi,0,301)
a.plot(.5*np.cos(u),.5*np.sin(u),color=blue,lw=2.5)
a.annotate("",xy=(.5,0),xytext=(.498,.07),
           arrowprops={"arrowstyle":"->","color":blue,"lw":2.5})
a.text(-.92,-.36,"Open zero patch",fontsize=17)
a.text(-.88,-.57,r"$D(-1/2,1/8)$",fontsize=17)
a.text(.10,-.15,r"$g(x)=x=0$",color=red,fontsize=16)
a.text(-.77,.79,"Euler coefficients on overlaps",fontsize=17,color=blue)
a.text(-.78,-.89,"Purity detects the center",fontsize=17,color=red)
a.set(xlim=(-1.06,1.06),ylim=(-1.06,1.06),xlabel=r"$\operatorname{Re}x$",
      ylabel=r"$\operatorname{Im}x$")
a.set_xticks([-1,0,1]);a.set_yticks([-1,0,1])
a.set_title("A. Identity on a smooth graph patch",fontsize=19,pad=15)

a=axes[1]
rho=1/32
yy=np.linspace(-.21,.21,601)
a.fill_betweenx(yy,-1.05,-.5-2*np.abs(yy),color=grey,alpha=.15)
a.plot(-.5-2*np.abs(yy),yy,"--",color=grey,lw=1.7)
for sign,color in [(1,blue),(-1,red)]:
    h=sign/8
    xx=np.linspace(-1.05,rho,1000)
    half=np.where(xx<=0,rho,np.sqrt(np.maximum(0,rho*rho-xx*xx)))
    a.fill_between(xx,h-half,h+half,color=color,alpha=.13)
    a.plot(xx,h-half,color=color,lw=1.3)
    a.plot(xx,h+half,color=color,lw=1.3)
    # Exact intersection J with W2: x<-1/2-2|Im t|.
    yp=np.linspace(h-rho,h+rho,201)
    cut=-.5-2*np.abs(yp)
    a.fill_betweenx(yp,-1.05,cut,color=color,alpha=.32)
    xc=np.linspace(-rho/2,rho,200)
    yc=np.where(xc<=0,rho,np.sqrt(np.maximum(0,rho*rho-xc*xc)))
    a.fill_between(xc,h-yc,h+yc,color=color,alpha=.32)
    a.plot([-rho/2,-rho/2],[h-rho,h+rho],color=color,lw=2)
    a.scatter([0],[h],color=color,s=40)
    a.text(-.42,h+.042,r"$h_+=i/8$"if sign==1 else r"$h_-=-i/8$",
           fontsize=17,color=color)
a.text(-1.02,.185,r"$J_+$",color=blue,fontsize=18)
a.text(-1.02,-.18,r"$J_-$",color=red,fontsize=18)
a.text(-.95,.015,r"$W_2$",color=grey,fontsize=18)
a.set(xlim=(-1.05,.07),ylim=(-.21,.21),xlabel=r"$\operatorname{Re}t$",
      ylabel=r"$\operatorname{Im}t$")
a.set_xticks([-1,-.5,0]);a.set_yticks([-.125,0,.125])
a.set_yticklabels([r"$-1/8$","0",r"$1/8$"])
a.set_title("B. Restriction detects the cap value\n"
            r"$x_*=-1/4,\quad \rho=1/32$",fontsize=19,pad=18)
a.text(-.31,.012,r"$Q(I_j)\hookrightarrow Q(J_j)$",
       ha="center",va="center",fontsize=17)
a.text(-.31,-.035,"SE.20",ha="center",va="center",fontsize=16)

a=axes[2];a.axis("off")
a.set_title("C. The singular germ is retained",fontsize=19,pad=16)
lines=[
 r"$\Phi^\infty(s)=0\quad\hbox{for every }\Phi$",
 r"$\Downarrow$",
 r"$s_{p_j}=0\quad\hbox{on every generic sheet}$",
 r"$\Downarrow\quad\hbox{smooth-branch identity}$",
 r"$s|_{A\setminus F^{-1}(H)}=0$",
 r"$\Downarrow\quad\operatorname{codim}Z\geq n+2$",
 r"$\mathcal{H}^{0}_{Z}(N)=0\quad\Longrightarrow\quad s=0$"]
# Mathtext supports \mathrm but not TeX's general \hbox primitive.
lines=[t.replace(r"\hbox{for every }",r"\mathrm{for\ every\ }")
        .replace(r"\hbox{on every generic sheet}",r"\mathrm{on\ every\ generic\ sheet}")
        .replace(r"\hbox{smooth-branch identity}",r"\mathrm{smooth\ branch\ identity}")
        for t in lines]
for y,t in zip(np.linspace(.93,.02,len(lines)),lines):
    a.text(.5,y,t,ha="center",va="center",fontsize=18,transform=a.transAxes)
for ax in axes[:2]:
    ax.spines[["top","right"]].set_visible(False)
fig.savefig(root/"singular-directional-separation.png",dpi=160,
            metadata={"Software":"Matplotlib"})
fig.savefig(root/"singular-directional-separation.svg",
            metadata={"Date":None,"Creator":"Open mathematics course figures"})
plt.close(fig)
data={
 "panel_A":{"parameter_ball_radius":"1","exception_equation":"g(x)=x",
            "zero_patch_center":"-1/2","zero_patch_radius":"1/8",
            "path":"x=(1/2)exp(i theta), pi>=theta>=0",
            "diagram_of_identity_hypothesis_not_sampled_section":True},
 "panel_B":{"curve":"t^2=x^3","x_star":"-1/4",
            "roots":["i/8","-i/8"],"rho":str(Q(1,32)),"a":"2",
            "W_equation":"Re t<-1/2-2|Im t|",
            "inner_cut_Re_T":"-1/64",
            "J_is_nonempty_and_inner_connected":True,
            "left_boundary_is_plot_crop_only":True},
 "panel_C":{"base_dimension":"n+1","normalized_ambient_dimension":"2n+1",
            "dim_Z_at_most":"n-1","codim_Z_at_least":"n+2"},
 "proof_locators":["SE.5","SE.6","SE.18","SE.20","SE.24","SE.27","SE.28"],
 "source_context":"https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf"}
(root/"singular-directional-separation-exact-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
