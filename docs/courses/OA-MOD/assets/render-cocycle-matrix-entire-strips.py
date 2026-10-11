"""Original exact-label schematic for CMX01--02; no source artwork."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig=plt.figure(figsize=(9,12),dpi=100,facecolor='#f8fafc')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,9),ylim=(0,12));ax.axis('off')
ink='#142b43';blue='#1b658b';orange='#99521d'
def text(x,y,s,size=16,**kw):
    ax.text(x,y,s,fontsize=size,color=kw.pop('color',ink),ha=kw.pop('ha','center'),va='center',**kw)
text(4.5,11.55,'Cocycle matrices and entire domains',23,weight='bold')
text(4.5,11.1,'Exact constructions on an arbitrary von Neumann algebra',13)
text(4.5,10.55,r'$\beta_t=\mathrm{Ad}(\mathrm{diag}(u_t,1))\circ(\sigma_t\otimes\mathrm{id})$',20)
for x,y,label,formula,color in [(1.0,8.2,'B',r'$\alpha_z(b)$',blue),(4.7,8.2,'C',r'$\rho_z(c)$',orange),(1.0,6.35,r'$C^*$',r'$\rho_{\overline{z}}(d)^*$',orange),(4.7,6.35,'A',r'$\sigma_z(a)$',blue)]:
    ax.add_patch(FancyBboxPatch((x,y),3.3,1.55,boxstyle='round,pad=0.04',facecolor='white',edgecolor=color,linewidth=2))
    text(x+1.65,y+1.12,label,21,color=color,weight='bold')
    text(x+1.65,y+.5,formula,23,color=color)
text(4.5,5.95,r'$BCA\subseteq C,\qquad C^*C\subseteq A,\qquad CC^*\subseteq B$',18)
text(4.5,5.55,'CMX01: equations CMX.5–8; the starred entry uses conjugate time.',12)
text(4.5,4.95,'Integer strip domains join to an entire orbit',18,weight='bold')
for lo,hi,color in [(2.9,4.15,'#e3eef5'),(1.65,2.9,'#f4e7d9')]:
    ax.fill_between([1.15,7.75],lo,hi,color=color,zorder=0)
for j in [-2,-1,0,1,2]:
    y=2.9+j*.625
    ax.plot([1.15,7.75],[y,y],color=ink if j==0 else '#8196a8',lw=1.5 if j==0 else 1,ls='-' if j==0 else '--')
    text(.7,y,str(j),13)
ax.annotate('',xy=(8.05,2.9),xytext=(1,2.9),arrowprops=dict(arrowstyle='->',color=ink))
ax.annotate('',xy=(1.15,4.4),xytext=(1.15,1.45),arrowprops=dict(arrowstyle='->',color=ink))
text(.65,4.42,r'$\mathrm{Im}\,z$',12)
text(8.2,2.64,r'$\mathrm{Re}\,z$',12)
text(4.5,3.82,'positive strips',16,color=blue)
text(4.5,1.96,'negative strips',16,color=orange)
text(4.5,1.23,r'$\|\gamma_{t+iy}(x)\|=\|\gamma_{iy}(x)\|$',19)
text(4.5,.81,'CMX02: equations CMX.10–12; schematic shown at integer heights ±1, ±2.',11)
text(4.5,.35,'Source correspondence: Takesaki II, VIII.3, pp. 116 and 128. Original diagram.',10)
fig.savefig(Path(__file__).with_name('cocycle-matrix-entire-strips.png'),dpi=100)
plt.close(fig)
