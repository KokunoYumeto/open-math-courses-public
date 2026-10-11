"""Original exact example AD.24-26; numerical curves illustrate proved formulas."""
from pathlib import Path
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
for height in [Fraction(0),Fraction(1,2),Fraction(1)]:
    b=1+height
    for t in [Fraction(-2),Fraction(-1),Fraction(0),Fraction(1),Fraction(2)]:
        re=b/(b*b+t*t);im=t/(b*b+t*t);c=1/(2*b)
        assert (re-c)**2+im**2==c*c
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":22,"mathtext.fontset":"dejavusans"})
fig=plt.figure(figsize=(9,12),dpi=100,facecolor="white")
fig.text(.5,.97,"One density, two strip boundaries",ha="center",va="top",fontsize=27,weight="bold")
fig.text(.5,.885,r"$h(s)=1/s,\quad a(s)=s,\quad F(z)=1/(1-iz)$",ha="center",fontsize=25)
ax=fig.add_axes([.15,.36,.80,.46])
theta=np.linspace(-np.pi+1e-6,np.pi-1e-6,1601)
for height,color,lw,style in [(0,"#176c9b",3.5,"-"),(.5,"#9ca3af",2.0,"--"),(1,"#b65022",3.5,"-")]:
    c=1/(2*(1+height))
    label={0:r"Lower edge: $\psi(a u_t)$",.5:r"Middle height $y=1/2$",1:r"Upper edge: $\varphi(a u_t)$"}[height]
    ax.plot(c*(1+np.cos(theta)),c*np.sin(theta),color=color,lw=lw,ls=style,label=label)
ax.scatter([1,.5],[0,0],color=["#176c9b","#b65022"],s=90,zorder=5)
ax.scatter([0],[0],facecolor="white",edgecolor="#162c3d",s=85,zorder=6)
ax.annotate(r"$t=0:\ 1$",xy=(1,0),xytext=(.92,-.16),fontsize=24,color="#176c9b",ha="center",arrowprops={"arrowstyle":"-","color":"#176c9b"})
ax.annotate(r"$t=0:\ 1/2$",xy=(.5,0),xytext=(.65,.12),fontsize=24,color="#b65022",ha="center",arrowprops={"arrowstyle":"-","color":"#b65022"})
ax.scatter([.5,.4],[.5,.2],color=["#176c9b","#b65022"],s=65,zorder=5)
ax.annotate(r"$t=1$",xy=(.5,.5),xytext=(.64,.47),fontsize=23,color="#176c9b")
ax.annotate(r"$t=1$",xy=(.4,.2),xytext=(.10,.30),fontsize=23,color="#b65022",arrowprops={"arrowstyle":"-","color":"#b65022"})
ax.set_xlim(-.07,1.07);ax.set_ylim(-.57,.57);ax.set_aspect("equal")
ax.set_xlabel(r"$\operatorname{Re}F$",fontsize=25);ax.set_ylabel(r"$\operatorname{Im}F$",fontsize=25)
ax.set_xticks([0,.5,1]);ax.set_yticks([-.5,0,.5]);ax.tick_params(labelsize=21)
ax.grid(alpha=.18)
handles,labels=ax.get_legend_handles_labels()
fig.legend(handles,labels,loc="lower center",bbox_to_anchor=(.52,.14),frameon=False,fontsize=21,ncol=1)
fig.text(.5,.105,r"$\psi(1)=\infty,\qquad \psi(a)=1,\quad\varphi(a)=1/2$",ha="center",fontsize=24)
fig.text(.5,.063,"The open point 0 is a limit as |t| tends to infinity.",ha="center",fontsize=19)
fig.text(.5,.032,"Exact circles and boundary values: AD.25-26.",ha="center",fontsize=19)
out=P/"abelian-kms-boundary-circles.png"
fig.savefig(out,dpi=100);plt.close(fig)
print(out)
