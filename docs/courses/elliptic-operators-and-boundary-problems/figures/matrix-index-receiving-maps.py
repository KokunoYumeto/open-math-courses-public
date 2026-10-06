"""Render the exact central-lift and analytic coefficient maps in FC8 and AT1."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,9));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.95,'The complete connection lift and the original analytic coefficients',ha='center',fontsize=20)
ax.text(.5,.865,r'$A_0=\sum_j(Q_j\,dp_j-P_j\,dq_j),\qquad B=-2\sum_jp_j\,dq_j,\qquad A=A_0+B$',ha='center',fontsize=18)
ax.text(.25,.76,r'$d+\hbar^{-1}[A_0,-]=d-\delta$',ha='center',fontsize=18)
ax.text(.75,.76,r'$d+\hbar^{-1}[A_0+B,-]=d-\delta$',ha='center',fontsize=18)
ax.annotate('',xy=(.59,.76),xytext=(.41,.76),arrowprops=dict(arrowstyle='<->',lw=2,color='#326b96'))
ax.text(.5,.705,'B is fiber central: the actual derivation and horizontal algebra are identical.',ha='center',fontsize=12)
ax.text(.5,.635,r'$\Omega_0=+\omega,\quad dB=-2\omega,\quad\Omega_s=\Omega_0+s\,dB,\quad\Omega_1=-\omega$',ha='center',fontsize=19)
ax.text(.5,.555,r'$\frac{d}{ds}[\gamma\,e^{-\Omega_s/(2\pi i\hbar)}]_{2n}=d[-(2\pi i\hbar)^{-1}\gamma B\,e^{-\Omega_s/(2\pi i\hbar)}]_{2n-1}$',ha='center',fontsize=17)
ax.text(.5,.48,'FC8: γ is closed, its rank term is zero, and its positive-degree terms have compact support K.\nThe full primitive therefore has compact support; both characteristic integrals agree.',ha='center',fontsize=12)
ax.axhline(.42,xmin=.05,xmax=.95,color='#a9b9c4',lw=1)
ax.text(.5,.355,r'$L\geq n+1,\quad N\geq L+1,\quad d_j=[\lambda^j](e_\infty-e_0),\quad a_\varepsilon(z)=a(\varepsilon z)$',ha='center',fontsize=19)
ax.text(.5,.265,r'$\mathrm{ind}\,a^w=(2\pi)^{-n}\sum_{j=0}^{L-1}\varepsilon^{2j-2n}\int\mathrm{tr}_{2\nu}d_j\,\Omega_{\rm AN}+O(\varepsilon^{2L-2n})$',ha='center',fontsize=20)
ax.text(.5,.17,'AT1: both original ordered error powers, the full phase Jacobian and every Fourier factor remain.\nSuccessive coefficient limits give zero for j ≠ n and the actual analytic index at j = n.',ha='center',fontsize=12)
ax.text(.5,.07,'Proofs: FM6–FM10, FC8; RP12–RP15 at each finite degree, IP22–IP28, AT1.\nSource framework: Pflaum–Posthuma–Tang, CyclicWeyl.tex 336–382;\ncentral-lift observation: Feigin–Felder–Shoikhet, FFSrevised.tex 2189–2194.',ha='center',fontsize=10.5)
fig.savefig(P/'matrix-index-receiving-maps.svg')
fig.savefig(P/'matrix-index-receiving-maps.png',dpi=160)
