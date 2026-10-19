"""Original diagrams for WD01–10. Run with --output-dir to reproduce elsewhere."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.spines.top':False,
                     'axes.spines.right':False,'savefig.facecolor':'white'})
BLUE='#155e8d'; ORANGE='#bb4a18'; INK='#152c3b'; GREEN='#126a59'

def canvas(title, subtitle):
    fig=plt.figure(figsize=(9,11),dpi=100)
    fig.text(.07,.957,title,size=23,weight='bold',color=INK)
    fig.text(.07,.918,subtitle,size=14,color=INK)
    return fig

def box(fig,xywh,title,body,color=BLUE):
    x,y,w,h=xywh
    fig.add_artist(FancyBboxPatch((x,y),w,h,transform=fig.transFigure,
                   boxstyle='round,pad=0.008',facecolor='#f3f7fa',edgecolor=color,lw=1.5))
    fig.text(x+.025,y+h-.033,title,size=16,weight='bold',color=color)
    fig.text(x+.025,y+h-.068,body,size=14,color=INK,va='top',linespacing=1.25)

def footer(fig,text):
    fig.text(.07,.028,text,size=10,color=INK,linespacing=1.35)

def render(out):
    out.mkdir(parents=True,exist_ok=True)
    fig=canvas('Closed graph, separable GNS space','Separable C*-algebra A; any lower-semicontinuous weight.')
    box(fig,(.07,.685,.86,.185),'WD01–02 · The separability argument',
        r'$F_m=\{x:\ \varphi(x^*x)\leq m^2\}$ has a countable norm-dense subset.'+'\n'
        'Bounded-energy approximants converge weakly in the GNS space.\n'
        'The closed span of their countable GNS images contains every\n'
        'finite-energy vector. No norm-dense finite ideal is assumed.')
    ax=fig.add_axes([.12,.34,.78,.28]);n=np.arange(1,9)
    ax.plot(n,1/n,'o-',color=BLUE,lw=2,label=r'$\|x_n\|_A=1/n$')
    ax.plot(n,np.ones_like(n),'s--',color=ORANGE,lw=2,label=r'$\|\Lambda(x_n)\|=1$')
    ax.set(xlabel='Index n (eight exact samples)',ylabel='Norm',xticks=n,ylim=(0,1.23))
    ax.grid(alpha=.2);ax.legend(loc='center right',fontsize=14)
    box(fig,(.07,.095,.86,.16),'WD03 · Weak convergence is the correct conclusion',
        r'$A=c_0,\quad \varphi(a)=\sum_{j\geq1}j^2a_j,\quad x_n=e_n/n$'+'\n'
        r'$x_n\to0$ in algebra norm; $\Lambda(x_n)=e_n\rightharpoonup0$.'+'\n'
        'The GNS norms stay equal to one for every n.',ORANGE)
    footer(fig,'Proofs: WD01–03, equations WD.1–WD.7. Samples illustrate the proved sequence.\nAntecedent: Takesaki, Theory of Operator Algebras II, VIII.4.9 (p.137). Original figure.')
    fig.savefig(out/'gns-closed-graphs.png');plt.close(fig)

    fig=canvas('Two density arguments in disintegration','Separable A; a faithful lower-semicontinuous modular weight\nwith a norm-dense finite domain.')
    box(fig,(.07,.685,.86,.18),'WD06–07 · First construct the compatible fibres',
        r'$\psi_y(a)=\Phi_y(\pi_y(a)),\qquad\varphi(a)=\int_Y\psi_y(a)\,d\mu(y)$'+'\n'
        'Use the actual fibre GNS spaces of the normal weights.\n'
        'A countable dense algebra × rational times gives one conull set.\n'
        'Norm continuity and modular continuity then give all elements/times.')
    box(fig,(.07,.435,.86,.20),'WD08 · Algebra norm density gives fibre semifiniteness',
        r'Choose a countable norm-dense family $d_j\in\mathfrak{m}_\varphi$.'+'\n'
        r'$\int_Y\psi_y(d_j^*d_j)\,d\mu=\varphi(d_j^*d_j)<\infty$.'+'\n'
        'Off a countable null union, all these elements are fibre-finite.\n'
        'Hence the fibre finite left ideal is norm dense in A.',GREEN)
    box(fig,(.07,.165,.86,.22),'WD08 · Hilbert density makes the fibre isometry onto',
        r'Choose $a_j\in\mathfrak{n}_\varphi$ with globally total $\Lambda(a_j)$.'+'\n'
        r'$P_y$: projection onto $\overline{\mathrm{span}}\{\Lambda_{\Phi_y}(\pi_y(a_j))\}$.'+'\n'
        r'Measurability gives $P=\int^\oplus P_y$; global totality gives $P=I$.'+'\n'
        r'Uniqueness gives $P_y=I$ almost everywhere.'+'\n'
        r'The isometry $V_y\Lambda_{\psi_y}(a)=\Lambda_{\Phi_y}(\pi_y(a))$ is onto.',ORANGE)
    fig.text(.09,.105,'On A, the GNS kernel of '+r'$\psi_y$ is exactly $\ker\pi_y$.',size=15,color=INK)
    footer(fig,'Proofs: WD06–09, equations WD.19–WD.30; projection and uniqueness: DF04, DF08.\nAntecedents: Takesaki, Theory of Operator Algebras II,\nVIII.4.11–13 (pp.138–140). Original diagram.')
    fig.savefig(out/'cstar-disintegration-fibres.png');plt.close(fig)

    fig=canvas('Finite positive weight ≠ finite GNS energy',r'$A=C_0((0,1]),\quad\varphi(f)=\int_0^1 y^{-2}f(y)\,dy,\quad f_\beta(y)=y^\beta$')
    ax=fig.add_axes([.12,.46,.78,.37]);b=np.linspace(.501,3,1400);c=np.linspace(1.001,3,1400)
    ax.plot(b,1/(2*b-1),color=BLUE,lw=2.5,label=r'GNS energy: $1/(2\beta-1)$')
    ax.plot(c,1/(c-1),color=ORANGE,lw=2.5,label=r'Positive weight: $1/(\beta-1)$')
    ax.axvline(.5,color=BLUE,ls=':',lw=1.5);ax.axvline(1,color=ORANGE,ls=':',lw=1.5)
    ax.scatter([.75],[2],s=65,color=BLUE,zorder=3)
    ax.annotate(r'$\beta=3/4$: energy $2$',(.75,2),xytext=(1.25,3.5),arrowprops={'arrowstyle':'->','color':BLUE},color=BLUE,fontsize=14)
    ax.set(xlim=(0,3),ylim=(0,8),xlabel=r'Exponent $\beta>0$',ylabel='Finite value (vertical display clipped at 8)')
    ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=13)
    box(fig,(.07,.24,.86,.145),'WD10 · The thresholds are different',
        r'$0<\beta\leq1/2$: both quantities are infinite.'+'\n'
        r'$1/2<\beta\leq1$: finite GNS energy; infinite positive weight.'+'\n'
        r'$\beta>1$: both are finite. The two boundary divergences are logarithmic.')
    box(fig,(.07,.065,.86,.12),'Every fibre evaluation is finite',
        r'$\psi_y(f_\beta)=y^{\beta-2},\quad y>0;\qquad\Lambda_{\psi_y}(f)=f(y)/y$'+'\n'
        'Finiteness at each point does not imply integrability over the base.',GREEN)
    footer(fig,'Proof: WD10, equations WD.31–WD.34. Curves show only the finite branches. Original example and figure.')
    fig.savefig(out/'cstar-weight-finite-domains.png');plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
    render(parser.parse_args().output_dir)
