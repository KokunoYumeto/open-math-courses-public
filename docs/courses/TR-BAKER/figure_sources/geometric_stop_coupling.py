"""Exact proof-route diagram for TR-BAKER-10 Theorem 10.141; CC0.

GPT-6.1 Sol (OpenAI), Ultra. Human mathematical context: Yu's freely
accessible 2013 paper, Section 6. Every arrow is proved in the lesson;
the graphic contains no numerical sample of contradiction parameters.
Font glyphs retain their existing licences.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(12,14.4),dpi=170)
fig.patch.set_facecolor('#f6f8fb');ax.set_facecolor('#f6f8fb')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.982,'The geometric stopping contradiction',ha='center',va='top',fontsize=21,weight='bold',color='#12263b')
ax.text(.5,.954,'Original field K, independent bases, weighted least rank r ≥ 2',ha='center',va='top',fontsize=11.5,color='#42566d')

boxes=[
 (.785,'1  Actual terminal family',[
  r'$I=I^*=\lfloor 3D/\ln Q\rfloor+1\leq I_1,\quad Q^I>\exp(3D)$',
  r'$|s|\leq\lfloor qS_I\rfloor,\quad |\mathbf{t}|\leq\lfloor\eta T_I\rfloor:\quad\Phi_I(s;\mathbf{t})=0$',
  'An integral coefficient attains δ; the family is nonzero.  [10.140]']),
 (.595,'2  Ordinary polynomial and hyperplane jets',[
  r'$P_I=Y^{\mathbf{d}}Q_I\ne0,\quad \deg_X P_I\leq kL,\quad\deg_{Y_j}P_I\leq 2q^{\nu-I}D_j$',
  'Triangular binomial changes and the Laurent shift preserve total order.',
  'The Euler directions span the original W.  [10.23, 10.30–10.31]']),
 (.405,'3  Multiplicity theorem with every allocation',[
  r'$\mathcal{R}_0>36/25,\quad\mathcal{R}_{m,J}>8,\quad\mathcal{R}_r>31$',
  r'$1\leq m<r,\quad u_1,\ldots,u_m\in\mathbb{Z}^r\ \mathrm{independent},\quad \mathbf{B}\in\mathrm{span}_{\mathbb{Q}}(u_i)$',
  r'$\beta_i=\prod_j\alpha_j^{u_{ij}}\in K,\quad h(\beta_i)\leq R_i=\sum_j|u_{ij}|\sigma_j$'+'  [10.100–10.101]']),
 (.215,'4  Actual residue-index-dependent profile',[
  r'$\prod_i R_i<\frac{1}{700}\,\Gamma_n^{r-m}\frac{M_r}{M_m}\prod_j\sigma_j$',
  'Original field and local prime retained; the rank-one residue order is retained.',
  'All ranks and original parameter cases satisfy this strict bound.  [10.102]']),
 (.025,'5  Smaller admissible rank: contradiction',[
  r'$L_i^\prime=\sum_j u_{ij}L_j,\quad \sum_k |a^\prime_{ik}|h(a_k)\leq R_i$',
  r'$\prod_i R_i<\frac{1}{700}\,\Psi_m\prod_kh(a_k),\quad m<r$',
  'Same nonzero form, independent integral forms, original allowance.  [10.103]'])]
for y,title,lines in boxes:
 ax.add_patch(FancyBboxPatch((.035,y),.93,.145,boxstyle='round,pad=0.008,rounding_size=0.012',facecolor='white',edgecolor='#8da8bc',linewidth=1.5))
 ax.text(.063,y+.12,title,va='center',fontsize=14.3,weight='bold',color='#16324f')
 for j,line in enumerate(lines):ax.text(.063,y+.089-j*.03,line,va='center',fontsize=12.4,color='#21384c')
for upper,lower in zip(boxes,boxes[1:]):
 ax.annotate('',xy=(.5,lower[0]+.153),xytext=(.5,upper[0]-.009),arrowprops={'arrowstyle':'-|>','color':'#176a85','lw':2.2,'mutation_scale':18})
fig.subplots_adjust(left=.015,right=.985,top=.995,bottom=.005)
target=Path(__file__).resolve().parent/'geometric-stop-coupling.png'
fig.savefig(target,facecolor=fig.get_facecolor());plt.close(fig)
print(target)
