"""Reproduce the original CORE figure and its exact mathematical data.

Run: python render_general_core_trace.py
Requirements: Python 3, matplotlib, numpy, sympy.
Outputs are written beside this source. No external data or network is used.
Original renderer/diagram/data: CC0-1.0 to the extent of rights held.
DejaVu Sans font terms are in FONT-LICENSE.txt.
"""
from pathlib import Path
import json
import shutil
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
    "font.size": 13, "axes.titlesize": 17, "axes.labelsize": 13,
    "svg.fonttype": "path", "svg.hashsalt": "oa-flow-core-original-20261006",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.edgecolor": "#526079", "text.color": "#14243c",
    "axes.labelcolor": "#14243c", "xtick.color": "#465570",
    "ytick.color": "#465570", "figure.facecolor": "#f8fafc",
    "axes.facecolor": "#ffffff",
})
BLUE, ORANGE, INK, TEAL = "#2456a6", "#bc4c17", "#14243c", "#13746b"
s = sp.log(2)
mass = (1-sp.exp(-1))/(2*sp.pi)
translated = sp.exp(-s)*mass
H, K = sp.diag(4,1), sp.Matrix([[2,1],[1,2]])
commutator = H*K-K*H
z, w = sp.symbols("z w", nonzero=True)
Ht = sp.diag(w,1)
Kt = sp.Matrix([[z+1,z-1],[z-1,z+1]])/2
c = Kt*Ht.inv()
assert sp.simplify(c*Ht-Kt) == sp.zeros(2)
assert sp.simplify(translated/mass) == sp.Rational(1,2)
r, eps = sp.symbols("r eps", positive=True)
resolvent_limits = {}
for name,D in [("H",H),("K",K)]:
    Q = D*(r*D+eps*sp.eye(2)).inv()
    L = Q.applyfunc(lambda entry: sp.limit(entry,eps,0,dir="+"))
    assert sp.simplify(L-sp.eye(2)/r) == sp.zeros(2)
    resolvent_limits[name]=str(L)

h = sp.diag(1,4)
X = sp.ones(2)
def B(e):
    v=sp.Matrix([(1+e)**(-sp.Rational(1,2)),(4+e)**(-sp.Rational(1,2))])
    return v*v.T
difference = sp.simplify(B(1)-B(4))
assert sp.simplify(difference.det()) == -sp.Rational(1,400)
values = {str(e):sp.trace(h*B(e)) for e in [1,4]}
assert values == {"1":sp.Rational(13,10),"4":sp.Rational(7,10)}
phi = 1/(1+eps)+4/(4+eps)
assert sp.limit(phi,eps,0,dir="+")==2
derivative = sp.diff(phi,eps)
assert derivative == -1/(1+eps)**2-4/(4+eps)**2

fig=plt.figure(figsize=(16,12),dpi=160)
fig.text(.058,.955,"One trace across Fourier charts",fontsize=27,weight="bold",color=INK)
fig.text(.058,.920,
         "Right translation lowers the weighted mass. Ordered chart factors preserve the same trace.",
         fontsize=15,color="#465570")
left_top=[.075,.565,.385,.295]
left_bottom=[.075,.115,.385,.295]
right_top=[.535,.545,.410,.340]
right_bottom=[.580,.115,.365,.290]
xs=np.linspace(-.12,1.90,801)
density=np.exp(-xs)
def scalar_panel(position,lo,hi,color,title,mass_label,interval_label):
    ax=fig.add_axes(position)
    ax.plot(xs,density,color=INK,lw=2.5)
    q=np.linspace(lo,hi,401)
    ax.fill_between(q,0,np.exp(-q),facecolor=color,alpha=.24)
    ax.plot([lo,lo],[0,np.exp(-lo)],color=color,lw=2)
    ax.plot([hi,hi],[0,np.exp(-hi)],color=color,lw=2,ls=(0,(4,3)))
    ax.scatter([lo],[np.exp(-lo)],color=color,s=45,zorder=4)
    ax.scatter([hi],[np.exp(-hi)],facecolors="white",edgecolors=color,s=45,lw=1.6,zorder=4)
    ax.set_xlim(-.12,1.90); ax.set_ylim(0,1.17)
    ax.set_xticks([0,float(s),1,1+float(s)])
    ax.set_xticklabels(["0",r"$\log 2$","1",r"$1+\log 2$"])
    ax.set_yticks([0,.25,.5,.75,1])
    ax.set_xlabel(r"Fourier coordinate $p$",labelpad=7)
    ax.set_ylabel(r"$e^{-p}$",labelpad=9)
    ax.grid(axis="y",alpha=.13,color=INK)
    ax.set_title(title,loc="left",pad=15,weight="bold")
    ax.text(.97,.91,mass_label,transform=ax.transAxes,ha="right",va="top",color=color,fontsize=17)
    ax.text(.97,.71,interval_label,transform=ax.transAxes,ha="right",va="top",color=color,fontsize=14)
    return ax
scalar_panel(left_top,0,1,BLUE,"A   The original interval",
             r"$A=\dfrac{1-e^{-1}}{2\pi}$",r"$f=1_{[0,1)}$")
scalar_panel(left_bottom,float(s),1+float(s),ORANGE,"B   Its support moves to the right",
             r"$e^{-s}A=\dfrac{A}{2}$",r"$s=\log 2$")
fig.text(.075,.489,r"$\theta_s f(p)=f(p-s),\qquad"
         r"\tau(\theta_s f)=e^{-s}\tau(f)$",fontsize=19,color=ORANGE)
fig.text(.075,.458,"Shading uses density relative to dp/(2π); the total trace is infinite.",
         fontsize=11.5,color="#465570")

ax=fig.add_axes(right_top)
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ax.text(0,1.00,"C   Keep the matrix factors in order",fontsize=17,weight="bold",va="top")
def matrix(x0,y0,entries,label):
    ax.text(x0-.025,y0,label+" =",ha="right",va="center",fontsize=18)
    ax.plot([x0+.015,x0,x0,x0+.015],[y0+.085,y0+.085,y0-.085,y0-.085],color=INK,lw=1.5)
    ax.plot([x0+.175,x0+.190,x0+.190,x0+.175],[y0+.085,y0+.085,y0-.085,y0-.085],color=INK,lw=1.5)
    for iy in range(2):
        for ix in range(2):
            ax.text(x0+.057+ix*.077,y0+.039-iy*.078,str(entries[iy][ix]),
                    ha="center",va="center",fontsize=17)
matrix(.130,.805,[[4,0],[0,1]],"H")
matrix(.620,.805,[[2,1],[1,2]],"K")
ax.text(.5,.652,r"$HK-KH\neq0$",ha="center",fontsize=16,color=ORANGE)
ax.add_patch(FancyBboxPatch((.018,.365),.960,.218,boxstyle="round,pad=0.012,rounding_size=.02",
                           facecolor="#eaf1fc",edgecolor="#bdcde7",lw=1))
ax.text(.5,.524,r"$\lambda_K(t)\ \longmapsto\ "
        r"K^{it}H^{-it}\lambda_H(t)$",ha="center",fontsize=19,color=BLUE)
ax.text(.5,.415,r"$(K^{it}H^{-it})(H^{it}e^{itp})"
        r"=K^{it}e^{itp}$",ha="center",fontsize=20,color=BLUE)
ax.text(.5,.266,"Only adjacent inverse factors cancel.",ha="center",fontsize=13,color="#465570")
ax.text(.5,.120,r"$\tau_D(Y)=\int_{\mathbb{R}}e^{-p}\,"
        r"\mathrm{Tr}(Y(p))\,\frac{dp}{2\pi}$",ha="center",fontsize=20,color=TEAL)
ax.text(.5,.025,r"For every $Y\geq0$, including infinite values; $D=H$ or $K$.",
        ha="center",fontsize=12,color="#465570")

ax=fig.add_axes(right_bottom)
es=np.linspace(0,4,801)
ys=1/(1+es)+4/(4+es)
ax.plot(es,ys,color=TEAL,lw=2.8)
ax.scatter([4,1],[.7,1.3],color=TEAL,s=65,zorder=4)
ax.scatter([0],[2],facecolors="white",edgecolors=TEAL,lw=1.7,s=65,zorder=4)
ax.annotate(r"$7/10$",xy=(4,.7),xytext=(3.73,.84),fontsize=14,color=TEAL)
ax.annotate(r"$13/10$",xy=(1,1.3),xytext=(1.65,1.45),fontsize=14,color=TEAL,
            arrowprops={"arrowstyle":"-","color":TEAL})
ax.text(.12,1.95,"limit 2",fontsize=13,color=TEAL,ha="right")
ax.set_xlim(4.2,-.20); ax.set_ylim(.52,2.14)
ax.set_xticks([4,3,2,1,0]);ax.set_yticks([.7,1.0,1.3,1.6,2])
ax.set_xlabel(r"Cutoff parameter $\varepsilon$ decreases $\longrightarrow$",labelpad=9)
ax.set_ylabel(r"$\Phi(B_\varepsilon)$",labelpad=8)
ax.grid(alpha=.13,color=INK)
ax.set_title("D   Scalar increase; no matrix order",loc="left",pad=44,weight="bold")
ax.text(0,1.055,r"$\Phi(B_\varepsilon)=\dfrac{1}{1+\varepsilon}"
        r"+\dfrac{4}{4+\varepsilon}$",transform=ax.transAxes,fontsize=17,color=TEAL)
ax.text(.05,.78,r"$\det(B_1-B_4)=-\dfrac{1}{400}<0$",
        transform=ax.transAxes,ha="left",fontsize=16,color=ORANGE)
ax.text(.05,.635,"The difference has both eigenvalue signs.",
        transform=ax.transAxes,ha="left",fontsize=11.5,color="#465570")
fig.text(.580,.047,r"Here $h=\mathrm{diag}(1,4)$, $X_{ij}=1$, "
         r"$B_\varepsilon=(h+\varepsilon I)^{-1/2}X(h+\varepsilon I)^{-1/2}$.",
         fontsize=11,color="#465570")
fig.text(.058,.022,
         "Exact proof locators: CORE.9.b,h,j · CORE.10.e,g · CORE.3.b. "
         "The cutoff panel is a centralizer model, not a finite-dimensional scaling core.",
         fontsize=10.5,color="#526079")

fig.savefig(OUT/"general-core-trace.png",dpi=160)
fig.savefig(OUT/"general-core-trace.svg",metadata={"Date":None})
plt.close(fig)

data={
 "title":"One trace across Fourier charts",
 "license":"CC0-1.0 to the extent of rights held; DejaVu Sans has separate retained terms",
 "normalization":{"positive_fourier":"lambda_t(p)=exp(i*t*p)","measure":"dp/(2*pi)",
                  "theta":"theta_s f(p)=f(p-s)","generator":"h(p)=exp(p)",
                  "trace_density_relative_to_measure":"exp(-p)"},
 "scalar":{"s_exact":"log(2)","original_interval":"[0,1)","translated_interval":"[log(2),1+log(2))",
           "original_integral_exact":str(mass),"translated_integral_exact":str(translated),
           "ratio_exact":"1/2","original_integral_decimal":float(mass),
           "translated_integral_decimal":float(translated),
           "curve_formula":"exp(-p)","curve_domain":[-.12,1.90],"curve_sample_count":801,
           "fill_samples_per_interval":401,
           "endpoint_marker_convention":"filled left and open right show half-open interval; endpoint choices do not affect the integral"},
 "matrices":{"H":[[4,0],[0,1]],"K":[[2,1],[1,2]],
             "commutator_HK_minus_KH":[[0,3],[-3,0]],
             "H_eigenvalues":[4,1],"K_eigenvalues":[3,1],
             "H_power":"diag(4^(it),1)",
             "K_power":"(1/2)*[[3^(it)+1,3^(it)-1],[3^(it)-1,3^(it)+1]]",
             "cocycle_order":"K^(it) H^(-it)",
             "checked_symbolic_identity":"(K^(it) H^(-it)) H^(it) = K^(it)",
             "symbolic_parameter_substitutions":{"z":"3^(it)","w":"4^(it)"},
             "inverse_density_limit":"D*(r*D+epsilon*I)^(-1) -> r^(-1)*I, D=H,K",
             "whole_positive_cone_trace":"integral exp(-p)*Tr(Y(p))*dp/(2*pi)"},
 "cutoff":{"h":[[1,0],[0,4]],"X":[[1,1],[1,1]],
           "weight":"Phi(Y)=Tr(hY)",
           "B":"v_epsilon*v_epsilon^*, v_epsilon=((1+epsilon)^(-1/2),(4+epsilon)^(-1/2))^T",
           "scalar_formula":"1/(1+epsilon)+4/(4+epsilon)",
           "values_exact":{"epsilon=4":"7/10","epsilon=1":"13/10","epsilon->0+":"2"},
           "difference_determinant_exact":"-1/400",
           "difference_eigenvalues_exact":["(15-sqrt(241))/80","(15+sqrt(241))/80"],
           "scalar_derivative":"-1/(1+epsilon)^2-4/(4+epsilon)^2 < 0",
           "parameter_axis":"decreases from left to right",
           "curve_sample_count":801,"curve_domain":[0,4],
           "scope":"centralizer perturbation model; not a finite-dimensional scaling core"},
 "render":{"size_inches":[16,12],"dpi":160,"png_pixels":[2560,1920],
           "font":"DejaVu Sans","svg_fonttype":"path",
           "axes_bounds":{"scalar_original":left_top,"scalar_translated":left_bottom,
                          "ordered_chart":right_top,"cutoff":right_bottom}},
 "proof_locators":["CORE.9.b","CORE.9.h","CORE.9.j","CORE.10.e","CORE.10.g","CORE.3.b"],
 "symbolic_checks":{"scalar_ratio":True,"ordered_factor_cancellation":True,
                    "both_matrix_resolvent_limits":True,"cutoff_determinant":True,
                    "cutoff_values_and_limit":True,"cutoff_scalar_derivative":True},
 "runtime":{"matplotlib":matplotlib.__version__,"numpy":np.__version__,"sympy":sp.__version__},
}
(OUT/"general-core-trace-data.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
font_license=Path(matplotlib.get_data_path())/"fonts/ttf/LICENSE_DEJAVU"
shutil.copyfile(font_license,OUT/"FONT-LICENSE.txt")
(OUT/"TERMS.md").write_text(
 "# Original figure terms\n\n"
 "The original diagram, mathematical data and renderer are dedicated under CC0-1.0 "
 "to the extent of rights held. No external image, paper figure or book diagram is incorporated.\n\n"
 "The renderer uses DejaVu Sans. Its complete upstream font terms are retained in "
 "FONT-LICENSE.txt; those terms are separate from the original diagram dedication.\n\n"
 "The SVG contains vector glyph paths. Mathematical proof locators and human-source context "
 "are given in the accompanying lesson caption. The exact formulas, plotted coordinates, "
 "normalization and symbolic checks are retained in general-core-trace-data.json and the renderer.\n",
 encoding="utf-8")
print(json.dumps({"rendered_pixels":[2560,1920],"symbolic_checks":data["symbolic_checks"]}))



