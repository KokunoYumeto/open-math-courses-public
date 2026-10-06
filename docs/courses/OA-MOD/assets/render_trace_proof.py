"""Original reproducible proof-object diagrams; CC0-1.0 plotting code."""
from pathlib import Path
import sys
if sys.flags.optimize:raise RuntimeError('Figure validation requires assertions; run Python without -O or -OO')
import argparse, hashlib, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
INK='#172438';BLUE='#185aa0';GREEN='#087c68'
def panel(ax,y,title,body,h=.17,color=BLUE):
    ax.add_patch(FancyBboxPatch((.05,y),.90,h,boxstyle='round,pad=.01,rounding_size=.01',facecolor='#f4f8fc',edgecolor=color,linewidth=1.5))
    ax.text(.5,y+h-.02,title,ha='center',va='top',color=color,fontsize=14,fontweight='bold')
    ax.text(.5,y+h-.06,body,ha='center',va='top',color=INK,fontsize=12,linespacing=1.55)
def arrow(ax,y):
    ax.annotate('',xy=(.5,y-.037),xytext=(.5,y+.01),arrowprops={'arrowstyle':'->','lw':1.7,'color':INK})
def save(fig,p):
    assert not p.exists(),p
    fig.savefig(p,dpi=220,facecolor='white',metadata={'Software':'OA-MOD original plotting code','Copyright':'CC0-1.0'})
    plt.close(fig)
def render(out):
    out.mkdir(parents=True,exist_ok=True)
    fig=plt.figure(figsize=(4.4,10.2));ax=fig.add_axes((.02,.01,.96,.98));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.99,'A trace from one finite corner',ha='center',va='top',fontsize=16,fontweight='bold',color=INK)
    panel(ax,.775,'Source: the finite corner',r'$\theta:(pMp)_+\longrightarrow[0,\infty)$'+'\nNonzero, normal, finite trace.\nFaithfulness is not assumed.',h=.16)
    arrow(ax,.756)
    panel(ax,.545,'Orthogonal outgoing ranges',r'$v_i^*v_i=e_i\leq p,\quad v_iv_i^*=r_i$'+'\n'+r'$r_i\perp r_j,\quad\sum_i r_i=z=c(p)$'+'\nThe initial corners may repeat.',h=.17)
    arrow(ax,.527)
    panel(ax,.310,'Typed matrix entries',r'$a_{ji}=v_j^*av_i\in e_jMe_i\subseteq pMp$'+'\n'+r'$a\in Mz$'+'\nEach block lies in the trace domain.',h=.17)
    arrow(ax,.292)
    panel(ax,.067,'Nonnegative double sums',r'$\Theta(a^*a)=\sum_{i,j}\theta(a_{ji}^*a_{ji})$'+'\n'+r'$=\sum_{j,i}\theta(a_{ji}a_{ji}^*)=\Theta(aa^*)$'+'\nNormality inserts the range sum.',h=.185,color=GREEN)
    ax.text(.5,.009,'TE-07–08; TE.13–17. Any index set I.\nSums: finite-subset suprema.\nAntecedent: Takesaki I, V.2.14–2.15.',ha='center',va='bottom',fontsize=10,color=INK)
    save(fig,out/'trace-corner-matrix-v004.png')
    fig=plt.figure(figsize=(4.4,10.2));ax=fig.add_axes((.02,.01,.96,.98));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.99,'Filling central trace supports',ha='center',va='top',fontsize=16,fontweight='bold',color=INK)
    panel(ax,.780,'Local nonzero trace',r'$0\ne\Theta\text{ on }Mc(p)$'+'\nRemove its largest null projection.\nThe trace makes that projection central.',h=.155)
    arrow(ax,.763)
    panel(ax,.545,'Disjoint central trace supports',r'$z_j\in Z(M),\quad z_j\perp z_k$'+'\n'+r'$\tau_j\text{ faithful normal semifinite on }Mz_j$'+'\n'+r'$\tau(x)=\sum_j\tau_j(z_jx)$',h=.17)
    arrow(ax,.527)
    panel(ax,.313,'Ordered positive cutoffs',r'$0\leq u\leq z,\quad\tau(u)<\infty,\quad u\uparrow z$'+'\n'+r'$y=x^{1/2}ux^{1/2}\leq x,\quad y\uparrow x$'+'\n'+r'$\tau(y)\leq\|x\|\tau(u)<\infty$',h=.17,color=GREEN)
    arrow(ax,.295)
    panel(ax,.073,'A trace in any central gap',r'$d=1-\sum_jz_j\ne0$'+'\nSemifiniteness gives a finite p under d.\nTE-06 gives a nonzero corner trace.\nTE-08–09 yield a new support in d.',h=.18)
    ax.text(.5,.004,'Contradiction to maximality: sum of supports is 1.\nTE-08–11; TE.18–24. Arbitrary families and nets.\nAntecedent: Takesaki I, V.2.10, 2.12, 2.15.',ha='center',va='bottom',fontsize=10,color=INK)
    save(fig,out/'trace-central-gluing-v004.png')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output-directory',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();render(args.output_directory)
    print(json.dumps({'figures':[{ 'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest().upper()} for p in args.output_directory.glob('trace-*-v004.png')]}))
