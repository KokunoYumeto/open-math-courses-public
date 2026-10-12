"""Original positive strip and exact local correction: reproducible samples."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P = Path(__file__).resolve()
data = json.loads((P.parent.parent/'state/CHEN_HOU_VERTICAL_CELL_AREA_EXACT_CHECK.json').read_text(encoding='utf-8'))
number = lambda value: float(Fraction(value))
mid = lambda row: (number(row['lower'])+number(row['upper']))/2
eps = 2**-12
x = np.linspace(0, 1, 301)
t = np.linspace(0, eps, 151)
X, T = np.meshgrid(x, t)
K = ((X+1)**2-T*T)/(2*((X+1)**2+T*T)**2)
A = mid(data['original_integral_A'])
fig, axs = plt.subplots(2, 2, figsize=(13, 9.5), layout='constrained')
fig.suptitle('Original positive strip: a full cell integral must be counted once\nChen–Hou vertical routine, lines 260–279 · exact proof VA1–VA19', fontsize=14)
ax=axs[0,0]
mesh=ax.pcolormesh(x,t,K,shading='auto',cmap='viridis')
fig.colorbar(mesh,ax=ax,label='Full original kernel K₊(x,t)')
ax.set(xlabel='Original coordinate x',ylabel='Original height t',title='Positive on the entire original strip · VA1')
ax.set_yticks([0,eps/2,eps],['0','2⁻¹³','2⁻¹²'])
ax.text(.04,.92,'Height enlarged for visibility\nUnequal display scales',transform=ax.transAxes,va='top',color='white',fontsize=10)
ax=axs[0,1]
density=eps*np.sqrt(2)/4*np.sqrt(x)/((1+x)**2+eps**2)
ax.plot(x,density,color='#187786',lw=2)
ax.fill_between(x,0,density,alpha=.2,color='#187786')
ax.set(xlabel='Original coordinate x',ylabel='Full height-integrated density',title='The exact regular contribution A · VA9–VA11')
ax.text(.04,.13,'A = 0.000024634639988116…\nEntire finite-series remainder retained',transform=ax.transAxes,fontsize=10)
ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax.grid(alpha=.2)
ax=axs[1,0]
vals=[3*eps**2/4096,A,np.sqrt(2)*eps/8]
labels=['Coded value: strict upper bound','Exact intended integral A','Elementary upper bound for U']
ax.barh(range(3),vals,color=['#bd633e','#187786','#6b7a95'])
ax.set_xscale('log');ax.set_xlim(1e-12,1e-3)
ax.set_yticks(range(3),labels,fontsize=9);ax.invert_yaxis()
ax.set(xlabel='Per-quadrant contribution (log scale)',title='Extra cell area causes a real undercount · VA5–VA7')
for i,val in enumerate(vals):ax.text(val*1.18,i,f'{val:.5g}',va='center',fontsize=9)
ax.grid(axis='x',alpha=.2)
ax=axs[1,1]
keys=['vx_2.60','uy_2.61'];pos=np.arange(2)
coarse=[mid(data['full_anisotropy_and_repair_margins'][k]) for k in keys]
direct=[mid(data['direct_repair_and_anisotropy_margins'][k]) for k in keys]
ax.bar(pos-.16,coarse,width=.30,label='Elementary correction d*',color='#6b7a95')
ax.bar(pos+.16,direct,width=.30,label='Direct integral correction dA',color='#187786')
ax.set_xticks(pos,['vₓ: target 2.60','uᵧ: target 2.61'])
ax.set(ylabel='Remaining margin below the printed target',title='Complete parameter change and both repairs\nVA16, VA19')
ax.legend(fontsize=9);ax.grid(axis='y',alpha=.2)
ax.text(.03,.95,'Arithmetic comparisons only:\nremaining saved costs are not certified.',transform=ax.transAxes,va='top',fontsize=9)
ax.set_ylim(0,max(direct)*1.4)
fig.supxlabel('Original width ε = 2⁻¹². Plotted samples illustrate the proof; exact rational checks certify the bounds.',fontsize=10)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=175)
plt.close(fig)
meta={'at':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'proof':'CHEN_HOU_VERTICAL_CELL_AREA_WORK_20261011.md','locators':'VA1–VA19','original_epsilon':'1/4096',
 'source_attribution':'Jiajie Chen and Thomas Y. Hou, original vertical routine lines260–279, Part II v3 int_holy_vx_in0–int_holy_vx_in2 and Part I v4 lines3367–3378.',
 'scope':'Original coordinates and full local receiving factors; comparisons are not full saved-cost certificates.',
 'visual_inspection':'pending'}
P.with_suffix('.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':str(P.with_suffix('.png'))}))
