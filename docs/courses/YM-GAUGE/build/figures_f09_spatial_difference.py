from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
F=Path(__file__).resolve().parents[1]/'figures'
def build():
    plt.rcParams.update({'svg.hashsalt':'YM-GAUGE-F09-differences','svg.fonttype':'none','font.size':11})
    S = 4.0
    s = np.geomspace(0.002, S, 600)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.7), gridspec_kw={'width_ratios':[1,1.25]})
    fig.patch.set_facecolor('#fcfcfa')
    ax = axes[0]
    for alpha, color, label in [(3/4,'#245c9e',r'$\alpha=3/4$ (LG.18)'),
                               (1/8,'#bd5c23',r'$\alpha=1/8$ (LG.26)')]:
        ax.plot(s, np.sqrt((1-(s/S)**(2*alpha))/(2*alpha)), color=color, lw=2.2, label=label)
        ax.axhline((2*alpha)**(-0.5), color=color, ls='--', lw=1)
    ax.set_xscale('log')
    ax.set_xlim(s[0],S)
    ax.set_ylim(0,2.12)
    ax.set_xlabel(r'Original heat time $s$ (square metres); $S=4$ square metres')
    ax.set_ylabel(r'Exact squared-kernel row norm in $L^2(dr/r)$')
    ax.set_title('Finite interval, retained upper endpoint', pad=12)
    ax.grid(alpha=.16)
    ax.legend(loc='lower left',framealpha=.93)
    
    ax = axes[1]
    ax.axis('off')
    ax.set_title(r'Actual difference field: $Z=G-G^\prime$', pad=12)
    rows = [
        (.88, r'$Z(s)=Z(S)-\int_s^S(\Delta Z+N^\delta)(r)\,dr$', 'LG.17: exact field identity'),
        (.65, r'$D_2^\delta\leq d_c\mathcal{F}_{5/2}^{\delta,2}$', 'LG.20: full difference wave norm; original speed c'),
        (.43, r'$\delta g^2\leq\sqrt{2/3}S^{3/4}Z_4^\delta$', ''),
        (.32, r'$\quad+\frac{4}{3}(\sqrt{3}d_c\mathcal{F}_{5/2}^{\delta,2}+\mathcal{N}_\delta)$', 'LG.18 and LG.21: actual endpoint retained'),
        (.09, r'$L_Q\leq4(\delta e\,g+e^\prime\mathcal{G}_\delta^2)$', 'LG.31: input to the temporal-boundary estimate')
    ]
    for y, formula, subtitle in rows:
        ax.text(.02,y,formula,fontsize=15,color='#17324d',transform=ax.transAxes)
        if subtitle:
            ax.text(.02,y-.065,subtitle,fontsize=10,color='#555555',transform=ax.transAxes)
    fig.subplots_adjust(left=.07,right=.98,bottom=.20,top=.88,wspace=.35)
    fig.text(.07,.055,'Dashed lines are the proved limiting row bounds; each row norm vanishes at s = S.\n'
             'The graph depicts exact scalar kernels, not sampled Yang–Mills solutions. Superscript 2 labels heat integrability.',
             fontsize=10,color='#444444')
    fig.savefig(F/'f09-spatial-difference.png',dpi=170)
    fig.savefig(F/'f09-spatial-difference.svg',metadata={'Date':None})
    plt.close(fig)
if __name__=='__main__':build()
