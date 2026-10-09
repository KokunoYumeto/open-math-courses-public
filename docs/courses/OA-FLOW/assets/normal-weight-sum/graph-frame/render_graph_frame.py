from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-normal-weight-sum-graph-frame-20261009-v1"

d=Path(__file__).resolve().parent
(d/"assets").mkdir(exist_ok=True)
s=np.linspace(0,6,401)
gamma=np.exp(-s*s/4)
b=gamma*np.exp(-s/2);c=gamma*np.exp(s/2)
raw=np.cosh(s/2)
smooth=(np.sqrt(4+(b-c)**2)+b+c)/4
numerical=np.array([np.linalg.norm(np.array([[1,bb],[cc,1]])/2,2) for bb,cc in zip(b,c)])
assert np.max(abs(smooth-numerical))<1e-13
assert np.max(smooth)<=np.exp(.25)+1e-13
fig,(ax,diagram)=plt.subplots(1,2,figsize=(14,8))
fig.subplots_adjust(left=.075,right=.97,top=.78,bottom=.32,wspace=.3)
fig.suptitle("One Gaussian supplies the missing right graph bound",fontsize=18,fontweight="bold",y=.97)
fig.text(.5,.87,r"$\Gamma(x)=\pi^{-1/2}\int e^{-t^2}\sigma_t(x)\,dt,\qquad \|\sigma_{-i/2}(\Gamma(x))\|\leq e^{1/4}\|x\|$",
         ha="center",fontsize=14)
ax.semilogy(s,raw,color="#a45d30",lw=2.3,label="Before smoothing: cosh(s/2)")
ax.semilogy(s,smooth,color="#1a7b77",lw=2.3,label="After smoothing: exact norm")
ax.axhline(np.exp(.25),color="#334b62",ls="--",lw=1.6,label="Universal bound exp(1/4)")
ax.set_xlabel(r"$s=\log(\mathrm{density\ eigenvalue\ ratio})$")
ax.set_ylabel("Half-shift operator norm (log scale)")
ax.set_xlim(0,6);ax.grid(alpha=.18,which="both");ax.legend(fontsize=10,loc="upper left")
ax.set_title("Exact noncommuting M₂ example",fontsize=13,pad=14)
ax.text(.5,-.27,r"$d_s=\mathrm{diag}(1,e^s),\quad P_+=(I+E_{12}+E_{21})/2$",
        transform=ax.transAxes,ha="center",fontsize=11)
ax.text(.5,-.4,r"$\Gamma(P_+)=(I+e^{-s^2/4}(E_{12}+E_{21}))/2$",
        transform=ax.transAxes,ha="center",fontsize=11)
diagram.axis("off");diagram.set_title("The complete arbitrary-weight construction",fontsize=13,pad=14)
rows=[
 (r"$p_jp_k=0\ (j\ne k),\quad \sum_jp_j=1$","Modular-fixed projection blocks: GF2"),
 (r"$u_{j,n}\uparrow p_j,\quad d_{j,n}=u_{j,n}-u_{j,n-1}\geq0$","Each increment has finite opposite weight"),
 (r"$a_{j,n}=\Gamma(d_{j,n})^{1/2}$","The same Gaussian for every block and increment"),
 (r"$s_F=\sum_F a_{j,n}^*a_{j,n}\leq1,\quad s_F\longrightarrow1$","Positive partial sums converge strongly"),
 (r"$\|\theta(b s_F)\|\leq e^{1/4}\|\theta(b)\|$","Uniform right bound gives the weak graph limit")
]
for j,(formula,label) in enumerate(rows):
    y=.97-j*.235
    diagram.text(.5,y,formula,ha="center",va="top",fontsize=13,color="#154450",
                 bbox=dict(boxstyle="round,pad=.45",fc="#eff7f6",ec="#b6d2cf"))
    diagram.text(.5,y-.14,label,ha="center",va="top",fontsize=9.6)
    if j<4:diagram.annotate("",xy=(.5,y-.225),xytext=(.5,y-.19),
                            arrowprops=dict(arrowstyle="->",color="#607783",lw=1.4))
fig.text(.5,.04,"Exact example proof: GRAPH-FRAME-FIGURE.md.  Full theorem mechanism: GRAPH_FRAME_RECONSTRUCTION.md, GF1–GF4.",
         ha="center",fontsize=10)
fig.savefig(d/"assets"/"gaussian-graph-frame.png",dpi=180,bbox_inches="tight")
fig.savefig(d/"assets"/"gaussian-graph-frame.svg",bbox_inches="tight",metadata={"Date": None})
plt.close(fig)
(d/"graph-frame-numerics.json").write_text(json.dumps({
    "s":s.tolist(),"raw_norm":raw.tolist(),"smoothed_norm":smooth.tolist(),
    "universal_bound":float(np.exp(.25)),
    "closed_formula_vs_svd_max_error":float(np.max(abs(smooth-numerical))),
    "exact_formula":"(sqrt(4+(b-c)^2)+b+c)/4, b=exp(-s^2/4-s/2), c=exp(-s^2/4+s/2)",
    "proof":"GRAPH-FRAME-FIGURE.md; numerical checks validate the renderer only"
},indent=2)+"\n")
