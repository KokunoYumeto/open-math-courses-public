"""Exact weighted-lattice sample and real torus-coset projection. CC0.

GPT-6.1 Sol (OpenAI), Ultra. Matplotlib font glyphs retain their licences.
Mathematical locators: TR-BAKER-10 (10.66), (10.69)-(10.71), Figure10.3.
"""
import argparse
from fractions import Fraction
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

def render(output):
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans'})
    fig,axes=plt.subplots(1,2,figsize=(12.2,6.7),dpi=180)
    fig.subplots_adjust(left=.065,right=.98,bottom=.20,top=.88,wspace=.25)
    ax=axes[0]
    ax.set_title('A sharp weighted relation',fontweight='bold',pad=14)
    ax.add_patch(Polygon([(12,0),(0,12),(-12,0),(0,-12)],closed=True,facecolor='#edf2fa',edgecolor='#295a8d',linewidth=1.6))
    radius=12/np.sqrt(2)
    ax.add_patch(Circle((0,0),radius,facecolor='#d9e6f3',edgecolor='#6689af',linewidth=1.3,linestyle='--'))
    xx=np.linspace(-13,13,401)
    ax.plot(xx,-xx,color='#7c6277',linewidth=1.2)
    for m in (-2,-1,0,1,2):
        ax.scatter(6*m,-6*m,s=24 if abs(m)!=1 else 58,c='#8190a4' if abs(m)!=1 else '#963f58',zorder=5)
    ax.annotate(r'$(6,-6)$',xy=(6,-6),xytext=(7.2,-5.1),fontsize=11,color='#963f58')
    ax.annotate(r'$(-6,6)$',xy=(-6,6),xytext=(-11.8,7.5),fontsize=11,color='#963f58')
    ax.text(0,10.3,r'$|x|+|y|\leq12$',ha='center',fontsize=11)
    ax.text(-7.8,-1.3,r'$x^2+y^2\leq72$',fontsize=10,color='#295a8d')
    ax.axhline(0,color='#b2b8bf',linewidth=.7);ax.axvline(0,color='#b2b8bf',linewidth=.7)
    ax.set(xlim=(-14,14),ylim=(-14,14),xlabel=r'Weighted coordinate $2u_1$',ylabel=r'Weighted coordinate $3u_2$')
    ax.set_aspect('equal')
    ax.set_xticks([-12,-6,0,6,12]);ax.set_yticks([-12,-6,0,6,12])
    ax.grid(alpha=.12)
    ax.text(.5,-.20,r'$u=(3,-2),\quad A=(2,3),\quad B=6$'+'\n'+r'$R=12=K_{2,1}B=2B$',transform=ax.transAxes,ha='center',va='top',fontsize=11)
    ax=axes[1]
    ax.set_title('Three distinct cosets',fontweight='bold',pad=14)
    x=np.linspace(.45,4.65,400)
    colors=['#295a8d','#c47723','#347b61']
    for s,color in enumerate(colors):
        character=Fraction(8,9)**s
        y=np.sqrt(x**3/float(character))
        label=r'$\chi='+('1' if s==0 else (r'\frac{8}{9}' if s==1 else r'\frac{64}{81}'))+'$'
        ax.plot(x,y,color=color,linewidth=1.8,label=label)
        px,py=2**s,3**s
        assert Fraction(px**3,py**2)==character
        ax.scatter([px],[py],s=48,c=color,zorder=5)
        ax.annotate('('+str(px)+','+str(py)+')',xy=(px,py),xytext=(px+.12,py-.52),color=color,fontsize=10)
    ax.annotate('',xy=(2.32,3.72),xytext=(2,3),arrowprops={'arrowstyle':'->','color':'#71395b','lw':2})
    ax.text(2.2,1.5,r'Tangent: $(2Y_1,3Y_2)$',fontsize=10,color='#71395b')
    ax.set(xlim=(.35,4.85),ylim=(0,11.6),xlabel=r'$Y_1>0$',ylabel=r'$Y_2>0$')
    ax.grid(alpha=.16)
    ax.legend(loc='upper left',frameon=True,fontsize=11)
    ax.text(.5,-.20,r'$\chi=Y_1^3/Y_2^2,\quad H_m:\chi=1$'+'\n'+r'$\sigma=0$: derivatives stay in a coset',transform=ax.transAxes,ha='center',va='top',fontsize=11)
    fig.savefig(output,facecolor='white',dpi=180)
    plt.close(fig)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    render(parser.parse_args().output)
