"""Exact proof map for the Lesson 13 all-weight primitive/Fricke proof."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

PACKAGE=Path(__file__).resolve().parents[1]
fig,ax=plt.subplots(figsize=(9,27),dpi=100)
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0,900),ylim=(0,2700)); ax.axis('off')
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
ax.text(450,2650,'Primitive forms and Fricke',ha='center',fontsize=22,weight='bold',color='#17324d')
ax.text(450,2611,r'Every weight $k\geq1$, every level $N$, fixed $\chi$ of conductor $C\mid N$',ha='center',fontsize=13,color='#394b63')

def panel(y,h,title,lines,colour='#e8f1fa'):
    y+=600
    ax.add_patch(FancyBboxPatch((50,y),800,h,boxstyle='round,pad=0,rounding_size=14',facecolor=colour,edgecolor='#597f9f',linewidth=1.5))
    ax.text(72,y+h-36,title,fontsize=16,weight='bold',color='#17324d',va='top')
    for i,line in enumerate(lines):
        ax.text(72,y+h-82-34*i,line,fontsize=12.5,color='#17324d',va='top')

def arrow(upper,lower):
    upper+=600; lower+=600
    ax.annotate('',xy=(450,lower+5),xytext=(450,upper-5),arrowprops={'arrowstyle':'->','color':'#446983','lw':2})

panel(1690,260,'1. Finite covers give the actual adjoint — F.1',[
    r'$H=\Gamma\cap A^{-1}\Gamma A\quad\longrightarrow\quad H^{\prime}=\Gamma\cap A\Gamma A^{-1}$',
    r'Unfold, change $w=Az$, then retile: $\mathcal{A}_A^*=\mathcal{A}_{A^*}$, $A^*=\det(A)A^{-1}$.',
    r'$y^{k/2}|f|$ and every rational slash are bounded; the finite covers have finite area.',
    r'$\sigma_p\beta_p=\alpha_p\gamma_\infty$ gives $T_p^*=\chi(p)^{-1}T_p$ for $p\nmid N$.',
    'The convergence and density calculation include weight one.'
])
panel(1440,215,'2. Good operators preserve old and new — F.2',[
    r'$T_p^N B_d=B_dT_p^L$ for $p\nmid N$; its adjoint has the same preservation.',
    'Commuting normal operators give an orthogonal simultaneous eigenbasis.',
    r'Theorem S: $a_1=0$ forces a good eigenvector in the new space to be zero.',
    r'Hence every primitive good eigenspace is a line, normalized by $a_1=1$.'
])
panel(1155,250,'3. Fricke and reflection transport both spaces — F12',[
    r'$\mathcal{W}_N,J:\ S_k(N,\chi)\longrightarrow S_k(N,\overline{\chi})$',
    r'$\mathcal{W}_N$ is unitary; $Jf(z)=\overline{f(-\overline{z})}$ is antiunitary.',
    r'$e=N/(dL),\qquad \mathcal{W}_NB_dh=(e/d)^{k/2}B_e\mathcal{W}_Lh$',
    r'Old $\longrightarrow$ old and new $\longrightarrow$ new, with the displayed characters.',
    r'$W_N^{-1}\beta_pW_N=\alpha_p$ transports the exhaustive coset adjoint.'
])
panel(870,250,'4. The bad adjoint preserves the whole old space — F13–F14',[
    r'$U_{p,\chi}^*=\mathcal{W}_N^{-1}U_{p,\overline{\chi}}\mathcal{W}_N\quad(p\mid N)$',
    r'$p\mid d:\ U_pB_dh=B_{d/p}h$',
    r'$p\nmid d,\ p\mid L:\ U_pB_dh=B_dU_ph$',
    r'$p\nmid dL:\ U_pB_dh=B_dT_p^Lh-\chi(p)p^{k-1}B_{dp}h$',
    r'Adjoint preservation gives new invariance; good commutation gives $U_pf=a_p(f)f$.'
],colour='#fff2d9')
panel(585,250,'5. Two vectors in the same primitive line — F.3',[
    r'$f\in S_k(N,\chi)^{\rm new},\qquad T_pf=\lambda_pf\ (p\nmid N)$',
    r'$\mathcal{W}_Nf,\ Jf\in S_k(N,\overline{\chi})^{\rm new}$',
    r'Both have good eigenvalues $\overline{\lambda_p}=\chi(p)^{-1}\lambda_p$.',
    r'The common line gives $\mathcal{W}_Nf=\omega_fJf$.',
    r'The two norm identities give $|\omega_f|=1$.'
])
panel(300,250,'6. Primitive packets occur at an actual lower level — F.4',[
    r'Finite-dimensional splitting: $S_k(N,\chi)=\mathrm{Old}\oplus\mathrm{New}$.',
    r'Divisor induction spans it by $B_dh$ with $h$ primitive at $L\mid N$, $C\mid L$.',
    r'Each $B_dh$ retains the eigenvalues of $h$ at every prime outside $N$.',
    'A finite product of separating good operators isolates the chosen packet.',
    'Some lower primitive form therefore has exactly that packet outside N.'
])
panel(0,265,'7. The descending-character bad-prime norm — F.5',[
    r'Assume $p\mid N$ and $C\mid N/p$.',
    r'$p^2\mid N:\ U_pf$ lies at lower level and in the new space, so $a_p(f)=0$.',
    r'$p\parallel N:\ p\langle Qf,h\rangle_{N/p}=p^k\langle f,B_ph\rangle_N$ gives $Qf=0$.',
    r'The verified unitary normalizer gives $a_p(f)^2=\chi(p)p^{k-2}$.',
    r'At $k=1$, the two cases give $|a_p(f)|=0$ or $p^{-1/2}\leq1$.'
],colour='#fff2d9')
panel(-300,265,'8. Ramified characters cancel the extra cosets — F.6',[
    r'Assume $p\mid N$ and $C\nmid N/p$: $\chi$ is nontrivial on the reduction kernel.',
    r'$p^2\mid N$: $\sum_r\chi(1-(N/p)jr)=0$ cancels every $j\ne0$ row.',
    r'$p\parallel N$: both ordinary and exceptional terms have vanishing $\psi$ sums.',
    r'Exactly $p$ identity terms remain: $U_p^*U_p=p^{k-1}I$.',
    r'For a primitive form, $|a_p(f)|=p^{(k-1)/2}$; at $k=1$ this is $1$.'
],colour='#e5f4e9')
for top,bottom in [(1690,1655),(1440,1405),(1155,1120),(870,835),(585,550),(300,265),(0,-35)]:arrow(top,bottom)
ax.text(450,225,'Exact proof locators: Lesson 13 §3.2C, Lemma F.1–Theorem F.6, F1–F26.',ha='center',fontsize=10.5,color='#394b63')
ax.text(450,193,'Free human source: Li, Newforms and functional equations (1975), printed294–297.',ha='center',fontsize=10.5,color='#394b63')
ax.text(450,150,r'Every bad-prime case at weight one gives $|a_p(f)|\leq1$ in the written proof.',ha='center',fontsize=12.5,weight='bold',color='#245a36')
ax.text(450,116,'Conductor descent and all ramified-character cases are included in F.5–F.6.',ha='center',fontsize=10.5,color='#394b63')
fig.savefig(PACKAGE/'assets/weight-one-primitive-fricke-proof-map.png',dpi=100,facecolor=fig.get_facecolor())
plt.close(fig)
