"""Reproduce Figure10.11 from exact exponent sets. Original work, CC0."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(14,8.5),layout='constrained')
grid=fig.add_gridspec(2,2,height_ratios=[1,.20])
ax=fig.add_subplot(grid[0,0])
ax.add_patch(Rectangle((-2,-1),4,2,facecolor='#fef3c7',edgecolor='#d97706',lw=2,ls='--',label='Coordinate box: 15 integer points'))
ax.add_patch(Polygon([(2,0),(0,1),(-2,0),(0,-1)],facecolor='#dbeafe',edgecolor='#2563eb',lw=2,label='Actual diamond: 7 integer points'))
box=[(i,j) for i in range(-2,3) for j in range(-1,2)]
diamond=[(i,j) for i,j in box if abs(i)+2*abs(j)<=2]
outside=[(i,j) for i,j in box if (i,j) not in diamond]
ax.scatter(*zip(*outside),s=55,color='#d97706',zorder=3)
ax.scatter(*zip(*diamond),s=65,color='#2563eb',zorder=4)
active=[((2,0),'Real place: (2, 0)',(-1.15,.42)),((-2,0),'2-adic: (-2, 0)',(-2.18,.56)),((0,-1),'3-adic: (0, -1)',(.35,-1.30))]
for point,label,xy in active:
 ax.scatter(*point,s=135,facecolor='white',edgecolor='#0f172a',lw=1.7,zorder=5)
 ax.annotate(label,xy=point,xytext=xy,arrowprops={'arrowstyle':'->','color':'#475569'},fontsize=11,color='#0f172a')
ax.set(xlim=(-2.6,2.6),ylim=(-1.6,1.6),xlabel=r'Exponent $m_1$',ylabel=r'Exponent $m_2$',title=r'$\theta=(2,3)$: exact support and enclosing box')
ax.set_aspect('equal');ax.set_xticks(range(-2,3));ax.set_yticks([-1,0,1]);ax.grid(alpha=.18)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.19),frameon=False,fontsize=11)

bar=fig.add_subplot(grid[0,1])
contributions=[('Actual diamond',[4,4,3],48),('Coordinate box',[12,4,3],144)]
colors=['#2563eb','#059669','#7c3aed']
labels=['Real place','2-adic place','3-adic place']
for y,(name,values,total) in enumerate(contributions):
 left=0
 for j,n in enumerate(values):
  width=math.log(n);bar.barh(y,width,left=left,height=.42,color=colors[j],label=labels[j] if y==0 else None)
  bar.text(left+width/2,y,rf'$\ln {n}$',ha='center',va='center',color='white',fontsize=13)
  left+=width
 bar.text(left+.07,y,rf'$h=\ln {total}$',ha='left',va='center',fontsize=13)
bar.set_yticks([0,1],labels=[a[0] for a in contributions])
bar.invert_yaxis()
bar.set(xlim=(0,6.2),ylim=(1.7,-.65),xlabel='Projective height (natural logarithm)',title='Exact local contributions')
bar.spines[['top','right']].set_visible(False)
bar.grid(axis='x',alpha=.15);bar.set_axisbelow(True)
bar.legend(loc='upper left',bbox_to_anchor=(0,-.15),ncol=1,frameon=False,fontsize=11)

note=fig.add_subplot(grid[1,:]);note.axis('off')
note.text(.5,.78,r'Diamond: $|m_1|+2|m_2|\leq2$       Box: $|m_1|\leq2,\ |m_2|\leq1$',ha='center',fontsize=14,color='#0f172a')
note.text(.5,.39,r'Exact height loss from the box: $\ln144-\ln48=\ln3$',ha='center',fontsize=14,color='#0f172a')
note.text(.5,.06,'Theorems 10.59–10.60 and Corollaries 10.61–10.62; equations (10.159)–(10.168); Solution 31.',ha='center',fontsize=11,color='#475569')
fig.savefig(Path(__file__).with_name('support-height-envelope.png'),dpi=150,facecolor='white')
plt.close(fig)
