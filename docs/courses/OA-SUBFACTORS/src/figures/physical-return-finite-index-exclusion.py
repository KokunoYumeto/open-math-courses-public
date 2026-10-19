"""Normal physical hypertraces, the actual center bound and finite-index exclusion. CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
P=Path(__file__).resolve().with_suffix('');ink='#182a3a';blue='#164b7a';green='#126856'
fig=plt.figure(figsize=(12,11),facecolor='#fafcff')
a=fig.add_axes([.04,.45,.92,.51]);a.axis('off')
a.text(.5,.97,'Finite normal hypertraces force the physical trace',ha='center',fontsize=20,weight='bold',color=ink)
rows=[('Original global finite approximation','Every shifted row has compatible hypertraces',blue),
 (r'Assume also $h\geq\varepsilon1>0$','Finite whole modules: every such hypertrace is normal',blue),
 ('Actual center transport (63.42)',r'$c_j\in Z(D_j),\quad 0\leq c_j\leq\delta^{-1}1,\quad\tau(c_j)=1$',green),
 (r'$[c_j,M_j]=0$ and the original tower generates the factor $T$',r'$c_j\longrightarrow1$ ultraweakly; compatibility descends through every cup',green),
 ('PH.20: every physical return preserves the trace',r'$K_l=1,\quad h=1,\quad U=N,\quad D_0=M$',green)]
for n,(title,detail,color) in enumerate(rows):
 y=.80-n*.165
 a.text(.5,y,title,ha='center',fontsize=14,color=color,weight='bold')
 a.text(.5,y-.052,detail,ha='center',fontsize=12,color=ink)
 if n<4:a.annotate('',xy=(.5,y-.125),xytext=(.5,y-.075),arrowprops=dict(arrowstyle='->',color='#778899'))
b=fig.add_axes([.11,.20,.78,.20],facecolor='white');x=np.arange(3)
p=np.array([1/5,3/10,1/2]);q=np.array([1/2,1/4,1/4]);density=q/p
b.bar(x,density,.5,color=green);b.axhline(5,color=blue,linestyle='--',label=r'$\delta^{-1}=5$')
b.set_xticks(x,[r'$p_1=1/5$',r'$p_2=3/10$',r'$p_3=1/2$']);b.set_ylim(0,5.6);b.set_ylabel('Central trace density');b.legend(loc='upper right')
b.set_title('Numerical center data only: density (5/2, 5/6, 1/2), trace one',fontsize=12,color=ink)
for i,t in enumerate(['5/2','5/6','1/2']):b.text(i,density[i]+.12,t,ha='center',fontsize=11)
c=fig.add_axes([.06,.015,.88,.115]);c.axis('off')
c.text(.5,.85,'PH.21: if U is a factor, the index is 1 or infinite',ha='center',fontsize=15,color=green,weight='bold')
c.text(.5,.52,'Finite proper index is excluded; state-distance limit is 0 or 2.',ha='center',fontsize=13,color=ink)
c.text(.5,.20,'The infinite-index / zero-mass branch is still unresolved at the original hypotheses.',ha='center',fontsize=12,color='#8b3d32')
for ext in ['.svg','.png']:
 fig.savefig(str(P)+ext,dpi=160,facecolor=fig.get_facecolor())
 if ext=='.svg':
  f=P.with_suffix('.svg');f.write_text('\n'.join(line.rstrip() for line in f.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
