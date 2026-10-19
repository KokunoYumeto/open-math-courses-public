"""Exact covariance and nonlinear maps, SC1–SC11 and NI4–NI7."""
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
text(.65,12.72,"The stress inverse and the actual velocity update",25)
text(.65,12.17,"Both pulse signs, both averages and every remainder remain",16)
panel(8.85,2.8,"1  Positive amplitudes realize the prescribed stress · SC1–SC4")
text(.85,10.95,r"$\mathsf{H}=[\mathcal{C}(b_+)\mid\mathcal{C}(b_-)],\qquad a_\sigma=\sqrt{(\mathsf{H}^{-1}T)_\sigma}$",22)
text(.85,10.25,r"$W_0=\sqrt{\varepsilon}\,(a_+b_++a_-b_-),\qquad\mathcal{C}(W_0)=\varepsilon T$",22)
text(.85,9.5,"The exact columns include the finite-width and moving-frame errors.",17)
panel(6.15,2.35,"2  The signed map inverts the derivative · SC5, SC11")
text(.85,7.8,r"$\delta a_\sigma=\frac{[\mathsf{H}^{-1}(\Sigma/\varepsilon)]_\sigma}{2a_\sigma},\qquad"
     r"\mathcal{B}_{\rm cov}(W_0,\mathcal{L}\Sigma)=\Sigma$",22)
text(.85,7.02,r"$\mathcal{C}(W_0+\mathcal{L}\Sigma)=\varepsilon T+\Sigma+\mathcal{C}(\mathcal{L}\Sigma)$",22)
panel(3.35,2.45,"3  The full curls produce three retained error groups · SC7–SC9")
text(.85,5.08,r"$U=W_0^{\rm as}+E,\qquad V=\mathcal{L}^{\rm as}\Sigma+R$",23)
text(.85,4.36,r"$\mathcal{C}(U+V)-\mathcal{C}(U)=\Sigma"
     r"+\mathcal{B}_{\rm cov}(E,\mathcal{L}^{\rm as}\Sigma)"
     r"+\mathcal{B}_{\rm cov}(U,R)+\mathcal{C}(V)$",19)
panel(.7,2.3,"4  Exact divergence removes the large phase contraction · NI4–NI6")
text(.85,2.3,r"$ikm\,n\cdot a=-\mathfrak{d}a,\qquad"
     r"ikm'(n\cdot a)b=-\frac{m'}{m}(\mathfrak{d}a)b$",23)
text(.85,1.5,"Keep all radial, axial and cylindrical frame terms.",18,orange)
text(.65,.34,"Source: OpenAI, sections 7 and 9.1.  Full proofs, actual shear and viscosity factors: SC1–SC11.",13)
for ext in ["svg","png"]:fig.savefig(out/("stress-and-interactions."+ext),dpi=100)
p=out/"stress-and-interactions.svg"
p.write_text(re.sub(r'width="1008pt" height="936pt"','width="1400" height="1300"',
    p.read_text(encoding="utf8")),encoding="utf8")
plt.close(fig)
