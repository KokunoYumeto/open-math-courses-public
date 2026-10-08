"""Reproducible exact scientific plots; four-real-dimensional geometry is labeled."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
 'axes.titlesize':13,'svg.hashsalt':'AN02-surface-169','savefig.facecolor':'white'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',metadata={'Date':None})
 plt.close(fig)

x=np.geomspace(.22,12,500)
plane=1+np.maximum(1-x**-2,0)
mass=2+3*np.maximum(1-x**-2,0)
fig,ax=plt.subplots(1,2,figsize=(13.2,5.6),layout='constrained')
ax[0].semilogx(x,plane,lw=2.4,color='#176b91',label=r'Area of $t(t-h)=0$: $S/(\pi r^2)$')
ax[0].semilogx(x,mass,lw=2.4,color='#ad542c',label=r'Mass of $\log|t^2(t-h)^3|$: $\mu/(2\pi^2r^2)$')
ax[0].axhline(2,color='#176b91',ls=':',label='Geometric degree bound: 2')
ax[0].axhline(5,color='#ad542c',ls=':',label='Multiplicity degree bound: 5')
ax[0].axvline(1,color='.6',lw=1)
ax[0].set(xlabel=r'Euclidean ball radius $r/h$',ylabel='Normalized area or mass (legend)',
 title='Two parallel complex planes in four real dimensions',ylim=(.65,5.35))
ax[0].legend(loc='center right',fontsize=8.8)
z=np.geomspace(.08,40,500)
ax[1].semilogx(z,1-np.log1p(z*z)/(z*z),lw=2.4,color='#534594')
ax[1].axhline(1,color='.4',ls=':',label=r'Limit: area $\pi r^2$ times $2\pi$')
ax[1].set(xlabel=r'$r/\delta$',ylabel=r'$\mu_\delta(B_r)/(2\pi^2r^2)$',
 title='Exact smooth normal mass for the plane $t=0$',ylim=(0,1.08))
ax[1].text(.04,.82,r'$1-\log(1+(r/\delta)^2)/(r/\delta)^2$',
 transform=ax[1].transAxes,fontsize=11)
ax[1].legend(loc='lower right',fontsize=9)
for a in ax:a.grid(alpha=.2)
save(fig,'algebraic-area-and-normal-mass')

r=np.geomspace(.035,12,500)
b=2*r*r/(np.sqrt(1+4*r*r)+1)
total=2-1/(1+b);projection=1/(1+b)
fig,ax=plt.subplots(1,2,figsize=(13.2,5.6),layout='constrained')
ax[0].semilogx(r,total,lw=2.4,color='#176b91',label=r'Full graph area $S_N/(\pi r^2)$')
ax[0].semilogx(r,projection,lw=2.2,ls='--',color='#ad542c',label=r'Parameter projection: $b(r)/r^2$')
ax[0].axhline(2,color='.4',ls=':',label='Degree-two upper bound')
ax[0].set(xlabel='Euclidean ball radius r',ylabel='Area divided by '+r'$\pi r^2$',
 title=r'Exact area of $N=\{(y,y^2)\}\subset\mathbb{C}^2$',ylim=(0,2.18))
ax[0].legend(loc='upper left',fontsize=9)
angles=np.linspace(0,2*np.pi,600);ellipsoid_radius=.6
centers=[0,2,5];colors=['#176b91','#ad542c','#534594']
for center,color in zip(centers,colors):
 sigma=1/(1+center)
 ax[1].plot(center+ellipsoid_radius*np.cos(angles),
    ellipsoid_radius*sigma*np.sin(angles),color=color,lw=2.3)
 ax[1].plot(center,0,'o',color=color,ms=4)
 ax[1].text(center,.76,'a='+str(center)+'\n'+r'$\sigma=$'+('1' if center==0 else '1/'+str(1+center)),
    ha='center',va='top',color=color,fontsize=10)
ax[1].set(xlim=(-.9,5.9),ylim=(-.85,.92),xlabel=r'Real section coordinate $t$',
 ylabel=r'Real section coordinate $y$',
 title='Exact anisotropic sections: m=2, radius r=0.6')
ax[1].set_aspect('equal',adjustable='box')
ax[1].text(.5,.03,'Real sections of complex ellipsoids; not a full-space cover',
 transform=ax[1].transAxes,ha='center',fontsize=9)
for a in ax:a.grid(alpha=.2)
save(fig,'curved-area-and-anisotropic-cover')

geometry=dict(ambient_real_dimension=4,surface_real_dimension=2,
 sphere_volume_coefficient='b_2=pi',surface_graph='Gamma(y)=(y,y^2)',
 graph_area_density='1+4|y|^2',euclidean_ball_cutoff='|y|^2=b(r)=(sqrt(1+4r^2)-1)/2',
 area='pi*(b+2*b^2)=pi*(2*r^2-b)',projection_area='pi*b',
 parallel_planes=dict(polynomial='t(t-h)',surface_area='pi*r^2+pi*(r^2-h^2)_+',
  repeated_polynomial='t^2(t-h)^3',log_laplacian_mass='2*pi^2*(2*r^2+3*(r^2-h^2)_+)'),
 normal_regularization=dict(logarithm='0.5*log(|t|^2+delta^2)',
  laplacian='2*delta^2/(|t|^2+delta^2)^2',
  ball_mass='2*pi^2*(r^2-delta^2*log(1+r^2/delta^2))'),
 ellipsoid_sections=dict(m=2,radius=ellipsoid_radius,
  centers=[dict(a=c,b=0,sigma_exact='1/'+str(1+c)) for c in centers],
  equation='|t-a|^2+(1+|theta|)^2*|y-b|^2<r^2',
  real_section_only=True,three_drawn_sections_do_not_claim_a_cover=True),
 exact_proof_locators=['SR7-SR13','SR16-SR23','L152.1-L152.6','L152.10-L152.14'],
 human_source='Lars Hormander, Analysis of Linear PDE I, Theorem4.1.12; II, Theorem15.3.3',
 original_plot_sources=True,blender_useful=False,
 blender_reason='Exact scalar plots and labeled real sections preserve the actual four-dimensional metric; a three-dimensional embedding would not.')
(OUT/'geometry.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_pairs':2,'geometry':str(OUT/'geometry.json')}))
