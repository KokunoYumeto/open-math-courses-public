"""Exact maps and point-observation functions for FC02 and FC08; CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
out=Path(__file__).with_name('form-domain-completion.png')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,(left,right)=plt.subplots(1,2,figsize=(12,5.2),dpi=150,gridspec_kw={'width_ratios':[1.05,1]})
fig.patch.set_facecolor('#fafbfd')
left.set_axis_off();left.set_xlim(0,1);left.set_ylim(0,1)
left.set_title('The completion remembers energy',weight='bold',pad=16)
for x,y,s in [(.12,.70,r'$D$'),(.78,.70,r'$V=\widehat{D}^{\,\|\cdot\|_q}$'),(.45,.30,r'$H$')]:
 left.text(x,y,s,ha='center',va='center',fontsize=20,color='#18334d',bbox={'facecolor':'#eaf2fb','edgecolor':'#8ca8c2','boxstyle':'round,pad=0.4'})
for start,end,label,pos in [((.21,.70),(.56,.70),r'$\iota$',(.38,.77)),((.13,.60),(.37,.37),'inclusion',(.13,.44)),((.76,.60),(.53,.37),r'$j$',(.71,.44))]:
 left.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#246287','lw':2})
 left.text(*pos,label,ha='center',fontsize=15,color='#246287')
left.text(.5,.13,r'$j\iota x=x$',ha='center',fontsize=16)
left.text(.5,.025,r'Closable $\Longleftrightarrow\ \ker j=\{0\}$',ha='center',fontsize=15,weight='bold')
t=np.linspace(0,1,961)
for n,color in [(1,'#2066a5'),(3,'#00846b'),(8,'#b74b35')]:
 values=np.maximum(1-n*t,0)
 right.plot(t,values,color=color,lw=2.5,label=rf'$n={n}:\ \|f_n\|_2^2=1/{3*n}$')
right.scatter([0],[1],color='#18334d',s=55,zorder=5)
right.set(xlim=(-.015,1.02),ylim=(-.04,1.08),xlabel=r'$t$',ylabel=r'$f_n(t)$')
right.set_title('One observation survives norm decay',weight='bold',pad=16)
right.grid(alpha=.18);right.legend(loc='upper right',fontsize=11,framealpha=1)
right.text(.50,.70,r'$q[f_n]=1$',ha='center',fontsize=17)
right.text(.58,.60,r'$q[f_n-f_m]=0$',ha='center',fontsize=15)
fig.subplots_adjust(left=.03,right=.98,bottom=.12,top=.86,wspace=.22)
fig.savefig(out,facecolor=fig.get_facecolor(),metadata={'Software':'Matplotlib; reproducible OA-MOD FC proof illustration'})
plt.close(fig)
print(out)
