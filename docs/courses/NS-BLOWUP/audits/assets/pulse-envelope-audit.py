"""Display the exact scalar envelope and proved bounds, not a numerical proof.

Source: OpenAI, Finite Time Blowup for Navier-Stokes, (7.2), (7.12), (7.16).
Proof: pulse-inverse-audit.md, P0 and P3. The chosen scalar parameters do not
purport to be an instantiated global Navier-Stokes construction.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
u=2.; lam=1.; L=40.
v=np.linspace(0,L,601); y=u/2+u*v/L
logp=lam*L/u*(np.arcsinh(y)-np.arcsinh(u)-(y+y**3/3-u-u**3/3)/(1+u*u)**1.5)
cminus=lam*u*u/2*((1+9*u*u/4)**-1.5+2*(1+u*u)**-1.5)
cplus=3*lam*u*u/2*((1+u*u/4)**-1.5+2*(1+u*u)**-1.5)
lower=-cplus*(v-L/2)**2/(2*L);upper=-cminus*(v-L/2)**2/(2*L)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(11.8,7.4),dpi=150)
fig.patch.set_facecolor('#f7fafc');ax.set_facecolor('white')
ax.fill_between(v,lower,upper,color='#b8d9eb',alpha=.48,label='Proved quadratic bounds (P3.5)')
ax.plot(v,logp,color='#163e5b',lw=2.7,label=r'Exact $\log P(v)$ from P3.2')
ax.plot(v,lower,color='#8aa6b6',lw=1.2,ls='--')
ax.plot(v,upper,color='#8aa6b6',lw=1.2,ls='--')
ax.axvline(L/2,color='#657887',lw=1,ls=':')
ax.axvspan(0,L/2-L/5,color='#eac7ad',alpha=.20)
ax.axvspan(L/2+L/5,L,color='#eac7ad',alpha=.20)
ax.scatter([L/2],[0],color='#163e5b',zorder=5,s=34)
ax.annotate(r'$P(L_s/2)=1,\quad P^\prime(L_s/2)=0$',xy=(L/2,0),xytext=(21,-2.5),
            fontsize=12,arrowprops={'arrowstyle':'->','color':'#163e5b'})
ax.set_xlim(0,L);ax.set_ylim(min(lower)-.6,.6)
ax.set_xlabel(r'Original pulse coordinate $v$');ax.set_ylabel(r'$\log P(v)$')
ax.grid(alpha=.16);ax.spines[['top','right']].set_visible(False)
ax.legend(loc='lower center',frameon=True,fontsize=11)
fig.suptitle('The original phase coefficient gives a pulse centered at the midpoint',x=.07,ha='left',fontsize=17,weight='bold')
fig.text(.07,.915,r'Scalar example: $\lambda_0=1,\ u_*=2,\ L_s=40$.  Original (7.2) has numerator $\lambda_0$.',fontsize=12)
fig.text(.07,.095,r'Brown regions: $|v-L_s/2|\geq L_s/5$, where the cutoff error may remain.',fontsize=11)
fig.text(.07,.060,r'Bounds are proved analytically in P3.3-P3.5; the curve is evaluated only for display.',fontsize=11)
fig.text(.07,.025,'Source: OpenAI, Finite Time Blowup for Navier-Stokes, (7.2), (7.12), (7.16).',fontsize=10,color='#42566b')
fig.subplots_adjust(left=.08,right=.965,bottom=.20,top=.86)
fig.savefig(out/'pulse-envelope-audit.png',dpi=150)
fig.savefig(out/'pulse-envelope-audit.svg')
plt.close(fig)
print(out/'pulse-envelope-audit.png')
