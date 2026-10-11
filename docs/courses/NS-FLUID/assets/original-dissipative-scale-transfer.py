"""Exact original stage, energy and physical-time bounds; schematic geometry."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(17,12),facecolor='white')
ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
teal='#126471';orange='#b85b19'
def txt(x,y,t,size=19,**kw):ax.text(x,y,t,ha='center',va='center',fontsize=size,**kw)
txt(.5,.96,'The original dissipative pump transfers between actual scales',25)
txt(.5,.914,r'$\lambda>1,\quad \nu>0,\quad a_0>0,\quad 0<\alpha<1/2,\quad 0<\delta\leq1-2\alpha$',19)
txt(.5,.872,r'$n=n_0+j,\quad A_j=a_0\lambda^{-\delta j},\quad k=\lambda^n,\quad r=\lambda^{-\delta}$',20)
for x,title,initial in [(.09,r'$X=X_n$',r'$X(0)=A_j$'),(.64,r'$Y=X_{n+1}$',r'$Y(0)=0,\quad Y(\tau_j)=rA_j$')]:
    ax.add_patch(FancyBboxPatch((x,.65),.27,.16,boxstyle='round,pad=0.012',facecolor='#f0f6f7',edgecolor=teal,lw=2))
    txt(x+.135,.766,title,27,color=teal);txt(x+.135,.704,initial,20)
ax.annotate('',xy=(.62,.738),xytext=(.38,.738),arrowprops=dict(arrowstyle='-|>',lw=3,color=orange))
txt(.5,.794,r'$X^\prime=-d_1X-kXY$',20,color=orange)
txt(.5,.678,r'$Y^\prime=-d_2Y+kX^2$',20,color=orange)
txt(.5,.605,r'$d_1=\nu\lambda^{2\alpha n},\qquad d_2=\nu\lambda^{2\alpha(n+1)}=\lambda^{2\alpha}d_1$',22)
txt(.5,.546,r'$X^2+Y^2+2\int_0^\tau(d_1X^2+d_2Y^2)\,ds=A_j^2$',23)
txt(.5,.481,r'$\dfrac{d_2}{kA_j}=\dfrac{\nu\lambda^{2\alpha}}{a_0}\lambda^{-(1-2\alpha)n_0}\lambda^{-(1-2\alpha-\delta)j}\leq\eta_*$',22)
txt(.5,.422,r'$H=2\,\mathrm{atanh}(r),\quad B(H)=(e^{\sqrt{5}H}-1)/\sqrt{5},\quad \eta_*=(\tanh H-r)/(2B(H))$',19)
txt(.5,.36,r'$\dfrac{r}{a_0\lambda^{n_0}}\lambda^{-(1-\delta)j}\leq\tau_j\leq\dfrac{H}{a_0\lambda^{n_0}}\lambda^{-(1-\delta)j}$',24)
txt(.5,.293,'At the endpoint, the damping ratio stays constant; the physical durations still form a summable series.',17)
txt(.5,.244,r'$\delta=1-2\alpha:\quad \lambda^{-(1-2\alpha-\delta)j}=1,\qquad \lambda^{-(1-\delta)j}=\lambda^{-2\alpha j}$',22)
txt(.5,.177,r'$\delta>1-2\alpha:\quad d_2/(kA_j)\longrightarrow\infty,\quad Y(\tau)<kA_j^2/d_2$',21,color=orange)
txt(.5,.131,'Eventually the prescribed next amplitude cannot be reached. This restriction concerns this original transfer schedule.',15)
txt(.5,.085,'DT1–DT25 prove the actual flow, explicit scale choice, finite transfer time, sharp range and strong energy-space endpoint.',13)
txt(.5,.05,'Human source: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex1091–1140. The endpoint is a proved extension.',12)
txt(.5,.022,'Box widths are schematic. All variables and times are the original ones. This is the externally timed scalar model.',12)
for ext in ['png','svg']:fig.savefig(OUT/f'original-dissipative-scale-transfer.{ext}',dpi=150)
plt.close(fig)
