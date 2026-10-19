"""Exact cochain and derived-support maps of AM.19d–AM.19h."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

parser = argparse.ArgumentParser()
parser.add_argument("--output-dir", type=Path)
args = parser.parse_args()
out = args.output_dir.resolve() if args.output_dir else Path(__file__).resolve().parent
out.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 14,
                     "mathtext.fontset": "dejavusans",
                     "svg.hashsalt": "diagonal-support-adjunction-AM19-20261018"})
bg, navy, blue = "#f9fbfd", "#173d56", "#1f6b91"
fig = plt.figure(figsize=(16,9), facecolor=bg)
fig.text(.035,.95,"Diagonal kernels: the full support-forgetting homotopy",
         fontsize=24, weight="bold", color=navy)
fig.text(.035,.898,
         r"$A=\Delta,\quad B=p_2^{-1}H,\quad k=(a,b),\quad e=(c,f),\quad \deg k=N$",
         fontsize=19, color=navy)
upper = fig.add_axes([.035,.49,.93,.35])
upper.set_xlim(0,1); upper.set_ylim(0,1); upper.axis("off")
for x,w,c in [(.01,.46,"#eef4fb"),(.54,.45,"#edf7f1")]:
    upper.add_patch(FancyBboxPatch((x,.015),w,.94,boxstyle="round,pad=.01",
                                   facecolor=c,edgecolor="#7290a5",lw=1.2))
upper.text(.035,.84,"Four-entry cube · every complement retained",fontsize=17,weight="bold",color=navy)
upper.text(.035,.66,r"$F(k,e)=(ac,\ bc,\ (-1)^Naf,\ (-1)^{N-1}bf)$",fontsize=19,color=navy)
upper.text(.035,.44,r"$\pi_A(x,x_A,x_B,z)=(x,x_A)$",fontsize=20,color=navy)
upper.text(.035,.20,r"$\pi_AF(k,e)=(ac,bc)=k\cup c$",fontsize=20,color=navy)
upper.annotate("",xy=(.53,.50),xytext=(.48,.50),
               arrowprops={"arrowstyle":"->","color":blue,"lw":2})
upper.text(.565,.84,"Proper homotopy · AM.19f",fontsize=17,weight="bold",color=navy)
upper.text(.565,.66,r"$S=\pi_AH_\rho,\qquad S(x,x_A,x_B,z)=(0,-\rho_Bz)$",fontsize=18,color=navy)
upper.text(.565,.44,r"$\pi_A-j_{A\cap B,A}\Phi_\rho=dS+Sd$",fontsize=21,color=navy)
upper.text(.565,.20,r"$(-1)^NQ_NL_\eta SF(k,-)$  is the traced homotopy.",fontsize=16,color=navy)

lower = fig.add_axes([.035,.14,.93,.29])
lower.set_xlim(0,1); lower.set_ylim(0,1); lower.axis("off")
lower.text(.01,.92,"The square is in the derived category of sheaves, before global sections.",fontsize=17,weight="bold",color=navy)
lower.text(.03,.64,r"$K=R\Gamma_H\mathcal{O}$",fontsize=23,color=navy,ha="left")
lower.text(.41,.64,r"$K=R\Gamma_H\mathcal{O}$",fontsize=23,color=navy,ha="left")
lower.annotate("",xy=(.40,.70),xytext=(.24,.70),
               arrowprops={"arrowstyle":"->","color":blue,"lw":1.8})
lower.text(.32,.79,r"$a_H^\Delta$",fontsize=21,color=navy,ha="center")
for x in [.12,.50]:
    lower.annotate("",xy=(x,.20),xytext=(x,.59),
                   arrowprops={"arrowstyle":"->","color":blue,"lw":1.8})
    lower.text(x+.014,.39,r"$j_H$",fontsize=21,color=navy)
lower.text(.12,.08,r"$\mathcal{O}$",fontsize=25,color=navy,ha="center")
lower.text(.50,.08,r"$\mathcal{O}$",fontsize=25,color=navy,ha="center")
lower.annotate("",xy=(.47,.14),xytext=(.15,.14),
               arrowprops={"arrowstyle":"->","color":blue,"lw":1.8})
lower.text(.32,.23,r"$T_+$",fontsize=21,color=navy,ha="center")
lower.text(.65,.64,r"$j_Ha_H^\Delta=T_+j_H$",fontsize=24,color=navy)
lower.text(.65,.39,"The support adjunction makes the lift unique.",fontsize=15,color=navy)
lower.text(.65,.12,r"$a_H^\Delta=R\Gamma_HT_+$",fontsize=25,color=navy)
fig.text(.035,.071,
         r"One collar $\eta=1$ near the entire diagonal makes the cup and every homotopy proper. "
         r"$\rho_Bz$ is defined on $U_A$; it is not extended across $A$.",
         fontsize=14,color=navy)
fig.text(.035,.026,
         "Exact proofs: AM.19d–h. The positive kernel is a normally convergent holomorphic coefficient on punctured normal domains.",
         fontsize=14,color=navy)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
width,height=fig.canvas.get_width_height()
for text in list(fig.texts)+list(upper.texts)+list(lower.texts):
    bounds=text.get_window_extent(renderer)
    assert bounds.x0>=5 and bounds.x1<=width-5,(text.get_text(),tuple(bounds.extents))
    assert bounds.y0>=5 and bounds.y1<=height-5,(text.get_text(),tuple(bounds.extents))
fig.savefig(out/"euler-model-diagonal-support.png",dpi=150,facecolor=bg)
fig.savefig(out/"euler-model-diagonal-support.svg",metadata={"Date":None},facecolor=bg)
plt.close(fig)
data={
    "type":"exact cochain/derived-object diagram, with no sampled geometry",
    "supports":{"A":"complex diagonal Delta","B":"p2^-1 H","H":"Re t >= 0"},
    "input":"e=(c,f)","kernel":"k=(a,b), degree N",
    "cup":"(ac,bc,(-1)^N af,(-1)^(N-1) bf)",
    "projection":"pi_A(x,x_A,x_B,z)=(x,x_A)",
    "homotopy":"S=pi_A H_rho; S(x,x_A,x_B,z)=(0,-rho_B z)",
    "identity":"pi_A-j_(A intersect B,A) Phi_rho=dS+Sd",
    "proper_traced_homotopy":"(-1)^N Q_N L_eta S F(k,-)",
    "domain_condition":"rho_B z is a coefficient on U_A; no extension across A",
    "collar_condition":"eta=1 near the whole diagonal; proper over the inner output",
    "derived_square":{
        "top_left":"K=R Gamma_H O","top_right":"K=R Gamma_H O",
        "top_arrow":"a_H^Delta","vertical_arrows":"j_H",
        "bottom_left":"O","bottom_right":"O","bottom_arrow":"T_+",
        "equation":"j_H a_H^Delta=T_+ j_H",
        "adjunction_conclusion":"a_H^Delta=R Gamma_H T_+",
        "category":"bounded-below derived category of complex-vector sheaves"
    },
    "proof_locators":["AM.19d","AM.19e","AM.19f","AM.19g","AM.19h"],
    "arbitrary_holonomic_comparison_asserted":False
}
(out/"euler-diagonal-support-exact-data.json").write_text(
    json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Generated the exact full-cube projection, proper homotopy and support-adjunction diagram.")
