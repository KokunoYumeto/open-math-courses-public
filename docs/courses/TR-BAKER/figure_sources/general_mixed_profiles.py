"""Original complete mixed interpolation profile, TR-BAKER Figure10.30. CC0.

Theorem10.132, Lemma10.133 and Solution51 prove the displayed quantities.
Human-source context: Yu's freely accessible2013 paper, Section5; the
full arbitrary-layer cardinal and input bounds are proved in this course.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

nodes = list(range(-18,19))
weights = [5 if abs(s)<=9 and s%3 else 3 if abs(s)<=9 else 1 for s in nodes]
deleted = [s for s in range(-9,10) if s%3]
counts = [sum(s%4==r for s in deleted) for r in range(4)]
assert sum(weights)==99 and counts==[4,3,2,3]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig,(ax,bx)=plt.subplots(2,1,figsize=(7.9,7.8),layout='constrained')
fig.set_facecolor('#f8fafc')
ax.bar(nodes,[1]*len(nodes),width=.73,color='#cdd9e5',edgecolor='#70849a',linewidth=.6)
ax.bar([s for s in nodes if abs(s)<=9],[2]*19,bottom=1,width=.73,color='#74aaa9',edgecolor='#396d73',linewidth=.6)
ax.bar(deleted,[2]*12,bottom=3,width=.73,color='#d18b66',edgecolor='#934620',linewidth=.6)
ax.axvline(-9.5,color='#396d73',linestyle=':',linewidth=1)
ax.axvline(9.5,color='#396d73',linestyle=':',linewidth=1)
ax.set_xlim(-19,19);ax.set_ylim(0,11)
ax.set_xticks([-18,-9,0,9,18]);ax.set_yticks([0,1,3,5])
ax.set_xlabel('Integer node s');ax.set_ylabel('Multiplicity μ(s)')
ax.set_title('All full layers plus the deleted increment',fontweight='bold',pad=14)
ax.legend(handles=[Patch(facecolor='#cdd9e5',label='Full outer layer: 37 nodes ×1'),
 Patch(facecolor='#74aaa9',label='Full inner increment: 19 nodes ×2'),
 Patch(facecolor='#d18b66',label='q-deleted increment: 12 nodes ×2')],loc='upper center',fontsize=12,framealpha=.96)
ax.text(.03,.54,'N*=37+38+24=99; M=5; B=⌊log₂36⌋=5.\nCardinal losses: −10, −20, −30 in the three node types.',
 transform=ax.transAxes,fontsize=12,bbox={'facecolor':'white','edgecolor':'#cfd8e3','boxstyle':'round,pad=.4'})
bx.bar(range(4),counts,color=['#185b78','#5895a4','#a9cbd1','#5895a4'],width=.65)
for r,n in enumerate(counts):bx.text(r,n+.1,str(n),ha='center',va='bottom',fontweight='bold')
bx.set_ylim(0,10);bx.set_yticks(range(6));bx.set_xticks(range(4))
bx.set_xlabel('Residue class modulo p²=4');bx.set_ylabel('Number of q-deleted nodes')
bx.set_title('Deleted counts can differ by two',fontweight='bold',pad=14)
bx.text(.03,.96,'p=2, q=3, A=9.\nDeleted nodes exclude\n−9, −6, −3, 0, 3, 6, 9.',
 transform=bx.transAxes,fontsize=12,va='top')
bx.text(.03,.59,'The separate EB=2×5=10 cost survives.\nThe Taylor inverse has\nits own additional loss.',
 transform=bx.transAxes,fontsize=12,bbox={'facecolor':'white','edgecolor':'#cfd8e3','boxstyle':'round,pad=.4'})
for axis in (ax,bx):axis.grid(axis='y',alpha=.13);axis.set_axisbelow(True)
fig.savefig(Path(__file__).with_name('general-mixed-profiles.png'),dpi=180,
 metadata={'Software':'GPT-6.1 Sol (OpenAI), Ultra; original CC0 figure'})
