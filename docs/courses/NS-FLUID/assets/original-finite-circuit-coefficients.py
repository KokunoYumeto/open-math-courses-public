"""Exact coefficient constraints and physical return maps; no sampled ODE."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,8.8),facecolor='#f7fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#16354b';blue='#16758c';orange='#b96120'
ax.text(.045,.956,'The finite circuit retains its full coefficients and physical clock',fontsize=21,fontweight='bold',color=ink)
ax.text(.045,.918,r'$K\geq10^{10},\quad 0<\varepsilon\leq K^{-100}e^{-10K^{10}},\quad 1<q<2,\quad \Gamma=q^{5/2}K\in[K,6K]$',fontsize=15,color=ink)
def box(x,y,w,h):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.01',fc='white',ec='#cedbe4',lw=1.1))
box(.035,.44,.52,.425);box(.585,.44,.37,.425)
ax.text(.055,.83,'A diagram of polynomial coefficient constraints',fontsize=15,fontweight='bold',color=ink)
positions={1:(.11,.64),2:(.29,.76),3:(.49,.76),4:(.29,.54),5:(.49,.54)}
for i,j,label,loc in [(1,2,r'$2\varepsilon(A_2-A_1)=0$',(.12,.746)),(2,3,r'$2\varepsilon^{-1}K^{10}(A_3-A_2)=0$',(.28,.797)),(1,4,r'$2\varepsilon^{-2}(A_4-A_1)=0$',(.095,.55)),(4,5,r'$2\Gamma(A_5-A_4)=0$',(.30,.485))]:
    x1,y1=positions[i];x2,y2=positions[j]
    ax.plot([x1,x2],[y1,y2],color=blue,lw=2,zorder=1)
    ax.text(*loc,label,fontsize=11,color=ink,bbox=dict(fc='white',ec='none',pad=1))
for i,(x,y) in positions.items():
    ax.add_patch(Circle((x,y),.027,fc='#e8f3f6',ec=blue,lw=1.6,zorder=3))
    ax.text(x,y,rf'$A_{i}$',ha='center',va='center',fontsize=15,color=ink,zorder=4)
ax.text(.055,.463,'All ten mixed terms and all five linear terms vanish (EX3–EX5).',fontsize=10.5,color=ink)
ax.text(.605,.825,'The complete degree-two answer',fontsize=15,fontweight='bold',color=ink)
ax.text(.605,.768,r'$P=p_0+\beta(a^2+b^2+c^2+d^2+Z^2)$',fontsize=15,color=ink)
ax.text(.605,.716,'The graph vertices are coefficients of P,',fontsize=12,color=ink)
ax.text(.605,.68,'and its edges are exact polynomial identities.',fontsize=12,color=ink)
ax.text(.605,.623,'They are not trajectories or energy-flow arrows.',fontsize=12,color=ink)
ax.text(.605,.56,r'EX1–EX6 hold for every $\varepsilon,K,\Gamma>0$.',fontsize=13,color=blue)
ax.text(.605,.5,'The delay bounds use the parameter range above.',fontsize=11.5,color=ink)
box(.035,.15,.52,.245);box(.585,.15,.37,.245)
ax.text(.055,.36,'The original inter-scale output pump',fontsize=15,fontweight='bold',color=ink)
ax.text(.055,.312,r'$Y_d^{\prime}=q^{5n/2}\varepsilon^{-2}Y_cY_a-q^{5(n+1)/2}KY_dY_Z$',fontsize=14,color=ink)
ax.text(.055,.264,r'$Y_Z^{\prime}=q^{5(n+1)/2}K Y_d^2,\qquad \kappa=q^{5n/2}$',fontsize=14,color=ink)
ax.text(.055,.213,r'$Y(t)=A\,U\!\left(q^{5n/2}A(t-t_0)\right)$',fontsize=15,color=blue)
ax.text(.055,.174,'All three other equations keep their coefficients from EX1.',fontsize=11,color=ink)
ax.text(.605,.36,'The actual delayed output persists',fontsize=15,fontweight='bold',color=ink)
ax.text(.605,.307,r'$T_2=T_c+q^{-5n/2}A^{-1}K^{-1/2}$',fontsize=14,color=ink)
ax.text(.605,.255,r'$0\leq A-Y_Z(t)\leq4AK^{-80}\quad(t\geq T_2)$',fontsize=13,color=orange)
ax.text(.605,.208,r'$\left(Y_a^2+Y_b^2+Y_c^2+Y_d^2\right)^{1/2}\leq2AK^{-40}$',fontsize=13,color=ink)
ax.text(.605,.173,'These are finite-circuit bounds (EX7–EX20).',fontsize=11,color=ink)
ax.text(.045,.106,'Every displayed relation is proved for the original coordinates. The diagram makes no infinite-cascade claim.',fontsize=12,color=ink)
ax.text(.045,.066,'Proof: FINITE_DELAY_EXERCISES_20261010.md, EX1–EX20. Human comparison: Terence Tao, arXiv:1402.0290v3,',fontsize=10.5,color='#445f73')
ax.text(.045,.04,'original navier-blowup.tex, lines 1220–1290 and 1506–1512. Reproducible mathematical diagram; no numerical solution samples.',fontsize=10.5,color='#445f73')
for ext in ['png','svg']:fig.savefig(root/f'original-finite-circuit-coefficients.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
