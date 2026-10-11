"""Original annular supports and exact pump energy map; CC1–CC22."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
P=Path(__file__).resolve().parent
epsilon=1/8;q=1+epsilon;L=1-2*epsilon;U=1+2*epsilon
fig,(ax,bx)=plt.subplots(1,2,figsize=(15,7),gridspec_kw={'width_ratios':[1,1.45]})
fig.subplots_adjust(top=.84,bottom=.22,wspace=.25)
records=[]
for n in range(-2,3):
 lower=L*q**n;upper=U*q**n
 ax.plot([lower,upper],[n,n],lw=8,solid_capstyle='butt',color='#237b89',alpha=.8)
 ax.plot([lower,upper],[n,n],'|',color='#174c61',markersize=17)
 records.append(dict(n=n,lower=lower,upper=upper))
ax.set(xlabel=r'Original source Fourier radius $|\xi|$',ylabel=r'Original integer scale $n$',yticks=range(-2,3),ylim=(-2.6,2.6))
ax.grid(alpha=.17);ax.set_title(r'Actual annuli: $\epsilon_0=1/8$, $q=9/8$'+'\n'+r'$A_n=[(3/4)q^n,(5/4)q^n]$')
bx.set(xlim=(0,10),ylim=(0,7));bx.axis('off')
for x,label in [(0.2,r'$\frac{c_1(t)^2}{2A}$'+'\n'+r'$=\frac{a^2A}{2}\operatorname{sech}^2(\kappa t)$'),(6.2,r'$\frac{c_2(t)^2}{2B}$'+'\n'+r'$=\frac{a^2A}{2}\tanh^2(\kappa t)$')]:
 bx.add_patch(FancyBboxPatch((x,4.1),3.5,1.6,boxstyle='round,pad=.08',facecolor='#e8f1f4',edgecolor='#174c61',lw=2))
 bx.text(x+1.75,4.9,label,ha='center',va='center',fontsize=14,linespacing=1.6)
bx.annotate('',xy=(6.1,4.9),xytext=(3.9,4.9),arrowprops=dict(arrowstyle='->',color='#12858a',lw=2.5))
bx.text(5,5.5,r'$k\,c_1(t)^2c_2(t)$',ha='center',fontsize=14,color='#12858a')
bx.text(5,6.6,'Exact energy transfer at one original scale',ha='center',fontsize=14)
bx.text(5,3.25,r'$A=\|\phi_1\|_2^2,\quad B=\|\phi_2\|_2^2,\quad k=q^{5n_*/2}$',ha='center',fontsize=13)
bx.text(5,2.6,r'$\kappa=kaA\sqrt{AB},\qquad \|u(t)\|_2^2=a^2A$',ha='center',fontsize=14)
bx.text(5,1.65,r'$f=C_{\rm pump}(u,u)-B(u,u)-\nu\Delta u$',ha='center',fontsize=14)
bx.text(5,.9,r'$\langle f,u\rangle=\nu\|\nabla u\|_2^2$',ha='center',fontsize=14)
bx.text(5,.15,'Complete transfer occurs only as t tends to infinity.',ha='center',fontsize=11)
fig.suptitle('The original local cascade: retained supports and a fully constructed pump',fontsize=18)
fig.text(.5,.14,'Left: five exact support intervals; all integer scales remain in the proof. No Fourier weight is replaced.',ha='center',fontsize=11)
fig.text(.5,.09,'Right: the two energy contributions and original force. The diagram states proved formulas; it does not plot a simulated trajectory.',ha='center',fontsize=11)
fig.text(.5,.04,'Complete proofs CC1–CC22. Human source: Tao, arXiv:1402.0290v3, original local-cascade definition at lines 450–474.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(P/f'original-local-cascade-and-pump.{ext}',dpi=160)
(P/'original-local-cascade-and-pump-data.json').write_text(json.dumps(dict(epsilon_0=epsilon,q=q,L=L,U=U,annuli=records,diagram='Exact symbolic pump energies and original physical force; no sampled flow'),indent=2)+'\n',encoding='utf-8')
print('Rendered original local-cascade and pump figure.')
