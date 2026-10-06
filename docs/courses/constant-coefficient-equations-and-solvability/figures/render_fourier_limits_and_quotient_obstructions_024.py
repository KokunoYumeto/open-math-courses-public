"""Reproduce the exact envelope and punctured-open-set compatibility figure."""
import json
import math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
STEM="fourier-limits-and-quotient-obstructions-024"
a=math.pi/12
def root_function(h):return (1+h)/math.tan((a+h)/2)-6
lo,hi=0.,1.
assert root_function(lo)>0 and root_function(hi)<0
for _ in range(80):
    mid=(lo+hi)/2
    if root_function(mid)>0:lo=mid
    else:hi=mid
hstar=(lo+hi)/2
def envelope(h):return 2*np.abs(np.sin((a+h)/2))/(1+np.abs(h))**3

plt.rcParams.update({"font.family":"DejaVu Sans","font.size":15,
    "svg.fonttype":"none","svg.hashsalt":"AN02-GL-024",
    "axes.titleweight":"bold","axes.spines.top":False,"axes.spines.right":False})
fig,(left,right)=plt.subplots(1,2,figsize=(20,10),dpi=120)
fig.subplots_adjust(left=.065,right=.96,bottom=.22,top=.78,wspace=.25)
fig.suptitle("Choose the frequency. Check the quotient pairing.",fontsize=27,y=.966,weight="bold")
fig.text(.5,.915,"Exact Fourier geometry and an exact removed-point example",ha="center",fontsize=18)
h=np.linspace(-1.5,2.3,1801)
left.plot(h,envelope(h),color="#216b93",lw=3)
left.axvline(0,color="#697985",lw=1.5,ls="--")
left.axvline(hstar,color="#b46026",lw=1.7,ls=":")
left.scatter([hstar],[float(envelope(hstar))],s=95,color="#b46026",zorder=5)
left.annotate("Maximizing center\n"+rf"$h_* \approx {hstar:.5f}$",
    xy=(hstar,float(envelope(hstar))),xytext=(.64,.274),
    arrowprops={"arrowstyle":"->","color":"#9b4f20","lw":1.5},fontsize=16,color="#9b4f20")
left.text(-1.4,.308,r"$u=\delta_0-\delta_1$,  $\eta_0=\pi/12$,  $N=3$",fontsize=16)
left.text(-1.4,.283,r"$2|\sin((\eta_0+h)/2)|(1+|h|)^{-3}$",fontsize=16)
left.text(.32,.155,"Move the maximum to zero.\nDivide by the complex Fourier value.\nThe normalized value at zero is exactly 1.",
    fontsize=15,bbox={"facecolor":"#f5f7f8","edgecolor":"none","alpha":.95})
left.text(-1.36,.017,"Original center: h = 0",fontsize=13,color="#546672")
left.set(xlim=(-1.5,2.3),ylim=(0,.335),xlabel=r"relative frequency $h=\xi-\eta_j$",ylabel="weighted Fourier modulus")
left.set_title("GL4-GL7: a nonzero singularity limit",fontsize=18,pad=20)
left.grid(alpha=.16)

x=np.linspace(-2.2,2.2,1801)
bump=np.zeros_like(x)
inside=np.abs(x)<1
bump[inside]=np.exp(1-1/(1-x[inside]**2))
right.plot(x,bump,color="#427b56",lw=3)
right.scatter([0],[1],s=85,color="#427b56",zorder=6)
right.annotate(r"$\langle\delta_0,\phi\rangle=\phi(0)=1$",xy=(0,1),xytext=(.43,.84),
    arrowprops={"arrowstyle":"->","color":"#764220","lw":1.5},fontsize=16,color="#764220")
right.annotate("",xy=(0,.97),xytext=(0,.10),arrowprops={"arrowstyle":"-|>","color":"#b46026","lw":2.5})
right.text(-.65,.49,r"action of $\delta_0$",fontsize=14,color="#9b4f20",rotation=90)
right.plot([-2,-.035],[-.12,-.12],lw=4,color="#216b93")
right.plot([.035,2],[-.12,-.12],lw=4,color="#216b93")
right.scatter([-2,0,2],[-.12,-.12,-.12],facecolor="white",edgecolor="#216b93",s=70,lw=2,zorder=6)
right.text(-1.83,-.27,r"$Y=(-2,2)\setminus\{0\}$",fontsize=17,color="#216b93")
right.text(-1.97,1.16,r"$\mathrm{supp}\,\phi=[-1,1]\subset\overline{Y}=[-2,2]$",fontsize=16)
right.text(-1.97,1.045,r"$\phi(x)=e^{1-(1-x^2)^{-1}}$ for $|x|<1$;  zero outside",fontsize=14)
right.set(xlim=(-2.2,2.2),ylim=(-.34,1.29),xlabel=r"physical coordinate $x$",ylabel=r"smooth test value $\phi(x)$")
right.set_title("GL20-GL21: closure support is insufficient",fontsize=18,pad=20)
right.grid(alpha=.13)
fig.text(.065,.090,"Left: a repeating envelope for centers 2πj + π/12; only the marked decimal is numerical.\n"
    "Right: δ₀ vanishes on Y but detects this smooth closure-supported test. The arrow shows evaluation, not a delta density.",
    fontsize=16,linespacing=1.55)
fig.text(.065,.045,"Original figure · Proof locators GL4-GL7 and GL20-GL21 · GPT-6.1 Sol (OpenAI), Ultra · CC0",fontsize=13,color="#465361")
fig.savefig(OUT/f"{STEM}.png",dpi=120,metadata={"Software":"AN02 original deterministic mathematical figure"})
fig.savefig(OUT/f"{STEM}.svg",metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI), Ultra; CC0"})
plt.close(fig)
geometry={"schema":"exact-mathematical-figure/v1","coordinate_systems":{"left":"relative Fourier frequency h=xi-eta_j","right":"physical real coordinate x"},
    "left":{"distribution":"delta_0-delta_1","Fourier_transform":"1-exp(-i*xi)","eta_j":"2*pi*j+pi/12","N":3,
        "envelope":"2*abs(sin((pi/12+h)/2))/(1+abs(h))**3","maximizer_exact_contract":"unique root of (1+h)*cot((pi/12+h)/2)=6 in (0,1)",
        "maximizer_numerical_sample":hstar,"sample_root_residual":abs(root_function(hstar)),
        "numerical_sample_not_used_as_proof":True,"normalized_Fourier_value_at_zero":1},
    "right":{"Y":"(-2,2) minus {0}","closure_Y":"[-2,2]","test_support":"[-1,1]","test_value_at_zero":1,
        "test_formula":"exp(1-1/(1-x*x)) for abs(x)<1; zero otherwise","distribution":"delta_0",
        "delta_restriction_to_Y":0,"pairing_with_test":1,"delta_arrow_is_evaluation_not_density":True,
        "explicit_weighted_quotient":{"n":1,"p":2,"k":"(1+abs(xi))^-1","delta_norm_squared":"1/pi"}},
    "proof_locators":["GL4-GL7","GL20-GL21","GL24"],"width":2400,"height":1200,
    "original_expression_license":"CC0-1.0","external_figure_reproduced":False}
(OUT/f"{STEM}.json").write_text(json.dumps(geometry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"figure":STEM,"width":2400,"height":1200,"sample_maximizer":hstar,"root_residual":abs(root_function(hstar))}))
