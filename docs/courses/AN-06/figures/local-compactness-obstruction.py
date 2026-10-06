"""Exact local compactness proof diagram. Original CC0; Matplotlib required."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'local-compactness-obstruction'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(11.5,6.3),layout='constrained');ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(x,y,s,color='#e5f1f7'):
 ax.text(x,y,s,ha='center',va='center',fontsize=13,bbox={'boxstyle':'round,pad=.65','facecolor':color,'edgecolor':'#216184'})
def arrow(start,end):ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':'#216184','lw':1.8})
ax.text(.5,.96,r'Local compactness with $0\ne w\in\Lambda(p)$',ha='center',fontsize=18)
box(.25,.77,r'$M_t\phi=e^{itw\cdot x}\phi$'+'\n'+r'$\|M_t\phi\|_{X_p}=\|\phi\|_{X_p}$'+'\n'+'Every graph component and support is retained')
box(.75,.77,r'$VM_t\phi=M_t\sum_{k=0}^{m}t^k c_k$'+'\n'+'Precompact output is bounded in '+r'$L^2$')
arrow((.43,.77),(.57,.77))
box(.75,.44,'Bounded vector polynomial'+ '\n'+r'$c_m=\cdots=c_1=0$'+'\n'+r'$M_t c_0\rightharpoonup0$, $\|M_tc_0\|_2=\|c_0\|_2$')
arrow((.75,.66),(.75,.56))
box(.25,.44,'Compactness forces '+r'$c_0=V\phi=0$'+'\n'+'Every compact smooth test'+ '\n'+'forces every local coefficient to vanish')
arrow((.57,.44),(.43,.44))
box(.5,.14,r'Nonlocal compact maps survive: $Ku=b(u,a)$'+'\n'+r'$Ka=\|a\|_2^2b$, with disjoint supports of $a,b$'+'\n'+'One-dimensional range; the output can leave the input support',color='#fbecde')
fig.savefig(out/'local-compactness-obstruction.svg',metadata={'Date':None,'Creator':'Original CC0 mathematical figure'})
fig.savefig(out/'local-compactness-obstruction.png',dpi=180,metadata={'Software':'Original CC0 mathematical figure'})
plt.close(fig)
