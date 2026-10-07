"""Exact saturated Euler geometry and mean cost mechanism, original CC0.

GPT-6.1 Sol (OpenAI), Ultra; Figure10.17, complete10.84–10.87.
Human context: free Yu2013 equations2.8/4.23/5.6; own earlier proofs.
Finite support/phase/coordinates/eigenvalues are exact rational data.
"""
from pathlib import Path
from fractions import Fraction as Q
import json

POINTS=[(x,y) for x in range(9) for y in range(7) if (x+y)%2==0]
ORIGINAL=[(Q(x,2),Q(y,2)) for x,y in POINTS]
VALUES=[6*x-4*y for x,y in POINTS]
assert len(POINTS)==32 and (min(VALUES),max(VALUES))==(-24,48)
assert all(v==4*(3*mu[0]-2*mu[1]) for v,mu in zip(VALUES,ORIGINAL))

def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    plt.rcParams.update({'font.size':15,'font.family':'DejaVu Sans'})
    fig=plt.figure(figsize=(10.5,9.5))
    grid=fig.add_gridspec(2,2)
    axes=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1]),fig.add_subplot(grid[1,:])]
    norm=Normalize(-24,48)
    for ax,points,xmax,ymax,title,xlabel,ylabel in [
        (axes[0],POINTS,8,6,r'Integer support $\lambda$',r'$\lambda_1$',r'$\lambda_2$'),
        (axes[1],ORIGINAL,4,3,r'Original coordinates $\mu=B\lambda$',r'$\mu_1$',r'$\mu_2$')]:
        ax.plot([0,xmax,xmax,0,0],[0,0,ymax,ymax,0],color='#7a8493',lw=1.5)
        ax.scatter([float(p[0]) for p in points],[float(p[1]) for p in points],c=VALUES,
                   norm=norm,cmap='viridis',s=58,zorder=3,edgecolor='white',lw=.5)
        ax.set_title(title,pad=18);ax.set_xlabel(xlabel);ax.set_ylabel(ylabel)
        ax.set_xlim(-.6,xmax+.7);ax.set_ylim(-.6,ymax+.9);ax.set_aspect('equal')
        ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
        ax.annotate(r'$\omega=-24$',(0,ymax),xytext=(12,8),textcoords='offset points',fontsize=15)
        ax.annotate(r'$\omega=48$',(xmax,0),xytext=(-12,15),textcoords='offset points',ha='right',fontsize=15)
        ax.annotate(r'$\lambda_0=0$' if ax==axes[0] else r'$\mu_0=0$',(0,0),
                    xytext=(10,12),textcoords='offset points',fontsize=14)
    fractions=[Q(j,60) for j in range(21)]
    xs=[float(x) for x in fractions]
    euler=[Q(1,2)*(1-x) for x in fractions]
    clearing=[2*x for x in fractions]
    joint=[a+b for a,b in zip(euler,clearing)]
    assert all(x<=1 for x in joint) and joint[-1]==1
    ax=axes[2]
    ax.plot(xs,list(map(float,euler)),color='#176f98',lw=2.4,label=r'$\overline{h}/t_0=(1-a)/2$')
    ax.plot(xs,list(map(float,clearing)),color='#ae4c32',lw=2.4,label=r'$2\overline{u}/t_0=2a$')
    ax.plot(xs,list(map(float,joint)),color='#1c2737',lw=2.6,label='sum')
    ax.axhline(1,ls='--',color='#7a8493',lw=1.3)
    ax.set_xlim(0,1/3);ax.set_ylim(0,1.14)
    ax.set_xticks([0,1/6,1/3],['0',r'$1/6$',r'$1/3$'])
    ax.set_yticks([0,.5,1],['0',r'$1/2$','1'])
    ax.set_xlabel(r'$a=\overline{u}/t_0$');ax.set_ylabel('normalized mean orders')
    ax.set_title('The mean costs share one degree budget',pad=18)
    ax.grid(alpha=.18);ax.spines[['top','right']].set_visible(False)
    ax.legend(loc='upper left',fontsize=14,frameon=True,framealpha=.96,edgecolor='none')
    fig.suptitle(r'The saturated factor $J=4$ and the mean derivative allocation',fontsize=19,y=.975)
    fig.text(.525,.505,r'$B=\frac{1}{2} I,\quad \omega=6\lambda_1-4\lambda_2=4(3\mu_1-2\mu_2)$',ha='center',fontsize=15)
    fig.text(.525,.023,r'$r=2,\quad \overline{h}+2\overline{u}\leq t_0$',ha='center',fontsize=16)
    fig.subplots_adjust(left=.09,right=.97,top=.86,bottom=.1,wspace=.22,hspace=.66)
    target=Path(__file__).with_name('mean-clearing-euler.png')
    fig.savefig(target,dpi=155,facecolor='white');plt.close(fig)
    return target

if __name__=='__main__':
    print(json.dumps({'figure':str(figure()),'support_points':len(POINTS),'J':4,
                      'euler_min':min(VALUES),'euler_max':max(VALUES)}))
