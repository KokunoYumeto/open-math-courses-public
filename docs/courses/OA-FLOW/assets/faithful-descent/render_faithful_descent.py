"""Exact scalar spectral-window sample and the general finite-domain proof map.

Original figure/code: CC0-1.0 to the extent of rights held.
"""
import argparse,json,math
from fractions import Fraction
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent/'assets')
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.hashsalt':'oa-flow-faithful-descent-20261004','axes.spines.top':False,'axes.spines.right':False})
    fig=plt.figure(figsize=(12,8.5),dpi=200,facecolor='#f5f8fc')
    fig.text(.5,.968,'Faithful descent: one spectral window, the whole weight',ha='center',fontsize=20,color='#18364b')
    fig.text(.5,.932,r'General mechanism: $\tau\beta=\lambda\tau$, $\Psi\beta=\Psi$, $\Psi=\tau_H$, $0<\lambda<1$.',
             ha='center',fontsize=13,color='#4b607b')
    ax=fig.add_axes([.085,.56,.405,.30],facecolor='white')
    ax.set_title(r'A. Exact scalar sample: $\lambda=1/2$, $H_n=(3/4)2^{-n}$',fontsize=13,pad=14)
    for n in range(-2,3):
        y=-n
        left,right=-n-1,-n
        ax.plot([left,right],[y,y],color='#8bb1d3',linewidth=9,alpha=.45,solid_capstyle='butt')
        ax.plot(left,y,'o',color='#1e6d9f',markersize=6)
        ax.plot(right,y,'o',markeredgecolor='#1e6d9f',markerfacecolor='white',markersize=6,zorder=5)
        ax.plot(math.log2(.75)-n,y,'D',color='#b65035',markersize=6,zorder=6)
    ax.set_xlim(-3.3,2.4);ax.set_ylim(-2.6,2.6)
    ax.set_yticks([-2,-1,0,1,2],['n=2','n=1','n=0','n=-1','n=-2'])
    ax.set_xlabel(r'$\log_2 r$: interval $[-n-1,-n)$, diamond at $\log_2 H_n$',fontsize=10.5)
    ax.grid(axis='x',alpha=.2)
    bx=fig.add_axes([.61,.56,.33,.30],facecolor='white')
    ns=list(range(-3,4));tm=[2.**n for n in ns];hm=[.75*2.**(-n) for n in ns]
    bx.plot(ns,tm,'o-',color='#1e6d9f',label=r'$\tau(e_n)=2^n$')
    bx.plot(ns,hm,'s--',color='#b65035',label=r'$H_n=(3/4)2^{-n}$')
    bx.plot(ns,[.75]*7,':',linewidth=2.5,color='#39795f',label=r'$\tau(k_n)=3/4$')
    bx.set_yscale('log',base=2);bx.set_ylim(.0625,16);bx.set_xticks(ns)
    bx.set_xlabel('Integer n: a finite sample of the full family',fontsize=10.5)
    bx.set_ylabel('Exact scalar masses');bx.set_title('B. Trace and density factors cancel',fontsize=13,pad=14)
    bx.set_yticks([.125,.25,.5,1,2,4,8],['1/8','1/4','1/2','1','2','4','8'])
    bx.legend(fontsize=10,loc='upper right');bx.grid(alpha=.2)
    fig.text(.5,.468,r'Full identity: $\widehat{\varphi_F}(E(y))=\sum_n\tau_{\lambda^n\beta^{-n}(d)}(y)=\tau_H(y)=\Psi(y)$',
             ha='center',fontsize=15,color='#18364b')
    fig.text(.5,.429,r'$d=H1_{[\lambda,1)}(H)$; all sums are suprema of finite nonnegative subsums, including infinity.',
             ha='center',fontsize=11,color='#4b607b')
    fx=fig.add_axes([.025,.095,.95,.285]);fx.set_xlim(0,1);fx.set_ylim(0,1);fx.axis('off')
    boxes=[
        (.02,.34,.285,.62,'C. Spectral centralizer cutoffs',
         r'$q_J=\sum_{j\in J}\beta^j(p)\uparrow1$'+'\n'+r'$q_J\in B_\Psi$, $E(q_J)=|J|1$'+'\n'+r'$z=xq_J\in N_\Psi\cap N_E$'+'\n'+r'$\Psi(z^*z)\leq\Psi(x^*x)$'),
        (.357,.34,.285,.62,'D. Bounded finite images',
         r'$a_z=E(z^*z)\in F_+$'+'\n'+r'$\varphi_F(a_z)=\Psi(z^*z)<\infty$'+'\n'+r'$r\,a_z\,r=0\Rightarrow zr=0$'+'\n'+'Density of common ideal forces r=0.'),
        (.695,.34,.285,.62,'E. Semifiniteness and uniqueness',
         r'$\bigvee_z s(a_z)=1$'+'\n'+r'$1_{[\epsilon,\infty)}(a_z)\leq a_z/\epsilon$'+'\n'+'Finite thresholds fill 1 (GW-4).'+'\n'+r'$E(x^{1/2}px^{1/2})=x$')]
    for x,y,w,ht,title,body in boxes:
        fx.add_patch(FancyBboxPatch((x,y),w,ht,boxstyle='round,pad=0.008',facecolor='white',edgecolor='#779fc1',linewidth=1.3))
        fx.text(x+w/2,y+ht-.095,title,ha='center',fontsize=10.5,color='#18364b')
        fx.text(x+w/2,y+ht-.2,body,ha='center',va='top',fontsize=10.5,linespacing=1.5,color='#25455f')
    for left,right in ((.305,.35),(.642,.688)):
        fx.add_patch(FancyArrowPatch((left,.63),(right,.63),arrowstyle='->',mutation_scale=15,color='#607c98',linewidth=1.5))
    fx.text(.5,.18,r'Exact finite ideal: $N_{\varphi_F}=\{x\in F:px\in N_\Psi\}$; no commutation of $p$ with $F$ is assumed.',
            ha='center',fontsize=11,color='#18364b')
    fx.text(.5,.015,'A/B are scalar samples; C/D/E are the proved arbitrary-algebra mechanism. No type classification or cocycle realization.',
            ha='center',fontsize=9.5,color='#4b607b')
    prefix=args.output_dir/'faithful-descent'
    fig.savefig(prefix.with_suffix('.png'),dpi=200,metadata={'Software':'OA-FLOW original deterministic mathematical illustration'})
    fig.savefig(prefix.with_suffix('.svg'),metadata={'Date':None,'Creator':'OA-FLOW original mathematical illustration'})
    plt.close(fig)
    data={'scope':'Exact scalar model, not a finite-dimensional crossed product or a proof by numerical approximation',
          'lambda':'1/2','c':'3/4','native_pixels':[2400,1700],
          'samples':[{'n':n,'trace_mass':str(Fraction(2)**n),'density':str(Fraction(3,4)*Fraction(2)**(-n)),
                      'paired_mass':'3/4','spectral_interval':['2^'+str(-n-1),'2^'+str(-n)],'left_closed':True,'right_closed':False}
                     for n in ns]}
    (args.output_dir/'faithful-descent-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':main()
