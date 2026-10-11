"""Reproducible diagram of the exact original band decomposition and memory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,10),facecolor='white');ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
teal='#126471';orange='#b85b19'
def txt(x,y,t,size=17,**kw):ax.text(x,y,t,ha='center',va='center',fontsize=size,**kw)
def box(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.01',facecolor='#f0f6f7',edgecolor=teal,lw=2))
txt(.5,.955,'Viscosity creates an exact memory term in each original band',25)
txt(.5,.901,r'$0<\epsilon_0\leq1/1024,\quad q=1+\epsilon_0,\quad \nu\geq0,\quad 0\leq t<T_*$',17)
txt(.5,.847,r'$u_{i,n}=\dfrac{X_{i,n}}{A_i}\psi_{i,n}+h_{i,n},\quad'
                  r'\langle h_{i,n},\psi_{i,n}\rangle=0,\quad'
                  r'E_{i,n}=\dfrac{X_{i,n}^2}{2A_i}+\dfrac{\|h_{i,n}\|_2^2}{2}$',20)
box(.035,.60,.445,.165);box(.52,.60,.445,.165)
txt(.257,.724,'Original scalar coordinate',18,color=teal)
txt(.257,.670,r"$X'_{i,n}=A_iF_{i,n}-\nu q^{2n}\dfrac{G_i}{A_i}X_{i,n}"
                  r"+\nu\langle h_{i,n},g_{i,n}\rangle$",15)
txt(.742,.724,'Entire orthogonal band component',18,color=teal)
txt(.742,.670,r"$h'_{i,n}=\nu L_{i,n}h_{i,n}+\dfrac{\nu X_{i,n}}{A_i}g_{i,n}$",19)
txt(.5,.545,r'$g_{i,n}=q^{2n}D_{q^n}\!\left(\Delta\psi_i+\dfrac{G_i}{A_i}\psi_i\right),'
                  r'\quad \sigma_i^2=J_i-\dfrac{G_i^2}{A_i}>0$',20)
txt(.5,.495,r'$A_i=\|\psi_i\|_2^2,\qquad G_i=\|\nabla\psi_i\|_2^2,\qquad J_i=\|\Delta\psi_i\|_2^2$',18)
ax.annotate('',xy=(.5,.421),xytext=(.5,.466),arrowprops=dict(arrowstyle='-|>',lw=2,color=orange))
box(.035,.254,.93,.156)
txt(.5,.376,'Exact elimination for the original data with zero initial orthogonal component',17,color=teal)
txt(.5,.316,r"$X'_{i,n}=A_iF_{i,n}-\nu q^{2n}\dfrac{G_i}{A_i}X_{i,n}"
                  r"+\dfrac{\nu^2}{A_i}\int_0^t\mathscr{K}_{i,n}(t-r)X_{i,n}(r)\,dr$",22)
txt(.5,.211,r'$\mathscr{K}_{i,n}(t)=\langle e^{\nu tL_{i,n}}g_{i,n},g_{i,n}\rangle'
                  r'=\|e^{\nu tL_{i,n}/2}g_{i,n}\|_2^2$',20)
txt(.5,.154,r'$q^{4n}\sigma_i^2e^{-4\pi^2\nu(1+\epsilon_0/2)^2q^{2n}t}'
                  r'\ \leq\ \mathscr{K}_{i,n}(t)\ \leq\ '
                  r'q^{4n}\sigma_i^2e^{-4\pi^2\nu q^{2n}t}$',19)
txt(.5,.087,'VD1–VD35 prove the original local flow, complete band equations, defect and exact memory map.',13)
txt(.5,.052,'Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex827–1008.',12)
txt(.5,.022,'This diagram states exact operator identities and proved bounds. It is not a computed blowup trajectory.',12)
for ext in ['png','svg']:fig.savefig(OUT/f'original-viscous-cascade-memory.{ext}',dpi=160)
plt.close(fig)
