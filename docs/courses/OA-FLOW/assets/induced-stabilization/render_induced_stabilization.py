"""Exact affine-group coordinates and normal stabilization ladder; CC0 new expression."""
from pathlib import Path
import json, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,"svg.hashsalt":"OA-FLOW-induced-stabilization-20261005"})
D=Path(__file__).resolve().parent;(D/"assets").mkdir(exist_ok=True)
fig=plt.figure(figsize=(18,12),dpi=200,facecolor="#f5f8fc")
fig.text(.5,.97,"A quotient factor and a subgroup crossed product",ha="center",fontsize=25,weight="bold",color="#152e49")
fig.text(.5,.925,"Exact lcsc stabilization, including the nonunimodular density and arbitrary coefficient algebra",ha="center",fontsize=14,color="#476078")
grid=fig.add_gridspec(2,2,left=.06,right=.96,bottom=.07,top=.875,hspace=.38,wspace=.24)
ax=fig.add_subplot(grid[0,0]);ax.set_facecolor("white")
for b in [-2,-1,0,1,2]:ax.plot([b,b],[-1.4,1.8],color="#accad8",lw=2)
ax.plot([-2.5,2.5],[0,0],color="#de943a",lw=3,label=r"section $\sigma(b)=(b,1)$")
ax.plot([0,0],[-1.4,1.8],color="#247c98",lw=3)
ax.scatter([1],[.35],s=80,color="#aa4b67",zorder=4)
ax.annotate("",xy=(1,1.35),xytext=(1,.35),arrowprops={"arrowstyle":"->","lw":2.8,"color":"#aa4b67"})
ax.text(1.13,.73,r"$R_G(0,e^1):\ u\mapsto u+1$"+"\n"+r"amplitude $e^{-1/2}$",fontsize=11,color="#81374d")
ax.text(-2.38,1.58,"Each vertical line is one complete coset",fontsize=10,color="#476078")
ax.text(-2.36,-1.22,r"$ds=e^{-u}\,db\,du,\quad \rho=e^u,\quad \rho\,ds=db\,du$",fontsize=12,bbox={"facecolor":"#eff5fb","edgecolor":"none","pad":6})
ax.set(xlim=(-2.5,2.5),ylim=(-1.4,1.8),xlabel=r"quotient coordinate $b$",ylabel=r"subgroup coordinate $u=\log a$")
ax.set_title("A. Affine group: the measure correction is visible",loc="left",fontsize=15,weight="bold",pad=16)
ax.legend(loc="lower right",bbox_to_anchor=(1,-.30),frameon=False,fontsize=10)
ax2=fig.add_subplot(grid[0,1]);ax2.axis("off");ax2.set_title("B. The full-domain right action",loc="left",fontsize=15,weight="bold",pad=16)
steps=[
(.82,r"$\xi(b,e^u)\in L^2(e^{-u}\,db\,du)$","Ambient Haar norm"),
(.49,r"$(J\xi)(b,u)=e^{-u/2}\xi(b,e^u)$",r"Product norm in $L^2(db\,du)$"),
(.16,r"$JR_G(0,c)J^*\eta(b,u)=\eta(b,u+\log c)$","Subgroup right action: no amplitude factor")]
for y,form,label in steps:
    ax2.add_patch(FancyBboxPatch((.015,y-.10),.965,.20,boxstyle="round,pad=.012",facecolor="#eaf3f8",edgecolor="#8aabbc",transform=ax2.transAxes))
    ax2.text(.50,y+.025,form,ha="center",va="center",fontsize=15,transform=ax2.transAxes)
    ax2.text(.50,y-.052,label,ha="center",va="center",fontsize=11,color="#476078",transform=ax2.transAxes)
for y in [.66,.33]:ax2.annotate("",xy=(.5,y-.06),xytext=(.5,y+.035),arrowprops={"arrowstyle":"->","lw":2,"color":"#de943a"},xycoords=ax2.transAxes)
ax3=fig.add_subplot(grid[1,0]);ax3.axis("off");ax3.set_title("C. Exact normal algebra identifications",loc="left",fontsize=15,weight="bold",pad=16)
ladder=[
(.86,r"$M\rtimes_\alpha G$","NCF4: commuting-action interchange"),
(.60,r"$(N\bar{\otimes} B(L^2G))\cap(V\otimes R_G(H))'$","W: regular transformation coordinates"),
(.34,r"$D\bar{\otimes} B(L^2Y)$","J: quotient / subgroup coordinates"),
(.08,r"$(N\rtimes_\beta H)\bar{\otimes} B(L^2Y)$","NCF2–3 / CCM7: identify D")]
for y,form,label in ladder:
    ax3.text(.50,y,form,ha="center",va="center",fontsize=14,transform=ax3.transAxes)
    ax3.text(.50,y-.065,label,ha="center",va="center",fontsize=10,color="#476078",transform=ax3.transAxes)
for y in [.73,.47,.21]:ax3.annotate("",xy=(.5,y-.025),xytext=(.5,y+.025),arrowprops={"arrowstyle":"->","lw":1.7,"color":"#247c98"},xycoords=ax3.transAxes)
ax4=fig.add_subplot(grid[1,1]);ax4.axis("off");ax4.set_title("D. Finite matrices close the reverse inclusion",loc="left",fontsize=15,weight="bold",pad=16)
for i in range(3):
    for j in range(3):
        x=.26+j*.15;y=.73-i*.15
        ax4.add_patch(FancyBboxPatch((x-.065,y-.065),.13,.13,boxstyle="round,pad=.002",facecolor="#d7e8f1",edgecolor="white",transform=ax4.transAxes))
        ax4.text(x,y,rf"$a_{{{i+1}{j+1}}}\in D$",ha="center",va="center",fontsize=12,transform=ax4.transAxes)
ax4.text(.50,.91,r"$F=\{i_1,i_2,i_3\}$: one finite sample",ha="center",fontsize=11,color="#476078",transform=ax4.transAxes)
ax4.text(.50,.28,r"$p_Fap_F=\sum_{i,j\in F}a_{ij}\otimes|e_i\rangle\langle e_j|$",ha="center",fontsize=14,transform=ax4.transAxes)
ax4.text(.50,.15,r"$\|p_Fap_F\|\leq\|a\|,\qquad p_Fap_F\longrightarrow a$ strong*",ha="center",fontsize=13,transform=ax4.transAxes)
ax4.text(.50,.035,"The net runs over all finite subsets of any basis.\nNo separability of N or its Hilbert space is imposed.",ha="center",fontsize=11,color="#476078",transform=ax4.transAxes)
fig.text(.5,.021,"IS1–IS6: complete section, measure, unitary, normal transport and reverse tensor inclusion proofs",ha="center",fontsize=12,color="#476078")
fig.savefig(D/"assets/induced-stabilization.png",dpi=200,metadata={"Software":"OA-FLOW original mathematical figure"})
fig.savefig(D/"assets/induced-stabilization.svg",metadata={"Date":None})
data={"native_dimensions":[3600,2400],"group":"(b,a)(c,r)=(b+ac,ar)","left_haar":"db da / a^2","ambient_modular":"a^-1","subgroup":"H={(0,r):r>0}","subgroup_left_haar":"dr/r","subgroup_modular":1,"quotient":"R_b","section":"sigma(b)=(b,1)","rho":"a=e^u","quotient_measure":"db","plot_coordinates":{"b_range":[-2.5,2.5],"u_range":[-1.4,1.8],"cosets":[-2,-1,0,1,2],"sample_arrow":{"b":1,"u_start":.35,"u_end":1.35,"c":"e","ambient_amplitude":"e^-1/2"}},"finite_matrix_scope":"Symbolic 3x3 sample of an arbitrary finite-basis compression; no numerical operator or finite-dimensional theorem restriction.","logical_scope":"lcsc G, closed H, arbitrary N and normal continuous beta; stabilization of the defined induced system only."}
(D/"figure-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8",newline="\n")
print("Rendered exact 3600x2400 PNG/SVG/data")

