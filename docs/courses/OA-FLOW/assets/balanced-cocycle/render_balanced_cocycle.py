"""Exact noncommuting M2 densities: twisted versus ordinary multiplication."""
from pathlib import Path
import json, re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
matplotlib.rcParams["svg.hashsalt"] = "OA-FLOW-balanced-cocycle-v1"

d=Path(__file__).resolve().parent
rotation=np.array([[1,-1],[1,1]],dtype=float)/np.sqrt(2)
dphi=np.diag([1.,4.])/5
dpsi=rotation@dphi@rotation.T
tau=np.pi/(2*np.log(4))
def power(a,t):
    val,vec=np.linalg.eigh(a)
    return (vec*np.exp(1j*t*np.log(val)))@vec.conj().T
def cocycle(t):return power(dpsi,t)@power(dphi,-t)
u=cocycle(tau);target=cocycle(2*tau)
twisted=u@power(dphi,tau)@u@power(dphi,-tau)
ordinary=u@u
exact_target=np.array([[0,-1],[1,0]],dtype=complex)
exact_ordinary=np.array([[-1+1j,-1-1j],[1-1j,-1-1j]])/2
assert np.linalg.norm(target-exact_target)<1e-13
assert np.linalg.norm(ordinary-exact_ordinary)<1e-13
fig,axes=plt.subplots(1,3,figsize=(13.8,6.1))
fig.subplots_adjust(left=.055,right=.96,top=.69,bottom=.28,wspace=.36)
fig.suptitle("The modular twist is visible in a two-dimensional example",fontsize=18,fontweight="bold",y=.98)
fig.text(.5,.90,r"$d_\varphi=\mathrm{diag}(1,4)/5,\quad d_\psi=\frac{1}{2}I-\frac{3}{10}(E_{12}+E_{21}),\quad \tau=\pi/(2\log4)$",
         ha="center",fontsize=14)
fig.text(.5,.82,r"$u_t=d_\psi^{\,it}d_\varphi^{-it},\qquad \sigma_t^\varphi(x)=d_\varphi^{\,it}x d_\varphi^{-it}$",ha="center",fontsize=14)
labels0=[["0","-1"],["1","0"]]
labels2=[[r"\frac{-1+i}{2}",r"\frac{-1-i}{2}"],[r"\frac{1-i}{2}",r"\frac{-1-i}{2}"]]
for ax,m,labels,title in zip(axes,[exact_target,exact_target,exact_ordinary],[labels0,labels0,labels2],
                           [r"$u_{2\tau}$",r"$u_\tau\,\sigma_\tau^\varphi(u_\tau)$",r"$u_\tau u_\tau$"]):
    ax.imshow(np.abs(m),cmap="Blues",vmin=0,vmax=1.7)
    for i in range(2):
        for j in range(2):ax.text(j,i,"$"+labels[i][j]+"$",ha="center",va="center",fontsize=22,color="#132f40")
    ax.set_xticks([-.5,.5,1.5],minor=True);ax.set_yticks([-.5,.5,1.5],minor=True)
    ax.grid(which="minor",color="white",lw=3);ax.tick_params(which="both",bottom=False,left=False,labelbottom=False,labelleft=False)
    ax.set_title(title,fontsize=19,pad=13)
    for sp in ax.spines.values():sp.set_visible(False)
axes[0].text(.5,-.18,"Target at the combined time",transform=axes[0].transAxes,ha="center",fontsize=12)
axes[1].text(.5,-.18,r"Exact error norm: $0$",transform=axes[1].transAxes,ha="center",fontsize=12,color="#176d70")
axes[2].text(.5,-.18,r"Exact error norm: $1$",transform=axes[2].transAxes,ha="center",fontsize=12,color="#aa531c")
fig.text(.5,.135,r"$u_{s+t}=u_s\,\sigma_s^\varphi(u_t)$",ha="center",fontsize=19,fontweight="bold")
fig.text(.5,.052,"BC-4, equation BC20. The entries and error norms are exact; cell shading records entry modulus only.",
         ha="center",fontsize=11)
fig.savefig(d/"assets"/"balanced-cocycle.png",dpi=180,bbox_inches="tight")
svg_path=d/"assets"/"balanced-cocycle.svg"
fig.savefig(svg_path,bbox_inches="tight",metadata={"Date":None})
# Identical embedded images share a backend ID; unused image IDs are omitted.
svg_text=svg_path.read_text(encoding="utf-8")
image_ids=re.findall(r'<image\b[^>]*\bid="([^"]+)"',svg_text)
assert all("#"+ident not in svg_text for ident in image_ids), "Referenced image ID"
svg_text=re.sub(r'(<image\b[^>]*?)\s+id="[^"]+"',r"\1",svg_text)
svg_path.write_text(svg_text,encoding="utf-8")
plt.close(fig)
def serial(m):return [[[float(z.real),float(z.imag)] for z in row] for row in m]
(d/"balanced-cocycle-numerics.json").write_text(json.dumps({
 "density_phi":dphi.tolist(),"density_psi":dpsi.tolist(),"tau":tau,
 "u_tau":serial(u),"u_2tau":serial(target),"twisted":serial(twisted),"ordinary":serial(ordinary),
 "twisted_error_operator_norm":float(np.linalg.norm(twisted-target,2)),
 "ordinary_error_operator_norm":float(np.linalg.norm(ordinary-target,2)),
 "exact_ordinary_error_norm":1,"exact_twisted_error_norm":0,
 "proof":"BALANCED-COCYCLE-FIGURE.md proves the values algebraically; numerical errors only verify the implementation."
},indent=2)+"\n",encoding="utf-8")
