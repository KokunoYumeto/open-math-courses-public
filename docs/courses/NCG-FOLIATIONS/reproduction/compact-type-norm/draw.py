"""Original CC0 diagram of CTNR.1--9; no external artwork."""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,
                    'svg.hashsalt':'ncg-compact-types-norm-20261011','svg.fonttype':'path'})
BLUE='#245b84'; GREEN='#24755e'; RED='#a43d42'; GRAY='#4c5664'
def box(ax,x,y,w,h,label,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.014',edgecolor=color,facecolor='white',linewidth=1.5))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',color=color,linespacing=1.7)
def arrow(ax,x,y,xx,yy):
    ax.annotate('',xy=(xx,yy),xytext=(x,y),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
def save(fig,out,name):
    fig.savefig(out/(name+'.svg'),metadata={'Date':None,'Creator':'Original CC0 mathematical diagram'})
    p=out/(name+'.svg');p.write_bytes(p.read_bytes().replace(b'\r\n',b'\n'))
    fig.savefig(out/(name+'.png'),dpi=150,metadata={'Software':'Original CC0 mathematical diagram'})
    plt.close(fig)
def draw(out):
    fig,ax=plt.subplots(figsize=(12.8,8.4));fig.patch.set_facecolor('#f5f7fa')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.text(.5,.966,'One actual compact kernel, two different representation norms',ha='center',fontsize=19,color=BLUE)
    box(ax,.035,.69,.43,.19,'Full geometric metric carrier\n'+r'$C=\int_L U_l R_u U_l^*\,dl$'+'\npositive compact average; finite invariant E\nCTNR.1–2 (no physical carrier removed)')
    box(ax,.535,.69,.43,.19,'Full regular carrier\n'+r'$B(\lambda_g\otimes\overline{\sigma}_g)B^*=\lambda_g\otimes1$'+'\nexact finite matrix absorption\nCTNR.4; every actual word retained')
    arrow(ax,.25,.67,.41,.625);arrow(ax,.75,.67,.59,.625)
    box(ax,.075,.31,.85,.29,r'$k_R=\frac{1}{4}\sum_{s=a^{\pm1},b^{\pm1}}\chi_R u_s\otimes\overline{\sigma}_s$'+'\n'+
        'Four actual return bisections; compact range support\n'+r'$\Omega=r^{-1/2}\sum_i e_i\otimes\overline{e}_i,\quad P\Omega=\Omega$'+'\nCTNR.3, CTNR.7–8')
    arrow(ax,.41,.29,.25,.265);arrow(ax,.59,.29,.75,.265)
    box(ax,.035,.08,.43,.16,r'$\|\Pi^{(r)}(k_R)\|>9/10$'+'\ncompact cutoff on the invariant vector\ngeometric representation',RED)
    box(ax,.535,.08,.43,.16,r'$\|k_R\|_r\leq\sqrt{3}/2<9/10$'+'\nabsorption + complete four-tree bound\nreduced regular representation',GREEN)
    ax.text(.5,.025,'CTNR.9 excludes this representation. The actual tree replacement still supplies a reduced graph class.',ha='center',fontsize=11,color=GRAY)
    fig.text(.5,.04,'Exact norm test schematic: original q = 3, metric d = 6 and total n = 9; full inverse lift and final Clifford actions retained.',ha='center',fontsize=11,color=GRAY)
    save(fig,out,'compact-type-receiving-norm')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[2]/'figures')
    args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True);draw(args.output)
