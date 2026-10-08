"""Original proof-route diagram and certified coefficient gaps. CC0."""
from pathlib import Path
import importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('yu_certificate',HERE/'yu_first_main_bound_certificate.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
rows=cert.certificate()['rows']

def draw(output):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,bars)=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1.45,1]})
    fig.patch.set_facecolor('white');ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
    def box(x,y,w,h,text,color):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.10',
                     linewidth=1.1,edgecolor=color,facecolor=color+'12'))
        ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,linespacing=1.55)
    def arrow(a,b):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.4,'color':'#4b5563'})
    box(1.4,8.5,7.2,1.0,'Original independent bases: n ≥ 2\nLeast admissible rank 1 ≤ r ≤ n','#264f88')
    box(.2,5.6,4.1,1.9,'r = 1\nActual residue order g\nPower identity + Theorem 10.21','#26715d')
    box(5.0,5.6,4.7,1.9,'r ≥ 2\nGeometric stop: Theorem 10.141\nMultiplicity stop: Corollary 10.150','#7545a0')
    arrow((3,8.4),(2.3,7.6));arrow((7,8.4),(7.4,7.6))
    box(.2,3.0,4.1,1.7,'Two elementary contributions\n< 1/400 + 1/4000\nof the final target','#26715d')
    box(5.0,3.0,4.7,1.7,r'$\operatorname{ord}_{\mathfrak{p}}(\Xi-1)<eU_r$'+'\nHeight profile cancels Mᵣ\nRemaining rank ratio ≤ 1','#7545a0')
    arrow((2.3,5.5),(2.3,4.8));arrow((7.4,5.5),(7.4,4.8))
    box(1.0,.35,8.0,2.05,'Theorem 10.152\n'+r'$\operatorname{ord}_{\mathfrak{p}}(\Xi-1)<C_1\,\mathsf{h}\,\prod_{j=1}^n h(a_j)$','#264f88')
    arrow((2.3,2.9),(3.0,2.5));arrow((7.4,2.9),(7.0,2.5))
    ax.set_title('The complete least-rank argument',fontsize=16,pad=20)
    vals=[x['strict_gap_per_million']/10**6 for x in rows]
    colors=['#264f88' if x['case']!='III.2' else '#bb6330' for x in rows]
    bars.barh(range(7),vals,color=colors,height=.6)
    bars.set_yticks(range(7),[x['case'] for x in rows]);bars.invert_yaxis()
    bars.set_xscale('log');bars.set_xlim(.001,2)
    bars.set_xlabel('Strict lower coefficient gap (log scale)')
    bars.grid(axis='x',which='both',alpha=.2);bars.set_axisbelow(True)
    for i,val in enumerate(vals):bars.text(val*1.08,i,f'>{val:.6f}',va='center',fontsize=11)
    bars.set_title('All ranks r ≥ 2, Lemma 10.151',fontsize=15,pad=20)
    bars.spines[['top','right']].set_visible(False)
    fig.text(.5,.025,'Exact rational endpoints + a proved decreasing enclosure; both IV branches use the same row.',
             ha='center',fontsize=11,color='#4b5563')
    fig.tight_layout(rect=(0,.07,1,1));fig.savefig(output,dpi=150,facecolor='white');plt.close(fig)

if __name__=='__main__':draw(HERE.parent/'figures/yu-first-main-bound.png' if HERE.name=='figure_sources' else HERE/'yu-first-main-bound.png')
