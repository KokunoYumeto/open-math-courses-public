"""Original sinh coordinates, derivative factors and exact integration measures."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':11})
fig=plt.figure(figsize=(15,8.5),layout='constrained');g=fig.add_gridspec(2,3,height_ratios=[1,0.32])
az=fig.add_subplot(g[0,0]);ay=fig.add_subplot(g[0,1]);aw=fig.add_subplot(g[0,2]);cap=fig.add_subplot(g[1,:])
for a in range(-3,4):
    az.plot([a,a],[0,3],color='#628ca7',lw=1)
    ay.plot([np.sinh(a)]*2,[0,np.sinh(3)],color='#628ca7',lw=1)
for b in range(4):
    az.plot([-3,3],[b,b],color='#628ca7',lw=1)
    ay.plot([-np.sinh(3),np.sinh(3)],[np.sinh(b)]*2,color='#628ca7',lw=1)
zz=np.array([(a,b) for a in range(-3,4) for b in range(4)])
az.scatter(zz[:,0],zz[:,1],s=15,color='#263e51');ay.scatter(np.sinh(zz[:,0]),np.sinh(zz[:,1]),s=15,color='#263e51')
az.set(xlim=(-3.4,3.4),ylim=(-0.25,3.5),xlabel=r'$z_1$',ylabel=r'$z_2$',title='Uniform coordinate grid')
ay.set(xlim=(-11.3,11.3),ylim=(-0.8,11.7),xlabel=r'$y_1=\sinh z_1$',ylabel=r'$y_2=\sinh z_2$',title='The same points in original coordinates')
for a in [az,ay]:a.spines[['top','right']].set_visible(False);a.set_aspect('equal',adjustable='box')
az.text(-3.2,3.25,r'$L_1=L_2=3$',fontsize=12)
ay.text(-10.8,10.8,r'$J=\cosh z_1\cosh z_2$',fontsize=12)
xs=np.linspace(-3,3,601);ys=1/np.cosh(xs)**2
aw.axvspan(-1,1,color='#dfedda',label=r'near origin: $|z_i|\leq1$')
aw.plot(xs,ys,color='#ac4c2c',lw=2.3,label=r'$\operatorname{sech}^2 z_i$')
aw.axhline(1/np.cosh(1)**2,color='#437541',ls='--',lw=1.5,label=r'$\operatorname{sech}^2(1)$')
aw.set(xlim=(-3,3),ylim=(0,1.08),xlabel=r'$z_i$',ylabel='original gradient-square factor',title='The full derivative weight')
aw.legend(loc='upper left',bbox_to_anchor=(0,-0.18),fontsize=10,frameon=False)
aw.spines[['top','right']].set_visible(False)
cap.axis('off')
lines=[
 r'$|\nabla_y f|^2\circ S=\sum_i\operatorname{sech}^2z_i\,|\partial_{z_i}(f\circ S)|^2,\qquad dy_1dy_2=\cosh z_1\cosh z_2\,dz_1dz_2.$',
 'The pictured upper-domain rectangle uses L₁=L₂=3 for legibility. The original source computational size is not replaced by this illustration.',
 'The grid and curve are direct evaluations of the exact map and coefficient; they contain no trained profile or fitted data.',
 'Proof: SG1–SG5, SG19–SG23. Source: Wang, Lai, Gómez-Serrano and Buckmaster, arXiv:2201.06780v3, main190–203; supplement194–248.'
]
for yy,txt in zip([0.97,0.65,0.38,0.12],lines):cap.text(0,yy,txt,va='top',fontsize=12 if yy>0.8 else 11)
for ext in ['png','svg']:fig.savefig(R/f'sinh-profile-metric.{ext}',dpi=180,facecolor='white')
print(str(R/'sinh-profile-metric.png'))
