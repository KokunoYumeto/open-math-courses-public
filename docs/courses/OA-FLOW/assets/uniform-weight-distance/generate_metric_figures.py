"""Original CC0 diagrams for Uniform distance and limits of weights.

Run: python -B generate_metric_figures.py
Dependencies: NumPy and Matplotlib. No TeX, network, source images or copied fonts.
All files are written beside this script. Mathematical references are manuscript anchors.
"""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
BG,INK,MUTED='#fcfbf7','#172d3c','#536575'
BLUE,TEAL,RED,GOLD='#236c9c','#087e80','#b4443f','#b88024'
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':13,
    'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':'#9ba9b1','xtick.color':MUTED,'ytick.color':MUTED,
    'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'svg.fonttype':'path',
    'svg.hashsalt':'oa-flow-uniform-metric-20261007','axes.spines.top':False,'axes.spines.right':False})

def save(fig,stem):
    fig.savefig(HERE/(stem+'.png'),dpi=160)
    fig.savefig(HERE/(stem+'.svg'),metadata={'Date':None,'Creator':'Original OA-FLOW mathematical illustration','Rights':'CC0-1.0'})
    plt.close(fig)

def canvas(title,subtitle,size=(15,8.5)):
    fig=plt.figure(figsize=size)
    fig.text(.05,.95,title,fontsize=24,weight='bold',va='top')
    fig.text(.05,.894,subtitle,fontsize=13,color=MUTED,va='top')
    return fig

def footer(fig,text):fig.text(.05,.035,text,fontsize=10.5,color=MUTED,va='bottom')

def matrix(ax,x,y,data,label,scale=.085,color=INK):
    rows,cols=len(data),len(data[0]);w=cols*scale;h=rows*scale
    ax.text(x-.025,y,label,ha='right',va='center',fontsize=17,color=color)
    for i,row in enumerate(data):
        for j,value in enumerate(row):ax.text(x+(j+.5)*scale,y+h/2-(i+.5)*scale,str(value),ha='center',va='center',fontsize=18,color=color)
    for xx,sgn in [(x-.012,1),(x+w+.012,-1)]:ax.plot([xx+sgn*.012,xx,xx,xx+sgn*.012],[y+h/2+.012,y+h/2+.012,y-h/2-.012,y-h/2-.012],color=color,lw=1.5)

def entire():
    fig=canvas('Two all-depth comparisons join into one entire cocycle',
        r'$\varphi,\psi$ faithful normal semifinite; $r\geq0$. Entire means operator-norm holomorphic.')
    fig.text(.05,.80,r'$e^{-r}\varphi\preceq_\infty\psi\preceq_\infty e^r\varphi\quad\Longleftrightarrow\quad\|U(z)\|\leq e^{r|\operatorname{Im}z|}\quad(z\in\mathbb{C})$',fontsize=22,color=TEAL)
    ax=fig.add_axes([.08,.25,.39,.43]);ax.set(xlim=(-2,2),ylim=(-2,2),xlabel=r'$\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z$')
    ax.axhspan(0,2,color='#e7f2ed');ax.axhspan(-2,0,color='#e5eef5');ax.axhline(0,color=INK,lw=1.8)
    ax.set_xticks([-2,-1,0,1,2]);ax.set_yticks([-2,-1,0,1,2])
    ax.text(0,1.4,'Upper half-plane',ha='center',fontsize=16,color=TEAL,weight='bold')
    ax.text(0,.85,r'$U(z)=V(\overline{z})^*$',ha='center',fontsize=19,color=TEAL)
    ax.text(0,.27,r'$V(t)=(D\varphi:D\psi)_t$',ha='center',fontsize=13,color=TEAL)
    ax.text(0,-.25,r'$U(t)=(D\psi:D\varphi)_t$',ha='center',va='top',fontsize=14,color=BLUE,bbox={'fc':BG,'ec':'none','pad':3})
    ax.text(0,-1.12,'Lower half-plane',ha='center',fontsize=16,color=BLUE,weight='bold')
    ax.text(0,-1.66,'Boundary values glue on the real axis.',ha='center',fontsize=12,color=BLUE)
    bx=fig.add_axes([.59,.25,.35,.43]);yy=np.linspace(-2,2,401);r=math.log(2)
    bx.plot(yy,np.exp(r*np.abs(yy)),color=TEAL,lw=3,ls='--',label=r'bound $2^{|\operatorname{Im}z|}$')
    bx.plot(yy,np.exp(-r*yy),color=BLUE,lw=2,label=r'exact $|2^{iz}|=2^{-\operatorname{Im}z}$')
    bx.axhline(1,color='#b7c4ca',lw=1);bx.axvline(0,color='#b7c4ca',lw=1)
    bx.set(xlabel=r'$\operatorname{Im}z$',ylabel='norm',title=r'Scalar model: $\psi=2\varphi$, $r=\log 2$',xlim=(-2,2),ylim=(0,4.5))
    bx.legend(frameon=False,fontsize=12,loc='upper center');bx.grid(alpha=.15)
    fig.text(.08,.135,r'$U^{-1}(z)=U^\sharp(z)=U(\overline{z})^*$',fontsize=19)
    fig.text(.59,.135,'Curves are numerical samples of exact scalar formulas.',fontsize=12,color=MUTED)
    footer(fig,'Proof: Uniform distance and limits of weights, §2 (#um-entire), (UM3)–(UM5); scalar model: §8 (#um-model), item 5.  The scalar example illustrates the bound, not the general proof.')
    save(fig,'metric-entire-growth')

def cauchy():
    fig=canvas('One metric bound controls every positive evaluation',
        r'On $\ell^\infty(\mathbb{N})$ with counting trace, $n\geq1$: $h_n=2^{-n}$, $k_n^{(m)}=2^{-n}\exp((-1)^n/m)$.')
    fig.text(.05,.80,r'$d(\tau_{k^{(m)}},\tau_h)=1/m,\qquad d(\tau_{k^{(m)}},\tau_{k^{(l)}})=|1/m-1/l|$',fontsize=21,color=TEAL)
    ax=fig.add_axes([.075,.28,.38,.40]);nn=np.arange(1,13)
    for m,color in [(1,GOLD),(2,BLUE),(4,TEAL)]:ax.plot(nn,(-1.)**nn/m,'o-',lw=1.3,ms=5,color=color,label=fr'$m={m}$')
    ax.axhline(0,color=MUTED,lw=.9);ax.set(xlabel=r'coordinate $n$ (first 12 shown)',ylabel=r'$\log(k_n^{(m)}/h_n)$',xlim=(.6,12.4),ylim=(-1.2,1.2),title='A. Exact alternating logarithmic errors')
    ax.set_xticks([1,2,4,6,8,10,12]);ax.legend(frameon=False,loc='upper right',fontsize=11);ax.grid(alpha=.13)
    bx=fig.add_axes([.565,.28,.38,.40]);mm=np.linspace(1,20,400);lo=np.exp(-1/mm);hi=np.exp(1/mm)
    bx.fill_between(mm,lo,hi,color='#d9eee8',label='all positive evaluations')
    bx.plot(mm,hi,color=TEAL,lw=1.7,label=r'$e^{1/m}$');bx.plot(mm,lo,color=TEAL,lw=1.7,label=r'$e^{-1/m}$')
    exact=(2*lo+hi)/3
    bx.plot(mm,exact,color=BLUE,lw=2,label=r'$x=1$: $(2e^{-1/m}+e^{1/m})/3$')
    bx.axhline(1,color=MUTED,lw=.9,ls='--');bx.set(xlabel=r'sequence index $m$',ylabel=r'$\tau_{k^{(m)}}(x)/\tau_h(x)$',xlim=(1,20),ylim=(.25,2.85),title='B. Uniform multiplicative band')
    bx.set_xticks([1,5,10,15,20]);bx.legend(frameon=False,fontsize=10.5,loc='upper right');bx.grid(alpha=.13)
    fig.text(.075,.145,r'$\sup_{n\geq1}|\log k_n^{(m)}-\log h_n|=1/m$',fontsize=18)
    fig.text(.565,.145,r'$e^{-1/m}\leq\dfrac{\tau_{k^{(m)}}(x)}{\tau_h(x)}\leq e^{1/m}$',fontsize=21,color=TEAL)
    fig.text(.075,.088,'Both densities are faithful and summable; their inverses are unbounded.',fontsize=12)
    fig.text(.565,.088,r'Every nonzero $x\in\ell^\infty(\mathbb{N})_+$; $0<\tau_h(x)<\infty$.',fontsize=12)
    footer(fig,'Proof: §5 (#um-evaluations), (UM15), and §8 (#um-model), (UM25)–(UM27).  Panel A displays exact finite samples; panel B samples the exact band, with integer m as sequence indices.')
    save(fig,'metric-cauchy-evaluations')

def noncommuting():
    fig=canvas('The exact noncommuting distance is log 4',
        r'$\varphi=\mathrm{Tr}(h\,\cdot)$, $\psi=\mathrm{Tr}(k\,\cdot)$ on $M_2(\mathbb{C})$; $h k\ne k h$.',size=(16,9))
    ax=fig.add_axes([.05,.33,.26,.48]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    matrix(ax,.16,.82,[[1,0],[0,3]],r'$h=$',.11,BLUE)
    matrix(ax,.16,.49,[[3,1],[1,3]],r'$k=$',.11,TEAL)
    ax.text(0,.23,r'$\operatorname{spec}(h)=\{1,3\}$',fontsize=17,color=BLUE)
    ax.text(0,.11,r'$\operatorname{spec}(k)=\{2,4\}$',fontsize=17,color=TEAL)
    bx=fig.add_axes([.355,.33,.31,.48]);bx.set(xlim=(0,1),ylim=(0,1));bx.axis('off')
    bx.text(0,.98,r'Test the low cutoff at $c=e^r$.',fontsize=16,weight='bold',va='top')
    bx.text(0,.83,r'$\operatorname{Ran}E_{ch}([0,c])=\mathbb{C}e_1$',fontsize=17,color=BLUE)
    bx.text(0,.66,r'Range of $E_k([0,c])$:',fontsize=15,color=TEAL)
    rows=[(r'$1\leq c<2$',r'$\{0\}$','fails'),(r'$2\leq c<4$',r'$\mathbb{C}(1,-1)$','fails'),(r'$c=4$',r'$\mathbb{C}^2$','passes')]
    for j,(interval,subspace,status) in enumerate(rows):
        yy=.49-j*.17
        bx.text(0,yy,interval,fontsize=14)
        bx.text(.36,yy,subspace,fontsize=14,color=TEAL)
        bx.text(.98,yy,status,fontsize=12,ha='right',color=RED if status=='fails' else TEAL)
    bx.text(0,-.05,'The test is range containment,\nnot a comparison of ranks.',fontsize=14,color=RED)
    cx=fig.add_axes([.74,.35,.22,.40]);cx.set_aspect('equal');cx.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel=r'first real coordinate',ylabel=r'second real coordinate')
    cx.axhline(0,color=BLUE,lw=2.6);tt=np.array([-1.2,1.2]);cx.plot(tt,-tt,color=TEAL,lw=2.6)
    cx.scatter([1],[0],s=70,color=BLUE,zorder=4);cx.text(.68,.17,r'$e_1$',fontsize=17,color=BLUE)
    cx.text(-1.15,1.07,r'$(1,-1)$ line',fontsize=12,color=TEAL)
    cx.set_title(r'$2\leq c<4$',fontsize=17);cx.set_xticks([-1,0,1]);cx.set_yticks([-1,0,1]);cx.grid(alpha=.13)
    fig.text(.05,.20,r'Upper bound, every $p>0$:',fontsize=16,weight='bold')
    fig.text(.34,.20,r'$k^p\leq4^p I\leq4^p h^p,\qquad h^p\leq3^p I\leq4^p k^p$',fontsize=20,color=TEAL)
    fig.text(.05,.12,r'Lower bound: if $1\leq c<4$, $E_{ch}([0,c])\nleq E_k([0,c])$; the comparison $\psi\preceq_\infty c\varphi$ fails.',fontsize=17,color=RED)
    footer(fig,'Proof: §8 (#um-model), (UM28), using the projection criterion in Comparing weights through strips and spectral tails, §4 (#wo-tails), (WO13).  Exact real slices of complex spectral subspaces.')
    save(fig,'metric-noncommuting-log4')

def main():
    entire();cauchy();noncommuting()
    h=np.diag([1.,3.]);k=np.array([[3.,1.],[1.,3.]])
    minus=np.array([1.,-1.])/math.sqrt(2);pminus=np.outer(minus,minus);e1=np.array([1.,0.])
    diagnostic={'noncommuting_example':{'h':h.tolist(),'k':k.tolist(),'commutator':(h@k-k@h).tolist(),
        'h_spectrum':np.linalg.eigvalsh(h).tolist(),'k_spectrum':np.linalg.eigvalsh(k).tolist(),
        'low_k_projection_between_2_and_4':pminus.tolist(),'squared_distance_e1_to_low_k_range':float(np.sum((e1-pminus@e1)**2)),
        'exact_distance':'log(4)','distance_numerical':math.log(4),'upper_bound_scope':'all positive powers, proved by spectral bounds'},
        'cauchy_example':{'index_start':1,'exact_sum_h':1,'exact_sum_h_odd': '2/3','exact_sum_h_even':'1/3',
        'exact_distance_to_h':'1/m','exact_pair_distance':'abs(1/m-1/l)','density_inverses':'unbounded',
        'identity_evaluation_ratio':'(2*exp(-1/m)+exp(1/m))/3','m1_identity_evaluation_numerical':(2*math.exp(-1)+math.exp(1))/3},
        'scalar_entire_example':{'ratio':2,'exact_distance':'log(2)','exact_U':'exp(i*z*log(2))','exact_modulus':'exp(-Im(z)*log(2))'},
        'font':'Matplotlib-installed DejaVu Sans; no font files copied','outputs':['metric-entire-growth','metric-cauchy-evaluations','metric-noncommuting-log4'],
        'rendered_formats':['png','svg']}
    assert np.allclose(np.linalg.eigvalsh(k),[2,4])
    assert np.isclose(diagnostic['noncommuting_example']['squared_distance_e1_to_low_k_range'],.5)
    assert not np.allclose(h@k,k@h)
    (HERE/'diagnostics.json').write_text(json.dumps(diagnostic,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(diagnostic,indent=2))

if __name__=='__main__':main()
