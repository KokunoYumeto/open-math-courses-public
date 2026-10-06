from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12})
fig,axs=plt.subplots(1,3,figsize=(15.6,6.0),constrained_layout=True)
navy="#17324d"; blue="#2878b5"; amber="#d9822b"; green="#2d8a56"; red="#b94242"; gray="#66727d"; pale="#f4f7fa"

def box(ax,xy,w,h,text,edge=navy,face=pale,fs=11):
    b=FancyBboxPatch(xy,w,h,boxstyle="round,pad=0.02,rounding_size=0.03",linewidth=1.8,edgecolor=edge,facecolor=face)
    ax.add_patch(b); ax.text(xy[0]+w/2,xy[1]+h/2,text,ha="center",va="center",fontsize=fs,color=navy)

def arrow(ax,a,b,color=navy,label=None,dy=0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=14,linewidth=2,color=color))
    if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+dy,label,ha="center",va="center",fontsize=10,color=color)

# Panel 1
ax=axs[0]; ax.set_title("1  Reflected stable modes",loc="left",fontweight="bold",color=navy)
ax.plot([0,0],[0.08,0.90],color=navy,lw=2); ax.text(0,0.95,"seam  Y",ha="center",va="top",fontweight="bold",color=navy)
ax.add_patch(FancyBboxPatch((-1.0,0.08),0.98,0.76,boxstyle="round,pad=0.02",facecolor="#fff5e9",edgecolor=amber,lw=1.7))
ax.add_patch(FancyBboxPatch((0.02,0.08),0.98,0.76,boxstyle="round,pad=0.02",facecolor="#edf6fc",edgecolor=blue,lw=1.7))
ax.text(-0.51,0.78,r"$X_2$  ($r=-t_2$)",ha="center",fontweight="bold",color=amber)
ax.text(0.51,0.78,r"$X_1$  ($r=t_1$)",ha="center",fontweight="bold",color=blue)
ax.text(-0.51,0.61,r"stable:  $E^+$",ha="center",fontsize=13,color=green)
ax.text(0.51,0.61,r"stable:  $E^-$",ha="center",fontsize=13,color=green)
ax.text(-0.51,0.45,r"$e^{-\lambda^+t_2}a^+$",ha="center",color=navy)
ax.text(0.51,0.45,r"$e^{-\lambda^-t_1}a^-$",ha="center",color=navy)
arrow(ax,(-0.04,0.31),(-0.73,0.31),amber,r"decay as $t_2\uparrow$",0.06)
arrow(ax,(0.04,0.20),(0.73,0.20),blue,r"decay as $t_1\uparrow$",-0.07)
ax.text(0,-0.055,"same signed-collar symbol:\n"+r"$\mathrm{diag}(\rho+i\lambda^+,-\rho+i\lambda^-)$",ha="center",va="center",fontsize=10,color=gray)
ax.set_xlim(-1.08,1.08); ax.set_ylim(-0.12,1); ax.axis("off")

# Panel 2
ax=axs[1]; ax.set_title("2  Coupling from separation to gluing",loc="left",fontweight="bold",color=navy)
box(ax,(0.05,0.69),0.9,0.17,r"$C_\tau=(\gamma u_2^+-\tau\gamma u_1^+,\;\gamma u_1^--\tau\gamma u_2^-)$",blue,"#edf6fc",10)
box(ax,(0.05,0.39),0.37,0.16,"$\\tau=0$\n$\\gamma u_2^+=0$\n$\\gamma u_1^-=0$",amber,"#fff5e9",10)
box(ax,(0.58,0.39),0.37,0.16,"$\\tau=1$\n$\\gamma u_2^+=\\gamma u_1^+$\n$\\gamma u_1^-=\\gamma u_2^-$",green,"#edf8f1",10)
arrow(ax,(0.43,0.47),(0.57,0.47),navy,r"Fredholm path",0.07)
ax.text(0.235,0.26,r"$(P_1,B_1)\oplus(P_2,B_2)$",ha="center",fontsize=10,color=navy)
ax.text(0.765,0.26,r"$\widehat P:H^1(\widehat X)\to L^2(\widehat X)$",ha="center",fontsize=10,color=navy)
ax.text(0.5,0.09,r"On stable traces:  $C_\tau(0,a^-;a^+,0)=(a^+,a^-)$",ha="center",fontsize=10.5,color=green)
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")

# Panel 3
ax=axs[2]; ax.set_title("3  The index convention is part of the datum",loc="left",fontweight="bold",color=navy)
box(ax,(0.05,0.71),0.9,0.14,r"$\mathrm{ind}\,D=\mathrm{ind}\,A+\mathrm{ind}\,C$",navy,"#f4f7fa",13)
box(ax,(0.06,0.40),0.88,0.17,"geometric double\n$\\mathrm{ind}\\,C=0$\n$\\mathrm{ind}\\,D=\\mathrm{ind}\\,A$",green,"#edf8f1",11)
box(ax,(0.06,0.12),0.88,0.17,"same-index double datum\n$\\mathrm{ind}\\,C=\\mathrm{ind}\\,A$\n$\\mathrm{ind}\\,A=\\frac{1}{2}\\mathrm{ind}\\,D$",red,"#fceded",11)
arrow(ax,(0.36,0.70),(0.36,0.59),green)
ax.add_patch(FancyArrowPatch((0.68,0.70),(0.78,0.30),arrowstyle="-|>",mutation_scale=14,linewidth=2,color=red,connectionstyle="arc3,rad=-0.32"))
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")

fig.suptitle("Split boundary modes, gluing, and the doubled index",fontsize=18,fontweight="bold",color=navy)
fig.savefig(OUT/'split_doubling_index.svg',bbox_inches='tight')
fig.savefig(OUT/'split_doubling_index.png',dpi=220,bbox_inches='tight')
