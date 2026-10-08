from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 10), dpi=160)
fig.patch.set_facecolor('#faf9f4')
ax.set(xlim=(0,15), ylim=(0,10)); ax.axis('off')

def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',
                               facecolor=color,edgecolor='#254a45',lw=1.2))
    ax.text(x+.17,y+h-.22,title,va='top',fontsize=13.5,fontweight='bold',color='#203e3b')
    ax.text(x+.17,y+h-.68,'\n'.join(lines),va='top',fontsize=12.2,linespacing=1.5,color='#203e3b')

def arrow(a,b):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.8,color='#254a45'))

ax.text(.3,9.72,'The induction closes at each support dimension',fontsize=22,
        fontweight='bold',color='#203e3b',va='top')
ax.text(.3,9.20,'All smooth ambient dimensions, singular supports and bounded complexes',
        fontsize=14,color='#203e3b',va='top')
box(.35,6.78,6.3,1.72,'Exact SNC dual and curve tests',
    [r'$\theta_i^t=-\theta_i-1$; dual residue $=-A_i^t$  (5.15e)',
     r'Positive degree: $b_iI+A_i^t$ contracts  (5.15i)',
     r'Degree zero: full residue Koszul complex  (5.15g)'], '#e6e4f1')
box(7.30,6.78,7.32,1.72,'Lower support supplies both standard tests',
    [r'$C_{n-1},P_{n-1}$ act on $R\Gamma_W$; $\dim W<n$.',
     r'$j_!E$ and $j_*E$ are curve-tested  (5.17c)–(5.17h)',
     r'No same-dimensional converse is used here.'], '#e1ede8')
arrow((6.84,7.60),(7.09,7.60))
box(.35,3.95,14.27,1.93,'Forward assertion $R_n$: the canonical map retains the lower-support cone',
    [r'$j_!E\longrightarrow j_*E$, image $S=j_{!*}E$  (5.17e), (5.17i)',
     r'Kernel and cokernel have support dimension $<n$: $C_{n-1}$ makes them regular.',
     r'The tested kernel and $j_!E$ make every regular simple $S$ curve-tested  (5.17j).'], '#e7edf7')
arrow((10.96,6.58),(10.96,6.08))
box(.35,.82,6.7,2.00,'Converse $C_n$: finite socle peeling',
    [r'Lowest cohomology: every simple subobject is regular.',
     r'Remove $S[-a]$; total cohomology length drops by $1$.',
     r'$R_n$ makes removed object tested  (5.16a)–(5.16f).'], '#f2ecd8')
box(7.72,.82,6.90,2.00,'Direct image $P_n$: localization triangle',
    [r'$R\Gamma_BS\longrightarrow S\longrightarrow j_*E$  (5.17k)',
     r'Boundary support: $C_{n-1},P_{n-1}$.',
     r'Connection term: SNC graph, Gauss–Manin, $C_n$.'], '#e1ede8')
arrow((3.7,3.75),(3.7,3.02))
arrow((7.25,1.80),(7.51,1.80))
ax.text(.35,.32,r'$R_{n-1},C_{n-1},P_{n-1}\quad\Rightarrow\quad R_n\quad\Rightarrow\quad C_n\quad\Rightarrow\quad P_n$  (5.17a)',
        fontsize=17,color='#344f81')
fig.savefig(out/'full-regularity-induction.png',bbox_inches='tight',facecolor=fig.get_facecolor())
fig.savefig(out/'full-regularity-induction.svg',bbox_inches='tight',facecolor=fig.get_facecolor())
