"""Exact formal trace and n=2 scalar cutoff-defect sample, FC10 and EP1--EP2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,9),facecolor='#f8fafc')
fig.text(.06,.95,'The complete formal trace and the compact Chern defect',
         fontsize=21,weight='bold',color='#0f172a')
panel=fig.add_axes([.06,.69,.88,.20]);panel.axis('off')
panel.add_patch(FancyBboxPatch((0,.02),1,.94,boxstyle='round,pad=.015,rounding_size=.03',
                 fc='white',ec='#2563eb',lw=1.5,transform=panel.transAxes))
panel.text(.025,.79,'Coefficientwise compact relative projector: support inside the original K',
           fontsize=14,weight='bold',color='#1e40af',transform=panel.transAxes)
panel.text(.025,.49,r'$\tau_{2\nu}(e_\infty-e_0)=(2\pi)^n\lambda^n\,\mathrm{ind}\,a^w$',
           fontsize=23,color='#0f172a',transform=panel.transAxes)
panel.text(.025,.22,r'$T_m=0\ (m\ne n),\qquad T_n=(2\pi)^n\,\mathrm{ind}\,a^w,\qquad\hbar=\lambda/i$',
           fontsize=15,color='#334155',transform=panel.transAxes)
panel.text(.025,.06,'Every coefficient proved by a finite expansion: FC5–FC11. No analytic series convergence.',
           fontsize=11,color='#475569',transform=panel.transAxes)

t=np.linspace(0,1,1001)
dc=4*t**3*(1-t**2)
da=4*t**2*(1-t)
w=-4*t**3/3+2*t**4-2*t**6/3
ax=fig.add_axes([.08,.27,.39,.32],facecolor='white')
ax.plot(t,dc,color='#2563eb',lw=2.7,label=r'$d_C(t)=4t^3(1-t^2)$')
ax.plot(t,da,color='#c2410c',lw=2.7,label=r'$d_A(t)=4t^2(1-t)$')
ax.set_xlim(0,1);ax.set_ylim(0,.82)
ax.set_xlabel(r'$t=1-\psi$ (dimensionless cutoff coordinate)')
ax.set_ylabel('Scalar coefficient')
ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=12,framealpha=.95)
fig.text(.08,.62,'Exact n = 2 coefficients of the two four-forms',
         fontsize=14,weight='bold',color='#0f172a')
fig.text(.08,.17,r'$\int_0^1d_C(t)\,dt=\int_0^1d_A(t)\,dt=1/3$',
         fontsize=16,color='#0f172a')
fig.text(.08,.13,r'Both multiply the unchanged $dt\wedge\mathrm{tr}\,\theta^3$.',
         fontsize=11,color='#475569')

bx=fig.add_axes([.57,.27,.35,.32],facecolor='white')
bx.plot(t,w,color='#7c3aed',lw=2.7)
bx.axhline(0,color='#64748b',lw=.8)
bx.plot([0,1],[0,0],'o',color='#7c3aed',ms=6)
bx.text(.02,-.105,'t = 0: order 3',color='#6d28d9',ha='left',va='top',fontsize=11)
bx.text(.98,-.105,'t = 1: order 2',color='#6d28d9',ha='right',va='top',fontsize=11)
bx.set_xlim(0,1);bx.set_ylim(-.15,.012)
bx.set_xlabel(r'$t=1-\psi$')
bx.set_ylabel(r'$W_2(t)$')
bx.grid(alpha=.2)
fig.text(.57,.62,'The full compact-primitive scalar factor',
         fontsize=14,weight='bold',color='#0f172a')
fig.text(.57,.17,r'$W_2(t)=-\frac{2}{3}t^3(1-t)^2(t+2)$',
         fontsize=17,color='#0f172a')
fig.text(.57,.13,r'$W_2^\prime=d_C-d_A$, with both endpoint values zero.',
         fontsize=11,color='#475569')

fig.text(.06,.075,'Outward boundary coefficient at n = 2: −1/3, in the original interleaved orientation (CP13).',
         fontsize=12,color='#334155')
fig.text(.06,.045,'Lower plots are scalar coefficient samples, not numerical operators. Complete proofs: CX1–CX5 and EW1–EP2.',
         fontsize=10.5,color='#475569')
fig.text(.06,.018,'Reproducible original programme calculation. No novelty claim and no external theorem used.',
         fontsize=10,color='#64748b')
for extension in ('png','svg'):
    fig.savefig(OUT/f'relative-projector-complete-formal-trace.{extension}',dpi=180,
                facecolor=fig.get_facecolor(),metadata={'Creator':'Matplotlib programme figure'} if extension=='svg' else {})
plt.close(fig)
