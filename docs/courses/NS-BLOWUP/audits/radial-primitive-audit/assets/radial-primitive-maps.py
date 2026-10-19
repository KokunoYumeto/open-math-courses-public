"""Reproduce the radial audit's exact-map illustration, R1–R3 and R7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(14,8),dpi=140)
fig.patch.set_facecolor('#f5f8fc')
ax.set(xlim=(0,14),ylim=(0,8));ax.axis('off')
ink='#19334b';blue='#175e9c';green='#2d765d'
def box(x,y,w,h,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#bac9d7'))
def text(x,y,s,size=18,**kw):ax.text(x,y,s,fontsize=size,color=ink,va='center',**kw)
def arrow(x1,y1,x2,y2):ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color=blue,lw=2))
text(.25,7.65,'Two exact maps determine the corrections',23,weight='bold')
text(.25,7.20,'Original physical coordinates, torus covering, and stated curl convention',15)
box(.3,5.35,4.05,1.25,'#e4edf7')
box(5.1,5.35,8.45,1.25,'#dcefe6')
text(.55,6.22,r'$Y^{\prime}=Y+((r^{\prime})^{d_r}-r^{d_r})v_r$',18)
text(.55,5.65,r'$y=J_g^{i_0}Y,\quad r=\sqrt{Q}\,R$',18)
arrow(4.5,5.95,4.95,5.95)
text(5.4,6.22,r'$y^{\prime}=y+\Lambda_g^{i_0}Q^{d_r/2}((R^{\prime})^{d_r}-R^{d_r})v_r$',18)
text(5.4,5.65,r'$M=\Lambda_g^{i_0}Q^{d_r/2}$',19)
text(.45,4.78,r'Reading copy: $\widetilde M=\Lambda_g^{i_0}Q^{d_r}/2=(Q^{d_r/2}/2)M$',18)
text(.45,4.30,'The physical path fixes the exponent and every multiplier.  Proof: R1–R3.',16)
box(.3,2.22,4.05,1.22,'#e4edf7')
box(5.1,2.22,8.45,1.22,'#dcefe6')
text(.55,3.06,r'$\Psi=+r^{-1}\mathcal{I}_c(r\gamma_d)$',19)
text(.55,2.53,r'$\mathcal{A}=\Psi e_\theta$',19)
arrow(4.5,2.84,4.95,2.84)
text(5.4,3.06,r'$\Delta\beta=-\partial_z\Psi$',19)
text(5.4,2.53,r'$\Delta\gamma=(\mathfrak{r}+r^{-1})\Psi=\gamma_d-\mathcal{A}_1\gamma_d$',18)
text(.45,1.66,'Reversing the potential sign reverses both velocity components.  Proof: R7.',16)
text(.45,1.14,'The cutoff remainder is retained; its all-order physical estimate is proved in R5–R6.',16)
text(.45,.48,'Reading-copy corrections; no whole-theorem validation or disproof is claimed.',15)
fig.subplots_adjust(left=.02,right=.98,top=.98,bottom=.02)
out=Path(__file__).with_suffix('.png')
fig.savefig(out,facecolor=fig.get_facecolor());plt.close(fig)
print(out.name)
