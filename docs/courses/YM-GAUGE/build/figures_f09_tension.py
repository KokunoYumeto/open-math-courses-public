"""Exact specified Fourier decomposition and finite original heat kernel."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def build():
    out=Path(__file__).resolve().parents[1]/'figures'
    plt.rcParams.update({'svg.hashsalt':'YM-F09-tension-20261009',
     'font.size':11,'axes.labelsize':12,'axes.titlesize':13,'font.family':'DejaVu Sans'})
    fig,axes=plt.subplots(1,2,figsize=(12.8,6.2))
    fig.subplots_adjust(left=.08,right=.96,bottom=.25,top=.8,wspace=.35)
    B=np.array([2.,1.]);xi=np.array([1.,2.])
    cf=xi*np.dot(xi,B)/np.dot(xi,xi);df=B-cf
    ax=axes[0]
    for v,col,label in [(B,'#344957','B = (2, 1)'),(cf,'#126b75','Pcf B = (4/5, 8/5)'),(df,'#ad5d23','Pdf B = (6/5, −3/5)')]:
        ax.annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'->','color':col,'lw':2.4})
        ax.plot([],[],color=col,lw=2.4,label=label)
    ax.plot([cf[0],B[0]],[cf[1],B[1]],ls='--',color='#ad5d23',lw=1.4)
    ax.plot([df[0],B[0]],[df[1],B[1]],ls='--',color='#126b75',lw=1.4)
    ax.axhline(0,color='#aaaaaa',lw=.7);ax.axvline(0,color='#aaaaaa',lw=.7)
    ax.set(xlim=(-.2,2.35),ylim=(-.85,1.85),xlabel='First coefficient component (m²)',
     ylabel='Second coefficient component (m²)',title='Exact Hodge projection (NX.22, NX.45)')
    ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.15)
    handles,labels=ax.get_legend_handles_labels()
    fig.legend(handles,labels,loc='lower center',bbox_to_anchor=(.5,.11),
     ncol=3,frameon=False,fontsize=10)
    S=1.;s=np.geomspace(1e-5,S,1201)
    J=.5*np.log(S/s)**2;y=np.sqrt(s)*J
    axes[1].semilogx(s,y,color='#6b4a9b',lw=2.3)
    star=S*np.exp(-4);value=8*np.sqrt(S)/np.exp(2)
    axes[1].plot([star],[value],'o',color='#ad5d23',ms=7)
    axes[1].annotate('s = S exp(−4)\n8√S / e²',xy=(star,value),xytext=(.00012,.84),
     arrowprops={'arrowstyle':'->','color':'#344957'},fontsize=11)
    axes[1].set(xlim=(1e-5,1),ylim=(0,1.25),xlabel='Original heat time s (m²)',
     ylabel='√s J₀₀(s,S) (m)',title='Finite logarithmic kernel (NX.40–NX.41)')
    axes[1].grid(alpha=.2)
    fig.suptitle('An exact projection and the full temporal heat weight',fontsize=18,y=.96)
    fig.text(.5,.025,
     'Left: ξ = (1,2,0) m⁻¹ and one Fourier coefficient B = (2,1,0) m²; third components are zero.\n'
     'Right: S = 1 m², actual finite kernel; its continuous limit at s = 0 is zero. Proofs: NX.22–NX.28, NX.38–NX.41.',
     ha='center',va='bottom',fontsize=10)
    fig.savefig(out/'f09-tension-hodge.svg',metadata={'Date':None})
    fig.savefig(out/'f09-tension-hodge.png',dpi=150,metadata={'Software':'YM-GAUGE reproducible figure'})
    plt.close(fig)
if __name__=='__main__':build()
