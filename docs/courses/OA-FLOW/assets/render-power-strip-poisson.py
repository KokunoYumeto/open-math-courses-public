# Original figure and reproduction code: any rights held are dedicated under CC0-1.0.
# NumPy, Matplotlib and installed font software retain their own terms.
"""Reproduce the normalized strip and its exact Poisson boundary masses."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','svg.hashsalt':'oa-flow-power-strip-20261004'})
fig = plt.figure(figsize=(14,9), constrained_layout=True)
grid = fig.add_gridspec(2,2,height_ratios=[1.1,1])
ax = fig.add_subplot(grid[0,:])
ax.add_patch(Rectangle((-2,-1),4,1,facecolor='#edf3fc',edgecolor='none'))
ax.plot([-2,2],[0,0],color='#1565a9',lw=3)
ax.plot([-2,2],[-1,-1],color='#c05b16',lw=3)
ax.set(xlim=(-2.15,2.15),ylim=(-1.42,.36),xlabel=r'$t=\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
ax.set_yticks([-1,-.5,0]); ax.set_yticklabels(['−1','−1/2','0'])
ax.text(-1.95,.15,r'$A(t)=H^{it}K^{-it}$: unitary top edge',color='#1565a9',fontsize=14)
ax.text(-1.95,-1.24,r'$B(t)=H^{it}TK^{-it}$: contractive bottom edge',color='#c05b16',fontsize=14)
ax.plot([.5,.5],[-1,0],ls=':',color='#58626f',lw=1.5)
ax.scatter([.5],[-.4],s=55,color='#172e4f',zorder=4)
ax.text(.62,-.42,r'$z=t-is,\quad0<s<1$',fontsize=13)
ax.annotate('',xy=(.5,0),xytext=(.5,-.33),arrowprops={'arrowstyle':'->','color':'#1565a9','lw':2})
ax.annotate('',xy=(.5,-1),xytext=(.5,-.48),arrowprops={'arrowstyle':'->','color':'#c05b16','lw':2})
ax.text(-1.93,-.32,r'$s\downarrow0:\ P_s^0\to\delta_0,\quad\int P_s^1\to0$',color='#1565a9')
ax.text(-1.93,-.66,r'$s\uparrow1:\ \int P_s^0\to0,\quad P_s^1\to\delta_0$',color='#c05b16')
ax.set_title('Closed-strip continuity from vector Poisson integrals',loc='left',fontsize=17,pad=10)
for spine in ['top','right']: ax.spines[spine].set_visible(False)

kernel = fig.add_subplot(grid[1,0])
r = np.linspace(-2,2,1601); sample_s=.12
p0 = np.sin(np.pi*sample_s)/(2*(np.cosh(np.pi*r)-np.cos(np.pi*sample_s)))
p1 = np.sin(np.pi*sample_s)/(2*(np.cosh(np.pi*r)+np.cos(np.pi*sample_s)))
kernel.plot(r,p0,color='#1565a9',lw=2,label=r'$P_s^0(r)$: top contribution')
kernel.plot(r,p1,color='#c05b16',lw=2,label=r'$P_s^1(r)$: bottom contribution')
kernel.fill_between(r,p0,alpha=.12,color='#1565a9')
kernel.fill_between(r,p1,alpha=.12,color='#c05b16')
kernel.set(xlabel=r'$r$ (horizontal displacement)',ylabel='Kernel density',xlim=(-2,2),ylim=(0,3))
kernel.set_title(r'Exact kernels (DP.3), sampled at $s=0.12$',loc='left',fontsize=14)
kernel.legend(fontsize=10,loc='upper right'); kernel.grid(alpha=.15)
kernel.text(.02,.74,'Window shown: −2 ≤ r ≤ 2.\nMass identities integrate over all ℝ.',transform=kernel.transAxes,fontsize=10)

mass = fig.add_subplot(grid[1,1]); depths=np.linspace(0,1,301)
mass.plot(depths,1-depths,color='#1565a9',lw=3,label=r'$\int_{\mathbb{R}}P_s^0=1-s$')
mass.plot(depths,depths,color='#c05b16',lw=3,label=r'$\int_{\mathbb{R}}P_s^1=s$')
mass.set(xlabel=r'$s=-\operatorname{Im}z$',ylabel='Exact boundary mass',xlim=(0,1),ylim=(0,1))
mass.set_title('Total mass = 1; opposite-edge mass vanishes',loc='left',fontsize=14)
mass.set_xticks([0,.25,.5,.75,1]); mass.grid(alpha=.15); mass.legend(fontsize=12,loc='upper center')
fig.suptitle(r'$H=h^a,\ K=k^a,\ T=\overline{HK^{-1}},\quad U(z)=V(z/a),\quad\|V(z)\|\leq1$',fontsize=18)
fig.text(.5,-.012,'(DP.7)–(DP.8) apply these kernels to boundary vectors and adjoints. '
         '(DP.5) and (DP.11) control tails and joint limits; normal GNS representations give the intrinsic seminorms.\n'
         'Original figure and proof. Scalar antecedents: Vizeff, Berkeley Complex Analysis, Lectures 6, 9–11; '
         'spectral antecedent: Kowalski, Theorems 3.1 and 4.42.',ha='center',va='top',fontsize=10)
fig.savefig(HERE/'power-strip-poisson.png',dpi=170,bbox_inches='tight',facecolor='white')
fig.savefig(HERE/'power-strip-poisson.svg',bbox_inches='tight',facecolor='white',metadata={'Date':'2026-10-04T00:00:00Z'})
svg_path=HERE/'power-strip-poisson.svg'
svg=svg_path.read_text(encoding='utf-8')
start=svg.index('<!DOCTYPE '); end=svg.index('>',start)+1
svg_path.write_text(svg[:start]+svg[end:].lstrip('\n'),encoding='utf-8',newline='\n')
plt.close(fig)
print('Saved power-strip-poisson.png and power-strip-poisson.svg')
