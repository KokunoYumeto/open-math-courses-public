"""Reproduce the actual Gaussian fields and exact energy derivative in MB14–MB17."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
R=np.array([[3.,-4.],[4.,3.]])/5.
Q=np.diag([1.,2.])
J=np.array([[0.,-1.],[1.,0.]])
Qp=R@Q@R.T
nu=1.
D=480*np.pi**1.5/(241*np.sqrt(1446))
gradnorm=11*np.pi**1.5/2
critical=nu*gradnorm/D
A=np.linspace(0,1.5*critical,301)
rate=-nu*A*A*gradnorm+A*A*A*D
grid=np.linspace(-1.4,1.4,9)
X,Y=np.meshgrid(grid,grid)
points=np.stack([X,Y],axis=-1)
dense=np.linspace(-1.9,1.9,201)
Xd,Yd=np.meshgrid(dense,dense)
p=np.stack([Xd,Yd],axis=-1)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(18,7.2),gridspec_kw={'width_ratios':[1,1,1.2]})
records=[]
for ax,M,title,color in zip(axes[:2],[Q,Qp],
    [r'Original field $u(x_1,x_2,0)$',r'Rotated field $\operatorname{Rot}_R u(x_1,x_2,0)$'],
    ['#174a67','#137f84']):
    gaussian=np.exp(-np.einsum('...i,ij,...j->...',points,M,points))
    vectors=2*np.einsum('ij,...j->...i',J@M,points)*gaussian[...,None]
    background=np.exp(-np.einsum('...i,ij,...j->...',p,M,p))
    contours=ax.contour(Xd,Yd,background,levels=[.2,.4,.6,.8],colors=color,alpha=.5,linewidths=.8)
    ax.clabel(contours,inline=True,fontsize=8)
    ax.quiver(X,Y,vectors[...,0],vectors[...,1],angles='xy',scale_units='xy',scale=1,
              color=color,width=.005)
    ax.set(xlim=(-2,2),ylim=(-2,2),xlabel=r'Original $x_1$',ylabel=r'Original $x_2$',title=title)
    ax.set_aspect('equal')
    ax.grid(alpha=.15)
    records.append({'field':title,'points':points.reshape(-1,2).tolist(),'vectors':vectors.reshape(-1,2).tolist()})
axes[2].plot(A,rate,color='#71419b',linewidth=2.3)
axes[2].axhline(0,color='#555555',linewidth=.8)
axes[2].axvline(critical,color='#bd6811',linestyle='--',label=r'$A_*$')
axes[2].fill_between(A,0,rate,where=A>=critical,color='#71419b',alpha=.12)
axes[2].set(xlabel=r'Actual initial amplitude $A$',ylabel=r'Initial derivative of $\frac{1}{2}\|u_{\rm flow}\|_2^2$',
            title='Actual local evolution from datum Au')
axes[2].grid(alpha=.2)
axes[2].legend()
axes[2].ticklabel_format(axis='y',style='sci',scilimits=(0,0))
fig.suptitle('Admissible averaging can have a nonzero energy defect',fontsize=20,y=.98)
fig.subplots_adjust(left=.05,right=.98,top=.84,bottom=.32,wspace=.32)
fig.text(.5,.20,
    r'$\widetilde B(u,v)=\operatorname{Rot}_{R^{-1}}B(u,v),\quad'
    r'\langle\widetilde B(u,u),u\rangle=\frac{480\pi^{3/2}}{241\sqrt{1446}},\quad'
    r'\|\nabla u\|_2^2=\frac{11}{2}\pi^{3/2}$',ha='center',fontsize=14)
fig.text(.5,.115,
    r'Right: $-\nu A^2(11\pi^{3/2}/2)+A^3(480\pi^{3/2}/(241\sqrt{1446}))$, '
    r'$\nu=1$, $A_*=(11\cdot241\sqrt{1446}/960)\nu$.',ha='center',fontsize=11)
fig.text(.5,.065,'MB14–MB17 prove every field and coefficient. Left panels are exact x3 = 0 sections; arrows show actual vectors.',ha='center',fontsize=10)
fig.text(.5,.023,'Human comparison: Tao, arXiv:1402.0290v3, original definitions at source lines 288–347. This explicit example is a course derivation.',ha='center',fontsize=9)
fig.savefig(out/'original-averaged-energy-defect.png',dpi=160)
fig.savefig(out/'original-averaged-energy-defect.svg')
(out/'original-averaged-energy-defect-data.json').write_text(json.dumps({
    'proof':'ORIGINAL_AVERAGED_OPERATOR_20261010.md MB14–MB17',
    'meaning':'Exact original Gaussian fields sampled at x3=0; analytic initial energy derivative, not a numerically evolved flow.',
    'nu':nu,'rotation':R.tolist(),'original_quadratic_form':Q.tolist(),'rotated_quadratic_form':Qp.tolist(),
    'energy_defect':D,'full_gradient_norm_squared':gradnorm,'critical_amplitude':critical,
    'field_samples':records,'energy_samples':[{'amplitude':float(a),'energy_derivative':float(v)} for a,v in zip(A,rate)]
},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'critical_amplitude':critical,'field_samples':sum(len(r['points']) for r in records),'energy_samples':len(A)}))
