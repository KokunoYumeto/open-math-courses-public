"""Exact planar conic geometry for AN01-U100; GPT-6 Astra (OpenAI), CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U100-overlap-sum','text.usetex':False})
D=Path(__file__).resolve().parent
blue='#1266a0';orange='#bd6109';green='#147a50';purple='#7750a4'
fig,axs=plt.subplots(1,2,figsize=(12.6,6.6))
def ray(ax,angle,color,style='-',r=1.15):
 t=np.deg2rad(angle);ax.plot([0,r*np.cos(t)],[0,r*np.sin(t)],color=color,ls=style,lw=1.6)
def sector(ax,a,b,color,alpha):
 ax.add_patch(Wedge((0,0),1.15,a,b,facecolor=color,alpha=alpha,edgecolor='none'))
for ax in axs:
 ax.axhline(0,color='#b6bfca',lw=.8);ax.axvline(0,color='#b6bfca',lw=.8)
 ax.set_aspect('equal');ax.set_xlim(-1.45,1.45);ax.set_ylim(-1.32,1.5)
 ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.spines[['top','right']].set_visible(False)
 ax.spines[['left','bottom']].set_color('#c4cbd4')
ax=axs[0]
sector(ax,-75,75,blue,.20);sector(ax,45,195,orange,.22);sector(ax,45,75,green,.65)
for a,c in [(-75,blue),(75,blue),(45,orange),(195,orange)]:ray(ax,a,c)
ax.scatter([0],[0],c='#263445',s=22,zorder=6)
ax.text(.67,-.55,r'$C_1$',color=blue,fontsize=16)
ax.text(-.67,.58,r'$C_2$',color=orange,fontsize=16)
ax.annotate(r'$C_1\cap C_2$',xy=(.51,.88),xytext=(.30,1.30),ha='center',color=green,arrowprops=dict(arrowstyle='-',color=green))
ax.set_title('Covector space',fontweight='bold',pad=13)
ax.set_xlabel(r'$\xi_1$');ax.set_ylabel(r'$\xi_2$')
ax.text(.5,-.19,'Closed sectors: −75°…75°, 45°…195°\nIntersection: 45°…75°',transform=ax.transAxes,ha='center',va='top')
ax=axs[1]
sector(ax,-15,135,purple,.13);sector(ax,-15,15,blue,.45);sector(ax,105,135,orange,.45)
for a,c in [(-15,blue),(15,blue),(105,orange),(135,orange)]:ray(ax,a,c,'--')
v1=np.array([1.,0.]);v2=np.array([-.5,np.sqrt(3)/2]);v=v1+v2
assert np.allclose(v,[.5,np.sqrt(3)/2]) and abs(np.linalg.norm(v)-1)<1e-12
for w,c in [(v1,blue),(v2,orange),(v,green)]:
 ax.annotate('',xy=w,xytext=(0,0),arrowprops=dict(arrowstyle='->',color=c,lw=2))
ax.annotate('',xy=v,xytext=v1,arrowprops=dict(arrowstyle='->',color='#737d89',ls=':',lw=1.6))
ax.text(.89,-.20,r'$v_1$',color=blue);ax.text(-.77,.92,r'$v_2$',color=orange)
ax.text(.55,.94,r'$v_1+v_2$',color=green)
ax.text(.64,.48,r'$G_1+G_2$',color=purple,fontsize=14)
ax.scatter([0],[0],facecolor='white',edgecolor='#263445',s=28,zorder=7)
ax.set_title('Imaginary approach space',fontweight='bold',pad=13)
ax.set_xlabel(r'$y_1$');ax.set_ylabel(r'$y_2$')
ax.text(.5,-.19,'Open duals: (−15°,15°), (105°,135°)\nSum: (−15°,135°); dashed rays excluded',transform=ax.transAxes,ha='center',va='top')
fig.suptitle('An overlap of singular directions gives a larger holomorphic approach cone',fontsize=15,y=.98)
fig.subplots_adjust(left=.065,right=.98,top=.88,bottom=.24,wspace=.30)
fig.savefig(D/'overlap-and-sum-cones.png',dpi=150,facecolor='white',metadata={'Software':'GPT-6 Astra (OpenAI); reproducible CC0 figure'})
fig.savefig(D/'overlap-and-sum-cones.svg',facecolor='white',metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI); CC0'})
p=D/'overlap-and-sum-cones.svg';p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
