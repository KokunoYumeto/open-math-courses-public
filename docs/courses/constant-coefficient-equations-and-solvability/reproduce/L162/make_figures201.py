"""Original compact-kernel and Baire-weight illustrations."""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/"figures";OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.fonttype":"path","svg.hashsalt":"frequency-selective201",
                     "axes.grid":True,"grid.alpha":.2})
COLORS=["#15618a","#b44236","#26774f"]
def raw(x):
    t=1-4*x*x
    return np.exp(-1/t) if t>0 else 0.
mass=quad(raw,-.5,.5,epsabs=1e-13,epsrel=1e-13)[0]
def save(fig,name):
    fig.savefig(OUT/(name+".png"),dpi=160,bbox_inches="tight",
                metadata={"Software":"Matplotlib;original mathematical figure"})
    fig.savefig(OUT/(name+".svg"),bbox_inches="tight",
                metadata={"Date":None,"Creator":"Original mathematical figure"})
    plt.close(fig)
x=np.linspace(-.65,.65,601);w=np.linspace(-10,10,601)
seed=np.array([raw(t)/mass for t in x])
transform=np.array([quad(lambda t:raw(t)*np.cos(s*t),-.5,.5,
                         epsabs=1e-13,epsrel=1e-13)[0]/mass for s in w])
fig,axes=plt.subplots(1,2,figsize=(12.4,4.5))
axes[0].plot(x,seed,color=COLORS[0],lw=2.5)
axes[0].axvline(-.5,color="#666666",ls="--",lw=1)
axes[0].axvline(.5,color="#666666",ls="--",lw=1)
axes[0].set(xlabel=r"Physical coordinate $x$",ylabel=r"Probability density $\psi(x)$",
            title=r"Smooth seed: support $[-1/2,1/2]$, integral $1$")
for k,color in zip([4,16,64],COLORS):
    axes[1].plot(w,np.abs(transform)**k,lw=2,color=color,label=fr"$k={k}$")
axes[1].set(xlabel=r"Scaled frequency $w=(\xi-c_j)/k_j$",
            ylabel=r"$|F_\psi(w)|^k$",ylim=(-.025,1.075),
            title="Transform powers concentrate around the center")
axes[1].legend()
fig.suptitle("Compact smooth kernels with an exact central transform value",fontsize=15)
fig.text(.5,.01,"Transform curves are numerical quadrature samples; these are smooth test kernels.",
         ha="center",fontsize=10)
fig.tight_layout(rect=(0,.035,1,.92));save(fig,"compact-kernels-and-transform-peaks")
ell=np.arange(20,801,dtype=float);k=np.floor(ell)
fig,axes=plt.subplots(1,3,figsize=(13.7,4.45))
for n,color in zip([1,2,3],COLORS):
    axes[0].plot(ell,np.sqrt(ell)/np.log(10)-n*np.log10(k),color=color,lw=2,
                 label=fr"Dimension $n={n}$")
axes[0].axhline(0,color="#666666",lw=.8)
axes[0].set(xlabel=r"$\ell=\log Q$",ylabel=r"$\log_{10}(t/k^n)$",
            title="Weight outruns kernel height")
axes[0].legend(fontsize=9)
axes[1].plot(ell,(np.sqrt(ell)-ell)/np.log(10),color=COLORS[1],lw=2)
axes[1].set(xlabel=r"$\ell=\log Q$",ylabel=r"$\log_{10}(t/Q)$",
            title=r"$C^1$ Fourier decay defeats the weight")
axes[2].plot(ell,-1/np.sqrt(ell),color=COLORS[0],lw=2,
             label=r"Lower bound $-1/\sqrt{\ell}$")
axes[2].axhline(0,color=COLORS[1],ls="--",label="Reference value 0")
axes[2].set(xlabel=r"$\ell=\log Q$",ylabel="Normalized logarithm",
            title="The lower error tends to zero")
axes[2].legend(loc="lower right",fontsize=8.5)
fig.suptitle(r"One evaluation weight: $t=e^{\sqrt{\log Q}}$",fontsize=15)
fig.text(.5,.01,"Exact comparison functions; no transform of the Baire-selected function is plotted.",
         ha="center",fontsize=10)
fig.tight_layout(rect=(0,.035,1,.92));save(fig,"evaluation-weights-and-zero-profiles")
geometry=dict(authorship="Original mathematics and figures;GPT-6.1 Sol (OpenAI),Ultra;CC0 1.0",
    kernel=dict(seed="exp(-1/(1-4*x*x))/I for |x|<1/2;zero outside",
                normalization="I=integral from -1/2 to1/2 exp(-1/(1-4*x*x))dx",
                numerical_normalization=mass,support=[-.5,.5],integral=1,convolution_powers=[4,16,64],
                transform_formula="F_u_j(c_j+k_j*w)=F_psi(w)^k_j",
                central_value=1,curves_are_quadrature_samples=True,
                nonsmooth_selected_function_plotted=False,proof_locators=["Formal2.4–2.5","Formal Lemma2.2"]),
    weights=dict(log_frequency_range=[20,800],k="floor(logQ)",weight="exp(sqrt(logQ))",
                 dimensions=[1,2,3],height_ratio_log10="sqrt(ell)/log(10)-n*log10(floor(ell))",
                 C1_ratio_log10="(sqrt(ell)-ell)/log(10)",central_lower="-1/sqrt(ell)",
                 zero_line_is_reference=True,actual_selected_transform_plotted=False,
                 proof_locators=["Formal4.1–4.6"]),
    references=["Terence Tao,245B Notes9 and246B Notes2","Lars Hörmander,Analysis of Linear Partial Differential Operators I and II"])
(OUT/"geometry201.json").write_text(json.dumps(geometry,indent=2,allow_nan=False)+"\n",encoding="utf-8")
print(json.dumps(dict(figures=2,formats=["PNG","SVG"],seed_normalization=mass)))
