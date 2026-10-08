"""Reproduce the original entropy diagram with Python and Matplotlib.

Run beside data.json; the fonts are shared with ../typeiii-zero-decomposition/.
For a separate working directory, pass --font-dir with that existing folder.
"""
from pathlib import Path
from fractions import Fraction
import argparse
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle

BASE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=BASE.parent/'typeiii-zero-decomposition')
args = parser.parse_args()
for name in ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf']:
    font_manager.fontManager.addfont(args.font_dir/name)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'path',
                     'svg.hashsalt':'oa-flow-entropy-returns-v1','savefig.facecolor':'#f7f9fc'})
d = json.loads((BASE/'data.json').read_text(encoding='utf-8'))
prob = [Fraction(v) for v in d['return_probabilities']]
tail = Fraction(d['return_tail_n_at_least_7'])
assert prob == [Fraction(1,2**n) for n in range(1,7)]
assert sum(prob) + tail == 1 and tail == Fraction(1,64)
assert d['included_word_times'] == [1,2,3] and d['return_mean'] == 2
heights = [float(Fraction(v)) for v in d['entropy_multiples_of_log2']]
assert heights == [1,2,.5]

ink, blue, green, orange = '#18334b', '#2768a8', '#16765f', '#b66024'
fig = plt.figure(figsize=(16,12), facecolor='#f7f9fc')
gs = fig.add_gridspec(2,2,left=.075,right=.955,top=.86,bottom=.13,hspace=.58,wspace=.32,
                      height_ratios=[.85,1])
a = fig.add_subplot(gs[0,:]); b = fig.add_subplot(gs[1,0]); c = fig.add_subplot(gs[1,1])
fig.text(.075,.955,'The same information, counted by three clocks',fontsize=23,
         fontweight='bold',color=ink)
fig.text(.075,.915,'Fair binary shift: E = {current bit is 1}, μ(E) = 1/2; logarithms are natural.',
         fontsize=14,color=ink)
a.set_title('A. A return word starts after the current visit and includes the next visit',
            loc='left',fontsize=16,color=ink,pad=22)
a.set_xlim(-.5,3.8);a.set_ylim(-.85,1.3);a.axis('off')
a.add_patch(Rectangle((.67,-.21),2.66,.7,facecolor=blue,alpha=.10,edgecolor=blue))
for x,symbol in enumerate(d['word_symbols']):
    a.scatter([x],[.12],s=1050,facecolor='white',edgecolor=green if symbol else blue,lw=2.5,zorder=3)
    a.text(x,.12,str(symbol),ha='center',va='center',fontsize=18,fontweight='bold',color=ink)
    a.text(x,-.38,f't = {x}',ha='center',color=ink)
    a.text(x,.68,'E' if symbol else 'outside E',ha='center',fontsize=13,color=green if symbol else blue)
    if x:
        a.annotate('',(x-.14,.12),(x-1+.14,.12),arrowprops={'arrowstyle':'->','color':ink,'lw':1.6})
a.text(0,-.73,'known from the past',ha='center',fontsize=12,color=green)
a.text(2,-.73,'word 001: conditional probability 1/8; information 3 log 2',ha='center',fontsize=13,color=blue)
a.text(1.5,1.09,'The previous return word ends at t = 0. The current word is t = 1, 2, 3.',
       ha='center',fontsize=12,color=ink)
for ax in (b,c):
    ax.set_facecolor('white');ax.spines[['top','right']].set_visible(False)
    ax.tick_params(colors=ink);ax.yaxis.label.set_color(ink);ax.xaxis.label.set_color(ink)
b.set_title('B. All return lengths remain present',loc='left',fontsize=16,color=ink,pad=20)
bars=b.bar(range(1,8),[float(x) for x in prob]+[float(tail)],color=[blue]*6+[orange],width=.68)
b.set_xticks(range(1,8),['1','2','3','4','5','6','≥ 7'])
b.set_ylim(0,.61);b.set_ylabel('normalized section probability ν');b.set_xlabel('return length r; final bar groups the infinite tail')
for bar,label in zip(bars,d['return_probabilities']+[d['return_tail_n_at_least_7']]):
    b.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.015,label,ha='center',fontsize=11,color=ink)
b.text(.98,.90,'ν(r = n) = 2⁻ⁿ\nmean return = 2\nentropy = 2 log 2',transform=b.transAxes,
       ha='right',va='top',fontsize=13,color=ink)
c.set_title('C. Entropy per step depends on the clock',loc='left',fontsize=16,color=ink,pad=20)
bars=c.bar(range(3),heights,color=[blue,green,orange],width=.58)
c.set_ylim(0,2.48);c.set_ylabel('entropy / log 2')
c.set_xticks(range(3),['one shift\nstep','one return\nto E','one tower\nstep'],fontsize=12)
for bar,label in zip(bars,['1','2','1/2']):
    c.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.09,label,ha='center',fontsize=15,color=ink)
c.text(.5,-.26,'Return: divide by μ(E) = 1/2.\nTower over the binary shift: divide by mean roof 2.',
       transform=c.transAxes,ha='center',va='top',fontsize=11,color=ink)
fig.text(.075,.055,'Proofs: endpoint convention IE32/37/42; complete geometric law IE56; entropy changes IE3 and IE48.',
         fontsize=12,color=ink)
fig.text(.075,.025,'The tower in C is a separate system over the binary shift, with the unbounded roof from Diagnostic 9.',
         fontsize=11,color=ink)
fig.savefig(BASE/'entropy-returns.png',dpi=140,metadata={'Software':'OA-FLOW original figure'})
fig.savefig(BASE/'entropy-returns.svg',metadata={'Date':None,'Creator':'OA-FLOW original figure'})
plt.close(fig)
print(json.dumps({'return_mass_exact':str(sum(prob)+tail),'tail_exact':str(tail),'entropy_multiples':heights}))
