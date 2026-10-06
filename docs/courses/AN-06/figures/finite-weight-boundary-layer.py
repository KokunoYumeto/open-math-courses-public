"""CC0 exact cone layer and proof diagram for U020 Lemma 4.1.

No solution or error magnitude is sampled. Curves are A=x1^2-x2^2
at epsilon=1/4; the diagram states the proved inequalities in the lesson.
Run with Python, NumPy and Matplotlib. Outputs remain beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,
                     'svg.hashsalt':'finite-weight-boundary-layer-v1'})
out=Path(__file__).resolve().parent
eps=1/4
fig,(ax,bx)=plt.subplots(2,1,figsize=(6.4,10.8),gridspec_kw={'height_ratios':[1,1.18]})
fig.subplots_adjust(left=.14,right=.95,bottom=.07,top=.84,hspace=.42)
blue='#246ca2';orange='#bd5a24';ink='#253b49'
grid=np.linspace(-3,3,601);x,y=np.meshgrid(grid,grid);a=x*x-y*y
ax.contourf(x,y,a,levels=[0,20],colors=['#e4eff7'])
ax.contourf(x,y,a,levels=[eps,2*eps],colors=['#efbf88'])
yy=np.linspace(-3,3,601)
for level,style in [(eps,'-'),(2*eps,':')]:
 xx=np.sqrt(yy*yy+level)
 assert np.max(np.abs(xx*xx-yy*yy-level))<1e-12
 for sign in [-1,1]:ax.plot(sign*xx,yy,color=orange,lw=2,ls=style)
ax.plot(grid,grid,'--',color=ink,lw=1.2);ax.plot(grid,-grid,'--',color=ink,lw=1.2)
ax.text(2.1,0,r'$O:\ A>0$',color=blue,ha='center',fontsize=16)
ax.text(-2.1,0,r'$O:\ A>0$',color=blue,ha='center',fontsize=16)
ax.annotate(r'$A=\varepsilon$',xy=(np.sqrt(.8**2+eps),.8),xytext=(1.6,2.5),
            color=orange,fontsize=15,arrowprops={'arrowstyle':'->','color':orange})
ax.annotate(r'$A=2\varepsilon$',xy=(-np.sqrt(1.3**2+2*eps),-1.3),xytext=(-2.6,-2.5),
            color=orange,fontsize=15,arrowprops={'arrowstyle':'->','color':orange})
ax.set_xlim(-3,3);ax.set_ylim(-3,3);ax.set_aspect('equal')
ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$');ax.grid(alpha=.1)
ax.set_title(r'$A=x_1^2-x_2^2,\quad\varepsilon=1/4$',fontsize=17,pad=13)
ax.text(.5,-.24,'Orange: '+r'$\varepsilon<A<2\varepsilon$'+' (continues beyond window)',
        transform=ax.transAxes,ha='center',fontsize=13,color=orange)
bx.set_xlim(0,1);bx.set_ylim(0,1);bx.axis('off')
def box(y,h,lines,color):
 bx.add_patch(FancyBboxPatch((.02,y),.96,h,boxstyle='round,pad=.018',
                            facecolor=color,edgecolor='#a6b8c4'))
 for off,label in lines:bx.text(.5,y+off,label,ha='center',va='center',color=ink,fontsize=15)
box(.77,.18,[(.125,r'$s\geq1,\quad K\leq4\lambda s$'),
              (.055,'One weighted '+r'$H^1$'+' exponent')],'#edf4f8')
box(.49,.20,[(.145,r'$(E_\varepsilon^{\rm err})^2\leq4C^2(2\varepsilon)^{s-1}I_\varepsilon$'),
              (.073,r'$I_\varepsilon\longrightarrow0$'+' by dominated convergence'),
              (.018,r'$s=1$'+' included')],'#fff1e0')
box(.23,.18,[(.125,r'$\|\partial_t v_\varepsilon\|\longrightarrow0$'),
              (.055,r'$K=4\lambda s$'+' included')],'#edf4f8')
box(.015,.13,[(.085,r'$v\in L^2(dt\,d\mu),\quad\partial_t v=0$'),
               (.033,r'$v=0\quad\Longrightarrow\quad u=0\ \mathrm{on}\ O$')],'#edf4f8')
for upper,lower in [(.77,.69),(.49,.41),(.23,.145)]:
 bx.annotate('',xy=(.5,lower+.005),xytext=(.5,upper-.008),
             arrowprops={'arrowstyle':'->','color':ink,'lw':1.5})
fig.suptitle('One finite weight suffices\nin a fixed quadratic cone',fontsize=20,y=.972)
fig.text(.5,.023,'U020 Lemma 4.1: boundary error and equality at the threshold.\n'
         'Exact geometry and proved bounds; no numerical solution sample.',ha='center',fontsize=12,color=ink)
fig.savefig(out/'finite-weight-boundary-layer.png',dpi=180,metadata={'Software':'Original CC0 mathematical plot'})
fig.savefig(out/'finite-weight-boundary-layer.svg',metadata={'Date':None,'Creator':'Original CC0 mathematical plot'})
plt.close(fig)
print('Generated exact finite-weight boundary layer and endpoint proof diagram.')
