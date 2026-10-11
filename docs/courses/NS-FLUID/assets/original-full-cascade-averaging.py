"""Exact extension and all-scale averaging diagrams, with original coordinates."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12})
fig,ax=plt.subplots(figsize=(15,10),facecolor='white');ax.set(xlim=(0,15),ylim=(0,10));ax.axis('off')
def box(x,y,w,h):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor='#f1f7f8',edgecolor='#176b75',lw=1.8))
ax.text(7.5,9.55,'From the complete original fiber to actual Fourier multipliers',ha='center',fontsize=21)
ax.text(7.5,9.04,r'$0<\epsilon_0\leq1/1024,\quad |\xi_j-\xi_j^0|<2\epsilon_0^3,\quad |G_\xi(R(0))|<1/64,\quad 0\leq s\leq1$',ha='center',fontsize=13)
box(.4,7.47,6.4,1.28);box(8.25,7.47,6.3,1.28)
ax.text(3.6,8.34,r'$G_\xi(R)=R_1\xi_1+R_2\xi_2+R_3\xi_3$',ha='center',fontsize=16)
ax.text(3.6,7.78,r'$K=\sum_j(r_j^2I-y_jy_j^{\mathsf{T}})\geq I/16$',ha='center',fontsize=16)
ax.text(11.4,8.34,r'$G_\xi(R(s))=(1-s)G_\xi(R(0))$',ha='center',fontsize=15)
ax.text(11.4,7.78,r'$\Pi_\xi(R)=R(1)\in\Sigma_\xi$',ha='center',fontsize=17)
ax.add_patch(FancyArrowPatch((6.98,8.07),(8.08,8.07),arrowstyle='-|>',mutation_scale=19,color='#bd611e',lw=2))
ax.text(7.5,6.87,r'$\dot R_j=[-y_j\times K^{-1}G_\xi(R(0))]_\times R_j$',ha='center',fontsize=19)
box(.4,4.86,14.15,1.42)
ax.text(7.5,5.83,r'$\mathcal{E}(R,\xi)=\chi_1(\xi_1)\chi_2(\xi_2)\chi_3(\xi_3)\lambda(G_\xi(R))W_\xi(\Pi_\xi(R))$',ha='center',fontsize=16)
ax.text(7.5,5.28,r'$\mathcal{E}(R,\xi)=\int_{\mathbb{R}^9}\mathfrak{a}(R,x)\prod_{j=1}^3e^{2\pi i x_j\cdot\xi_j}\,dx$',ha='center',fontsize=18)
ax.text(7.5,4.27,'All 27 tensor components and every multiplier derivative moment are retained.',ha='center',fontsize=14)
ax.text(7.5,3.66,r'$d\mu=\|\mathfrak{a}(R,x)\|\,dR_1dR_2dR_3\,dx\quad$ on each original component copy',ha='center',fontsize=16)
ax.text(7.5,2.89,r'$m_{1,\omega}(\zeta)=\frac{f_\alpha(R,x)}{-\pi i}e^{2\pi i x_1\cdot R_1^{-1}\zeta}\overline{\widehat{\psi}_{1,\alpha_1}(R_1^{-1}\zeta)}$',ha='center',fontsize=19)
ax.text(7.5,2.05,r'$\mathcal{C}_0(u,v,w)=\int_\Omega\langle B(A_{1,\omega}u,A_{2,\omega}v),A_{3,\omega}w\rangle\,d\mu$',ha='center',fontsize=20)
ax.text(7.5,1.32,'The auxiliary rotation time s is not physical fluid time. Each original radius remains fixed.',ha='center',fontsize=12)
ax.text(7.5,.79,'AF1–AF27 prove the smooth retraction, compact extension, full Fourier inversion and exact Euler average.',ha='center',fontsize=11)
ax.text(7.5,.4,'Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex624–708. No numerical flow is represented.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,bottom=.01,top=.99)
for ext in ['png','svg']:fig.savefig(P/f'original-fiber-extension.{ext}',dpi=160,facecolor='white')
plt.close(fig)

e=1/1024;q=1+e
fig=plt.figure(figsize=(15,9),facecolor='white');grid=fig.add_gridspec(2,1,height_ratios=[1.2,1],hspace=.37)
bx=fig.add_subplot(grid[0])
bx.axvspan(1-20*e*e,1+20*e*e,color='#81c7b7',alpha=.65,label=r'Original allowed ratio: $|N_3/N_1-1|<20\epsilon_0^2$')
ratios=[]
for d in [-2,-1,0,1,2]:
 value=q**d;ratios.append(dict(index_difference=d,ratio=value))
 bx.plot(value,d,'o',markersize=9,color='#176b75' if d==0 else '#bd611e')
 bx.text(value+e*.09,d+.16,f'd = {d}',fontsize=11)
bx.axvline(1,color='#176b75',lw=.6)
bx.set_ylim(-2.5,2.7);bx.set_xlim(q**-2-e*.5,q**2+e*.7)
bx.set_xlabel(r'Original ratio $N_3/N_1$');bx.set_ylabel(r'Original index difference $d=n_3-n_1$')
bx.ticklabel_format(axis='x',style='p'+'lain',useOffset=False)
bx.set_yticks([-2,-1,0,1,2]);bx.legend(loc='upper left',fontsize=11)
bx.set_title(r'Central frequencies at $\epsilon_0=1/1024$: only equal indices enter the original ratio window',fontsize=14,pad=14)
cx=fig.add_subplot(grid[1]);cx.axis('off')
cx.text(.5,.94,r'$n_j\ne n_1\ \Longrightarrow\ |N_j/N_1-s_j|\geq\epsilon_0/4>20\epsilon_0^2$',ha='center',fontsize=19)
cx.text(.5,.67,r'$n_1=n_2=n_3=n:\qquad\int_\Omega\langle B_{\eta,\rho}(A_{1,n}u,A_{2,n}v),A_{3,n}w\rangle\,d\mu=q^{5n/2}\mathcal{C}_n(u,v,w)$',ha='center',fontsize=16)
cx.text(.5,.39,'Every original scale survives with its full coefficient; every mixed-scale term is zero.',ha='center',fontsize=14)
cx.text(.5,.12,r'$w\in\mathbb{R}^{\mathbb{Z}}:\quad C_{\rm pump}^{\,w}$ is an averaged Euler operator $\Longleftrightarrow\ \sup_{n\in\mathbb{Z}}|w_n|<\infty$',ha='center',fontsize=17)
fig.suptitle('The complete original scale sum and its exact weight criterion',fontsize=21,y=.98)
fig.subplots_adjust(left=.095,right=.96,top=.88,bottom=.16)
fig.text(.5,.088,'Points mark exact central ratios. AV15–AV20 prove separation for the full original caps, including their nonzero widths.',ha='center',fontsize=11)
fig.text(.5,.053,'AV1–AV35 and Exercise 4, EX14–EX19. Human source: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex559–622.',ha='center',fontsize=10)
fig.text(.5,.02,'This is frequency geometry and an operator classification; it is not a computed blowup trajectory.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(P/f'original-cascade-scale-selection.{ext}',dpi=160,facecolor='white')
(P/'original-cascade-scale-selection-data.json').write_text(json.dumps(dict(epsilon0=e,q=q,points=ratios,window=[1-20*e*e,1+20*e*e]),indent=2)+'\n',encoding='utf-8')
