"""Exact boundary pairings and complex lower-form balance, WQ33/WQ37."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,axes=plt.subplots(1,2,figsize=(12.6,4.7),layout='constrained')
ax=axes[0]
values=[-.5,1,.5]
bars=ax.bar([0,1,2],values,color=['#a94d24','#18818b','#3a586d'],width=.58)
ax.axhline(0,color='#243746',lw=.8)
ax.set_xticks([0,1,2],['Interior\npairing','Boundary\nterm','Weak\nform'])
for bar,value,label in zip(bars,values,['−1/2','+1','+1/2']):
 ax.text(bar.get_x()+bar.get_width()/2,value+(.05 if value>0 else -.07),label,
         ha='center',va='bottom' if value>0 else 'top',fontweight='bold')
ax.set(title='The retained boundary contribution (WQ33)',ylabel='exact real pairing',ylim=(-.8,1.3))
ax.text(.5,1.19,'−1/2 + 1 = 1/2',ha='center')
ax=axes[1]
gamma=np.linspace(0,1,501)
exact=np.sqrt(5)*gamma/2
upper=np.sqrt(5)*(1+gamma*gamma)/4
ax.plot(gamma,exact,color='#146575',lw=2.5,label='Exact magnitude: √5 γ / 2')
ax.plot(gamma,upper,color='#a94d24',lw=2,label='Upper bound: √5 (1 + γ²) / 4')
ax.fill_between(gamma,exact,upper,color='#d8e8e6',label='Gap: √5 (γ − 1)² / 4')
ax.scatter([1],[np.sqrt(5)/2],color='#146575',zorder=5)
ax.set(title='Both complex lower terms retained (WQ37)',xlabel='inverse tangential weight γ',
       ylabel='magnitude / bound',xlim=(0,1),ylim=(0,1.25))
ax.legend(loc='lower right',fontsize=9)
for ax in axes:ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
fig.suptitle('Weak-form quantities and exact norm balance — no ray or solution-amplitude interpretation',fontsize=12)
out=HERE/'weak-quadratic-boundary-balance.svg'
fig.savefig(out,metadata={'Date':None});plt.close(fig)
result={'svg':out.relative_to(HERE.parent).as_posix(),
 'svg_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'proof_locators':['WQ33','WQ37'],'exact_boundary_values':['-1/2','1','1/2'],
 'lower_term_magnitude':'sqrt(5)*gamma/2','upper_bound':'sqrt(5)*(1+gamma**2)/4',
 'gap':'sqrt(5)*(gamma-1)**2/4','gamma_range':[0,1],
 'actually_inspected':False,'depicts_PDE_solution':False}
(HERE.parent/'figure-check.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'svg_bytes':out.stat().st_size,'proof_locators':result['proof_locators']}))
