"""Reproduce the exact reflection diagram; no numerical PDE approximation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch

N=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":13,"axes.titlesize":16,"savefig.facecolor":"white"})
fig=plt.figure(figsize=(16,10))
left=fig.add_axes([.04,.29,.43,.54])
right=fig.add_axes([.51,.29,.46,.54])
fig.suptitle("Exact phase and reflection: the original graph kernel and the full L² kernel",fontsize=21,weight="bold",y=.96)
left.set_title(r"$\rho(x_1,x_2)=(x_1,-x_2),\quad Jf(x)=e^{-i\varepsilon x_2}f(\rho x)$",pad=35)
left.add_patch(Rectangle((-.25,-.25),.5,.5,facecolor="#f0f6fb",edgecolor="#25455a",linewidth=2))
left.plot([-.25,.25],[0,0],color="#708b9a",linestyle="--",linewidth=1)
left.scatter([.125,.125],[.125,-.125],s=55,c=["#bd4d37","#2d6790"],zorder=4)
left.annotate("",xy=(.125,-.115),xytext=(.125,.115),arrowprops=dict(arrowstyle="->",color="#25455a",linewidth=2))
left.text(.145,.14,r"$x=(1/8,1/8)$",fontsize=13)
left.text(.145,-.17,r"$\rho x=(1/8,-1/8)$",fontsize=13)
left.text(0,.285,r"$\gamma_{2,+}(Ju)=e^{-i\varepsilon/4}\gamma_{2,-}u$",ha="center",fontsize=15)
left.text(0,-.31,r"$\gamma_{2,-}(Ju)=e^{i\varepsilon/4}\gamma_{2,+}u$",ha="center",fontsize=15)
left.set_xlim(-.34,.39);left.set_ylim(-.34,.34)
left.set_xticks([-.25,0,.25],["−1/4","0","1/4"])
left.set_yticks([-.25,0,.25],["−1/4","0","1/4"])
left.set_xlabel(r"$x_1$");left.set_ylabel(r"$x_2$")
left.set_aspect("equal");left.spines[["top","right"]].set_visible(False)
right.axis("off");right.set_xlim(0,1);right.set_ylim(0,1)
def box(x,y,w,h,label,color):
    right.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.013",facecolor=color,edgecolor="#31465a",linewidth=1.5))
    right.text(x+w/2,y+h/2,label,ha="center",va="center",linespacing=1.5,fontsize=14)
def arrow(start,end,label,offset=(0,0)):
    right.annotate("",xy=end,xytext=start,arrowprops=dict(arrowstyle="<->",linewidth=1.8,color="#24475c"))
    right.text((start[0]+end[0])/2+offset[0],(start[1]+end[1])/2+offset[1],label,ha="center",va="center",fontsize=13)
box(.025,.64,.40,.22,r"$N=\ker(P:H\to L^2)$"+"\nOriginal graph kernel","#eaf3fa")
box(.59,.64,.385,.22,r"$\ker T_{\min}^*\cap H$"+"\nGraph part of the\nadjoint kernel","#eaf3fa")
arrow((.435,.75),(.58,.75),r"$J$",offset=(0,.052))
right.text(.50,.575,r"$\kappa_\beta^{-1}\|u\|_H\leq\|Ju\|_H\leq\kappa_\beta\|u\|_H$",ha="center",fontsize=13)
box(.025,.22,.40,.22,r"$K_P=\{u\in L^2:Pu=0\}$"+"\nFull distributional kernel","#fff3de")
box(.59,.22,.385,.22,r"$\ker T_{\min}^*$"+"\nFull L² adjoint kernel","#fff3de")
arrow((.435,.33),(.58,.33),r"$J$",offset=(0,.052))
right.text(.50,.14,"The full distributional kernels carry the original L² norm.",ha="center",fontsize=12)
for x in [.225,.78]:
    right.annotate("",xy=(x,.46),xytext=(x,.62),arrowprops=dict(arrowstyle="->",linewidth=1.6,color="#24475c"))
    right.text(x+.065,.54,"inclusion",ha="center",fontsize=11)
fig.text(.50,.215,r"$Ju_z^{\rm e}=v_z^{\rm e}=g_{-z-i\varepsilon}^{\rm e},\quad Ju_z^{\rm o}=v_z^{\rm o}=g_{-z-i\varepsilon}^{\rm o},\quad J^2=I$",ha="center",fontsize=17)
fig.text(.50,.165,r"$JH_{\min}=H_{\min},\quad AJ=JP,\quad A=-\partial_1^2-\partial_2-i\varepsilon x_1\partial_1-i\varepsilon,\quad F=JEJ$",ha="center",fontsize=15)
fig.text(.50,.11,r"$\varepsilon=2/(Ka),\quad K=41472\lambda_*\sqrt{33}\,e^2,\quad a=\sqrt{(\sqrt{2}-1)/2},\quad U=(-1/4,1/4)^2$",ha="center",fontsize=15)
fig.text(.50,.055,"The picture compares the unchanged operators. J is unitary in L²; the original graph metric retains its full phase contribution.\nProofs: JM4–JM5, JM13–JM20, JM23 and JM27. Boundary traces: JM17.",ha="center",fontsize=12)
path=N/"reflection_graph_kernel_bridge.png"
fig.savefig(path,dpi=150)
plt.close(fig)
def rec(path):
    data=path.read_bytes()
    return dict(path=path.name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
receipt=dict(created_utc=datetime.now(timezone.utc).isoformat(),figure=rec(path),reproducible_source=rec(Path(__file__)),license="CC0-1.0",figure_kind="Exact diagram, not a PDE numerical sample",original_square="(-1/4,1/4)^2",reflection="rho(x1,x2)=(x1,-x2)",phase="exp(-i epsilon x2)",epsilon="2/(Ka)",K="41472 lambda_star sqrt(33) e^2",a="sqrt((sqrt(2)-1)/2)",reflection_determinant=-1,absolute_jacobian=1,sample_point=["1/8","1/8"],reflected_point=["1/8","-1/8"],proof_locators=["JM4","JM5","JM13","JM14","JM15","JM16","JM17","JM19","JM20","JM23","JM27"],graph_kernel_intersection_retained=True,graph_unitarity_claimed=False,formal_adjoint_zero_order_term_retained=True)
(N/"FIGURE_FORMULAS_AND_REPRODUCTION.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(figure=rec(path),exact_diagram=True)))
