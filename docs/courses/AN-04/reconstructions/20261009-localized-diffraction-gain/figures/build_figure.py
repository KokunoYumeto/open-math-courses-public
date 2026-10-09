"""CC0-1.0. Exact norm bounds and boundary trace scaling in LG28–LG29."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-localized-source-trace','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(12,5.2));fig.subplots_adjust(left=.075,right=.975,bottom=.2,top=.78,wspace=.33)
fig.suptitle('Localized source pairings and the actual weak normal trace',fontsize=15,fontweight='bold',y=.96)
epsilon=np.geomspace(.01,1,2000)
axes[0].plot(epsilon,.5*np.sqrt(np.floor(1/epsilon)),color='#155f86',label='L2 norm: proved lower bound')
axes[0].axhline(np.sqrt(2),color='#b44c1c',label='H−1 norm: proved upper bound')
axes[0].set(xscale='log',xlabel='Regularizer parameter ε',ylabel='Norm bound',title='A global L2 bound need not be uniform')
axes[0].legend(loc='upper right',fontsize=9);axes[0].grid(alpha=.18)
lam=np.linspace(1,64,600)
axes[1].plot(lam,np.ones_like(lam),color='#155f86',label='Boundary H−3/2 norm = 1')
axes[1].plot(lam,lam**.25,color='#b44c1c',label='Boundary H−5/4 norm = λ¹/⁴')
axes[1].set(xlabel='Tangential frequency weight λ',ylabel='Exact boundary norm',title='The lower trace exponent is sharp')
axes[1].legend(loc='upper left',fontsize=9);axes[1].grid(alpha=.18)
fig.text(.525,.06,'Both input norms in the right panel equal 1/√2.',ha='center',fontsize=11)
svg=ROOT/'figures/localized-source-and-trace.svg';fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['LG28','LG29','F0'],
 'left_domain':[.01,1],'left_formulae':['sqrt(floor(1/epsilon))/2','sqrt(2)'],
 'right_domain':[1,64],'right_formulae':['1','lambda**(1/4)'],
 'meaning':'Analytic bounds and exact norm scaling for the solved sequences; no numerical PDE or propagation claim.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps(record))
