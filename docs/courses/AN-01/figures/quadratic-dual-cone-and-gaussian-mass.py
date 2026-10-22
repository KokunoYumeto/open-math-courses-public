"""The dual quadratic cone and its Gaussian mass; Theorem15, Exercise17. CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':11,'svg.hashsalt':'quadratic-dual-cone-and-gaussian-mass'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(12,5.4),layout='constrained')
ax=fig.add_subplot(121,projection='3d')
r=np.linspace(0,2,36);theta=np.linspace(0,2*np.pi,101)
rr,tt=np.meshgrid(r,theta)
xx=rr*np.cos(tt);yy=rr*np.sin(tt)
for sign,color in [(1,'#237eb6'),(-1,'#da7833')]:
 ax.plot_surface(xx,yy,sign*rr,color=color,alpha=.55,linewidth=0,shade=True)
 ax.plot(2*np.cos(theta),2*np.sin(theta),np.full_like(theta,sign*2),color=color)
ax.set(xlabel=r'$\xi$',ylabel=r'$\eta$',zlabel=r'$\tau$',title=r'Both sheets: $\tau=\pm\sqrt{\xi^2+\eta^2}$')
ax.set_box_aspect((1,1,1));ax.view_init(22,-55)
ax.text2D(.03,.91,r'Surface shown only for $0\leq r\leq2$',transform=ax.transAxes)
ax2=fig.add_subplot(122)
r=np.linspace(0,3,500)
for b,col in [(.5,'#237eb6'),(1,'#da7833'),(2,'#36916e')]:
 ax2.plot(r,2*np.pi*np.exp(-2*b*r*r),label=fr'$b={b:g}$',color=col,lw=2)
ax2.set(xlabel=r'Spatial radius $r=\sqrt{\xi^2+\eta^2}$',ylabel='Gaussian-weighted radial density',
        title=r'Cone mass: $2\pi e^{-2br^2}\,dr$',xlim=(0,3),ylim=(0,6.8))
ax2.grid(alpha=.2);ax2.legend()
ax2.text(.98,.55,r'$\int_0^\infty 2\pi e^{-2br^2}\,dr$'+'\n'+r'$=\pi^{3/2}/\sqrt{2b}$',
 transform=ax2.transAxes,ha='right',fontsize=14)
fig.savefig(out/'quadratic-dual-cone-and-gaussian-mass.png',dpi=160)
fig.savefig(out/'quadratic-dual-cone-and-gaussian-mass.svg',metadata={'Date':None})
p=out/'quadratic-dual-cone-and-gaussian-mass.svg'
p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
plt.close(fig)
