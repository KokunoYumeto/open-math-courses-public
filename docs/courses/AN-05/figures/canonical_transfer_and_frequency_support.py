"""Exact phase-plane and operator mechanisms for the localized affine proof;CC0."""
from pathlib import Path
from fractions import Fraction as F
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,FancyBboxPatch
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':11})
fig=plt.figure(figsize=(14,10),dpi=150,facecolor='#fffdfa')
fig.text(.045,.955,'The canonical transfer keeps its support condition',fontsize=20,weight='bold',color='#193249')
fig.text(.045,.918,'Exact symbol-cell images above; exact unitary and finite-remainder mechanisms below',fontsize=12,color='#4b5867')
fig.text(.5,.879,r'$\rho^{2\alpha}\sum_b\|w_b\theta_bU_i\|^2\leq C\left(\sum_b\|P\theta_bU_i\|^2+\|u\|^2\right),\quad i=1,2$',ha='center',fontsize=12,color='#193249')
fig.text(.5,.850,r'$i=1:(\theta_b,w_b)=(\varphi_a,m_a),\quad i=2:(\theta_b,w_b)=(\Phi_j,M_j),\quad \alpha=1/(k+1)$; full conclusions: Theorem1.1',ha='center',fontsize=10,color='#4b5867')
corners=[(-F(3,4),-F(1,2)),(F(3,4),-F(1,2)),(F(3,4),F(1,2)),(-F(3,4),F(1,2))]
sheared=[(z,p+z) for z,p in corners];rotated=[(p+z,-z) for z,p in corners]
panels=[(corners,'Canonical coordinates',r'$z$',r'$\xi$'),
    (sheared,'Gauge shear',r'$X=z$',r'$\Xi=\xi+z$'),
    (rotated,'Fourier rotation',r'$Y=\xi+z$',r'$\mathrm{H}=-z$')]
for j,(points,title,xlab,ylab) in enumerate(panels):
    ax=fig.add_axes([.055+j*.32,.43,.25,.4],facecolor='#fffdfa')
    if j==2:
        ax.axhspan(-.75,.75,color='#e5f1e9',zorder=0)
        ax.axhline(-.75,color='#497a64',ls='--',lw=1);ax.axhline(.75,color='#497a64',ls='--',lw=1)
    xy=np.array([[float(x),float(y)] for x,y in points])
    ax.add_patch(Polygon(xy,closed=True,facecolor='#4389b7',edgecolor='#193249',alpha=.65,lw=2,zorder=3))
    for x,y in xy:ax.plot(x,y,'o',color='#193249',ms=4,zorder=4)
    ax.axhline(0,color='#6c7988',lw=.7);ax.axvline(0,color='#6c7988',lw=.7)
    ax.set_xlim(-1.5,1.5);ax.set_ylim(-1.5,1.5);ax.set_aspect('equal');ax.grid(alpha=.18)
    ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,-.5,0,.5,1])
    ax.set_xlabel(xlab,fontsize=12);ax.set_ylabel(ylab,fontsize=12);ax.set_title(title,fontsize=13,weight='bold',pad=12)
    for spine in ax.spines.values():spine.set_color('#bdc7ce')
fig.text(.18,.395,r'$|z|\leq3/4,\quad|\xi|\leq1/2$',ha='center',fontsize=12,color='#193249')
fig.text(.50,.395,r'$S=z^2/2,\quad(X,\Xi)=(z,\xi+z)$',ha='center',fontsize=12,color='#193249')
fig.text(.82,.395,r'$T_0(X,\Xi)=(\Xi,-X),\quad|\mathrm{H}|\leq3/4$',ha='center',fontsize=12,color='#193249')
boxes=[(.045,.08,.29,.24,'Exact gauge derivative',
    [r'$Vv=e^{iz^2/2}v$',r'$(D_X-X)V=VD_z$',r'$D=-i\partial$']),
    (.355,.08,.29,.24,'Coefficient order under Fourier',
    [r'$\mathcal{F} D_X\mathcal{F}^{-1}=Y$',r'$\mathcal{F} X\mathcal{F}^{-1}=-D_Y$',r'$\mathcal{F}(D_Xc(X))\mathcal{F}^{-1}=Yc(-D_Y)$']),
    (.665,.08,.29,.24,'Repair output Fourier support',
    [r'$w=h(B_2^{\prime}D_2)\Phi U_2$',r'$\operatorname{supp}\widehat w:\ |B_2^{\prime}\Xi_2|<c_0^{\prime}<1$',r'$\sum_j\|E_ju\|^2\leq C_L\lambda^{2L-2n}\|u\|^2$'])]
for x,y,w,h,title,lines in boxes:
    patch=FancyBboxPatch((x,y),w,h,transform=fig.transFigure,boxstyle='round,pad=0.008',facecolor='#f4f7f8',edgecolor='#587a92',lw=1.2)
    fig.add_artist(patch);fig.text(x+w/2,y+h-.035,title,ha='center',fontsize=11.5,weight='bold',color='#193249')
    for l,line in enumerate(lines):fig.text(x+w/2,y+h-.083-l*.06,line,ha='center',fontsize=12 if x<.35 else 10.5,color='#193249')
fig.text(.045,.045,'Proof: Sections2,4–7,(2.1)–(2.2),(4.3)–(4.8),(5.1)–(5.5),(6.1)–(6.3). All polygons are symbol cells;output support requires the multiplier.',fontsize=8.6,color='#4b5867')
fig.text(.045,.024,'Hörmander IV,Lemma27.6.4,printed215–217. Exact illustrative maps;no full adaptive-symbol example assigned. Original diagram and source;CC0.',fontsize=8.6,color='#4b5867')
fig.savefig(Path(__file__).with_name('canonical-transfer-and-frequency-support.png'),dpi=150)
