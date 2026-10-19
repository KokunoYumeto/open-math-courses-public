from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
matplotlib.rcParams.update({'font.size':17,'svg.hashsalt':'oa-classify-twisted-folner-v1','font.family':'DejaVu Sans'})
fig,ax=plt.subplots(figsize=(6.5,10));ax.set(xlim=(0,6.5),ylim=(0,10));ax.axis('off')
ax.text(.25,9.65,'Twisted Følner compression',fontsize=22,weight='bold',va='top')
ax.text(.25,8.9,'F = {−2, −1, 0, 1, 2};  g = 1',fontsize=18)
ax.text(.25,8.45,'Columns: t     Rows: s     Survive: s = g + t',fontsize=16)
origin=(1.1,3.7);step=.85;vals=list(range(-2,3))
for i,s in enumerate(vals):
 ax.text(.72,origin[1]+(4-i+.5)*step,str(s),ha='center',va='center')
 for j,t in enumerate(vals):
  yes=s==t+1;x=origin[0]+j*step;y=origin[1]+(4-i)*step
  ax.add_patch(Rectangle((x,y),step,step,facecolor='#79c8b6' if yes else '#eef1f5',edgecolor='white',linewidth=2))
  ax.text(x+step/2,y+step/2,'✓' if yes else '0',ha='center',va='center',color='#103e39' if yes else '#68707c',fontsize=22 if yes else 16)
for j,t in enumerate(vals):ax.text(origin[0]+(j+.5)*step,8.13,str(t),ha='center',va='center')
ax.text(.25,3.15,'The actual unitary factors cancel:',weight='bold',fontsize=17)
ax.text(.25,2.6,r'$U_s E(U_s^* z U_t) U_t^* = z$',fontsize=22)
ax.text(.25,1.95,'4 surviving pairs / 5 columns',fontsize=20)
ax.text(.25,1.4,r'$\Psi_F\Phi_F(aU_g)=\frac{4}{5}\,aU_g$',fontsize=22)
ax.text(.25,.5,'Exact count: equations (4.2)–(4.5).\nFinite diagram; the factor proof is in the text.',fontsize=15,linespacing=1.5)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
base=Path(__file__).with_name('twisted-folner-compression')
fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-CLASSIFY mathematical figure source'})
fig.savefig(base.with_suffix('.png'),dpi=160,metadata={'Software':'OA-CLASSIFY mathematical figure source'})
plt.close(fig)
