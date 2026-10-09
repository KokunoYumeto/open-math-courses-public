"""Exact coordinate plots for MBE:B3 and MBE:X2. Original work: CC0."""
from pathlib import Path
import hashlib,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'path','svg.hashsalt':'AN04-MBE-20261008',
                    'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
angle=np.linspace(0,2*np.pi,601)
beta=.5;c=1.2
uy=np.sin(angle)/c;ut=np.cos(angle)-beta*uy
a=axes[0]
a.plot(ut,uy,color='#166b82',lw=2.5)
a.axhline(0,color='#aebbc3',lw=.8);a.axvline(0,color='#aebbc3',lw=.8)
a.set(xlabel=r'$u_t$',ylabel=r'$u_y$',title='Positive tangent energy',aspect='equal')
a.text(.03,.96,r'$(u_t+\frac{1}{2}u_y)^2+(\frac{6}{5}u_y)^2=1$',transform=a.transAxes,va='top',
       bbox={'facecolor':'white','edgecolor':'none'})
a.text(.03,.05,r'Real slice: $u=0,\ u_q=0$',transform=a.transAxes,color='#455b68')
a.set_xlim(-1.45,1.45);a.set_ylim(-1.15,1.15)
a=axes[1];q=np.linspace(0,1,201)
a.plot(q,-q,label=r'$\operatorname{Im}v_1=-q$',color='#b54b28',lw=2.5)
a.plot(q,np.ones_like(q),label=r'$v_2=1$',color='#166b82',lw=2.5)
a.set(xlabel=r'normal coordinate $q$',ylabel='component value',
      title='The flux is preserved by the gauge',xlim=(0,1),ylim=(-1.15,1.35))
a.legend(loc='center right',frameon=False)
a.text(.03,.78,r'$D_qv=(-1,0)^T$'+'\n'+r'$Mv=(1,0)^T$'+'\n'+r'$D_qu=0$',
       transform=a.transAxes,va='top',bbox={'facecolor':'white','edgecolor':'none'})
fig.suptitle('Exact derivative-energy slice and boundary-gauge profiles',fontsize=16)
target=ROOT/'figures/matrix-boundary-energy.svg'
fig.savefig(target,metadata={'Date':None});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/matrix-boundary-energy.svg','svg_sha256':sha(target),
        'generator_sha256':sha(Path(__file__)),'proof_locators':['MBE:B3','MBE:X2','MBE:F0'],
        'parameters':{'beta':'1/2','c':'6/5','q_interval':[0,1],'matrix_time':0},
        'meaning':'Exact energy ellipse and exact matrix-gauge profiles; neither panel asserts a PDE solution or ray.',
        'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure':target.name,'bytes':target.stat().st_size}))
