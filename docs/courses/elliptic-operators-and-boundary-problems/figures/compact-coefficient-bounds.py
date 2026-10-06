"""Exact two-stage compactness approximation, equations B39--B43."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,6));ax.set(xlim=(0,13),ylim=(0,6));ax.axis('off')
def txt(x,y,s,size=16):ax.text(x,y,s,ha='center',va='center',fontsize=size)
txt(6.5,5.66,'Compact coefficients: two explicit norm approximations',20)
txt(6.5,5.08,r'All maps: $L^2(\mathbb{R}^n;H_1)\ \longrightarrow\ L^2(\mathbb{R}^n;H_2)$',16)
txt(1.8,4.08,r'$a^w$',23);txt(6.5,4.08,r'$a_F^w$',23);txt(11.2,4.08,r'$(Pa_FQ)^w$',23)
for x,y in [(2.55,5.7),(7.35,9.9)]:
 ax.annotate('',xy=(y,4.08),xytext=(x,4.08),arrowprops=dict(arrowstyle='->',lw=1.7,color='#245078'))
txt(4.2,3.22,'Original partition removes the phase tail',13)
txt(4.2,2.68,r'$\|(a-a_F)^w\|\leq CC_J\varepsilon\,p_{\leq J}(a;m,g)$',15)
txt(9.1,3.22,'Fixed finite coefficient projections',13)
txt(9.1,2.68,r'$\|(a_F-Pa_FQ)^w\|\leq 2C\delta\max_{0\leq j\leq J}(2n/c_F)^{j/2}$',14)
txt(6.5,1.95,r'$Q:H_1\to H_1,\quad P:H_2\to H_2,\quad g_X(T)\geq c_F|T|^2\quad(X\in K_F)$',16)
txt(6.5,1.26,'Finite matrix of compact scalar operators; both errors tend to zero.',15)
txt(6.5,.61,r'Converse: $C_w(bR)^w I_v=b^w,\qquad Rz=\langle z,v\rangle w$',16)
fig.text(.5,.02,'B39–B43 retain the original metric, weight and coefficient spaces. No coefficient basis of the entire space is used.\nThe compact coefficient argument is proved in the lesson.',ha='center',fontsize=10)
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.11)
fig.savefig(p/'compact-coefficient-bounds.svg');fig.savefig(p/'compact-coefficient-bounds.png',dpi=160);plt.close(fig)
