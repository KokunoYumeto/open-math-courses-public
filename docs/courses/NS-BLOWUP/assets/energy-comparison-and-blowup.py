"""Exact energy, comparison and blowup implications, EC0–EC7. CC0."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(15,17),dpi=100)
fig.patch.set_facecolor('#f6f8fb');ax.set_xlim(0,15);ax.set_ylim(0,17);ax.axis('off')
ink='#142c44';blue='#dcebf8';green='#e0eee6';gold='#f7ebd9'
ax.text(7.5,16.52,'Energy, comparison and actual blowup',ha='center',fontsize=27,color=ink,weight='bold')
ax.text(7.5,16.08,'The same velocity, pressure, force and zero initial datum throughout',ha='center',fontsize=15,color=ink)
def box(y,h,title,lines,color,size=15):
    ax.add_patch(FancyBboxPatch((.45,y),14.1,h,boxstyle='round,pad=0.10,rounding_size=0.15',facecolor=color,edgecolor='#8aa2b5'))
    ax.text(.72,y+h-.35,title,fontsize=18,color=ink,weight='bold')
    for k,line in enumerate(lines):ax.text(.75,y+h-.87-k*.40,line,fontsize=size,color=ink)
def arrow(y):ax.annotate('',xy=(7.5,y-.33),xytext=(7.5,y+.04),arrowprops=dict(arrowstyle='->',color='#335c7b',lw=2))
box(13.55,1.95,'Actual force and full energy identity  |  LF0–LF5; EC0',[
    r'$f\in C_c^\infty,\quad u(0)=0,\quad \frac{1}{2}\frac{d}{dt}\|u\|_2^2+\|\nabla u\|_2^2=\langle f,u\rangle$',
    r'$\|u(t)\|_2^2+2\int_0^t\|\nabla u\|_2^2\,ds\leq\left(\int_0^t\|f\|_2\,ds\right)^2$',
    'Energy and total dissipation stay finite up to time one.'],blue)
arrow(13.4)
box(10.3,2.85,'Whole-space comparison with the exact pressure terms  |  EC1–EC2',[
    r'$w=v-u,\quad g_{ij}=w_iw_j+w_iu_j+u_iw_j,\quad \nabla\pi=\nabla\sum_{i,j}R_iR_jg_{ij}$',
    r'$\chi_R=\varphi(x/R)^8,\quad E_R=\int\chi_R|w|^2,\quad A_R^2=\int\chi_R|\nabla w|^2$',
    r'$\frac{1}{2}E_R^{\prime}+\frac{1}{2}A_R^2\leq\|\nabla u\|_{\mathrm{op},\infty}E_R+C_TR^{-4/3}$',
    r'Retained Young remainders: $R^{-4},\ R^{-4/3},\ R^{-14/5}$.',
    'Same initial velocity gives w = 0; no pressure-growth assumption is added.'],green)
arrow(10.15)
box(7.7,2.2,'The actual Cartesian growth path  |  EC3',[
    r'$x_\tau=(\sqrt{2X_{\rm in}\tau},0,0),\quad t_\tau=1-\tau$',
    r'$u_\theta(x_\tau,1-\tau)=\tau^{-A}\{e_0+O(\tau^{2h})\},\quad e_0>0$',
    'A global smooth bounded-energy competitor would coincide with this field.',
    'The growing component contradicts boundedness near the point (0, 1).'],gold)
arrow(7.55)
box(4.55,2.75,'Every positive viscosity and the exact periodic clock  |  EC4–EC5',[
    r'$u_\nu(x,t)=\sqrt{\nu}\,u(x/\sqrt{\nu},t),\quad p_\nu=\nu p(x/\sqrt{\nu},t),\quad f_\nu=\sqrt{\nu} f(x/\sqrt{\nu},t)$',
    r'$t_0=1-\lambda^{-2},\quad \widetilde u=\lambda u_\nu(\lambda x,\lambda^2(t-t_0))$',
    r'$\widetilde p=\lambda^2p_\nu(\lambda x,\lambda^2(t-t_0)),\quad \widetilde f=\lambda^3f_\nu(\lambda x,\lambda^2(t-t_0))$',
    r'$\lambda^{-1}\mathcal{K}_\nu\subset(-1/4,1/4)^3$ gives disjoint translated supports.',
    'Periodize all three fields; every cross term vanishes and viscosity stays unchanged.'],blue,size=14)
arrow(4.4)
box(1.55,2.6,'Exact consequences of these maps  |  EC6–EC7',[
    r'$e^{-H_\nu(t)}\|w_\nu(t)\|_2^2+\nu\int_0^t e^{-H_\nu(s)}\|\nabla w_\nu(s)\|_2^2\,ds\leq\|w_\nu(0)\|_2^2$',
    r'$H_\nu(t)=2\int_0^t\|\nabla u_\nu(s)\|_{\mathrm{op},\infty}\,ds$',
    r'$\int_0^\infty\|F_{\rm per}(t)\|_2\,dt=\lambda^{-1/2}\nu^{5/4}\int_0^\infty\|f(s)\|_2\,ds$',
    'Integrated force can be arbitrarily small; the full derivative scaling remains.',
    'Formal statement maps retain energy, periodic pressure and every decay exponent.'],green,size=14)
ax.text(7.5,.88,'Every arrow refers to the complete proofs in the lesson.',ha='center',fontsize=14,color=ink)
ax.text(7.5,.45,'Sources: OpenAI, Lemmas 10.4–10.5, Theorem 1.1 and Corollary 10.6; Stein (1970).',ha='center',fontsize=12,color=ink)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(P/'energy-comparison-and-blowup.svg');fig.savefig(P/'energy-comparison-and-blowup.png');plt.close(fig)
p=P/'energy-comparison-and-blowup.svg'
p.write_text(re.sub(r'width="1080pt" height="1224pt"','width="1500" height="1700"',p.read_text(encoding='utf8')),encoding='utf8')
