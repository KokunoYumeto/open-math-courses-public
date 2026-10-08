"""Original integer-extension margins and q-denominator absorption. CC0.

TR-BAKER-10 Figure10.28; Lemmas10.122,10.124–10.125 and Solution48.
All infinite-case and endpoint arguments are proved in the lesson.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from integer_comparison_bounds import records, analytic_endpoints

analytic_endpoints(); exact=records()
names=['I.1','I.2','II','III.1','III.2','IV.P1','IV.Plarge','V']
labels=['I.1','I.2','II','III.1','III.2','IV\nP=1','IV\nP≥7','V']
low=np.array([80,17,91,52,22,28,592,248])/1000
high=np.array([76,5,89,65,45,47,690,402])/1000
for name,a,b in zip(names,low,high):
 assert min(v['lower_decimal'] for v in exact if v['case']==name and not v['uniform_after_rank8'])>a
 assert next(v['lower_decimal'] for v in exact if v['case']==name and v['uniform_after_rank8'])>b
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,5.8),gridspec_kw={'width_ratios':[1.1,1]},layout='constrained')
fig.set_facecolor('#f8fafc')
xs=np.arange(8)
ax.scatter(xs-.09,low,s=70,color='#1d6d9a',label='Minimum over ranks 2–7')
ax.scatter(xs+.09,high,s=65,marker='D',color='#b5472d',label='Uniform bound for all ranks ≥8')
ax.axhline(1/200,color='#63489a',linestyle='--',linewidth=1.5,label='Required strict margin: 1/200')
ax.set_yscale('log');ax.set_ylim(.0035,1.1);ax.set_xticks(xs,labels)
ax.set_yticks([.005,.01,.05,.1,.5,1],['0.005','0.01','0.05','0.1','0.5','1'])
ax.grid(axis='y',alpha=.2);ax.set_ylabel('Proved lower bound for comparison margin')
ax.set_title('All original field and rank cases',pad=14,fontweight='bold')
ax.legend(loc='upper left',fontsize=10,framealpha=.93)
ax.annotate('I.2 exact margin > 0.005153',xy=(1.09,.005),xytext=(2,.008),fontsize=10,
 arrowprops={'arrowstyle':'->','color':'#b5472d'},color='#96361f')
q=2;c2=7/4;c4=20.8;eta=1-.538/3;Q=q*eta**3;D=4+math.log(3);lam=189/188;j=1
end=3*D/math.log(Q)
depth=np.linspace(0,end,450)
def ratio(z):return Q**(-z)+lam*c2*math.log(q)*z/(c4*q**(j+1)*D)
curve=ratio(depth);endpoint=ratio(end)
assert 0<endpoint<1
chord=1+(endpoint-1)*depth/end
bx.plot(depth,curve,color='#1d6d9a',linewidth=2.4,label='Torus height + depth cost')
bx.plot(depth,chord,color='#b5472d',linestyle='--',linewidth=1.7,label='Convex upper chord')
nodes=np.arange(0,math.floor(end)+1)
bx.scatter(nodes,ratio(nodes),s=9,color='#1d6d9a',alpha=.75)
bx.axhline(1,color='#63489a',linewidth=1,linestyle=':',label='Original budget at depth zero')
bx.scatter([0,end],[1,endpoint],s=60,color='#b5472d',zorder=4)
bx.set_xlim(0,end);bx.set_ylim(0,1.08);bx.grid(alpha=.2)
bx.set_xlabel('Continuous geometric depth z; dots at integers')
bx.set_ylabel('Cost divided by its value at depth zero')
bx.set_title('Contraction pays the q-denominator',pad=14,fontweight='bold')
bx.legend(loc='upper right',fontsize=10,framealpha=.93)
bx.text(.47,.45,'I.2, r=2, j=1\nGeometric depth only\nMultiplicity condition separate',transform=bx.transAxes,
 ha='center',fontsize=10,bbox={'facecolor':'white','edgecolor':'#d3dae4','boxstyle':'round,pad=.5'})
fig.savefig(Path(__file__).with_name('general-integer-extension.png'),dpi=180,
 metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 figure'})
