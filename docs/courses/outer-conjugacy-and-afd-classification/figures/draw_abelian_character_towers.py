"""Exact C5 x C3 finite tower illustration of the relative spectral-row proof.
The finite permutation model illustrates internal covariance and seam error;
it is not asserted to be a faithful action of the infinite quotient.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
dest=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':19,'svg.fonttype':'path','svg.hashsalt':'abelian-character-towers-v1'})
fig,ax=plt.subplots(figsize=(8,10),layout='constrained');ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.975,'Character coefficients on a tower',ha='center',va='top',fontsize=24,weight='bold')
ax.text(.5,.915,r'$\chi(m,a)=i^m\zeta^a,\quad\zeta=e^{2\pi i/3}$',ha='center',fontsize=23)
ax.text(.5,.865,r'$W=\sum_{m,a}i^{-m}\zeta^{-a}E_{m,a}$',ha='center',fontsize=23)
for a in range(3):ax.text(.33+a*.255,.785,f'a = {a}',ha='center',fontsize=20)
phases=['-1','i','1','-i','-1']
for j,m in enumerate(range(-2,3)):
 y=.69-j*.085;ax.text(.08,y+.033,f'm = {m}',ha='center',va='center',fontsize=18)
 for a in range(3):
  x=.215+a*.255;fill='#f9e7da' if j in [0,4] else '#e8f2ec'
  ax.add_patch(Rectangle((x,y),.225,.067,facecolor=fill,edgecolor='#58606a',linewidth=1))
  suffix=['',r'\zeta^{-1}',r'\zeta^{-2}'][a]
  coeff=phases[j];label=(coeff+suffix) if coeff!='1' or not suffix else suffix
  ax.text(x+.1125,y+.033,'$'+label+'$',ha='center',va='center',fontsize=20)
ax.text(.5,.28,r'Internal shift: $\gamma(E_{m,a})=E_{m+1,a}$',ha='center',fontsize=21)
ax.text(.5,.225,r'$i^{-m}\zeta^{-a}=i\,i^{-(m+1)}\zeta^{-a}$',ha='center',fontsize=23)
ax.text(.5,.164,r'Wrap at $m=-2$: $-\zeta^{-a}$ versus $-i\zeta^{-a}$',ha='center',fontsize=19)
ax.text(.5,.11,r'$\|\gamma(W)-iW\|_2=\sqrt{2/5}\leq2/\sqrt{5}$',ha='center',fontsize=22)
ax.text(.5,.047,'15 orthogonal levels, each with trace 1/15\nSource and target boundary masses: 1/5 each',ha='center',va='center',fontsize=18)
fig.savefig(dest/'abelian-character-towers.svg',metadata={'Date':None,'Creator':'Matplotlib','Description':'Exact finite character coefficients, oriented boundary masses and seam norm.'})
fig.savefig(dest/'abelian-character-towers.png',dpi=170,metadata={'Software':'Matplotlib'});plt.close(fig)
