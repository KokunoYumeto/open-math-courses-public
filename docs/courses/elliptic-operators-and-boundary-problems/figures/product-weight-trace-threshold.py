"""Draw the exact ordered product-metric trace factorization in PT15--PT21."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13.5,8.2))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.94,'The original product-weight trace threshold is N > n',ha='center',fontsize=20)
ax.text(.5,.845,r'$q\in S(h_G^N,G),\quad h_G=(\langle x\rangle\langle\xi\rangle)^{-1},\quad s=N/2>n/2$',ha='center',fontsize=17)
ax.text(.5,.75,r'$q^w=A_NB_N,\quad A_N=M_{-s}F_{-s},\quad B_N=F_sM_sq^w$',ha='center',fontsize=18)
nodes=[.10,.5,.9]
for x in nodes:ax.text(x,.59,r'$H_\nu$',ha='center',va='center',fontsize=24,bbox=dict(boxstyle='round,pad=.45',fc='#f0f4f7',ec='#45667d'))
for x1,x2 in zip(nodes[:-1],nodes[1:]):ax.annotate('',xy=(x2-.055,.59),xytext=(x1+.055,.59),arrowprops=dict(arrowstyle='->',lw=2,color='#326b96'))
ax.text(.30,.655,r'$B_N=(\langle\xi\rangle^s$ # $\langle x\rangle^s$ # $q)^w$',ha='center',fontsize=15)
ax.text(.70,.655,r'$A_N=M_{-s}F_{-s}$',ha='center',fontsize=16)
ax.text(.5,.48,r'$\|A_N\|_2^2=\nu(2\pi)^{-n}\int\langle x\rangle^{-N}dx\int\langle\xi\rangle^{-N}d\xi$',ha='center',fontsize=17)
ax.text(.5,.395,r'$\|B_N\|_2^2=(2\pi)^{-n}\int\mathrm{tr}(b_N^*b_N)\,dx\,d\xi,\quad b_N\in S(h_G^{N/2},G)$',ha='center',fontsize=16)
ax.text(.5,.305,r'$\|q^w\|_1\leq\|A_N\|_2\|B_N\|_2,\qquad q^wf\in D(M_s),\quad M_sq^wf\in D(F_s)$',ha='center',fontsize=16)
ax.text(.5,.215,'Both original n-dimensional integrals converge exactly for N > n.\nThe positive symbol hGᴺIν proves failure at and below N = n by its coherent-state integral.',ha='center',fontsize=12.5)
ax.text(.5,.13,'Bounded local smooth symbol convergence gives trace-norm convergence by PT20.\nThe two original radial error powers therefore work at N = n + 1; the earlier larger-power proof remains.',ha='center',fontsize=12)
ax.text(.5,.052,'PT15–PT21 prove all products, domains, Fourier and fiber factors, continuity and necessity.\nBoth original coordinate groups are retained.',ha='center',fontsize=10.5)
fig.savefig(P/'product-weight-trace-threshold.svg')
fig.savefig(P/'product-weight-trace-threshold.png',dpi=160)
