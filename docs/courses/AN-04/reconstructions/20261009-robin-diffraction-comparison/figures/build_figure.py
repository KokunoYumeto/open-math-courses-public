"""CC0-1.0. Exact Hamilton orbit and actual Dirichlet comparison identities."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'svg.fonttype':'none','svg.hashsalt':'AN04-robin-comparison','font.size':10})
fig,(ax,flow)=plt.subplots(1,2,figsize=(12,6.4),gridspec_kw={'width_ratios':[1,1.2]})
fig.subplots_adjust(left=.07,right=.98,bottom=.2,top=.82,wspace=.25)
fig.suptitle('Recover the actual value trace through a Dirichlet comparison',fontsize=14,fontweight='bold',y=.97)
for low,high,color,label in [(-.5,0,'#b4542a','Negative normal root: ρ < 0'),(0,.5,'#1d6484','Positive normal root: ρ > 0')]:
 s=np.linspace(low,high,240);x=s*s;t=-s-2*s**3/3
 ax.plot(t,x,color=color,label=label,lw=2)
 j=95;ax.annotate('',xy=(t[j+22],x[j+22]),xytext=(t[j],x[j]),arrowprops={'arrowstyle':'->','color':color,'lw':2})
ax.axhline(0,color='#657681',lw=.8)
ax.scatter([25/96],[1/16],color='#b4542a',zorder=5)
ax.annotate('Incoming cap\ns = −1/4\n(t, x) = (25/96, 1/16)',xy=(25/96,1/16),xytext=(.14,.145),
 arrowprops={'arrowstyle':'->','color':'#5c6570'},fontsize=9)
ax.scatter([0],[0],color='#172c3a',zorder=5)
ax.set(xlabel='Physical time t = y₁ + y₂',ylabel='Normal position x',xlim=(-.61,.61),ylim=(-.01,.285),
 title='Exact tangent orbit: μ = 0, λ = 1')
ax.set_yticks([0,1/16,1/4],['0','1/16','1/4'])
ax.legend(loc='upper center',fontsize=8);ax.grid(alpha=.15)
flow.set(xlim=(0,1),ylim=(0,1));flow.axis('off')
flow.set_title('Actual traces determine the order of inference')
labels=[
 'h = γu;   e = E⁺ᴰ hᶜ;   v = u − e',
 'γv is smooth; v has a regular incoming germ',
 'Finite-order Dirichlet theorem ⇒ Cv is smooth',
 'B⁺hᶜ = β − Cv is smooth',
 'Invert the full Robin row ⇒ h is smooth',
 'Uniform Airy collar regularity ⇒ u is regular'
]
for i,label in enumerate(labels):
 y=.88-i*.155
 box=FancyBboxPatch((.02,y-.055),.96,.108,boxstyle='round,pad=.008',facecolor='#edf4f6',edgecolor='#467d8b')
 flow.add_patch(box);flow.text(.5,y,label,ha='center',va='center',fontsize=9)
 if i<5:flow.annotate('',xy=(.5,y-.096),xytext=(.5,y-.059),arrowprops={'arrowstyle':'->','color':'#345b6a'})
fig.text(.5,.105,'Left: arrows follow +Hₚ; the positive-root Airy relation does not meet the marked negative-normal cap.',ha='center',fontsize=10)
fig.text(.5,.060,'The omitted coordinate is y₁ − y₂ = −s + 2s³/3.  Right: operator identities, not a solution plot.',ha='center',fontsize=10)
fig.text(.5,.022,'Proofs: R1–R8 and Exercise 3.  C = γDₓ + Mγ; the complete matrix Robin row is retained.',ha='center',fontsize=10)
svg=ROOT/'figures/robin-comparison-and-branches.svg'
fig.savefig(svg,metadata={'Date':None,'Creator':'Independent AN-04 figure; CC0-1.0'});plt.close(fig)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'svg':'figures/'+svg.name,'svg_sha256':sha(svg),'generator_sha256':sha(Path(__file__)),
 'licence':'CC0-1.0','proof_locators':['R6','R7','RC22','RC24','RC25','RC29','F0','Exercise 3'],
 'left_parameter_interval':['-1/2','1/2'],'left_coordinates':['t=y1+y2','x'],
 'left_formula':{'x':'s^2','rho':'s','t':'-s-2s^3/3','y1-y2':'-s+2s^3/3','mu':'0','lambda':'1'},
 'marked_cap':{'s':'-1/4','x':'1/16','t':'25/96'},
 'arrow_direction':'+H_p','right_meaning':'Actual value-trace subtraction and full conormal inverse, in the proved order.',
 'actually_inspected':False,'exact_coordinate_review_complete':False}
(ROOT/'figure-check.json').write_text(json.dumps(record,indent=2)+'\n','utf-8')
print(json.dumps({'figure':svg.name,'sha256':record['svg_sha256']}))
