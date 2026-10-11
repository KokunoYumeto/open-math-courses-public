"""Original-coordinate illustration of JC18–JC22; sampled curves, exact witness."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
def cutoff(s):
    z=(1/16-s*s)/(3/64)
    value=np.zeros_like(s); first=np.zeros_like(s); second=np.zeros_like(s)
    value[z>=1]=1
    mid=(z>0)&(z<1); zm=z[mid]
    q=-1/zm+1/(1-zm)
    th=np.empty_like(q);pos=q>=0
    th[pos]=1/(1+np.exp(-q[pos])); eq=np.exp(q[~pos]);th[~pos]=eq/(1+eq)
    qp=1/zm**2+1/(1-zm)**2; qpp=-2/zm**3+2/(1-zm)**3
    thp=th*(1-th)*qp; thpp=th*(1-th)*((1-2*th)*qp**2+qpp)
    zp=-128*s[mid]/3; zpp=-128/3
    value[mid]=th; first[mid]=thp*zp; second[mid]=thpp*zp*zp+thp*zpp
    return value,first,second
radius=np.linspace(1/2000,1,4001);x=radius/np.sqrt(2);y=x.copy()
k,kp,kpp=cutoff(x);ell,ellp,ellpp=cutoff(y)
chi=x*y*k*ell+y**3*kp*ell/3+x*y**3*kpp*ell/6+x*y*y*k*ellp+x*y**3*k*ellpp/6
epsilon=1/1000;H=x*y
raw=epsilon*H;correction=-epsilon*chi;residual=raw+correction
# On this inner region both cutoffs are exactly one, so cancellation is exact.
inner=radius<=np.sqrt(2)/8
residual[inner]=0
weighted=residual/radius**3
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(13.2,5.2),layout='constrained')
ax=axes[0]
ax.plot(radius,raw,label=r'$E(0)=\varepsilon H$',color='#1669a8',lw=2)
ax.plot(radius,correction,label=r"$a'(0)\chi=-\varepsilon\chi$",color='#b4413c',lw=1.8)
ax.plot(radius,residual,label=r'$E_2(0)=\varepsilon(H-\chi)$',color='#147653',lw=2)
ax.axhline(0,color='#768493',lw=.6)
ax.axvspan(0,np.sqrt(2)/8,color='#dcece5',alpha=.6)
ax.set(xlabel=r'Original radius $r$, on $x=y=r/\sqrt{2}$',ylabel='Actual residual value',title='The full correction includes the time derivative')
ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax.legend(loc='upper right',fontsize=9)
ax=axes[1]
ax.plot(radius,weighted,color='#147653',lw=2,label=r'$r^{-3}E_2(0,x,y)$')
ax.axhline(0,color='#b4413c',linestyle='--',lw=1.4,label='Omitted-term bound at time zero')
ax.axvspan(0,np.sqrt(2)/8,color='#dcece5',alpha=.6)
point=(3/4,1/1500)
ax.scatter(*point,color='#14293d',zorder=5)
ax.annotate(r'$r=3/4:\quad 2\varepsilon/3=1/1500>0$',xy=point,xytext=(.39,.0095),arrowprops={'arrowstyle':'->','color':'#14293d'},fontsize=10)
ax.set(xlabel=r'Original radius $r$',ylabel='Actual singularly weighted residual',title='The stated zero bound fails at an exact point')
ax.legend(loc='upper right',fontsize=9)
for ax in axes:
    ax.grid(alpha=.2);ax.set_xlim(0,1)
fig.suptitle(r'Exact correction example: $\varepsilon=1/1000$, $t=0$; proofs JC18–JC22',fontsize=14)
fig.savefig(R/'chen-hou-exact-jet-correction.png',dpi=170)
fig.savefig(R/'chen-hou-exact-jet-correction.svg')
out=dict(epsilon='1/1000',ray='x=y=r/sqrt(2)',time=0,exact_witness={'radius':'3/4','x':'3/(4 sqrt(2))','y':'3/(4 sqrt(2))','weighted_residual':'1/1500','omitted_bound':'0'},
 curve_scope='Floating-point samples of explicit smooth functions; witness value and inequalities are proved exactly in JC18–JC22.',
 support_chi_radius='sqrt(2)/4',inner_cancellation_radius='sqrt(2)/8',
 samples=[dict(r=float(radius[i]),raw=float(raw[i]),correction=float(correction[i]),residual=float(residual[i]),weighted_residual=float(weighted[i])) for i in range(0,len(radius),20)])
(R/'chen-hou-exact-jet-samples.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':str(R/'chen-hou-exact-jet-correction.png'),'sha256':hashlib.sha256((R/'chen-hou-exact-jet-correction.png').read_bytes()).hexdigest(),'weighted_range':[float(weighted.min()),float(weighted.max())]}))
