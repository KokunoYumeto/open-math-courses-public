"""Original adaptive V derivative profile, TR-BAKER Figure10.31. CC0.

Lemmas10.134–10.135, Theorem10.136 and Solution52 prove the bounds.
Human-source context: free Yu2013 Section5 original parameter ranges.
"""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from V_adaptive_comparison import terms, run, node_factor, step_margin

t=terms(2)
a,q=t['a'],t['q']
common=t['b']+t['n']+t['e']*t['H']+3*t['l']/2
B0=common+q*(1+1/t['Sm'])/(t['c2']*t['Q'])
B1=common+t['l']+q*q/(t['c2']*t['Q'])
d0=(B0+step_margin)/(2*q*(q-1)*a)
d1=node_factor*(B1+step_margin)/(2*q*q*a)
tau=[1-d0,1-d0-d1]
cutoffs=[int(x*10000) for x in tau]
old=[int(t['eta']**j*10000) for j in [1,2]]
out=int(t['H']*10000)
assert all(x>y for x,y in zip(cutoffs,old)) and out<old[-1]
data=run()
mass=[];inputs=[]
for rank in list(range(2,8))+['all_r_ge_8']:
    vals=[x for x in data['finite']+data['uniform'] if x['rank']==rank]
    mass.append((min(int(F(x['fractional_gap'])*1000) for x in vals))/1000)
    inputs.append((min(int(F(x['input_gap'])*1000) for x in vals))/1000)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,(ax,bx)=plt.subplots(2,1,figsize=(7.9,8.0),layout='constrained')
fig.set_facecolor('#f8fafc')
inner=F(3003,1000)
ax.step([0,float(inner),9],[cutoffs[0],cutoffs[1],cutoffs[1]],where='post',
        color='#12667e',linewidth=2.5,label='Adaptive full integer cutoff')
ax.step([0,float(inner),9],[old[0],old[1],old[1]],where='post',
        color='#af7045',linewidth=2,linestyle='--',label='Original full integer cutoff')
ax.axhline(out,color='#5e6574',linestyle=':',linewidth=2,label='Fractional output cutoff')
ax.axhline(10000,color='#76945b',linewidth=1.5,xmin=0,xmax=float(inner/9))
ax.text(.1,9580,'Deleted inner nodes: order 10000',fontsize=12)
ax.set_xlim(0,9);ax.set_ylim(3500,12500)
ax.set_xticks([0,float(inner),9],['0','3.003','9']);ax.set_xlabel('Absolute integer radius / Sᵢ (rounded inner 3.003, outer 9)')
ax.set_ylabel('Retained total derivative order')
ax.set_title('More retained derivatives feed the fractional step',fontweight='bold',pad=12)
ax.text(5.1,10100,f'Adaptive cutoffs: {cutoffs[0]}, {cutoffs[1]}\nOriginal cutoffs: {old[0]}, {old[1]}\nFractional output: {out}',fontsize=12)
ax.legend(loc='upper left',fontsize=11,framealpha=.96)
xs=list(range(7))
bx.bar([x-.18 for x in xs],mass,width=.34,color='#12667e',label='Fractional mass minus arithmetic')
bx.bar([x+.18 for x in xs],inputs,width=.34,color='#af7045',label='Fractional input minus arithmetic')
for x,m,i in zip(xs,mass,inputs):
    bx.text(x-.18,m+.15,f'{m:.3f}',ha='center',fontsize=10,rotation=90)
    bx.text(x+.18,i+.15,f'{i:.3f}',ha='center',fontsize=10,rotation=90)
bx.axhline(0,color='#526174',linewidth=1)
bx.set_xticks(xs,['2','3','4','5','6','7','Every r≥8'])
bx.set_ylim(0,17);bx.set_ylabel('Strict certified lower gap')
bx.set_xlabel('Original rank r');bx.set_title('Both fractional entries exceed the arithmetic bound',fontweight='bold',pad=12)
bx.legend(loc='upper left',fontsize=11,framealpha=.96)
for axis in [ax,bx]:axis.grid(axis='y',alpha=.13);axis.set_axisbelow(True)
fig.savefig(Path(__file__).with_name('V-adaptive-profile.png'),dpi=170,
            metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 figure'})
print({'adaptive_orders':cutoffs,'original_orders':old,'fractional_output':out})
