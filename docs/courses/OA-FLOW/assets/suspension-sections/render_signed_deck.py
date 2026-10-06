"""Original CC0 signed deck-map illustration; exact rational constants."""
from pathlib import Path
from fractions import Fraction as Q
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'mathtext.fontset':'dejavusans','svg.fonttype':'path','svg.hashsalt':'oa-flow-l38-signed-deck-v1'})
navy='#17334d';blue='#2563a6';teal='#147a70';orange='#b45118';light='#f1f5f9';gray='#718294'
r0=Q(2);r1=Q(3);s=Q(11,4);sp=s-r0
assert sp==Q(3,4) and r0<=s<r0+r1 and 0<=sp<r1
n=1;np=0
assert np==n-1 and s==r0+sp
checks={'r(z)':str(r0),'r(Sz)':str(r1),'s':str(s),'s-r(z)':str(sp),'n(s,z)':n,'n(s-r(z),Sz)':np,'deck':'B(s,z)=(s-r(z),Sz)','cover_deck':'L(m,y)=(m-1,y)','same_point':'F_(11/4) z = F_(3/4) (Sz)','scope':'Local orbit segment, not a finite base; no freeness or ergodicity inferred from the drawing.','all_exact_assertions_pass':True}
OUT.joinpath('exact_checks.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
fig=plt.figure(figsize=(16,10),facecolor='white')
fig.text(.06,.945,'A deck step preserves the flow point',fontsize=25,weight='bold',color=navy)
fig.text(.06,.895,'Local orbit segment:  r(z) = 2,  r(Sz) = 3.  Both roofs are positive.',fontsize=17,color=gray)
ax=fig.add_axes([.08,.31,.40,.51]);ax.set_xlim(-.65,2.7);ax.set_ylim(-.28,3.55)
ax.spines[['top','right','bottom']].set_visible(False);ax.spines['left'].set_color(gray)
ax.set_xticks([]);ax.set_yticks([0,.75,2,2.75,3]);ax.set_yticklabels(['0',r'$\frac{3}{4}$','2',r'$\frac{11}{4}$','3']);ax.tick_params(axis='y',length=0,pad=9)
ax.set_ylabel('lifted time coordinate  s',fontsize=15,labelpad=12,color=navy)
ax.set_title(r'Time lifts in $\mathbb{R}\times Z$',loc='left',fontsize=20,color=navy,pad=16)
for x,r,col,base in [(0,r0,blue,'z'),(2,r1,teal,'Sz')]:
 ax.add_patch(Rectangle((x-.20,0),.40,float(r),facecolor=col,alpha=.12,edgecolor='none'))
 ax.plot([x,x],[0,3.38],color=col,lw=2)
 ax.plot([x-.28,x+.28],[float(r),float(r)],color=col,lw=2,ls='--')
 ax.scatter([x],[0],s=45,c=col,zorder=4)
 ax.text(x,-.19,'$'+base+'$',ha='center',va='top',fontsize=20,color=col)
 ax.text(x+.24,float(r)+.10,'roof '+str(r),ha='left',va='bottom',fontsize=13,color=col)
ax.scatter([0],[float(s)],s=130,c=blue,zorder=6);ax.scatter([2],[float(sp)],s=130,c=teal,zorder=6)
ax.text(0,3.03,r'$(\frac{11}{4},z)$',ha='center',fontsize=20,color=blue,bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.text(2,1.03,r'$(\frac{3}{4},Sz)$',ha='center',fontsize=20,color=teal,bbox={'facecolor':'white','edgecolor':'none','pad':2})
ax.annotate('',xy=(1.89,.83),xytext=(.12,2.68),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':orange,'connectionstyle':'arc3,rad=.03','mutation_scale':18})
ax.text(.9,1.35,r'$B$: subtract 2'+'\nadvance to $Sz$',ha='center',va='center',fontsize=15,color=orange,bbox={'facecolor':'white','edgecolor':'none','pad':4})
ax2=fig.add_axes([.64,.31,.29,.51]);ax2.set_xlim(-.2,2.4);ax2.set_ylim(-.25,1.5)
ax2.spines[['top','right','bottom']].set_visible(False);ax2.spines['left'].set_color(gray)
ax2.set_xticks([]);ax2.set_yticks([0,1]);ax2.tick_params(axis='y',length=0,pad=9)
ax2.set_ylabel('integer coordinate  m',fontsize=15,labelpad=12,color=navy)
ax2.set_title(r'Hitting cover $\mathbb{Z}\times\Gamma$',loc='left',fontsize=20,color=navy,pad=16)
for m,col in [(1,blue),(0,teal)]:
 ax2.plot([0,2.1],[m,m],color=gray,lw=1,ls=':')
 ax2.scatter([.9],[m],s=130,c=col,zorder=6)
 ax2.text(1.12,m+.055,'$('+str(m)+',y)$',fontsize=21,ha='left',va='bottom',color=col)
ax2.annotate('',xy=(.9,.11),xytext=(.9,.88),arrowprops={'arrowstyle':'-|>','lw':2.8,'color':orange,'mutation_scale':18})
ax2.text(1.10,.5,r'$L$: $m\mapsto m-1$',fontsize=15,color=orange,va='center')
ax2.text(.9,-.17,'same flow point  $y$',fontsize=16,ha='center',va='top',color=navy)
fig.text(.535,.59,r'$\Phi$',fontsize=27,color=navy,ha='center')
fig.text(.535,.54,'identifies',fontsize=13,color=gray,ha='center')
fig.text(.535,.505,'the labels',fontsize=13,color=gray,ha='center')
box=FancyBboxPatch((.06,.075),.88,.16,transform=fig.transFigure,boxstyle='round,pad=0.012',facecolor=light,edgecolor='#d9e2eb');fig.patches.append(box)
fig.text(.50,.183,r'$y=F_{11/4}z=F_{3/4}(Sz)$',ha='center',fontsize=22,color=navy)
fig.text(.50,.122,r'$\Phi B=L\Phi,\qquad n(\frac{11}{4}-2,Sz)=1-1=0$',ha='center',fontsize=22,color=navy)
fig.text(.06,.026,'Exact coordinates. Shading marks the half-open fundamental roof intervals. Proof: L38, hitting-cover construction.',fontsize=12,color=gray)
fig.savefig(OUT/'signed-deck-map.png',dpi=200,facecolor='white')
fig.savefig(OUT/'signed-deck-map.svg',metadata={'Date':None},facecolor='white')
plt.close(fig)
print(json.dumps({'png':'signed-deck-map.png','pixels':[3200,2000],'exact_checks':True}))
