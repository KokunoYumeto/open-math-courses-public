"""CC0-1.0. Exact lower bounds EC27 and EC28, with their stated domains."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-normal-ratio-bounds','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(12,5.2))
fig.subplots_adjust(left=.075,right=.975,bottom=.2,top=.77,wspace=.33)
fig.suptitle('Two mechanisms control the interior normal kernel',fontsize=15,fontweight='bold',y=.96)
q=np.linspace(0,128,400)
axes[0].plot(q,1/16-q/8192,color='#155f86',label='1/16 − q/8192')
axes[0].axhline(1/32,color='#ad4a24',ls='--',label='Retained bound 1/32')
axes[0].scatter([128],[3/64],color='#155f86',zorder=4)
axes[0].annotate('3/64',(128,3/64),xytext=(-38,12),textcoords='offset points')
axes[0].set(xlabel='Normal input/output ratio q = y/x',ylabel='Lower bound for |g|/|σ|',title='Cancel the rapid normal phase',xlim=(0,132),ylim=(.025,.073))
q=np.linspace(16,160,500)
axes[1].plot(q,.25-4/q,color='#155f86',label='1/4 − 4/q')
axes[1].axhline(3/16,color='#ad4a24',ls='--',label='Used bound 3/16 for q ≥ 64')
axes[1].scatter([64],[3/16],color='#155f86',zorder=4)
axes[1].set(xlabel='Normal input/output ratio q = y/x',ylabel='Lower bound for (yr − xt)/y',title='Use separation from the kernel diagonal',xlim=(16,160),ylim=(-.015,.275))
for ax in axes:
    ax.axvspan(64,128,color='#97c8bc',alpha=.22,zorder=0)
    ax.grid(alpha=.18)
    ax.legend(loc='upper center',fontsize=9)
fig.text(.5,.07,'Shading: the smooth-partition overlap 64 ≤ y/x ≤ 128.  Proof: M3–M4 and Exercise 2.',ha='center',fontsize=10)
svg=ROOT/'figures/normal-ratio-bounds.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'})
plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['EC14','EC17','EC27','EC28','F0'],
 'left_domain':[0,128],'left_formulae':['1/16-q/8192','1/32'],
 'right_domain':[16,160],'right_formulae':['1/4-4/q','3/16'],
 'overlap':[64,128],'meaning':'Proved phase and profile-separation lower bounds under the exact symbol-support conditions; no PDE simulation.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps(record))
