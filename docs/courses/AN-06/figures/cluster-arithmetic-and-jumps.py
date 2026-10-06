"""Exact proof diagram for U027 Corollaries 4.2, 4.3 and 5.3. CC0."""
from pathlib import Path
from math import gcd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

matplotlib.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'svg.hashsalt':'AN06-cluster-arithmetic-v1'})
out=Path(__file__).resolve().parent
fig=plt.figure(figsize=(8,14),facecolor='white')
gs=fig.add_gridspec(4,1,height_ratios=[2.7,1.6,3.4,2.0],hspace=.52,left=.13,right=.96,top=.91,bottom=.075)
fig.suptitle('Arithmetic constraints and counting jumps',fontsize=23,y=.977)
ax=fig.add_subplot(gs[0]);ax.set_axis_off()
ax.add_patch(FancyBboxPatch((.01,.04),.98,.92,boxstyle='round,pad=.02',transform=ax.transAxes,facecolor='#edf4fa',edgecolor='#9bb2c6'))
lines=[r'$d=n-1,\quad a=nV/\Pi^n$',
       r'$v_0(k)=\sum_{r=0}^{d} A_r\binom{k}{r},\quad A_r\in\mathbb{Z}$',
       r'$A_d=d!a=D=n!V/\Pi^n>0$',
       r'$A_{d-1}=D[(n-2)/2-c/h]$',
       r'$c/h=\alpha/4+\ell\quad\Longrightarrow\quad4\mid D(2n-4-\alpha)$']
for y,t in zip([.83,.65,.47,.29,.11],lines):ax.text(.5,y,t,ha='center',va='center',fontsize=17,transform=ax.transAxes)
ax=fig.add_subplot(gs[1]);ax.set_axis_off()
factors=[4//gcd(4,r) for r in range(4)]
assert factors==[1,4,2,4]
ax.add_patch(FancyBboxPatch((.01,.07),.98,.73,boxstyle='round,pad=.02',transform=ax.transAxes,facecolor='#edf4fa',edgecolor='#9bb2c6'))
ax.text(.035,.62,r'$2n-4-\alpha$ (mod 4)',va='center',fontsize=14,transform=ax.transAxes)
ax.text(.035,.27,r'$D$ is a multiple of',va='center',fontsize=14,transform=ax.transAxes)
for x,r,factor in zip([.54,.67,.80,.93],range(4),factors):
    ax.text(x,.62,str(r),ha='center',va='center',transform=ax.transAxes)
    ax.text(x,.27,str(factor),ha='center',va='center',transform=ax.transAxes)
ax.text(.5,.96,'Necessary conditions; no realization claim',ha='center',transform=ax.transAxes,fontsize=16)
ax=fig.add_subplot(gs[2]);ax.plot([-1,0],[0,0],color='#1b71a7',lw=3);ax.plot([0,1],[1,1],color='#1b71a7',lw=3)
ax.scatter([0,0],[0,1],s=90,facecolors='white',edgecolors='#1b71a7',linewidths=2,zorder=5)
ax.axhline(.5,color='#4a8b52',ls='--',lw=2)
ax.annotate('',xy=(.08,0),xytext=(.08,.5),arrowprops={'arrowstyle':'<->','color':'#b64c21','lw':2})
ax.annotate('',xy=(.08,.5),xytext=(.08,1),arrowprops={'arrowstyle':'<->','color':'#b64c21','lw':2})
ax.text(.15,.25,r'$1/2$',va='center',color='#b64c21');ax.text(.15,.75,r'$1/2$',va='center',color='#b64c21')
ax.text(-.94,.57,'best common limiting value',color='#37743e',fontsize=15)
ax.set(xlim=(-1,1),ylim=(-.16,1.2),xticks=[-.8,0,.8],xticklabels=['below $hk$','$hk$','above $hk$'],yticks=[0,.5,1])
ax.set_ylabel('counting jump divided by its size')
ax.set_title(r'Jump size $\mu(k)\sim ak^{n-1}$',fontsize=19,pad=12)
ax.spines[['top','right']].set_visible(False)
ax.text(.5,-.24,r'$\max(|e_-|,|e_+|)\geq\mu(k)/2$',ha='center',transform=ax.transAxes,fontsize=20)
ax=fig.add_subplot(gs[3]);ax.set_axis_off()
ax.add_patch(FancyBboxPatch((.01,.08),.98,.82,boxstyle='round,pad=.02',transform=ax.transAxes,facecolor='#fff3e9',edgecolor='#c7ab92'))
ax.text(.5,.73,'Fixed polynomial moment: exact quotient bound',ha='center',transform=ax.transAxes,fontsize=17)
ax.text(.5,.46,r'$|\mathrm{Tr}(f(B)|_{V_k})/\mu(k)-m_f|\leq\frac{2(C_f+|m_f|C_0)}{ak}$',ha='center',transform=ax.transAxes,fontsize=17)
ax.text(.5,.18,r'For sufficiently large $k\geq2C_0/a$; $a>0$',ha='center',transform=ax.transAxes,fontsize=16)
fig.text(.5,.018,'U027 Corollaries 4.2–4.3 and 5.3; Theorem 4.1; Solution 9.1.\nExact coefficients and bounds. Jump panel shows the best midpoint value. CC0.',ha='center',fontsize=12)
fig.savefig(out/'cluster-arithmetic-and-jumps.png',dpi=180,metadata={'Software':'Matplotlib; independently authored AN06 proof diagram'})
fig.savefig(out/'cluster-arithmetic-and-jumps.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Description':'Exact U027 Newton, jump and fixed-polynomial bounds; no geometric realization claim.'})
plt.close(fig)
