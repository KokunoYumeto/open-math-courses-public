"""The exact open-cover gluing in Remark 13.2, equations BE1--BE2."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,4.4));ax.set(xlim=(0,12),ylim=(0,4.5));ax.axis('off')
def text(x,y,s,size=16):ax.text(x,y,s,ha='center',va='center',fontsize=size)
text(6,4.16,'One global matrix from the original two domains',19)
text(2.85,3.18,r'$G|_{U_\rho}=\Psi^{-1}M_G\iota A_0$')
text(9.1,3.18,r'$G|_{\mathbb{R}^{\nu}\setminus K}=A_\infty$')
text(6,2.3,r'Overlap $U_\rho\setminus K$:  $aA_0=A_\infty$',17)
for x in [2.85,9.1]:ax.annotate('',xy=(6,2.62),xytext=(x,2.92),arrowprops=dict(arrowstyle='->',lw=1.7,color='#245078'))
text(6,1.5,r'$P_{\mathrm{ext}}=G+R_0,\quad R_0=\Psi^{-1}(P_1\oplus0)\iota A_0$',17)
text(6,.83,r'Kernel support: $L\times L\Subset U_\rho\times U_\rho$;  $K\subset U_\rho$',14)
text(6,.35,'The formulas agree on the complete overlap. No invertible extension through K is assumed.',12)
fig.text(.5,.018,'BE1–BE2 retain the target frame, the full multiplication and every kernel factor.\nFull proof: bott-suspension.md, Remark 13.2; matrix-extension input: matrix-extension.md, M1–M26.',ha='center',fontsize=10)
fig.subplots_adjust(left=.02,right=.98,top=.97,bottom=.16)
fig.savefig(p/'bott-frame-gluing.svg');fig.savefig(p/'bott-frame-gluing.png',dpi=170);plt.close(fig)
