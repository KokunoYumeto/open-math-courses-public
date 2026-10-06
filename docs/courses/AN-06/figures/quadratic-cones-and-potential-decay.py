"""Original CC0 figure for a dual quadratic cone and its permitted potential.

Run with Python, NumPy and Matplotlib; outputs are beside this source.
All curves use the explicit formulas in the accompanying lesson.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'svg.hashsalt':'quadratic-cones-decay-v1'})
out=Path(__file__).resolve().parent
fig,(ax,bx)=plt.subplots(2,1,figsize=(8.4,8.8))
fig.subplots_adjust(left=.13,right=.95,bottom=.095,top=.88,hspace=.48)
blue='#246ca2';orange='#bd5a24'
grid=np.linspace(-3.5,3.5,400)
x,y=np.meshgrid(grid,grid)
a=x*x-y*y
ax.contourf(x,y,a,levels=[0,100],colors=['#e4eff7'],alpha=1)
for level,color in [(1,blue),(4,'#477e48')]:
    yy=np.linspace(-3.5,3.5,500)
    xx=np.sqrt(yy*yy+level)
    for sign in [1,-1]:
        ax.plot(sign*xx,yy,color=color,lw=1.7)
ax.plot(grid,grid,ls='--',color=orange,lw=1.5)
ax.plot(grid,-grid,ls='--',color=orange,lw=1.5)
ax.text(2.5,0,r'$A>0$',ha='center',color=blue,fontsize=13)
ax.text(-2.5,0,r'$A>0$',ha='center',color=blue,fontsize=13)
ax.text(0,1.85,r'$A<0$',ha='center',color='#576573')
ax.annotate(r'$A=1,\ r=1$',xy=(np.sqrt(1+.7**2),.7),xytext=(0,2.9),
            ha='center',color=blue,arrowprops={'arrowstyle':'->','color':blue})
ax.annotate(r'$A=4,\ r=2$',xy=(2,0),xytext=(0,-2.9),
            ha='center',color='#477e48',arrowprops={'arrowstyle':'->','color':'#477e48'})
ax.text(-.13,.86,'Dashed:\n'+r'$A=0$',transform=ax.transAxes,ha='right',color=orange)
ax.set_xlim(-3.5,3.5);ax.set_ylim(-3.5,3.5);ax.set_aspect('equal')
ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$')
ax.set_title(r'Dual form $A(x)=x_1^2-x_2^2$ and cone radius $r=\sqrt{A}$',fontsize=12,pad=12)
ax.grid(alpha=.12)

radius=np.geomspace(1,1e4,500)
off=(radius*radius+1+radius)**-.5
null=(1+radius)**-.5
assert np.all(null>off) and np.all(off>0)
bx.loglog(radius,null,color=orange,lw=2.2,label=r'Null ray: $x=\rho(1,1)/\sqrt{2}$')
bx.loglog(radius,off,color=blue,lw=2.2,label=r'Off-cone ray: $x=(\rho,0)$')
bx.loglog(radius[160:],radius[160:]**-.5,color=orange,ls=':',lw=1.5)
bx.loglog(radius[160:],radius[160:]**-1,color=blue,ls=':',lw=1.5)
bx.text(2200,.027,r'$\rho^{-1/2}$',color=orange)
bx.text(2200,.0008,r'$\rho^{-1}$',color=blue)
bx.set_xlim(1,1e4);bx.set_ylim(7e-5,1)
bx.set_xlabel(r'Euclidean distance $\rho=|x|$');bx.set_ylabel(r'Potential $V(x)$')
bx.set_title(r'Exact potential $V=(|A|+1+|x|)^{-1/2}$ on two rays',fontsize=12,pad=12)
bx.grid(which='both',alpha=.15);bx.legend(loc='lower left',fontsize=10)
fig.suptitle('The cone boundary permits a slower decay rate',fontsize=15,y=.965)
fig.text(.5,.025,'Lemma 1.1, Example 1.2 and Example 5.2. Solid curves are exact; dotted lines show asymptotic powers.',
         ha='center',fontsize=9.1,color='#4b5965')
fig.savefig(out/'quadratic-cones-and-potential-decay.png',dpi=160,
            metadata={'Software':'Original CC0 mathematical plot'})
fig.savefig(out/'quadratic-cones-and-potential-decay.svg',
            metadata={'Date':None,'Creator':'Original CC0 mathematical plot'})
plt.close(fig)
print('Original cone geometry and exact potential curves generated.')
