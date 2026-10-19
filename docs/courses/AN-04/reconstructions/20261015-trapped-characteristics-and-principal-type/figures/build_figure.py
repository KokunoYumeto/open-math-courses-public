"""Plot exact phase data and a numerical sample of the proved integral turn."""
from pathlib import Path
import math,hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'AN04-TCP-band'})
E=lambda x:math.exp(-1/x) if x>0 else 0.
phi=lambda u:math.pi*E(u)/(E(u)+E(1-u))
S0,Serr=quad(lambda u:math.sin(phi(u)),0,1,epsabs=1e-12,epsrel=1e-12)
epsilon=.12;s0=.22;lam=epsilon/S0
us=np.linspace(0,1,401);turn=[];errs=[Serr]
for u in us:
 c,ce=quad(lambda v:math.cos(phi(v)),0,float(u),epsabs=1e-12,epsrel=1e-12)
 sn,se=quad(lambda v:math.sin(phi(v)),0,float(u),epsabs=1e-12,epsrel=1e-12)
 turn.append((s0-lam*c,lam*sn));errs.extend([ce,se])
turn[0]=(s0,0.);turn[-1]=(s0,epsilon)
fig,axes=plt.subplots(2,1,figsize=(11,7.7),gridspec_kw={'height_ratios':[1,1.25]})
ax=axes[0];ts=np.linspace(-math.pi,3*math.pi,601)
ax.plot(ts,np.cos(ts),color='#17697b',label='Re coefficient: cos(t)')
ax.plot(ts,np.sin(ts),color='#bc6b24',label='Im coefficient: sin(t)')
ax.plot(ts,np.ones_like(ts),color='#586c36',linestyle='--',label='squared norm: cos²(t) + sin²(t) = 1')
ax.axhline(0,color='#7f8e99',lw=.7)
ax.set(xlim=(-math.pi,3*math.pi),ylim=(-1.22,1.2),ylabel='coefficient',title='The explicit multiplier exp(-it) stays smooth when either real component vanishes')
ax.set_xticks([-math.pi,0,math.pi,2*math.pi,3*math.pi],labels=['-π','0','π','2π','3π'])
ax.legend(loc='lower left',fontsize=9);ax.grid(alpha=.12)
ax=axes[1]
ax.axvspan(-.02,.32,color='#67824b',alpha=.16)
ax.axvspan(.9,1.08,color='#17697b',alpha=.12)
ax.plot([1,s0],[0,0],color='#17697b',lw=2)
ax.plot([s0,1],[epsilon,epsilon],color='#17697b',lw=2)
ax.plot([q[0] for q in turn],[q[1] for q in turn],color='#17697b',lw=2)
ax.annotate('',xy=(.5,0),xytext=(.79,0),arrowprops={'arrowstyle':'->','color':'#17697b'})
ax.annotate('',xy=(.79,epsilon),xytext=(.5,epsilon),arrowprops={'arrowstyle':'->','color':'#17697b'})
ax.plot([1,1],[0,epsilon],'o',color='#283a4c')
ax.plot([.62],[0],'D',color='#a84634')
ax.annotate('marked point retained',xy=(.62,0),xytext=(.45,-.073),arrowprops={'arrowstyle':'->','color':'#a84634'},fontsize=10)
ax.text(.14,.225,'rank-two\nturn collar',ha='center',va='center',fontsize=10)
ax.text(.61,.225,'parallel admissible\nreal-flow passages',ha='center',va='center',fontsize=10)
ax.text(.99,.225,'rank two\noutside K',ha='center',va='center',fontsize=10)
ax.set(xlim=(-.02,1.08),ylim=(-.105,.28),xlabel='flow-band coordinate s',ylabel='transverse coordinate r',
 title='A turn in the starting collar joins two sides with far endpoints in the same outside target')
ax.set_xticks([0,s0,.62,1],labels=['0','s₀','marked s','1'])
ax.set_yticks([0,epsilon],labels=['0','ε'])
ax.grid(alpha=.12)
fig.tight_layout(pad=1.5)
out=root/'trapped-limit-and-admissible-band.svg'
fig.savefig(out,metadata={'Date':None,'Title':'Explicit phase and admissible band','Creator':'Independent CC0 programme figure'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(root.parent/'figure-check.json').write_text(json.dumps({
 'svg':'figures/trapped-limit-and-admissible-band.svg','svg_sha256':sha(out),
 'generator_sha256':sha(Path(__file__)),                           
 'phase_formulas':['cos(t)','sin(t)','cos(t)^2+sin(t)^2=1'],
 'band_parameters':{'epsilon':'0.12','s0':'0.22','marked_s':'0.62','target_s':'1'},
 'turn_formula':'TC16; numerical quadrature samples only; endpoints fixed by the exact reflection proof',
 'largest_quadrature_error_estimate':max(errs),'S0_sample':S0,
 'scope':'Exact phase coefficients and proved endpoint data; numerical samples of the exact turn in flow-band coordinates, with no assertion about original Euclidean geometry.',
 'independent_expression_licence':'CC0-1.0'},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure_written':True,'largest_quadrature_error_estimate':max(errs)}))
