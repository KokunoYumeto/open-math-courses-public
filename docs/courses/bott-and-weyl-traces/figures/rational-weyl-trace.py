"""Draw the exact n=nu=1 Gaussian eigenvalues and trace norms in WT9."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
t=np.geomspace(.1,10,1201)
q=(1-t)/(1+t)
e0=(1+t)**-1
e1=e0*q
trace_norm=np.where(t<=1,(2*t)**-1,.5)
assert np.allclose(e0[0],1/(1+t[0]))
assert np.all(e1[t<1]>0) and np.all(e1[t>1]<0)
fig,axes=plt.subplots(1,2,figsize=(12.4,7.4))
fig.subplots_adjust(top=.76,bottom=.29,wspace=.28)
for ax in axes:
    ax.set_xscale('log');ax.axvline(1,color='#777777',lw=1,ls=':')
    ax.set_xlabel(r'$t>0$');ax.grid(alpha=.2)
axes[0].plot(t,e0,color='#326b96',lw=2.2,label=r'$\lambda_0(t)=(1+t)^{-1}$')
axes[0].plot(t,e1,color='#ac4d28',lw=2.2,label=r'$\lambda_1(t)=(1+t)^{-1}(1-t)/(1+t)$')
axes[0].axhline(0,color='#555555',lw=.8)
axes[0].set_title('Actual eigenvalues, including the sign')
axes[0].set_ylabel('Eigenvalue');axes[0].legend(loc='upper right',fontsize=10)
axes[1].plot(t,trace_norm,color='#326b96',lw=2.2,label=r'$\|T_t\|_1$')
axes[1].plot(t,e0,color='#ac4d28',lw=1.8,ls='--',label=r'$\|T_t\|=(1+t)^{-1}$')
axes[1].set_yscale('log');axes[1].set_ylabel('Operator norm or trace norm')
axes[1].set_title(r'Exact trace norm: $(2t)^{-1}$ then $1/2$')
axes[1].legend(loc='upper right',fontsize=11)
fig.suptitle('The same rational Weyl symbol is trace class exactly when M > n',fontsize=18,y=.96)
fig.text(.5,.835,r'$T_t=(e^{-t(|x|^2+|\xi|^2)})^w,\qquad n=\nu=1,\qquad q_t=(1-t)/(1+t)$',ha='center',fontsize=16)
fig.text(.5,.205,r'$a_M^w=\Gamma(M)^{-1}\int_0^\infty t^{M-1}e^{-t}(T_t\otimes I_\nu)\,dt$',ha='center',fontsize=16)
fig.text(.5,.13,r'The full small-$t$ trace-norm integrand is $\nu\,2^{-n}\Gamma(M)^{-1}t^{M-n-1}e^{-t}$.',ha='center',fontsize=14)
fig.text(.5,.065,'WT7–WT10 prove the kernel, every eigenvalue and the trace-norm integral. WT11 proves necessity.\nThe plotted case is exact; the complete WT7–WT11 proof covers every n and nu.',ha='center',fontsize=10.5)
fig.savefig(P/'rational-weyl-trace.svg')
fig.savefig(P/'rational-weyl-trace.png',dpi=160)
