"""Original exact frozen metric ellipses; CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R=10000.0
Lambda=(1+R*R)**0.5
parameters=[0.4,0.2,0.1]
colors=["#156a86","#bc591e","#46753b"]
t=np.linspace(0,2*np.pi,801)
fig,axes=plt.subplots(1,3,figsize=(13.5,5.4),sharex=True,sharey=True)
for ax,d,color in zip(axes,parameters,colors):
    a=1+d*d*Lambda
    A=R**0.5/a**0.5
    B=a**0.5/(d*d*R**0.5)
    ax.plot(A*np.cos(t),B*np.sin(t),color=color,linewidth=2.5)
    ax.fill(A*np.cos(t),B*np.sin(t),color=color,alpha=0.07)
    ax.axhline(0,color="#aaaaaa",linewidth=0.7)
    ax.axvline(0,color="#aaaaaa",linewidth=0.7)
    ax.set_aspect("equal",adjustable="box")
    ax.set_xlim(-11.5,11.5);ax.set_ylim(-11.5,11.5)
    ax.set_xticks([-10,-5,0,5,10]);ax.set_yticks([-10,-5,0,5,10])
    ax.grid(alpha=0.15)
    ax.set_title(rf"$d={d:g}$",fontsize=16,pad=10)
    ax.set_xlabel(r"$Y=\sqrt{R}\,\Delta x$",fontsize=12)
    ax.text(0.5,-0.23,rf"$H^2w=d^2={d*d:g}$",
            transform=ax.transAxes,ha="center",fontsize=13,color=color)
    ax.text(0.5,-0.33,rf"Area $=\pi/d^2={1/(d*d):g}\pi$",
            transform=ax.transAxes,ha="center",fontsize=11)
axes[0].set_ylabel(r"$\eta=\Delta\xi/\sqrt{R}$",fontsize=12)
fig.suptitle("A smaller parameter widens the cell and reduces the product error",
             fontsize=16,y=0.97)
fig.text(0.5,0.025,
         r"Exact frozen ellipses $g_d(\Delta x,\Delta\xi)=1$ at $R=10\,000$. "
         r"They are regions in symbol phase space.",ha="center",fontsize=10)
fig.subplots_adjust(left=0.07,right=0.98,top=0.84,bottom=0.25,wspace=0.13)
fig.savefig(Path(__file__).with_name("parameter-cells.png"),dpi=150,
            metadata={"Software":"Matplotlib; original CC0 diagram"})
plt.close(fig)
