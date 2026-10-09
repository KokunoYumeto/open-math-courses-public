"""CC0: exact coordinate/sign and metric-neighbourhood illustrations."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

D=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans','svg.fonttype':'none','svg.hashsalt':'SH02-IC-mechanisms-v1'})
fig=plt.figure(figsize=(13,9),layout='constrained')
gs=fig.add_gridspec(3,1,height_ratios=[1,1.7,0.27])
ax=fig.add_subplot(gs[0]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
ax.text(0,0.96,'Exact cotangent exchange for I1',fontsize=17,weight='bold',va='top')
ax.text(0,0.79,r'$u=x-y,\ z=y:\quad \alpha\,dx-\beta\,dy=\alpha\,du+(\alpha-\beta)\,dz$',fontsize=15)
boxes=[(0.02,r'$(x-y,\alpha-\beta)/h$'+'\nnormal limit'),
       (0.275,r'$(v,w)$'+'\nnormal vector'),
       (0.54,r'$(w,-v)$'+'\nFourier covector'),
       (0.805,r'$(v,w)$'+'\nin '+r'$C(A,B)$')]
for x,label in boxes:
    patch=FancyBboxPatch((x,0.22),0.17,0.35,boxstyle='round,pad=0.01',facecolor='#e9f0fa',edgecolor='#335680',linewidth=1.4)
    ax.add_patch(patch); ax.text(x+0.09,0.395,label,ha='center',va='center',fontsize=12)
for x in [0.2,0.465,0.73]:
    ax.annotate('',xy=(x+0.06,0.395),xytext=(x,0.395),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#335680'})
ax.text(0.48,0.09,r'$H(a\,dz+b\,d\xi)=(b,-a),\qquad -H(w\,dz-v\,d\xi)=(v,w)$',ha='center',fontsize=14)
ax.text(0,0.0,'Proof: IC1, equations IC1.1–IC1.3. The order A then B is retained.',fontsize=10,color='#444444')

ax=fig.add_subplot(gs[1]); ax.set_title('An exact variable-size neighbourhood in the tautness proof',loc='left',fontsize=17,weight='bold')
x=np.linspace(-1.8,1.8,1101); z=np.linspace(-0.65,0.65,451)
xx,zz=np.meshgrid(x,z)
dist_c=np.sqrt(zz**2+np.maximum(np.abs(xx)-1,0)**2)
dist_complement=np.sqrt(zz**2+np.maximum(1.6-np.abs(xx),0)**2)
phi=dist_complement/3-dist_c
ax.contourf(xx,zz,phi,levels=[0,float(phi.max()+1)],colors=['#bddcd3'],alpha=0.8)
ax.contour(xx,zz,phi,levels=[0],colors=['#127358'],linewidths=2)
ax.axhline(0,color='#6a6a6a',lw=1.2,zorder=3)
ax.plot([-1.6,1.6],[0,0],lw=7,color='#b0b0b0',solid_capstyle='butt',zorder=4)
ax.plot([-1,1],[0,0],lw=4,color='#28466b',solid_capstyle='butt',zorder=5)
ax.plot([-1.6,1.6],[0,0],'o',mfc='white',mec='#666666',ms=8,zorder=6)
ax.plot([-1,1],[0,0],'o',color='#28466b',ms=6,zorder=7)
ax.text(-1.78,0.06,r'$Y=\mathbb{R}\times\{0\}$',fontsize=12)
ax.text(0,0.21,r'$V:\ d((x,z),C)<\frac{1}{3}d((x,z),Y\setminus U)$',ha='center',fontsize=13,color='#0b5c45')
ax.text(0,-0.12,r'$C=[-1,1]\times\{0\},\qquad U=(-1.6,1.6)\times\{0\}$',ha='center',fontsize=12)
ax.set_xlabel(r'ambient horizontal coordinate $x$'); ax.set_ylabel(r'ambient normal coordinate $z$')
ax.set_xlim(-1.8,1.8); ax.set_ylim(-0.65,0.65); ax.set_aspect('equal',adjustable='box')
ax.grid(alpha=0.15)
caption=fig.add_subplot(gs[2]); caption.axis('off')
caption.text(0,0.83,'Proof: IC4, equation IC4.2. One local member is shown; the proof uses a locally finite family covering all of Y.',fontsize=10,va='top')
caption.text(0,0.28,'The boundary is sampled from the exact inequality. Distances are '+r'$\sqrt{z^2+(|x|-1)_+^2}$'+' to C and '+r'$\sqrt{z^2+(1.6-|x|)_+^2}$'+' to '+r'$Y\setminus U$'+'.',fontsize=10,va='top')
fig.savefig(D/'involutivity_mechanisms.png',dpi=180,bbox_inches='tight')
fig.savefig(D/'involutivity_mechanisms.svg',bbox_inches='tight',metadata={'Date':None})
plt.close(fig)
print('figure_written')
