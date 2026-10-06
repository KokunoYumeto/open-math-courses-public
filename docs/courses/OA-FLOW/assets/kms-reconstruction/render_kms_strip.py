"""Exact M2 KMS strip; coordinates and all displayed values are analytic."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

d=Path(__file__).resolve().parent
q=np.log(4.0); period=2*np.pi/q
t=np.linspace(0,period,601); s=np.linspace(0,1,201)
T,S=np.meshgrid(t,s)
G=.2*np.exp(-1j*q*(T+1j*S))
fig,axes=plt.subplots(1,2,figsize=(13.6,6.8),gridspec_kw={"width_ratios":[1.2,1]})
fig.subplots_adjust(left=.065,right=.965,top=.72,bottom=.29,wspace=.3)
fig.suptitle("One exact KMS strip: the product order changes at height i",fontsize=18,fontweight="bold",y=.975)
fig.text(.5,.885,r"$d=\mathrm{diag}(1,4)/5,\quad \varphi(x)=\mathrm{Tr}(dx),\quad a=E_{12},\quad b=E_{21}$",
         ha="center",fontsize=14)
ax=axes[0]
im=ax.pcolormesh(T,S,np.abs(G),shading="auto",cmap="viridis",vmin=.2,vmax=.8,rasterized=True)
for k,phase in enumerate([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]):
    tk=phase/q
    ax.axvline(tk,color="white",lw=.7,alpha=.65)
    ax.text(tk,.49,["0",r"$-\pi/2$",r"$-\pi$",r"$-3\pi/2$",r"$-2\pi$"][k],
            color="white",ha="center",fontsize=11,
            bbox={"facecolor":"#233f4d","alpha":.55,"edgecolor":"none","pad":2})
ax.set_title(r"$G(t+is)=\frac{1}{5}\,4^s e^{-it\log4}$"+"\n"+
             r"$s=1:\ \varphi(b\sigma_t(a))=\frac{4}{5}e^{-it\log4}$",fontsize=13,pad=13)
ax.set_xlim(-.07,period+.07);ax.set_ylim(0,1)
ax.set_xlabel(r"$t$ (one period $2\pi/\log4$)",fontsize=12)
ax.set_ylabel(r"$s=\mathrm{Im}\,z$",fontsize=12)
ax.set_xticks([0,period/4,period/2,3*period/4,period],["0","T/4","T/2","3T/4","T"])
ax.set_yticks([0,.5,1])
ax.text(.5,-.27,r"$s=0:\ \varphi(\sigma_t(a)b)=\frac{1}{5}e^{-it\log4}$",
        transform=ax.transAxes,ha="center",fontsize=12)
cb=fig.colorbar(im,ax=ax,pad=.025,fraction=.055)
cb.set_label(r"$|G|$",fontsize=12);cb.set_ticks([.2,.4,.8])
ax=axes[1]
colors=["#46327e","#218d8d","#b58b13"]
for sk,color in zip([0,.5,1],colors):
    radius=.2*4**sk
    vals=radius*np.exp(-1j*q*t)
    ax.plot(vals.real,vals.imag,color=color,lw=2.5,label=f"s = {sk:g}, radius = {radius:g}")
    ta=.4;tb=.58
    ax.annotate("",xy=(radius*np.cos(tb),-radius*np.sin(tb)),
                xytext=(radius*np.cos(ta),-radius*np.sin(ta)),
                arrowprops={"arrowstyle":"-|>","color":color,"lw":2})
    ax.scatter([radius],[0],color=color,s=35,zorder=5)
ax.axhline(0,color="#bbc5ca",lw=.8);ax.axvline(0,color="#bbc5ca",lw=.8)
ax.set_aspect("equal");ax.set_xlim(-.95,.95);ax.set_ylim(-.95,.95)
ax.set_xlabel(r"$\mathrm{Re}\,G$",fontsize=12);ax.set_ylabel(r"$\mathrm{Im}\,G$",fontsize=12)
ax.set_title("Horizontal lines map to clockwise circles",fontsize=13,pad=13)
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.19),ncol=1,frameon=False,fontsize=11)
ax.grid(alpha=.15)
fig.text(.5,.025,"Exact example, not a picture of an arbitrary weight. KT-1–2 prove the full strip; KU-3 proves group uniqueness.",
         ha="center",fontsize=11)
fig.savefig(d/"assets"/"kms-strip.png",dpi=180,bbox_inches="tight")
fig.savefig(d/"assets"/"kms-strip.svg",bbox_inches="tight")
plt.close(fig)
(d/"kms-figure-numerics.json").write_text(json.dumps({
 "density":[.2,.8],"log_spectral_ratio":-q,"real_time_period":period,
 "upper_strip":"G(z)=(1/5) exp(-i z log 4)",
 "height_radii":[{"s":sk,"radius":.2*4**sk} for sk in [0,.5,1]],
 "maximum_log_convexity_error":float(np.max(np.abs(np.abs(G)-(.2**(1-S))*(.8**S)))),
 "proof":"KMS-FIGURE.md; KT1–KT7; KU9–KU14",
 "interpretation":"Complete exact M2 scalar coefficient; phase labels are continuous unwrapped phases, not principal arguments."
},indent=2)+"\n",encoding="utf-8")
