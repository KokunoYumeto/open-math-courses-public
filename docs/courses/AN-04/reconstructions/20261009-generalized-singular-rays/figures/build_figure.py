"""CC0-1.0. Three exact normal-position projections in physical wave time."""
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-generalized-rays','font.size':10})
fig,axs=plt.subplots(1,3,figsize=(12,5.4))
fig.subplots_adjust(left=.06,right=.98,bottom=.30,top=.76,wspace=.30)
fig.suptitle('Reflection, strict tangency and gliding in the physical clock',fontsize=14,fontweight='bold',y=.97)
t=np.linspace(-.6,.6,301)
data=[
 (4*np.abs(t)/5,'#315f82','Transverse reflection: κ = 0',
  'η = 3/5;  x = 4|t|/5\nρ = 4/5 before, −4/5 after\ny = −3t/5'),
 (t*t/4,'#b65a32','Strict diffraction: κ = −1',
  'η = 1;  x = t²/4\nρ = −t/2\ny = −t + t³/12'),
 (np.zeros_like(t),'#417b59','Boundary gliding: κ = 1',
  'η = 1;  x = ρ = 0\ny = −t\nThe gliding field cancels ρ̇ = 1/2')
]
for ax,(x,col,title,note) in zip(axs,data):
 ax.axhline(0,color='#75818a',lw=.8)
 ax.plot(t,x,color=col,lw=2.5)
 for j in [60,205]:
  ax.annotate('',xy=(t[j+20],x[j+20]),xytext=(t[j],x[j]),
   arrowprops={'arrowstyle':'->','lw':2,'color':col})
 ax.scatter([0],[0],color=col,s=25,zorder=5)
 ax.set(xlabel='Physical time t',ylabel='Normal position x',
  xlim=(-.65,.65),ylim=(-.035,.54),title=title)
 ax.set_xticks([-.6,0,.6],['−3/5','0','3/5'])
 ax.set_yticks([0,.09,.48],['0','9/100','12/25'])
 ax.grid(alpha=.15)
 ax.text(.5,-.31,note,transform=ax.transAxes,ha='center',va='top',fontsize=9)
fig.text(.5,.85,'pκ = τ² − ρ² − (1 + κx)η²,   x ≥ 0,   τ = 1.  Arrows follow increasing physical time.',ha='center',fontsize=11)
fig.text(.5,.025,'Exact coordinate projections for three different operators; no prescribed-ray solution construction is asserted.  Proof: Exercise 1.',ha='center',fontsize=9)
svg=ROOT/'figures/three-generalized-motions.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['SR19','SR20','SR21','F0'],
 'coordinates':['t','x'],'parameter_interval':['-3/5','3/5'],'tau':1,
 'panels':[{'kappa':0,'eta':'3/5','x':'4*abs(t)/5','rho':'4/5 before; -4/5 after','y':'-3*t/5'},
 {'kappa':-1,'eta':1,'x':'t^2/4','rho':'-t/2','y':'-t+t^3/12'},
 {'kappa':1,'eta':1,'x':0,'rho':0,'y':'-t','boundary_field':'Gliding, not the interior normal equation.'}],
 'meaning':'Exact normal-position projections for three distinct symbols, not numerical PDE solutions.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure':svg.name,'sha256':record['svg_sha256']}))
