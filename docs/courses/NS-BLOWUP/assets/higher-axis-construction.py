"""Reproduce the exact six-coordinate map and physical axis cancellation."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'svg.fonttype':'path'})
fig=plt.figure(figsize=(14,11.2),dpi=100,facecolor='#f6f8fb')
ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1400);ax.set_ylim(1120,0);ax.axis('off')
ink='#183047';blue='#17639b';green='#166e60';orange='#98491d'
def txt(x,y,s,size=14,color=ink,**kw):ax.text(x,y,s,va='top',fontsize=size,color=color,**kw)
def box(x,y,w,h,fill='#e5eef7'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',
        facecolor=fill,edgecolor='#c5d2dd'))
txt(35,24,'One fixed axis interval for the original coefficient system',24)
txt(35,66,'Exact derivative structure → convergent integral solution → physical residual cancellation',15)
box(40,114,1320,294)
txt(60,132,'1. THE ORIGINAL SIX COORDINATES — D2–D3',16,blue,weight='bold')
txt(65,184,r'$E_4=\operatorname{span}(e_1,e_2,e_3,e_4)$',23)
txt(65,230,r'$(\phi_n,U_n,K_n,\Pi_n)$',23)
txt(920,184,r'$E_2=\operatorname{span}(e_5,e_6)$',23)
txt(920,230,r'$(\partial_\xi\phi_n,\partial_\xi U_n)$',23)
ax.annotate('',xy=(887,220),xytext=(545,220),arrowprops=dict(arrowstyle='->',lw=3,color=green))
txt(675,176,r'$A_1$',24,green)
txt(955,290,r'$A_1E_2=\{0\}$',24,green)
txt(65,295,r'$A_1(\xi)D_0\,\partial_\eta^j A_1(s)=0\quad(j\geq0)$',23)
txt(65,357,'The diagonal integral kernels preserve both spaces. Adjacent parameter-derivative factors vanish.',14)
box(40,443,1320,188,'#e4f1ec')
txt(60,461,'2. THE RADIAL INTERVAL STAYS FIXED — D2, D4–D5',16,green,weight='bold')
xs=[90,410,785,1260];y=535
ax.plot([xs[0],xs[-1]],[y,y],color=ink,lw=2)
ax.plot([xs[0],xs[2]],[y,y],color=green,lw=7)
for x,label in zip(xs,[r'$0$',r'$X_a$',r'$a^2$',r'$X_{\rm an}$']):
    ax.plot([x,x],[y-10,y+10],color=ink);txt(x,y+17,label,21,ha='center')
txt(75,592,r'$X=\xi^2,\quad 0\leq\xi\leq a,\quad X_a<a^2<X_{\rm an}$',20)
txt(790,594,'Order only; radial positions are not to scale.',13)
box(40,662,1320,174)
txt(60,680,'3. THE FULL INTEGRAL SERIES CONVERGES — D3–D4',16,blue,weight='bold')
txt(65,725,r'$\|\mathcal{K}^kGf_n\|\leq\dfrac{(C_n a)^{k+1}}{(k+1)!}\max(1,p_k/\Delta)^{p_k},'
    r'\qquad p_k=\lceil k/2\rceil,\quad\Delta=\rho-\rho^\prime>0$',22)
txt(65,802,'The radial factorial wins over the parameter loss for every fixed a. No smallness of a is needed.',14)
box(40,866,1320,181,'#fff0e5')
txt(60,884,'4. THE ACTUAL FIRST CORRECTION — D7.21–D7.27',16,orange,weight='bold')
txt(65,928,r'$U_{1,X}(0,0)=Aj_0,\qquad'
    r'u_{z,1,\nu}(r_\nu,0,t)=\dfrac{Aj_0}{2\sqrt{\nu}}(1-t)^{-A-2D}r_\nu^2+O(r_\nu^4)$',23)
txt(65,995,r'$\mathcal{R}_\nu(u_\nu^{(0)}+u_{1,\nu},p_\nu^{(0)}+p_{1,\nu})\cdot e_z=0'
    r'\quad(r_\nu=0,\ t<1)$',22)
txt(40,1068,'Exact axis identity; residuals away from the axis require the later global construction. No numerical flow is plotted.',11)
txt(40,1090,'Source: OpenAI, pp.24–26,45–49, Lemma5.1. Full proofs: N3.1 D0–D7. Figure source: CC0.',11)
fig.savefig(HERE/'higher-axis-construction.svg',metadata={'Creator':'GPT-6 Astra (OpenAI)','Title':'Fixed axis interval and exact first correction'})
fig.savefig(HERE/'higher-axis-construction.png',dpi=100);plt.close(fig)
p=HERE/'higher-axis-construction.svg';t=p.read_text(encoding='utf8')
assert 'width="1008pt" height="806.4pt"' in t
p.write_text(t.replace('width="1008pt" height="806.4pt"','width="1400" height="1120"'),encoding='utf8')
