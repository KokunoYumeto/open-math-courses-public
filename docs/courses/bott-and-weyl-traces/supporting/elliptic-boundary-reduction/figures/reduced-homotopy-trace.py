"""Exact cycle homotopy, actual boundary range and Hilbert quotient."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,5));ax.set(xlim=(0,12),ylim=(0,5));ax.axis('off')
def txt(x,y,s,size=16):ax.text(x,y,s,ha='center',va='center',fontsize=size)
txt(6,4.68,'A cycle difference vanishes in reduced cohomology',20)
txt(1.1,3.6,r'$Z_j$',22);txt(4.5,3.6,r'$\mathrm{ran}\,d_{j-1}$',19);txt(8.1,3.6,r'$B_j$',22);txt(10.7,3.6,r'$Z_j$',22)
for x,y in [(1.7,3.3),(5.85,7.5),(8.65,10.1)]:
 ax.annotate('',xy=(y,3.6),xytext=(x,3.6),arrowprops=dict(arrowstyle='->',lw=1.7,color='#245078'))
txt(2.5,4.08,r'$d_{j-1}h_j$',17);txt(6.65,4.08,'closure inclusion',12);txt(9.38,4.08,'inclusion',12)
txt(6,2.68,r'$(R_j-Q_j)x=d_{j-1}h_jx,\quad B_j=\overline{\mathrm{ran}\,d_{j-1}}$',17)
txt(6,1.89,r'$q_j:Z_j\to Z_j/B_j,\quad q_j(R_j-Q_j)|_{Z_j}=0$',18)
txt(6,1.09,r'$\sum_{j=0}^m(-1)^j\mathrm{Tr}_{H_j}R_j=\sum_{j=0}^m(-1)^j\mathrm{Tr}_{H_j}Q_j$',18)
txt(6,.5,'Closed unbounded case: every cycle satisfies the exact h and differential domains.',12)
fig.text(.5,.015,'T46–T49 and the complete reduced-supertrace proof T23–T26 supply all maps, domain bounds and traces.\nNo individual homotopy product trace is taken.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.14)
fig.savefig(p/'reduced-homotopy-trace.svg');fig.savefig(p/'reduced-homotopy-trace.png',dpi=165);plt.close(fig)
