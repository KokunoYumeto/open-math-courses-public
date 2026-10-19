"""Exact compact radial and mean maps, RP1–RP8 and RM1–RM4."""
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
text(.65,13.73,"Compact radial corrections with every defect retained",25)
text(.65,13.15,"An exact map of operators and moments; no numerical flow samples",16)
panel(9.75,2.85,"1  The physical path fixes the radial operator · RP1–RP3")
text(.85,11.85,r"$y'=y+M((R')^{d_r}-R^{d_r})v_r,\qquad M=\Lambda_g^{i_0}Q^{d_r/2}$",22)
text(.85,11.13,r"$\mathsf{T}_e f=R^{-e}\mathcal{I}_c(R^ef),\qquad"
     r"(D_r+e/R)\mathsf{T}_e f=f-\mathcal{A}_e f$",22)
text(.85,10.4,"The full-integral subtraction gives compact support; its remainder is explicit.",17)
panel(6.75,2.65,"2  Pressure and the actual solenoidal velocity · RP5–RP8")
text(.85,8.67,r"$p_m=\mathsf{T}_0(g_r-\rho\mathcal{P}),\qquad"
     r"\mathcal{P}=\int\langle g_r\rangle_y\,dR$",22)
text(.85,7.95,r"$\Psi=\mathsf{T}_1\gamma_d,\qquad"
     r"(\Delta\beta,\Delta\gamma)=(-\varepsilon\partial_Z\Psi,\gamma_d-\mathcal{A}_1\gamma_d)$",22)
text(.85,7.2,r"Zero weighted Haar moment: every fixed derivative is $O(q^N)$ for every $N$.",17)
panel(3.65,2.75,"3  Weighted equations identify the tangential defects · RM2")
text(.85,5.67,r"$\mathcal{M}_\theta=\mathcal{M}_z=0:\qquad"
     r"\int R^2\langle E_\theta\rangle_y\,dR=\varepsilon\partial_Z\mathcal{J}_\theta$",22)
text(.85,4.9,r"$\int R\langle E_z\rangle_y\,dR"
     r"=\varepsilon\partial_Z(\mathcal{J}_z+c_\rho\mathcal{P})$",23)
text(.85,4.2,r"$c_\rho=\frac{q}{2Q}\int x^2\widehat{\rho}(x)\,dx$"
     "   retains its axial and time dependence.",19)
panel(.7,2.6,"4  Compact stress cancels the means and leaves the bumps · RM3")
text(.85,2.57,r"$(D_r+2/R)H_\theta=-\langle E_\theta\rangle_y"
     r"+\sigma_\theta\varepsilon\partial_Z\mathcal{J}_\theta$",22)
text(.85,1.83,r"$(D_r+1/R)H_z=-\langle E_z\rangle_y"
     r"+\sigma_z\varepsilon\partial_Z(\mathcal{J}_z+c_\rho\mathcal{P})$",22)
text(.85,1.13,"Recompute every covariance, quadratic increment and pressure after an update.",17,orange)
text(.65,.34,"Source: OpenAI, section 8.1–8.4, pages 88–95.  Complete proofs and original viscosity: RP1–RP9; RM1–RM4.",12.5)
for ext in ["svg","png"]:fig.savefig(out/("radial-mean-corrections."+ext),dpi=100)
p=out/"radial-mean-corrections.svg"
p.write_text(re.sub(r'width="1008pt" height="1008pt"','width="1400" height="1400"',
    p.read_text(encoding="utf8")),encoding="utf8")
plt.close(fig)
