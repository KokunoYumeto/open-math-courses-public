"""Exact finite-matrix illustration of NC/CR/MC; no sampled theorem claim."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':14,'svg.hashsalt':'oa-flow-natural-cone-20261004'})
fig=plt.figure(figsize=(16,12),facecolor='#f6f8fb')
gs=fig.add_gridspec(2,2,left=.06,right=.96,bottom=.15,top=.86,hspace=.42,wspace=.22)
ax=fig.add_subplot(gs[0,0],projection='3d')
t=np.linspace(0,2*np.pi,100); h=np.linspace(0,1.1,35)
T,H=np.meshgrid(t,h)
ax.plot_surface(H*np.cos(T),H*np.sin(T),H,color='#65b6ce',alpha=.16,linewidth=0,shade=False)
r=1/np.sqrt(2)
v0=np.array([r,0,r]); v1=np.array([0,r,r]); q=np.array([r/2,0,r/2])
for v,c,l in [(v0,'#147b9c',r'$p_0$'),(v1,'#bb5365',r'$p_{\pi/4}$'),(q,'#263a64',r'$q_{p_0}(p_{\pi/4})=\frac{1}{2}p_0$')]:
 ax.plot([0,v[0]],[0,v[1]],[0,v[2]],color=c,lw=2.8)
 ax.scatter(*v,color=c,s=40,depthshade=False)
 ax.text(*(v+np.array([.03,.03,.035])),l,color=c,fontsize=11)
ax.plot([v1[0],q[0]],[v1[1],q[1]],[v1[2],q[2]],'--',color='#777f8e',lw=1.7)
ax.set(xlabel=r'$y=(a-c)/\sqrt{2}$',ylabel=r'$z=\sqrt{2}b$',zlabel=r'$x=(a+c)/\sqrt{2}$')
ax.set_title('A. A real symmetric section of the natural cone',pad=12,loc='left')
ax.set_xlim(-1.1,1.1);ax.set_ylim(-1.1,1.1);ax.set_zlim(0,1.2)
ax.view_init(elev=21,azim=-64)
ax.set_box_aspect((1,1,1))
ax.text2D(.00,.97,r'$x\geq\sqrt{y^2+z^2}$;  $q_p(X)=pXp$',transform=ax.transAxes)

ax=fig.add_subplot(gs[0,1]);theta=np.linspace(0,np.pi/2,301)
a=2*np.sin(theta)**2;b=2*np.sin(theta);c=2*np.sin(theta)*np.sqrt(1+np.cos(theta)**2)
ax.fill_between(theta,a,b,color='#65b6ce',alpha=.16)
ax.plot(theta,a,color='#147b9c',lw=2.5,label=r'$\|p_\theta-p_0\|_{HS}^2=2\sin^2\theta$')
ax.plot(theta,b,color='#bb5365',lw=2.5,label=r'$\|f_\theta-f_0\|=2\sin\theta$')
ax.plot(theta,c,color='#5e6682',lw=1.8,ls='--',label=r'$\|p_\theta-p_0\|_{HS}\|p_\theta+p_0\|_{HS}$')
ax.scatter([np.pi/4,np.pi/4],[1,np.sqrt(2)],c=['#147b9c','#bb5365'],zorder=4)
ax.set(ylim=(0,2.15),xlim=(0,np.pi/2),xlabel=r'$\theta$',ylabel='Exact norm values')
ax.set_xticks([0,np.pi/4,np.pi/2],['0',r'$\pi/4$',r'$\pi/2$'])
ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=10,framealpha=.9)
ax.set_title('B. The cone-vector estimate includes singular supports',loc='left',pad=14)

p0=np.array([[1.,0],[0,0]]);p1=np.ones((2,2))/2
P=np.block([[p0,np.zeros((2,2))],[np.zeros((2,2)),p1]])
I=np.eye(2);U=np.block([[I,I],[-I,I]])/np.sqrt(2);R=U@P@U.T
for index,data,title in [(0,P,r'C. Nonfaithful diagonal vector $\Omega=P=\mathrm{diag}(p_0,p_{\pi/4})$'),(1,R,r'D. Canonical unitary transport $U\Omega U^*$')]:
 ax=fig.add_subplot(gs[1,index]);im=ax.imshow(data,cmap='RdBu_r',norm=TwoSlopeNorm(vmin=-1,vcenter=0,vmax=1))
 ax.set_title(title,loc='left',pad=14,fontsize=12)
 for i in range(4):
  for j in range(4):
   val=data[i,j]; label='0' if abs(val)<1e-12 else {1.:'1',.5:'1/2',.75:'3/4',.25:'1/4',-.25:'−1/4'}.get(round(float(val),8),f'{val:.2g}')
   ax.text(j,i,label,ha='center',va='center',fontsize=14,color='white' if abs(val)>.6 else '#142b43')
 ax.axhline(1.5,color='#263a64',lw=2.5);ax.axvline(1.5,color='#263a64',lw=2.5)
 ax.set_xticks(range(4),['1','2','3','4']);ax.set_yticks(range(4),['1','2','3','4'])
 ax.set_xlabel('Hilbert–Schmidt coordinates in $M_4$')
 if index==1:
  ax.text(.5,-.19,r'Whole matrix: eigenvalues $1,1,0,0$.'+'\n'+r'Off-diagonal block: eigenvalues $\pm1/(2\sqrt{2})$.',ha='center',va='top',transform=ax.transAxes,fontsize=11)
 else:
  ax.text(.5,-.19,r'$\dim_{\mathbb{C}} H=16$,  $\dim_{\mathbb{C}} HP=8$,  $\dim_{\mathbb{C}} PHP=4$.'+'\n'+'Full functional GNS: $HP$.  Faithful support corner: $PHP$.',ha='center',va='top',transform=ax.transAxes,fontsize=11)
fig.suptitle('Natural cones, exact supports and matrix transport',fontsize=22,color='#1f3455',y=.972)
fig.text(.06,.929,'Finite matrix examples of NC-3/5, CR-3/6/8 and MC-3/4; the proofs apply to arbitrary von Neumann algebras.',fontsize=12,color='#4a586e')
fig.savefig(HERE/'assets/natural-cone.png',dpi=160,facecolor=fig.get_facecolor())
fig.savefig(HERE/'assets/natural-cone.svg',facecolor=fig.get_facecolor(),metadata={'Date':None})
svg=HERE/'assets/natural-cone.svg'
svg.write_text(svg.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
checks={'p0_projection':bool(np.allclose(p0@p0,p0)),'p1_projection':bool(np.allclose(p1@p1,p1)),'q_formula':bool(np.allclose(p0@p1@p0,p0/2)),'U_unitary':bool(np.allclose(U@U.T,np.eye(4))),'P_projection':bool(np.allclose(P@P,P)),'transport_projection':bool(np.allclose(R@R,R)),'transport_spectrum':np.linalg.eigvalsh(R).tolist(),'off_diagonal_spectrum':np.linalg.eigvalsh(R[:2,2:]).tolist(),'ranks':{'P':int(np.linalg.matrix_rank(P)),'ambient_complex_dimension':16,'cyclic_complex_dimension':8,'support_corner_complex_dimension':4},'sample_norm_estimate':bool(np.all(a<=b+1e-12) and np.all(b<=c+1e-12)),'scope':'Numerical checks of the exact caption formulas, not proofs of the general theorems'}
(HERE/'FIGURE_NUMERICAL_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(checks,indent=2))
