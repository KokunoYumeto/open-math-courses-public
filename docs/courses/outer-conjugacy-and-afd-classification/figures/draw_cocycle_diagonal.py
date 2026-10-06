"""Original explanatory figure for Lemma 4.1 and Theorem 2.1; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
out=Path(__file__).resolve().parent
plt.rcParams.update({'svg.hashsalt':'oa-classify-cocycle-diagonal-v1','font.family':'DejaVu Sans','font.size':13.5})
fig,axes=plt.subplots(2,1,figsize=(6,9.3))
fig.patch.set_facecolor('#faf9f5')
ax=axes[0]
for x in range(3):
 for y in range(3):
  ax.add_patch(Rectangle((x,y),.92,.92,facecolor='#e5a24e' if x==0 else '#89bdce',edgecolor='#354550'))
  ax.text(x+.46,y+.46,f'({x},{y})',ha='center',va='center')
ax.annotate('',xy=(2.9,3.3),xytext=(1,3.3),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#354550'})
ax.text(1.95,3.52,'g = (1,0)',ha='center')
ax.set(xlim=(-.2,3.2),ylim=(-1.3,3.85));ax.set_aspect('equal');ax.axis('off')
ax.set_title('Interior cancellation; boundary mass',pad=16,fontsize=14)
ax.text(1.4,-.28,'Blue: 6 interior; orange: 3 boundary',ha='center',fontsize=12)
ax.text(1.4,-.61,r'Trace $1/9$ per label: $B_g=1/3$',ha='center',fontsize=12)
ax.text(1.4,-.98,r'If $\delta=0$, error $\leq 2/\sqrt{3}$',ha='center',fontsize=12)
ax=axes[1]
for j in range(1,10):
 k=int(j**.5)
 for r in range(1,4):
  ax.add_patch(Rectangle((j-.43,r-.33),.86,.66,facecolor='#dce9d9' if j>=r*r else '#eee9e3',edgecolor='white'))
  if r==k:ax.plot(j,r,'o',color='#155872',markersize=8)
ax.set(xticks=range(1,10),yticks=range(1,4),xlim=(.4,9.6),ylim=(3.6,.4),xlabel='Representative index j',ylabel='Stage r')
ax.set_title('Select the lift controlled at its own stage',pad=16,fontsize=14)
ax.spines[['top','right']].set_visible(False)
fig.text(.54,.075,r'Toy tests: $E_r=\{j:j\geq r^2\}$, $k(j)=\lfloor\sqrt{j}\rfloor$',ha='center',fontsize=12)
fig.text(.54,.037,r'Dots select $z_{k(j),j}$; fixed cocycle uses index $j$.',ha='center',fontsize=12)
fig.subplots_adjust(left=.12,right=.97,bottom=.16,top=.93,hspace=.5)
fig.savefig(out/'cocycle-diagonal-and-boundary.svg',metadata={'Date':'2026-10-01','Creator':'OA-CLASSIFY Writing AI'},facecolor=fig.get_facecolor())
fig.savefig(out/'cocycle-diagonal-and-boundary.png',dpi=150,metadata={'Software':'OA-CLASSIFY Writing AI'},facecolor=fig.get_facecolor())
plt.close(fig)
