"""Draw the full Gaussian Weyl operator and its exact inverse in GE1--GE2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,8))
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.94,'A Gaussian example in the original isotropic symbol class',ha='center',fontsize=19)
ax.text(.5,.86,r'$a_G(x,\xi)=2+e^{-x^2-\xi^2},\quad n=\nu=1,\quad \psi_G=1,\quad b_G=(2+e^{-x^2-\xi^2})^{-1}$',ha='center',fontsize=15)
ax.text(.5,.76,r'$g_0(x)=\pi^{-1/4}e^{-x^2/2},\quad P_0f=g_0\langle f,g_0\rangle,\quad (e^{-x^2-\xi^2})^w=\frac{1}{2}P_0$',ha='center',fontsize=17)
ax.text(.5,.65,r'$L^2(\mathbb{R})=\operatorname{span}\{g_0\}\oplus\{g_0\}^{\perp}$',ha='center',fontsize=23)
for x,title,operator,inverse in [(.26,'On the Gaussian line',r'$a_G^w=\frac{5}{2} I$',r'$(a_G^w)^{-1}=\frac{2}{5} I$'),(.74,'On its full orthogonal complement',r'$a_G^w=2I$',r'$(a_G^w)^{-1}=\frac{1}{2} I$')]:
    ax.text(x,.535,title,ha='center',fontsize=14)
    ax.text(x,.455,operator,ha='center',fontsize=24,bbox=dict(boxstyle='round,pad=.4',fc='#eef4f8',ec='#45667d'))
    ax.text(x,.35,inverse,ha='center',fontsize=21)
ax.text(.5,.245,r'$a_G^w=2I+\frac{1}{2}P_0,\qquad (a_G^w)^{-1}=\frac{1}{2}I-\frac{1}{10}P_0$',ha='center',fontsize=23)
ax.text(.5,.16,'Both ordered products equal I. The actual operator inverse is computed above.\nThe cutoff symbol bG is the reciprocal symbol used in the formal projector construction.',ha='center',fontsize=12)
ax.text(.5,.075,'GE1–GE2 and CI13 prove the complete Fourier kernel and both inverses.\nThe analytic index, formal relative trace and classical cutoff integral all equal zero.\nevery original coefficient is retained.',ha='center',fontsize=10.5)
fig.savefig(P/'relative-projector-gaussian-example.svg')
fig.savefig(P/'relative-projector-gaussian-example.png',dpi=160)
