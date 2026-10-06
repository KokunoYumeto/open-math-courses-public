"""Original reproducible L18 model figure; no external data/network.
Run: python render_trace_scaling_central_corners.py
Needs Python3, matplotlib, numpy, sympy. Original diagram/data/renderer:
CC0-1.0 to extent of rights held; DejaVu Sans terms in FONT-LICENSE.txt.
"""
from pathlib import Path
import json,shutil
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,FancyBboxPatch
OUT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
 "font.size":12,"axes.titlesize":17,"axes.labelsize":14,"svg.fonttype":"path",
 "svg.hashsalt":"oa-flow-l18-original-20261006","figure.facecolor":"#f8fafc",
 "axes.facecolor":"white","text.color":"#17263e","axes.labelcolor":"#17263e",
 "axes.edgecolor":"#57677e","xtick.color":"#57677e","ytick.color":"#57677e",
 "axes.spines.top":False,"axes.spines.right":False})
BLUE,ORANGE,INK,GREY="#2458a6","#ba4c19","#17263e","#58697f"
D=sp.Matrix([[-1,1],[0,1]])
assert D.det()==-1 and D*D==sp.eye(2)
rect=[(0,-1),(1,-1),(1,1),(0,1)]
shifted=[(x-1,y) for x,y in rect]
original=[tuple(D*sp.Matrix(q)) for q in rect]
translated=[(ss+1,rr) for ss,rr in original]
assert [tuple(D*sp.Matrix(q)) for q in translated]==shifted
def area(vertices):
    return sp.Rational(1,2)*abs(sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1]
                   -vertices[(i+1)%len(vertices)][0]*vertices[i][1]
                   for i in range(len(vertices))))
assert area(original)==area(translated)==area(rect)==area(shifted)==2
ss,rr,t,x,y=sp.symbols("s r t x y",real=True)
assert sp.simplify((rr-(ss-t)).subs({ss:y-x,rr:y}, simultaneous=True)-(x+t))==0
assert tuple(D*sp.Matrix([sp.Rational(-1,2),0]))==(sp.Rational(1,2),0)
assert tuple(D*sp.Matrix([sp.Rational(1,2),0]))==(sp.Rational(-1,2),0)
fig=plt.figure(figsize=(15,11),dpi=160)
fig.text(.060,.953,"The active coordinate and the corner unit",fontsize=25,weight="bold")
fig.text(.060,.916,
 "A measure-preserving shear exposes the translation factor. A supported map selects one central summand.",
 fontsize=13.5,color=GREY)
ax1=fig.add_axes([.075,.585,.380,.270])
ax2=fig.add_axes([.585,.585,.340,.270])
def panel(ax,first,second,xlabel,ylabel,title,centers,label):
    a=np.array(first,dtype=float); b=np.array(second,dtype=float)
    for poly,col in [(a,BLUE),(b,ORANGE)]:
        ax.add_patch(Polygon(poly,closed=True,facecolor=col,edgecolor=col,alpha=.20,lw=2))
        ax.plot(*np.vstack((poly,poly[0])).T,color=col,lw=1.6)
    for point,col in zip(centers,[BLUE,ORANGE]):
        ax.scatter([point[0]],[point[1]],color=col,s=65,zorder=5)
    ax.annotate("",xy=centers[1],xytext=centers[0],
       arrowprops={"arrowstyle":"->","color":INK,"lw":2.0,"shrinkA":7,"shrinkB":7})
    ax.text((centers[0][0]+centers[1][0])/2,.23,label,ha="center",fontsize=12)
    ax.set_ylim(-1.50,1.50); ax.set_yticks([-1,0,1])
    ax.set_xlabel(xlabel,labelpad=6);ax.set_ylabel(ylabel,labelpad=7)
    ax.set_title(title,loc="left",weight="bold",pad=14);ax.grid(alpha=.16,color=INK)
panel(ax1,original,translated,r"group coordinate $s$",r"coefficient coordinate $r$",
 "A   Regular coordinates",((-0.5,0),(.5,0)),r"support $+1$ in $s$")
ax1.set_xlim(-2.45,2.45);ax1.set_xticks([-2,-1,0,1,2])
ax1.text(-1.35,-.65,r"$\xi$",color=BLUE,fontsize=19)
ax1.text(-.25,-.65,r"$u_1\xi$",color=ORANGE,fontsize=18)
panel(ax2,rect,shifted,r"active coordinate $x=r-s$",r"multiplicity coordinate $y=r$",
 "B   The same vectors after J",((.5,0),(-.5,0)),r"support $-1$ in $x$")
ax2.set_xlim(-1.65,1.65);ax2.set_xticks([-1,0,1])
ax2.text(.50,-.65,r"$J\xi$",color=BLUE,fontsize=19,ha="center")
ax2.text(-.50,-.65,r"$Ju_1\xi$",color=ORANGE,fontsize=18,ha="center")
fig.text(.5,.518,r"$[J\xi](x,y)=\xi(y-x,y),\qquad [Ju_tJ^*\eta](x,y)=\eta(x+t,y)$",
 ha="center",fontsize=19)
fig.text(.5,.485,
 r"Blue: $0\leq r-s<1,\ -1\leq r<1$.  Orange: support of $u_1\xi$.  Both windows have area 2.",
 ha="center",fontsize=12.5,color=GREY)
fig.text(.5,.450,r"$JMJ^*=B(L^2(\mathbb{R}_x))\otimes1_{L^2(\mathbb{R}_y)}$",
 ha="center",fontsize=20,color=BLUE)
ax=fig.add_axes([.055,.090,.890,.337])
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis("off")
ax.text(0,.985,"C   The unit chooses a direct summand",fontsize=17,weight="bold",va="top")
ax.text(.27,.842,r"$\iota_1(f)=(f,0),\quad \iota_1(1)=e_1$",ha="center",fontsize=18,color=BLUE)
ax.text(.735,.842,"The second copy has its own unit.",ha="center",fontsize=13,color=GREY)
def box(x0,y0,w,h,face,edge):
    ax.add_patch(FancyBboxPatch((x0,y0),w,h,boxstyle="round,pad=0.007,rounding_size=.015",
                               facecolor=face,edgecolor=edge,lw=1.5))
for x0,xc,unit,col,face in [(.075,.27,"e_1",BLUE,"#e9f0fb"),(.540,.735,"e_2",GREY,"#eef1f5")]:
    box(x0,.535,.390,.220,face,col)
    ax.text(xc,.657,r"$L^\infty(\mathbb{R})$",ha="center",va="center",fontsize=23,color=col)
    ax.text(xc,.567,r"corner unit $"+unit+"$",ha="center",va="center",fontsize=12,color=col)
    ax.annotate("",xy=(xc,.314),xytext=(xc,.511),
                arrowprops={"arrowstyle":"->","color":col,"lw":2})
    ax.text(xc+.020,.405,r"$\rtimes_\theta\mathbb{R}$",va="center",fontsize=15,color=col)
    box(x0,.080,.390,.220,face,col)
    ax.text(xc,.213,r"$B(L^2(\mathbb{R}))$",ha="center",va="center",fontsize=22,color=col)
    ax.text(xc,.122,"semifinite, properly infinite factor",ha="center",va="center",fontsize=12,color=col)
ax.text(.015,.653,r"$N^{(2)}$",ha="center",va="center",fontsize=18)
ax.text(.015,.203,r"$M^{(2)}$",ha="center",va="center",fontsize=18)
ax.text(.502,.653,r"$\oplus$",ha="center",va="center",fontsize=22)
ax.text(.502,.203,r"$\oplus$",ha="center",va="center",fontsize=22)
fig.text(.5,.069,
 r"The whole algebra is semifinite and properly infinite; $Z(M^{(2)})=\mathbb{C}e_1\oplus\mathbb{C}e_2$.",
 ha="center",fontsize=14)
fig.text(.060,.030,
 "Proof locators: L18.9.c–g (coordinates and multiplicity), L18.9.h–j (corner model), L18.10.g (general corner conclusion).",
 fontsize=10.5,color=GREY)
fig.savefig(OUT/"trace-scaling-central-corners.png",dpi=160)
fig.savefig(OUT/"trace-scaling-central-corners.svg",metadata={"Date":None})
plt.close(fig)
def ints(vs):return [[int(q) for q in v] for v in vs]
data={
 "title":"The active coordinate and the corner unit",
 "license":"CC0-1.0 to the extent of rights held; font terms retained separately",
 "model":{"N":"L-infinity(R,dr)","action":"theta_s f(r)=f(r+s)",
          "trace":"tau(f)=integral exp(r)*f(r)*dr","scaling":"tau theta_s=exp(-s)tau"},
 "coordinates":{"map":"x=r-s, y=r","inverse":"s=y-x, r=y","matrix":[[-1,1],[0,1]],
                "determinant_exact":-1,"absolute_determinant_exact":1,
                "unitary":"J xi(x,y)=xi(y-x,y)","inverse_unitary":"J* eta(s,r)=eta(r-s,r)",
                "coefficient":"J pi(f) J*=M_f tensor 1",
                "group_operator":"J u_t J* eta(x,y)=eta(x+t,y)"},
 "support_window":{"test_vector":"1_[0,1)(r-s)*1_[-1,1)(r)",
                   "time_exact":1,"area_exact":2,
                   "original_sr_polygon_vertices":ints(original),
                   "translated_sr_polygon_vertices":ints(translated),
                   "original_xy_polygon_vertices":ints(rect),
                   "translated_xy_polygon_vertices":ints(shifted),
                   "support_centers_sr":[["-1/2","0"],["1/2","0"]],
                   "support_centers_xy":[["1/2","0"],["-1/2","0"]],
                   "support_motion":"u_1 moves support by +1 in s and -1 in x; y unchanged",
                   "argument_motion":"u_1 evaluates at s-1; J u_1 J* evaluates at x+1",
                   "boundaries":"Half-open sets are specified by the test-vector formula. Polygon outlines draw boundaries of Lebesgue measure zero.",
                   "scope":"finite window of one test vector; full representation on R^2"},
 "operator_algebra":{"regular_image":"B(L2(R_x)) tensor 1_L2(R_y)",
                     "multiplicity_space":"L2(R_y)","abstract_algebra":"B(L2(R))",
                     "normal_inverse":"compression by zeta -> zeta tensor eta, for a fixed unit vector eta"},
 "direct_sum":{"N":"L-infinity(R) direct-sum L-infinity(R)",
               "M":"B(L2(R)) direct-sum B(L2(R))",
               "map":"iota_1(f)=(f,0)","map_unit":"e_1=(1,0)","complement_unit":"e_2=(0,1)",
               "detected_corner":"M e_1","center":"C e_1 direct-sum C e_2",
               "each_corner_type":"I_infinity factor, semifinite and properly infinite",
               "whole_type":"semifinite, properly infinite, nonfactor",
               "qualification":"This complement is semifinite by its own copy; one map alone does not determine a general complementary corner."},
 "proof_locators":["L18.9.c","L18.9.d","L18.9.e","L18.9.f","L18.9.g","L18.9.h","L18.9.i","L18.9.j","L18.10.g"],
 "symbolic_checks":{"coordinate_inverse":True,"absolute_determinant":True,
                    "support_polygons_and_areas":True,"group_argument_sign":True,"support_center_signs":True},
 "render":{"inches":[15,11],"dpi":160,"png_pixels":[2400,1760],"font":"DejaVu Sans","svg_fonttype":"path"},
 "runtime":{"matplotlib":matplotlib.__version__,"numpy":np.__version__,"sympy":sp.__version__}}
(OUT/"trace-scaling-central-corners-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
shutil.copyfile(Path(matplotlib.get_data_path())/"fonts/ttf/LICENSE_DEJAVU",OUT/"FONT-LICENSE.txt")
(OUT/"TERMS.md").write_text(
 "# Original figure terms\n\nThe original diagram, exact data and renderer are dedicated under "
 "CC0-1.0 to the extent of rights held. No external images or source diagrams are incorporated.\n\n"
 "DejaVu Sans is used under its separately retained full upstream terms in FONT-LICENSE.txt. "
 "The SVG uses vector glyph paths. Mathematical proof locators and human-source context "
 "are supplied by the accompanying lesson caption.\n",encoding="utf-8")
print(json.dumps({"pixels":[2400,1760],"checks":data["symbolic_checks"]}))


