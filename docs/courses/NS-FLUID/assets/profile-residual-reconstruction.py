"""Exact finite paths and retained errors in RQ4–RQ19; no sampled solution."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
import numpy as np

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig=plt.figure(figsize=(15,7.4),layout='constrained')
grid=fig.add_gridspec(2,3,width_ratios=[1.1,0.9,1.6],height_ratios=[1,0.20])
ax=fig.add_subplot(grid[0,:2]);eq=fig.add_subplot(grid[0,2]);cap=fig.add_subplot(grid[1,:])
A=2;B0=1.5;px=1.2;py=1.0
ax.add_patch(Rectangle((-A,0),2*A,B0,facecolor='#eaf2f8',edgecolor='#27445a',lw=1.5))
ax.axhline(0,color='#27445a',lw=2)
ax.annotate('',(px,0),(0,0),arrowprops=dict(arrowstyle='->',color='#ad412a',lw=3))
ax.annotate('',(px,py),(px,0),arrowprops=dict(arrowstyle='->',color='#ad412a',lw=3))
ax.plot([0,px],[0,py],'o',color='#ad412a',ms=7)
ax.text(0.08,-0.17,r'$(0,0):\ \Theta=C,\ P=P_0$',fontsize=12)
ax.text(px+0.08,py,r'$y=(1.2,1.0)$',fontsize=12)
ax.text(0.43,0.09,'horizontal path',color='#8a3020',fontsize=11)
ax.text(px-0.13,0.50,'vertical path',color='#8a3020',rotation=90,ha='right',fontsize=11)
ax.text(-1.85,1.34,r'$Q_{A,B_0}=[-A,A]\times[0,B_0]$',fontsize=13)
ax.text(-1.85,1.17,r'Illustration: $A=2,\ B_0=1.5$',fontsize=11)
ax.text(-1.85,-0.17,r'wall: $U_2(y_1,0)=0$',fontsize=12)
ax.set(xlim=(-2.25,2.25),ylim=(-0.32,1.75),xlabel=r'$y_1$',ylabel=r'$y_2$')
ax.set_aspect('equal',adjustable='box')
ax.set_title('Original coordinates and the two finite paths',loc='left',fontweight='bold',pad=16)
ax.spines[['top','right']].set_visible(False)

inset=ax.inset_axes([0.10,0.24,0.27,0.36])
inset.add_patch(Polygon([(0,0),(1,0),(1,1)],facecolor='#e9c487',edgecolor='#926520',lw=1.5))
inset.plot([0,1],[0,1],color='#926520',lw=1.5)
inset.set(xlim=(0,1.1),ylim=(0,1.1),xticks=[0,1],yticks=[0,1])
inset.set_xticklabels(['0',r'$y_2$']);inset.set_yticklabels(['0',r'$y_2$'])
inset.set_xlabel(r'$s$',labelpad=-3);inset.set_ylabel(r'$t$',labelpad=-4)
inset.set_title(r'$0\leq t\leq s\leq y_2$',fontsize=11)
inset.text(0.60,0.22,r'$\frac{y_2^2}{2}$',ha='center',fontsize=16)
inset.spines[['top','right']].set_visible(False)
eq.axis('off')
eq.set_title('Every residual reaches the full equation',loc='left',fontweight='bold',pad=16)
items=[
 (0.91,r'$I(y)=\int_0^{y_2} f_6(y_1,s)\,ds$'),
 (0.79,r'$\nabla\Theta=(\Phi-I,\ \Psi)$'),
 (0.67,r'$B=f_1-f_5-V\cdot\nabla f_5$'),
 (0.59,r'$\qquad+f_4(\Omega-f_5)+I$'),
 (0.44,r'$M=\left(-\varepsilon\int_0^{y_2} B(y_1,s)\,ds,\ 0\right)$'),
 (0.28,r'$\partial_1T=f_2-(2+\partial_1U_1)I-V\cdot\nabla I$'),
 (0.16,r'$\partial_2T=f_3-(\partial_2U_1)I$')]
for yy,txt in items:eq.text(0,yy,txt,fontsize=14,va='center')
cap.axis('off')
cap.text(0,0.88,'The paths define temperature and pressure on the original half-plane. The shaded triangle retains the exact nested-integral factor.',fontsize=12,va='top')
cap.text(0,0.56,'M is the complete momentum error; T is the temperature error. The sign ε is +1 for the main-text curl and −1 for the included supplement.',fontsize=12,va='top')
cap.text(0,0.24,'Proof: RQ4–RQ19. Human sources: Wang, Lai, Gómez-Serrano and Buckmaster, arXiv:2201.06780v3, main106–139; supplement180–259.',fontsize=11,va='top')
for suffix in ['png','svg']:fig.savefig(OUT/f'profile-residual-reconstruction.{suffix}',dpi=180,facecolor='white')
print(str(OUT/'profile-residual-reconstruction.png'))
