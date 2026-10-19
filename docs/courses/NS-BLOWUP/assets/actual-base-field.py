"""Reproduce the exact base-field operators and axis identity, Z0–Z9."""
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'path'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,12.8),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,14);ax.set_ylim(0,12.8);ax.axis('off')
ink='#19354c';blue='#206798';green='#177368'
ax.text(.35,12.38,'The actual base: full cutoff curl and exact residual',fontsize=23,color=ink)
ax.text(.35,12.02,'One coefficient sequence • one cutoff sequence • every fixed derivative',fontsize=16,color=ink)
def panel(y,h,title,color,face):
    ax.add_patch(FancyBboxPatch((.4,y),13.2,h,boxstyle='round,pad=0.02,rounding_size=.08',
        facecolor=face,edgecolor='#c4d4df'))
    ax.text(.6,y+h-.37,title,fontsize=16,weight='bold',color=color)
panel(9.15,2.48,'1. THE POTENTIAL AND ITS COMPLETE CUTOFF CURL — Z2, Z9.1–Z9.4',blue,'#e5eff7')
ax.text(.65,10.7,r'$S_n=q^{1-A+2nh}F_n,\qquad\mathcal{A}_n=(S_n/r)e_\theta$',fontsize=22,color=ink)
ax.text(.65,10.12,r'$u_n^{\rm cut}=\operatorname{curl}(\chi(c_nq)\mathcal{A}_n)+\chi(c_nq)u_{\theta,n}e_\theta$',fontsize=22,color=ink)
ax.text(.65,9.52,r'$ru_{r,n}^{\rm cut}=q^{2nh}\left[\chi(c_nq)V_n-\frac{2\eta}{L}(c_nq)\chi^\prime(c_nq)F_n\right]$',fontsize=22,color=ink)
panel(6.35,2.48,'2. ONE FIXED FINITE SUM CONTROLS THE ACTUAL RESIDUAL — Z3–Z5',green,'#e4f2ec')
ax.text(.65,7.92,r'$c_n=1+\left\lceil\max\{2c_{n-1},2,(2^nM_n)^{1/(nh)}\}\right\rceil$',fontsize=22,color=ink)
ax.text(.65,7.32,r'$|\mathcal{U}_B-\mathcal{U}^{[J]}|_m\leq2^{-J}q^{h(J+1)-(2A+m+1)}\quad(0<q<(2c_J)^{-1},\ J\geq\max\{1,m\})$',fontsize=18,color=ink)
ax.text(.65,6.72,'Choose derivative and decay orders, then a finite J, then its q neighborhood.',fontsize=17,color=ink)
panel(3.55,2.48,'3. EVERY RESIDUAL TERM REMAINS — Z5.1, Z9.5–Z9.8',blue,'#e5eff7')
ax.text(.65,5.12,r'$\partial_te-\Delta e+\nabla\pi+(v\cdot\nabla)e+(e\cdot\nabla)v+(e\cdot\nabla)e$',fontsize=21,color=ink)
ax.text(.65,4.53,r'$\quad+(\partial_r+2/r)\tau_\theta e_\theta+(\partial_r+1/r)\tau_z e_z$',fontsize=21,color=ink)
ax.text(.65,3.94,r'$|\mathcal{E}_B|_m\leq C_{m,M}q^M\quad$ for every fixed m and M.',fontsize=21,color=ink)
panel(.77,2.48,'4. EXACT AXIS IDENTITY AT THE ORIGINAL VISCOSITY — Z9.13–Z9.17',green,'#fff0e4')
ax.text(.65,2.35,r'$\mathcal{E}_{B,\nu}|_{\rm axis}=-\sqrt{\nu}[1-\chi(c_1q_\nu)]q_\nu^{-A-2D}$',fontsize=22,color=ink)
ax.text(4.15,1.85,r'$\times\,(\mathscr{Z}_{c-D}\mathscr{Z}_cU_*)(\eta_\nu)e_z$',fontsize=22,color=ink)
ax.text(.65,1.23,r'$q_\nu\leq(2c_1)^{-1}:\quad\mathcal{E}_{B,\nu}|_{\rm axis}=0,\qquad u_{B,\nu}|_{\rm axis}=\sqrt{\nu}q_\nu^{-A}(4\eta_\nu+j_0)e_z$',fontsize=19,color=ink)
ax.text(.4,.39,'Source: OpenAI, pp.55–62, Propositions5.3,5.5. Full proof: N3.3 Z0–Z9. No numerical field is sampled.',fontsize=11,color=ink)
ax.text(.4,.14,'M_n contains the finite norms proved in Z3. The axis identity does not assert zero residual off the axis. CC0 figure source.',fontsize=11,color=ink)
fig.savefig(out/'actual-base-field.svg',facecolor=fig.get_facecolor())
svg=out/'actual-base-field.svg'
t=svg.read_text(encoding='utf8')
t=re.sub(r'(<svg\b[^>]*?)width="[^"]+" height="[^"]+"',r'\1width="1400" height="1280"',t,count=1)
svg.write_text(t,encoding='utf8')
fig.savefig(out/'actual-base-field.png',dpi=100,facecolor=fig.get_facecolor())
plt.close(fig)
