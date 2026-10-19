"""Exact support geometry from AN01-U085, Exercises2 and8. CC0.

Left arrows are .16 times the exact covectors +/-(g'(s)*-1,1).
Right C is conv(0,closed disk((0,1),2/5)); Ceps=.75*C+.25*(0,1).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Circle
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig,ax=plt.subplots(1,2,figsize=(12.7,6.2),layout='constrained')
s=np.linspace(-1.25,1.25,500);g=np.abs(s)**1.5
ax[0].fill_between(s,-.4,g,color='#e7edf4');ax[0].plot(s,g,color='#1a5f98',lw=2.3)
for q in [-.81,-.36,.36,.81]:
    point=np.array([q,abs(q)**1.5]);normal=np.array([-1.5*np.sign(q)*np.sqrt(abs(q)),1.])
    for sign in [-1,1]:ax[0].annotate('',xy=point+sign*.16*normal,xytext=point,arrowprops=dict(arrowstyle='->',color='#1a5f98',lw=1.5))
    ax[0].scatter(*point,s=18,color='#1a5f98',zorder=4)
for sign in [-1,1]:ax[0].annotate('',xy=(0,sign*.32),xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#a23466',lw=2,linestyle='--'))
ax[0].scatter([0],[0],s=24,color='#a23466',zorder=5)
ax[0].text(-1.08,-.25,r'$F:\ t\leq |s|^{3/2}$',fontsize=14)
ax[0].text(0,1.43,'At s=0: limiting\nvertical covectors',ha='center',fontsize=11,color='#a23466')
ax[0].set(xlim=(-1.3,1.3),ylim=(-.4,1.8),xlabel='$s$',ylabel='$t$')
ax[0].set_title('A first-derivative normal may require closure\n'+r'$(-\frac{3}{2}\operatorname{sgn}(s)\sqrt{|s|},1)\to(0,1)$',pad=15)
r=.4;theta=np.linspace(-np.arcsin(r),np.pi+np.arcsin(r),400)
arc=np.c_[r*np.cos(theta),1+r*np.sin(theta)]
C=np.vstack([[0,0],arc,[0,0]])
eps=.25;Ceps=(1-eps)*C+eps*np.array([0,1])
ax[1].axhspan(-.2,0,color='#e7edf4');ax[1].axhline(0,color='#697a8d',lw=.8)
ax[1].add_patch(Polygon(C,facecolor='#dcebf6',edgecolor='#1a5f98',lw=1.5))
ax[1].add_patch(Circle((0,1),r,facecolor='none',edgecolor='#1a5f98',linestyle=':',lw=1.2))
ax[1].add_patch(Polygon(Ceps,facecolor='#f7dce8',edgecolor='#a23466',lw=1.6,alpha=.9))
ax[1].scatter([0,0],[0,eps],s=25,color=['#1a5f98','#a23466'],zorder=5)
ax[1].annotate('',xy=(0,eps),xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2,color='#a23466'))
ax[1].text(.07,.02,r'$a=(0,0)$',fontsize=11)
ax[1].text(.07,.25,r'$b=(0,1/4)$',fontsize=11)
ax[1].text(-.66,-.13,r'$F:\ t\leq0$',fontsize=12)
ax[1].text(-.62,.65,'$C$',fontsize=15,color='#1a5f98')
ax[1].text(.42,.95,r'$C_{1/4}$',fontsize=14,color='#a23466')
ax[1].text(-.64,1.5,r'$n=(b-a)/|b-a|=(0,1)$',fontsize=12)
ax[1].set(xlim=(-.75,.75),ylim=(-.2,1.65),xlabel='$s$',ylabel='$t$')
ax[1].set_title('Contract the convex set and take a closest pair\n'+r'$C_\varepsilon=(1-\varepsilon)C+\varepsilon(0,1)$',pad=15)
for a in ax:
    a.set_aspect('equal');a.spines[['top','right']].set_visible(False);a.grid(alpha=.12)
fig.suptitle('Support geometry forces both analytic covector signs',fontsize=18,fontweight='bold')
fig.text(.5,-.06,'Solid left arrows: 0.16 times the covectors. Dashed arrows indicate the limiting directions.\nRight: disk radius 2/5, contraction parameter 1/4. Coordinates and closest pair are exact.',ha='center',fontsize=11)
fig.savefig(out/'support-normals-and-convex-contact.png',dpi=210,bbox_inches='tight',facecolor='white')
fig.savefig(out/'support-normals-and-convex-contact.svg',bbox_inches='tight',facecolor='white')
p=out/'support-normals-and-convex-contact.svg';p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines()).rstrip()+'\n',encoding='utf-8')
