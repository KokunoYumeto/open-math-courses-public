"""Original exact L114 illustration. Deterministic PNG/SVG/data, local writes only."""
from pathlib import Path
import argparse, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

parser=argparse.ArgumentParser()
parser.add_argument("--output",type=Path,default=Path(__file__).resolve().parent)
args=parser.parse_args();out=args.output/"assets";out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":16,"svg.hashsalt":"L114-integrable-point-spectrum-20261005","axes.titlesize":20,"axes.labelsize":16})
blue="#1769aa";orange="#d86a16";green="#267449";ink="#172b42";muted="#486179"
fig=plt.figure(figsize=(16,11),dpi=200,facecolor="#f6f8fc")
gs=fig.add_gridspec(3,2,height_ratios=[1,1,.83],hspace=.45,wspace=.28,left=.075,right=.965,top=.85,bottom=.07)
title=fig.suptitle("Integrable orbits produce actual eigenoperators",fontsize=26,fontweight="bold",color=ink,y=.985)
subtitle=fig.text(.5,.925,"Exact real translation model above · arbitrary-LCA proof mechanism below",ha="center",fontsize=15.5,color=muted)
axes=[fig.add_subplot(gs[0,0]),fig.add_subplot(gs[0,1]),fig.add_subplot(gs[1,0]),fig.add_subplot(gs[1,1])]
for ax in axes[:3]:
    ax.set_facecolor("white");ax.grid(alpha=.18);ax.spines[["top","right"]].set_visible(False)
r=np.linspace(-6,6,801);x=np.exp(-abs(r));y=.5*(1+abs(r))*x
ax=axes[0];ax.plot(r,x,color=blue,lw=3,label=r"$x(r)=e^{-|r|}$");ax.plot(r,y,color=orange,lw=3,label=r"$y(r)=\frac{1+|r|}{2}e^{-|r|}$")
ax.set(title="A  Positive orbit and filtered orbit",xlabel="spatial coordinate r",ylabel="multiplier value",ylim=(0,1.08));ax.legend(loc="upper right",fontsize=13)
ax.text(.03,.08,r"$b(t)=\frac{1}{2}e^{-|t|},\quad y=b*x$"+"\n"+r"$\int x=\int y=2,\quad\int b=1$",transform=ax.transAxes,color=ink,fontsize=15,bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
p=np.linspace(-5,5,801);a=2/(1+p*p);d=2/(1+p*p)**2
ax=axes[1];ax.plot(p,a,color=blue,lw=3,label=r"$\|\widehat{x}(p)\|=2/(1+p^2)$");ax.plot(p,d,color=orange,lw=3,label=r"$\|\widehat{y}(p)\|=2/(1+p^2)^2$")
ax.set(title="B  Exact Fourier-field amplitudes",xlabel="positive frequency p",ylabel="multiplier norm",ylim=(0,2.16));ax.legend(loc="upper right",fontsize=13)
ax.text(.035,.11,r"$f(p)=1/(1+p^2)$"+"\n"+r"Both supports are $\mathbb{R}$",transform=ax.transAxes,color=ink,fontsize=15,bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
rphase=np.linspace(-math.pi,math.pi,801)
ax=axes[2];ax.plot(rphase,np.cos(rphase),color=blue,lw=2.6,label=r"$\Re\,\widehat x(1)$");ax.plot(rphase,-np.sin(rphase),color=green,lw=2.6,label=r"$\Im\,\widehat x(1)$")
ax.plot(rphase,.5*np.cos(rphase),color=blue,lw=2.3,ls="--",label=r"$\Re\,\widehat y(1)$");ax.plot(rphase,-.5*np.sin(rphase),color=green,lw=2.3,ls="--",label=r"$\Im\,\widehat y(1)$")
ax.set(title=r"C  Actual eigenfunctions at $p=1$",xlabel="spatial coordinate r",ylabel="real / imaginary part",ylim=(-1.15,1.15))
ax.set_xticks([-math.pi,0,math.pi],labels=[r"$-\pi$","0",r"$\pi$"]);ax.legend(loc="upper center",fontsize=12,ncol=2,framealpha=.9)
ax.text(.03,.055,r"$\widehat x(1)=e^{-ir},\quad\widehat y(1)=\frac{1}{2}e^{-ir}$",transform=ax.transAxes,color=ink,fontsize=16,bbox={"facecolor":"white","alpha":.85,"edgecolor":"none"})
ax=axes[3];ax.axis("off")
ax.set_title("D  Two signs, one exact dictionary",loc="left",color=ink)
ax.text(.015,.79,r"Field: $\widehat x(p)=\int_G\overline{p(s)}\,\alpha_s(x)\,ds$",fontsize=17,color=blue)
ax.text(.015,.59,r"Filter: $f(p)=\int_G b(t)p(t)\,dt=F_b^-(-p)$",fontsize=17,color=orange)
ax.text(.015,.39,r"$\alpha_t(\widehat x(p))=p(t)\widehat x(p)$",fontsize=19,color=green)
ax.text(.015,.16,"Positive label p  ↔  GL/SS label −p\nWeak C₀ field; no general norm-decay claim",fontsize=17,color=ink,linespacing=1.6)
bottom=fig.add_subplot(gs[2,:]);bottom.axis("off")
bottom.text(0,1.06,"GENERAL PROOF  ·  integrability is required from the second box onward",fontsize=17,color=ink,fontweight="bold")
boxes=[
 (r"$T_{\alpha,K}(a)$"+"\nnormal compact\naverages",r"$T_\alpha(a)\in\widehat{M^\alpha}_+$"+"\nincluding infinity",blue),
 ("Semifinite average",r"$\mathfrak{p}_\alpha$ ultraweakly dense"+"\nbounded sandwiches",green),
 ("Normal open filter",r"$T_bx\ne0,\quad x\in\mathfrak{p}_\alpha$"+"\nfrom density",blue),
 (r"$\widehat{T_bx}=f\,\widehat x$"+"\nfield injectivity",r"$p\in V,\quad\widehat x(p)\ne0$",orange),
 ("Actual eigenoperator",r"$\alpha_t(\widehat x(p))=p(t)\widehat x(p)$"+"\n"+r"$\operatorname{Sp}(\alpha)=\overline{P_\alpha}$",green),
]
width=.17;gap=.025
for j,(heading,tail,color) in enumerate(boxes):
    xx=.015+j*(width+gap)
    patch=FancyBboxPatch((xx,.04),width,.88,boxstyle="round,pad=.009,rounding_size=.025",linewidth=1.6,edgecolor=color,facecolor="white",transform=bottom.transAxes)
    bottom.add_patch(patch)
    bottom.text(xx+width/2,.67,heading,ha="center",va="center",fontsize=12.5,color=color,linespacing=1.6,transform=bottom.transAxes)
    bottom.text(xx+width/2,.28,tail,ha="center",va="center",fontsize=11.5,color=ink,linespacing=1.7,transform=bottom.transAxes)
    if j<4:
        bottom.add_patch(FancyArrowPatch((xx+width+.005,.49),(xx+width+gap-.005,.49),arrowstyle="-|>",mutation_scale=15,lw=1.5,color=muted,transform=bottom.transAxes))
fig.text(.075,.028,"Exact formulas: IP10–11 and I20 · full average: IP3–4 · density: IP5 · open localization: IP12 · point spectrum: I33–37",fontsize=13,color=muted)
fig.canvas.draw()
renderer=fig.canvas.get_renderer()
title_box=title.get_window_extent(renderer);subtitle_box=subtitle.get_window_extent(renderer)
panel_boxes=[ax.title.get_window_extent(renderer) for ax in axes[:2]]
title_subtitle_gap=title_box.y0-subtitle_box.y1
subtitle_panel_gap=subtitle_box.y0-max(v.y1 for v in panel_boxes)
assert title_subtitle_gap>=16 and subtitle_panel_gap>=16,(title_subtitle_gap,subtitle_panel_gap)
layout={"PNG_dimensions":[3200,2200],"title_bbox":list(title_box.bounds),"subtitle_bbox":list(subtitle_box.bounds),
        "first_panel_title_bboxes":[list(v.bounds) for v in panel_boxes],
        "title_subtitle_gap_pixels":title_subtitle_gap,"subtitle_panel_gap_pixels":subtitle_panel_gap,
        "minimum_required_gap_pixels":16,"no_title_subtitle_or_first_panel_heading_overlap":True}
(args.output/"LAYOUT_CHECK.json").write_text(json.dumps(layout,indent=2)+"\n",encoding="utf-8")
fig.savefig(out/"integrable-point-spectrum.png",dpi=200,metadata={"Software":"Original local L114 renderer"})
fig.savefig(out/"integrable-point-spectrum.svg",metadata={"Date":None,"Creator":"Original local L114 renderer"})
plt.close(fig)
data={
 "scope":{"exact_model":"G=R, M=L∞(R,dr), alpha_t x(r)=x(r-t)","diagram":"arbitrary LCH abelian G, nonzero M, normal point-ultraweak action; last four boxes assume integrability"},
 "formulas":{"x":"exp(-abs(r))","b":"0.5*exp(-abs(t))","y":"0.5*(1+abs(r))*exp(-abs(r))","filter":"1/(1+p^2)","field_x":"2*exp(-i*r*p)/(1+p^2)","field_y":"2*exp(-i*r*p)/(1+p^2)^2"},
 "masses":{"integral_x":2,"integral_b":1,"integral_y":2,"orbit_average_x":"2*I","orbit_average_y":"2*I"},
 "frequency_labels":{"positive_p":1,"canonical_negative_label":-1,"eigenphase":"exp(i*t)","spatial_eigenfunction":"exp(-i*r)"},
 "support":{"x_field":"R","y_field":"R","strict_cut_shown":False},
 "sample_kind":"Numerical samples of proved exact formulas, not theorem verification",
 "spatial_samples":[{"r":float(v),"x":float(u),"y":float(w)} for v,u,w in zip(r,x,y)],
 "frequency_samples":[{"p":float(v),"field_x_norm":float(u),"field_y_norm":float(w)} for v,u,w in zip(p,a,d)],
 "p1_samples":[{"r":float(v),"field_x_real":float(math.cos(v)),"field_x_imag":float(-math.sin(v)),"field_y_real":float(.5*math.cos(v)),"field_y_imag":float(-.5*math.sin(v))} for v in rphase],
 "normalization":"Lebesgue dr,ds; no inverse Fourier integration performed and no missing 2*pi factor",
}
(out/"integrable-point-spectrum-data.json").write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"output":str(out),"PNG_dimensions":[3200,2200],"samples_per_panel":801}))
