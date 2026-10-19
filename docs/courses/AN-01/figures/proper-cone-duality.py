"""Exact planar cones for AN01-U093 Lemma 7a; original illustration, CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-proper-cone-duality'})
fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
ax=axs[0];theta=np.linspace(0,np.pi/2,241)
arc=np.column_stack([np.cos(theta),np.sin(theta)])
ax.add_patch(Polygon(arc,closed=True,facecolor='#b5dbed',alpha=.8,edgecolor='none'))
ax.plot(arc[:,0],arc[:,1],color='#155b81',lw=3,label=r'$S=C\cap S^1$')
ax.plot([0,1],[1,0],color='#a34d16',lw=2,label=r'$q_1+q_2=1$')
ax.annotate('',xy=(.5,.5),xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=2,color='#753f8d'))
ax.scatter([.5],[.5],s=55,color='#753f8d',zorder=5)
ax.annotate(r'$p=(1/2,1/2)$',(.5,.5),xytext=(.02,.43),arrowprops=dict(arrowstyle='-',color='#753f8d'),fontsize=11)
ax.text(.61,.65,r'$H$',fontsize=19,color='#155b81')
ax.set(xlim=(-.08,1.15),ylim=(-.08,1.17),xlabel=r'$q_1$',ylabel=r'$q_2$',title='A uniform positive pairing')
ax.legend(loc='upper right',bbox_to_anchor=(1.02,1.01),fontsize=10,framealpha=1)
ax=axs[1]
ax.axvspan(0,1.6,color='#b5dbed',alpha=.8)
ax.axvline(0,color='#155b81',ls='--',lw=2)
ax.text(.56,.82,r'$\Gamma=\{y_1>0\}$',fontsize=16,color='#155b81')
ax.text(-.92,.68,'Excluded\nboundary',fontsize=11)
ax.annotate('',xy=(-.02,.1),xytext=(-.57,.6),arrowprops=dict(arrowstyle='->',color='#155b81'))
ax.annotate('',xy=(1.4,0),xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=3,color='#a34d16'))
ax.scatter([0],[0],color='#a34d16',s=40,zorder=6)
ax.text(.48,-.43,r'$C=\mathbb{R}_+(1,0)$',fontsize=14,color='#a34d16')
ax.text(.46,-.69,'Ray includes zero',fontsize=10,color='#a34d16')
ax.set(xlim=(-1.1,1.6),ylim=(-1.05,1.25),xlabel=r'$y_1$ / first coordinate',ylabel=r'$y_2$ / second coordinate',title='A ray has an open half-space dual')
for ax in axs:
 ax.set_aspect('equal');ax.axhline(0,color='#627180',lw=.7,zorder=0)
 ax.spines[['top','right']].set_visible(False)
 ax.grid(alpha=.16)
out=Path(__file__).resolve().parent
fig.savefig(out/'proper-cone-duality.png',dpi=160,metadata={'Software':'Matplotlib; original illustration, CC0'})
fig.savefig(out/'proper-cone-duality.svg',metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI), Ultra; CC0'})
p=out/'proper-cone-duality.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
