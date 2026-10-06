"""Exact SB-2 rectangle and shrinking-square illustration. Original CC0-1.0."""
from pathlib import Path
from fractions import Fraction
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
OUT=Path(__file__).resolve().parent/'assets';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none','svg.hashsalt':'oa-flow-mf-scalar-contour'})
fig,ax=plt.subplots(figsize=(13.6,6.5),facecolor='#fbfcfe')
R=2;rho=.12;p=.5
for x,y,w,h in [(-R,0,R-rho,1),(rho,0,R-rho,1),(-rho,0,2*rho,p-rho),(-rho,p+rho,2*rho,1-p-rho)]:
 ax.add_patch(Rectangle((x,y),w,h,facecolor='#e8f0f7',edgecolor='#abb8c7',linewidth=1))
ax.add_patch(Rectangle((-R,0),2*R,1,fill=False,edgecolor='#245b92',linewidth=2.4))
ax.add_patch(Rectangle((-rho,p-rho),2*rho,2*rho,fill=False,edgecolor='#ae4c30',linewidth=2))
def arrow(a,b,c):
 ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':c,'lw':2.5})
for a,b in [((-.4,0),(.4,0)),((R,.32),(R,.68)),((.4,1),(-.4,1)),((-R,.68),(-R,.32))]:arrow(a,b,'#245b92')
for a,b in [((-.06,p-rho),(.06,p-rho)),((rho,p-.06),(rho,p+.06)),((.06,p+rho),(-.06,p+rho)),((-rho,p+.06),(-rho,p-.06))]:arrow(a,b,'#ae4c30')
ax.scatter([0],[p],c='#ae4c30',s=34,zorder=5)
ax.annotate(r'$p=i/2$',xy=(0,p),xytext=(.45,.77),arrowprops={'arrowstyle':'-','color':'#77564d'},color='#8c3b24')
ax.text(0,-.17,r'Lower edge: $I_R(x)$',ha='center',color='#245b92',fontsize=15)
ax.text(0,1.16,r'Upper edge, including reverse traversal: $+e^{-x} I_R(x)$',ha='center',color='#245b92',fontsize=15)
ax.text(2.2,.5,r'Both vertical edges:'+'\n'+r'$|\mathrm{sum}|\leq 1/\sinh(\pi R)$',va='center',fontsize=13)
ax.text(-1.0,.5,'Four rectangles\ncancel their shared edges',ha='center',va='center',color='#455d71')
ax.set_xlim(-2.45,3.55);ax.set_ylim(-.35,1.38);ax.set_aspect('equal')
ax.set_xticks([-2,0,2]);ax.set_xticklabels([r'$-R$',r'$0$',r'$R$']);ax.set_yticks([0,.5,1]);ax.set_yticklabels([r'$0$',r'$1/2$',r'$1$'])
ax.set_xlabel(r'Real part of $z$');ax.set_ylabel(r'Imaginary part of $z$')
ax.spines[['top','right']].set_visible(False)
fig.suptitle('SB-2: one pole, a shrinking square and the cosh kernel',fontsize=20,y=.97)
fig.text(.07,.25,r'For continuous $q$:  $|\int_{\partial Q_\rho}q(z)\,dz|\leq 8\rho\sup_{\partial Q_\rho}|q|\longrightarrow 0$',fontsize=15)
fig.text(.07,.16,r'For the principal part:  $\int_{\partial Q_\rho}(z-p)^{-1}\,dz=2\pi i$',fontsize=15)
fig.text(.07,.07,r'$R=2,\ \rho=3/25$ in this drawing; the proof holds for all $R>0$, $0<\rho<\min(R,1/2)$ and $x\geq0$.',fontsize=12,color='#4d596c')
fig.subplots_adjust(left=.07,right=.97,top=.83,bottom=.38)
fig.savefig(OUT/'kernel-contour.png',dpi=170)
fig.savefig(OUT/'kernel-contour.svg',metadata={'Date':None,'Creator':'Original CC0-1.0 SB-2 contour source'})
plt.close(fig)
svg=OUT/'kernel-contour.svg';svg.write_text('\n'.join(x.rstrip() for x in svg.read_text(encoding='utf8').splitlines())+'\n',encoding='utf8',newline='\n')
data={'rights':'CC0-1.0 original figure and code','R':R,'rho':str(Fraction(3,25)),'pole':[0,'1/2'],'outer_rectangle':[[-2,0],[2,0],[2,1],[-2,1]],'inner_square_center':[0,'1/2'],'both_contour_orientations':'counterclockwise','upper_edge_factor_including_orientation':'+exp(-x)','vertical_edges_total_bound':'1/sinh(pi R)','q_small_square_bound':'8 rho sup(abs(q))','principal_integral':'2 pi i','proof':'MF scalar bridge SB-2'}
(OUT/'figure-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
print('Rendered original kernel contour and exact data.')

