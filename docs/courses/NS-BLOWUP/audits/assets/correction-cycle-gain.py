"""Draw the exact exponent gains proved in correction-cycle-audit.md, K7.

Source comparison: OpenAI, Finite Time Blowup for Navier–Stokes, original
Proposition 9.6, pages 107–111. This is a plot of proved rational bounds,
not numerical evidence for the estimates or the blowup theorem.
"""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

k=F(1,100000)
gains=[F(2,5)-k,F(9,50)-k,F(9,10)-2*k]
assert gains==[F(39999,100000),F(17999,100000),F(89998,100000)]
assert min(gains)>F(1,10)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(13.6,5.7),dpi=160)
fig.patch.set_facecolor('#f6f8fb');ax.set_facecolor('#f6f8fb')
colors=['#276986','#9c5b28','#35775d']
names=['Supported wave residual','Complete tangential means','Three integral defects']
bars=ax.barh([2,1,0],[float(x) for x in gains],height=.47,color=colors)
for y,x in zip([2,1,0],gains):
 ax.text(float(x)+.015,y,f'{int(x*100000)}/100000 = {float(x):.5f}',va='center',fontsize=11,color='#172c3c')
ax.axvline(.1,color='#687885',ls='--',lw=1.5)
ax.axvline(float(min(gains)),color='#9c5b28',ls=':',lw=1.8)
ax.text(.1,2.48,'Original required gain\n1/10',ha='center',va='bottom',fontsize=10,color='#526370')
ax.text(float(min(gains)), -.64,'Common proved gain: 17999/100000',ha='left',va='top',fontsize=11,color='#9c5b28')
ax.set_yticks([2,1,0],names);ax.set_ylim(-.9,3.1);ax.set_xlim(0,1.25)
ax.set_xlabel('Gain in the exponent of ε, for one complete correction cycle')
ax.set_xticks([0,.1,.2,.4,.6,.8,1.0]);ax.grid(axis='x',alpha=.16);ax.set_axisbelow(True)
for side in ['top','right','left']:ax.spines[side].set_visible(False)
ax.spines['bottom'].set_color('#b7c5cd');ax.tick_params(axis='y',length=0,pad=12)
fig.suptitle('The four updates improve all three residual bounds',x=.05,y=.98,ha='left',fontsize=18,fontweight='bold',color='#172c3c')
fig.text(.05,.91,'Exact inequalities from K7.1–K7.2; κₛ = 1/100000. Original stage definitions are unchanged.',fontsize=11,color='#3c5365')
fig.text(.05,.025,'Original source: OpenAI, Proposition 9.6, pp. 107–111. This local cycle estimate does not verify the complete blowup theorem.',fontsize=9.5,color='#526370')
fig.subplots_adjust(left=.245,right=.98,bottom=.21,top=.8)
stem=Path(__file__).with_suffix('')
fig.savefig(stem.with_suffix('.png'),facecolor=fig.get_facecolor())
fig.savefig(stem.with_suffix('.svg'),facecolor=fig.get_facecolor())
print('Wrote the rational-gain diagram and its SVG; no numerical proof calculation.')
