from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
fig, (ax, bx) = plt.subplots(1,2,figsize=(13.6,6.3),facecolor='white')
for a in (ax,bx):
    a.set(xlim=(0,1),ylim=(0,1)); a.axis('off')
ax.set_title('Graph factorization and native normalization',fontsize=13,pad=10)
for x,y,t in [(.08,.74,r'$X$'),(.56,.74,r'$Y\times\mathbb{R}^n$'),(.56,.24,r'$Y$')]:
    ax.text(x,y,t,ha='center',va='center',fontsize=16,
            bbox=dict(boxstyle='round,pad=.4',facecolor='#eff6ff',edgecolor='#475569'))
for p,q in [((.16,.74),(.40,.74)),((.56,.64),(.56,.34)),((.10,.64),(.45,.26))]:
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='-|>',lw=1.8,color='#075985'))
ax.text(.28,.83,r'$i=(f,e)$',ha='center',fontsize=12)
ax.text(.62,.49,r'$p$',fontsize=14)
ax.text(.23,.41,r'$f=p\circ i$',fontsize=12,rotation=-34,
        bbox=dict(facecolor='white',edgecolor='none',pad=2))
ax.text(.5,.08,r'$d=\dim Y-\dim X,\qquad r=n+d$',ha='center',fontsize=11)
ax.text(.5,.015,r'$i!=\varepsilon_r\tau_N[e_{\rm tube}],\quad p!=\varepsilon_n\eta_n$',ha='center',fontsize=11)
bx.set_title('The middle graph is removed as a global cycle',fontsize=13,pad=10)
boxes = [(.80,r'$(\alpha-df^*\zeta,\zeta;\ u,w-dg\,u)$'),
         (.55,r'$(\Sigma_{f^*TY},\ c(\zeta)-i\widehat c(u))$'+'\n'+r'$\widehat\otimes\ (S_{gf},\ c_{gf}(\alpha,w))$'),
         (.24,r'$\ker D=\mathbb{C} g_W$: even, trivial $O(n)$ character'+'\n'+r'$\Rightarrow\quad 1_{C_0(X)}\ \#\ (gf)!_{\rm out}$')]
for y,t in boxes:
    bx.text(.5,y,t,ha='center',va='center',fontsize=11,
            bbox=dict(boxstyle='round,pad=.6',facecolor='#f0fdf4',edgecolor='#475569'))
for p,q in [(.71,.64),(.42,.34)]:
    bx.annotate('',xy=(.5,q),xytext=(.5,p),arrowprops=dict(arrowstyle='-|>',lw=1.8,color='#047857'))
bx.text(.51,.665,'invertible shears; full spinor evaluation',ha='center',fontsize=9,
        bbox=dict(facecolor='white',edgecolor='none',pad=2))
bx.text(.51,.365,'bounded radial path; equivariant kernel',ha='center',fontsize=9,
        bbox=dict(facecolor='white',edgecolor='none',pad=2))
bx.text(.5,.035,r'Source multiplication $a(x)$ is retained throughout.',ha='center',fontsize=10)
fig.text(.5,.032,r'$\varepsilon_d=(-1)^{d(d-1)/2}$ for integer $d$; '+
         r'$\varepsilon_r\varepsilon_n=\varepsilon_d(-1)^{rn+n}$, including negative $d$.',ha='center',fontsize=11)
fig.text(.5,.005,'Graph symbols: Connes–Skandalis (1984), Sections I–II. Global proof: Theorems 6.1 and 7.3.',ha='center',fontsize=9)
fig.subplots_adjust(left=.035,right=.965,top=.89,bottom=.12,wspace=.28)
fig.savefig(root/'KT-KK-16-factorization.svg',bbox_inches='tight')
fig.savefig(root/'KT-KK-16-factorization.png',dpi=160,bbox_inches='tight')
print('Rendered KT-KK-16-factorization.svg and .png')

