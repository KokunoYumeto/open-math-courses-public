"""Reproduce the exact coordinate comparison in Section 6.

Both panels refer to odd n >= 3 and A_r = {k >= 2r}.
The norm is the normalized tracial 2-norm. No finite sampling
is used to infer the ultrafilter conclusion.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

DEST=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':22,
                     'svg.fonttype':'path','svg.hashsalt':'relative-coordinate-commutation-v1'})
fig,ax=plt.subplots(figsize=(8.0,6.2),layout='constrained')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
ax.text(.5,.97,r'Odd coordinate $n\geq3$',ha='center',va='top',fontsize=26,weight='bold')
ax.text(.5,.87,r'Prescribed element: $x_n=a_n$',ha='center',va='center',fontsize=25)
panels=[(.48,'#eaf6ef','#206b44','Keep coordinate n',
          r'$u_n=u_n^{(v(n))}=x_n=a_n$',r'$\|[u_n,x_n]\|_2=0$'),
        (.08,'#fff0e8','#a84618','Replace n by 2n',
          r'$\widetilde u_n=u_{2n}^{(n)}=x_{2n}=b_n$',r'$\|[\widetilde u_n,x_n]\|_2=2$')]
for y,fill,color,title,equation,norm in panels:
    ax.add_patch(FancyBboxPatch((.025,y),.95,.32,
                boxstyle='round,pad=0.015',facecolor=fill,edgecolor=color,linewidth=1.5))
    ax.text(.5,y+.267,title,ha='center',va='center',fontsize=23,color=color,weight='bold')
    ax.text(.5,y+.155,equation,ha='center',va='center',fontsize=26)
    ax.text(.5,y+.048,norm,ha='center',va='center',fontsize=25,color=color)
ax.text(.5,.013,r'$a_nb_n=-b_na_n$',ha='center',va='center',fontsize=23)
fig.savefig(DEST/'relative-coordinate-commutation.svg',metadata={
    'Date':None,'Creator':'Matplotlib','Description':'Exact Pauli-coordinate counterexample in Section 6.'})
fig.savefig(DEST/'relative-coordinate-commutation.png',dpi=190,metadata={'Software':'Matplotlib'})
plt.close(fig)
