"""Exact spectral rows for Exercise 1 of Shrinking oscillators ...

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026.
Public domain (CC0). Self-checked; no independent review.
Proof locators: Lemma 4.1, Proposition 5.1, Theorem 1.1.
References: Sjostrand (1974), quadratic spectra; Hormander, The Analysis
of Linear Partial Differential Operators III, uniform quadratic criteria.
Run with Python and matplotlib; the PNG is saved beside this source.
"""
from fractions import Fraction
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(11,6.5),dpi=150)
fig.patch.set_facecolor('#fafaf7');ax.set_facecolor('#fafaf7')
labels=['Limit cost ray']
for N,row in [(31,1),(7,2),(1,3)]:
 a=Fraction(1,2*N+2)
 values=[a*(2*j+1)-1 for j in range(2*N+2)]
 assert all(-1<v<1 and v!=0 for v in values)
 assert min(abs(v) for v in values)==a
 ax.scatter([float(v) for v in values],[row]*len(values),s=30,color='#136c82',zorder=3)
 ax.scatter([-float(a),float(a)],[row,row],s=90,facecolors='none',edgecolors='#b85d22',lw=2,zorder=4)
 labels.append(f'N = {N}, a = 1/{2*N+2}')
ax.annotate('',(1.04,0),(-1,0),arrowprops={'arrowstyle':'->','color':'#65538e','lw':3})
ax.scatter([-1],[0],s=50,color='#65538e',zorder=3)
ax.axvline(0,color='#b85d22',lw=1.2,ls='--',alpha=.7)
ax.annotate(r'Nearest values: $\pm a_N$',(.26,2.55),color='#b85d22',fontsize=14)
ax.annotate(r'$-1+[0,\infty)$',(-.78,.2),color='#65538e',fontsize=15)
ax.set_yticks([0,1,2,3],labels)
ax.set(xlim=(-1.09,1.09),ylim=(-.4,3.5),xlabel=r'Real eigenvalue of $Q_N^w-1$')
ax.grid(axis='x',alpha=.15)
ax.set_title('Every displayed oscillator is invertible; the lower constants diverge',fontsize=17,pad=18)
fig.text(.5,.045,'Rows separate parameter values; they are not imaginary coordinates. Higher spectral levels are omitted.',ha='center',fontsize=11.5)
fig.subplots_adjust(left=.21,right=.97,bottom=.18,top=.88)
fig.savefig(Path(__file__).with_name('shrinking-oscillator-levels.png'),metadata={'Software':'Matplotlib; original CC0 mathematical figure'})
plt.close(fig)
