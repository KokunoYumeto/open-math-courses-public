"""Exact heat-polynomial distances; AN01-U137, Exercise 19. CC0 1.0.

The curves are evaluations of the proved formulas H15 and H17.
They are not numerical estimates of a complex minimization problem.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def distance(t):
    t=np.asarray(t,dtype=float)
    return np.where(t<=0.5,t,np.sqrt(np.maximum(t-0.25,0)))

def main(out):
    plt.rcParams.update({'font.size':12,'axes.titlesize':14,'figure.facecolor':'white',
                         'svg.hashsalt':'AN01-U137-hypoelliptic-distance-and-heat'})
    fig,ax=plt.subplots(1,2,figsize=(12,4.8),layout='constrained')
    t=np.linspace(0,6,1201)
    ax[0].plot(t,distance(t),lw=2.5,color='#15659d',label=r'$d_P(0,T)$')
    ax[0].plot(t,np.sqrt(t),ls='--',color='#bd6633',label=r'$\sqrt{T}$')
    ax[0].scatter([.5],[.5],color='#15659d',zorder=5)
    ax[0].annotate('Nearest zero changes\nat T = 1/2',(.5,.5),(1.5,.18),
                   arrowprops={'arrowstyle':'->','color':'#444444'},fontsize=11)
    ax[0].set(xlabel=r'Real frequency $T$',ylabel='Distance in complex frequency space',
              title=r'$P(z,w)=z^2+iw$: exact distance',xlim=(0,6),ylim=(0,2.6))
    t=np.geomspace(.03,1e4,1000)
    inv_scale=np.minimum(t,np.sqrt(t))
    ax[1].loglog(t,distance(t),lw=2.5,color='#15659d',label=r'$d_P(0,T)$')
    ax[1].loglog(t,inv_scale,ls='--',lw=1.8,color='#8844a5',
                 label=r'$1/T_P(0,T)=\min(T,\sqrt{T})$')
    ax[1].set(xlabel=r'Real frequency $T$',ylabel='Distance or reciprocal derivative scale',
              title='Derivative scale and zero separation')
    for a in ax:
        a.grid(alpha=.2,which='both');a.legend(loc='upper left',frameon=True)
    fig.savefig(out.with_suffix('.png'),dpi=180)
    svg=out.with_suffix('.svg')
    fig.savefig(svg,metadata={'Date':None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
    plt.close(fig)

if __name__=='__main__':
    main(Path(__file__).with_suffix(''))
