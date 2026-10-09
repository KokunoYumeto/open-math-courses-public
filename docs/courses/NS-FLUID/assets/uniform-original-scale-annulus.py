"""Exact original-coordinate mass factors and logarithmic support diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,10),facecolor='#f7f9fc')
ax=fig.add_axes([.04,.51,.92,.43]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(0,1.04,'Original mass gives a positive velocity integral at every scale',
        fontsize=20,weight='bold',color='#102942')
boxes=[
 (.01,.48,.29,.40,'Vorticity mass and volume',
  r'$\int_{\mathrm{shell}}|\omega|^2\,dx\ \geq\ e_F/\ell_a$'+'\n'+
  r'$|\mathrm{shell}|\leq v_3(\beta_s^3-\alpha_s^3)\overline{R}_c^3\ell_a^3$'+'\n'+
  r'$|\omega(x_*)|\geq m_c\ell_a^{-2}$'),
 (.355,.48,.29,.40,'Full derivative neighborhood',
  r'$|\nabla\omega|\leq\nu^{-1/2}\ell_a^{-3}$'+'\n'+
  r'$r=r_c\ell_a,\quad r_c\leq 2m_c\sqrt{\nu}/(3\mu)$'+'\n'+
  r'$\mathrm{mean}\geq(m_c-\mu r_c/\sqrt{\nu})\ell_a^{-2}$'),
 (.70,.48,.29,.40,'Original curl and Jacobian',
  r'$\mathrm{mean}=-r^{-1}\int u\cdot(e\times\nabla\varphi)$'+'\n'+
  r'$dx=r^3\,dy$'+'\n'+
  r'$\int_{B(x_*,r)}|u|^3\,dx\geq r^6\,\mathrm{mean}^3/C_{3,\varphi}^3$')
]
for x,y,w,h,title,body in boxes:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.008',facecolor='white',edgecolor='#b7c7db',linewidth=1.5))
 ax.text(x+w/2,y+h-.055,title,ha='center',va='top',fontsize=13,weight='bold',color='#17446b')
 ax.text(x+w/2,y+.17,body,ha='center',va='center',fontsize=11,linespacing=2)
for a,b in [(.308,.347),(.652,.692)]:
 ax.annotate('',xy=(b,.69),xytext=(a,.69),arrowprops=dict(arrowstyle='->',lw=2,color='#26787d'))
ax.text(.5,.33,r'$\ell_a^6\ell_a^{-6}=1,\qquad'
 r'\int_{B(x_*,r)}|u(t_0,x)|^3\,dx\geq L_c'
 r'=\dfrac{r_c^6(m_c-\mu r_c/\sqrt{\nu})^3}{C_{3,\varphi}^3}>0$',
 ha='center',fontsize=19,color='#176057')
ax.text(.5,.14,'All constants are proved independent of the selected original time scale S.',
 ha='center',fontsize=14)
ax.text(.5,.02,'Proof: 5.3–6.1. The original viscosity, derivative loss and every radius factor remain visible.',
 ha='center',fontsize=12,color='#44556a')
bx=fig.add_axes([.10,.13,.81,.28]);bx.set_xlim(-.15,3.15);bx.set_ylim(-.4,2.7)
bx.spines[['top','right','left']].set_visible(False);bx.set_yticks([])
for j in range(3):
 y=2.1-j*.72
 bx.plot([j,j+1],[y,y],lw=13,color=['#26787d','#416bb5','#915c9e'][j],solid_capstyle='butt')
 bx.scatter([j,j+1],[y,y],s=65,facecolor='white',edgecolor='#18324c',zorder=4)
 bx.text(j+.5,y+.19,rf'$S_{j}=S_{{\min}}q_{{\rm shell}}^{j}$',ha='center',fontsize=13)
bx.set_xticks([0,1,2,3],['0','1','2','3'])
bx.set_xlabel(r'Display coordinate $\log(r/(A_S\sqrt{S_{\min}}))/\log(B_S/A_S)$',labelpad=10)
bx.set_title(r'Actual shells $[A_S\sqrt{S_j},\,B_S\sqrt{S_j}]$ with $q_{\rm shell}=(B_S/A_S)^2$',
 fontsize=17,pad=22,color='#102942')
fig.text(.5,.026,r'6.2–6.3: $(J+1)L_c\leq\|u(t_0)\|_3^3\leq U^3$. '
 'Interiors are disjoint; boundary spheres have zero volume.',
 ha='center',fontsize=13,color='#17446b')
for ext in ['png','svg']:
 fig.savefig(out/f'uniform-original-scale-annulus.{ext}',dpi=170,facecolor=fig.get_facecolor())
plt.close(fig)
