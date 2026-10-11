"""Reproducible diagrams of the actual CR and CP maps; CC0 1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
D=Path(__file__).resolve().parent.parent/'figures'
plt.rcParams.update({'svg.hashsalt':'YM-F09-CR-CP','font.family':'DejaVu Sans','font.size':12})
def panel(ax,xy,w,h,title,body):
    x,y=xy
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.016',facecolor='#eef5fa',edgecolor='#28516b',linewidth=1.5))
    ax.text(x+w/2,y+h-0.055,title,ha='center',va='top',fontweight='bold',fontsize=14,color='#17384d')
    ax.text(x+w/2,y+h/2-0.035,body,ha='center',va='center',linespacing=1.65)
def arrow(ax,a,b,label):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color='#28516b',linewidth=1.8))
    ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+0.036,label,ha='center',fontsize=12)
def save(fig,stem):
    fig.savefig(D/(stem+'.svg'),metadata={'Date':None},bbox_inches='tight')
    fig.savefig(D/(stem+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)
def build():
    D.mkdir(exist_ok=True)
    fig,ax=plt.subplots(figsize=(12,6));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.98,'The original gauge is reconstructed in two steps',ha='center',va='top',fontsize=18,fontweight='bold')
    panel(ax,(.02,.49),.25,.29,'Heat boundary',r'$a(0),\ E(0)$'+'\n'+r'$a_s=0,\ a_t(S)=0$')
    panel(ax,(.375,.49),.25,.29,'Temporal gauge',r'$A^{\mathrm{phys}}=U\cdot a(0)$'+'\n'+r'$E^{\mathrm{phys}}=\mathrm{Ad}(U)E(0)$')
    panel(ax,(.73,.49),.25,.29,'Original fields',r'$A^0=Q_0\cdot A^{\mathrm{phys}}$'+'\n'+r'$E^0=\mathrm{Ad}(Q_0)E^{\mathrm{phys}}$')
    arrow(ax,(.28,.64),(.36,.64),r'$U_t=Ub$')
    arrow(ax,(.64,.64),(.715,.64),r'$Q_0$')
    ax.text(.5,.405,r'$U(t_*)=I,\quad b=a_t(0),\quad Q_0=V_0(t_*,S)$',ha='center',fontsize=15)
    ax.text(.5,.30,'A static affine term cancels from a time increment',ha='center',fontweight='bold',fontsize=15)
    ax.text(.5,.205,r'$\Delta_t(Q_0\cdot A^{\mathrm{phys}})=\mathrm{Ad}(Q_0)\Delta_t A^{\mathrm{phys}}$',ha='center',fontsize=17)
    ax.text(.5,.105,'Its spatial derivative still contains the commutator with '+r'$(\partial Q_0)Q_0^{-1}$.',ha='center',fontsize=12)
    ax.text(.5,.025,'Exact maps: CR.46–CR.48 and CR.79. Each solution retains its own anchors.',ha='center',fontsize=11,color='#354b59')
    save(fig,'f09-original-gauge-reconstruction')
    fig,ax=plt.subplots(figsize=(12,6.8));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    ax.text(.5,.98,'Two coupled estimates give initial-data stability',ha='center',va='top',fontsize=18,fontweight='bold')
    panel(ax,(.04,.63),.42,.22,'Wave difference',r'$\mathcal{R}\leq i\delta_*+\mu\sqrt{T}(\mathcal{R}+\rho)$')
    panel(ax,(.54,.63),.42,.22,'Original physical difference',r'$\rho\leq a\delta_*+b\mathcal{R}+\nu\sqrt{T}(\mathcal{R}+\rho)$')
    ax.text(.5,.56,r'$\mu=2cK,\quad\nu=g,\quad L=\nu+\mu(1+b)$',ha='center',fontsize=15)
    arrow(ax,(.5,.52),(.5,.435),'')
    ax.text(.5,.37,r'$\Delta=(1-\mu\sqrt{T})(1-\nu\sqrt{T})-\mu\sqrt{T}(b+\nu\sqrt{T})$',ha='center',fontsize=15)
    ax.text(.5,.29,r'$\Delta=1-\sqrt{T} L\ \geq\ \frac{1}{2}$',ha='center',fontsize=19,color='#174b4b')
    ax.text(.5,.205,r'$0<T\leq\min\{H,\tau_{\mathrm{ind}},(2L)^{-2}\}\quad(L>0)$',ha='center',fontsize=14)
    ax.text(.5,.135,r'$L=0:\quad \mu=\nu=0,\quad\Delta=1$',ha='center',fontsize=14)
    ax.text(.5,.065,'The inverse has nonnegative entries: both differences are bounded by the initial difference.',ha='center',fontsize=12)
    ax.text(.5,.005,'CP.48–CP.51. Existing regular solutions; original c, S, length and gauge anchors retained.',ha='center',fontsize=11,color='#354b59')
    save(fig,'f09-initial-data-stability')
if __name__=='__main__':build()
