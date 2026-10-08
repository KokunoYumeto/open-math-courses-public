"""Original weighted-basis geometry and exact universal coefficient bounds. CC0."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('dependent_enclosures',HERE/'yu_dependent_application_enclosures.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
data=cert.certificate();upper=F(data['coefficient_normalized_upper'])

def draw(output):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,bars)=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1.1,1]})
    fig.patch.set_facecolor('white')
    ax.set_xlim(-.2,5.9);ax.set_ylim(-.25,1.8);ax.set_aspect('equal',adjustable='box')
    ax.axhline(0,color='#77808f',lw=.8);ax.axvline(0,color='#77808f',lw=.8)
    for x,y,color,label,offset in [(1,0,'#26715d','2: (1, 0)',(0,-.14)),(0,1,'#26715d','3: (0, 1)',(.15,.04)),(2,0,'#b0612f','4: (2, 0)',(.1,.08))]:
        ax.annotate('',xy=(x,y),xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':color})
        ax.scatter([x],[y],s=50,color=color,zorder=4);ax.text(x+offset[0],y+offset[1],label,color=color,fontsize=11)
    ax.plot([0,5],[0,1],'--',color='#7545a0',lw=1.4);ax.scatter([5],[1],s=55,color='#7545a0')
    ax.text(4.0,1.2,r'$\Xi=96$: (5, 1)',color='#7545a0')
    ax.text(2.6,1.47,r'$v(4)=2v(2)$',ha='center',color='#4b5563')
    ax.set_xticks(range(6));ax.set_yticks([0,1]);ax.set_xlabel(r'Prime valuation $v_2(a)$');ax.set_ylabel(r'Prime valuation $v_3(a)$')
    ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
    ax.set_title('Exact indexed list: 2, 3, 4 at p = 5',fontsize=15,pad=25)
    fig.text(.23,.245,'Greedy basis: (2, 3), rank 2, residue index 1\n'+r'$4\cdot2^{-2}=1$: (1, 1, 2) → (5, 1)'+'\nB = 3: the local-height branch applies.',ha='center',va='center',fontsize=11,linespacing=1.55)
    bounds=[upper,upper*F(3,8),upper*F(3,56)]
    labels=['Terminal removal','Internal: largest base selected','Internal: largest base unselected']
    vals=[]
    for v in bounds:
        scaled=v*10**6;vals.append((scaled.numerator+scaled.denominator-1)//scaled.denominator/10**6)
    bars.barh(range(3),vals,height=.48,color=['#264f88','#26715d','#b0612f'])
    bars.set_yticks(range(3),labels);bars.invert_yaxis();bars.set_xlim(0,1.12)
    for i,v in enumerate(vals):
        bars.text(v-.02 if i==0 else v+.02,i,f'<{v:.6f}',ha='right' if i==0 else 'left',va='center',fontsize=12,color='white' if i==0 else '#17202a')
    bars.axvline(1,color='#bc4634',ls='--',lw=1.2);bars.text(.985,-.32,'threshold 1',ha='right',color='#bc4634',fontsize=11)
    bars.set_xlabel('Normalized circuit coefficient upper bound')
    bars.set_title('All original fields, ranks and circuits',fontsize=15,pad=25)
    bars.grid(axis='x',alpha=.18);bars.set_axisbelow(True);bars.spines[['top','right']].set_visible(False)
    fig.text(.5,.025,'Lemma 10.155 proves the three envelopes; Theorem 10.156 performs the complete main-bound induction.',ha='center',fontsize=11,color='#4b5563')
    fig.tight_layout(rect=(0,.17,1,1));fig.savefig(output,dpi=150,facecolor='white');plt.close(fig)

if __name__=='__main__':draw(HERE.parent/'figures/yu-dependent-application.png' if HERE.name=='figure_sources' else HERE/'yu-dependent-application.png')
