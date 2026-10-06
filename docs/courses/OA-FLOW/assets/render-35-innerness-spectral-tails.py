from pathlib import Path
import json, hashlib
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='oa-flow-innerness-tail-v1'
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
b=Path(__file__).resolve().parent
levels=np.array([0,2,5]); frequencies=levels[:,None]-levels[None,:]
x=np.zeros((3,3),dtype=int); x[1,0]=1; x[2,1]=1
assert (frequencies[x==1]==np.array([2,3])).all()
def tails(s):
 if s<=0: return [1,1,1]
 return [int(any(frequencies[j,k]>=s for k in range(3))) for j in range(3)]
assert tails(0)==[1,1,1] and tails(1)==[0,1,1] and tails(2)==[0,1,1]
assert tails(2.01)==[0,0,1] and tails(5)==[0,0,1] and tails(5.01)==[0,0,0]
fig,(ax,bx)=plt.subplots(1,2,figsize=(12,5.9),gridspec_kw={'width_ratios':[1,1.15]})
fig.patch.set_facecolor('#ffffff')
fig.suptitle('Spectral differences reconstruct an internal implementer',fontsize=17,y=.98)
ax.set_title(r'$h=\mathrm{diag}(0,2,5),\quad x=E_{21}+E_{32}$',fontsize=14,pad=16)
for j in range(3):
 for k in range(3):
  chosen=bool(x[j,k]); y=2-j
  ax.add_patch(Rectangle((k,y),1,1,facecolor='#cbe8ee' if chosen else '#f3f5f7',edgecolor='white',lw=2))
  ax.text(k+.5,y+.60,f'{frequencies[j,k]:+d}' if frequencies[j,k] else '0',ha='center',va='center',fontsize=19,color='#143c4b' if chosen else '#596574')
  if chosen: ax.text(k+.5,y+.22,r'$x_{%d%d}=1$'%(j+1,k+1),ha='center',va='center',fontsize=12,color='#143c4b')
ax.set_xlim(0,3); ax.set_ylim(0,3); ax.set_aspect('equal')
ax.set_xticks([.5,1.5,2.5],['0','2','5']); ax.set_yticks([2.5,1.5,.5],['0','2','5'])
ax.set_xlabel(r'Input level $\lambda_k$',fontsize=12); ax.set_ylabel(r'Output level $\lambda_j$',fontsize=12)
ax.tick_params(length=0,pad=7); [sp.set_visible(False) for sp in ax.spines.values()]
ax.text(.5,-.31,r'Each cell is $\lambda_j-\lambda_k$. Shaded blocks give $S_\alpha(x)=\{2,3\}$.',transform=ax.transAxes,ha='center',fontsize=11)
bx.set_title(r'Range tail $Q_s=E([s,\infty))$',fontsize=14,pad=16)
colors=['#6d8296','#31788a','#184b60']
for j,level in enumerate(levels):
 bx.plot([-.7,level],[j,j],lw=5,color=colors[j],solid_capstyle='butt')
 bx.plot(level,j,'o',ms=8,color=colors[j],zorder=5)
 bx.plot([level,5.7],[j,j],lw=1,color='#cbd4db',ls=':')
bx.set_yticks([0,1,2],[r'$e_1$ (level $0$)',r'$e_2$ (level $2$)',r'$e_3$ (level $5$)'])
bx.set_xticks([0,2,5]); bx.set_xlim(-.7,5.7); bx.set_ylim(-.6,2.6)
bx.set_xlabel(r'Threshold $s$',fontsize=12)
bx.grid(axis='x',color='#dce3e8',lw=.8)
bx.spines['top'].set_visible(False); bx.spines['right'].set_visible(False)
bx.text(.5,-.23,'A solid segment means the coordinate is in the range.\nFilled endpoints record the closed tail [s, ∞).',transform=bx.transAxes,ha='center',fontsize=11)
fig.subplots_adjust(left=.07,right=.98,top=.83,bottom=.30,wspace=.50)
fig.text(.5,.03,'Exact finite example; the general proof uses arbitrary projection joins.  Proof: GI.11–GI.19; Exercise 1.',ha='center',fontsize=10,color='#3c4753')
fig.savefig(b/'35-innerness-spectral-tails.png',dpi=180,metadata={'Software':'OA-FLOW reproducible mathematical figure'})
fig.savefig(b/'35-innerness-spectral-tails.svg',metadata={'Date':None,'Creator':'OA-FLOW reproducible mathematical figure'})
# Remove only Matplotlib's external SVG document-type declaration.
# The original vector geometry and attributes remain unchanged.
import re
svg_path=b/'35-innerness-spectral-tails.svg'
svg_path.write_bytes(re.sub(br'<!DOCTYPE[^>]*>\s*',b'',svg_path.read_bytes(),count=1))
plt.close(fig)
checks={'kind':'finite_example_only_not_theorem_proof','levels':levels.tolist(),'matrix_frequencies':frequencies.tolist(),'nonzero_x_entries':[[2,1],[3,2]],'x_spectrum':[2,3],'tail_intervals':[{'condition':'s <= 0','range_coordinates':[1,2,3]},{'condition':'0 < s <= 2','range_coordinates':[2,3]},{'condition':'2 < s <= 5','range_coordinates':[3]},{'condition':'s > 5','range_coordinates':[]}],'generator_norm':5,'proof_locators':['GI.11','GI.13','GI.15','GI.16','GI.17','GI.18','GI.19','GI.8 Exercise 1'],'artifacts':[]}
for name in ['35-innerness-spectral-tails.png','35-innerness-spectral-tails.svg']:
 p=b/name; data=p.read_bytes(); checks['artifacts'].append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(b/'35-innerness-figure-data.json').write_bytes((json.dumps(checks,indent=2)+'\n').encode())
print(json.dumps(checks,indent=2))
