"""Original application-bound proof diagram and exact finite margins. CC0."""
from pathlib import Path
import importlib.util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from fractions import Fraction as F
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('application_certificate',HERE/'yu_application_height_certificate.py')
cert=importlib.util.module_from_spec(spec);spec.loader.exec_module(cert)
rows=cert.certificate()['rows']

def draw(output):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
    fig,(ax,bars)=plt.subplots(1,2,figsize=(14,7),gridspec_kw={'width_ratios':[1.4,1]})
    fig.patch.set_facecolor('white');ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
    def box(x,y,w,h,text,color):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.1',linewidth=1.1,edgecolor=color,facecolor=color+'12'))
        ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,linespacing=1.5)
    def arrow(a,b):ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.4,'color':'#4b5563'})
    box(1.2,8.5,7.6,1.0,'Independent local units: n ≥ 2\n'+r'Compare $B/\ln B$ with $W_B$','#264f88')
    box(.2,5.3,4.25,2.05,r'$B/\ln B\leq W_B$'+'\nLocal height inequality\nSmall remainder: < 1/7900\nTotal strictly below target','#26715d')
    box(5.0,5.3,4.75,2.05,r'$B/\ln B>W_B$'+'\nLemma 10.153 supplies the heights\n'+r'$\mathsf{h}\leq(n+1)H$'+'\nApply Theorem 10.152','#7545a0')
    arrow((3,8.4),(2.3,7.5));arrow((7,8.4),(7.4,7.5))
    box(1,2.6,8,1.7,'Theorem 10.154\n'+r'$\operatorname{ord}_{\mathfrak{p}}(\Xi-1)<\mathcal{T}=C_1^*\Omega H$','#264f88')
    arrow((2.3,5.2),(3.0,4.4));arrow((7.4,5.2),(7,4.4))
    box(.6,.5,8.8,1.2,'Rank one: two elementary contributions\n'+r'$1/2688+1/10000<1/2100$'+' of the same target','#b0612f')
    ax.set_title('Maximum-coefficient bound: both branches',fontsize=15,pad=20)
    vals=[]
    for row in rows:
        x=F(row['minimum_exact_log_margin'])*10**6
        vals.append((x.numerator//x.denominator)/10**6)
    bars.barh(range(7),vals,height=.6,color=['#264f88' if x['case']!='IV' else '#b0612f' for x in rows])
    bars.set_yticks(range(7),[x['case'] for x in rows]);bars.invert_yaxis();bars.set_xlim(0,.061)
    for i,v in enumerate(vals):bars.text(v+.001,i,f'>{v:.6f}',va='center',fontsize=11)
    bars.set_xlabel('Strict lower logarithmic threshold margin')
    bars.set_title('Every exact rank 2–511, seven cases',fontsize=15,pad=20)
    bars.grid(axis='x',alpha=.2);bars.set_axisbelow(True);bars.spines[['top','right']].set_visible(False)
    fig.text(.5,.025,'For all n ≥ 512: the factorial and positive-series proof in Lemma 10.153 supplies the remaining ranks.',ha='center',fontsize=11,color='#4b5563')
    fig.tight_layout(rect=(0,.07,1,1));fig.savefig(output,dpi=150,facecolor='white');plt.close(fig)

if __name__=='__main__':draw(HERE.parent/'figures/yu-application-height.png' if HERE.name=='figure_sources' else HERE/'yu-application-height.png')
