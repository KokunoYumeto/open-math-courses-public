"""Exact sampled potentials of YM-F02 Example 5.2. Original figure: CC0-1.0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build():
    root=Path(__file__).resolve().parents[1]
    plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans',
                        'svg.fonttype':'none','svg.hashsalt':'YM-GAUGE-F02-gauge-pair-20261009'})
    fig,axes=plt.subplots(1,2,figsize=(12.8,6.4),layout='constrained')
    B0=2.0
    x,y=np.meshgrid(np.arange(-2,3,dtype=float),np.arange(-2,3,dtype=float))
    values=[(-B0*y/2,B0*x/2,'#176a87','A₁ = (−B₀x²/2, B₀x¹/2, 0)'),
            (np.zeros_like(x),B0*x,'#b55a24','A₂ = (0, B₀x¹, 0)')]
    for ax,(a1,a2,color,title) in zip(axes,values):
        ax.quiver(x,y,a1,a2,color=color,angles='xy',scale_units='xy',scale=5,
                  width=.006,headwidth=4,headlength=5,pivot='tail')
        ax.scatter(x,y,s=6,c='#263b43')
        ax.set(xlim=(-3,3),ylim=(-3,3),xlabel='First coordinate x¹ (m)',
               ylabel='Second coordinate x² (m)',title=title,aspect='equal')
        ax.grid(alpha=.18)
        ax.spines[['top','right']].set_visible(False)
    fig.suptitle('Different potentials; the same curl B = (0, 0, B₀)\n'
                 'B₀ = 2 N s/(C m),  x³ = 0,  A₁³ = A₂³ = 0',fontsize=16)
    fig.supxlabel('Arrow scale in both panels: 1 N s/C corresponds to 0.20 m on the coordinate axes.',fontsize=12)
    fig.savefig(root/'figures/f02-gauge-pair.svg',metadata={'Date':None,'Creator':'YM-GAUGE figure source; CC0-1.0'})
    fig.savefig(root/'figures/f02-gauge-pair.png',dpi=150,metadata={'Software':'YM-GAUGE figure source; CC0-1.0'})
    plt.close(fig)

if __name__=='__main__':build()
