"""Reproduce SG's spectral map and exact EX1–EX4 matrix examples.

Run beside the output assets. Figure one is a schematic spectral map with
explicit illustrative coordinates, not a computed fluid spectrum. Figure two
evaluates exact proved matrix formulas. Human comparison: Albritton, Brue and
Colombo, arXiv:2112.03116v1, main.tex2487–2633; full proofs in NS-FLUID-35.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.titlesize':15,'figure.titlesize':20,'svg.fonttype':'none'})
navy='#15375b';teal='#008592';orange='#bd6519';purple='#774596'
h=.8;w=.1;free=np.exp(-h/4);cut=np.exp(w*h)
fig,axs=plt.subplots(1,2,figsize=(14,7.5));fig.subplots_adjust(top=.83,bottom=.23,wspace=.3)
fig.suptitle('The original generator and one actual evolution step',y=.97)
ax=axs[0];ax.set_title('Generator plane: the finite spectral space')
ax.axvspan(-.65,-.25,color=purple,alpha=.1);ax.axvline(-.25,color=purple,ls='--',lw=2)
ax.axvline(w,color=teal,ls=':',lw=2);ax.axhline(0,color='#888',lw=.6)
ax.scatter([.7,.7],[.8,-.8],color=orange,s=60)
ax.text(.7,.91,r'$\lambda$',ha='center');ax.text(.7,-1.04,r'$\overline{\lambda}$',ha='center')
ax.text(-.25,-1.24,r'$-1/4$',ha='center',color=purple)
ax.text(w,-1.24,r'$w$',ha='center',color=teal)
ax.set(xlim=(-.65,1.15),ylim=(-1.4,1.4),xlabel=r'$\operatorname{Re}\lambda$',ylabel=r'$\operatorname{Im}\lambda$')
ax.grid(alpha=.15);ax.set_aspect('equal',adjustable='box')
ax=axs[1];ax.set_title(r'Evolution plane: $T=S(h)=E(h)+K_h$')
ax.add_patch(Circle((0,0),free,color=purple,alpha=.12))
ax.add_patch(Circle((0,0),free,fill=False,color=purple,ls='--',lw=2))
ax.add_patch(Circle((0,0),cut,fill=False,color=teal,ls=':',lw=2))
z=np.exp(h*(.7+.8j));ax.scatter([z.real,z.real],[z.imag,-z.imag],color=orange,s=60)
ax.text(z.real+.12,z.imag,r'$e^{h\lambda}$',va='center')
ax.text(z.real+.12,-z.imag,r'$e^{h\overline{\lambda}}$',va='center')
ax.plot([0,free],[0,0],color=purple,lw=2);ax.text(free*.4,.1,r'$e^{-h/4}$',color=purple,ha='center')
ax.text(-cut-.08,.2,r'$e^{wh}$',color=teal,ha='right')
ax.axhline(0,color='#888',lw=.6);ax.axvline(0,color='#888',lw=.6)
ax.set(xlim=(-1.65,2.35),ylim=(-1.6,1.6),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
ax.set_aspect('equal');ax.grid(alpha=.15)
fig.text(.5,.14,r'$F\subset D(L),\quad A_F=L|_F,\quad S(t)|_F=e^{tA_F}$',ha='center',fontsize=19,color=navy)
fig.text(.5,.085,'The finite generator fixes the logarithm branches. The complementary powers give the growth bound (SG9–SG17).',ha='center',fontsize=11)
fig.text(.5,.038,'Schematic coordinates: h = 0.8, w = 0.1, shown pair 0.7 ± 0.8i. No fluid eigenvalues are computed.',ha='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(OUT/f'original-velocity-spectral-growth.{ext}',dpi=160)
plt.close(fig)
a=.4;b=1.3;c=1.5;k=.8;delta=.2
tau=np.linspace(-3,2.5,441);t=np.linspace(0,10,501)
real=abs(c)*np.exp(a*tau)*np.sqrt(np.cos(b*tau)**2+4*np.sin(b*tau)**2)
low=abs(c)*np.exp(a*tau);high=2*low
star=np.sqrt(delta**-2-4/k**2)
pref=np.exp(-delta*star)*(np.sqrt(4+k*k*star*star)+k*star)/2
jordan=np.exp(a*t)*(np.sqrt(4+k*k*t*t)+k*t)/2
bound=pref*np.exp((a+delta)*t)
fig,axs=plt.subplots(1,2,figsize=(14,6.5));fig.subplots_adjust(top=.8,bottom=.2,wspace=.28)
fig.suptitle('Exact growth keeps the phase and the Jordan factor',y=.96)
ax=axs[0];ax.set_title('The real mode retains both phase components')
ax.fill_between(tau,low,high,color=teal,alpha=.1)
ax.plot(tau,real,color=navy,lw=2.5,label=r'$\|\operatorname{Re}(e^{(a+ib)\tau}\eta)\|$')
ax.plot(tau,low,color=teal,ls='--',label=r'$|c|e^{a\tau}$')
ax.plot(tau,high,color=teal,ls=':',label=r'$2|c|e^{a\tau}$')
ax.set(xlabel=r'Original time $\tau$',ylabel='Full real-vector norm');ax.legend(fontsize=11);ax.grid(alpha=.2)
ax=axs[1];ax.set_title('A positive margin has its exact best prefactor')
ax.semilogy(t,jordan,color=navy,lw=2.5,label=r'$\|e^{tJ}\|$')
ax.semilogy(t,bound,color=orange,ls='--',label=r'$M_\delta e^{(a+\delta)t}$')
ax.semilogy(t,np.exp(a*t),color='#777',ls=':',label=r'$e^{at}$')
touch=np.exp(a*star)*(np.sqrt(4+k*k*star*star)+k*star)/2
ax.scatter([star],[touch],color=orange,zorder=4)
ax.annotate(r'$t_*$',(star,touch),xytext=(star+.6,touch*.6),arrowprops={'arrowstyle':'->','color':orange},color=orange)
ax.set(xlabel='Original time t',ylabel='Full matrix operator norm');ax.legend(fontsize=11);ax.grid(alpha=.2)
fig.text(.5,.105,'Exact finite-dimensional examples EX1–EX4: a = 0.4, b = 1.3, c = 1.5, |κ| = 0.8, δ = 0.2.',ha='center',fontsize=11)
fig.text(.5,.052,'The vectors and matrices retain their actual amplitudes. These are examples of the proved mechanism, not fluid discretizations.',ha='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(OUT/f'original-real-mode-and-jordan-growth.{ext}',dpi=160)
plt.close(fig)
data={'scope':'Exact finite-dimensional examples; no computed fluid spectrum.','parameters':{'a':a,'b':b,'c':c,'kappa_abs':k,'delta':delta,'t_star':star,'M_delta':pref},'real_mode':[{'tau':float(x),'norm':float(y),'lower':float(l),'upper':float(u)} for x,y,l,u in zip(tau,real,low,high)],'jordan':[{'t':float(x),'norm':float(y),'bound':float(z)} for x,y,z in zip(t,jordan,bound)]}
(OUT/'original-velocity-growth-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
print(json.dumps({'figures':2,'samples':len(tau)+len(t),'M_delta':pref,'t_star':star}))
