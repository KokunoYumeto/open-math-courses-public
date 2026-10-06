"""Reproduce the exact scalar model in Resolvents, domains and spectral density.

Original plotting source by GPT-6.1 Sol (OpenAI), October 2026. CC0.
The samples illustrate the proved formula; they do not prove the bound.
"""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def render(output):
    plt.rcParams.update({'font.size':12,'svg.fonttype':'none'})
    x=np.unique(np.r_[np.linspace(-4,4,2401),-2,2])
    fig,ax=plt.subplots(figsize=(9.2,5.3),layout='constrained')
    for eps,color,label in [(0.5,'#2563eb','1/2'),(0.2,'#0891b2','1/5'),(0.05,'#b45309','1/20')]:
        values=np.arctan((2-x)/eps)-np.arctan((-2-x)/eps)
        ax.plot(x,values,color=color,lw=2,label=r'$\varepsilon='+label+'$')
    for lo,hi,value in [(-4,-2,0),(-2,2,np.pi),(2,4,0)]:
        ax.plot([lo,hi],[value,value],color='#111827',ls='--',lw=1.7,
                label='Pointwise limit' if lo==-4 else None)
    ax.scatter([-2,-2,2,2],[0,np.pi,0,np.pi],facecolors='white',edgecolors='#111827',s=48,zorder=5)
    ax.scatter([-2,2],[np.pi/2,np.pi/2],color='#111827',s=42,zorder=6)
    ax.annotate(r'$(-2,\pi/2)$',(-2,np.pi/2),xytext=(-3.7,1.95),
                arrowprops={'arrowstyle':'->','color':'#374151'})
    ax.annotate(r'$(2,\pi/2)$',(2,np.pi/2),xytext=(2.45,1.95),
                arrowprops={'arrowstyle':'->','color':'#374151'})
    ax.set(xlim=(-4,4),ylim=(-0.12,3.48),xlabel=r'Energy $\lambda$',
           ylabel=r'$F_{\varepsilon,f}(\lambda)=\operatorname{Im}(R_A(\lambda+i\varepsilon)f,f)$',
           title='A uniform bound can coexist with a discontinuous limit')
    ax.set_yticks([0,np.pi/2,np.pi],['0',r'$\pi/2$',r'$\pi$'])
    ax.set_xticks([-4,-2,0,2,4]);ax.grid(alpha=.17)
    ax.legend(loc='upper right',ncol=2,fontsize=10,framealpha=1)
    fig.savefig(output)
    plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    render(args.output or Path(__file__).with_suffix('.svg'))
