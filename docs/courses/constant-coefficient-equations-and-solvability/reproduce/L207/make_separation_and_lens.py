"""Reproduce the separated Cauchy kernel and the exact convex lens."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'AN02-L207-separation-and-lens','font.family':'DejaVu Sans'})

def main():
    data=json.loads((HERE/'separation-and-lens-geometry.json').read_text(encoding='utf-8'))
    assert data['separated_kernel']['pole']==['2','0'] and data['lens']['radii']==['1','1']
    fig,axes=plt.subplots(1,2,figsize=(11.4,5.1),dpi=170)
    fig.patch.set_facecolor('white')
    ax=axes[0]
    ax.add_patch(Circle((0,0),1,facecolor='#dcecf9',edgecolor='#17638d',lw=1.8))
    ax.axvline(1,color='#a75c12',ls='--',lw=1.5)
    ax.scatter([1,2],[0,0],color=['#17638d','#963447'],s=32,zorder=5)
    ax.annotate(r'$x_0=1$',(1,0),xytext=(.42,-.5),fontsize=14,arrowprops={'arrowstyle':'-','color':'#4b5563'})
    ax.text(1.83,.16,r'$\zeta=2$',fontsize=14,color='#963447')
    ax.annotate('',xy=(2,-.15),xytext=(1,-.15),arrowprops={'arrowstyle':'<->','color':'#963447','lw':1.4,'shrinkA':0,'shrinkB':0})
    ax.plot([1,1],[0,-.15],color='#963447',lw=.8)
    ax.plot([2,2],[0,-.15],color='#963447',lw=.8)
    ax.text(1.35,-.4,r'$\delta=1$',fontsize=14,color='#963447')
    ax.text(-.55,.45,r'$K$',fontsize=22,color='#17638d')
    ax.text(.96,1.12,r'$\mathrm{Re}\,z=1$',fontsize=13,ha='center',color='#a75c12')
    ax.set_xlim(-1.35,2.55);ax.set_ylim(-1.55,1.5)
    ax.set_title('A separating line for the Cauchy kernel',fontsize=15,pad=16)
    ax.text(.6,-1.35,r'$\mathrm{Re}(z-2)\leq -1\quad(z\in K)$',fontsize=14,ha='center')
    ax=axes[1]
    for center in [-.5,.5]:ax.add_patch(Circle((center,0),1,fill=False,edgecolor='#94a3b8',lw=1.1,ls='--'))
    x=np.linspace(-.5,.5,701);y=np.sqrt(np.maximum(0,1-(np.abs(x)+.5)**2))
    ax.fill_between(x,-y,y,color='#dfecdc',alpha=.95)
    ax.plot(x,y,color='#347e47',lw=1.8);ax.plot(x,-y,color='#347e47',lw=1.8)
    ax.scatter([-.5,.5],[0,0],color='#64748b',s=20)
    ax.annotate('',xy=(.5,0),xytext=(-.5,0),arrowprops={'arrowstyle':'<->','color':'#17638d','lw':1.5,'shrinkA':0,'shrinkB':0})
    ax.text(0,-.19,r'$1$',fontsize=15,ha='center',color='#17638d')
    top=np.sqrt(3)/2
    ax.annotate('',xy=(1.48,top),xytext=(1.48,-top),arrowprops={'arrowstyle':'<->','color':'#8d3e9f','lw':1.5,'shrinkA':0,'shrinkB':0})
    ax.plot([0,1.48],[top,top],color='#8d3e9f',ls=':',lw=1)
    ax.plot([0,1.48],[-top,-top],color='#8d3e9f',ls=':',lw=1)
    ax.text(1.56,0,r'$\sqrt{3}$',fontsize=15,va='center',color='#8d3e9f')
    ax.text(-.76,-.35,r'$-\frac{1}{2}$',fontsize=13,color='#4b5563')
    ax.text(.52,-.35,r'$\frac{1}{2}$',fontsize=13,color='#4b5563')
    ax.set_xlim(-1.65,1.98);ax.set_ylim(-1.55,1.5)
    ax.set_title('A convex intersection that is not a disc',fontsize=15,pad=16)
    ax.text(.15,-1.35,r'$|z-\frac{1}{2}|<1,\quad |z+\frac{1}{2}|<1$',fontsize=14,ha='center')
    for ax in axes:
        ax.set_aspect('equal');ax.set_xlabel('real coordinate',fontsize=12);ax.set_ylabel('imaginary coordinate',fontsize=12)
        ax.set_xticks([-1,0,1,2]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.15);ax.tick_params(labelsize=10)
    axes[1].set_xticks([-1,0,1])
    fig.subplots_adjust(left=.065,right=.985,bottom=.13,top=.87,wspace=.26)
    out=HERE/'figures';out.mkdir(exist_ok=True)
    fig.savefig(out/'separated-kernel-and-convex-lens.png',metadata={'Software':'Matplotlib; GPT-6.1 Sol (OpenAI)'})
    svg=out/'separated-kernel-and-convex-lens.svg';fig.savefig(svg,metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI); Matplotlib'})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

if __name__=='__main__':main()
