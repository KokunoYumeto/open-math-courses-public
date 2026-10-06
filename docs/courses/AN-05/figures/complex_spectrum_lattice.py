"""Exact finite subset of the spectral list in Exercise 2.

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026.
Public domain (CC0). Self-checked; no independent review.
Theorem 1.1, Sections 4–5 of The spectrum of a complex quadratic polynomial.
Reference: Sjostrand, Parametrices ... (1974), Section 3.
Run with Python and matplotlib; the PNG is saved beside this source.
"""
from fractions import Fraction as F
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13})
fig,ax=plt.subplots(figsize=(11,6.7),dpi=150)
fig.patch.set_facecolor('#fafaf7');ax.set_facecolor('#fafaf7')
colors=['#136c82','#a24e25','#66518e','#3d7556']
def point(a,b):
 return float(F(3,2)+2*a+3*b),float(F(7,12)+a-F(1,2)*b)
for a in range(4):
 for b in range(4):
  x,y=point(a,b)
  if a<3:ax.plot([x,point(a+1,b)[0]],[y,point(a+1,b)[1]],color='#b3c3cb',lw=1,zorder=1)
  if b<3:ax.plot([x,point(a,b+1)[0]],[y,point(a,b+1)[1]],color='#c9bfae',lw=1,zorder=1)
  ax.scatter([x],[y],s=70,color=colors[b],zorder=3)
  ax.annotate(f'({a}, {b})',(x,y),xytext=(6,7),textcoords='offset points',fontsize=12)
x,y=point(0,0)
for end,color in [(point(1,0),'#136c82'),(point(0,1),'#a24e25')]:
 ax.annotate('',end,(x,y),arrowprops={'arrowstyle':'->','lw':2.4,'color':color},zorder=4)
ax.annotate(r'$2+i$',(2.3,1.15),color='#136c82',fontsize=16)
ax.annotate(r'$3-i/2$',(2.5,-0.3),color='#a24e25',fontsize=16)
ax.annotate(r'Ground: $3/2+7i/12$',(x,y),xytext=(1,-1.65),textcoords='data',
 arrowprops={'arrowstyle':'-','color':'#364d59'},fontsize=13)
ax.set(xlim=(0,18),ylim=(-2,4.7),xlabel='Real part of the eigenvalue',ylabel='Imaginary part of the eigenvalue')
ax.set_aspect('equal',adjustable='box');ax.grid(alpha=.18)
ax.set_title('Two oscillator occupations give a discrete complex lattice',fontsize=18,pad=18)
fig.text(.5,.045,r'Labels: $(\alpha_1,\alpha_2)$, each from 0 to 3. Segments show increments; further points are omitted.',ha='center',fontsize=12)
fig.subplots_adjust(left=.1,right=.96,bottom=.16,top=.88)
fig.savefig(Path(__file__).with_name('complex-spectrum-lattice.png'),metadata={'Software':'Matplotlib; original CC0 mathematical figure'})
plt.close(fig)
