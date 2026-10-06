"""Exact phase-cell and monomial scale factors for the lesson's cubic model.

Original figure, GPT-6.1 Sol (OpenAI), Ultra, September 2026. CC0.
These are symbol cells and scale factors, not operator norm constants.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R=10000
k=3
weights=(1,2)
colors=("#08769a","#be5413")
angle=np.linspace(0,2*np.pi,1201)
fig,axes=plt.subplots(1,2,figsize=(11.5,5.0),gridspec_kw={"width_ratios":[1.1,1]})
fig.subplots_adjust(left=.085,right=.98,bottom=.22,top=.81,wspace=.30)
for j,(weight,color) in enumerate(zip(weights,colors),1):
    dx=R**(-weight/(k+1))
    dxi=R**(weight/(k+1))
    axes[0].plot(dx*np.cos(angle),dxi*np.sin(angle),color=color,lw=2.1,
        label=f"Pair {j}: semiaxes {dx:g}, {dxi:g}")
axes[0].set(xlim=(-.12,.12),ylim=(-112,112),
    xlabel=r"Position displacement $\Delta x_j$",
    ylabel=r"Frequency displacement $\Delta\xi_j$",
    title="Unequal widths, equal phase area")
axes[0].axhline(0,color="#9fa8ab",lw=.7)
axes[0].axvline(0,color="#9fa8ab",lw=.7)
axes[0].grid(alpha=.16)
axes[0].legend(loc="upper right",fontsize=8.3,framealpha=.95)
terms=[r"$D_1$",r"$x_1^3\,R$",r"$x_1^3\,\Delta\xi_2$"]
values=[R**.25,R**.25,R**(-.25)]
axes[1].bar(range(3),values,width=.55,color=[colors[0],colors[0],colors[1]])
axes[1].set_yscale("log")
axes[1].set(ylim=(.035,30),xticks=range(3),xticklabels=terms,
    ylabel="Monomial scale factor",title="Both leading terms balance")
axes[1].grid(axis="y",alpha=.18)
for i,value in enumerate(values):
    axes[1].text(i,value*1.22,f"{value:g}",ha="center",va="bottom",fontsize=11)
fig.suptitle(r"Cubic model: $p=\xi_1+i x_1^3\xi_2$, $R=10\,000$",
    fontsize=15,y=.955)
fig.text(.5,.875,r"$k=3,\quad m=(1,2),\quad\mu=(3,2),\quad m_j+\mu_j=4$",
    ha="center",fontsize=12)
fig.text(.5,.105,r"Each ellipse: $(\Delta x_j/\sigma_{x_j})^2+(\Delta\xi_j/\sigma_{\xi_j})^2=1$; area $=\pi$.",
    ha="center",fontsize=10)
fig.text(.5,.052,"Scale factors describe the dilation; they are not measured operator norms or spectral values.",
    ha="center",fontsize=9,color="#3e484c")
target=Path(__file__).with_name("weighted-packets.png")
fig.savefig(target,dpi=180,facecolor="white",metadata={
    "Software":"Matplotlib; original mathematical figure, GPT-6.1 Sol (OpenAI); CC0"})
plt.close(fig)
print(target.name)
