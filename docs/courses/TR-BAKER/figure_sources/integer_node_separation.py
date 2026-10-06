"""Figure 10.5: exact integer-node residue partitions. Original CC0 source.

GPT-6.1 Sol (OpenAI), Ultra. Context: free Yu1990 and Yu2013 articles
linked in TR-BAKER-10; the complete argument is equations10.99-10.103.
Run with Python and Matplotlib; output is adjacent to this program.
Line lengths represent a residue partition, not p-adic distances.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def valuation(n,p=3):
    if n==0:return float('inf')
    n=abs(n);v=0
    while n%p==0:n//=p;v+=1
    return v

nodes=list(range(-3,4))
matrix=np.array([[valuation(s-t) for t in nodes] for s in nodes])
assert sum(matrix[3,j] for j in range(7) if j!=3)==2
assert all(matrix[i,j]==(1 if nodes[i]%3==nodes[j]%3 else 0)
           for i in range(7) for j in range(7) if i!=j)
plt.rcParams.update({'font.size':18,'font.family':'DejaVu Sans'})
fig,(left,right)=plt.subplots(1,2,figsize=(13.6,6.2),gridspec_kw={'width_ratios':[1.08,1]})
colors=['#14648d','#558236','#a7541e']
left.set_xlim(-3.3,2.9);left.set_ylim(-.7,3.15);left.axis('off')
left.set_title('Residue classes of the seven nodes',pad=20,fontweight='bold')
left.text(-.2,2.65,r'$E=\{-3,-2,-1,0,1,2,3\}$',ha='center',va='center',
          bbox={'boxstyle':'round,pad=0.4','fc':'#f4f7fa','ec':'#617382'})
groups=[(-1.95,[-3,0,3],[-2.6,-1.95,-1.3]),(0,[-2,1],[-.35,.35]),(1.75,[-1,2],[1.4,2.1])]
for residue,((center,group,xs),color) in enumerate(zip(groups,colors)):
    left.plot([-.2,center],[2.45,1.8],color=color,lw=1.6,zorder=0)
    left.text(center,1.65,f'{residue} mod 3',ha='center',va='center',color=color,
              bbox={'boxstyle':'round,pad=.35','fc':'white','ec':color})
    for node,x in zip(group,xs):
        left.plot([center,x],[1.48,.6],color=color,lw=1.6,zorder=0)
        left.text(x,.38,str(node),ha='center',va='center',fontsize=20,
                  bbox={'boxstyle':'circle,pad=.28','fc':'white','ec':color,'lw':1.8})
        left.text(x,-.01,str(node%9),ha='center',va='center',color=color)
left.text(-.2,-.34,'Bottom labels: residues modulo 9',ha='center',fontsize=17)
left.text(-.2,-.61,'Branch lengths are schematic.',ha='center',fontsize=17,color='#485663')
display=np.where(np.isinf(matrix),2,matrix)
right.imshow(display,cmap=ListedColormap(['#f4f7fa','#c5e0ef','#f8e6ad']),vmin=0,vmax=2)
right.set_title(r'Exact valuations $v_3(s-t)$',pad=20,fontweight='bold')
right.set_xticks(range(7),nodes);right.set_yticks(range(7),nodes)
right.set_xlabel(r'node $t$');right.set_ylabel(r'node $s$')
right.set_xticks(np.arange(-.5,7,1),minor=True);right.set_yticks(np.arange(-.5,7,1),minor=True)
right.grid(which='minor',color='white',lw=2);right.tick_params(which='minor',bottom=False,left=False)
for i in range(7):
    for j in range(7):right.text(j,i,r'$\infty$' if i==j else str(int(matrix[i,j])),ha='center',va='center',fontsize=20)
for spine in right.spines.values():spine.set_visible(False)
fig.text(.75,.045,r'$B=\lfloor\log_3 6\rfloor=1$'+'\n'+r'Row $s=0$: off-diagonal sum $2$',ha='center',va='center',fontsize=17)
fig.subplots_adjust(left=.02,right=.975,top=.85,bottom=.2,wspace=.19)
out=Path(__file__).with_name('integer-node-separation.png')
fig.savefig(out,dpi=180,facecolor='white')
print(out.name)
