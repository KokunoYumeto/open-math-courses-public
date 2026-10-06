"""Exact frame maps for the fixed-domain family, equations M34--M38."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,4.8));ax.set(xlim=(0,12),ylim=(0,5));ax.axis('off')
def txt(x,y,s,sz=15):ax.text(x,y,s,ha='center',va='center',fontsize=sz)
def arrow(a,b,label,xy):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.8,color='#245078'))
    txt(*xy,label,14)
txt(3.3,4.65,'Exact maps on the original overlap',17)
txt(1.4,3.7,r'$\mathbb{C}^{N}$')
txt(5.4,3.7,r'$\mathbb{C}^{N}_{U,(x,z)}$')
txt(5.4,1.6,r'$\mathbb{C}^{N}_{V,(x,z)}$')
arrow((2.05,3.7),(4.4,3.7),r'$F_U(x,z)$',(3.2,4.04))
arrow((5.4,3.35),(5.4,1.98),r'$a(x,z)$',(6.05,2.65))
arrow((1.72,3.38),(4.47,1.79),r'$F_V(x,z)$',(2.75,2.24))
txt(3.65,.67,r'$F_V(x,z)=a(x,z)F_U(x,z)$',16)
ax.plot([7.15,7.15],[.4,4.3],color='#b3c3d3',lw=1)
txt(9.65,4.65,'Same domains for every parameter',17)
txt(9.65,3.72,r'$z\in Z,\quad x\in U\setminus K$')
txt(9.65,2.9,r'$A_0(x,z)=F_U(x,z)$')
txt(9.65,2.12,r'$A_\infty(x,z)=F_V(h(x),z)$')
txt(9.65,1.34,r'$h|_U=\mathrm{id},\quad h(x)=2Rx/|x|$')
txt(9.65,.86,r'for $|x|\geq 2R$; the radius $R$ is fixed',12)
fig.text(.5,.012,'M34–M38: the radial transport proves smooth dependence and every exterior derivative bound.\n',ha='center',fontsize=10)
fig.subplots_adjust(left=.015,right=.99,top=.96,bottom=.15)
fig.savefig(p/'matrix-extension-parameters.svg')
fig.savefig(p/'matrix-extension-parameters.png',dpi=170)
plt.close(fig)
