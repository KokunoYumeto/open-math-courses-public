"""Original exact phase-kernel diagram, GPT-6.1 Sol (OpenAI), Ultra. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':19,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(16,7.6),facecolor='white')
fig.text(.5,.96,'Phased bases outside the rational field; kernel rows inside it',ha='center',fontsize=24,weight='bold')
fig.text(.5,.88,r'$\gamma_1=2^P\zeta^{-P},\quad\gamma_2=3^P\zeta^{-3P},\quad P=125,\quad\zeta^2=-1,\quad b=6^P$',ha='center',fontsize=23)
left=fig.add_axes([.045,.32,.23,.44])
left.plot(range(4),range(4),color='#bfdbfe',lw=3,zorder=1)
left.scatter(range(4),range(4),s=120,color='#1d4ed8',zorder=2)
left.set(xlim=(-.4,3.4),ylim=(-.4,3.4),xticks=range(4),yticks=range(4))
left.set_aspect('equal');left.grid(alpha=.22)
left.set_xlabel(r'$\lambda_1$');left.set_ylabel(r'$\lambda_2$')
left.set_title(r'$\Lambda=\{(j,j):0\leq j\leq3\}$',fontsize=20,pad=18)
fig.text(.17,.165,r'$\gamma^{s(j,j)}=b^{sj}\in\mathbb{Q}$',ha='center',fontsize=22)

matrix=fig.add_axes([.39,.31,.35,.43]);matrix.set(xlim=(0,4),ylim=(-.5,3.5));matrix.axis('off')
matrix.set_title(r'$M_{s,j}=(s+1)b^{sj}$',fontsize=23,pad=35)
rows=[['0']*4,['1']*4,['2','2b','2b^2','2b^3']]
for j in range(4):
    matrix.text(j+.5,3.3,f'$j={j}$',ha='center',va='center',fontsize=18,color='#475569')
for a,(label,row) in enumerate(zip(['s=-1','s=0','s=1'],rows)):
    y=2.5-a
    matrix.text(-.18,y,'$'+label+'$',ha='right',va='center',fontsize=19)
    for j,entry in enumerate(row):
        matrix.text(j+.5,y,'$'+entry+'$',ha='center',va='center',fontsize=24,color='#64748b' if a==0 else '#1d4ed8')
matrix.plot([.1,0,0,.1],[3.0,3.0,0,0],color='#334155',lw=2)
matrix.plot([3.9,4,4,3.9],[3.0,3.0,0,0],color='#334155',lw=2)
fig.text(.55,.21,r'$N=4,\quad M_*=3,\quad \Delta(-1;1)=0$',ha='center',fontsize=22)

vector=fig.add_axes([.83,.29,.115,.47]);vector.set(xlim=(0,1),ylim=(0,4));vector.axis('off')
vector.set_title(r'$c$',fontsize=24,pad=12)
for j,entry in enumerate(['-b','C','-C','b']):
    vector.text(.5,3.5-j,'$'+entry+'$',ha='center',va='center',fontsize=25,color='#b45309')
vector.plot([.13,.05,.05,.13],[4,4,0,0],color='#334155',lw=2)
vector.plot([.87,.95,.95,.87],[4,4,0,0],color='#334155',lw=2)
fig.text(.885,.2,r'$C=b^2+b+1$',ha='center',fontsize=22)
fig.text(.79,.49,r'$\longrightarrow$',ha='center',fontsize=25)
fig.text(.5,.10,r'$Mc=0,\qquad A(Y)=b(Y-b^{-1})(Y-1)(Y-b)$',ha='center',fontsize=24)
fig.text(.5,.045,'Theorem 10.55 and equations (10.150)–(10.153); exact support, nodes and kernel.',ha='center',fontsize=19,color='#475569')
folder=Path(__file__).resolve().parent
destination=folder.parent/'figures/phase-kernel-matrix.png' if folder.name=='figure_sources' else folder/'phase-kernel-matrix.png'
destination.parent.mkdir(exist_ok=True)
fig.savefig(destination,dpi=180,bbox_inches='tight')
print(destination)
