"""Exact matrices for RA04; no numerical approximation enters the proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(9,9),dpi=100,facecolor='#fafbfc')
top=fig.add_gridspec(1,3,left=.055,right=.965,bottom=.56,top=.79,wspace=.26)
labels=[r'Canonical $\xi a$',r'Algebra $\rho_\eta\xi$',r'Corrected $\rho_{\Delta^{1/2}\eta}\xi$']
for k,value in enumerate([1,2,1]):
 ax=fig.add_subplot(top[0,k]);matrix=np.array([[0,value],[0,0]])
 ax.imshow(matrix,cmap='Blues',vmin=0,vmax=2)
 for i in range(2):
  for j in range(2):ax.text(j,i,str(matrix[i,j]),ha='center',va='center',fontsize=22,color='white' if matrix[i,j]==2 else '#123246')
 ax.set_xticks([]);ax.set_yticks([]);ax.set_title(labels[k],fontsize=13,pad=12)
 ax.set_xticks(np.arange(-.5,2,1),minor=True);ax.set_yticks(np.arange(-.5,2,1),minor=True)
 ax.grid(which='minor',color='white',linewidth=2);ax.tick_params(which='minor',length=0)
fig.text(.5,.94,'The right action includes a modular half-power',ha='center',fontsize=17)
fig.text(.5,.885,r'$h=\mathrm{diag}(1,4),\quad\xi=\alpha=\mathrm{diag}(1,2),\quad a=E_{12},\quad\eta=2E_{12}$',ha='center',fontsize=13)
fig.text(.5,.515,'The uncorrected algebra product is twice the canonical action.',ha='center',fontsize=12)
bottom=fig.add_gridspec(1,2,left=.19,right=.81,bottom=.18,top=.39,wspace=.40)
for k,values in enumerate([[4,4,0],[2,2,0]]):
 ax=fig.add_subplot(bottom[0,k]);a=np.array(values);matrix=a[None,:]-a[:,None]
 ax.imshow(np.sign(matrix),cmap='PuOr_r',vmin=-1,vmax=1)
 for i in range(3):
  for j in range(3):ax.text(j,i,str(matrix[i,j]),ha='center',va='center',fontsize=20,color='#102333' if matrix[i,j]==0 else 'white')
 ax.set_xticks(range(3),labels=[1,2,3]);ax.set_yticks(range(3),labels=[1,2,3])
 ax.set_xlabel('column j');ax.set_ylabel('row i')
 ax.set_title([r'$h_j-h_i$',r'$\sqrt{h_j}-\sqrt{h_i}$'][k],pad=12,fontsize=16)
 ax.set_xticks(np.arange(-.5,3,1),minor=True);ax.set_yticks(np.arange(-.5,3,1),minor=True)
 ax.grid(which='minor',color='white',linewidth=2);ax.tick_params(which='minor',length=0)
fig.text(.5,.485,r'Nonfaithful example: $h=\mathrm{diag}(4,4,0)$',ha='center',fontsize=15)
fig.text(.5,.068,'Both commutators vanish exactly on the same block algebra: '+r'$M_2\oplus\mathbb{C}$'+'.\n'
         'Zero coefficient: the entry is free. Nonzero coefficient: the entry must vanish.',ha='center',fontsize=11)
fig.text(.5,.018,'Exact entries and proofs: RA02–04, equations RA.5, RA.7, RA.11–12.',ha='center',fontsize=10)
fig.savefig(Path(__file__).with_name('right-action-and-centralizer.png'),dpi=100,
            metadata={'Software':'OA-MOD original figure','Title':'Right action and nonfaithful centralizer'})
plt.close(fig)
