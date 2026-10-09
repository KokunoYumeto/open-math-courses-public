"""Exact real sections of PB.1-PB.3. Original reproducible CC0 drawing."""
from pathlib import Path
from fractions import Fraction as F
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

R=F(1);rz=F(32);kappa=F(4)/rz;C=F(2);L=F(1,2048)
a0=F(1,128);a=-a0;t=-a0/8;x=F(1,20);b=R/16
alpha=L/4
g=lambda r:2*alpha*r*r
mu=-t-g(x)
delta=min(b/2,mu/(4*L))
assert delta==F(1,32)
assert kappa*F(5,4)*a0<b/2
assert C*F(5,4)*a0<F(1,2)
assert a0<R/16 and L<=F(1,8) and L*kappa<=F(1,8) and L*R<a0/8
for theta in [F(j,256) for j in range(257)]:
    s=a+theta*(t-a);length=t-s;radius=delta+kappa*length
    # In d=1 the maximum |y| in the entire complex disc is |x|+radius.
    actual_margin=-s-g(x+radius)
    proved_margin=F(3,4)*mu+F(1,4)*length
    assert actual_margin>=proved_margin>0
data={name:str(value) for name,value in [('R',R),('r_z',rz),('kappa',kappa),('C',C),('L',L),('a_0',a0),('a',a),('t',t),('x',x),('b',b),('alpha',alpha),('mu',mu),('delta_t',delta)]}
data.update({'dimension':1,'section':'Im s=Im x=0; real sections of complex spatial discs','left_vertical_rescaling':1000000,'right_vertical_rescaling':1000,'proof_locators':'PB.1-PB.3; PB.2-PB.9','exact_inequalities_checked':True,'complex_disc_radial_margin_checked_samples':257,'all_sample_checks_use_exact_rational_arithmetic':True})

ink='#183d46';orange='#ab592e';green='#467d69';blue='#466da2'
fig,axs=plt.subplots(1,2,figsize=(13.5,5.8),constrained_layout=True)
y=np.linspace(-.1,.1,801)
old=-float(alpha)*y*y
majorant=-2*float(alpha)*y*y
ax=axs[0]
ax.set_facecolor('#fafbf9')
ax.fill_between(y,majorant*1e6,1.5,color=green,alpha=.12)
ax.fill_between(y,old*1e6,1.5,color=orange,alpha=.16)
ax.plot(y,old*1e6,color=orange,lw=2,label=r'Original $Z$: $T\geq-\alpha |v|^2$')
ax.plot(y,majorant*1e6,color=green,lw=2.5,label=r'Majorant $Z_g$: $T\geq-2\alpha |v|^2$')
ax.scatter([0],[0],color=ink,s=35,zorder=5)
ax.text(-.082,-3.9,r'Convex complement $\Omega_g$',color=green,fontsize=12)
ax.text(-.082,-4.5,r'$g(r)=\int_0^{2r}\alpha s\,ds=2\alpha r^2$',fontsize=11,color=ink)
ax.set(xlim=(-.1,.1),ylim=(-5.25,1.25),xlabel=r'Real spatial section $x$',ylabel=r'$10^6 T$',title='Exact cofinal majorant in a real section')
ax.legend(loc='upper center',fontsize=10)
ax.grid(alpha=.16)

ax=axs[1];ax.set_facecolor('#fafbf9')
time=np.linspace(float(a),float(t),401)
radius=float(delta)+float(kappa)*(float(t)-time)
ax.fill_betweenx(1000*time,float(x)-radius,float(x)+radius,color=blue,alpha=.2)
ax.plot(np.full_like(time,float(x)),1000*time,color=ink,lw=2)
ax.plot(float(x)-radius,1000*time,color=blue,lw=1.5)
ax.plot(float(x)+radius,1000*time,color=blue,lw=1.5)
spatial=np.linspace(0,.1,401)
ax.plot(spatial,-2*float(alpha)*spatial**2*1000,color=green,lw=2)
for st,color,label in [(a,orange,r'Anchor $a=-1/128$'),(t,blue,r'Target $t=-1/1024$')]:
    rad=float(delta+kappa*(t-st))
    ax.plot([float(x)-rad,float(x)+rad],[float(st)*1000]*2,color=color,lw=2)
    ax.scatter([float(x)],[float(st)*1000],color=color,s=48,zorder=5)
    ax.text(.003,float(st)*1000-.34,label,color=color,fontsize=10)
label_box={'facecolor':'#fafbf9','edgecolor':'none','alpha':.95,'pad':3}
ax.text(.038,-4.0,r'$\delta_s=\frac{1}{32}+\frac{1}{8}|t-s|$',fontsize=11,color=blue,bbox=label_box,zorder=6)
ax.text(.038,-4.7,r'$x=\frac{1}{20}$',fontsize=12,color=ink,bbox=label_box,zorder=6)
ax.text(.003,.27,r'$T=-g(|x|)$',color=green,fontsize=10)
ax.set(xlim=(0,.1),ylim=(-8.7,.75),xlabel=r'Real spatial section $y$',ylabel=r'$10^3\,\operatorname{Re}s$',title='One fixed segment and its Cauchy discs')
ax.grid(alpha=.16)
fig.suptitle('Cofinal support and the common domain for every spatial Taylor term',fontsize=15,color=ink)
fig.savefig(Path(__file__).with_name('ordinary-action-prerequisites.png'),dpi=190)
fig.savefig(Path(__file__).with_name('ordinary-action-prerequisites.svg'))
Path(__file__).with_name('ordinary-action-prerequisites-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
