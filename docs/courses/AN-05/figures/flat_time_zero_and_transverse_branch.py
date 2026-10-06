"""An exact flat time curve, transverse zero branch and finite bracket tree; CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':11})
fig=plt.figure(figsize=(14,10),dpi=150,facecolor='#fffdfa')
ink='#193249';muted='#4b5867';blue='#4389b7';green='#497a64';purple='#865987'
fig.text(.045,.955,'An infinitely flat time zero can still have finite bracket type',fontsize=20,weight='bold',color=ink)
fig.text(.045,.915,r'$p=\tau+iq,\quad q=t^2\eta_2+\eta_3(t^5x_2^2+f(t)),\quad f(t)=\mathrm{sgn}(t)e^{-1/t^2},\ f(0)=0,\quad\eta_3>0$',fontsize=13,color=ink)
fig.text(.045,.884,'Exact normalized homogeneous model; the two plots are the labelled slice x₂ = 0, η₃ = 1, v = η₂.',fontsize=11,color=muted)
fig.text(.045,.852,'Marked point c: (t, x₂, x₃; τ, η₂, η₃) = (0, 0, 0; 0, 0, 1).',fontsize=11,color=muted)
t=np.linspace(-.8,.8,801)
def flat(t):
    result=np.zeros_like(t,dtype=float)
    nz=t!=0
    result[nz]=np.sign(t[nz])*np.exp(-1/t[nz]**2)
    return result
f=flat(t);a=np.zeros_like(t);nz=t!=0;a[nz]=-f[nz]/t[nz]**2
ax=fig.add_axes([.08,.39,.39,.39],facecolor='#fffdfa')
ax.fill_between(t,a,.4,color='#e4f1f8')
ax.fill_between(t,-.4,a,color='#f5e8e8')
ax.plot(t,a,color=blue,lw=2.5,label=r'$v=a(t)=-f(t)/t^2\ (t\ne0)$')
ax.axvline(0,color=purple,ls='--',lw=1.7,label=r'$t=0:\ q=0\ \mathrm{for\ every}\ v$')
ax.axhline(0,color=ink,lw=1.3)
ax.text(.08,.035,r'$v=0:\ q=f(t)$',color=ink,fontsize=10.5)
ax.set_xlim(-.8,.8);ax.set_ylim(-.4,.4);ax.set_xlabel(r'$t$');ax.set_ylabel(r'$v=\eta_2$')
ax.set_title('The characteristic zero set on this slice',fontsize=13,weight='bold',pad=16)
ax.text(.46,.26,r'$q>0$',color=ink,fontsize=13)
ax.text(-.63,-.27,r'$q<0$',color=ink,fontsize=13)
ax.grid(alpha=.2)
ax.legend(loc='lower center',bbox_to_anchor=(.5,-.31),frameon=False,fontsize=10)
for spine in ax.spines.values():spine.set_color('#bdc7ce')
curve=fig.add_axes([.60,.46,.34,.32],facecolor='#fffdfa')
curve.plot(t,f,color=green,lw=2.5)
curve.axhline(0,color='#9daab3',lw=1);curve.axvline(0,color='#9daab3',lw=1)
curve.set_xlim(-.8,.8);curve.set_ylim(-.23,.23)
curve.set_xlabel(r'$t$');curve.set_ylabel(r'$q(t,0)=f(t)$')
curve.set_title('Every pure time jet is zero at the origin',fontsize=12.5,weight='bold',pad=16)
curve.text(-.70,-.16,'negative',color=green,fontsize=11)
curve.text(.36,.145,'positive',color=green,fontsize=11)
curve.grid(alpha=.2)
for spine in curve.spines.values():spine.set_color('#bdc7ce')
fig.text(.60,.379,r'$a\,{}^\prime(t)=-[f\,{}^\prime(t)-2f(t)/t]/t^2<0\quad(0<|t|<1)$',fontsize=11.5,color=ink)
fig.text(.60,.335,'The zero limit of a(t) and the characteristic slope',fontsize=10.5,color=muted)
fig.text(.60,.306,'force q(t, 0) ≤ 0 to the left and ≥ 0 to the right.',fontsize=10.5,color=muted)
fig.text(.08,.264,'Curves are sampled for display. They have no zero interval; the formulas specify their flat behavior.',fontsize=9.5,color=muted)
box=FancyBboxPatch((.045,.115),.91,.125,transform=fig.transFigure,boxstyle='round,pad=.008',facecolor='#f4f7f8',edgecolor='#587a92',lw=1.3)
fig.add_artist(box)
fig.text(.5,.211,r'$Q_j=\partial_t^j q:\quad\{Q_2,\{Q_2,Q_5\}\}(c)=960,\quad3+3+6=12\ \mathrm{leaves}$',ha='center',fontsize=13,color=ink)
fig.text(.5,.168,'Weights (t, τ; x₂, η₂; x₃, η₃ − 1) = (1, 11; 3, 9; 6, 6): every canonical pair sums to 12.',ha='center',fontsize=10.5,color=ink)
fig.text(.5,.133,'Every word through eleven leaves vanishes; this twelve-leaf tree does not. Full bracket depth is eleven.',ha='center',fontsize=10.5,color=ink)
fig.text(.045,.068,'Exact proof: Lemmas3.1,4.1; Exercises2–3,(7.1)–(7.3). The vertical zero line is part of the zero set,not an omitted branch.',fontsize=9,color=muted)
fig.text(.045,.039,'Hörmander IV,Theorem27.1.11,pp170–171. Original mathematical example,figure and reproducible Python source;CC0.',fontsize=9,color=muted)
fig.savefig(Path(__file__).with_name('flat-time-zero-and-transverse-branch.png'),dpi=150)
