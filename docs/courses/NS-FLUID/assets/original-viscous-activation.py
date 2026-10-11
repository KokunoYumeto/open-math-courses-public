"""Exact activation orders and full viscous memory; schematic, no solution samples."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,9.5),facecolor='#f7fafc')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ink='#16354b';blue='#16758c';orange='#b96120'
ax.text(.04,.956,'Every upper scale activates in the actual viscous cascade',fontsize=21,fontweight='bold',color=ink)
ax.text(.04,.919,r'$u(0)=\psi_{1,n_0},\quad \|\psi_i\|_2^2=1,\quad\nu>0,\quad\kappa_n=q^{5n/2},\quad q=1+\epsilon_0\in(1,2)$',fontsize=15,color=ink)
def box(x,y,w,h):ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',fc='white',ec='#cad9e3'))
box(.04,.53,.43,.33);box(.51,.53,.44,.33)
ax.text(.06,.82,'Exact first nonzero powers of physical time',fontsize=15,fontweight='bold',color=ink)
ax.text(.06,.772,r'$n=n_0+j,\quad m_j=6^j-1$',fontsize=17,color=blue)
cols=[.09,.19,.29,.39]
for x,label in zip(cols,[r'$j$',r'$a_n$',r'$b_n,c_n$',r'$d_n$']):ax.text(x,.728,label,fontsize=16,ha='center',color=ink)
for j,y in enumerate([.686,.646,.606,.566]):
    m=6**j-1
    for x,label in zip(cols,[str(j),str(m),str(2*m+1),str(3*m+2)]):ax.text(x,y,label,fontsize=15,ha='center',color=ink)
ax.text(.53,.82,'All leading coefficients are positive',fontsize=15,fontweight='bold',color=ink)
ax.text(.53,.769,r'$A_0=1,\quad B_j=\frac{\kappa_{n_0+j}\epsilon A_j^2}{2m_j+1}$',fontsize=18,color=ink)
ax.text(.53,.703,r'$C_j=\frac{\kappa_{n_0+j}\epsilon^2e^{-K^{10}}A_j^2}{2m_j+1}$',fontsize=18,color=ink)
ax.text(.53,.636,r'$D_j=\frac{\kappa_{n_0+j}\epsilon^{-2}C_jA_j}{3m_j+2}$',fontsize=18,color=ink)
ax.text(.53,.569,r'$A_{j+1}=\frac{\kappa_{n_0+j+1}K D_j^2}{6m_j+5}$',fontsize=18,color=ink)
box(.04,.24,.91,.23)
ax.text(.06,.432,'The full memory preserves the drive sign at every later time',fontsize=17,fontweight='bold',color=ink)
ax.text(.06,.38,r"$c_n'=\kappa_n\epsilon^2e^{-K^{10}}a_n^2+\left(\kappa_n\epsilon^{-1}K^{10}b_n-\nu q^{2n}G_3\right)c_n+\nu^2\int_0^t\mathscr{K}_{3,n}(t-s)c_n(s)\,ds$",fontsize=17,color=ink)
ax.text(.06,.316,r'$\mathscr{K}_{3,n}(r)=\langle e^{\nu rL_{3,n}}g_{3,n},g_{3,n}\rangle>0$',fontsize=17,color=blue)
ax.text(.58,.316,r'$c_n(t)>0\quad(n\geq n_0,\ 0<t<T_*)$',fontsize=17,color=orange)
ax.text(.06,.268,'Positive integrating factors and the convergent Volterra series prove the sign; viscosity remains in the equation.',fontsize=12,color=ink)
ax.text(.04,.183,'Each expansion has its own proved remainder at a fixed scale. No uniform amplitude lower bound over all scales is asserted.',fontsize=12,color=ink)
ax.text(.04,.143,'The orders are exact integers, not numerical trajectory samples. Infinite-cascade transfer estimates remain a separate calculation.',fontsize=12,color=ink)
ax.text(.04,.088,'Proof: ORIGINAL_VISCOUS_ACTIVATION_20261010.md, VA1–VA22. Original fields, coefficients, clock and memory retained.',fontsize=11,color='#445f73')
ax.text(.04,.054,'Human comparison: Terence Tao, arXiv:1402.0290v3, original navier-blowup.tex, band equations and lines 2039–2106.',fontsize=11,color='#445f73')
for ext in ['png','svg']:fig.savefig(root/f'original-viscous-activation.{ext}',dpi=150,facecolor=fig.get_facecolor())
plt.close(fig)
