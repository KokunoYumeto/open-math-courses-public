"""Reproducible exact permutation/shift diagram for UC01–02."""
from pathlib import Path
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def render():
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,axes=plt.subplots(3,1,figsize=(9,9),dpi=100)
    fig.patch.set_facecolor('white')
    blue='#14648b';red='#b1443b';grey='#75858b'
    for ax,N in zip(axes,[3,5,None]):
        ax.set_xlim(-0.7,7.4);ax.set_ylim(-0.68,1.2);ax.axis('off')
        for k in range(7):
            ax.plot(k,0,'o',color=blue,markersize=8)
            ax.text(k,-.24,rf'$e_{k}$',ha='center',va='top',fontsize=13)
        title=rf'$u_{N}$: cycle $0\to1\to\cdots\to {N}\to0$' if N is not None else r'$S$: the limiting forward shift'
        ax.text(-.45,1.01,title,fontsize=15,color='#173441',va='top')
        end=N if N is not None else 6
        for k in range(end):
            ax.add_patch(FancyArrowPatch((k+.13,.03),(k+.86,.03),arrowstyle='-|>',mutation_scale=16,lw=2,color=blue))
        if N is not None:
            ax.add_patch(FancyArrowPatch((N,.13),(0,.13),connectionstyle='arc3,rad=.33',arrowstyle='-|>',mutation_scale=16,lw=2,color=red))
            ax.text(N/2,.57,rf'$u_{N}^*e_0=e_{N}$',ha='center',color=red,fontsize=14)
            for k in range(N+1,7):
                ax.add_patch(FancyArrowPatch((k-.14,.1),(k+.14,.1),connectionstyle='arc3,rad=-2',arrowstyle='-|>',mutation_scale=12,lw=1.4,color=grey))
            ax.text(3,-.57,rf'Indices $k>{N}$ are fixed.',ha='center',color=grey,fontsize=11)
        else:
            ax.add_patch(FancyArrowPatch((6.13,.03),(7.12,.03),arrowstyle='-|>',mutation_scale=16,lw=2,color=blue,linestyle='--'))
            ax.text(0,.55,r'No vector maps to $e_0$',ha='left',color=red,fontsize=13)
            ax.text(3,-.57,r'$\|e_3-e_5\|=\sqrt{2}$: the inverse images are not Cauchy.',ha='center',fontsize=12,color=red)
    fig.subplots_adjust(left=.06,right=.98,top=.97,bottom=.035,hspace=.19)
    out=io.BytesIO();fig.savefig(out,format='png',dpi=100,metadata={'Software':'OA-MOD exact UC diagram'});plt.close(fig)
    return out.getvalue()

if __name__=='__main__':
    target=Path(__file__).with_name('automorphism-two-sided-limit.png')
    target.write_bytes(render())
    print(str(target))
