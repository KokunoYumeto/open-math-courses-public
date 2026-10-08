"""Original CC0 diagrams for Comparing weights through strips and spectral tails.

Run: python -B generate_order_figures.py
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
from matplotlib.patches import FancyBboxPatch, Circle

HERE = Path(__file__).resolve().parent
BG, INK, MUTED = '#fcfbf7', '#172d3c', '#536575'
BLUE, TEAL, RED, GOLD = '#236c9c', '#087e80', '#b4443f', '#b88024'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'dejavusans',
    'font.size': 13, 'text.color': INK, 'axes.labelcolor': INK, 'axes.edgecolor': '#9ba9b1',
    'xtick.color': MUTED, 'ytick.color': MUTED, 'figure.facecolor': BG,
    'axes.facecolor': BG, 'savefig.facecolor': BG, 'svg.fonttype': 'path',
    'svg.hashsalt': 'oa-flow-weight-order-20261007', 'axes.spines.top': False,
    'axes.spines.right': False})

def save(fig, stem):
    fig.savefig(HERE / (stem + '.png'), dpi=160)
    fig.savefig(HERE / (stem + '.svg'), metadata={'Date': None, 'Creator': 'Original OA-FLOW mathematical illustration', 'Rights': 'CC0-1.0'})
    plt.close(fig)

def canvas(title, subtitle, size=(15, 8.5)):
    fig = plt.figure(figsize=size)
    fig.text(.05, .95, title, fontsize=24, weight='bold', va='top')
    fig.text(.05, .894, subtitle, fontsize=13, color=MUTED, va='top')
    return fig

def footer(fig, text):
    fig.text(.05, .035, text, fontsize=10.5, color=MUTED, va='bottom')

def box(ax, xy, width, height, label, color=BLUE, size=17):
    x,y=xy
    patch=FancyBboxPatch((x,y),width,height,boxstyle='round,pad=0.014,rounding_size=0.025',
        linewidth=1.5,edgecolor=color,facecolor='white')
    ax.add_patch(patch)
    ax.text(x+width/2,y+height/2,label,ha='center',va='center',fontsize=size,color=color)

def arrow(ax, start, end, text='', color=INK, dy=.025):
    ax.annotate('',end,start,arrowprops={'arrowstyle':'-|>','lw':1.7,'color':color,'mutation_scale':16})
    if text: ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+dy,text,ha='center',fontsize=12,color=color)

def matrix(ax, x, y, data, label, scale=.085, color=INK):
    rows,cols=len(data),len(data[0]); w=cols*scale; h=rows*scale
    ax.text(x-.025,y,label,ha='right',va='center',fontsize=17,color=color)
    for i,row in enumerate(data):
        for j,value in enumerate(row):
            ax.text(x+(j+.5)*scale,y+h/2-(i+.5)*scale,str(value),ha='center',va='center',fontsize=18,color=color)
    for xx,sgn in [(x-0.012,1),(x+w+.012,-1)]:
        ax.plot([xx+sgn*.012,xx,xx,xx+sgn*.012],[y+h/2+.012,y+h/2+.012,y-h/2-.012,y-h/2-.012],color=color,lw=1.5)

def reflection():
    fig=canvas('A positive test in the core recovers every weight value',
        r'$M$ arbitrary; $C=M\rtimes_\sigma\mathbb{R}$, coefficient embedding $\pi$, normalized averaging weight $T$.')
    ax=fig.add_axes([.05,.14,.90,.69]); ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
    ax.text(.02,.93,r'Choose $f\in C_c(\mathbb{R})$ with $\|f\|_2=1$:',fontsize=15)
    ax.text(.55,.93,r'$T(\lambda(f)^*\lambda(f))=1$',fontsize=19,color=TEAL)
    box(ax,(.03,.63),.22,.15,r'$x\in M_+$',BLUE)
    box(ax,(.385,.63),.22,.15,r'$X_x\in C_+$',TEAL)
    box(ax,(.745,.63),.22,.15,r'$\pi(x)$',BLUE)
    arrow(ax,(.25,.705),(.385,.705),'positive lift')
    arrow(ax,(.605,.705),(.745,.705),r'$T$')
    ax.text(.50,.535,r'$X_x=\pi(x^{1/2})\lambda(f)^*\lambda(f)\pi(x^{1/2})$',ha='center',fontsize=20)
    ax.text(.50,.462,'The bimodule identity makes the averaging map onto the bounded positive coefficients.',ha='center',fontsize=13,color=MUTED)
    box(ax,(.15,.205),.70,.145,r'$\widetilde\eta(X_x)=\eta(x)\quad\leq\quad\nu(x)=\widetilde\nu(X_x)$',TEAL,20)
    arrow(ax,(.50,.435),(.50,.366),'',TEAL)
    ax.text(.50,.105,r'$\widetilde\eta\leq\widetilde\nu\quad\Longrightarrow\quad\eta\leq\nu$',ha='center',fontsize=23,color=TEAL)
    ax.text(.50,.015,r'For every $x\in M_+$, including values in $[0,\infty]$. No subtraction of infinite values.',ha='center',fontsize=13)
    footer(fig,'Proof: Comparing weights through strips and spectral tails, §2 (#wo-dual-order), (WO4)–(WO8).  Diagram of exact identities; no finite-dimensional assumption.')
    save(fig,'order-reflection')

def obstruction():
    fig=canvas('Half-depth order does not force depth-one order',
        r'On $M_2(\mathbb{C})$: $\varphi=\mathrm{Tr}(h\,\cdot)$, $\psi=\mathrm{Tr}(k\,\cdot)$; strip depth $a$ tests $h^{2a}\leq k^{2a}$.')
    ax=fig.add_axes([.05,.17,.47,.64]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
    matrix(ax,.13,.87,[[1,0],[0,2]],r'$h=$',.092,BLUE)
    matrix(ax,.65,.87,[[2,1],[1,3]],r'$k=$',.092,TEAL)
    ax.text(.00,.65,r'Depth $a=\frac{1}{2}$ passes',fontsize=19,color=TEAL,weight='bold')
    matrix(ax,.32,.49,[[1,1],[1,1]],r'$k-h=$',.081,TEAL)
    ax.text(.58,.49,r'$\geq0$',fontsize=19,va='center',color=TEAL)
    ax.text(.00,.30,r'Depth $a=1$ fails',fontsize=19,color=RED,weight='bold')
    matrix(ax,.32,.14,[[4,5],[5,6]],r'$k^2-h^2=$',.081,RED)
    ax.text(.64,.14,r'$\xi=(5,-4)$',fontsize=16,ha='left',va='center')
    ax.text(.00,-.03,r'$\langle(k^2-h^2)\xi,\xi\rangle=-4$',fontsize=18,color=RED)
    bx=fig.add_axes([.61,.23,.33,.56]);bx.set_aspect('equal');bx.set(xlim=(-.6,9.3),ylim=(-10,1),xlabel='first coordinate',ylabel='second coordinate')
    bx.axhline(0,color='#c3cbd0',lw=1);bx.axvline(0,color='#c3cbd0',lw=1)
    bx.add_patch(Circle((0,0),math.sqrt(85),fill=False,ls='--',lw=1.3,ec=BLUE,alpha=.7))
    for end,color in [((6,-7),BLUE),((5,-8),RED)]:
        bx.annotate('',end,(0,0),arrowprops={'arrowstyle':'-|>','color':color,'lw':2.5,'mutation_scale':18})
        bx.scatter(*end,color=color,s=40,zorder=5)
    bx.text(6.2,-6.9,r'$k\xi=(6,-7)$',fontsize=13,color=BLUE)
    bx.text(.5,-8.65,r'$h\xi=(5,-8)$',fontsize=13,color=RED)
    bx.text(.02,.98,r'$B_1=hk^{-1}:\ k\xi\longmapsto h\xi$',transform=bx.transAxes,fontsize=15,va='top')
    bx.text(.04,.40,r'$\|k\xi\|^2=85$'+'\n'+r'$\|h\xi\|^2=89$',transform=bx.transAxes,fontsize=17,bbox={'fc':BG,'ec':'none','alpha':.92})
    fig.text(.61,.13,r'$\|B_1\|^2\geq 89/85>1$.',fontsize=16,color=RED)
    fig.text(.61,.087,'The forced endpoint is not contractive.',fontsize=13,color=RED)
    footer(fig,'Proof: §7 (#wo-model), (WO24)–(WO25); endpoint mechanism: §3 (#wo-strips), (WO10).  Exact vectors and squared norms; no claim about the maximal strip depth.')
    save(fig,'order-depth-obstruction')

def halfplane():
    fig=canvas('The lower half-plane selects nonpositive frequencies',
        r'Convention: $\widehat f(p)=\int f(t)e^{itp}\,dt$.  A mode $e^{itp}x$ continues as $e^{izp}x$, with $|e^{i(t-iy)p}|=e^{yp}$.',size=(16,8.8))
    axs=[fig.add_axes([.055,.31,.265,.48]),fig.add_axes([.375,.31,.265,.48]),fig.add_axes([.695,.31,.265,.48])]
    ax,bx,cx=axs
    ss=np.linspace(-5,5,701)
    for y,color in [(.25,BLUE),(.65,TEAL),(1.4,GOLD)]:ax.plot(ss,y/(np.pi*(ss*ss+y*y)),color=color,lw=2,label=fr'$y={y:g}$')
    ax.set(xlabel=r'$s$',ylabel=r'$P_y(s)$',xlim=(-5,5),ylim=(0,1.4),title='A. Positive averaging kernels')
    ax.legend(frameon=False,fontsize=11);ax.grid(alpha=.15)
    ax.text(.5,-.24,r'$P_y(s)=\dfrac{y}{\pi(s^2+y^2)},\quad\int P_y=1$',transform=ax.transAxes,ha='center',fontsize=15)
    t=np.linspace(-2,2,81);im=np.linspace(-3,0,101)
    zz=np.tile(np.exp(im)[:,None],(1,len(t)))
    bx.pcolormesh(t,im,zz,cmap='Blues',vmin=0,vmax=1,shading='nearest')
    bx.set(xlabel=r'$t=\operatorname{Re}z$',ylabel=r'$\operatorname{Im}z=-y$',title=r'B. Scalar mode $p=-1$')
    bx.axhline(0,color=BLUE,lw=2)
    for y in [0,1,2,3]: bx.text(-1.8,-y-.04 if y<3 else -2.93,fr'$|e^{{-iz}}|=e^{{-{y}}}$' if y else r'$|e^{-it}|=1$',fontsize=13,va='top' if y<3 else 'bottom',color='white' if y<.5 else INK)
    bx.text(.5,-.24,r'$z=t-iy,\ y\geq0$',transform=bx.transAxes,ha='center',fontsize=15)
    yy=np.linspace(0,3,301)
    for p,color,lab in [(-1,BLUE,r'$p=-1$: decay'),(0,TEAL,r'$p=0$: constant'),(1,RED,r'$p=+1$: growth')]:cx.plot(yy,np.exp(p*yy),color=color,lw=2.3,label=lab)
    cx.set(yscale='log',xlabel=r'depth $y$',ylabel=r'$|e^{i(t-iy)p}|$',title='C. The sign is decisive',xlim=(0,3),ylim=(.04,25))
    cx.legend(frameon=False,fontsize=11,loc='upper left');cx.grid(alpha=.15)
    cx.text(.5,-.24,r'$p\leq0\ \Longleftrightarrow\ e^{yp}\leq1\ (y\geq0)$',transform=cx.transAxes,ha='center',fontsize=15)
    fig.text(.055,.135,r'General construction: $F(t-iy)=\int P_y(s)\alpha_{t+s}(x)\,ds$, when $\mathrm{Sp}_\alpha(x)\subseteq(-\infty,0]$.',fontsize=16)
    fig.text(.055,.08,r'Balanced corner: for $\varphi=e^{-1}\psi$, $e_{12}$ has frequency $-1$ and $e_{21}$ has frequency $+1$. Zero frequency is included.',fontsize=13)
    footer(fig,'Proof: §5 (#wo-half-plane), (WO14)–(WO20), and §6 (#wo-balanced), (WO21)–(WO23).  Curves and shading are numerical samples of the displayed exact scalar formulas.')
    save(fig,'order-half-plane-sign')

def power(a,p):
    w,v=np.linalg.eigh(a)
    return (v*w**p)@v.T

def main():
    reflection(); obstruction(); halfplane()
    h=np.diag([1.,2.]);k=np.array([[2.,1.],[1.,3.]]);xi=np.array([5.,-4.])
    diagnostic={'matrix_example':{'h':h.tolist(),'k':k.tolist(),'eigenvalues_k_minus_h':np.linalg.eigvalsh(k-h).tolist(),
        'k2_minus_h2':(k@k-h@h).tolist(),'quadratic_form_on_xi':float(xi@(k@k-h@h)@xi),
        'input_k_xi':(k@xi).tolist(),'output_h_xi':(h@xi).tolist(),'input_squared_norm':int(np.dot(k@xi,k@xi)),
        'output_squared_norm':int(np.dot(h@xi,h@xi)),
        'half_depth_endpoint_norm_numerical':float(np.linalg.norm(power(h,.5)@power(k,-.5),2)),
        'depth_one_endpoint_norm_numerical':float(np.linalg.norm(h@np.linalg.inv(k),2))},
        'poisson':{'exact_total_mass':1,'exact_transform':'exp(-y*abs(p))','normalization':'Lebesgue dt'},
        'sign':{'convention':'hat f(p)=integral f(t) exp(i t p) dt','exact_mode_modulus_at_t_minus_iy':'exp(y*p)','scalar_ratio': 'exp(-1)','e12_frequency':-1,'e21_frequency':1},
        'font':'Matplotlib-installed DejaVu Sans; no font files copied',
        'outputs':['order-reflection','order-depth-obstruction','order-half-plane-sign'],'rendered_formats':['png','svg']}
    assert diagnostic['matrix_example']['input_squared_norm']==85
    assert diagnostic['matrix_example']['output_squared_norm']==89
    assert diagnostic['matrix_example']['quadratic_form_on_xi']==-4
    assert abs(diagnostic['matrix_example']['half_depth_endpoint_norm_numerical']-1)<1e-12
    (HERE/'diagnostics.json').write_text(json.dumps(diagnostic,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(diagnostic,indent=2))

if __name__=='__main__':main()
