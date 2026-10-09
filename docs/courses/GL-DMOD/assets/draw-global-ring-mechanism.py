"""Exact schematic for GR.4 and GR.8-GR.11; independently authored CC0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(13.6,9.5))
fig.patch.set_facecolor('#f7f8fb')
ax.set_facecolor('#f7f8fb'); ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.04,.96,'Every complex parameter: the actual global operator ring',
        fontsize=20,weight='bold',va='top',color='#152c44')
ax.text(.04,.887,r'$G$ connected complex semisimple; $X=G/B$; $\tau=-\lambda-\rho$',
        fontsize=14,color='#354e65')

def box(x,y,w,h,title,lines,color='#e7eef9'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.013',
                facecolor=color,edgecolor='#496580',linewidth=1.4))
    ax.text(x+.012,y+h-.025,title,fontsize=13,weight='bold',va='top',color='#172f47')
    ax.text(x+.012,y+h-.075,'\n'.join(lines),fontsize=12.5,va='top',linespacing=1.40,
            color='#20394f')

box(.05,.615,.40,.245,'1. Exterior cohomology (GR.2–GR.4)',[
    r'$\mathcal{N}=G\times^B\mathfrak{n}$',
    r'$H^q(X,\wedge^j\mathcal{N})=0\quad(q\ne j)$',
    r'$H^j(X,\wedge^j\mathcal{N})=\mathbf{C}^{c_j}$',
    r'$c_j=\#\{w\in W:\ell(w)=j\}$; action trivial'])
box(.55,.615,.40,.245,'2. Universal resolution (GR.7–GR.8)',[
    r'$C^{-j}=U^{\mathrm{o}}\otimes\wedge^j\mathcal{N}$',
    r'$H^{q>0}(X,\mathscr{D}_A)=0$',
    r'$B=\Gamma(X,\mathscr{D}_A)$',
    r'$\mathrm{gr}_j^F B=U(\mathfrak{g})^{c_j}$'])
ax.annotate('',xy=(.53,.736),xytext=(.475,.736),
            arrowprops={'arrowstyle':'->','lw':2,'color':'#345674'})

box(.05,.29,.90,.245,'3. Identify the whole universal ring (GR.9–GR.10)',[
    r'$A=\mathbf{C}[\mathfrak{h}^*],\quad B^G=A,\quad z\mapsto q_z(-\Lambda-\rho)$',
    r'$\mathrm{gr}_j^F A=Z(U)^{c_j}$',
    r'$\Psi: U(\mathfrak{g})\otimes_{Z(U)}A\ \overset{\sim}{\longrightarrow}\ \Gamma(X,\mathscr{D}_A)$',
    r'Graded comparison: $U\otimes_Z Z^{c_j}\ \overset{\sim}{\longrightarrow}\ U^{c_j}$'], '#e7f3ec')
ax.annotate('',xy=(.745,.548),xytext=(.745,.594),
            arrowprops={'arrowstyle':'->','lw':2,'color':'#345674'})

box(.05,.075,.90,.142,'4. Specialize by the finite parameter Koszul complex (GR.11)',[
    r'$\Lambda=\lambda:\quad U(\mathfrak{g})/U\ker\chi_{-\lambda-\rho}'
    r'\ \overset{\sim}{\longrightarrow}\ \Gamma(X,\mathscr{D}_\lambda)$',
    'All complex λ, including singular parameters; every central quotient.'],'#fbefd9')
ax.annotate('',xy=(.495,.232),xytext=(.495,.273),
            arrowprops={'arrowstyle':'->','lw':2,'color':'#345674'})
ax.text(.05,.025,'Schematic of proved maps and cohomology counts; no rank-specific geometry. '
        'Section 5A.10, GR.4 and GR.8–GR.11.  CC0 1.0.',fontsize=10,color='#47596a')
fig.savefig(ROOT/'global-ring-mechanism.png',dpi=170,bbox_inches='tight')
fig.savefig(ROOT/'global-ring-mechanism.svg',bbox_inches='tight')
plt.close(fig)
print('Rendered global-ring-mechanism.png and .svg')
