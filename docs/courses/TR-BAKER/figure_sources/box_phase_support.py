"""Figure10.13: exact closed box, saturated lattice and phase classes. CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle

fig,axes=plt.subplots(1,2,figsize=(14,7.8))
fig.subplots_adjust(top=.83,bottom=.22,left=.07,right=.97,wspace=.22)
fig.suptitle('A closed box supplies enough points in one phase class',fontsize=18,weight='bold',y=.96)
fig.text(.5,.895,r'Basis columns: $(1,0),\ (1/2,1/2)$     $\Delta=1/2,\quad V=2,\quad V/\Delta=4$',ha='center',fontsize=15)
points=[((0,0),(0,0)),((.5,.5),(0,1)),((1,0),(1,0)),((1.5,.5),(1,1)),((2,0),(2,0))]
colours={0:'#dc2626',2:'#2563eb'}
left,right=axes
left.add_patch(Rectangle((0,0),2,1,facecolor='#fef3c7',edgecolor='#d97706',lw=2,label='Closed box'))
left.add_patch(Polygon([(0,0),(1,0),(1.5,.5),(.5,.5)],facecolor='#cbd5e1',edgecolor='#64748b',alpha=.35,label='Fundamental cell: area 1/2'))
for (x,y),(a,b) in points:
 phase=2*(a+b)%4;color=colours[phase]
 left.scatter(x,y,s=100,c=color,zorder=5,edgecolor='white',lw=1.2)
 right.scatter(a,b,s=110,c=color,zorder=5,edgecolor='white',lw=1.2)
 offset=(8,13) if x!=2 else (-45,-24)
 left.annotate(f'λ=({a}, {b})',(x,y),xytext=offset,textcoords='offset points',fontsize=11,color='#0f172a')
 right.annotate(f'phase {phase}',(a,b),xytext=(0,13),textcoords='offset points',ha='center',fontsize=11,color=color)
left.set(xlim=(-.25,2.3),ylim=(-.25,1.25),xlabel=r'Original coordinate $\mu_1$',ylabel=r'Original coordinate $\mu_2$',title='Five points in the same lattice coset')
right.set(xlim=(-.35,2.35),ylim=(-.3,1.4),xlabel=r'Integral basis coordinate $\lambda_1$',ylabel=r'Integral basis coordinate $\lambda_2$',title='Two phases; the zero class keeps three points')
for ax in axes:ax.set_aspect('equal');ax.grid(alpha=.18)
left.legend(loc='upper left',fontsize=10,frameon=False);right.set_xticks([0,1,2]);right.set_yticks([0,1])
fig.text(.5,.15,r'$G_0=4,\quad d=(2,2),\quad g=2,\quad H=2:\qquad|\Lambda|\geq\lceil5/2\rceil=3$',ha='center',fontsize=15)
fig.text(.5,.095,r'$k=2,\ L=1,\ S=1,\ T=0:\qquad N=6,\quad M_*=3$',ha='center',fontsize=15)
fig.text(.5,.04,'Theorem10.66, Lemma10.67, Corollary10.68; equations(10.177)–(10.182); Solution33. Exact points and phases.',ha='center',fontsize=11,color='#475569')
fig.savefig(Path(__file__).with_name('box-phase-support.png'),dpi=150,facecolor='white')
plt.close(fig)
