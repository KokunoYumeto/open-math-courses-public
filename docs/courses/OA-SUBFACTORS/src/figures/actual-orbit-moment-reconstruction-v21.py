"""CC0-1.0. Reproducible exact-notation schematic for OM.1--OM.8."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"]="actual-orbit-moment-reconstruction-v21"
from matplotlib.patches import FancyBboxPatch

D = Path(__file__).resolve().parent
fig = plt.figure(figsize=(14, 9), facecolor="white")
ax = fig.add_axes([.035, .035, .93, .93])
ax.set(xlim=(0, 14), ylim=(0, 9))
ax.axis("off")
ax.text(.1, 8.7, "Full original invariant moments from actual normal boundary orbits",
        fontsize=19, weight="bold")
ax.text(.1, 8.27, r"Fixed $\lambda=1+2^{-31}25^{-198153}$; full "
        r"$H$ endpoints $(c,v,m)$ with $m\equiv\sum c\ (\mathrm{mod}\ 2)$",
        fontsize=13)

def box(x,y,w,h,txt,fc="#edf4fb",fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.10",
                 fc=fc,ec="#36516b",lw=1.3))
    ax.text(x+w/2,y+h/2,txt,ha="center",va="center",
            fontsize=fs,linespacing=1.6)
def arrow(x1,y1,x2,y2,label="",dy=0):
    ax.annotate("",(x2,y2),(x1,y1),
                arrowprops={"arrowstyle":"->","color":"#36516b","lw":1.6})
    if label:
        ax.text((x1+x2)/2,(y1+y2)/2+dy,label,ha="center",fontsize=11,
                bbox={"facecolor":"white","edgecolor":"none","pad":2})

box(.25,6.0,4,1.75,
    "Original normal law "+r"$\mu_U$"+"\n"+
    r"$\sigma=\sum_{j=0}^{N}a_j\mu_U\beta_{h_j}$"+"\n"+
    r"$a_j\geq0,\ \sum_j a_j=1$"+"\n"+
    "Full-center orbit density: OM.2–OM.3")
box(5.1,6.0,4,1.75,
    "Actual WM.16 right Følner sets\n"+
    r"$A_LT=|F_L|^{-1}\sum_{g\in F_L}\beta_gT$"+"\n"+
    r"$\Phi_{L,\sigma}=\sigma A_L$"+"\n"+
    "All finite normal summands: "+r"$\mu_U\beta_{h_jg}$")
box(10.0,6.0,3.6,1.75,
    "Potentially singular cluster "+r"$\omega$"+"\n"+
    r"$\|\Phi_{L,\sigma}\beta_s-\Phi_{L,\sigma}\|$"+"\n"+
    r"$\leq 2/(2L+1)$"+"\n"+
    r"$L\to\infty$: actual $H$-invariance")
arrow(4.35,6.86,4.98,6.86)
arrow(9.22,6.86,9.88,6.86)

box(.25,3.55,8.7,1.82,
    "Fix one finite orbit/Følner mixture first (OM.7)\n"+
    r"$p_{2n}^{+}(z)=N_{2n}^{+}(z)\lambda^{m(z)}/d^n$"+"\n"+
    r"$r_{i,n}(z)=N_{2n-1}^{-}(s_i^{-1}z)/N_{2n}^{+}(z)$"+"\n"+
    r"$q_{h,n}(z)=N_{2(n-k)-1}^{-}(hz)/(p_wN_{2n}^{+}(z))$"+"\n"+
    r"$p_w=\lambda^{m(h^{-1})}/(S_+d^k)$; odd prefix endpoint $h^{-1}$",
    fs=12)
box(9.7,3.55,3.9,1.82,
    "Only normal expectations\n"+
    r"$\sum_z p_{2n}^{+}(z)q_{h,n}(z)r_{i,n}(z)$"+"\n"+
    r"$\longrightarrow\mu_U(\beta_hR_i)$"+"\n"+
    "Count depth "+r"$n\to\infty$"+"\n"+
    "with "+r"$L,h,k$"+" fixed",fc="#edf8f0",fs=12)
arrow(9.07,4.42,9.59,4.42)
arrow(7.1,5.85,7.1,5.52,"evaluate summands",dy=0)

box(.25,1.0,8.7,1.70,
    "The complete actual attainable moment body (OM.5)\n"+
    r"$\mathcal{C}_L(T)=\overline{\mathrm{conv}}\{(\mu_U\beta_hA_LT_k)_k:h\in H\}$"+"\n"+
    r"$\mathcal{M}(T)\subset\mathcal{C}_L(T)$ for every $L$"+"\n"+
    r"$\mathrm{dist}_{\mathrm{Haus}}(\mathcal{C}_L(T),\mathcal{M}(T))\to0$"+"\n"+
    r"$T$: all five $R_i$, original inverse costs, full logarithms",
    fs=12)
box(9.7,1.0,3.9,1.70,
    "Original endpoint remains open\n"+
    r"$\max_{\omega\ {\rm inv}}\omega(R_1)$"+"\n"+
    "Zero-cost candidate: "+r"$\lambda/(4+\lambda)$"+"\n"+
    "No singular state passes through\n"+
    "the normal count-depth limit",fc="#fff2d9",fs=12)
arrow(4.6,3.43,4.6,2.83,"then take the Følner limit",dy=0)
ax.text(.25,.43,
    "Schematic boxes encode no trace masses. Both original phase laws and full "
    "endpoint blocks are retained; finite posteriors can differ for central endpoints.",
    fontsize=10.5)
for extension in ["svg","png"]:
    fig.savefig(D/f"actual-orbit-moment-reconstruction-v21.{extension}",dpi=160,metadata={"Date":None} if extension=="svg" else None)
print("Rendered reproducible SVG and PNG.")

svg_path=D/'actual-orbit-moment-reconstruction-v21.svg'
svg_path.write_text("\n".join(x.rstrip() for x in svg_path.read_text(encoding="utf-8").splitlines()).rstrip()+"\n",encoding="utf-8")
