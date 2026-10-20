"""Original exact diagrams for stable algebras and the parameter tensor witness."""
from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

r=Path(__file__).resolve().parent
matplotlib.rcParams.update({"font.family":"DejaVu Sans","font.size":19,
                           "svg.hashsalt":"actual-infinite-evaluation"})
blue,red,grey="#145da0","#a12b3a","#687587"
fig,axes=plt.subplots(3,1,figsize=(7.4,17.8),
                     gridspec_kw={"height_ratios":[1,1.3,1]})
fig.subplots_adjust(left=.055,right=.945,top=.94,bottom=.035,hspace=.56)
for a in axes:a.axis("off")

def line(a,y,txt,color="black",size=21):
    a.text(.5,y,txt,ha="center",va="center",color=color,
           fontsize=size,transform=a.transAxes)

a=axes[0]
a.set_title("A. The finite algebra quotients stabilize",fontsize=20,pad=13)
line(a,.90,r"$U'\subset U_*\quad\Longrightarrow\quad\Gamma_{U'}\twoheadrightarrow\Gamma_{U_*}$",
     grey,19)
line(a,.67,r"$A_{U'}/a_{U'}\ \longrightarrow\ A_{U_*}/a_{U_*}$",blue,22)
line(a,.49,"Surjective, with the same maximum dimension",blue,17)
line(a,.28,r"$\dim A_U/a_U\leq 1+m q^2$",size=23)
line(a,.05,"EV.13–EV.15: the algebra map is an isomorphism",size=17)

a=axes[1]
a.set_title("B. The independent normal parameter",fontsize=20,pad=15)
line(a,.95,r"$v\in C_{\mathrm{tr}}\otimes_R N$",size=22)
line(a,.79,r"$\downarrow\ \kappa$",blue,22)
line(a,.65,r"$\kappa(v)\in N^{[u]}$",size=22)
line(a,.50,r"$\downarrow\ D_s^{-1}\quad(\tau_s=1)$",blue,22)
line(a,.35,r"$w=e_\Phi^{[u]}(D_s^{-1}\kappa(v))$",size=21)
line(a,.17,r"$D_s w=(C_{\mathrm{tr}}\otimes e_\Phi)(v)$",red,21)
line(a,.015,"EV.28–EV.32: actual finite balancing witnesses",size=17)

a=axes[2]
a.set_title("C. Full scalar change and faithfulness",fontsize=20,pad=15)
a.text(.19,.91,r"$N$",ha="center",va="center",fontsize=24,color=blue,transform=a.transAxes)
a.text(.81,.91,r"$B\otimes_R K^\infty$",ha="center",va="center",fontsize=22,color=blue,transform=a.transAxes)
a.annotate("",xy=(.64,.91),xytext=(.31,.91),xycoords="axes fraction",
           arrowprops={"arrowstyle":"->","color":blue,"lw":2})
a.text(.48,.98,r"$\Psi$",ha="center",va="center",fontsize=20,color=blue,transform=a.transAxes)
for xx,txt in [(.19,r"$(\Phi_a^\infty)_a$"),(.81,"action")]:
    a.annotate("",xy=(xx,.46),xytext=(xx,.78),xycoords="axes fraction",
               arrowprops={"arrowstyle":"->","color":"black","lw":1.8})
    a.text(xx,.34,txt,ha="center",va="center",fontsize=19,transform=a.transAxes)
for xx in [.19,.81]:
    a.text(xx,.16,r"$\mathcal{C}^{\,q}$",ha="center",va="center",fontsize=25,transform=a.transAxes)
a.text(.5,.16,"=",ha="center",va="center",fontsize=25,transform=a.transAxes)
line(a,-.01,"EV.36: "+r"$\Psi$"+" is B-linear",blue,18)
line(a,-.08,"SE.1 and EV.39: "+r"$\Psi$"+" is injective",red,18)

fig.savefig(r/"actual-infinite-evaluation.png",dpi=160,
            metadata={"Software":"Matplotlib"})
fig.savefig(r/"actual-infinite-evaluation.svg",
            metadata={"Date":None,"Creator":"Open mathematics course figures"})
plt.close(fig)
data={
 "panel_A":{"group_map":"surjective; no group isomorphism asserted",
            "a_U":"I_U ker(rho_U)","dimension_bound":"1+m q^2",
            "U_star":"a product attaining the maximum finite quotient dimension",
            "algebra_map":"A_U'/a_U' -> A_Ustar/a_Ustar; surjective and equal dimension",
            "proof":["EV.13","EV.14","EV.15"]},
 "panel_B":{"coordinates":["independent output parameter u","input time s","spatial x"],
            "source_covector":"nu_u=0, tau_s=1",
            "C_tr":"D_infinity_(u,s,x) / D_infinity_(u,s,x) D_u",
            "w":"e_Phi^[u](D_s^-1 kappa(v))",
            "identity":"D_s w = (C_tr tensor_R e_Phi)(v)",
            "tensor":"ordinary algebraic; finitely many elementary factors",
            "proof":["EV.28","EV.29","EV.30","EV.31","EV.32"]},
 "panel_C":{"top_arrow":"Psi(s)=1 tensor e(s)",
            "right_vertical":"balanced full B action via j:K_infinity->C",
            "left_vertical":"the entire finite directional Hom evaluation",
            "commutes":True,"injectivity_input":"SE.1",
            "scalar_reconstruction":"B tensor_T N = N by ISR.8--ISR.10",
            "unproved_mixed_flatness_used":False,
            "proof":["EV.36","EV.37","EV.38","EV.39","EV.40"]},
 "diagram_has_no_geometric_scale":True,
 "source_context":"https://www.kurims.kyoto-u.ac.jp/~kenkyubu/kashiwara/HolIII.pdf"}
(r/"actual-infinite-evaluation-exact-data.json").write_text(
 json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
