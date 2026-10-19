"""Reproduce the exact kernel-coordinate relation from rational geometry data."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'AN02-L206-kernel-relation','font.family':'DejaVu Sans'})

def main():
    geometry=json.loads((HERE/'kernel-relation-geometry.json').read_text(encoding='utf-8'))
    pts=[[float(Fraction(x)) for x in pair] for pair in geometry['basis_coefficients']]
    fig,ax=plt.subplots(figsize=(8,6.9),dpi=170)
    fig.patch.set_facecolor('white')
    colors=['#1167a5','#28814b','#8d3e9f']
    for (u,v),color in zip(pts,colors):
        ax.annotate('',xy=(u,v),xytext=(0,0),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':color,'mutation_scale':20})
    ax.annotate('',xy=pts[2],xytext=pts[0],arrowprops={'arrowstyle':'->','ls':'--','lw':1.8,'color':colors[1],'mutation_scale':18})
    ax.text(1.035,.235,r'$g_2/2$',color=colors[1],fontsize=16,va='center')
    ax.text(.78,-.105,r'$g_1=(1,0)$',color=colors[0],fontsize=16)
    ax.text(.035,1.055,r'$g_2=(0,1)$',color=colors[1],fontsize=16)
    ax.text(1.04,.54,r'$g_3=(1,\frac{1}{2})$',color=colors[2],fontsize=16)
    ax.scatter([0],[0],color='#263341',s=20,zorder=4)
    ax.set_xlim(-.18,1.48);ax.set_ylim(-.18,1.3);ax.set_aspect('equal')
    ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
    ax.set_xticklabels(['0','1/2','1']);ax.set_yticklabels(['0','1/2','1'])
    ax.grid(alpha=.22);ax.tick_params(labelsize=12)
    ax.set_xlabel(r'coefficient of $g_1$',fontsize=14,labelpad=10)
    ax.set_ylabel(r'coefficient of $g_2$',fontsize=14,labelpad=10)
    ax.set_title('A generator and its relation',fontsize=20,pad=16)
    fig.text(.5,.085,r'$g_3=g_1+\frac{1}{2}g_2 \qquad C_1(1)=(-1,-\frac{1}{2},1)$',ha='center',fontsize=18)
    fig.text(.5,.035,r'$z_1=1,\ z_2=\frac{1}{2}:\quad x_0+x_1+\frac{1}{2}x_2=0$',ha='center',fontsize=15,color='#374151')
    fig.subplots_adjust(left=.12,right=.98,bottom=.22,top=.9)
    out=HERE/'figures';out.mkdir(exist_ok=True)
    fig.savefig(out/'a-generator-and-its-relation.png',metadata={'Software':'Matplotlib; GPT-6.1 Sol (OpenAI)'})
    svg=out/'a-generator-and-its-relation.svg';fig.savefig(svg,metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI); Matplotlib'})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

if __name__=='__main__':main()
