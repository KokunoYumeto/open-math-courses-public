"""Exact CV6 example, CC0; deterministic wide and stacked renderings."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'SH02-CV6-20261009','font.family':'DejaVu Sans','axes.spines.top':False,'axes.spines.right':False})
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path(__file__).parent/'figures');a=ap.parse_args();a.output.mkdir(parents=True,exist_ok=True)
blue='#2866A4';red='#BF4C45';green='#167D5E'
def panel(ax,target=False):
    ax.set_xlim(-1.25,1.25);ax.set_ylim(-1.3,1.6)
    ax.axhline(0,color='#C6CBD0',lw=.8);ax.axvline(0,color='#C6CBD0',lw=.8)
    if not target:
        ax.plot([-1.25,1.25],[0,0],color=blue,lw=3,label=r'$\Lambda$: zero section and origin fibre')
        ax.plot([0,0],[-1.3,1.6],color=blue,lw=3)
        xx=np.linspace(-.65,.8,160);ax.plot(xx,2*xx,color=red,lw=2.4,label=r'graph $d\varphi$: $\xi=2x$')
        ax.scatter([0],[0],s=85,c=green,zorder=5)
        ax.annotate(r'$E=\{0\}$',xy=(0,0),xytext=(.25,-.5),arrowprops={'arrowstyle':'->','color':green},color=green)
        ax.set_xlabel(r'base $x$');ax.set_ylabel(r'covector $\xi$')
        ax.set_title('Source: actual characteristic incidence\n'+r'$\varphi(x)=x^2$',pad=15)
    else:
        ax.plot([0,1.25],[0,0],color=blue,lw=3,label=r'$\Gamma$: positive zero ray and origin fibre')
        ax.plot([0,0],[-1.3,1.6],color=blue,lw=3)
        ax.plot([-1.25,1.25],[1,1],color=red,lw=2.4,label=r'fixed section $a=1$')
        ax.scatter([0],[1],s=85,c=green,zorder=5)
        ax.annotate(r'$(0,1)$',xy=(0,1),xytext=(.35,1.28),arrowprops={'arrowstyle':'->','color':green},color=green)
        ax.text(.35,-.42,r'$S_\varphi=\{0\}$',color=green)
        ax.set_xlabel(r'value $t=x^2$');ax.set_ylabel(r'covector $a$')
        ax.set_title('Target: selected values\n'+r'$\Gamma=\{(t,0):t\geq0\}\cup\{(0,a)\}$',pad=15)
    ax.legend(loc='lower center',bbox_to_anchor=(.5,-.37),frameon=False,fontsize=10)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.grid(alpha=.16)
for mode in ['wide','stacked']:
    fig,axs=plt.subplots(1,2,figsize=(12,6)) if mode=='wide' else plt.subplots(2,1,figsize=(6.4,12.8))
    panel(axs[0]);panel(axs[1],True)
    fig.suptitle('Closed conic isotropic sets: the exact quadratic example',fontsize=14,y=.985)
    if mode=='wide':fig.subplots_adjust(left=.07,right=.97,bottom=.27,top=.79,wspace=.28)
    else:fig.subplots_adjust(left=.15,right=.95,bottom=.12,top=.87,hspace=.75)
    name='characteristic-values-'+mode
    fig.savefig(a.output/(name+'.svg'),metadata={'Date':None,'Creator':'SH02 exact CV6 figure'})
    fig.savefig(a.output/(name+'.png'),dpi=180,metadata={'Software':'SH02 exact CV6 figure'})
    fig.savefig(a.output/(name+'.pdf'),metadata={'CreationDate':None,'ModDate':None,'Creator':'SH02 exact CV6 figure'})
    plt.close(fig)
math={'proof_locator':'CV6; equations CV6a, CV0b','example_only':True,'source_manifold':'R','function':'phi(x)=x^2','source_cotangent_set':'{(x,0):x in R} union {(0,xi):xi in R}','actual_graph':'G(x)=(x,2x)','actual_incidence':'{0}','correspondence_maps':{'phi_d':'(x,a)->(x,2ax)','phi_pi':'(x,a)->(x^2,a)'},'target_cotangent_set':'{(t,0):t>=0} union {(0,a):a in R}','selected_section':'a=1','selected_value_set':'{0}','display_limits':{'horizontal':[-1.25,1.25],'vertical':[-1.3,1.6]},'cutoffs_are_display_windows':True,'source':'independent CC0 scientific plotting source; all equations retained','license':'CC0-1.0'}
(a.output/'FIGURE_MATH.json').write_text(json.dumps(math,indent=2)+'\n',encoding='utf-8')
