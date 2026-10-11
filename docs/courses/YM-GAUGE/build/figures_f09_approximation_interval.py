"""Reproduce the exact approximation and continuation maps; CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
D=Path(__file__).resolve().parent.parent/'figures'
plt.rcParams.update({'svg.hashsalt':'YM-F09-GA-RC','font.family':'DejaVu Sans','font.size':12})
def box(ax,y,title,body):
    ax.add_patch(FancyBboxPatch((.08,y),.84,.135,boxstyle='round,pad=0.012',facecolor='#eef5fa',edgecolor='#28516b',linewidth=1.5))
    ax.text(.5,y+.105,title,ha='center',va='center',fontweight='bold',fontsize=14,color='#17384d')
    ax.text(.5,y+.047,body,ha='center',va='center',fontsize=13)
def arrow(ax,y,label):
    ax.add_patch(FancyArrowPatch((.5,y),(.5,y-.064),arrowstyle='-|>',mutation_scale=17,color='#28516b',linewidth=1.7))
    ax.text(.525,y-.032,label,va='center',fontsize=11)
def save(fig,stem):
    fig.savefig(D/(stem+'.svg'),metadata={'Date':None},bbox_inches='tight')
    fig.savefig(D/(stem+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)
def build():
    D.mkdir(exist_ok=True)
    fig,ax=plt.subplots(figsize=(11.5,8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.985,'Approximate the data while keeping Gauss law exact',ha='center',va='top',fontsize=18,fontweight='bold')
    box(ax,.785,'Original constrained data',r'$A\in L^6,\ \partial A\in L^2,\ E\in L^2,\quad D_A^iE_i=0$')
    arrow(ax,.77,'Cut off at the chosen radius')
    box(ax,.565,'Compact preliminary data',r'$B_n=\chi_{2r_n}A,\qquad g_n=\chi_{2r_n}E$')
    arrow(ax,.55,'Mollify at the chosen scale')
    box(ax,.345,'Smooth preliminary data',r'$A_n=\rho_{\epsilon_n}*B_n,\qquad f_n=\rho_{\epsilon_n}*g_n$')
    arrow(ax,.33,'Solve the covariant elliptic correction')
    box(ax,.125,'Smooth data with the exact constraint',r'$E_n=P_{A_n}f_n=f_n+D_{A_n}\phi_n,\qquad D_{A_n}^iE_{n,i}=0$')
    ax.text(.5,.06,r'$d_c((A_n,E_n),(A,E))\leq8\delta_n,\quad\delta_n=2^{-n}\ell^{-1/2}$',ha='center',fontsize=14)
    ax.text(.5,.005,r'If $F(A)\in L^2$: curvature error $\leq2\delta_n$ and graph-metric error $\leq10\delta_n$.',ha='center',fontsize=12)
    ax.text(.5,-.04,'GA.44–GA.55. The two cutoff/mollifier scales are selected by their actual error bounds.',ha='center',fontsize=11,color='#354b59')
    save(fig,'f09-constrained-approximation')
    fig,ax=plt.subplots(figsize=(11.5,8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.985,'Reach the common physical endpoint and restart',ha='center',va='top',fontsize=18,fontweight='bold')
    box(ax,.785,'Translation stability on every existing segment',r'$\sup_J\|\partial^{(2)}A^0\|_2\leq M_2\qquad$ (RC.21)')
    arrow(ax,.77,'Use the actual physical multiplier')
    box(ax,.565,'Finite bounds in the unchanged affine chart',r'$V=(A^0-A_*,E^0,B^0),\qquad\sup_J\|V\|_{X_q}\leq M_{X_q}$')
    arrow(ax,.55,'Integrate the nonlinear forcing')
    box(ax,.345,'Strong endpoint in every finite derivative order',r'$Z(t)=\mathcal{U}(t_*-t)V(t)\ \longrightarrow\ Z_T,\qquad V(t)\longrightarrow V_T$')
    arrow(ax,.33,'Apply the original local iteration')
    box(ax,.125,'A positive restart interval through the endpoint',r'$\delta_T=[4(a_2^*+2C_2R_T)]^{-1}>0,\qquad A_T=A_*+h_T$')
    ax.text(.5,.06,'The same frozen potential, physical constants and original gauge anchors are retained.',ha='center',fontsize=12)
    ax.text(.5,.005,r'RC.21–RC.29. The paired estimate uses total length $|J|\leq\tau$.',ha='center',fontsize=12)
    ax.text(.5,-.04,'Each arrow is proved for the original regular solution; the strong endpoint supplies the restart data.',ha='center',fontsize=11,color='#354b59')
    save(fig,'f09-common-regular-interval')
if __name__=='__main__':build()
