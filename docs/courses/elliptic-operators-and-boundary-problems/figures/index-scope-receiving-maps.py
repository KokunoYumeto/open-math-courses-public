"""Render the exact matrix, character and compressed-parametrix maps."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,8.5));ax.set(xlim=(0,13),ylim=(0,8.5));ax.axis("off")
ax.text(6.5,8.16,"Exact receiving maps for the index and its scope",ha="center",fontsize=17,weight="bold")
def box(y,title,lines,color):
    ax.add_patch(FancyBboxPatch((.4,y),12.2,1.75,boxstyle="round,pad=.12",fc=color,ec="#547489",lw=1.3))
    ax.text(6.5,y+1.47,title,ha="center",fontsize=12,weight="bold",color="#183d53")
    for i,(line,size) in enumerate(lines):ax.text(6.5,y+1.02-.36*i,line,ha="center",va="center",fontsize=size)
box(5.76,"Original bundle symbol → global invertible matrix → characteristic class",[
 (r"$g:\pi^*E\to\pi^*E,\quad e=ii^*,\quad G=igi^*+(I-e),\quad G^{-1}=ig^{-1}i^*+(I-e)$",13),
 ("ISS1–ISS2b: both inverse orders, actual conjugating rotation and full odd-character transgression.",11),
 ("The identity on the original orthogonal complement leaves kernel and cokernel unchanged.",11)],"#edf4f9")
box(3.5,"De Rham equivariant analytic index → character → actual fixed-point signs",[
 (r"$\operatorname{ind}_G\bar A_{\rm ev}=V_{\rm dR}=\sum_j(-1)^j[K_j,\rho_j],\quad \rho_j(g)\leftrightarrow\phi_{g^{-1}}^*$",13),
 (r"$\operatorname{ev}_{g^{-1}}(V_{\rm dR})=L(\phi_g)=\sum_{\phi_g(x)=x}\operatorname{sgn}\det(I-d\phi_{g,x})$",13),
 ("ISR1–ISR5: the group inverse remains. The sign formula requires nondegenerate fixed points.",11)],"#eff6ed")
box(1.24,"Original compression → both ordered compact errors → Fredholm operator",[
 (r"$T_U=\Pi U\Pi,\quad S=\Pi U^{-1}\Pi,\quad [\Pi,U^{-1}]=-U^{-1}[\Pi,U]U^{-1}$",13),
 (r"$ST_U-\Pi=\Pi U^{-1}[\Pi,U]\Pi,\quad T_US-\Pi=\Pi U[\Pi,U^{-1}]\Pi$",13),
 ("IST1–IST2: bounded invertible U with compact commutator; every unitary case is retained.",11)],"#faf2e9")
ax.text(6.5,.64,"Complete receiving proofs: Characteristic classes, Bott normalization, fixed points, and external index theories.",ha="center",fontsize=10)
ax.text(6.5,.28,"External characteristic source: Denis Perrot, Pseudodifferential extension and Todd class, arXiv:1112.1850v1.",ha="center",fontsize=9)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ["svg","png"]:fig.savefig(out/f"index-scope-receiving-maps.{ext}",dpi=180,facecolor="white")
plt.close(fig)
