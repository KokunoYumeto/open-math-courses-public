"""Reproduce the original GL8 exact example and GL4–6 mechanism. CC0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

D=Path(__file__).resolve().parent
OUT=D/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
                    "svg.hashsalt":"OA-FLOW-GL-Z6-square-v1"})
blue="#1366ad";orange="#d56d16";green="#268548";purple="#8756a4";dark="#15304c"
w=np.array([[0,0],[1,0],[1,2]],dtype=int)
group=np.array([(s,t) for s in range(6) for t in range(6)])
labels=group.copy()
selector_errors=[]; records=[]
for p,q in labels:
    f=np.exp(2j*np.pi*(group@np.array([p,q]))/6)/36
    for i in range(3):
        for j in range(3):
            phase=np.exp(2j*np.pi*(group@(w[i]-w[j]))/6)
            value=np.sum(f*phase)
            label=(w[j]-w[i])%6
            expected=int(np.array_equal(label,[p,q]))
            selector_errors.append(abs(value-expected))
            records.append({"filter_label":[int(p),int(q)],
                            "matrix_unit":[i+1,j+1],
                            "spectral_label":[int(x) for x in label],
                            "exact_filter_coefficient":expected})
assert max(selector_errors)<1e-13
dual_gram=np.exp(2j*np.pi*(group@labels.T)/6)
assert np.max(abs(dual_gram.conj().T@dual_gram-36*np.eye(36)))<1e-12
e12=np.zeros((3,3));e12[0,1]=1
e23=np.zeros((3,3));e23[1,2]=1
e13=np.zeros((3,3));e13[0,2]=1
assert np.array_equal(e12@e23,e13)

fig=plt.figure(figsize=(15,12),dpi=200,facecolor="white")
gs=fig.add_gridspec(2,2,height_ratios=[1,1.05],hspace=.29,wspace=.22,
                     left=.06,right=.97,top=.86,bottom=.055)
fig.text(.06,.965,"Spectral localization: filters, adjoints and products",
         fontsize=25,color=dark,weight="bold")
fig.text(.06,.925,"A–B: exact model on (ℤ/6ℤ)².    C: the arbitrary LCA-group proof mechanism.",
         fontsize=16,color=dark)
ax=fig.add_subplot(gs[0,0])
ax.set_title("A. Dual labels use the negative Fourier transform",loc="left",
             fontsize=16,pad=14,color=dark)
ax.scatter(*group.T,color="#ccd6df",s=33,zorder=1)
for point,color in [((1,0),blue),((0,2),orange),((1,2),green)]:
    ax.scatter(*point,s=145,color=color,zorder=4)
for point in [(5,0),(0,4),(5,4)]:
    ax.scatter(*point,s=125,facecolors="white",edgecolors=purple,
               linewidths=2,zorder=4)
ax.scatter(0,0,s=100,color=dark,zorder=4)
ax.annotate("",(1,0),(0,0),arrowprops={"arrowstyle":"->","color":blue,"lw":2})
ax.annotate("",(1,2),(1,0),arrowprops={"arrowstyle":"->","color":orange,"lw":2})
ax.annotate("",(1,2),(0,0),arrowprops={"arrowstyle":"->","color":green,"lw":2})
for point,text,offset,color in [
    ((1,0),r"$a=(1,0):\ e_{12}$",(12,-24),blue),
    ((0,2),r"$b=(0,2):\ e_{23}$",(12,55),orange),
    ((1,2),r"$a+b=(1,2):\ e_{13}$",(12,10),green),
    ((5,0),r"$-a:\ e_{21}$",(-65,-24),purple),
    ((0,4),r"$-b:\ e_{32}$",(12,8),purple),
    ((5,4),r"$-(a+b):\ e_{31}$",(-146,10),purple)]:
    ax.annotate(text,point,xytext=offset,textcoords="offset points",
                color=color,fontsize=13)
ax.text(.98,.98,"Coordinates modulo 6;\n0 is the diagonal label.",
        transform=ax.transAxes,ha="right",va="top",fontsize=11,color=dark)
ax.set_xticks(range(6));ax.set_yticks(range(6));ax.set_xlabel("p");ax.set_ylabel("q")
ax.set_xlim(-.45,5.6);ax.set_ylim(-.62,5.65);ax.set_aspect("equal")
ax.grid(alpha=.18)

ax=fig.add_subplot(gs[0,1]);ax.axis("off")
ax.set_title("B. An actual filter and an actual matrix product",loc="left",
             fontsize=16,pad=14,color=dark)
ax.text(.02,.95,r"$\gamma_{p,q}(s,t)=e^{2\pi i(ps+qt)/6}$"+"\n"
        +r"$f_{p,q}(s,t)=\gamma_{p,q}(s,t)/36,\quad"
        +r"\widehat f_{p,q}=1_{\{(p,q)\}}$",
        va="top",color=dark,linespacing=1.8,fontsize=17)
for x0,matrix,color,label in [
    (.025,e12,blue,r"$e_{12}$"),(.37,e23,orange,r"$e_{23}$"),
    (.72,e13,green,r"$e_{13}$")]:
    bx=ax.inset_axes([x0,.43,.24,.25])
    bx.imshow(matrix,cmap=matplotlib.colors.ListedColormap(["#eff3f7",color]),
              vmin=0,vmax=1)
    bx.set_xticks([]);bx.set_yticks([])
    for i in range(3):
        for j in range(3):
            bx.text(j,i,str(int(matrix[i,j])),ha="center",va="center",
                    color="white" if matrix[i,j] else "#50667b",fontsize=14)
    bx.set_title(label,color=color,pad=7,fontsize=18)
ax.text(.302,.55,"×",fontsize=25,color=dark,ha="center")
ax.text(.647,.55,"=",fontsize=25,color=dark,ha="center")
ax.text(.02,.33,r"$T_{f_{1,0}}(e_{12})=e_{12}$"+"\n"
        +r"$T_{f_{p,q}}(e_{12})=0\quad ((p,q)\ne(1,0))$"+"\n"
        +r"$\alpha_{s,t}(e_{ij})=\overline{\gamma_{w_j-w_i}(s,t)}\,e_{ij}$",
        va="top",color=dark,linespacing=1.4,fontsize=14)
ax.text(.02,.015,"Counting Haar on G; each dual point has Haar mass 1/36.\n"
        "Geometric sums prove every selector; no singleton converse is used.",
        va="bottom",color=dark,fontsize=11)

ax=fig.add_subplot(gs[1,:]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.set_title("C. General proof schematic — neighbourhood nets, full L¹ kernels, two normal limits",
             loc="left",fontsize=17,pad=10,color=dark)
def box(x,y,width,height,text,color):
    ax.add_patch(FancyBboxPatch((x,y),width,height,
        boxstyle="round,pad=0.012",facecolor="#f6f8fb",edgecolor=color,lw=1.8))
    ax.text(x+width/2,y+height/2,text,ha="center",va="center",
            color=dark,fontsize=13,linespacing=1.4)
box(.012,.49,.285,.38,
    r"$x\in M(E),\quad y\in M(F)$"+"\n"
    +r"$x_i=T_{k_i}x=T_{f_i}x$"+"\n"
    +r"$y_j=T_{k_j}y=T_{g_j}y$"+"\n"
    +r"$\|x_i\|\leq\|x\|,\quad\|y_j\|\leq\|y\|$"+"\n"
    +r"$x_i\to x,\ y_j\to y$ strongly-star",
    blue)
box(.36,.49,.285,.38,
    r"$\operatorname{supp}\widehat f_i\subset E+N$"+"\n"
    +r"$\operatorname{supp}\widehat g_j\subset F+N$"+"\n"
    +r"$D=\operatorname{supp}\widehat h$ compact"+"\n"
    +r"$D\cap(E+F+2N)=\varnothing$"+"\n"
    +"Compact plateaus: GL4–6",
    orange)
box(.71,.49,.275,.38,
    r"$\widehat K(\chi,\eta)=$"+"\n"
    +r"$\widehat h(\chi+\eta)\widehat f_i(\chi)\widehat g_j(\eta)=0$"+"\n"
    +r"$K=0\quad$ (Fourier injectivity)"+"\n"
    +r"$T_h(x_i y_j)=0$"+"\n"
    +"Whole L¹(G×G) identity: GL5",
    green)
for x0,x1 in [(.31,.347),(.66,.697)]:
    ax.annotate("",(x1,.67),(x0,.67),
                arrowprops={"arrowstyle":"->","lw":2,"color":dark})
box(.12,.045,.76,.32,
    r"$T_h(x_i y_j)=0\quad\longrightarrow\quad T_h(xy_j)=0"
    +r"\quad\longrightarrow\quad T_h(xy)=0$"+"\n"
    +"First i tends to its limit with j fixed; then j tends to its limit."+"\n"
    +"Fixed multiplication and each filter are normal at both separate limits."+"\n"
    +r"$\operatorname{sp}_\alpha(xy)\subset"
    +r"\overline{\operatorname{sp}_\alpha(x)+\operatorname{sp}_\alpha(y)}$",
    dark)
ax.annotate("",(.83,.36),(.83,.48),
            arrowprops={"arrowstyle":"->","lw":2,"color":dark})
fig.savefig(OUT/"spectral-localization.png",metadata={"Software":"OA-FLOW GL original CC0"})
fig.savefig(OUT/"spectral-localization.svg",metadata={"Date":None,"Creator":"OA-FLOW GL original CC0"})
plt.close(fig)
data={"group":"(Z/6Z)^2","Haar":"counting","dual_point_mass":"1/36",
      "weights":w.tolist(),"negative_Fourier_label_of_eij":"w_j-w_i modulo6",
      "all_324_exact_selector_coefficients":records,
      "numerical_selector_error":float(max(selector_errors)),
      "exact_product":"e12 e23 = e13",
      "general_panel":"schematic of GL4–6; not a finite-model reduction"}
(OUT/"spectral-localization-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"dimensions":[3000,2400],
                  "all_selector_checks":len(records),
                  "max_numeric_error":float(max(selector_errors))}))
