"""Original primitive partners and exact stored cutoff observations."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
R=Path(__file__).resolve().parent
datafile=R.parent/'state/CHEN_HOU_CUTOFF_LOOKUP_DATA.json'
if not datafile.exists():datafile=R/'CHEN_HOU_CUTOFF_LOOKUP_DATA.json'
data=json.loads(datafile.read_text(encoding='utf-8'))
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
r=np.linspace(0,3.2,1600)
P=lambda r:2*r/(((r-1)**2+1)*((r+1)**2+1))
Pa=np.where(r<=.5,P(r),np.where(r<=2.5,.5*(1/((r-1)**2+1)-4/13),0))
Ta=1+np.sqrt(5897/7428)
roots=np.roots([16,4,1,-256]);Tinf=float(next(v.real for v in roots if abs(v.imag)<1e-10 and v.real>0))
level=128/1025;ax=axs[0]
ax.plot(r,P(r),label='Full primitive P',color='#1d5d91',lw=2)
ax.plot(r,Pa,label='Rectangle primitive Pₐ',color='#bc5c25',lw=2)
ax.axhline(level,color='#657177',ls=':',lw=1.3)
ax.scatter([.25,Ta,Tinf],[level]*3,color=['#242e39','#bc5c25','#1d5d91'],zorder=4)
ax.annotate('r = 1/4',xy=(.25,level),xytext=(.08,.05),arrowprops={'arrowstyle':'->'})
ax.annotate('Tₐ = 1 + √(5897/7428)',xy=(Ta,level),xytext=(.15,.52),arrowprops={'arrowstyle':'->','color':'#bc5c25'},color='#9c4014')
ax.annotate('16T∞³ + 4T∞² + T∞ − 256 = 0',xy=(Tinf,level),xytext=(1.2,.44),arrowprops={'arrowstyle':'->','color':'#1d5d91'},color='#1d5d91',fontsize=10)
ax.set(xlabel='Original horizontal coordinate',ylabel='Full primitive value',ylim=(-.015,.66),title='The rectangle edge changes the partner\nh = 2, δ = 1, t = 1, a = 3/2')
ax.legend(loc='upper right',fontsize=10)
ax=axs[1];xs=np.arange(4)
ys=[float(Fraction(row['stored_upper'])) for row in data['rows']]
ax.bar(xs,ys,color='#819eb7',width=.6,label='Stored upper endpoints')
ax.axhline(2.549,color='#a44423',lw=2,label='Certified uniform bound: 2.549')
for n,(y,row) in enumerate(zip(ys,data['rows'])):
 ax.text(n,y-.1,f'{y:.6f}',ha='center',va='top',color='white',fontweight='bold',fontsize=10)
 ax.text(n,y+.025,'index '+str(row['matlab_index']),ha='center',fontsize=9)
ax.set_xticks(xs,['∞','6','3','3/2'])
ax.set(xlabel='Original window-to-separation argument A(d)',ylabel='Physical horizontal constant, including 4/π',ylim=(0,2.9),title='Stored finer values remain to be certified\nGlobal certification does not validate each entry')
ax.legend(loc='lower left',fontsize=9)
fig.supxlabel('Complete calculations: EX12–EX18 and EX26–EX32. Chen–Hou transport and author code, cited in the lesson.\nCurves and root markers are illustrative; formulas and intervals in the proof are exact. Blue bars are stored data, not certified integral bounds.',fontsize=10,y=-.055)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-partners-and-cutoff-values.'+ext),dpi=170,bbox_inches='tight')
(R/'chen-hou-partners-and-cutoff-samples.json').write_text(json.dumps({'localized_partner':Ta,'sampled_global_partner':Tinf,'stored_upper_values':ys,'uniform_certified_upper':'2549/1000','display_only':True},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'localized_partner':Ta,'sampled_global_partner':Tinf,'stored_values':ys}))
