"""Exact signed atoms,carrier sums,crossed supports and shared frequencies."""
from pathlib import Path
import hashlib,json
import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'figures';OUT.mkdir(exist_ok=True)
mp.mp.dps=65
mass=mp.quad(lambda t:mp.exp(-1/(1-t*t))if abs(t)<1 else mp.mpf(0),[-1,0,1])
normalizer=1/mass
blue='#17658a';red='#bb553f';green='#32765c';gray='#6b747b'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN02-joint-convolution195'})
geometry={
 'schema':'AN02-joint-convolution-original-geometry195/v1',
 'atomic':{'u':[[0,1],[1,1]],'v':[[0,1],[1,-1]],'convolution':[[0,1],[2,-1]],
 'cancelled_mass':{'location':1,'sum':0},'input_carriers':[[0,1],[0,1]],'output_carrier':[0,2],
 'input_indicators':'max(0,eta)','output_indicator':'2 max(0,eta)',
 'persistent_real_zero_sequence':'c_j=2*pi*j for v and u*v',
 'canonical_profile_at_z0':0,'exact_transform_log_at_z0':'minus infinity',
 'proof_locators':['Learner Worked example2','Formal Lemmas2.1–2.4','Formal Theorem1.1']},
 'crossed':{'p_support':{'x1':0,'x2_interval':[-1,1]},
 'q_support':{'x1_interval':[-1,1],'x2':0},'convolution_ordinary_support':[[-1,1],[-1,1]],
 'smooth_probability_density':'f(t)=C exp(-1/(1-t^2)) for |t|<1,otherwise0',
 'C_numerical_decimal':mp.nstr(normalizer,65),'convolution_function':'f(x1)*f(x2)',
 'convolution_singular_support':[],'convolution_logarithmic_carrier':[],
 'frequency_rays':[{'c':'(t,0),t->infinity','joint_status_after_extraction':['proper','collapsed']},
 {'c':'(0,t),t->infinity','joint_status_after_extraction':['collapsed','proper']},
 {'c':'(t,t),t->infinity','joint_status':['collapsed','collapsed']}],
 'individual_carrier_qualification':'A proper carrier is a nonempty compact convex subset of its component segment;the plot does not classify every such subset.',
 'heatmap_qualification':'257 by257 numerical samples of the specified actual smooth probability density product,inside its exact support square.',
 'proof_locators':['Learner Worked example3','Formal Lemma2.3','Formal Theorem1.1']},
 'Blender_assessment':'Signed one-dimensional masses,two-dimensional support geometry and a shared real-frequency plane are fully represented in exact vector plots;an added third spatial dimension would not explain the synchronization.'}
(OUT/'geometry195.json').write_text(json.dumps(geometry,indent=2)+'\n',encoding='utf-8')
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=160,bbox_inches='tight',facecolor='white')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white',metadata={'Date':None})
 plt.close(fig)

fig=plt.figure(figsize=(15.3,7.4))
grid=fig.add_gridspec(3,2,width_ratios=[1.05,1.25],hspace=.48,wspace=.28)
for i,(title,atoms,color)in enumerate([
 ('u = δ₀ + δ₁',geometry['atomic']['u'],blue),
 ('v = δ₀ − δ₁',geometry['atomic']['v'],red),
 ('u * v = δ₀ − δ₂',geometry['atomic']['convolution'],green)]):
 ax=fig.add_subplot(grid[i,0]);ax.axhline(0,color=gray,lw=.9)
 for x,w in atoms:
  ax.plot([x,x],[0,w],color=color,lw=2.6)
  ax.scatter([x],[w],color=color,s=55,zorder=5)
  ax.text(x,w+(.13 if w>0 else -.23),'+1' if w>0 else '−1',ha='center',color=color,fontsize=11)
 if i==2:
  ax.scatter([1],[0],s=55,facecolor='white',edgecolor=gray,zorder=5)
  ax.text(1,.24,'+δ₁ − δ₁ = 0',ha='center',color=gray,fontsize=11)
 ax.set(xlim=(-.4,2.4),ylim=(-1.45,1.5),xticks=[0,1,2],yticks=[-1,0,1],title=title,
  ylabel='signed mass')
 if i==2:ax.set_xlabel('spatial position x')
 ax.grid(alpha=.14)
ax=fig.add_subplot(grid[:2,1]);eta=np.linspace(-1,1,301)
ax.plot(eta,np.maximum(eta,0),color=blue,lw=2.5,label='hᵤ = hᵥ = max(0, η)')
ax.plot(eta,2*np.maximum(eta,0),color=green,lw=2.5,label=r'$h_{u*v}=h_u+h_v$')
ax.scatter([0],[0],color=green,zorder=5,s=45)
ax.annotate('canonical value at η = 0 is 0',(0,0),xytext=(-.87,.36),fontsize=11,
 arrowprops={'arrowstyle':'-','color':gray})
ax.set(xlabel='imaginary direction η',ylabel='canonical profile / indicator',
 title='The proper limiting profiles add in local L¹',xlim=(-1,1),ylim=(-.14,2.25))
ax.grid(alpha=.18);ax.legend(loc='upper left',fontsize=11)
ax=fig.add_subplot(grid[2,1])
for y,(interval,color,label)in enumerate([
 ([0,1],blue,'Cᵤ = [0,1]'),([0,1],red,'Cᵥ = [0,1]'),([0,2],green,'Cᵤ + Cᵥ = [0,2]')]):
 level=2-y;ax.plot(interval,[level,level],color=color,lw=5)
 ax.scatter(interval,[level,level],color=color,s=32)
 ax.text(-.36,level,label,ha='right',va='center',fontsize=11,color=color)
ax.set(xlim=(-1.35,2.2),ylim=(-.45,2.45),xticks=[0,1,2],yticks=[],xlabel='carrier coordinate')
for spine in ['top','right','left']:ax.spines[spine].set_visible(False)
fig.suptitle('Signed cancellation preserves the selected convex carrier sum',fontsize=17,y=.98)
save(fig,'atomic-cancellation-and-carrier-addition')

fig,axes=plt.subplots(1,3,figsize=(18.2,6.1),gridspec_kw={'width_ratios':[1,1.1,1.12]})
ax=axes[0]
ax.plot([0,0],[-1,1],color=blue,lw=5);ax.plot([-1,1],[0,0],color=red,lw=5)
ax.text(.08,.66,'p: δ₀ ⊗ f',color=blue,fontsize=12)
ax.text(-1.07,-.17,'q: f ⊗ δ₀',color=red,fontsize=12)
ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),xlabel='x₁',ylabel='x₂',
 title='Two singular compact factors')
ax.set_aspect('equal');ax.grid(alpha=.16)
coord=np.linspace(-1,1,257);density=np.zeros_like(coord)
inside=np.abs(coord)<1
density[inside]=float(normalizer)*np.exp(-1/(1-coord[inside]**2))
values=density[:,None]*density[None,:]
ax=axes[1]
im=ax.imshow(values,extent=[-1,1,-1,1],origin='lower',cmap='YlGn',vmin=0,
 interpolation='nearest')
ax.add_patch(Rectangle((-1,-1),2,2,fill=False,edgecolor=green,ls='--',lw=1.6))
ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),xlabel='x₁',ylabel='x₂',
 title='p * q = f(x₁) f(x₂) is smooth')
ax.set_aspect('equal');ax.text(0,-1.17,'ordinary support: [−1,1]²',ha='center',fontsize=10)
cbar=fig.colorbar(im,ax=ax,fraction=.047,pad=.035);cbar.set_label('smooth probability density',fontsize=10)
ax=axes[2]
for end,color in [((1,0),blue),((0,1),red),((1,1),gray)]:
 ax.annotate('',end,(0,0),arrowprops={'arrowstyle':'->','lw':2.4,'color':color})
ax.text(.44,-.2,'(t,0): proper / ∅',ha='center',color=blue,fontsize=11)
ax.text(-.3,1.17,'(0,t): ∅ / proper',ha='left',color=red,fontsize=11)
ax.text(.57,.68,'(t,t): ∅ / ∅',ha='center',color=gray,fontsize=11,rotation=45)
ax.set(xlim=(-.35,1.24),ylim=(-.36,1.35),xlabel='shared real frequency c₁',ylabel='shared real frequency c₂',
 title='Both factors use the same sequence',xticks=[0,1],yticks=[0,1])
ax.set_aspect('equal');ax.grid(alpha=.16)
ax.text(-.31,-.31,'t → ∞; proper cases use a subsequence',fontsize=9)
fig.suptitle('Separate proper carriers exist; a common sequence forces an empty product carrier',fontsize=17,y=1.02)
fig.tight_layout()
save(fig,'crossed-factors-and-shared-frequency')
manifest=[]
for p in sorted(OUT.iterdir()):
 if p.is_file():
  b=p.read_bytes();manifest.append(dict(path=p.name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest().upper()))
(ROOT/'figure-manifest195.json').write_text(json.dumps(dict(original_geometry=True,files=manifest),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(figures=2,PNG_and_SVG_pairs=2,exact_geometry=True)))
