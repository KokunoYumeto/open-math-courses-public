"""CC0-1.0. Exact incoming curves and ordered matrix transport."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-incoming-support','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(12,5.6))
fig.subplots_adjust(left=.08,right=.975,bottom=.2,top=.79,wspace=.34)
fig.suptitle('An entire incoming family and its ordered matrix transport',fontsize=15,fontweight='bold',y=.97)
ax=axes[0];x1=1/16;center=1/96;radius=1/384
ax.add_patch(Rectangle((-1/1024,0),2/1024,1/64,facecolor='#eedba9',edgecolor='#aa872f',alpha=.45,label='Initial family'))
for a,color in [(0,'#1d6484'),(1/256,'#885294'),(1/64,'#b75932')]:
 for z0 in [-1/1024,0,1/1024]:
  x=np.linspace(a,x1,220);z=z0+2/3*(x**1.5-a**1.5)
  ax.plot(z,x,color=color,lw=1.2)
  ax.scatter([z0],[a],s=12,color=color,zorder=4)
  lo,hi=125,151
  ax.annotate('',xy=(z[lo],x[lo]),xytext=(z[hi],x[hi]),arrowprops={'arrowstyle':'->','color':color,'lw':1.2})
ax.plot([center-radius,center+radius],[x1,x1],color='#167a52',lw=4,label='Assumed regular slice')
ax.scatter([center-radius,center+radius],[x1,x1],s=36,facecolor='white',edgecolor='#167a52',zorder=5)
ax.axhline(x1,color='#167a52',alpha=.18)
ax.set(xlabel='Tangential position z',ylabel='Normal position x',title='p = ρ² − xη²,  η = 1,  ρ = −√x',xlim=(-.0025,.0145),ylim=(-.003,.07))
ax.set_yticks([0,1/64,1/32,1/16],['0','1/64','1/32','1/16'])
ax.legend(loc='upper left',fontsize=8.5)
ax.grid(alpha=.15)
ax=axes[1];x=np.linspace(0,1,150)
ax.plot(x,np.ones_like(x),color='#1d6484',label='Re q₁₁ = 1')
ax.plot(x,2*np.ones_like(x),color='#885294',label='Re q₂₂ = 2')
ax.plot(x,x,color='#b75932',label='Im q₁₂ = x')
ax.set(xlabel='Evolution coordinate x (Exercise 1)',ylabel='Exact matrix entry',title='q = (I + ixN) diag(1,2) (I − ixN)',xlim=(0,1),ylim=(-.12,2.3))
ax.legend(loc='center right');ax.grid(alpha=.15)
fig.text(.5,.085,'Left arrows follow +Hₚ, toward smaller x.  Right: N₁₂ = 1, all other entries zero.',ha='center',fontsize=10)
fig.text(.5,.04,'Proofs and exact constants: Exercises 1 and 3, (IS23), (IS28)–(IS29).',ha='center',fontsize=10)
svg=ROOT/'figures/incoming-tube-and-matrix-transport.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['IS23','IS28','IS29','F0'],
 'initial_heights':['0','1/256','1/64'],'initial_positions':['-1/1024','0','1/1024'],
 'slice':'x=1/16','slice_center':'1/96','open_slice_radius':'1/384','Hamilton_arrows':'decreasing x',
 'matrix_entries':['Re q11=1','Re q22=2','Im q12=x'],'matrix_parameter_interval':[0,1],
 'meaning':'Exact formulas. The slice regularity is assumed, and no numerical PDE propagation is inferred.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps(record))
