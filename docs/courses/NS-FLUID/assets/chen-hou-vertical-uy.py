"""Original partner geometry, complete interval cover and physical receiving map."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import hashlib,json,sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Rectangle

P=Path(__file__).resolve()
R=P.parent.parent
sys.path.insert(0,str(R))
from replay_chen_hou_vertical_uy_rational import box
S=R/"state"
cert=json.loads((S/"CHEN_HOU_VERTICAL_UY_RATIONAL_96.json").read_text(encoding="utf-8"))
sample=json.loads((S/"CHEN_HOU_VERTICAL_UY_DIAGNOSTIC.json").read_text(encoding="utf-8"))
fig,axs=plt.subplots(2,2,figsize=(14,11),layout="constrained")
fig.suptitle("The complete vertical uᵧ bound for every physical midpoint\n"
             "Original Chen–Hou costs · comparison and receiving proof VU1–VU21",fontsize=16)
a=1.3;s=2.4;t=.25
T=np.sqrt((a*a+t*t)*(s*s-a*a+3*t*t)/(s*s-a*a-t*t))
def eq(U):
    return t*U*(U*U+t*U+t*t+2*s*s+2*a*a)-(s*s-a*a)**2
low=t;high=1.
while eq(high)<0:high*=2
for _ in range(80):
    middle=(low+high)/2
    if eq(middle)<0:low=middle
    else:high=middle
U=(low+high)/2
ax=axs[0,0];ss=np.linspace(a,4.2,500)
sig=(ss*ss-a*a)/np.sqrt(ss*ss+a*a+2*np.sqrt(ss**4-a*a*ss*ss+a**4))
ax.fill_between(ss,0,sig,color="#e6bc9d",alpha=.6,label="Negative kernel difference")
ax.fill_between(ss,sig,4.5,color="#a9cbd2",alpha=.45,label="Positive kernel difference")
ax.plot(ss,sig,color="#415f6b",lw=1.5,label="Exact sign threshold")
ax.scatter([s,T,s],[t,t,U],color=["#132b43","#a63d36","#187888"],zorder=5)
ax.annotate("",(T,t),(s,t),arrowprops=dict(arrowstyle="->",color="#a63d36",lw=2))
ax.annotate("",(s,U),(s,t),arrowprops=dict(arrowstyle="->",color="#187888",lw=2))
ax.annotate("(s, t)",(s,t),xytext=(12,10),textcoords="offset points",fontsize=10)
ax.annotate("(T, t)",(T,t),xytext=(-10,13),textcoords="offset points",fontsize=10,color="#a63d36")
ax.annotate("(s, U)",(s,U),xytext=(12,0),textcoords="offset points",fontsize=10,color="#187888")
ax.text(.03,.95,"a = 13/10, s = 12/5, t = 1/4\n"
        "Both partners use the full original kernel.\n"
        "Arrow endpoints are numerical illustrations.",transform=ax.transAxes,va="top",fontsize=10)
ax.set(xlim=(1.15,4.2),ylim=(0,4.5),xlabel="Original displacement s",
       ylabel="Original height t",title="Horizontal and vertical mass partners · VU2–VU4")
ax.legend(loc="lower right",fontsize=8)

ax=axs[0,1];patches=[];values=[]
for leaf in cert["leaves"]:
    al,ah,zl,zh=map(float,box(leaf["address"]))
    patches.append(Rectangle((al,zl),ah-al,zh-zl))
    values.append(float(Fraction(leaf["upper"])))
pc=PatchCollection(patches,cmap="viridis",edgecolor="#cad6d7",linewidth=.16)
pc.set_array(np.array(values));pc.set_clim(0,1);ax.add_collection(pc)
fig.colorbar(pc,ax=ax,label="Rational upper enclosure of H on each cell",shrink=.85)
ax.set(xlim=(0,1),ylim=(0,1),xlabel="α = (s − a)/(s + a)",ylabel="z = t/[(s − a)β]",
       title="All 712 closed cells checked · VU9–VU13, VU21")
ax.text(.03,.97,"Every cell upper bound < 99/100\nNo edge or corner omitted",
        transform=ax.transAxes,va="top",fontsize=10,
        bbox=dict(facecolor="white",alpha=.9,edgecolor="none"))

ax=axs[1,0]
xs=np.array([r["M"]-1 for r in sample["rows"]])
ys=np.array([r["coefficient"] for r in sample["rows"]])
ax.semilogx(xs,ys,"o-",color="#26788b",markersize=4,label="Numerical samples, for illustration")
ax.axhline(2.59,color="#a43f3c",lw=1.5,label="Proved uniform upper bound 2.590")
ax.axhline(float(Fraction(5850945274287295,2251799813685248)),
           color="#626c75",ls="--",lw=1.3,label="Original saved lower endpoint")
ax.set(xlabel="Original midpoint distance M − a, at a = 1",
       ylabel="Full physical coefficient, τ = 291/500",
       title="Every midpoint is bounded · VU15–VU19",ylim=(1.52,2.72))
ax.grid(alpha=.2)
ax.legend(fontsize=9,loc="lower left")

ax=axs[1,1];ax.axis("off");ax.set_title("Complete receiving argument · VU14–VU20",pad=12)
rows=[
    (r"$\frac{2}{3}\,\partial_M C_{\rm mid}(a,M)\leq E_a(M)"
     r"=-\partial_M C_{\rm vert}(a,M)$","Both complete transport distances are compared."),
    (r"$C_{\rm mid}(a,M)\longrightarrow\frac{\pi}{2}\sqrt{2a}"
     r"\quad(M\downarrow a)$","The singular residual mass is retained."),
    (r"$C_{\rm vert}(a,M)+\tau C_{\rm mid}(a,M)"
     r"\leq C_{\rm vert}(a,a)+\frac{\pi\tau}{2}\sqrt{2a}$",
     "Proved for all a > 0, M > a and 0 ≤ τ ≤ 2/3."),
    (r"$\frac{|\mathscr{D}_u|}{\sqrt{2a}}\leq"
     r"\left(\frac{C_{\rm vert}(a,a)+\tau C_{\rm in}(a)}"
     r"{\pi\sqrt{2a}}+\frac{\tau}{2}\right)N_\tau$",
     "At τ = 291/500 the coefficient is below 2.590."),
]
for yy,(formula,caption) in zip([.92,.69,.46,.21],rows):
    ax.text(.02,yy,formula,transform=ax.transAxes,fontsize=12,va="top")
    ax.text(.02,yy-.10,caption,transform=ax.transAxes,fontsize=10,va="top",color="#42586b")
fig.supxlabel("Human sources: Jiajie Chen and Thomas Y. Hou, Parts I v4 and II v3; "
              "complete source and proof links in the accompanying note.\n"
              "Saved vertical uᵧ and vₓ scalars are certified. The full stability theorem remains under audit.",
              fontsize=10)
for ext in ["png","svg"]:
    fig.savefig(P.with_suffix("."+ext),dpi=165)
plt.close(fig)
meta=dict(at=datetime.now(timezone.utc).isoformat(),source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),
          proof="CHEN_HOU_VERTICAL_UY_WORK_20261012.md",locators="VU1–VU21",
          physical_geometry={"a":"13/10","s":"12/5","t":"1/4"},
          sample_partner_T=float(T),sample_partner_U=float(U),
          certifying_partition_sha256=hashlib.sha256((S/"CHEN_HOU_VERTICAL_UY_RATIONAL_96.json").read_bytes()).hexdigest(),
          source_attribution="Jiajie Chen and Thomas Y. Hou, original Part II v3 vertical transport and cost formulas; complete physical proofs in included RV, KX and VN notes.",
          scope="Original physical partners, full certified partition, numerical illustration and exact receiving formulas",
          visual_inspection="pending")
P.with_suffix(".json").write_text(json.dumps(meta,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(dict(figure=str(P.with_suffix(".png")))))
