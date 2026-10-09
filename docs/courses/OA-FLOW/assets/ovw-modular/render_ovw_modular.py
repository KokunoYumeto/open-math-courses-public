"""Exact tensor cocycle, unbounded OVW cutoff, and analytic zero obstruction."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-ovw-modular-20261009-v1"

d=Path(__file__).resolve().parent
phi=np.diag([1.,4.])/5
rotation=np.array([[1.,-1.],[1.,1.]])/np.sqrt(2)
psi=rotation@phi@rotation.T
r=np.diag([1.,3.])
tstar=np.pi/np.log(4)
def ipower(a,t):
    val,vec=np.linalg.eigh(a)
    return (vec*np.exp(1j*t*np.log(val)))@vec.conj().T
u=ipower(psi,tstar)@ipower(phi,-tstar)
up=ipower(np.kron(psi,r),tstar)@ipower(np.kron(phi,r),-tstar)
exact=np.array([[0.,-1.],[1.,0.]])
assert np.linalg.norm(u-exact,2)<1e-13
assert np.linalg.norm(up-np.kron(exact,np.eye(2)),2)<1e-13
k=np.arange(15)
tails=2*(k+2)*2.**(-k)
ns=np.arange(1,61)
products=np.cumprod((2.*ns-1)/(2.*ns+1))
assert np.max(abs(products-1/(2.*ns+1)))<1e-14

fig,axs=plt.subplots(2,2,figsize=(14,11))
fig.subplots_adjust(left=.075,right=.96,top=.87,bottom=.20,wspace=.36,hspace=.72)
fig.suptitle("Transport preserves the modular action and the relative cocycle",fontsize=17,fontweight="bold",y=.975)
fig.text(.5,.923,"Exact finite matrices, an unbounded operator-valued value, and the analytic uniqueness mechanism",
         ha="center",fontsize=11)

ax=axs[0,0];ax.axis("off")
ax.set_title("A. A common positive tensor density",loc="left",fontsize=13,pad=17)
ax.text(.5,.89,r"$N=M_2\otimes I\ \subset\ M=M_2\otimes M_2$",ha="center",fontsize=15)
ax.text(.5,.68,r"$T(x\otimes y)=x\,\mathrm{Tr}(ry),\quad r=\mathrm{diag}(1,3)$",ha="center",fontsize=13)
ax.text(.23,.43,r"$d_\varphi,\ d_\psi$",ha="center",fontsize=17)
ax.text(.77,.43,r"$d_\varphi\otimes r,\ d_\psi\otimes r$",ha="center",fontsize=17)
ax.annotate("",xy=(.59,.47),xytext=(.38,.47),arrowprops=dict(arrowstyle="->",lw=1.8,color="#466471"))
ax.text(.49,.55,r"$\varphi T,\ \psi T$",ha="center",fontsize=12)
ax.text(.5,.20,r"$\sigma_t^{\varphi T}(x\otimes I)=\sigma_t^\varphi(x)\otimes I$",ha="center",fontsize=15,color="#177777")
ax.text(.5,-.02,r"$(D\psi T:D\varphi T)_t=(D\psi:D\varphi)_t\otimes I$",ha="center",fontsize=14,color="#177777")
ax.text(.5,-.22,r"$d_\varphi=\mathrm{diag}(1,4)/5,\quad d_\psi=R d_\varphi R^*$",ha="center",fontsize=11)
ax.text(.5,-.34,"R is the real rotation through π/4.  T(I) = 4I.",ha="center",fontsize=10)

ax=axs[0,1];m=np.kron(exact,np.eye(2))
ax.imshow(abs(m),cmap="Blues",vmin=0,vmax=1.6)
for i in range(4):
    for j in range(4):ax.text(j,i,str(int(m[i,j])),ha="center",va="center",fontsize=18,color="#173647")
ax.set_xticks(np.arange(-.5,4,1),minor=True);ax.set_yticks(np.arange(-.5,4,1),minor=True)
ax.grid(which="minor",color="white",lw=2)
ax.tick_params(which="both",bottom=False,left=False,labelbottom=False,labelleft=False)
for sp in ax.spines.values():sp.set_visible(False)
ax.set_title(r"B. Exact cocycle at $t_*=\pi/\log4$",fontsize=13,pad=17)
ax.text(.5,-.18,r"$u_{t_*}=E_{21}-E_{12},\qquad \widetilde u_{t_*}=u_{t_*}\otimes I$",
        transform=ax.transAxes,ha="center",fontsize=12)
ax.text(.5,-.33,r"The common factor cancels: $r^{it}r^{-it}=I$.",
        transform=ax.transAxes,ha="center",fontsize=11)

ax=axs[1,0]
ax.semilogy(k,tails,"o-",color="#177777",lw=2,ms=4)
ax.set_title("C. Full finite domain beyond bounded T-values",loc="left",fontsize=13,pad=18)
ax.set_xlabel(r"Cutoff index $k$ in $e_{2k}=1_{\{n\leq k\}}$")
ax.set_ylabel("Squared GNS error (log scale)")
ax.set_xticks(np.arange(0,15,2));ax.grid(alpha=.2,which="both")
ax.text(.5,.94,r"$2(k+2)2^{-k}$",transform=ax.transAxes,ha="center",va="top",fontsize=17)
ax.text(.5,-.29,r"$T(I)_n=2n,\quad \widetilde\varphi(I)=4,\quad I\notin N_T$",
        transform=ax.transAxes,ha="center",fontsize=12)
ax.text(.5,-.45,"OT4: spectral cutoffs converge in the scalar GNS norm.",
        transform=ax.transAxes,ha="center",fontsize=10)

ax=axs[1,1]
ax.semilogy(ns,products,color="#a6612c",lw=2)
ax.scatter([1,5,15,30,60],1/(2*np.array([1,5,15,30,60])+1),s=22,color="#a6612c")
ax.set_title("D. Imaginary integer zeros force equality",loc="left",fontsize=13,pad=18)
ax.set_xlabel(r"Number of zeros $N$")
ax.set_ylabel("Upper bound (log scale)")
ax.grid(alpha=.2,which="both")
ax.text(.52,.94,r"$|H(0)|/\|g\|_\infty\leq 1/(2N+1)$",transform=ax.transAxes,ha="center",va="top",fontsize=13)
ax.text(.5,-.29,r"$a_n=(2n-1)/(2n+1),\quad \prod_{n=1}^{N}a_n=1/(2N+1)$",
        transform=ax.transAxes,ha="center",fontsize=12)
ax.text(.5,-.45,"AS1: finite Blaschke products, with center z = i/2.",
        transform=ax.transAxes,ha="center",fontsize=10)
fig.text(.5,.022,"Full example proofs: OVW-MODULAR-FIGURE.md, equations OF1–OF6.  General proof: OT1–OT5 and AS1–AS4.",
         ha="center",fontsize=10)
fig.savefig(d/"assets"/"ovw-modular.png",dpi=180,bbox_inches="tight")
fig.savefig(d/"assets"/"ovw-modular.svg",bbox_inches="tight",metadata={"Date": None})
plt.close(fig)

def serial(a):return [[[float(z.real),float(z.imag)] for z in row] for row in a]
(d/"ovw-modular-numerics.json").write_text(json.dumps({
    "phi_density":phi.tolist(),"psi_density":psi.tolist(),"common_density":r.tolist(),"tstar":tstar,
    "base_cocycle":serial(u),"upstairs_cocycle":serial(up),"exact_base_cocycle":exact.tolist(),
    "base_matrix_error_operator_norm":float(np.linalg.norm(u-exact,2)),
    "tensor_cocycle_error_operator_norm":float(np.linalg.norm(up-np.kron(exact,np.eye(2)),2)),
    "cutoff_indices":k.tolist(),"squared_gns_tails":tails.tolist(),"exact_tail_formula":"2*(k+2)*2^(-k)",
    "zero_counts":ns.tolist(),"finite_products":products.tolist(),"exact_product":"1/(2*N+1)",
    "product_error":float(np.max(abs(products-1/(2.*ns+1)))),
    "proof":"OVW-MODULAR-FIGURE.md OF1–OF6; the numerical checks validate the renderer and do not establish the theorems."
},indent=2)+"\n",encoding="utf-8")
