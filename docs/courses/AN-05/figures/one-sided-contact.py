"""Original exact coordinate illustration for WX9--WX14 and W8--W16.

GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0 public-domain dedication.
No PDE solution, actual solution support, or actual theorem cutoff is supplied.
The central panel draws the explicitly constructed teaching cutoff of Exercise 5.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Patch
from matplotlib.lines import Line2D
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12,
                     "axes.titlesize": 14, "mathtext.fontset": "dejavusans",
                     "svg.hashsalt": "AN05-WX-one-sided-contact-20261005"})
blue, green, red, gold, purple = "#285a7a", "#176e67", "#aa343c", "#bd760e", "#76588b"
phi = lambda t: t+t*t/2
a, b = Q(-15,128), Q(-31,512)
assert b-a == Q(29,512)
assert Q(1,4)+Q(1,16) < 1  # squared maximum radius of kernel rectangle

fig, (kernel, contact, gap) = plt.subplots(1,3,figsize=(18.5,9))
fig.subplots_adjust(left=0.055,right=0.97,bottom=0.34,top=0.76,wspace=0.32)
fig.suptitle("One-sided smoothing and the compact-contact weight gap", y=0.965,
             fontsize=21, fontweight="bold", color="#22363f")
fig.text(0.5,0.91,"Exact coordinate teaching model: support envelopes are bounds, not solution data.",
         ha="center", fontsize=13)

# Panel A: the exact compact kernel support and the larger allowed ball.
kernel.add_patch(Circle((-2,0),1,facecolor="#eaf2f7",edgecolor=blue,lw=2))
kernel.add_patch(Rectangle((-2.5,-0.25),1,0.5,facecolor=green,alpha=0.23,
                           edgecolor=green,lw=2.3))
for x in (-3,-1):
    kernel.axvline(x,color=red,ls="--",lw=1.5)
kernel.plot([-2],[0],"o",color=blue,ms=5)
kernel.annotate(r"$B((-2,0),1)$",xy=(-2.56,0.84),xytext=(-3.02,1.20),
                arrowprops={"arrowstyle":"-","color":blue},color=blue,fontsize=13)
kernel.text(-2,0.36,r"$\operatorname{supp}j$",ha="center",color=green,fontsize=13)
kernel.text(-2,-0.54,r"$[-5/2,-3/2]\times[-1/4,1/4]$",ha="center",fontsize=11)
kernel.annotate("",xy=(-3,-1.23),xytext=(-1,-1.23),
                arrowprops={"arrowstyle":"<->","color":red,"lw":1.7})
kernel.text(-2,-1.16,r"$-3<q_1/h<-1$",ha="center",color=red,fontsize=13)
kernel.set(xlim=(-3.32,-0.68),ylim=(-1.43,1.40),xlabel=r"normal displacement $q_1/h$",
           ylabel=r"tangential displacement $q_2/h$",
           title="A. A kernel that shifts strictly inward")
kernel.set_xticks([-3,-2.5,-2,-1.5,-1])
kernel.set_yticks([-1,-0.25,0,0.25,1])
kernel.set_aspect("equal",adjustable="box")
kernel.grid(alpha=0.14)

# Panel B: exact model envelope F_* in a chart, with a separately specified chi.
# F_* has a central contact stem and the entire lower region t <= -1/8.
contact.add_patch(Rectangle((-0.85,-0.28),1.70,0.155,facecolor="#e4e6e6",edgecolor="none"))
contact.add_patch(Rectangle((-0.25,-0.125),0.5,0.125,facecolor="#e4e6e6",edgecolor="none"))
contact.add_patch(Rectangle((-0.75,-0.25),1.5,0.5,fill=False,edgecolor=purple,lw=2,ls="--"))
contact.add_patch(Rectangle((-0.50,-0.125),1.0,0.25,fill=False,edgecolor=green,lw=2))
contact.add_patch(Rectangle((-0.75,-0.25),1.5,0.125,facecolor=red,alpha=0.16,
                           edgecolor=red,lw=1.5,hatch="///"))
contact.add_patch(Rectangle((-0.25,-0.0625),0.5,0.125,facecolor=blue,alpha=0.16,
                           edgecolor=blue,lw=1.8))
contact.axhline(0,color="#46545d",lw=1.3)
contact.plot([-0.25,0.25],[0,0],color=gold,lw=6,solid_capstyle="round")
contact.annotate(r"$K\subset K_*=[-1/4,1/4]\times\{0\}$",
                 xy=(0.03,0),xytext=(-0.78,0.205),fontsize=11.5,color=gold,
                 arrowprops={"arrowstyle":"-","color":gold,"connectionstyle":"arc3,rad=-0.2"})
contact.text(0.12,0.037,r"$N$",color=blue,fontsize=14,ha="center")
contact.text(0,-0.183,r"$E_*:\ -1/4\leq t\leq-1/8$",color=red,ha="center",fontsize=12)
contact.text(0,-0.270,r"$F\subset F_*$ (gray envelope)",ha="center",fontsize=10.5,color="#525859")
contact.set(xlim=(-0.85,0.85),ylim=(-0.28,0.28),xlabel=r"tangential coordinate $x$",
            ylabel=r"normal coordinate $t$",title="B. Cover the entire contact envelope")
contact.set_xticks([-0.75,-0.5,-0.25,0,0.25,0.5,0.75])
contact.set_xticklabels([r"$-3/4$",r"$-1/2$",r"$-1/4$","0",r"$1/4$",r"$1/2$",r"$3/4$"],fontsize=10)
contact.set_yticks([-0.25,-0.125,-0.0625,0,0.0625,0.125,0.25])
contact.set_yticklabels([r"$-1/4$",r"$-1/8$",r"$-1/16$","0",r"$1/16$",r"$1/8$",r"$1/4$"],fontsize=10)
contact.grid(alpha=0.12)
contact.legend(handles=[Line2D([0],[0],color=green,lw=2,label=r"$O$: constructed $\chi=1$"),
                        Line2D([0],[0],color=purple,lw=2,ls="--",label=r"$\operatorname{supp}\chi$ bound"),
                        Patch(facecolor=red,alpha=.2,hatch="///",label=r"applied-error envelope $E_*$")],
               loc="lower left",bbox_to_anchor=(0,1.13),frameon=False,fontsize=10,ncol=1)

# Panel C: a scalar level graph, not a support drawing or a Hamilton curve.
ts=np.linspace(-0.26,0.055,650)
gap.axvspan(-0.25,-0.125,color=red,alpha=.10)
gap.axvspan(-0.0625,0,color=blue,alpha=.12)
gap.plot(ts,phi(ts),lw=2.8,color="#344a56")
gap.hlines([float(a),float(b)],-0.26,0.044,colors=[red,blue],linestyles="--",lw=1.5)
gap.vlines([-0.125,-0.0625],-0.255,[float(a),float(b)],colors=[red,blue],linestyles=":",lw=1.2)
gap.scatter([-0.125,-0.0625],[float(a),float(b)],s=48,color=[red,blue],zorder=5)
gap.annotate(r"$a=\phi(-1/8)=-15/128$",xy=(-0.125,float(a)),xytext=(-0.255,-0.170),
             color=red,fontsize=11,arrowprops={"arrowstyle":"-","color":red})
gap.annotate(r"$b=\phi(-1/16)=-31/512$",xy=(-0.0625,float(b)),xytext=(-0.255,-0.029),
             color=blue,fontsize=11,arrowprops={"arrowstyle":"-","color":blue})
gap.annotate("",xy=(0.025,float(a)),xytext=(0.025,float(b)),
             arrowprops={"arrowstyle":"<->","color":green,"lw":2})
gap.text(0.038,(float(a)+float(b))/2,r"$b-a>0$",rotation=90,va="center",color=green,fontsize=12)
gap.text(-0.255,0.033,r"$\phi(t)=t+t^2/2$",fontsize=13,color="#344a56")
gap.set(xlim=(-0.26,0.075),ylim=(-0.255,0.060),xlabel=r"normal coordinate $t$",
        ylabel=r"scalar weight level $\phi(t)$",title="C. Strict gap between error and target")
gap.set_xticks([-0.25,-0.125,-0.0625,0])
gap.set_xticklabels([r"$-1/4$",r"$-1/8$",r"$-1/16$","0"],fontsize=11)
gap.grid(alpha=.13)

for panel in (kernel,contact,gap):
    panel.spines[["top","right"]].set_visible(False)

fig.text(.195,.215,r"$j(q)=\dfrac{8}{I^2}\,\beta(2(q_1+2))\beta(4q_2)$",ha="center",fontsize=14)
fig.text(.195,.164,r"$z=y+q$, $y_1\leq0\ \Longrightarrow\ z_1\leq-3h/2<-h$",ha="center",fontsize=12)
fig.text(.515,.215,r"$\chi(t,x)=\Theta(2-8|t|)\Theta(3-4|x|)$",ha="center",fontsize=14)
fig.text(.515,.164,r"$\operatorname{supp}([P_e,\chi]u)\subset E_*$; $\chi=1$ on $N$",ha="center",fontsize=12)
fig.text(.835,.215,r"$b-a=29/512$",ha="center",fontsize=16,color=green)
fig.text(.835,.164,r"$\|u\|_{L^2(N)}^2\leq4C_0A^2\tau^{-3}e^{-29\tau/256}\to0$",ha="center",fontsize=12)
fig.text(.055,.086,"Fix the chart and e; fix tau; let h tend to zero in the graph norm; then let tau tend to infinity.",
         fontsize=12,color="#344a56")
fig.text(.055,.045,"Proof locators: WX9-WX14; W8-W16. Human source: L. Hormander, Analysis of Linear PDE IV, Section 28.4, pp. 243-247.",
         fontsize=10.5,color="#344a56")
fig.text(.97,.016,"Original figure: GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0.",
         ha="right",fontsize=9.5,color="#344a56")

png=HERE/"one-sided-contact.png"
svg=HERE/"one-sided-contact.svg"
fig.savefig(png,dpi=180,facecolor="white",metadata={"Title":"One-sided smoothing and compact-contact weight gap",
            "Author":"GPT-6.1 Sol (OpenAI)","Description":"Original exact teaching model, CC0; no PDE solution data"})
fig.savefig(svg,facecolor="white",metadata={"Title":"One-sided smoothing and compact-contact weight gap",
            "Creator":"GPT-6.1 Sol (OpenAI)","Rights":"CC0 1.0","Date":"2026-10-05"})
plt.close(fig)
result={"schema":"one-sided-contact-coordinate-render/v1","rendered_png":png.name,
        "pixels":list(Image.open(png).size),"svg":svg.name,
        "kernel_normal_support":["-5h/2","-3h/2"],"allowed_displacement":"(-3h,-h)",
        "error_upper_level":"t=-1/8","target_lower_level":"t=-1/16",
        "a":str(a),"b":str(b),"gap":str(b-a),
        "actual_solution_or_support_specified":False,"actual_theorem_cutoff_specified":False,
        "png_sha256":hashlib.sha256(png.read_bytes()).hexdigest().upper(),
        "svg_sha256":hashlib.sha256(svg.read_bytes()).hexdigest().upper(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
        "matplotlib_version":matplotlib.__version__}
(HERE/"render-result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
