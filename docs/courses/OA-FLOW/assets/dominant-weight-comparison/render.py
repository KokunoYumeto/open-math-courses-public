"""Original exact dominant-weight models; no external figure assets."""
from pathlib import Path
import json
import shutil
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "data.json").read_text(encoding="utf-8"))
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                    "mathtext.fontset":"dejavusans","svg.fonttype":"none"})
INK, MUTED = "#153046", "#4b6475"
BLUE, TEAL, ORANGE = "#216fa5", "#008578", "#c66629"
BG = "#f3f7fa"
fig = plt.figure(figsize=(18,14), facecolor=BG)
fig.text(.045,.958,DATA["title"],fontsize=24,weight="bold",color=INK)
fig.text(.045,.926,
    "Whole-cone normalization, noncommuting factors, and exact cancellation by an infinite row",
    fontsize=14,color=MUTED)

def panel(rect,title):
    ax=fig.add_axes(rect);ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
    ax.add_patch(FancyBboxPatch((0,0),1,1,
        boxstyle="round,pad=.006,rounding_size=.02",
        transform=ax.transAxes,facecolor="white",edgecolor="#cbd9e2",
        linewidth=1.2,clip_on=False))
    ax.text(.035,.949,title,fontsize=17,weight="bold",color=INK,va="top")
    return ax

def txt(ax,x,y,s,size=13,color=INK,**kw):
    return ax.text(x,y,s,fontsize=size,color=color,**kw)

def matrix(ax,x,y,entries,label,color=BLUE,scale=1):
    """Exact entries in a bracketed 2 by 2 matrix, in panel coordinates."""
    dx,dy=.060*scale,.080*scale
    for i,row in enumerate(entries):
        for j,val in enumerate(row):
            txt(ax,x+(j-.5)*dx,y+(.5-i)*dy,"$"+val+"$",
                size=16*scale,ha="center",va="center",color=color)
    lx,rx=x-.078*scale,x+.078*scale
    lo,hi=y-.09*scale,y+.09*scale
    for xx,sign in [(lx,1),(rx,-1)]:
        ax.plot([xx+.012*scale*sign,xx,xx,xx+.012*scale*sign],
                [hi,hi,lo,lo],color=color,lw=1.4)
    txt(ax,x,y+.126*scale,label,size=13*scale,ha="center",color=color)

a=panel([.045,.515,.438,.378],"A  |  Translation rescales the full weight")
txt(a,.045,.831,r"$D=1_K\otimes e^Q,\qquad X(r)=1_K\otimes L_r,\quad L_rf(q)=f(q-r)$",12.8)
p=a.inset_axes([.13,.32,.80,.43])
lo,hi=DATA["density"]["coordinate_window"]
q=np.linspace(lo,hi,DATA["density"]["curve_samples"])
p.plot(q,np.exp(q),color=BLUE,lw=2.3,label=r"$e^q$")
p.plot(q,2*np.exp(q),color=ORANGE,lw=2.3,label=r"$2e^q$")
p.axvspan(0,1,color=TEAL,alpha=.065)
p.set(xlim=(lo,hi),ylim=(0,8.7),xlabel=r"$q$",ylabel="density")
p.legend(frameon=False,fontsize=11,loc="upper left")
p.grid(alpha=.16);p.spines[["right","top"]].set_visible(False)
p.tick_params(labelsize=10.5)
txt(a,.045,.19,r"$D^{it}X(r)D^{-it}=e^{irt}X(r)$",14,color=BLUE)
txt(a,.045,.112,r"$\chi\circ\mathrm{Ad}\,X(\log2)=2\chi\quad\mathrm{on}\ B_+$",14,color=ORANGE)
txt(a,.045,.037,r"Rank-one test on $[0,1]$: $e-1\longmapsto2(e-1)$.",11.7,color=MUTED)

b=panel([.517,.515,.438,.378],"B  |  Absorption has an exact factor order")
txt(b,.045,.831,r"$t_0=\pi/(2\log2),\quad r=t_0/2,\quad c_t=k^{it}h^{-it}$",13.3)
txt(b,.17,.69,r"$\frac{1}{\sqrt{2}}$",16,color=BLUE,ha="center")
matrix(b,.31,.66,DATA["matrix"]["A_numerator"],r"$A=c_r$")
txt(b,.61,.69,r"$\frac{1}{\sqrt{2}}$",16,color=TEAL,ha="center")
matrix(b,.77,.66,DATA["matrix"]["B_numerator"],r"$B_0=a_{t_0}(c_{r-t_0}^*)$",TEAL)
matrix(b,.28,.35,DATA["matrix"]["A_times_B"],r"$AB_0=Y=c_{t_0}$",BLUE)
matrix(b,.76,.35,DATA["matrix"]["B_times_A"],r"$B_0A=-Z\ne c_{t_0}$",ORANGE)
txt(b,.5,.156,r"$c_{t_0}^2=I,\qquad c_{2t_0}=-I,\qquad c_{t_0}a_{t_0}(c_{t_0})=-I$",
    13.5,ha="center")
txt(b,.045,.054,"All entries are exact. The cocycle phase includes "+r"$2^{it}$"+".",
    11.7,color=MUTED)

c=panel([.045,.095,.438,.378],"C  |  A centralizer row fills one corner")
txt(c,.045,.832,r"$s_n(e_j\otimes\eta)=e_{\nu(n,j)}\otimes\eta,\quad"
    r"\nu(n,j)=\frac{(n+j)(n+j+1)}{2}+n$",12.8)
grid=c.inset_axes([.17,.36,.67,.36]);grid.axis("off")
tbl=grid.table(cellText=DATA["row"]["sample_values"],
    rowLabels=[f"n = {n}" for n in DATA["row"]["sample_n"]],
    colLabels=[f"j = {j}" for j in DATA["row"]["sample_j"]],
    loc="center",cellLoc="center")
tbl.auto_set_font_size(False);tbl.set_fontsize(12.7);tbl.scale(1,1.78)
for (i,j),cell in tbl.get_celld().items():
    cell.set_edgecolor("#cedbe2")
    cell.set_facecolor("#eaf4f4" if i==0 or j==-1 else "#f8fbfd")
    cell.get_text().set_color(INK)
txt(c,.5,.295,"Twelve coordinates only; every nonnegative integer has one preimage.",
    11.4,color=MUTED,ha="center")
txt(c,.045,.202,r"$R=\sum_{n\geq0}r_n\otimes E_{0n},\qquad R^*R=1,\quad RR^*=e$",
    13.3,color=BLUE)
txt(c,.045,.114,r"$\Omega(RaR^*)=\Omega(a)\quad(a\geq0),\qquad e=1\otimes E_{00}$",
    13.4,color=TEAL)
txt(c,.045,.037,r"$R_m\to R$ and $R_m^*\to R^*$ strongly; $\|R-R_m\|=1$ for finite $m$.",
    11.5,color=MUTED)

d=panel([.517,.095,.438,.378],"D  |  Two hypotheses, two boundaries")
table_ax=d.inset_axes([.055,.44,.89,.37]);table_ax.axis("off")
table=table_ax.table(
    cellText=[
      [r"$e^Q$ on $B(L^2)$","no","yes"],
      [r"$1_K\otimes e^Q$, $K$ infinite","yes","yes"],
      [r"$\mathrm{Tr}_K$, $K$ infinite","yes","no"]],
    colLabels=["Weight / density","Properly infinite\ncentralizer","All real\n eigenfield"],
    colWidths=[.50,.28,.22],loc="center",cellLoc="center")
table.auto_set_font_size(False);table.set_fontsize(11.6);table.scale(1,2.28)
for (i,j),cell in table.get_celld().items():
    cell.set_edgecolor("#cedbe2")
    cell.set_facecolor("#eaf4f4" if i in [0,2] else "#f8fbfd")
    cell.get_text().set_color(INK)
txt(d,.045,.378,"Same modular group does not determine normalization.",12.2,color=MUTED)
bar=d.inset_axes([.25,.17,.64,.14])
bar.barh([1,0],[1,2],color=[BLUE,ORANGE],height=.48)
bar.set(yticks=[1,0],yticklabels=[r"$\mathrm{Tr}(p)$",r"$2\mathrm{Tr}(p)$"],
        xlim=(0,2.35),xticks=[])
for yy,v in zip([1,0],[1,2]):bar.text(v+.05,yy,str(v),va="center",fontsize=13,color=INK)
bar.spines[["left","right","top","bottom"]].set_visible(False)
bar.tick_params(axis="y",length=0,labelsize=12)
txt(d,.045,.064,r"$p$ is rank one; every unitary conjugate still has trace $1$.",
    11.7,color=MUTED)

fig.text(.045,.047,"Proofs: DWC5.a–DWC5.w and the five solved diagnostics DWC6.",fontsize=12,color=MUTED)
fig.text(.045,.024,"Original diagram and source: CC0. Exact matrix and row data accompany the reproducible drawing.",fontsize=11,color=MUTED)
fig.savefig(HERE/"dwc-models.png",dpi=180,facecolor=BG)
fig.savefig(HERE/"dwc-models.svg",facecolor=BG)
plt.close(fig)
license_path=Path(font_manager.findfont("DejaVu Sans")).parent/"LICENSE_DEJAVU"
if not license_path.is_file():raise FileNotFoundError("The DejaVu license must be retained.")
shutil.copyfile(license_path,HERE/"FONT-LICENSE.txt")
print("Rendered dwc-models.png and dwc-models.svg; retained FONT-LICENSE.txt.")
