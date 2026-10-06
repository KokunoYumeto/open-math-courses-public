from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(17,11),facecolor='#fbfaf7')
gs=fig.add_gridspec(2,2,left=.055,right=.97,bottom=.075,top=.86,hspace=.48,wspace=.20)
fig.suptitle('Historical Thom transport keeps both input degrees and the entire Clifford module',
             x=.055,y=.955,ha='left',fontsize=21,fontweight='bold',color='#17354a')
fig.text(.055,.918,'Section 8E (AT4–AT34): full coefficient proof with the fixed second-cycle-first product.',
         fontsize=12,color='#475967')

ax=fig.add_subplot(gs[0,0]); ax.axis('off')
ax.set_title('One whole suspension module',loc='left',fontweight='bold',pad=12)
rows=[(r'$E_S=C_0(\mathbb{R}_\tau,H_A)\otimes\mathbb{C}^{1|1}$','#17354a'),
      (r'$s=s^*,\quad\|s\|\leq1,\quad a=1-s^2\in\mathcal{K}(H_A)$','#17354a'),
      (r'$F_n(\tau)=\dfrac{s\sigma_x+\tau\sqrt{a}\,\sigma_y}{\sqrt{1+\tau^2a}}$','#036b82'),
      (r'$F_n^2-1=-\dfrac{a}{1+\tau^2a}\in C_0(\mathbb{R},\mathcal{K}(H_A))$','#17354a'),
      (r'$\|F_n^2-1\|\leq\min(\|a\|,\tau^{-2})$','#17354a')]
for i,(t,c) in enumerate(rows):ax.text(.02,.88-i*.18,t,transform=ax.transAxes,color=c,fontsize=14)
ax.text(.02,-.04,'Creation vectors localize compact differences; (AT7) gives exact positivity.\nThe compact factor √a is needed for an infinite coefficient module.',transform=ax.transAxes,fontsize=11,color='#475967')

ax=fig.add_subplot(gs[0,1]); ax.set_title('Actual relative-projection homotopy',loc='left',fontweight='bold',pad=12)
position=ax.get_position();ax.set_position([position.x0,position.y0+.30*position.height,position.width,.70*position.height])
r=np.linspace(-.88,.88,600)
tau=.7
y=np.tan(np.pi*r/2);g=r/np.sqrt(1-r*r)
for v,col in [(0,'#c87820'),(.5,'#647ba3'),(1,'#036b82')]:
    im=(1-v)*y*np.sqrt(1+tau*tau)+v*g
    ax.plot(r,im,color=col,lw=2.1,label=fr'$v={v:g}$')
ax.set_xlim(-.9,.9);ax.set_ylim(-5,5);ax.axhline(0,c='#b6bdc2',lw=.8)
ax.set_xlabel('Universal spectral parameter r ∈ (−1,1)');ax.set_ylabel(r'$\operatorname{Im}z_v(\tau,r)$');ax.legend(frameon=False,loc='upper left')
ax.grid(alpha=.15)
ax.text(0,-.38,r'$z_v=\tau+i[(1-v)y(r)\sqrt{1+\tau^2}+vg(r)]$'+'\n'+r'$P(z_v)-e_{11}\ \in C([0,1],C_0(\mathbb{R}\times(-1,1),M_2))$',transform=ax.transAxes,fontsize=11,color='#17354a')
ax.text(0,-.54,'Sample τ=0.7. Joint properness is proved in (AT16).\nFunctional calculus r↦s sends the entire homotopy into S⊗K(H_A).',transform=ax.transAxes,fontsize=10.5,color='#475967')

ax=fig.add_subplot(gs[1,0]);ax.axis('off');ax.set_title('Phase, reducer and full leaf frame',loc='left',fontweight='bold',pad=12)
boxes=[(.82,r'$U_t=e^{itH}=e^{-itD},\quad H=-D$'),
       (.58,r'$S_h^0=S_n^0,\quad S_h^1=-S_n^1$'),
       (.34,r'$\phi_\alpha^0=-N_\alpha^0,\quad\phi_\alpha^1=+N_\alpha^1$'),
       (.10,r'$c_H(\xi)=c_{\rm fr}(-\xi),\quad\ell_H=(-1)^d\ell_{\rm fr}$')]
for yi,txt in boxes:
    ax.text(.03,yi,txt,transform=ax.transAxes,fontsize=14,bbox=dict(boxstyle='round,pad=.55',fc='#eef3f4',ec='#bacbd1'))
ax.text(.03,-.13,'Transport the spin-c line, grading, right Clifford action and inner product.\nOdd rank retains the reflected C₁; (AT31a) is a typed onto isometry.',transform=ax.transAxes,fontsize=11,color='#475967')

ax=fig.add_subplot(gs[1,1]);ax.axis('off');ax.set_title('All-coefficient signs and both inverse products',loc='left',fontweight='bold',pad=12)
table=ax.table(cellText=[['0','+ / +','+ / +'],['1','− / +','− / +'],['2','− / −','+ / +'],['3','+ / −','− / +']],
              colLabels=['d mod 4','vs native Φ\neven / odd','vs physical ℓ\neven / odd'],cellLoc='center',loc='upper center',bbox=[0,.30,1,.65])
table.auto_set_font_size(False);table.set_fontsize(12)
for (ri,ci),cell in table.get_celld().items():
    cell.set_edgecolor('#bdcbd1');cell.set_facecolor('#e4edf0' if ri==0 else '#f7f8f6')
ax.text(.02,.15,r'$X\star Y=(-1)^{|X||Y|}XY,\quad\widetilde\Theta=(-1)^ds_d\Theta$',transform=ax.transAxes,fontsize=12.5,color='#17354a')
ax.text(.02,.01,r'$\widetilde\Theta\star(s_dD_H)=1,\quad(s_dD_H)\star\widetilde\Theta=1$',transform=ax.transAxes,fontsize=12.5,color='#17354a')
ax.text(.02,-.14,'Exact source: IHES/M/80/28, §II pp.7–13, Appendix VI pp.29–31.\nLeaf realization: explicit full reflection (AT31), not an unprinted Pauli claim.',transform=ax.transAxes,fontsize=10.5,color='#475967')

fig.savefig(HERE/'all-coefficient-transport.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(HERE/'all-coefficient-transport.svg',facecolor=fig.get_facecolor())
plt.close(fig)
print('Rendered reproducible PNG and editable SVG.')


