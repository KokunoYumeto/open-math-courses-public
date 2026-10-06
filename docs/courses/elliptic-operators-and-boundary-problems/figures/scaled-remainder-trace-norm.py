"""Draw the original scaled-symbol factorization proved in IP22--IP28."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13.3,7.5))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.94,'A genuine scaled remainder has a trace-norm bound',ha='center',fontsize=20)
ax.text(.5,.84,r'$q_\varepsilon\in S(h_\varepsilon^M,g_\varepsilon),\quad h_\varepsilon=\varepsilon^2(1+|\varepsilon z|^2)^{-1},\quad k=n+1,\quad M\geq n+1$',ha='center',fontsize=15)
ax.text(.5,.755,r'$H_\varepsilon=I+\varepsilon^2(|x|^2+D^2),\qquad q_\varepsilon^w=C_\varepsilon B_\varepsilon$',ha='center',fontsize=18)
nodes=[.09,.5,.91]
for x in nodes:ax.text(x,.59,r'$H_\nu$',ha='center',va='center',fontsize=23,bbox=dict(boxstyle='round,pad=.5',fc='#f0f4f7',ec='#45667d'))
for x1,x2 in zip(nodes[:-1],nodes[1:]):ax.annotate('',xy=(x2-.06,.59),xytext=(x1+.06,.59),arrowprops=dict(arrowstyle='->',lw=2,color='#326b96'))
ax.text(.295,.66,r'$B_\varepsilon=(H_\varepsilon^{k/2}\otimes I_\nu)q_\varepsilon^w$',ha='center',fontsize=15)
ax.text(.705,.66,r'$C_\varepsilon=H_\varepsilon^{-k/2}\otimes I_\nu$',ha='center',fontsize=15)
ax.text(.295,.49,r'$\|B_\varepsilon\|_2\leq C(2\pi)^{-n/2}\varepsilon^{2M-n}$',ha='center',fontsize=15)
ax.text(.705,.49,r'$\|C_\varepsilon\|_2\leq C\sqrt{\nu}\,\varepsilon^{-n}$',ha='center',fontsize=15)
ax.text(.5,.375,r'$\|q_\varepsilon^w\|_1\leq\|C_\varepsilon\|_2\|B_\varepsilon\|_2\leq C\varepsilon^{2M-2n}$',ha='center',fontsize=19)
ax.text(.5,.265,r'$q_\varepsilon(z)=\varepsilon^{2M}\widehat q_\varepsilon(\varepsilon z),\quad w=\varepsilon z,\quad dz=\varepsilon^{-2n}dw$',ha='center',fontsize=17)
ax.text(.5,.17,'The full oscillator eigenvalue is 1 + nε² + 2ε²|γ|. The inverse range lies in its spectral domain.\nBoth Schatten norms use the original Hν norm; the original cutoff is separate from this remainder.',ha='center',fontsize=12)
ax.text(.5,.065,'IP23–IP28 prove every operator domain, Fourier factor and exponent. DE5a includes every high-degree product.\nNo novelty claim. No bound for the full cutoff errors is asserted.',ha='center',fontsize=11)
fig.savefig(P/'scaled-remainder-trace-norm.svg')
fig.savefig(P/'scaled-remainder-trace-norm.png',dpi=160)
