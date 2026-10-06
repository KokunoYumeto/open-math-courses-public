"""Exact original-coordinate illustration of GR3--GR8, with all volume factors."""
from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Rectangle
plt.rcParams.update({'svg.fonttype':'path','font.family':'DejaVu Sans','font.size':12})
A=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(11,5.8),layout='constrained')
ax.add_patch(Rectangle((-3.5,-1),7,2,facecolor='#e3eff9',edgecolor='#24577e',linewidth=2))
centers=[-3,-1.5,0,1.5,3]
for x in centers:
 ax.add_patch(Ellipse((x,0),1,2,facecolor='#ecb354',edgecolor='#733b0a',alpha=.65,linewidth=1.5))
 ax.plot(x,0,'o',color='#733b0a',markersize=4)
 ax.text(x,1.12,str(x),ha='center',fontsize=10)
ax.axhline(0,color='#24577e',linewidth=1.2,zorder=0)
ax.plot([0,0],[-1.05,1.05],color='#567681',linewidth=1,zorder=0)
ax.annotate('',xy=(3.5,-1.3),xytext=(-3.5,-1.3),arrowprops=dict(arrowstyle='<->',color='#24577e'))
ax.text(0,-1.62,r'Original coordinate width $7$; $g_X$-radius $R+\rho=7$',ha='center',fontsize=11)
ax.annotate('',xy=(3.92,1),xytext=(3.92,-1),arrowprops=dict(arrowstyle='<->',color='#24577e'))
ax.text(4.08,0,r'$2\rho=2$',rotation=90,va='center',fontsize=11)
ax.text(-4.5,1.83,r'$E=\mathbb{R}^2,\quad g_X(x,y)=4x^2+y^2,\quad V=\{(x,0)\},\quad W=\{(0,y)\}$',ha='left',fontsize=13)
ax.text(-4.5,1.50,r'$X=(0,0),\quad r=1,\quad \rho=1,\quad R=6,\quad G_X=\operatorname{diag}(4,1)$',ha='left',fontsize=12)
ax.set_xlim(-4.7,4.7);ax.set_ylim(-2,2.15);ax.set_aspect('equal')
ax.set_xlabel('Original x coordinate');ax.set_ylabel('Original y coordinate')
ax.set_xticks([-3.5,-3,-1.5,0,1.5,3,3.5]);ax.set_yticks([-1,0,1])
ax.spines[['top','right']].set_visible(False)
fig.text(.5,.005,r'$|\det J|=1,\ \det G_V=4,\ \det G_W=1,\ \det G_X=4;\quad \lambda_E(K_\nu)=\pi/2,\ \lambda_E(\mathcal{T}_X)=14,\quad 5\pi/2\leq14$',ha='center',fontsize=12)
fig.savefig(A/'original-phase-range-tube.png',dpi=180,bbox_inches='tight')
fig.savefig(A/'original-phase-range-tube.svg',bbox_inches='tight')
plt.close(fig)
(A/'original-phase-range-tube-parameters.json').write_text(json.dumps(dict(original_coordinates='(x,y)',original_metric_matrix=[[4,0],[0,1]],X=[0,0],rank=1,ambient_dimension=2,rho=1,R=6,centers=[[x,0] for x in centers],ellipse_coordinate_width=1,ellipse_coordinate_height=2,tube=[[-3.5,3.5],[-1,1]],detJ=1,detG_V=4,detG_W=1,detG_X=4,ambient_ball_volume='pi/2',ambient_tube_volume=14,shown_small_ball_overlap=1,proof_locators=['GR3','GR4','GR5','GR6','GR7','GR8'],finite_chosen_configuration_only=True,actual_localization_family_not_claimed=True),indent=2)+'\n',encoding='utf-8')
print('Rendered the original-coordinate tube and all exact determinant/volume factors.')
