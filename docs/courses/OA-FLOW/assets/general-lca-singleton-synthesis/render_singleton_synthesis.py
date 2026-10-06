"""Original exact SS4 model and SS1–3 norm mechanism. CC0."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
D=Path(__file__).resolve().parent;OUT=D/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":13,
                    "svg.hashsalt":"OA-FLOW-SS-Z6-v1"})
blue="#146bac";orange="#cc6e1e";green="#238250";purple="#7d58a1";dark="#19334e"
s=np.arange(6);zeta=np.exp(2j*np.pi/6)
a=np.zeros(6,dtype=complex);a[0]=1;a[1]=-zeta
k=zeta**s/6;shift=np.roll(k,1)
ahat=np.array([np.sum(a*zeta**(-n*s)) for n in s])
q=np.array([np.sum(k*zeta**(-n*s)) for n in s])
conv=np.array([sum(a[t]*k[(u-t)%6] for t in s) for u in s])
assert np.max(abs(conv))<1e-14
assert np.max(abs(q-np.eye(6)[1]))<1e-14
assert abs(np.sum(abs(k))-1)<1e-14
selector=sum(k[u]*zeta**(-u) for u in s)
assert abs(selector-1)<1e-14
fig=plt.figure(figsize=(15,11.5),dpi=200,facecolor="white")
fig.text(.05,.964,"Singleton synthesis: a norm proof and its exact phase",fontsize=25,
         weight="bold",color=dark)
fig.text(.05,.923,"A–C: exact Z/6Z example.    D: the arbitrary-LCA-group proof; no closed-set synthesis is assumed.",
         fontsize=15,color=dark)
gs=fig.add_gridspec(2,3,height_ratios=[1,1.1],left=.06,right=.96,top=.85,
                     bottom=.055,hspace=.3,wspace=.3)
ax=fig.add_subplot(gs[0,0])
ax.set_title("A. Vanishing at the chosen character",fontsize=14,color=dark,pad=12,loc="left")
ax.bar(s-.15,ahat.real,width=.28,color=blue,label=r"$\mathrm{Re}\,\widehat a(n)$")
ax.bar(s+.15,ahat.imag,width=.28,color=orange,label=r"$\mathrm{Im}\,\widehat a(n)$")
ax.scatter([1],[0],s=165,facecolors="white",edgecolors=green,lw=2.5,zorder=5)
ax.axvspan(.72,1.28,color=green,alpha=.08)
ax.annotate(r"$\widehat a(1)=0$",xy=(1,0),xytext=(.05,-.63),color=green,
            arrowprops={"arrowstyle":"->","color":green},fontsize=14)
ax.set_xticks(s);ax.set_xlabel(r"dual label $n$ (modulo 6)")
ax.set_ylim(-1.2,2.65);ax.axhline(0,color="#697a8d",lw=.8)
ax.grid(axis="y",alpha=.16);ax.legend(loc="upper left",bbox_to_anchor=(.02,.89),
                                    fontsize=10,frameon=False)
ax.text(.03,.98,r"$a=\delta_0-\zeta\delta_1,\quad"
        +r"\widehat a(n)=1-\zeta^{1-n}$",transform=ax.transAxes,
        va="top",fontsize=12,color=dark)

ax=fig.add_subplot(gs[0,1])
ax.set_title("B. The convolution cancels exactly",fontsize=14,color=dark,pad=12,loc="left")
t=np.linspace(0,2*np.pi,301)
ax.plot(np.cos(t)/6,np.sin(t)/6,color="#c5d2df",lw=1)
ax.scatter(k.real,k.imag,color=blue,s=65,zorder=3,label=r"$k(s)=\zeta^s/6$")
ax.scatter((zeta*shift).real,(zeta*shift).imag,facecolors="none",edgecolors=orange,
           s=145,lw=1.5,zorder=4,label=r"$\zeta k(s-1)=k(s)$")
for u in s:
    ax.annotate(str(u),xy=(k[u].real,k[u].imag),xytext=(7,7),
                textcoords="offset points",color=dark,fontsize=12)
ax.scatter([0],[0],marker="x",s=95,lw=2,color=green,zorder=5)
ax.text(0,-.06,r"$a*k=0$",ha="center",color=green,fontsize=14)
ax.axhline(0,lw=.7,color="#a0adb9");ax.axvline(0,lw=.7,color="#a0adb9")
ax.set_xlim(-.24,.24);ax.set_ylim(-.24,.24);ax.set_aspect("equal")
ax.set_xticks([-1/6,0,1/6],labels=[r"$-1/6$","0",r"$1/6$"])
ax.set_yticks([-1/6,0,1/6],labels=[r"$-1/6$","0",r"$1/6$"])
ax.set_xlabel("real part");ax.set_ylabel("imaginary part")
ax.legend(loc="upper left",bbox_to_anchor=(.01,.99),fontsize=9,frameon=False)

ax=fig.add_subplot(gs[0,2]);ax.axis("off")
ax.set_title("C. The spectral label is the exact phase",fontsize=14,color=dark,pad=12,loc="left")
ax.text(.02,.97,r"$U_s=\mathrm{diag}(1,\zeta^s),\quad\alpha_s=\mathrm{Ad}\,U_s$",
        va="top",color=dark,fontsize=14)
matrix=np.array([[0,1],[0,0]])
bx=ax.inset_axes([.27,.46,.43,.36]);bx.imshow(matrix,
    cmap=matplotlib.colors.ListedColormap(["#eff3f7",purple]),vmin=0,vmax=1)
for i in range(2):
    for j in range(2):
        bx.text(j,i,str(matrix[i,j]),ha="center",va="center",fontsize=19,
                color="white" if matrix[i,j] else "#647589")
bx.set_xticks([]);bx.set_yticks([]);bx.set_title(r"$e_{12}$",color=purple,fontsize=18)
ax.text(.02,.35,r"$\mathrm{sp}_\alpha(e_{12})=\{1\}$"+"\n"
        +r"$\alpha_s(e_{12})=\overline{\gamma_1(s)}\,e_{12}$"+"\n"
        +r"$T_k(e_{12})=e_{12}$"+"\n"
        +r"$M(\{0\})=$ diagonal matrices",
        va="top",color=dark,fontsize=14,linespacing=1.7)

ax=fig.add_subplot(gs[1,:]);ax.axis("off");ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title("D. General norm mechanism — the two kernels serve different purposes",
             fontsize=16,color=dark,pad=14,loc="left")
def box(x,y,w,h,text,color,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.01",
                facecolor="#f7f9fc",edgecolor=color,lw=1.8))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=dark,
            fontsize=size,linespacing=1.5)
box(.012,.49,.205,.39,
    r"$\widehat a(\gamma)=0$"+"\n"
    +"LF1–2: local plateau q"+"\n"
    +r"$q=1$ near $\gamma$"+"\n"
    +r"$\|k_\gamma\|_1<\sqrt{2}$"+"\n"
    +r"$\|a*k_\gamma\|_1<\varepsilon$",blue)
box(.268,.49,.205,.39,
    r"$b=a-a*k_\gamma$"+"\n"
    +r"$\widehat b=\widehat a(1-q)$"+"\n"
    +r"$\widehat b=0$ near $\gamma$"+"\n"
    +r"$\|a-b\|_1<\varepsilon$",orange)
box(.524,.49,.205,.39,
    "Distinct LF5 kernels:"+"\n"
    +r"$b*k_i\to b$ in $L^1$"+"\n"
    +"compact Fourier supports"+"\n"
    +"still missing γ"+"\n"
    +r"$\widehat b\in j(\gamma)$",green)
box(.78,.49,.205,.39,
    "ε can be arbitrarily small"+"\n"
    +r"$\widehat a\in j(\gamma)$"+"\n"
    +r"$I(\gamma)=j(\gamma)$"+"\n"
    +"singleton synthesis",purple)
for x0,x1 in [(.225,.255),(.482,.51),(.74,.766)]:
    ax.annotate("",(x1,.69),(x0,.69),arrowprops={"arrowstyle":"->","lw":2,"color":dark})
box(.09,.05,.82,.29,
    r"$\mathrm{sp}_\alpha(x)\subset\{\gamma\}"
    +r"\ \Longrightarrow\ I(\gamma)\subset J_x"
    +r"\ \Longrightarrow\ T_f x=\widehat f(\gamma)x$"+"\n"
    +r"$T_gx=x,\quad \alpha_sx=T_{L_sg}x=\overline{\gamma(s)}x$"+"\n"
    +"At the trivial character this is exactly the fixed algebra: SS3.",dark,14)
ax.annotate("",(.88,.35),(.88,.48),
            arrowprops={"arrowstyle":"->","lw":2,"color":dark})
fig.savefig(OUT/"singleton-synthesis.png",metadata={"Software":"OA-FLOW SS original CC0"})
fig.savefig(OUT/"singleton-synthesis.svg",metadata={"Date":None,"Creator":"OA-FLOW SS original CC0"})
plt.close(fig)
data={"group":"Z/6Z","physical_Haar":"counting","dual_point_mass":"1/6",
 "zeta":"exp(2pi i/6)","a":"delta0-zeta delta1","k":"zeta^s/6",
 "exact_ahat":["(1-i sqrt3)/2","0","(1+i sqrt3)/2",
               "(3+i sqrt3)/2","2","(3-i sqrt3)/2"],
 "exact_q":[0,1,0,0,0,0],"exact_convolution":[0]*6,"exact_k_L1_norm":1,
 "matrix":"e12","spectral_label":1,"action_phase":"conjugate gamma1(s)",
 "numerical_checks":{"max_convolution_error":float(np.max(abs(conv))),
    "max_selector_error":float(np.max(abs(q-np.eye(6)[1])))},
 "panel_D":"general norm proof schematic; not a finite-group reduction"}
(OUT/"singleton-synthesis-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"dimensions":[3000,2300],"exact_model_error":float(np.max(abs(conv)))}))
