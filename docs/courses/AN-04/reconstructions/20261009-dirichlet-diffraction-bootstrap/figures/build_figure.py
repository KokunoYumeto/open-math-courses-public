"""CC0-1.0. Exact normalized Hamilton projection and broken cap displacement."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-dirichlet-region','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(12,5.6))
fig.subplots_adjust(left=.08,right=.975,bottom=.2,top=.78,wspace=.32)
fig.suptitle('Turning, tangency and reflection share one continuous cap map',fontsize=14,fontweight='bold',y=.96)
h=1/16;ax=axes[0]
for mu,color,label in [(-.01,'#b4542a','μ = −1/100: reflection'),(0,'#1d6484','μ = 0: tangency'),(.01,'#855290','μ = 1/100: interior turn')]:
 a=np.sqrt(h-mu);b=np.sqrt(max(-mu,0))
 pieces=[np.linspace(-a,-b,170),np.linspace(b,a,170)] if mu<0 else [np.linspace(-a,a,300)]
 for k,r in enumerate(pieces):
  ax.plot(r,mu+r*r,color=color,label=label if k==0 else None)
  j=len(r)//3
  ax.annotate('',xy=(r[j+15],mu+r[j+15]**2),xytext=(r[j],mu+r[j]**2),arrowprops={'arrowstyle':'->','color':color})
 if mu<0:
  ax.plot([-b,b],[0,0],ls=':',lw=2,color=color)
  ax.annotate('',xy=(.055,0),xytext=(-.055,0),arrowprops={'arrowstyle':'->','color':color})
 else:ax.scatter([0],[mu],s=22,color=color,zorder=4)
ax.axhline(h,color='#71808b',ls='--',lw=.8)
ax.set(xlabel='Normal covector ρ',ylabel='Normal position x',xlim=(-.3,.3),ylim=(-.003,.077),title='Characteristic section: ζ = 1, τ = √(1 − μ)')
ax.set_yticks([0,1/32,1/16],['0','1/32','1/16'])
ax.legend(loc='upper center',fontsize=8);ax.grid(alpha=.15)
ax=axes[1]
mu=np.r_[np.linspace(-1/64,0,500,endpoint=False),np.linspace(0,1/64,500)]
dt=-4*np.sqrt(1-mu)*(np.sqrt(h-mu)-np.sqrt(np.maximum(-mu,0)))
ax.plot(mu,dt,color='#1d6484')
ax.scatter([0],[-1],s=24,color='#1d6484',zorder=4)
ax.axvline(0,color='#71808b',lw=.7,ls='--')
ax.set(xlabel='Extended minimum normal position μ',ylabel='Tangential cap displacement Δt',title='Exact displacement from x = h back to x = h',xlim=(-1/64,1/64))
ax.set_xticks([-1/64,0,1/64],['−1/64','0','1/64']);ax.grid(alpha=.15)
fig.text(.5,.09,'Left: arrows follow +Hₚ; dotted segment is a covector jump at x = 0.  Here h = 1/16.',ha='center',fontsize=10)
fig.text(.5,.04,'Right: continuity at μ = 0 is sufficient; differentiability there is not asserted.  Proof: B1 and Exercise 1.',ha='center',fontsize=10)
svg=ROOT/'figures/turning-reflection-and-cap.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['DB6','DB30','DB31','F0'],'cap_height':'1/16',
 'left_minima':['-1/100','0','1/100'],'left_coordinates':['rho','x'],'left_formula':'x=mu+rho^2, restricted to 0<=x<=1/16',
 'right_interval':['-1/64','1/64'],'right_formula':'-4*sqrt(1-mu)*(sqrt(1/16-mu)-sqrt(max(-mu,0)))',
 'reflection_segment':'Covector jump from -sqrt(-mu) to +sqrt(-mu) at x=0; not an ordinary Hamilton arc.',
 'meaning':'Exact coordinate projection and continuous broken cap map, not a numerical PDE solution.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps(record))
