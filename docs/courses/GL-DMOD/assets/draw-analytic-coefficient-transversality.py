"""Reproduce the common-domain resolution and exact nilpotent module diagram."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

r=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
 "svg.hashsalt":"GL-DMOD-AT-20261021"})
fig,(a,b)=plt.subplots(1,2,figsize=(14,8),facecolor="#f7f9fd")
ink="#14243d";blue="#2758aa";teal="#00818d";gold="#a76912"
for ax in [a,b]:ax.set(xlim=(0,1),ylim=(0,1));ax.axis("off")
def box(ax,y,text,sub="",color=blue,h=.14):
 ax.add_patch(FancyBboxPatch((.025,y-h/2),.95,h,
  boxstyle="round,pad=0.012",edgecolor=color,facecolor="white",linewidth=1.2))
 ax.text(.5,y+.018,text,ha="center",va="center",color=ink,fontsize=10.7)
 if sub:ax.text(.5,y-.044,sub,ha="center",va="center",color=color,fontsize=9.4)
def down(ax,y1,y2):
 ax.annotate("",(.5,y2),(.5,y1),arrowprops={"arrowstyle":"->","color":teal,"lw":1.6})
a.set_title("One product domain in every degree",fontweight="bold",color=ink,pad=18)
box(a,.87,"Coherent kernels on the outer product",
 "Finite global generators near K = closure(U) × closure(V); CX.M",h=.145)
down(a,.785,.715)
box(a,.64,r"$\cdots\to\mathcal{L}_1\to\mathcal{L}_0\to\mathcal{H}\to0$",
 "Exact on the same U × V in all degrees; AT.18–AT.19",h=.145)
down(a,.555,.485)
box(a,.41,"Sections form a strict, nuclearly free A-resolution",
 r"$A=\mathcal{O}(U),\quad L_q=A\,\widehat{\otimes}\,\mathcal{O}(V)^{r_q}$",h=.145)
down(a,.325,.255)
box(a,.18,"Actual restriction to U' × V",
 r"$B=\mathcal{O}(U'),\quad B\widehat{\otimes}_A E=\mathcal{H}(U'\times V)$",h=.16)
a.text(.5,.025,r"$\widehat{\mathrm{Tor}}^A_q(B,E)=0\ (q>0)$; Hausdorff in degree zero",
 ha="center",va="center",color=teal,fontsize=10.4)

b.set_title("A nonflat three-jet coefficient module",fontweight="bold",color=ink,pad=18)
b.text(.5,.93,r"$\mathcal{H}=\mathcal{O}/(z^3),\quad E=\mathcal{O}(V)e_0\oplus\mathcal{O}(V)e_1\oplus\mathcal{O}(V)e_2$",
 ha="center",va="center",color=ink,fontsize=11)
xs=[.10,.36,.62,.89]
for x,t in zip(xs,[r"$e_0=[1]$",r"$e_1=[z]$",r"$e_2=[z^2]$",r"$0$"]):
 b.text(x,.76,t,ha="center",va="center",color=blue,fontsize=14)
for x0,x1 in zip(xs,xs[1:]):
 b.annotate("",(x1-.06,.76),(x0+.065,.76),arrowprops={"arrowstyle":"->","color":teal,"lw":1.6})
 b.text((x0+x1)/2,.815,r"$z$",ha="center",va="center",color=teal,fontsize=12)
b.text(.27,.59,"Matrix columns are z·eⱼ",ha="center",color=ink,fontsize=10.5)
b.text(.27,.49,"[0  0  0]\n[1  0  0]\n[0  1  0]",ha="center",va="center",
 family="DejaVu Sans Mono",fontsize=14,color=blue,linespacing=1.45)
b.text(.73,.51,r"$J^3=0,\quad J^2\ne0$",ha="center",va="center",color=blue,fontsize=14)
box(b,.30,"If 0 lies in U': retain all three jet layers",
 r"$B\widehat{\otimes}_A E=\mathcal{O}(V)^3$",h=.125)
box(b,.12,"If U' avoids 0: z is invertible",
 r"$B\widehat{\otimes}_A E=0$",color=gold,h=.125)
b.text(.5,.015,"Basis layers are module coordinates, not separate support points.",
 ha="center",va="center",color=ink,fontsize=9.4)
fig.subplots_adjust(left=.025,right=.985,top=.91,bottom=.06,wspace=.10)
fig.savefig(r/"analytic-coefficient-transversality.png",dpi=170,facecolor=fig.get_facecolor())
fig.savefig(r/"analytic-coefficient-transversality.svg",metadata={"Date":None},facecolor=fig.get_facecolor())
records=[]
for m in range(1,7):
 j=[[int(i==k+1)for k in range(m)]for i in range(m)]
 records.append({"m":m,"basis":[f"[z^{k}]"for k in range(m)],
  "multiplication_by_z_columns":j,
  "power_m_is_zero":True,"power_m_minus_one_is_nonzero":True,
  "base_disc_contains_zero_rank":m,"base_disc_avoids_zero_rank":0})
(r/"analytic-coefficient-transversality-data.json").write_text(json.dumps({
 "kind":"exact integer nilpotent matrices and proof diagram",
 "proofs":["AT.18--AT.24","AT.36--AT.38"],
 "matrix_convention":"Rows and columns ordered e_0 through e_(m-1); column k is z times e_k.",
 "finite_records":records,"general_proof_is_in_source":True,
 "support_points_are_not_jet_basis_layers":True},indent=2)+"\n",encoding="utf-8")
plt.close(fig)
