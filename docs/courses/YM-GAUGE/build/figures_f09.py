"""Reproducible causal-section and covariant-projection teaching figure."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def build(preview=None):
    matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
        'svg.hashsalt':'YM-F09-causal-projection-v1','axes.titleweight':'bold'})
    fig,axes=plt.subplots(1,2,figsize=(13,8.5),gridspec_kw={'width_ratios':[1,1.1]})
    fig.set_facecolor('#fffef9')
    teal='#246d75';gold='#a56820';dark='#183b48'
    ax=axes[0];ax.set_facecolor('#fffef9')
    y=np.array([0.,2.])
    ax.fill_betweenx(y,-2+y,2-y,color='#dceee8')
    ax.plot([-2,0,2],[0,2,0],color=teal,linewidth=2.5)
    ax.plot([-2,2],[0,0],color=teal,linewidth=5)
    ax.plot([-1,1],[1,1],color=gold,linewidth=2,linestyle='--')
    ax.annotate('',xy=(1,1),xytext=(0,1),
                arrowprops=dict(arrowstyle='<->',color=gold,lw=1.5))
    ax.text(0.5,1.12,'1 m',ha='center',color=gold)
    ax.text(0,.48,r'$U(t,x)=V(t,x)$',ha='center',color=dark,fontsize=16)
    ax.text(0,-.25,'Initial data agree on the ball',ha='center',color=dark)
    ax.set_xlim(-2.45,2.45);ax.set_ylim(-.42,2.32);ax.set_aspect('equal',adjustable='box')
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([0,1,2])
    ax.set_xlabel(r'$x^1$ (metres)')
    ax.set_ylabel(r'$ct$ (metres); physical time is $t$')
    ax.set_title('Domain of dependence',pad=14,color=dark)
    ax.text(.5,-.24,'Section: '+r'$x^2=x^3=0$'+'\n'+r'$|x|<R-ct,\quad R=2$ metres',
            transform=ax.transAxes,ha='center',va='top',fontsize=12,color=dark)
    ax.spines[['top','right']].set_visible(False)
    ax=axes[1];ax.set_facecolor('#fffef9');ax.set_aspect('equal')
    ax.set_xlim(-.45,4.2);ax.set_ylim(-.55,3.05);ax.axis('off')
    ax.axhline(0,color='#adc2c0',linewidth=1);ax.axvline(0,color='#adc2c0',linewidth=1)
    def arrow(start,end,color):
        ax.annotate('',xy=end,xytext=start,
                    arrowprops=dict(arrowstyle='-|>',color=color,lw=2.6,mutation_scale=17))
    arrow((0,0),(3,0),teal)
    arrow((0,0),(0,2),gold)
    arrow((0,0),(3,2),dark)
    arrow((3,2),(3,0),gold)
    ax.plot([0,3],[2,2],linestyle=':',color='#9bb2b8')
    ax.plot([.22,.22,0],[0,.22,.22],color=teal)
    ax.text(1.5,-.28,r'$e=P_a f$',ha='center',color=teal,fontsize=17)
    ax.text(3.15,2.05,r'$f$',color=dark,fontsize=18)
    ax.text(3.17,1.1,r'$+D^a\phi$',color=gold,fontsize=15)
    ax.text(.13,1.17,r'$-D^a\phi$',color=gold,fontsize=15)
    ax.text(1.3,2.65,r'$f=P_a f-D^a\phi$',ha='center',color=dark,fontsize=16)
    ax.set_title('Repairing Gauss law',pad=14,color=dark)
    ax.text(.5,-.17,'Two-dimensional section of the '+r'$L^2$'+' decomposition\n'
            'Lengths are illustrative; orthogonality is exact.',
            transform=ax.transAxes,ha='center',va='top',fontsize=12,color=dark)
    fig.text(.5,.125,r'$\operatorname{div}_a(P_a f)=0,\qquad'
             r'\langle P_a f,D^a\phi\rangle_{L^2}=0,\qquad'
             r'\|P_a f\|_2^2+\|D^a\phi\|_2^2=\|f\|_2^2$',
             ha='center',fontsize=15,color=dark)
    fig.text(.5,.045,'Proofs: F9.32–F9.34 (causal section); F9.39–F9.45 (projection and smooth constrained data).',
             ha='center',fontsize=11,color=dark)
    fig.subplots_adjust(left=.07,right=.98,top=.88,bottom=.38,wspace=.3)
    target=Path(__file__).resolve().parents[1]/'figures/f09-propagation-projection.svg'
    target.parent.mkdir(exist_ok=True)
    fig.savefig(target,format='svg',metadata={'Date':None,'Title':'Causal domain and orthogonal Gauss projection',
        'Description':'Exact x2=x3=0 section of a ball shrinking at physical speed c, with R=2 metres. Schematic Hilbert-space section of f=P_a f-D_a phi; lengths illustrative and orthogonality exact. Proofs F9.32–F9.45.'})
    if preview:fig.savefig(preview,dpi=150)
    plt.close(fig)

if __name__=='__main__':
    build()
