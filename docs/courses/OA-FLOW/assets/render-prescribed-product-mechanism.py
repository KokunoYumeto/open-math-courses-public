# Original reproduction program: any rights held in this code are dedicated under CC0-1.0.
# Matplotlib and installed font software retain their own licenses; neither is distributed here.
"""Reproducible proof schematic; all geometry is diagram layout, not operator data."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

AREA = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none', 'svg.hashsalt': 'oa-flow-prescribed-product-20261004'})
fig, ax = plt.subplots(figsize=(16, 10), dpi=130)
fig.patch.set_facecolor('#f7f9fc')
ax.set(xlim=(0, 1), ylim=(0, 1))
ax.axis('off')

def panel(x, y, width, height, color='#ffffff'):
    ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.012',
        facecolor=color,edgecolor='#b7c4d6',linewidth=1.3))

def text(x, y, value, size=16, color='#142640', **kwargs):
    ax.text(x,y,value,fontsize=size,color=color,va='center',**kwargs)

def arrow(x1,y1,x2,y2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','color':'#365d91','lw':2})

text(.5,.967,'The prescribed product: a vector proof before its differential equation',21,ha='center',weight='bold')
text(.5,.924,r'$u_t=e^{itK}e^{-itH}\qquad D(H)=D(K)\qquad K=H+a,\quad a=a^*\in M$',20,ha='center')

panel(.03,.69,.94,.18)
text(.05,.842,'1. Exact domain calculation  ·  (PP.3)–(PP.8)',16,weight='bold')
text(.06,.788,r'$\xi\in D(H)\ \Longrightarrow\ e^{-isH}\xi\in D(K)$',19)
text(.06,.732,'Split the actual product quotient; both generator limits exist.',15)
arrow(.48,.785,.58,.785)
text(.62,.789,r'$\frac{d}{ds}u_s\xi=iB_s\xi$',21)
text(.62,.733,r'$B_s=e^{isK}a e^{-isH}$',20)

arrow(.50,.675,.50,.638)
panel(.03,.415,.445,.20)
panel(.525,.415,.445,.20)
text(.05,.588,'2. Vector integral and density  ·  (PP.9)–(PP.11)',15,weight='bold')
text(.05,.523,r'$u_t-1=i\int_0^t B_s\,ds$',22)
text(.05,.454,r'$\|u_t-1\|\leq |t|\,\|a\|$',21)
text(.545,.588,'3. Proved adjoint integral  ·  (PP.12)–(PP.16)',15,weight='bold')
text(.545,.523,r'$u_t^*-1=-i\int_0^t B_s^*\,ds$',22)
text(.545,.454,r'$B_s^*=e^{isH}a e^{-isK}$',21)

arrow(.25,.401,.25,.356)
arrow(.75,.401,.75,.356)
panel(.03,.14,.94,.195,color='#edf4ff')
text(.05,.310,'4. Quotients at t → 0, then every normal positive functional  ·  (PP.15)–(PP.22)',16,weight='bold')
text(.05,.259,r'$Q_t\xi\to ia\xi,\quad Q_t^*\xi\to -ia\xi,\quad \|Q_t\|\leq\|a\|$',22)
text(.70,.259,r'$Q_t=(u_t-1)/t$',20)
text(.05,.204,r'Finite head → 0; tail $\leq C^2\sum_{j>N}\|\xi_j\|\,\|\eta_j\|\to0$ as $N\to\infty$; $C=2\|a\|$.',16)
text(.05,.160,r'$\omega(z_t^*z_t)\to0,\quad\omega(z_tz_t^*)\to0\quad(\omega\in M_*^+,\ z_t=Q_t-ia)$',19)

text(.5,.082,r'At every time: $u_t^\prime=iB_t=i\,u_t\alpha_t^H(a)$, with continuous intrinsic strong-star derivative.',16,ha='center')
text(.5,.035,'Proof schematic for (PP.1)–(PP.23). Integrals are vector Riemann integrals; negative times use oriented intervals.',13,ha='center',color='#4d617c')
fig.subplots_adjust(left=.025,right=.975,bottom=.025,top=.99)
fig.savefig(AREA/'prescribed-product-mechanism.png',facecolor=fig.get_facecolor())
fig.savefig(AREA/'prescribed-product-mechanism.svg',facecolor=fig.get_facecolor(),metadata={'Date':'2026-10-04T00:00:00Z'})
# Keep the distributed vector image in the offline SVG profile: no external DTD.
svg_path = AREA/'prescribed-product-mechanism.svg'
svg = svg_path.read_text(encoding='utf-8')
start = svg.index('<!DOCTYPE ')
end = svg.index('>', start) + 1
svg_path.write_text(svg[:start] + svg[end:].lstrip('\n'), encoding='utf-8', newline='\n')
plt.close(fig)
