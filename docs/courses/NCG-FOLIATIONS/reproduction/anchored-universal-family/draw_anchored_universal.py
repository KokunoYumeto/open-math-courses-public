"""Original CC0 anchored nearest-face/family illustration, AG--LB."""
from pathlib import Path
import argparse
import json
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

HERE = Path(__file__).resolve().parent
FONT = HERE / "fonts"
REG = FontProperties(fname=str(FONT / "DejaVuSans.ttf"))
BOLD = FontProperties(fname=str(FONT / "DejaVuSans-Bold.ttf"))
INK = "#183348"; BLUE = "#156296"; GREEN = "#08785d"

def text_at(ax, x, y, value, size=12, bold=False, **kw):
    return ax.text(x, y, value, fontsize=size,
                   color=kw.pop("color", INK),
                   fontproperties=BOLD if bold else REG, **kw)

def arrow(ax, p, q, color=BLUE):
    ax.annotate("", xy=q, xytext=p, arrowprops={
        "arrowstyle":"->", "lw":2.3, "color":color})

def render(out):
    out.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({
        "svg.hashsalt":"anchored-universal-groupoid-AG-AF-OC-DI-LB-v1",
        "svg.fonttype":"path"})
    fig = plt.figure(figsize=(16, 10), facecolor="white")
    fig.text(.04,.958,"Anchored proper algebra and a continuous ordinary calibrated family",
             fontsize=22,fontproperties=BOLD,color=INK)
    left=fig.add_axes([.04,.51,.44,.38]);left.axis("off")
    left.set_xlim(0,1);left.set_ylim(0,1)
    text_at(left,0,.965,"AG.2–AG.3  Actual source and range fibres",17,True)
    left.scatter([.14,.83],[.73,.73],s=90,color=INK)
    arrow(left,(.19,.73),(.78,.73))
    text_at(left,.48,.80,"k : x → y",15,True,ha="center")
    text_at(left,.14,.62,"x = s(k)",12,ha="center")
    text_at(left,.83,.62,"y = r(k)",12,ha="center")
    text_at(left,.14,.43,"(h,n) ∈ Gˣ × N₀",14,True,ha="center")
    text_at(left,.83,.43,"(kh,n) ∈ Gʸ × N₀",14,True,ha="center")
    arrow(left,(.35,.43),(.62,.43),GREEN)
    text_at(left,.48,.51,"Lk",14,True,ha="center")
    text_at(left,.03,.28,"h : a → x;  kh : a → y.  Composition requires r(h) = s(k).",12)
    text_at(left,.03,.17,"Distinct isotropy arrows remain distinct vertices.",13,True)
    text_at(left,.03,.065,"Exterior line degree = |σ| − 1; the one-form ξμ is even.",12)

    right=fig.add_axes([.54,.50,.42,.39])
    right.set_aspect("equal");right.set_xlim(-5.1,1.5);right.set_ylim(-2.1,1.7)
    right.set_xticks([]);right.set_yticks([])
    for s in right.spines.values():s.set_visible(False)
    text_at(right,-5.05,1.40,"AF.7  An exact finite-plane face test",16,True)
    b1=np.array([-1,1,0])/math.sqrt(2)
    b2=np.array([-1,-1,2])/math.sqrt(6)
    centre=np.ones(3)/3
    project=lambda v:np.array([np.dot(v-centre,b1),np.dot(v-centre,b2)])
    vertices=np.array([project(v) for v in np.eye(3)])
    right.fill(vertices[:,0],vertices[:,1],facecolor="#e6eef5",edgecolor=BLUE,lw=1.7)
    right.plot(vertices[:2,0],vertices[:2,1],color=GREEN,lw=4)
    for i,v in enumerate(vertices):
        right.scatter([v[0]],[v[1]],s=50,color=INK)
        text_at(right,v[0]+(.10 if i==1 else -.28),v[1]-.22,f"e{i}",12,True)
    v=np.array([3.2,-2.2,0.]);w=np.array([3.,-2.12,.12])
    pv=project(v);pw=project(w)
    right.add_patch(Circle(pv,1,facecolor="#edf8f2",edgecolor=GREEN,lw=1.7))
    right.scatter([pv[0],pw[0]],[pv[1],pw[1]],s=50,c=[GREEN,BLUE])
    text_at(right,pv[0]-.65,pv[1]-.53,"v = (3.2, −2.2, 0)",11)
    text_at(right,pw[0]-.16,pw[1]+.38,"w = (3, −2.12, .12)",11)
    arrow(right,tuple(pw),tuple(vertices[0]),BLUE)
    text_at(right,-2.2,.86,"qΣ(w) = qF(w) = e0",12,True)
    text_at(right,-5.05,-1.98,"Σ = {e0,e1,e2}; F = {e0,e1}. Orthogonal view is isometric on their affine plane.",10.5)
    distance=float(np.linalg.norm(w-v))
    text_at(right,-5.05,-1.72,f"‖w − v‖ = √.0608 ≈ {distance:.4f} < 1;  v0 = 3.2 > 3 > 1 + √2.",11,True)
    text_at(right,-5.05,1.14,"Green disk: radius-one plane section of the Bott-defect ball.",10.5)

    bottom=fig.add_axes([.04,.105,.92,.30]);bottom.axis("off")
    bottom.set_xlim(0,1);bottom.set_ylim(0,1)
    text_at(bottom,0,.945,"OC.2–OC.3  A whole-base ordinary identity with both anchors retained",17,True)
    for x,label in [(.12,"C₀(MG)"),(.49,"PM = C₀(MG) ⊗T P"),(.88,"C₀(MG)")]:
        bottom.add_patch(FancyBboxPatch((x-.105,.51),.21,.15,
                         boxstyle="round,pad=.01",facecolor="#edf4f9",edgecolor=BLUE))
        text_at(bottom,x,.585,label,14,True,ha="center",va="center")
    arrow(bottom,(.23,.585),(.375,.585),GREEN)
    arrow(bottom,(.605,.585),(.765,.585),GREEN)
    text_at(bottom,.295,.735,"ForG(θM)",13,True,ha="center")
    text_at(bottom,.685,.735,"pM* D₀",13,True,ha="center")
    text_at(bottom,.49,.375,"ForG(θM) ⊗PM pM*D₀ = 1C₀(MG)  in ordinary anchored KK",
            14,True,ha="center")
    text_at(bottom,.02,.165,"DI.6–DI.8 supply q:E₁→Q, its anchored ordinary cpc section, and the equivariant cone kernel.",12)
    text_at(bottom,.02,.01,"LB.1 remains separate: q* must be proved bijective before zP or an equivariant D can be asserted.",12,True)
    fig.text(.04,.042,"Original CC0 diagram. Geometry AG.2–AG.6; bound AF.6–AF.7; shifted cycle AF.8–AF.13; calibration OC.1–OC.6.",
             fontsize=11,fontproperties=REG,color=INK)
    fig.text(.04,.022,"Human-source mechanism: Jean-Louis Tu, The Gamma Element for Groups which Admit a Uniform Embedding into Hilbert Space (2004), pp.275–281.",
             fontsize=10,fontproperties=REG,color=INK)
    notice=(HERE/"FONT-NOTICE.txt").read_text(encoding="utf-8")
    fig.savefig(out/"anchored-nearest-face-family.png",dpi=200,metadata={
        "Software":"Matplotlib; original CC0 diagram","Description":notice})
    fig.savefig(out/"anchored-nearest-face-family.svg",metadata={
        "Date":None,"Creator":"Original CC0 anchored nearest-face family","Description":notice})
    plt.close(fig)
    data={
        "proof_locators":["AG.2","AG.3","AG.6","AF.1","AF.6","AF.7","AF.8",
                          "AF.10","AF.11","AF.12","OC.2","OC.3","DI.6","DI.7","DI.8","LB.1"],
        "arrow_types":{"k":"x->y","h":"a->x","kh":"a->y","condition":"r(h)=s(k)"},
        "vertices":{"source":"G^x x N0","range":"G^y x N0",
                    "action":"(h,n)->(kh,n)","isotropy_labels_identified":False},
        "finite_plane_sample":{"Sigma":[0,1,2],"F":[0,1],
            "v":v.tolist(),"w":w.tolist(),"squared_distance":float(np.dot(w-v,w-v)),
            "distance":distance,"projection":[1,0,0],
            "plane_projection_basis":[b1.tolist(),b2.tolist()],
            "view":"orthogonal isometry on affine simplex plane","shown_disk_radius":1},
        "grading":{"simplex_line":"|sigma|-1","deficient_one_form":"even"},
        "family_product":"For_G(theta_M) tensor_{P_M} p_M^*D0 = 1_C0(M_G) in ordinary anchored KK",
        "not_asserted":["equivariant z_P","equivariant D","equivariant dual eta",
                        "scalar evaluation from M_G","compact anchored coarse-kernel route",
                        "FOL055 closure"]}
    (out/"anchored-nearest-face-data.json").write_text(
        json.dumps(data,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-dir",type=Path,default=HERE/"figures")
    render(parser.parse_args().output_dir.resolve())
