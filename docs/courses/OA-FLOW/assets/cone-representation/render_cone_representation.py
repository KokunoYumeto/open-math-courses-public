"""Cone order inverse and finite Dirichlet averages, CR5 and CR7.
CC0-1.0 to the extent of rights held. Run with Python, NumPy and Matplotlib.
All scalar samples illustrate the formulas; the lesson supplies their proofs.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "svg.hashsalt": "oa-flow-cone-order-dirichlet-v1",
    "axes.spines.top": False, "axes.spines.right": False,
})
out = Path(__file__).resolve().parent
navy, teal, orange, pale = "#17324d", "#087f8c", "#c26722", "#eaf3f5"
fig = plt.figure(figsize=(13, 10), facecolor="white")
grid = fig.add_gridspec(3, 1, height_ratios=[1.2, 1.4, 2.1], hspace=0.46)
ax = fig.add_subplot(grid[0])
ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis("off")
ax.text(0, 1.04, "A. The order inverse is a bounded positive form", color=navy,
        fontsize=15, weight="bold", transform=ax.transAxes)
boxes = [
    (0.115, r"$0\leq_P\eta\leq_P\Omega$"+"\n"+r"$F_\eta(y')=\langle D^{-1/4}y'\Omega,\eta\rangle$"),
    (0.455, r"$0\leq F_\eta\leq\omega_\Omega$"+"\n"+r"$\langle cy'\Omega,z'\Omega\rangle=F_\eta(z'^*y')$"),
    (0.815, r"$c\in M,\quad 0\leq c\leq1$"+"\n"+r"$D^{-1/4}\eta=c\Omega$"),
]
for x, label in boxes:
    ax.text(x, .59, label, ha="center", va="center",
            bbox={"boxstyle":"round,pad=.7", "fc":pale, "ec":teal})
for a, b in [(.26, .29), (.63, .66)]:
    ax.annotate("", xy=(b,.59), xytext=(a,.59),
                arrowprops={"arrowstyle":"->", "color":navy, "lw":1.8})
ax.text(.5, .07, r"Right Tomita graph core tests the full adjoint domain:  $\eta=D^{1/4}c\Omega$.",
        ha="center", color=navy)
ax = fig.add_subplot(grid[1])
ax.set(xlim=(-3.6,3.6), ylim=(-.6,1.05)); ax.axis("off")
ax.text(0, 1.1, "B. Positive averages solve a finite boundary problem", color=navy,
        fontsize=15, weight="bold", transform=ax.transAxes)
for j in range(-3,3):
    ax.annotate("", xy=(j+.82,.5), xytext=(j+.18,.5),
                arrowprops={"arrowstyle":"<->", "color":teal, "lw":1.8})
for j in range(-3,4):
    ax.scatter([j],[.5],s=440,color=orange if abs(j)==3 else teal,zorder=3)
    ax.text(j,.5,r"$\theta$" if abs(j)==3 else r"$u_{%s}$"%j,
            ha="center",va="center",color="white",fontsize=12)
    ax.text(j,.12, "j = "+str(j),ha="center",fontsize=10)
ax.text(0,.89,r"$n=3,\quad\varepsilon=1/12,\quad R_\varepsilon=(2+\varepsilon^2 L^2)^{-1}$",
        ha="center",color=navy)
ax.text(0,-.19,r"$u_j=R_\varepsilon(u_{j-1}+u_{j+1}),\qquad 0\leq_P u_j\leq_P\Omega$",
        ha="center",color=navy)
ax.text(0,-.51,r"Fixed endpoints $\theta$; zero initial interior.  Path bound: $\|T^6\|\leq63/64$.",
        ha="center",fontsize=10,color=navy)
ax = fig.add_subplot(grid[2])
x=np.linspace(0,12,601)
filters={str(n):1/np.cosh(2*n*np.arcsinh(x/(8*n))) for n in (1,3,8)}
target=1/np.cosh(x/4)
for n,color,style in [(1,orange,"--"),(3,teal,"-."),(8,"#8f6593",":")]:
    ax.plot(x,filters[str(n)],color=color,ls=style,lw=2.3,label=r"$f_{%s}$"%n)
ax.plot(x,target,color=navy,lw=1.7,label=r"$f(\lambda)=\mathrm{sech}(\lambda/4)$")
ax.set(xlim=(0,12),ylim=(0,1.04),xlabel=r"Spectral value $\lambda\geq0$ (all filters are even)",
       ylabel="Scalar multiplier")
ax.set_title("C. Central filters converge to the cone-preserving multiplier",loc="left",
             color=navy,fontsize=15,weight="bold",pad=16)
ax.grid(alpha=.2)
ax.legend(loc="upper right",frameon=False)
ax.text(.5,-.28,r"$u_0=f_n(L)\theta,\qquad f_n(\lambda)=\mathrm{sech}\!\left(2n\,\mathrm{arsinh}(|\lambda|/(8n))\right)$",
        transform=ax.transAxes,ha="center",color=navy)
fig.subplots_adjust(left=.09,right=.97,top=.94,bottom=.11)
fig.text(.09,-.012,"Exact constructions: CR5 and CR7. Curves are numerical samples; the strong spectral limit is proved in the lesson.",
         fontsize=10,color=navy)
fig.savefig(out/"cone-order-dirichlet.png",dpi=180,bbox_inches="tight")
fig.savefig(out/"cone-order-dirichlet.svg",bbox_inches="tight",metadata={"Date":None})
plt.close(fig)

# Independent scalar checks of the boundary recurrence and contraction count.
checks=[]
for n in (1,3,8):
    eps=1/(4*n)
    residual=0.0
    for lam in (0.,.5,2.,7.,12.):
        a=2*np.arcsinh(abs(lam)/(8*n))
        values=np.cosh(np.arange(-n,n+1)*a)/np.cosh(n*a)
        r=1/(2+eps**2*lam**2)
        residual=max(residual,float(np.max(np.abs(values[1:-1]-r*(values[:-2]+values[2:])))))
    assert residual<2e-14
    # Count paths which remain strictly between the fixed endpoints.
    mat=np.zeros((2*n-1,2*n-1),dtype=np.int64)
    for i in range(2*n-2):mat[i,i+1]=mat[i+1,i]=1
    paths=int(np.linalg.matrix_power(mat,2*n).sum(axis=1).max())
    assert paths<=2**(2*n)-1
    checks.append({"n":n,"epsilon":eps,"maximum_scalar_recurrence_residual":residual,
                   "maximum_surviving_paths_length_2n":paths,
                   "path_bound":2**(2*n)-1,
                   "maximum_sampled_filter_error":float(np.max(np.abs(filters[str(n)]-target)))})
samples=[{"lambda":float(x[k]),"limit":float(target[k]),
          "f_n":{n:float(v[k]) for n,v in filters.items()}} for k in (0,25,100,350,600)]
(out/"cone-order-numerics.json").write_text(json.dumps({
    "proof_locators":["OA-FLOW.CR.5","OA-FLOW.CR.7"],
    "licence":"CC0-1.0 to the extent of rights held",
    "interpretation":"Finite scalar checks and plotted samples; not a proof of the operator limit.",
    "filters":"f_n(lambda)=sech(2*n*asinh(abs(lambda)/(8*n)))",
    "limit":"sech(lambda/4)",
    "checks":checks,"samples":samples,
},indent=2)+"\n",encoding="utf-8")
