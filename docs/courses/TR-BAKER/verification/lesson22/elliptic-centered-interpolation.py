"""Figure22.19: the exact centered discs of Exercise22.226."""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

base=Path(__file__).resolve().parent
center=49.5
nodes=[j-center for j in range(100)]
targets=[s-center for s in [0,24,48]]
assert [abs(s)+1 for s in targets]==[50.5,26.5,2.5]
fig=plt.figure(figsize=(12.8,6.3),constrained_layout=True)
grid=fig.add_gridspec(2,2,width_ratios=[1.1,1.5],height_ratios=[1,1.25])
ax=fig.add_subplot(grid[:,0])
ax.add_patch(Circle((0,0),100*math.e,fill=False,lw=2,color='#315c87'))
ax.add_patch(Circle((0,0),51,facecolor='#e9f1f7',edgecolor='#2c7790',lw=1.8))
ax.scatter(nodes,[0]*100,s=5,color='#2c7790')
ax.annotate(r'Outer contour: $R=100e$',xy=(145,230),xytext=(-260,290),fontsize=11,arrowprops={'arrowstyle':'-','color':'#315c87'})
ax.annotate(r'Inner disc: $X=51$',xy=(40,30),xytext=(-260,-210),fontsize=11,arrowprops={'arrowstyle':'-','color':'#2c7790'})
ax.set(xlim=(-305,305),ylim=(-305,325),xlabel='Re(z − c)',ylabel='Im(z − c)',title='The full interpolation contour')
ax.set_aspect('equal');ax.grid(alpha=.15)
ax=fig.add_subplot(grid[0,1])
ax.add_patch(Circle((0,0),51,facecolor='#e9f1f7',edgecolor='#2c7790',lw=1.8))
ax.scatter(nodes,[0]*100,s=12,color='#537b91',zorder=3)
for position,label in zip(targets,['s = 0','s = 24','s = 48']):
    ax.add_patch(Circle((position,0),1,fill=False,color='#b65932',lw=2,zorder=5))
    ax.annotate(label,xy=(position,-1),xytext=(position,-3.8),ha='center',fontsize=10,arrowprops={'arrowstyle':'-','color':'#b65932'})
ax.set(xlim=(-54,54),ylim=(-5.5,5.5),xlabel='Re(z − c)',ylabel='Im(z − c)',title='Horizontal strip: 100 nodes and three unit circles')
ax.set_aspect('equal');ax.grid(alpha=.15)
ax=fig.add_subplot(grid[1,1])
ax.add_patch(Circle((0,0),51,facecolor='#e9f1f7',edgecolor='#2c7790',lw=1.8))
ax.add_patch(Circle((-49.5,0),1,fill=False,color='#b65932',lw=2))
ax.scatter([-49.5,-48.5],[0,0],s=25,color='#537b91',zorder=4)
ax.annotate('',xy=(-51,0),xytext=(-50.5,0),arrowprops={'arrowstyle':'<->','color':'#333'})
ax.text(-50.75,.15,'0.5',ha='center',fontsize=10)
ax.text(-49.5,-1.35,'Circle about s = 0',ha='center',fontsize=10,color='#994b2a')
ax.set(xlim=(-51.4,-47.8),ylim=(-1.7,1.7),xlabel='Re(z − c)',ylabel='Im(z − c)',title='The leftmost target circle fits inside the disc')
ax.set_aspect('equal');ax.grid(alpha=.15)
fig.suptitle('Centered interpolation and recovery of derivatives — (22.680)',fontsize=14)
fig.savefig(base/'elliptic-centered-interpolation.png',dpi=180)
plt.close(fig)
print('Figure22.19 saved:100 nodes and three unit circles strictly inside radius51.')
