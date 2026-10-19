from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
                     'svg.fonttype':'path','svg.hashsalt':'skew-odometer-flow-coordinate-v1'})
ROOT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(7.2,10.4),facecolor='white')
top=fig.add_axes([.04,.53,.92,.43]);top.set_axis_off()
top.text(.5,.95,'An invariant coordinate',ha='center',fontsize=22,color='#124e69')
for y,colour in [(.49,'#17667a'),(.10,'#6d43a6')]:
    top.add_patch(FancyBboxPatch((.025,y),.95,.32,boxstyle='round,pad=0.012',
                                linewidth=1.4,edgecolor=colour,facecolor='#fafafa'))
top.text(.5,.755,'The lifted odometer step',ha='center',fontsize=16,color='#17667a')
top.text(.5,.65,r'$(x,w,r,t)\ \longmapsto$'+'\n'+
         r'$(Tx,F_{-a}w,\ r+\log J_{-a}(w)+b,\ t+a)$',
         ha='center',va='center',fontsize=14,linespacing=1.7)
top.text(.5,.525,r'$q=F_t w\qquad F_{t+a}F_{-a}w=q$',ha='center',fontsize=16)
top.text(.5,.355,'The dual translation',ha='center',fontsize=16,color='#6d43a6')
top.text(.5,.26,r'$D_s(x,w,r,t)=(x,w,r,t+s)$',ha='center',fontsize=16)
top.text(.5,.155,r'$q\longmapsto F_s q$',ha='center',fontsize=18)
top.text(.5,.025,'Theorem 4.3: every invariant is a function of q.',ha='center',fontsize=12)

ax=fig.add_axes([.13,.11,.80,.35])
ax.set_facecolor('#fbfbf8')
a=math.log(2);s=math.log(3)
P=(1.,0.);M=(1.-a,a);D=(1.,s)
wx=[-.1,2.2]
ax.plot(wx,[1-x for x in wx],color='#17667a',linewidth=1.7)
ax.plot(wx,[1+s-x for x in wx],color='#6d43a6',linewidth=1.7,linestyle='--')
for point,colour in [(P,'#253c49'),(M,'#17667a'),(D,'#6d43a6')]:
    ax.scatter(*point,s=42,color=colour,zorder=4)
ax.annotate('',xy=M,xytext=P,arrowprops={'arrowstyle':'->','color':'#17667a','lw':2.5})
ax.annotate('',xy=D,xytext=P,arrowprops={'arrowstyle':'->','color':'#6d43a6','lw':2.5})
ax.text(1.20,.12,r'$P=(1,0)$',fontsize=12,va='center')
ax.text(.02,.84,r'$(1-\log2,\log2)$',fontsize=12,color='#17667a')
ax.text(1.08,1.14,r'$(1,\log3)$',fontsize=12,color='#6d43a6')
ax.text(1.05,.46,r'$D_{\log3}$',fontsize=12,color='#6d43a6',ha='left')
ax.text(.10,.30,r'$(-a,+a)$',fontsize=12,color='#17667a')
ax.text(1.40,-.12,r'$w+t=1$',fontsize=12,color='#17667a')
ax.text(1.25,.64,r'$w+t=1+\log3$',fontsize=12,color='#6d43a6',rotation=-35)
ax.set_xlim(-.1,2.2);ax.set_ylim(-.2,1.7)
ax.set_xlabel(r'$w$',fontsize=15);ax.set_ylabel(r'$t$',fontsize=15,rotation=0,labelpad=10)
ax.set_aspect('equal',adjustable='box')
ax.set_title(r'Gaussian sample: $F_s(w)=w+s$, $q=w+t$',fontsize=14,pad=12)
ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=10)
fig.text(.5,.055,'Exercise 6.3. The r-coordinate is omitted in this plane.',ha='center',fontsize=11)
fig.text(.5,.030,'This sample is transitive; the general flow is described above.',ha='center',fontsize=11)
fig.savefig(ROOT/'skew-odometer-flow-coordinate.svg',metadata={'Date':None},facecolor='white')
fig.savefig(ROOT/'skew-odometer-flow-coordinate.png',dpi=180,metadata={'Software':'Matplotlib'},facecolor='white')
plt.close(fig)
