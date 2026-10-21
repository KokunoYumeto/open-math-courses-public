"""The exact dependent radius, CC0, GPT-6 Astra (OpenAI)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main(output):
    degrees=np.unique(np.rint(np.geomspace(1,10**6,500)).astype(int))
    ln2=np.log(2.)
    exact=np.log(degrees)-np.log(ln2)
    height=(degrees+1)*ln2
    assert np.all(exact>0) and np.all(height>exact)
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(figsize=(8.4,4.9),layout='constrained')
    ax.loglog(degrees,height,color='#b56b20',lw=2,label=r'Height estimate: $(D+1)\log 2$')
    ax.loglog(degrees,exact,color='#17667c',lw=2.5,label=r'Exact radius: $\log D-\log\log 2$')
    for d in [1,100,10**6]:
        ax.scatter([d],[np.log(d)-np.log(ln2)],s=28,color='#17667c',zorder=4)
    ax.annotate(r'$D=100$: exact cost $\approx4.972$',(100,np.log(100)-np.log(ln2)),
                xytext=(22,-37),textcoords='offset points',
                arrowprops={'arrowstyle':'->','color':'#17667c'},fontsize=10)
    ax.set(xlabel='Field degree $D$ (integer samples)',ylabel=r'Cost $C$ in $\log|\Gamma|\geq-C$',
           title=r'$\beta=2^{1/D}$, $\Gamma=\log\beta$, $E=D+1$')
    ax.grid(which='major',alpha=.2);ax.legend(loc='upper left',fontsize=10)
    fig.savefig(output,dpi=160);plt.close(fig)


if __name__=='__main__':
    target=Path(__file__).resolve().parent/'dependent-exact-radius.png'
    main(target)
