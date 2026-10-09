"""Exact nonisolated z^2 example for GS/IV/HC; CC0, reproducible matplotlib."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'svg.hashsalt':'SH02-FH14-visible-morse-20261009'})
a=1/8; radius=1/2; eps=1/64; eta=1/16
blue='#2363aa';green='#087d64';red='#b62538';grey='#52606c'

def first(ax):
    xx=np.linspace(-.22,.22,450)
    ax.axhline(0,color=green,lw=3,label=r'$\Sigma_{K_N[1]}:\ \xi=0$')
    ax.plot(xx,2*xx,color=blue,lw=2.3,label=r'$dg:\ \xi=2x$')
    ax.plot(xx,2*xx+a,color=red,lw=2.3,label=r'$d(g+az):\ \xi=2x+1/8$')
    ax.plot(0,0,'o',color=blue,ms=8)
    ax.plot(-a/2,0,'o',color=red,ms=8)
    ax.annotate(r'$q=(0,0)$',(0,0),xytext=(.045,-.16),color=blue,
                arrowprops={'arrowstyle':'->','color':blue})
    ax.annotate(r'$q_a=(-1/16,0)$',(-a/2,0),xytext=(-.20,.33),color=red,
                arrowprops={'arrowstyle':'->','color':red})
    ax.set_xlim(-.22,.22);ax.set_ylim(-.48,.61)
    ax.set_xlabel(r'$x=\operatorname{Re}z$');ax.set_ylabel(r'$\operatorname{Re}\xi$')
    ax.set_title('One visible normal intersection',fontweight='bold',pad=14)
    ax.grid(alpha=.18);ax.legend(loc='lower right',fontsize=9,framealpha=.95)
    ax.text(.5,-.24,'Real section: Im z = Im ξ = 0.\nThe complex graph intersection is one point.',
            transform=ax.transAxes,ha='center',va='top',fontsize=10,color=grey)

def second(ax):
    xx=np.linspace(-radius,radius,801)
    tt=np.linspace(-radius,radius,801)
    x,t=np.meshgrid(xx,tt)
    u=x*x-t*t+a*x;v=2*x*t
    valid=(x*x+t*t<=radius*radius)&(abs(v)<=eta)
    um=np.ma.array(u,mask=~valid)
    layer=np.ma.array(np.ones_like(u),mask=~(valid&(abs(u)<=eps)))
    ax.contourf(x,t,layer,levels=[.5,1.5],colors=['#e4edf7'])
    ax.contour(x,t,um,levels=[-eps],colors=[green],linestyles='solid',linewidths=2)
    ax.contour(x,t,um,levels=[eps],colors=[blue],linestyles='solid',linewidths=2)
    vm=np.ma.array(v,mask=x*x+t*t>radius*radius)
    ax.contour(x,t,vm,levels=[-eta,eta],colors=[grey],linestyles='--',linewidths=1)
    ax.add_patch(Circle((0,0),radius,fill=False,color=grey,lw=1.3))
    ax.plot(-a/2,0,'o',color=red,ms=8)
    for end in [(-a/2,.15),(-a/2,-.15)]:
        ax.annotate('',xy=end,xytext=(-a/2,0),arrowprops={'arrowstyle':'->','color':red,'lw':1.8})
    ax.annotate('one negative\nreal direction',(-a/2,.13),xytext=(.16,.27),
                color=red,fontsize=10,arrowprops={'arrowstyle':'->','color':red})
    ax.set_xlim(-.53,.53);ax.set_ylim(-.53,.53);ax.set_aspect('equal')
    ax.set_xlabel(r'$x=\operatorname{Re}z$');ax.set_ylabel(r'$t=\operatorname{Im}z$')
    ax.set_title('The actual real band has one Morse jump',fontweight='bold',pad=14)
    ax.plot([],[],color=green,lw=2,label=r'lower: $u_a=-1/64$')
    ax.plot([],[],color=blue,lw=2,label=r'upper: $u_a=+1/64$')
    ax.plot([],[],color=grey,ls='--',label=r'fixed sides: $|2xt|=1/16$')
    ax.legend(loc='lower right',fontsize=8,framealpha=.96)
    ax.text(.5,-.24,r'$u_a=(x+1/16)^2-t^2-1/256$'+'\n'+
            r'$M_{z^2}(K_N[1])=K$ in degree zero; integer count = 1.',
            transform=ax.transAxes,ha='center',va='top',fontsize=10,color=grey)

def make(mobile):
    if mobile:
        fig,axes=plt.subplots(2,1,figsize=(7.2,13.6))
        fig.subplots_adjust(left=.14,right=.95,top=.80,bottom=.15,hspace=.72)
    else:
        fig,axes=plt.subplots(1,2,figsize=(14.6,7.4))
        fig.subplots_adjust(left=.065,right=.98,top=.76,bottom=.30,wspace=.29)
    first(axes[0]);second(axes[1])
    title=(r'$h(z,y)=z^2$ on $\mathbf{C}^2$'+'\nA whole critical line, one transverse jump') if mobile else r'$h(z,y)=z^2$ on $\mathbf{C}^2$: a whole critical line, one transverse jump'
    fig.suptitle(title,fontsize=14 if mobile else 16,fontweight='bold',y=.975)
    fig.text(.5,.905 if mobile else .86,
        'Y = {z = 0},  π(z,y) = y,  N = {y = 0},  r = dimℂ Y = 1.\n'
        'P = K on ℂ² shifted by [2];  P|N[−1] = K on ℂ shifted by [1].',
        ha='center',va='top',fontsize=10 if mobile else 11,color=grey)
    footer=('Exact choices: a = 1/8, radius = 1/2, ε = 1/64, η = 1/16.\n'
        'Contours sample the displayed exact equations. K may be any field.\n'
        'Proof: GS2–GS4, IV1–IV5 and HC2.\nThe transverse slice is only at the zero stratum.') if mobile else (
        'Exact choices: a = 1/8, radius = 1/2, ε = 1/64, η = 1/16. Contours are numerical samples of the displayed exact equations.\n'
        'Proof: GS2–GS4, IV1–IV5 and HC2. A constant coefficient K may be any field. The transverse slice is only at the zero stratum.')
    fig.text(.5,.018 if mobile else .06,footer,
        ha='center',va='bottom',fontsize=9,color=grey)
    stem=OUT/('visible-morse-mobile' if mobile else 'visible-morse-wide')
    fig.savefig(stem.with_suffix('.svg'),metadata={'Date':None,'Creator':'Independent CC0 mathematical diagram'})
    fig.savefig(stem.with_suffix('.png'),dpi=180,metadata={'Software':'Independent CC0 mathematical diagram'})
    fig.savefig(stem.with_suffix('.pdf'),metadata={'CreationDate':None,'ModDate':None,'Creator':'Independent CC0 mathematical diagram'})
    plt.close(fig)

make(False);make(True)
(OUT/'visible-morse-math.md').write_text('''# Exact figure mathematics

Independent CC0 diagram. Example only; the general proof retains arbitrary h and singular/nonisolated loci.

h(z,y)=z² on C²; Y={z=0}; π=y; N={y=0}; dim_C Y=1. For the perverse P=K_{C²}[2], the correctly normalized restriction is P|N[-1]=K_N[1]. In T*_{C}N, its microsupport is the zero section ξ=0. The original graph ξ=2z meets it at (0,0); the perturbation z²+(1/8)z meets it at z=-1/16. Panel one is precisely the real section Im z=Im ξ=0, not the whole complex cotangent surface.

On N write z=x+it. The perturbed real height is u_a=x²-t²+x/8=(x+1/16)²-t²-1/256. Its unique critical point has one negative direction t and one positive direction x. Choose |z|<=1/2, ε=1/64, η=1/16, with fixed sides |Im(z²)|=|2xt|<=η. The displayed blue/green contours are sampled exact levels u_a=+ε and u_a=-ε in that fixed cap; grey shading is the intervening band. The critical value -1/256 lies strictly inside it. At a radial-face point in this band, |Re(z²)|<=ε+a/2=5/64 and |Im(z²)|<=1/16, so |z²|<=sqrt(41)/64<1/4; that contradicts |z|=1/2. Thus this example has no radial-face point in the band, and introduces no hidden boundary jump.

The actual finite jump of K_N[1] is its point-normal object in ordinary degree zero: M_{z²}(K_N[1])=K. The dimension is the integer 1 over every field. Unshifted Φ_{z²}K_N[1]=K[1]. Ambient unshifted Φ_h P=K_Y[2], so the transverse normalization is essential. The ambient critical locus is the entire complex line Y, not an isolated point.

Proof locators: [visible normal slicing](../general-critical-support.html#GS2), [the finite visible Morse filtration](../general-critical-support.html#IV1), and [the critical-support argument](../general-critical-support.html#HC2). The complete lesson links its scholarly prerequisites.
''',encoding='utf-8')
print('Rendered wide/mobile SVG, PNG and PDF plus exact mathematical caption.')
