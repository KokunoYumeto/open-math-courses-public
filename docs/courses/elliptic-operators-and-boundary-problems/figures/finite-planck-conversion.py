"""Original phases and complete finite-weight inclusion constants."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,5.2));ax.set(xlim=(0,12),ylim=(0,5.2));ax.axis('off')
def txt(x,y,s,size=16):ax.text(x,y,s,ha='center',va='center',fontsize=size)
txt(6,4.91,'Quantization conversion on the original metric',20)
txt(6,4.27,r'$T_k=\exp(ik\langle D_x,D_\xi\rangle),\quad g^{A_k}=4k^{-2}g^\sigma,\quad k\ne0$',17)
txt(3,3.49,r'$h_{A_k}(X)=|k|h(X)/2$',17)
txt(9,3.49,r'$h(X)\leq h_*<\infty$',17)
txt(6,2.8,r'Actual remainder factor: $(|k|/2)^Nh(X)^N$; count: $(1+|k|h_*/2)^{2n}$',16)
txt(6,2.08,r'$S(h^dw,g)\ \longrightarrow\ S(h^Nw,g),\quad d\geq N$',17)
txt(6,1.44,r'$p_l(v;h^Nw,g)\leq h_*^{d-N}p_l(v;h^dw,g)$',17)
txt(6,.72,r'$a_1\circ_La_2=T_{1/2}((T_{-1/2}a_1)\#(T_{-1/2}a_2))$',17)
fig.text(.5,.02,'A35a–A35b and A52–A55 prove the complete phase comparison and every finite remainder inclusion.\nfinite-bound Gauss and Weyl proofs remain in their original lessons.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.13)
fig.savefig(p/'finite-planck-conversion.svg');fig.savefig(p/'finite-planck-conversion.png',dpi=165);plt.close(fig)
