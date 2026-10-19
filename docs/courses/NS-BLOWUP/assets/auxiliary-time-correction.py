"""The full temporal correction and its receiving maps, TM0–TM7."""
from pathlib import Path
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,14),dpi=100,facecolor="#f7f9fc")
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,14),ylim=(0,14));ax.axis("off")
ink,blue,orange="#172a42","#1b638f","#a24c16"
def text(x,y,s,size=20,color=ink):
    ax.text(x,y,s,va="top",fontsize=size,color=color,linespacing=1.45)
def panel(y,h,title):
    ax.add_patch(FancyBboxPatch((.45,y),13.1,h,boxstyle="round,pad=.12",
        linewidth=1,edgecolor="#b9cadb",facecolor="white"))
    text(.75,y+h-.2,title,20,blue)
text(.65,13.73,"The auxiliary-time inverse and the actual compact velocity",25)
text(.65,13.15,r"Original incoming classes of TM4, with $\alpha\geq0.9$ and $\kappa_s=10^{-5}$",17)
panel(9.75,2.85,"1  Invert only the zero Haar mean · TM1–TM2")
text(.85,11.85,r"$N=v_t\cdot\partial_y,\qquad"
     r"N^{-1}F=\sum_{k\ne0}\frac{\widehat{F}(k)}{2\pi i\,v_t\cdot k}\,e^{2\pi i k\cdot y}$",22)
text(.85,10.95,r"$\Delta v=-c^{-1}N^{-1}E_\theta^\circ,\qquad"
     r"\gamma_d=-c^{-1}N^{-1}E_z^\circ,\qquad c=T_g^{i_0}Q^{1+h}$",22)
text(.85,10.25,"The fixed Fourier multiplier preserves slow and radial support.",17)
panel(6.65,2.75,"2  Take the full curl of the compact potential · TM3, TM5")
text(.85,8.62,r"$\Psi_*=\mathsf{T}_1\gamma_d,\qquad"
     r"\Delta\beta=-\varepsilon\partial_Z\Psi_*,\qquad"
     r"\Delta\gamma=\gamma_d-\mathcal{A}_1\gamma_d$",22)
text(.85,7.78,r"$(D_r+R^{-1})\Delta\beta+D_z\Delta\gamma=0,\qquad"
     r"\langle\Delta\beta,\Delta v,\Delta\gamma\rangle_y=0$",22)
text(.85,7.02,"Both velocity moments are unchanged; every cutoff term remains.",17)
panel(3.55,2.75,"3  Retain the exact fast-time residual · TM3–TM4, TM7")
text(.85,5.57,r"$cN\Delta\gamma=-E_z^\circ+\mathcal{F}_{\rm ax},\qquad"
     r"\mathcal{F}_{\rm ax}=\mathcal{A}_1E_z^\circ$",23)
text(.85,4.73,r"$E_{\theta,\rm new}-\langle E_\theta\rangle_y,\quad"
     r"E_{z,\rm new}-\langle E_z\rangle_y-\mathcal{F}_{\rm ax}"
     r"\ \in\ \mathsf{M}_{\alpha+1-2\kappa_s}$",21)
text(.85,3.98,"Recompute the complete pressure and all nonlinear products.",17)
panel(.65,2.55,"4  The averaged and nonzero angular outputs · TM6–TM7")
text(.85,2.47,r"$\langle\delta E_\theta\rangle_y,\ \langle\delta E_z\rangle_y"
     r"\in\mathsf{M}_{\alpha+1.9},\qquad"
     r"\delta(\mathcal{P},\mathcal{J}_\theta,\mathcal{J}_z)\in\mathsf{S}_{\alpha+0.9}$",22)
text(.85,1.65,r"$w\in\mathsf{W}_{1/2}\quad\Longrightarrow\quad"
     r"\mathsf{P}_{\ne0}\delta\mathscr{R}\in\mathsf{W}_\alpha$",23)
text(.85,.98,"These are exact receiving bounds; the old three defects still remain.",17,orange)
text(.65,.3,"Source: OpenAI, Lemma 8.6, pages 95–96; Step 3, page 110.  Full original viscosity: TM5.  Proofs: TM0–TM7.",12.5)
for ext in ["svg","png"]:fig.savefig(out/("auxiliary-time-correction."+ext),dpi=100)
p=out/"auxiliary-time-correction.svg"
p.write_text(re.sub(r'width="1008pt" height="1008pt"','width="1400" height="1400"',
    p.read_text(encoding="utf8")),encoding="utf8")
plt.close(fig)
