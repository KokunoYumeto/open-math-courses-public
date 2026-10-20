"""Exact cusp projections and a fixed-domain Volterra memory contour."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fractions import Fraction as Q
r=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,
                     'svg.hashsalt':'linear-fibration-continuation-v1'})
fig,axes=plt.subplots(2,1,figsize=(8,12.5),layout='constrained')
ax=axes[0]
x=np.linspace(0,.85,601);t=x**1.5
ax.plot(x,t,color='#176b87',lw=2.5,label=r'$S:t^2=x^3$ (real section)')
ax.plot(x,-t,color='#176b87',lw=2.5)
ax.axvline(0,color='#a7335c',lw=2,label=r'$D_0:x=0$')
xx=np.linspace(-.45,.45,401)
ax.plot(xx,-2*xx,color='#bf7a17',lw=2,label=r'$D_1:x+t/2=0$')
ax.scatter([0],[0],color='black',s=28,zorder=5)
ax.annotate(r'$D_0\cap D_1=\{0\}\subset S$',(0,0),xytext=(.15,-.32),
            arrowprops={'arrowstyle':'->','color':'#333333'},fontsize=14)
for base,delta,col,label in [((-.28,.2),(0,.35),'#a7335c',r'$v_0=(1,0)$'),
                             ((.45,.2),(-.175,.35),'#bf7a17',r'$v_1=(1,-1/2)$')]:
 ax.annotate('',(base[0]+delta[0],base[1]+delta[1]),base,
             arrowprops={'arrowstyle':'-|>','lw':2,'color':col})
 ax.text(base[0]-.08,base[1]-.11,label,color=col,fontsize=14)
ax.set(xlim=(-.5,.95),ylim=(-.95,.95),xlabel=r'$x$ (real section)',ylabel=r'$t$ (real section)',
       title='Spanning linear fibre directions')
ax.text(.02,.015,'Vector coordinates are ordered (t,x).\nThe plotted axes are ordered (x,t).',
        transform=ax.transAxes,fontsize=14,ha='left',va='bottom')
ax.legend(loc='upper right',fontsize=14)
ax.grid(alpha=.15)
ax=axes[1]
alpha=Q(1,8);rho=Q(1,16);A=Q(-1,2);end=Q(1,2)
path=[]
stops=[float(A),float(-alpha-rho),float(-alpha+rho),float(alpha-rho),float(alpha+rho),float(end)]
for l,u in [(stops[0],stops[1]),(stops[2],stops[3]),(stops[4],stops[5])]:
 path.append(np.linspace(l,u,101).astype(complex))
for centre in [-float(alpha),float(alpha)]:
 theta=np.linspace(np.pi,0,161)
 path.append(centre+float(rho)*np.exp(1j*theta))
for piece in path:ax.plot(piece.real,piece.imag,color='#176b87',lw=2.5)
ax.scatter([float(A),float(end)],[0,0],s=35,color='#176b87',zorder=5)
ax.scatter([-float(alpha),float(alpha)],[0,0],marker='x',s=65,color='#a7335c',zorder=6)
for xx,label,dy in [(float(A),r'$A=-1/2$',-.025),(float(end),r'$t=1/2$',-.025),
                    (-float(alpha),r'$-1/8$',-.025),(float(alpha),r'$1/8$',-.025)]:
 ax.text(xx,dy,label,ha='center',va='top',fontsize=14)
ax.annotate('fixed memory contour',xy=(-.12,.063),xytext=(-.27,.16),
            arrowprops={'arrowstyle':'->','color':'#333333'})
ax.text(.02,.96,r'$(t^2-1/64)f(t)-\int_A^t f(s)\,ds=1$'+'\n'+
        r'$f(t)=\frac{81}{625}\frac{(t-1/8)^3}{(t+1/8)^5}$',
        transform=ax.transAxes,va='top',fontsize=14)
ax.text(.02,.04,'One scalar Volterra calibration.\nIt is not a classification of the full module.',
        transform=ax.transAxes,fontsize=14)
ax.set(xlim=(-.6,.6),ylim=(-.13,.35),xlabel=r'$\operatorname{Re}s$',ylabel=r'$\operatorname{Im}s$',
       title='A kernel domain containing the entire contour')
ax.grid(alpha=.15)
fig.suptitle('Linear fibrations and actual holomorphic continuation',fontsize=19)
fig.savefig(r/'linear-fibration-continuation.png',dpi=180,metadata={'Software':'Open mathematics course figures'})
fig.savefig(r/'linear-fibration-continuation.svg',metadata={'Date':None,'Creator':'Open mathematics course figures'})
plt.close(fig)
data={'cusp':'t^2=x^3','lambda':'1/2','fibrations':['F0=x','F1=x+t/2'],
 'fibre_vectors_t_x':[['1','0'],['1','-1/2']],'determinant':'-1/2',
 'bad_cylinder_intersection':'{t=x=0}; in this example it lies in S',
 'volterra':{'A':'-1/2','end':'1/2','alpha':'1/8','detour_radius':'1/16',
 'kernel':'-1','principal':'t^2-1/64',
 'solution':'(81/625)*(t-1/8)^3/(t+1/8)^5',
 'identity':'d[(t^2-1/64)*f]/dt=f; (A^2-1/64)*f(A)=1'},
 'scope':'Exact geometric section and scalar calibration only; the candidate proof treats all complex directions, rectangular matrices and singular strata.'}
(r/'linear-fibration-continuation-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
checks=0
def f(t):return Q(81,625)*(t-alpha)**3/(t+alpha)**5
def df(t):return Q(81,625)*(3*(t-alpha)**2/(t+alpha)**5-5*(t-alpha)**3/(t+alpha)**6)
assert (A*A-alpha*alpha)*f(A)==1
checks+=1
for i in range(-200,201):
 t=Q(i,400)
 if t==-alpha:continue
 assert 2*t*f(t)+(t*t-alpha*alpha)*df(t)==f(t)
 checks+=1
assert Q(-1,2)!=0
checks+=1
print(json.dumps({'exact_rational_checks':checks,'all_passed':True,'scope':'finite diagnostic identities only'}))
