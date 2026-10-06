from pathlib import Path
import json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib import font_manager
P=Path(__file__).resolve().parent
# Coordinates name the four left cosets of K=<b>, in this order.
labels=['K','aK','tK','btK']
perms={'a':[1,0,2,3],'b':[0,1,3,2],'t':[2,3,0,1]}
assert all(perms[g][perms[g][i]]==i for g in perms for i in range(4))
assert all(perms['t'][perms['a'][perms['t'][i]]]==perms['b'][i] for i in range(4))
assert all(perms['a'][perms['b'][i]]==perms['b'][perms['a'][i]] for i in range(4))
data={'group':'G=(C2 x C2) semidirect C2; tat=b','subgroups':{'H':'<a,b>','K':'<b>'},'points':labels,'left_action_permutations':perms,'quotient_q':[0,0,1,1],'quotient_q_prime':[1,1,0,0],'identity_fibre_kernels':{'q':'<b>','q_prime':'<a>'}}
(P/'data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,6.6));fig.patch.set_facecolor('#f8fafc');ax.set_facecolor('#f8fafc');ax.set(xlim=(-.65,6.5),ylim=(-.8,3.35));ax.axis('off')
ax.text(-.45,3.1,'One group action, two choices of fiber',fontsize=23,weight='bold',color='#10253f')
ax.text(-.45,2.72,r'$G=\langle a,b,t\mid a^2=b^2=t^2=e,\ ab=ba,\ tat=b\rangle$',fontsize=17,color='#26394f')
coords=[(0,1.8),(2.5,1.8),(0,0),(2.5,0)]
for y,c in [(1.8,'#dceafc'),(0,'#ffead5')]:ax.add_patch(FancyBboxPatch((-.37,y-.38),3.23,.76,boxstyle='round,pad=0.08',linewidth=0,facecolor=c))
for i,(x,y) in enumerate(coords):
 ax.scatter([x],[y],s=115,color='#152f4e',zorder=4);ax.text(x,y+.21,'$'+labels[i]+'$',ha='center',fontsize=19)
for inds,color,label,offset in [((0,1),'#245c99','$a$',.08),((2,3),'#b65a0c','$b$',-.12)]:
 p,q=[coords[i] for i in inds];ax.add_patch(FancyArrowPatch((p[0]+.15,p[1]),(q[0]-.15,q[1]),arrowstyle='<->',mutation_scale=20,linewidth=2.5,color=color));ax.text(1.25,p[1]+offset,label,ha='center',va='bottom' if offset>0 else 'top',fontsize=19,color=color)
for x in [0,2.5]:ax.add_patch(FancyArrowPatch((x,1.57),(x,.23),arrowstyle='<->',mutation_scale=20,linewidth=2.5,color='#28705a'));ax.text(x+.12,.84,'$t$',fontsize=19,color='#28705a')
ax.text(3.12,2.04,'Identity fiber of q',fontsize=18,weight='bold',color='#245c99')
ax.text(3.12,1.65,'a swaps; b fixes both points',fontsize=15,color='#26394f')
ax.text(3.12,1.3,r'kernel $\langle b\rangle$',fontsize=17,color='#245c99')
ax.text(3.12,.28,"Identity fiber of q′",fontsize=18,weight='bold',color='#a84b0b')
ax.text(3.12,-.11,'b swaps; a fixes both points',fontsize=15,color='#26394f')
ax.text(3.12,-.46,r'kernel $\langle a\rangle$',fontsize=17,color='#a84b0b')
ax.text(-.4,-.69,'q′ exchanges the two cosets of G/H. The inducing H-actions have different kernels.',fontsize=13,color='#374b63')
fig.tight_layout(pad=1);fig.savefig(P/'two-fibers.png',dpi=220,facecolor=fig.get_facecolor());fig.savefig(P/'two-fibers.svg',facecolor=fig.get_facecolor());plt.close(fig)
font=Path(font_manager.findfont('DejaVu Sans'));candidates=[font.parent/'LICENSE_DEJAVU',font.parent.parent/'LICENSE_DEJAVU',Path(matplotlib.get_data_path())/'fonts/ttf/LICENSE_DEJAVU']
for f in candidates:
 if f.exists():shutil.copyfile(f,P/'FONT-LICENSE.txt');break
else:raise RuntimeError('Font license not found')
print(json.dumps({'figure':str(P/'two-fibers.png'),'relations_verified':True}))
