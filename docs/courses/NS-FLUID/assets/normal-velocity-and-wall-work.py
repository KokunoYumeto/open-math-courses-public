"""Exact equatorial section of the NS-FLUID-06 boundary counterexample."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

HERE=Path(__file__).resolve().parent
R, omega, nu = 2.0, 0.5, 0.75
fig,ax=plt.subplots(figsize=(8,7))
fig.subplots_adjust(left=.12,right=.96,bottom=.17,top=.85)
ax.add_patch(Circle((0,0),R,facecolor="#edf3f7",edgecolor="#344e63",lw=2))
for radius in (1.,R):
    angles=np.linspace(0,2*np.pi,16,endpoint=False)
    x,y=radius*np.cos(angles),radius*np.sin(angles)
    ax.quiver(x,y,-omega*y,omega*x,color="#166499",angles="xy",
              scale_units="xy",scale=1,width=.007)
for angle in (0,np.pi/2,np.pi,3*np.pi/2):
    x,y=R*np.cos(angle),R*np.sin(angle)
    ax.quiver(x,y,x/R,y/R,color="#a14b25",angles="xy",
              scale_units="xy",scale=1,width=.007)
ax.axhline(0,color="#899399",lw=.7)
ax.axvline(0,color="#899399",lw=.7)
ax.set(xlim=(-3.6,3.6),ylim=(-3.6,3.6),aspect="equal",
       xlabel=r"$x_1$",ylabel=r"$x_2$",
       title=r"Section $x_3=0$: $R=2$, $\omega=1/2$, $\nu=3/4$"
       "\n" r"$u=\omega(-x_2,x_1,0)$, "
       r"$p=\omega^2(x_1^2+x_2^2)/2$, $f=0$")
ax.legend(handles=[Line2D([0],[0],color="#166499",lw=3,label="actual velocity u"),
                   Line2D([0],[0],color="#a14b25",lw=3,label="unit outward normal n")],
          loc="upper left",fontsize=11)
ax.text(0,-3.2,r"$u\cdot n=0$, but $u\neq0$ on the wall",ha="center",fontsize=12)
fig.text(.5,.035,r"$\nu\int_{B_R}|\nabla u|^2"
         r"=\nu\int_{\partial B_R}u\cdot\partial_nu"
         r"=8\pi\nu\omega^2R^3/3=4\pi$",
         ha="center",fontsize=12)
fig.savefig(HERE/"normal-velocity-and-wall-work.png",dpi=180)
fig.savefig(HERE/"normal-velocity-and-wall-work.svg")
plt.close(fig)
