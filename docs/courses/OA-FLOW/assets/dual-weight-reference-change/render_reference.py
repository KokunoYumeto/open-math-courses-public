"""Ordered change of reference for dual-weight recognition. CC0-1.0."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
matplotlib.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
                           "svg.hashsalt":"oa-flow-fr-reference-20261015"})
OUT=Path(__file__).resolve().parent/"assets"
OUT.mkdir(exist_ok=True)
fig=plt.figure(figsize=(15,9.5),dpi=200,facecolor="#f4f7fa")
fig.text(.05,.953,"A new reference changes the cocycle, not the recovered weight",
         size=21,weight="bold",color="#17364c")
fig.text(.05,.914,r"Fixed target $\Omega=\widetilde{\psi}$ and fixed Haar measure; "
         r"$w_t=(D\varphi_0:D\varphi_1)_t$.",size=14,color="#455e70")
def panel(pos,title):
    ax=fig.add_axes(pos);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
    ax.add_patch(FancyBboxPatch((.005,.01),.99,.98,boxstyle="round,pad=0,rounding_size=.025",
                               fc="white",ec="#b9cbd9",lw=1))
    ax.text(.025,.88,title,size=15,weight="bold",color="#17364c")
    return ax
def box(ax,x,y,w,h,text,color="#dcecf5",size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.01,rounding_size=.02",
                               fc=color,ec="#7694aa",lw=1))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",size=size,color="#17364c",linespacing=1.5)
def arrow(ax,start,end):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle="-|>",mutation_scale=17,color="#4f7891",lw=1.5))
a=panel([.05,.64,.90,.23],"1  The normalized chain rule fixes the order  (FR15–FR16)")
box(a,.03,.27,.28,.40,r"$z_{0,t}=(D\Omega:D\widetilde{\varphi}_0)_t$"+
    "\n"+r"$v_{0,t}=\pi^{-1}(z_{0,t})$",size=14)
box(a,.68,.27,.29,.40,r"$z_{1,t}=z_{0,t}\,\pi(w_t)$"+
    "\n"+r"$v_{1,t}=v_{0,t}\,w_t$",color="#daeee5",size=15)
arrow(a,(.325,.46),(.66,.46))
a.text(.49,.62,"multiply on the right",ha="center",size=13,color="#17364c")
a.text(.03,.09,r"$\varphi_0,\varphi_1$: arbitrary faithful normal semifinite weights",size=13,color="#17364c")
b=panel([.05,.39,.90,.22],"2  The modular action changes with the reference  (FR16–FR17)")
b.text(.03,.60,r"$\sigma_t^{\varphi_0}(a)=w_t\,\sigma_t^{\varphi_1}(a)\,w_t^*$",size=18,color="#17364c")
b.text(.03,.34,r"$v_{1,t+s}=v_{0,t}w_t\,\sigma_t^{\varphi_1}(v_{0,s}w_s)"
       r"=v_{1,t}\,\sigma_t^{\varphi_1}(v_{1,s})$",size=17,color="#17364c")
b.text(.03,.10,r"UR recovers the same $\psi$, with all its finite and infinite values.",size=14,color="#17364c")
c=panel([.05,.07,.90,.29],"3  Exact noncommuting matrices at "+r"$t_0=\pi/\log9$"+"  (FR18)")
c.text(.03,.68,r"$\varphi_0=\mathrm{Tr},\quad \varphi_1(a)=\mathrm{Tr}(Sa),"
       r"\quad\psi(a)=\mathrm{Tr}(Ra)$",size=14,color="#17364c")
c.text(.03,.55,r"$S=\mathrm{diag}(1,9),\qquad R_{11}=R_{22}=5,\quad R_{12}=R_{21}=4$",
       size=14,color="#17364c")
def matrix(ax,x,y,cells,label):
    w,h=.12,.25
    ax.plot([x+.015,x,x,x+.015],[y+h,y+h,y,y],color="#17364c",lw=1.5)
    ax.plot([x+w-.015,x+w,x+w,x+w-.015],[y+h,y+h,y,y],color="#17364c",lw=1.5)
    for i,row in enumerate(cells):
        for j,v in enumerate(row):
            ax.text(x+w*(.30+.40*j),y+h*(.75-.50*i),str(v),ha="center",va="center",size=18,color="#17364c")
    ax.text(x+w/2,y-.07,label,ha="center",va="top",size=13,color="#17364c")
matrix(c,.08,.19,[[0,-1],[-1,0]],r"$v_{0,t_0}=R^{it_0}$")
c.text(.235,.30,r"$\times$",size=20,ha="center",color="#17364c")
matrix(c,.28,.19,[[1,0],[0,-1]],r"$w_{t_0}=S^{-it_0}$")
c.text(.44,.30,r"$=$",size=20,ha="center",color="#17364c")
matrix(c,.50,.19,[[0,1],[-1,0]],r"$v_{1,t_0}=v_{0,t_0}w_{t_0}$")
c.text(.70,.31,r"$\ne$",size=22,ha="center",color="#9b4c25")
matrix(c,.79,.19,[[0,-1],[1,0]],r"$w_{t_0}v_{0,t_0}$")
fig.text(.05,.03,"The first two panels hold in the full scope of FR2. The last is an exact finite-dimensional example.",size=11,color="#455e70")
fig.savefig(OUT/"reference-change.png",dpi=200,metadata={"Software":"OA-FLOW FR reference-change renderer"})
fig.savefig(OUT/"reference-change.svg",metadata={"Date":None,"Creator":"OA-FLOW FR reference-change renderer"})
plt.close(fig)
f=OUT/"reference-change.svg"
f.write_text("\n".join(line.rstrip() for line in f.read_text(encoding="utf-8").splitlines())+"\n",encoding="utf-8")
def multiply(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
v0=[[0,-1],[-1,0]];w=[[1,0],[0,-1]]
correct=multiply(v0,w);reverse=multiply(w,v0)
assert correct==[[0,1],[-1,0]] and reverse==[[0,-1],[1,0]] and correct!=reverse
data={"target_fixed":"Omega=dual(psi)","reference_change":"phi0 to phi1","comparison":"w_t=(Dphi0:Dphi1)_t",
      "crossed_product_cocycle":"z1_t=z0_t*pi(w_t)","coefficient_cocycle":"v1_t=v0_t*w_t",
      "modular_action":"sigma_phi0_t=Ad(w_t) composed sigma_phi1_t","recovered_weight":"psi, unchanged",
      "R":[[5,4],[4,5]],"S":[[1,0],[0,9]],"time":"pi/log(9)","v0_at_time":v0,"w_at_time":w,
      "v0_times_w":correct,"w_times_v0":reverse,"proof":"FR5, equations FR15-FR18",
      "native_pixels":[3000,1900]}
(OUT/"reference-change-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print("Rendered ordered reference-change diagram and exact matrix products.")
