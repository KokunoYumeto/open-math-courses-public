"""Exact angular cone section and Gaussian level curves for the original proof."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Wedge

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
STEM="constant-strength-hypoellipticity-024"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
    "svg.fonttype":"none","svg.hashsalt":"AN02-HE-KG-024",
    "axes.titleweight":"bold","axes.spines.top":False,"axes.spines.right":False})
fig,(left,right)=plt.subplots(1,2,figsize=(20,10),dpi=120)
fig.subplots_adjust(left=.06,right=.96,bottom=.21,top=.77,wspace=.25)
fig.suptitle("Two ways to recover regularity from an equation",fontsize=28,y=.966,weight="bold")
fig.text(.5,.915,"An inverse preserves Fourier decay in a cone. Variable drift transfers diffusion into position.",
    ha="center",fontsize=18)
left.add_patch(Circle((0,0),4,color="#f0e6dc",zorder=1))
left.add_patch(Wedge((0,0),4,-30,30,facecolor="#ead69c",edgecolor="none",zorder=2))
left.add_patch(Wedge((0,0),4,-15,15,facecolor="#b9d9ee",edgecolor="none",zorder=3))
for angle,color,style in ((30,"#a68a37","--"),(-30,"#a68a37","--"),(15,"#21668e","-"),(-15,"#21668e","-")):
    a=np.deg2rad(angle)
    left.plot([0,4*np.cos(a)],[0,4*np.sin(a)],color=color,lw=1.8,ls=style,zorder=4)
for r in (1,2):left.add_patch(Circle((0,0),r,fill=False,color="#586676",lw=1.7,ls=(0,(4,3)),zorder=6))
left.annotate("",xy=(3.7,0),xytext=(0,0),arrowprops={"arrowstyle":"-|>","lw":2.5,"color":"#1e4e70"},zorder=8)
left.text(3.40,-.29,r"$\xi_0$",fontsize=19,color="#1e4e70",zorder=9)
left.text(2.45,.50,r"$\Gamma_1$: power $4$",fontsize=14,color="#174967",rotation=15,zorder=9)
left.text(2.13,1.63,r"$\Gamma_0$: half-angle $\pi/6$",fontsize=14,color="#806415",rotation=20,zorder=9)
left.text(-3.38,2.48,"Outside the larger cone:\npower -3",fontsize=15,color="#7a512d",
    bbox={"facecolor":"white","edgecolor":"none","alpha":.96},zorder=10)
left.text(-3.45,-2.67,"N = 4, M = 3; powers shown for r >= 2\nk = 1 for r <= 1\nThe annulus 1 < r < 2 smooths the weight.",
    fontsize=14,bbox={"facecolor":"white","edgecolor":"none","alpha":.96},zorder=10)
left.text(-.45,.10,"r = 1",fontsize=12,zorder=9)
left.text(-2.16,-.20,"r = 2",fontsize=12,zorder=9)
left.set(xlim=(-4.3,4.3),ylim=(-3.9,3.9),xlabel=r"frequency $\xi_1$",ylabel=r"frequency $\xi_2$")
left.set_aspect("equal",adjustable="box")
left.set_title("HE19-HE21: a regularity cone stays regular",pad=18,fontsize=18)
left.grid(alpha=.12,zorder=0)

theta=np.linspace(0,2*np.pi,1201)
W=2*np.cos(theta);Z=np.cos(theta)+np.sin(theta)/np.sqrt(3)
for tau,color,lw in ((1,"#246889",2.8),(.25,"#b46820",2.6)):
    w=np.sqrt(tau)*W;z=tau**1.5*Z
    right.plot(w,z,color=color,lw=lw,label=r"$\tau=1$" if tau==1 else r"$\tau=1/4$")
right.plot([-2.3,2.3],[-1.15,1.15],ls=(0,(5,3)),lw=1.7,color="#6d7380")
right.scatter([0],[0],s=40,color="#354759",zorder=8)
right.annotate("conditional mean at time 1:\nz = w/2",xy=(1.82,.91),xytext=(.28,1.42),
    arrowprops={"arrowstyle":"-","color":"#626e78"},fontsize=14,color="#52606c")
right.text(-2.18,-1.62,"Exact level curves, not support boundaries.\nH is positive everywhere for every tau > 0.",fontsize=14,
    bbox={"facecolor":"white","edgecolor":"#d0d8dd","boxstyle":"round,pad=.55"},zorder=10)
right.set(xlim=(-2.45,2.45),ylim=(-1.85,1.85),xlabel="velocity difference w",ylabel="position after subtracting source drift z")
right.set_aspect("equal",adjustable="box")
right.set_title("KG2-KG3, KG12: diffusion reaches position",pad=18,fontsize=18)
right.legend(loc="upper left",fontsize=15,framealpha=.96)
right.grid(alpha=.16)
fig.text(.25,.138,r"$k_N=\langle\xi\rangle^{\beta(r)b(\theta)}$; inner half-angle $\pi/12$.",
    fontsize=17,ha="center",color="#34536c")
fig.text(.75,.138,r"$w=2\sqrt{\tau}\cos\theta,\quad z=\tau^{3/2}(\cos\theta+\sin\theta/\sqrt{3})$",
    fontsize=17,ha="center",color="#34536c")
fig.text(.5,.067,"Proof locators: HE19-HE22 and KG2-KG12.  Human source comparison: Hormander II, section 13.4, printed pages 191-194.",
    fontsize=14,ha="center",color="#43566a")
fig.savefig(OUT/(STEM+".png"),dpi=120,metadata={"Software":"AN02 original reproducible mathematical figure"})
fig.savefig(OUT/(STEM+".svg"),metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI)",
    "Title":"Fourier regularity cones and the Kolmogorov Gaussian"})
plt.close(fig)
geometry={"schema":"constant-strength-hypoellipticity-exact-figure/v1",
    "left":{"coordinate_section":"two real Fourier coordinates","axis":[1,0],
        "inner_half_angle":"pi/12","outer_half_angle":"pi/6","N":4,"M":3,
        "radial_cutoff_zero_through":1,"radial_cutoff_one_from":2,
        "display_radius":4,"powers_only_apply_at_radius_at_least_2":True,
        "transition_inside_outer_cone":True,"weight_plot_is_geometric_section":True},
    "right":{"coordinates":"w=v-v0,z=x-x0-tau*v0","times":["1/4","1"],
        "level":"w^2/(4*tau)+3*(z-tau*w/2)^2/tau^3=1",
        "exact_parametrization":"w=2*sqrt(tau)*cos(theta); z=tau^(3/2)*(cos(theta)+sin(theta)/sqrt(3))",
        "covariance":"[[2*tau,tau^2],[tau^2,2*tau^3/3]]","determinant":"tau^4/3",
        "conditional_mean_at_time_1":"z=w/2","density_positive_everywhere_at_positive_time":True,
        "contours_are_support_boundaries":False,"contours_are_wavefronts":False},
    "proof_locators":["HE19","HE20","HE21","HE22","KG2","KG3","KG11","KG12"],
    "editable_SVG_text":True,"external_assets":False}
(OUT/(STEM+".json")).write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"png":str(OUT/(STEM+".png")),"size":[2400,1200],"exact_geometry":True}))
