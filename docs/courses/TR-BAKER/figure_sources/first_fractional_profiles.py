"""Original nested input profile and uniform first-stage margins. CC0.

TR-BAKER-10 Figure10.29; Lemmas10.128–10.129, Theorems10.130–10.131,
and Solutions49–50. Complete infinite-range proofs are in the lesson.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from first_fractional_bounds import records

data=records()
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13.3,5.8),gridspec_kw={'width_ratios':[1.1,1]},layout='constrained')
fig.set_facecolor('#f8fafc')
Rs=[379,758,1517];Ts=[1796752,1474535,1210101];O=993090
left=0;colors=['#9ccac8','#86b4d5','#b4b3d5']
for i,(R,T,color) in enumerate(zip(Rs,Ts,colors)):
 ax.fill_between([left,R],O/1e6,T/1e6,color=color,alpha=.8)
 ax.plot([left,R],[T/1e6]*2,color='#185b78',linewidth=2)
 if i<2:ax.plot([R,R],[Ts[i+1]/1e6,T/1e6],color='#185b78',linewidth=2)
 n=759 if i==0 else 2*(Rs[i]-Rs[i-1]);mu=T-O+1
 ax.text((left+R)/2,(O+T)/2e6,f'{n} nodes\nμ={mu:,}',ha='center',va='center',fontsize=10,color='#153746')
 left=R
ax.axhline(O/1e6,color='#ac4427',linestyle='--',linewidth=1.6,label='Target order: O=993090')
ax.axvline(687,color='#694b9b',linestyle=':',linewidth=1.6,label='Fractional target radius: |x|≤687')
ax.set_xlim(0,1517);ax.set_ylim(.87,1.87);ax.set_yticks([.99309,1.210101,1.474535,1.796752],['993090','1210101','1474535','1796752'])
ax.set_xlabel('Absolute argument; integer nodes and fractional targets')
ax.set_ylabel('Available total prepared-jet order')
ax.set_title('All earlier integer blocks contribute',fontweight='bold',pad=15)
ax.grid(axis='y',alpha=.16);ax.legend(loc='upper right',fontsize=9,framealpha=.95)
ax.text(.02,.035,'Annotations count both signs and zero.\nExact N*=1,304,340,501; last block alone: 658,631,420.',transform=ax.transAxes,fontsize=9,
 bbox={'facecolor':'white','edgecolor':'#cfd8e3','boxstyle':'round,pad=.4'})
names=['I.1','I.2','II','III.1','III.2','IV.P1','IV.Plarge','V']
labels=['I.1','I.2','II','III.1','III.2','IV\nP=1','IV\nP≥7','V']
lo=np.array([647,587,679,589,580,574,1061,25])/1000
co=np.array([392,332,420,384,348,391,836,6334])/1000
for name,a,b in zip(names,lo,co):
 row=next(v for v in data if v['case']==name and v['rank']=='all_r_ge_8')
 assert row['nested_gap_decimal']>a and row['contracted_gap_decimal']>b
xs=np.arange(8)
bx.scatter(xs-.09,lo,s=65,color='#185b78',label='Fractional: degree at most qʳd')
bx.scatter(xs+.09,co,s=65,color='#ac4427',marker='D',label='Contracted integers: degree d')
bx.axhline(1/50,color='#694b9b',linestyle='--',linewidth=1.5,label='Proved strict threshold: 1/50')
bx.set_yscale('log');bx.set_ylim(.015,10);bx.set_yticks([.02,.05,.1,.5,1,5],['0.02','0.05','0.1','0.5','1','5'])
bx.set_xticks(xs,labels);bx.grid(axis='y',alpha=.18)
bx.set_ylabel('Proved uniform lower comparison margin')
bx.set_title('Every original field case, all ranks ≥8',fontweight='bold',pad=15)
bx.legend(loc='upper left',fontsize=9,framealpha=.95)
bx.annotate('V exact fractional gap >0.025638',xy=(6.91,.025),xytext=(2.6,.04),fontsize=9,
 arrowprops={'arrowstyle':'->','color':'#185b78'},color='#185b78')
fig.savefig(Path(__file__).with_name('first-fractional-profiles.png'),dpi=180,
 metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 figure'})
