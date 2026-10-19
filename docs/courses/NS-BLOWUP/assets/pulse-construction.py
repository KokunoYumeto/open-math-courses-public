"""Exact maps in the pulse construction, PU1–PU8; no numerical flow data."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,13),dpi=100,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,13));ax.axis("off")
ink,blue,orange="#172a42","#1b638f","#a24c16"
def text(x,y,s,size=20,color=ink):
    ax.text(x,y,s,va="top",fontsize=size,color=color,linespacing=1.45)
def panel(y,h,title):
    ax.add_patch(FancyBboxPatch((.45,y),13.1,h,boxstyle="round,pad=.12",
        linewidth=1,edgecolor="#b9cadb",facecolor="white"))
    text(.75,y+h-.2,title,20,blue)
text(.65,12.72,"From the pulse equation to an actual velocity",25)
text(.65,12.17,"Original phase, moving plane, curl, pressure and retained residual",16)
panel(8.8,2.85,"1  The actual phase and its transverse equation · PU1–PU4")
text(.85,10.94,r"$\Phi=p\theta+p_z Z/\varepsilon+x_0R-v(pF+p_zG),\quad n=\nabla_*\Phi$",21)
text(.85,10.28,r"$t_m'+\mathcal{K}t_m+m^2d\,t_m+ikm\,n\pi_m=-f_m,\quad n\cdot t_m=0$",21)
text(.85,9.61,r"$d=\varepsilon k^2|n|^2,\quad B_s^2=\frac{\lambda_0}{\varepsilon k^2(1+u_*^2)^{3/2}}$",22)
panel(6.35,2.1,"2  A moving frame supplies the exact inverse · PU2–PU4")
text(.85,7.78,r"$t_m=Bz_m,\qquad z_m(v)=\int_0^v V_m(v,w)g_m(w)\,dw$",22)
text(.85,7.10,r"$V_m(v,w)=e^{-(m^2-1)\int_w^v d(a)\,da}\,V_1(v,w)$",22)
panel(3.65,2.35,"3  Take the whole curl after the cutoff · PU6")
text(.85,5.28,r"$\widehat{C}_m=\frac{i\,n\times(\psi t_m)}{km|n|^2},\quad"
                  r"\widehat{\pi}_m=\psi\pi_m$",23)
text(.85,4.52,r"$\operatorname{curl}_*(\widehat{C}_m e^{ikm\Phi})"
                  r"=(\widehat{t}_m+\widehat{r}_m)e^{ikm\Phi},"
                  r"\quad\operatorname{div}_*\operatorname{curl}_*=0$",20)
panel(.75,2.55,"4  The exact residual retains the curl and endpoint terms · PU7–PU8")
text(.85,2.64,r"$\mathscr{L}_m(a,\widehat{\pi}_m)+\mathscr{L}^{\rm rem}_m"
                  r"(a,\widehat{\pi}_m)+f_m,\quad a=\widehat{t}_m+\widehat{r}_m$",20)
text(.85,1.99,r"$=(1-\psi)f_m+\psi't_m+\mathscr{L}_m(\widehat{r}_m,0)"
                  r"+\mathscr{L}^{\rm rem}_m(a,\widehat{\pi}_m)$",20)
text(.85,1.29,"Cutoff residual: all-order physical decay.  Curl residual: kept in the class estimate.",14,orange)
text(.65,.38,"Source: OpenAI, sections 7 and 9.1.  Complete proofs and original viscosity factors: PU0–PU9.",13)
for ext in ["svg","png"]:fig.savefig(out/("pulse-construction."+ext),dpi=100)
p=out/"pulse-construction.svg"
p.write_text(re.sub(r'width="1008pt" height="936pt"','width="1400" height="1300"',
    p.read_text(encoding="utf8")),encoding="utf8")
plt.close(fig)
