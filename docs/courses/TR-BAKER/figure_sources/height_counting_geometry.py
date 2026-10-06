"""Exact height-counting samples, CC0. Font glyphs retain their licences.

Proof locators: TR-BAKER-10, Lemma10.16 (10.50), Theorem10.18 (10.56).
The left panel is a sample in Q(i); the right is the exact lattice M_Q(4,9).
Neither panel is numerical evidence for a uniform counting theorem.
"""
import argparse
import math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'figures/height-counting-geometry.png')
    output=parser.parse_args().output
    output.parent.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,axes=plt.subplots(1,2,figsize=(12.2,6.7))
    left,right=axes
    left.add_patch(Circle((0,0),1.5,fill=False,color='#334155',linewidth=1.6))
    left.add_patch(Circle((0,0),1,fill=False,color='#94a3b8',linestyle='--',linewidth=1.3))
    for x,y,label in [(0,0,'0'),(1,0,'1'),(-1,0,'−1'),(0,1,'i'),(0,-1,'−i')]:
        left.add_patch(Circle((x,y),.5,facecolor='#dbeafe',edgecolor='#2563eb',alpha=.75,linewidth=1.5))
        left.plot(x,y,'o',color='#153e75',markersize=4)
        left.text(x+.07,y+.07,label,color='#153e75',fontsize=12)
    left.annotate(r'$r=1/2$',xy=(.5,1),xytext=(.7,1.3),arrowprops={'arrowstyle':'->','color':'#2563eb'},color='#2563eb')
    left.annotate(r'$R+r=3/2$',xy=(-1.33,-.69),xytext=(-1.55,-1.4),arrowprops={'arrowstyle':'->','color':'#334155'},color='#334155')
    left.set(xlim=(-1.72,1.72),ylim=(-1.72,1.72),xlabel='Real part',ylabel='Imaginary part',title='One archimedean place\nFive sample centres in the unit disc')
    left.set_aspect('equal')
    left.grid(alpha=.12)
    left.text(.5,-.24,r'$N=2,\ d=f=2,\ X=Y=1$'+'\n'+r'$M\leq ((R+r)/r)^2=9$',transform=left.transAxes,ha='center',va='top',fontsize=11)

    a,b=1/math.log(4),1/math.log(9)
    right.add_patch(Polygon([(a,0),(0,b),(-a,0),(0,-b)],closed=True,facecolor='#d1fae5',edgecolor='#087f5b',linestyle='--',linewidth=2))
    lattice=[(j/2,k/2) for j in range(-2,3) for k in range(-2,3)]
    right.scatter([x for x,y in lattice],[y for x,y in lattice],s=28,color='#94a3b8',zorder=2)
    selected=[(-.5,0,'1/2'),(0,0,'1'),(.5,0,'2')]
    for x,y,label in selected:
        right.scatter([x],[y],s=48,color='#087f5b',zorder=3)
        right.annotate(r'$\beta='+label+'$',xy=(x,y),xytext=(x,-.23),ha='center',fontsize=12,color='#087f5b',arrowprops={'arrowstyle':'-','color':'#087f5b'})
    right.annotate(r'$1/\ln 4$',xy=(a,0),xytext=(.7,.32),ha='center',arrowprops={'arrowstyle':'->','color':'#087f5b'},color='#087f5b')
    right.annotate(r'$1/\ln 9$',xy=(0,b),xytext=(-.5,.72),ha='center',arrowprops={'arrowstyle':'->','color':'#087f5b'},color='#087f5b')
    right.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1),xlabel=r'$x$',ylabel=r'$y$',title='A saturated height diamond\n'+r'$M_{\mathbb{Q}}(4,9)=\frac{1}{2}\mathbb{Z}^2$')
    right.set_aspect('equal')
    right.set_xticks([-.5,0,.5]);right.set_yticks([-.5,0,.5]);right.grid(alpha=.12)
    average=8/(math.log(4)*math.log(9))
    assert 2<average<3
    assert all(math.log(4)*abs(x)+math.log(9)*abs(y)<1 for x,y,_ in selected)
    assert len([p for p in lattice if math.log(4)*abs(p[0])+math.log(9)*abs(p[1])<1])==3
    right.text(.5,-.24,r'$(\ln4)|x|+(\ln9)|y|<1$'+'\n'+r'$J\,\mathrm{vol}(S)=8/(\ln4\ln9)\approx '+f'{average:.4f}'+r'$',transform=right.transAxes,ha='center',va='top',fontsize=11)
    fig.subplots_adjust(left=.07,right=.98,top=.88,bottom=.28,wspace=.33)
    fig.savefig(output,dpi=180,facecolor='white')
    plt.close(fig)
    print(output)


if __name__=='__main__':
    main()
