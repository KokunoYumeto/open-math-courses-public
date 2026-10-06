"""Exact scalar partition and eigenunitary comparison for OA-FLOW-L19.

Original code, data and diagram: CC0-1.0 to the extent of rights held.
Run with Python 3, Matplotlib, SymPy and Pillow:
    python render_trace_scaling_eigenunitaries.py
All outputs are written beside this source. Font terms are retained separately.
"""
from pathlib import Path
import hashlib
import json
import shutil

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
from PIL import Image
import sympy as sp

HERE = Path(__file__).resolve().parent
T, m = sp.Integer(1), 2
selected = [{"n":n,"left":-n*T,"right":(1-n)*T}
            for n in range(m,-m-1,-1)]
assert [x["left"] for x in selected] == list(range(-2,3))
assert [x["right"] for x in selected] == list(range(-1,4))
assert all(selected[i]["right"]==selected[i+1]["left"] for i in range(4))
length = sum(x["right"]-x["left"] for x in selected)
assert length == (2*m+1)*T == 5
r0, s0 = sp.Rational(1,4), sp.Rational(1,2)
assert sp.floor(r0) == sp.floor(r0+s0) == 0
assert sp.floor(r0+1)-sp.floor(r0) == 1
assert (r0+s0)-r0 == s0

# Exact matrix checks for Section 6, retained in the reproducible data.
r,s=sp.symbols("r s",real=True)
K=sp.diag(1,-1)
B=sp.Matrix([[2,1],[1,2]])
Pplus=sp.Matrix([[1,1],[1,1]])/2
Pminus=sp.eye(2)-Pplus
def W(t): return sp.diag(sp.exp(sp.I*t),sp.exp(-sp.I*t))
def A(t): return W(-t)*B*W(t)
def h(t): return sp.exp(-t)*A(t)
assert B == 3*Pplus+Pminus
assert Pplus**2==Pplus and Pminus**2==Pminus
assert Pplus*Pminus==sp.zeros(2)
assert sp.simplify(A(r+s)-W(-s)*A(r)*W(s)) == sp.zeros(2)
assert sp.simplify(W(s)*h(r+s)*W(-s)-sp.exp(-s)*h(r)) == sp.zeros(2)
assert A(r)*sp.diag(1,0)-sp.diag(1,0)*A(r) != sp.zeros(2)
def matrix(m): return [[str(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]

data={
    "license":"CC0-1.0 original code/data/diagram; font terms separate",
    "figure_kind":"Exact translation partition and exact real-exponent graphs",
    "coordinate":"r",
    "action":"theta_s(f)(r)=f(r+s)",
    "trace":"tau(f)=integral f(r) exp(r) dr",
    "scalar_density":"h(r)=exp(-r)",
    "T":1,"m":2,
    "partition_formula":"q_n=1_[-nT,(1-n)T)",
    "visible_intervals":[{"q_index":-j,"left":j,"right":j+1,
                         "left_endpoint":"included","right_endpoint":"excluded",
                         "in_P2":(-2<=j<3)} for j in range(-3,4)],
    "P2":{"left":-2,"right":3,"right_endpoint":"excluded",
          "norm":1,"positive_integral":5},
    "support_translation":{"start_interval":[0,1],"image_interval":[-1,0],
                           "time":1,"direction":"left"},
    "continuous_unitary":"v_t(r)=exp(i*t*r)",
    "staircase_unitary":"w_t(r)=exp(i*T*t*floor(r/T))",
    "graphed_real_exponents":{"t":1,"continuous":"r","staircase":"floor(r)"},
    "half_step_check":{
        "r":"1/4","s":"1/2","t":1,"r_plus_s":"3/4",
        "continuous_exponents":["1/4","3/4"],
        "staircase_exponents":[0,0],
        "continuous_ratio":"exp(i/2)",
        "staircase_ratio":"1",
        "required_ratio":"exp(i/2)",
        "failure_set":"0<r<1/2 (positive Lebesgue measure)"
    },
    "matrix_model":{
        "K":matrix(K),"B":matrix(B),"B_eigenvalues":[1,3],
        "P_plus":matrix(Pplus),"P_minus":matrix(Pminus),
        "A(r)":matrix(A(r)),
        "h_covariance_checked":True,
        "A_transport_checked":True,
        "noncentrality_checked":True
    },
    "proof_locators":["OA-FLOW-L19.md#l19-5","L19.5.f","L19.5.g",
                      "L19.5.h","OA-FLOW-L19.md#l19-7","L19.7.c","L19.7.d"],
    "checks":{"exact_partition_endpoints":True,"sharp_bound":True,
              "integer_step":True,"half_step_failure":True,
              "matrix_covariance":True,"matrix_nonscalar_density":True}
}

plt.rcParams.update({
    "font.family":"DejaVu Sans","mathtext.fontset":"dejavusans",
    "font.size":13,"svg.fonttype":"path",
    "svg.hashsalt":"oa-flow-l19-trace-scaling-eigenunitaries-v1"
})
INK="#142c3b"; MUTED="#546b78"; BLUE="#007fa7"; ORANGE="#bf5a2c"
LIGHT="#d7edf4"; BORDER="#d0dbe1"
fig=plt.figure(figsize=(12,10),dpi=200,facecolor="#f5f7f9")
base=fig.add_axes([0,0,1,1]); base.set_axis_off()
def txt(x,y,t,size=14,color=INK,**kw):
    return fig.text(x,y,t,fontsize=size,color=color,va="center",**kw)
def card(x,y,w,h):
    base.add_patch(FancyBboxPatch((x,y),w,h,transform=base.transAxes,
        boxstyle="round,pad=0.01,rounding_size=0.015",
        facecolor="white",edgecolor=BORDER,linewidth=1))
txt(.06,.956,"A sharp integration bound and the missing half-step",23,
    fontweight="bold")
txt(.06,.907,r"$\theta_s(f)(r)=f(r+s)$,   "
    r"$\tau(f)=\int f(r)e^r\,dr$,   $h(r)=e^{-r}$",16,MUTED)
card(.045,.56,.91,.29)
txt(.065,.818,"A   AN EXACT TRANSLATION PARTITION",14,fontweight="bold")
txt(.934,.818,r"$T=1,\quad m=2$",14,MUTED,ha="right")
ax=fig.add_axes([.08,.611,.84,.164],facecolor="white")
ax.set_xlim(-3.35,4.35);ax.set_ylim(-.18,1.4)
ax.set_yticks([])
for side in ["left","right","top"]:ax.spines[side].set_visible(False)
ax.spines["bottom"].set_position(("data",.02))
ax.spines["bottom"].set_color("#9cabb4")
ax.set_xticks(range(-3,5));ax.tick_params(axis="x",labelsize=12,length=3,pad=5)
for j in range(-3,4):
    included=-2<=j<3
    fill=("#80c3d6" if j==0 else LIGHT) if included else "#edf0f3"
    ax.add_patch(Rectangle((j,.15),1,.49,facecolor=fill,
                          edgecolor="white",linewidth=2))
    ax.text(j+.5,.395,rf"$q_{{{-j}}}$",ha="center",va="center",
            color=INK if included else "#7d909c",fontsize=17)
ax.add_patch(Rectangle((-2,.15),5,.49,facecolor="none",edgecolor=BLUE,linewidth=1.7))
ax.annotate("",xy=(-.5,.95),xytext=(.5,.95),
            arrowprops={"arrowstyle":"-|>","color":BLUE,"lw":1.8})
ax.text(0,1.235,r"$\theta_1(p)=q_1$",ha="center",fontsize=15,color=BLUE)
ax.text(-3.22,.39,r"$\cdots$",ha="center",fontsize=17,color=MUTED)
ax.text(4.18,.39,r"$\cdots$",ha="center",fontsize=17,color=MUTED)
txt(.5,.585,r"$P_2=1_{[-2,3)},\qquad \|P_2\|=1,\qquad E(P_2)=5\cdot1$",
    18,ha="center")

card(.045,.115,.91,.40)
txt(.065,.486,"B   REAL EXPONENTS BEFORE APPLYING "+r"$x\mapsto e^{ix}$",
    14,fontweight="bold")
ax2=fig.add_axes([.093,.191,.47,.239],facecolor="white")
ax2.set_xlim(-1.2,2.2);ax2.set_ylim(-1.4,2.35)
ax2.axvspan(0,.5,color="#eef2f5",zorder=0)
ax2.set_xticks([-1,0,1,2]);ax2.set_yticks([-1,0,1,2])
ax2.grid(color="#dfe6eb",linewidth=.7)
for side in ["top","right"]:ax2.spines[side].set_visible(False)
for side in ["left","bottom"]:ax2.spines[side].set_color("#a7b6bf")
ax2.plot([-1.2,2.2],[-1.2,2.2],color=BLUE,lw=2.6,label=r"$r$")
for j in range(-2,3):
    ax2.plot([j,j+1],[j,j],color=ORANGE,lw=2.5,
             label=r"$\lfloor r\rfloor$" if j==0 else None)
    ax2.plot(j,j,"o",color=ORANGE,ms=6,zorder=5)
    ax2.plot(j+1,j,"o",mfc="white",mec=ORANGE,ms=6,zorder=5)
for rr in [float(r0),float(r0+s0)]:
    ax2.plot([rr,rr],[0,rr],ls=":",color="#7a8e9b",lw=1.1)
    ax2.plot(rr,rr,"o",color=BLUE,ms=5,zorder=6)
    ax2.plot(rr,0,"o",color=ORANGE,ms=5,zorder=6)
ax2.text(1.025,-.025,r"$r$",transform=ax2.transAxes,fontsize=14,color=INK)
ax2.set_ylabel("real exponent",fontsize=11,labelpad=5)
ax2.legend(loc="upper left",frameon=False,fontsize=13)

txt(.622,.414,r"$t=1,\quad r=\frac{1}{4},\quad s=\frac{1}{2}$",16)
txt(.622,.355,"Continuous coordinate",13,BLUE,fontweight="bold")
txt(.622,.318,r"$v_1(r)=e^{i/4},\quad v_1(r+s)=e^{3i/4}$",14)
txt(.622,.280,r"$v_1(r+s)/v_1(r)=e^{i/2}$",15,BLUE)
txt(.622,.229,"The staircase does not jump",13,ORANGE,fontweight="bold")
txt(.622,.192,r"$w_1(r)=w_1(r+s)=1$",15)
txt(.622,.154,r"$w_1(r+s)/w_1(r)=1\ne e^{i/2}$",15,ORANGE)
txt(.095,.146,"Integer shifts work; the half-step fails on "+r"$0<r<1/2$"+".",
    11,MUTED)
txt(.06,.073,"Half-open intervals and phase values are exact; only the displayed window is finite.",
    12,MUTED)
txt(.06,.037,"OA-FLOW-L19, Sections 5 and 7 • original diagram and data CC0 • font terms retained",
    10,MUTED)

png=HERE/"trace-scaling-eigenunitaries.png"
svg=HERE/"trace-scaling-eigenunitaries.svg"
fig.savefig(png,dpi=200,metadata={
    "Software":"Matplotlib",
    "Description":"Exact translation partition, sharp integration bound and half-step eigenunitary test"})
fig.savefig(svg,metadata={
    "Date":None,"Creator":"Original OA-FLOW mathematical illustration",
    "Description":"Exact translation partition, sharp integration bound and half-step eigenunitary test"})
plt.close(fig)
data["native_png_pixels"]=list(Image.open(png).size)
(HERE/"trace-scaling-eigenunitaries-data.json").write_text(
    json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
font_root=Path(matplotlib.get_data_path())/"fonts"/"ttf"
license_path=font_root/"LICENSE_DEJAVU"
if not license_path.is_file():
    raise FileNotFoundError("Installed DejaVu font license not found")
shutil.copyfile(license_path,HERE/"FONT-LICENSE.txt")
print(json.dumps({
    "png":str(png),"svg":str(svg),"native_pixels":data["native_png_pixels"],
    "exact_checks":data["checks"],
    "font_terms_source":str(license_path),
    "data_sha256":hashlib.sha256((HERE/"trace-scaling-eigenunitaries-data.json").read_bytes()).hexdigest()
},indent=2))


