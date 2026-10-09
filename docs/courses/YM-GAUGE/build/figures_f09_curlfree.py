"""Original finite backward kernel and the complete physical Morrey radius bound."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def build():
    out=Path(__file__).resolve().parents[1]/'figures'
    plt.rcParams.update({'svg.hashsalt':'YM-F09-curlfree-20261009',
     'font.size':11,'axes.labelsize':12,'axes.titlesize':13,'font.family':'DejaVu Sans'})
    fig,axes=plt.subplots(1,2,figsize=(12.8,6.2))
    fig.subplots_adjust(left=.08,right=.96,bottom=.25,top=.8,wspace=.33)
    S=4.;s=np.geomspace(.001,S,1001)
    for alpha,col in [(.75,'#126b75'),(.125,'#ad5d23')]:
        row=np.sqrt((1-(s/S)**(2*alpha))/(2*alpha))
        axes[0].semilogx(s,row,color=col,lw=2.3,label=f'α = {alpha:g}')
    axes[0].set(xlabel='Original heat time s (m²)',ylabel='Exact squared-kernel row norm',
     title='Finite backward operator (CF.19–CF.20)',xlim=(.001,S),ylim=(0,2.1))
    axes[0].legend(frameon=False);axes[0].grid(alpha=.2)
    D0=(3/(4*np.pi))**.25;A=(12*np.pi)**.75/(4*np.pi);U=2.;V=1.
    star=3*D0*U/(A*V);R=np.geomspace(.05,20,1001)
    avg=D0*U*R**(-.75);grad=A*V*R**.25
    axes[1].semilogx(R,avg,color='#126b75',lw=1.8,label='Ball average term')
    axes[1].semilogx(R,grad,color='#ad5d23',lw=1.8,label='Gradient term')
    axes[1].semilogx(R,avg+grad,color='#6b4a9b',lw=2.5,label='Complete bound')
    value=D0*U*star**(-.75)+A*V*star**.25
    axes[1].plot([star],[value],'o',color='#344957',ms=6)
    axes[1].annotate('R = 3D₀U/(AV)',xy=(star,value),xytext=(.25,6.5),
     arrowprops={'arrowstyle':'->','color':'#344957'},fontsize=11)
    axes[1].set(xlabel='Original ball radius R (m)',ylabel='Upper bound for |u| (m⁻¹)',
     title='Keep both contributions (CF.24–CF.25)',xlim=(.05,20),ylim=(0,14))
    axes[1].legend(frameon=False,loc='upper right');axes[1].grid(alpha=.2)
    fig.suptitle('Finite heat weights and the radius that minimizes the complete bound',fontsize=17,y=.96)
    fig.text(.5,.06,
      'Left: S = 4 m²; the displayed lower heat time is a viewing limit, not a changed endpoint.\n'
      'Right: U = 2 m⁻¹/⁴, V = 1 m⁻⁵/⁴. Both panels are exact scalar bounds; they are not sampled Yang–Mills fields.',
      ha='center',va='bottom',fontsize=10)
    fig.savefig(out/'f09-curlfree-backward.svg',metadata={'Date':None})
    fig.savefig(out/'f09-curlfree-backward.png',dpi=150,metadata={'Software':'YM-GAUGE reproducible figure'})
    plt.close(fig)
if __name__=='__main__':build()
