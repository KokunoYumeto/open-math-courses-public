"""Reproducible algebraic reduction and free-direction support geometry."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
root=Path(__file__).resolve().parent
out=root if root.name=="assets" else root/"assets";out.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
                     "svg.hashsalt":"AS-FD-Spencer","axes.spines.top":False,"axes.spines.right":False})
fig=plt.figure(figsize=(14,8.5))
grid=fig.add_gridspec(2,2,height_ratios=[1,.95],width_ratios=[1.15,1],hspace=.42,wspace=.27)
ax=fig.add_subplot(grid[:,0]);ax.set_axis_off()
blue,purple,red,green="#215d8c","#6c4d90","#a54536","#38755b"
ax.set_title("A  The entire algebraic Spencer reduction",loc="left",weight="bold",pad=20)
def box(y,text,color):
    ax.text(.5,y,text,ha="center",va="center",transform=ax.transAxes,
            fontsize=15,color=color,bbox={"boxstyle":"round,pad=.7","facecolor":"#faf9f4","edgecolor":color,"linewidth":1.6})
def arrow(y1,y2,text):
    ax.annotate("",xy=(.5,y2),xytext=(.5,y1),xycoords="axes fraction",
                arrowprops={"arrowstyle":"->","color":"#4e5e65","lw":1.5})
    ax.text(.55,(y1+y2)/2,text,transform=ax.transAxes,va="center",fontsize=11)
box(.88,r"$K^\bullet(\partial_{y_j}+z_j\tau)[d]$",blue)
arrow(.81,.69,r"$C^{-1}$,  $C=\exp(\tau^{-1}\sum_j\partial_{z_j}\partial_{y_j})$")
box(.63,r"$K^\bullet(z_1\tau,\ldots,z_d\tau)[d]$",purple)
arrow(.56,.44,"regular sequence; all lower cohomology is zero")
box(.38,r"$H^0=\mathbb{C}[u,y,\tau,\tau^{-1}]\,\gamma$",green)
arrow(.31,.19,r"$I(y^\alpha\tau^m\gamma)=\tau^{m-|\alpha|-d}\nu^\alpha e_\Delta$")
box(.13,r"$\Delta_{\rm alg}[\tau^{-1}]$",blue)
ax.text(.04,.005,"AS.14–AS.21: the exponential is finite on each polynomial in y.\n"
        "The moment map respects every endpoint Weyl action.",transform=ax.transAxes,fontsize=11,color="#3b4e5b")
ax=fig.add_subplot(grid[0,1]);ax.set_axis_off()
ax.set_title("B  Both diagonal classes before localization",loc="left",weight="bold",pad=18)
for y,text,color in [
    (.82,r"$a=\tau^d\gamma,\quad z_ja=wa=D_{u_i}a=0$",blue),
    (.58,r"$j(e_\Delta)=a,\qquad I(a)=e_\Delta$",green),
    (.38,r"$h=\dfrac{(-1)^d}{d!}\,a$",red),
    (.18,r"$h'=\dfrac{1}{d!}\,a'$",purple),
]:
    ax.text(.03,y,text,transform=ax.transAxes,fontsize=16,color=color)
ax.text(.03,-.02,"AS.22–AS.27 and AS.32–AS.35: raw ordered classes.\n"
        "The opposite spatial reflection contributes its own sign.",transform=ax.transAxes,fontsize=11)
ax=fig.add_subplot(grid[1,1])
ax.set_title("C  A free source direction contracts both opens",loc="left",weight="bold",fontsize=12,pad=15)
b=np.linspace(-1,1,301)
ax.fill_between(b,-2,-np.abs(b),color="#e0e9ef")
ax.plot(b,-np.abs(b),color=blue,lw=2)
ax.axhline(1,color=green,ls="--",lw=1)
ax.text(-.96,1.12,r"$a=c=1$",color=green,fontsize=11)
ax.text(-.94,-1.75,r"$G_1:\ a\leq-|b|$",color=blue,fontsize=12)
for a,col in [(-.25,purple),(-1.5,red)]:
    ax.plot([.5,.5],[a,1],color=col,lw=1.6,alpha=.9)
    ax.annotate("",xy=(.5,.70),xytext=(.5,.30),arrowprops={"arrowstyle":"->","color":col,"lw":1.7})
    ax.scatter([.5],[a],color=col,s=24,zorder=4)
ax.text(-.95,.12,"Complement points stay\nin the complement.",fontsize=10,color=purple)
ax.set(xlim=(-1,1),ylim=(-2,1.6),xlabel=r"$b$ (one real slice)",ylabel=r"$a$ (free direction)")
fig.suptitle("Incidence convolution, the diagonal module and a free source direction",
             fontsize=18,weight="bold",y=.98)
fig.subplots_adjust(left=.055,right=.965,bottom=.10,top=.90)
fig.text(.055,.025,"A–B: polynomial Ore localization at the time derivative; no assertion about localization of arbitrary analytic coefficient rings.  "
         "C: FD.5–FD.9, with R=2 and eta=1.",fontsize=10,color="#364b58")
stem="affine-spencer-and-free-direction"
fig.savefig(out/(stem+".png"),dpi=180)
fig.savefig(out/(stem+".svg"),metadata={"Date":None});plt.close(fig)
data={"spencer_dimensions":"every d>=0","tau":"D_w","relative_degree_interval":"[-d,0]",
      "finite_conjugation":"C=exp(tau^-1 sum_j partial_zj partial_yj)",
      "moment_map":"I(y^alpha tau^m gamma)=tau^(m-|alpha|-d) nu^alpha e_Delta",
      "diagonal_map":"j(e_Delta)=tau^d gamma",
      "forward_raw_pole_factor":"(-1)^d/d!","opposite_raw_pole_factor":"1/d!",
      "support_slice":{"eta":1,"R":2,"c":1,"b_sample":"1/2",
      "complement_start_a":"-1/4","whole_domain_start_a":"-3/2"},
      "support_homotopy":"a_s=(1-s)a+s*c; b fixed",
      "source_proof_locators":["AS.14-AS.27","AS.32-AS.35","FD.5-FD.9"],
      "canonical_microlocal_composition_identity_asserted":False}
(out/(stem+"-exact-data.json")).write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
if root!=out:(out/Path(__file__).name).write_bytes(Path(__file__).read_bytes())
print(json.dumps({"pixels":[2520,1530],"media_files":3,"editable_figure_source":True}))

