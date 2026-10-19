"""Exact jump and inverse matrices for AN01-U110 (S22)-(S23); CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':14,'font.family':'DejaVu Sans','svg.hashsalt':'AN01-U110'})
forward=np.array([[1,0,0],[0,1,0],[3,1,1]])
inverse=np.array([[1,0,0],[0,1,0],[-3,-1,1]])
assert np.array_equal(forward@inverse,np.eye(3,dtype=int))
fig,axes=plt.subplots(1,2,figsize=(11.5,5.8),layout='constrained')
for ax,M,rows,cols,title in [
 (axes[0],forward,[r'$w_2$',r'$w_1$',r'$w_0$'],[r'$g_0$',r'$g_1$',r'$g_2$'],'Normal jets → boundary source'),
 (axes[1],inverse,[r'$g_0$',r'$g_1$',r'$g_2$'],[r'$w_2$',r'$w_1$',r'$w_0$'],'Boundary source → normal jets')]:
 ax.imshow(M,cmap='RdBu_r',norm=TwoSlopeNorm(vmin=-3,vcenter=0,vmax=3))
 ax.set_xticks(range(3),cols);ax.set_yticks(range(3),rows)
 ax.set_xlabel('Input coefficients');ax.set_ylabel('Output coefficients')
 ax.set_title(title,pad=14)
 for i in range(3):
  for j in range(3):
   ax.text(j,i,str(M[i,j]),ha='center',va='center',fontsize=27,weight='bold' if M[i,j] else 'normal',color='white' if abs(M[i,j])==3 else '#172334')
 ax.set_xticks(np.arange(-.5,3,1),minor=True);ax.set_yticks(np.arange(-.5,3,1),minor=True)
 ax.grid(which='minor',color='#64748b',linewidth=1);ax.tick_params(which='minor',bottom=False,left=False)
fig.suptitle(r'$P=(1+t+t^2)\partial_t^3+(2+3t)\partial_t^2+4\partial_t$'+'\n'+r'$P(E_+u)=w_2\delta^{\prime\prime}+w_1\delta^\prime+w_0\delta$',fontsize=17)
fig.savefig(out/'canonical-cauchy-jump-matrix.png',dpi=160,bbox_inches='tight')
fig.savefig(out/'canonical-cauchy-jump-matrix.svg',metadata={'Date':None},bbox_inches='tight')
p=out/'canonical-cauchy-jump-matrix.svg'
p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
