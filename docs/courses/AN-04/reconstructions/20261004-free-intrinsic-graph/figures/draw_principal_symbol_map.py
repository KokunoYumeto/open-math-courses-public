"""Exact local maps in PS14, PS16 and PS28–PS29; CC0 original diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'path'})
fig,ax=plt.subplots(figsize=(4.8,9.2))
fig.subplots_adjust(left=.04,right=.96,top=.97,bottom=.02)
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(y,title,formula,color='#12677a'):
 ax.add_patch(FancyBboxPatch((.035,y-.051),.93,.102,
  boxstyle='round,pad=.012',facecolor='#edf5f7',edgecolor=color,lw=1.2))
 ax.text(.5,y+.029,title,ha='center',va='center',fontsize=11,color=color)
 ax.text(.5,y-.015,formula,ha='center',va='center',fontsize=13)
def arrow(top,bottom,label):
 ax.annotate('',xy=(.5,bottom),xytext=(.5,top),
  arrowprops={'arrowstyle':'->','color':'#233746','lw':1.2})
 ax.text(.5,(top+bottom)/2,label,ha='center',va='center',fontsize=10,
  bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(.5,.985,'Two routes to the same symbol',ha='center',va='top',fontsize=15)
box(.875,'Critical half-density (PS8)',r'$A=a_C\,|\det Q_\phi|^{-1/2}|d\xi|^{1/2}$')
arrow(.81,.765,'Phase normalization (PS16)')
box(.70,'Phase-line coordinate',r'$s=e^{i\pi N/4}A$')
arrow(.635,.59,r'Evaluate at $\mu$: multiply by $e^{i\pi(q-N)/4}$')
box(.525,'Geometric symbol (PS28)',r'$\sigma_m(u)(\mu)=e^{i\pi q/4}A$')
ax.text(.5,.431,r'The two $N$ factors cancel.',ha='center',fontsize=11)
box(.335,'Fourier route (PS14)',r'$b=e^{iH}\widehat{u}_{\rm coeff}$')
ax.text(.5,.252,r'$b=(2\pi)^{n/4}e^{i\pi q/4}a_C|\det Q_\phi|^{-1/2}$',
 ha='center',fontsize=12)
arrow(.232,.198,r'Multiply by $(2\pi)^{-n/4}|d\xi|^{1/2}$')
box(.135,'Same geometric symbol (PS29)',r'$\sigma_m(u)(\mu)=e^{i\pi q/4}A$')
ax.text(.5,.057,r'$q=\mathrm{sgn}\,Q_\phi$; $\mu$ is the horizontal test plane.',
 ha='center',fontsize=10)
ax.text(.5,.027,'All equalities are modulo one lower order.\n'
 'Fourier order: m − n/4. Geometric order: m + n/4.',
 ha='center',va='center',fontsize=10)
fig.savefig(out/'principal-symbol-map.svg')
fig.savefig(out/'principal-symbol-map.png',dpi=160)
print('Wrote exact principal-symbol map diagram.')
