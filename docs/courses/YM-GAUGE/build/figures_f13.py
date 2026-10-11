"""Reproducible plots of the exact one-loop coefficient and scale formulas."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures'
INK='#173f4a';TEAL='#187c78';BLUE='#445fa6';OCHRE='#a75c18'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor=fig.get_facecolor())
    fig.savefig(OUT/(name+'.png'),dpi=145,metadata={'Software':'YM-GAUGE reproducible figure'},facecolor=fig.get_facecolor())
    plt.close(fig)
def build():
    OUT.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':INK,
      'xtick.color':INK,'ytick.color':INK,'svg.hashsalt':'YM-F13-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
    fig,ax=plt.subplots(figsize=(11.4,7.5));fig.subplots_adjust(left=.1,right=.96,bottom=.27,top=.77)
    fig.suptitle('Where the one-loop coefficient comes from',fontsize=19,y=.96,weight='bold')
    fig.text(.09,.85,r'Each displayed coefficient multiplies $N J(B)/(16\pi^2)$. The original $J(B)$ retains all ordered indices.',fontsize=12)
    vals=[2,-1/3,1/6,11/6];labs=['Vector endomorphism','Vector curvature','Ghost curvature','Complete sum']
    ax.bar(range(4),vals,color=[TEAL,OCHRE,BLUE,INK],width=.6)
    ax.axhline(0,color=INK,lw=1);ax.set_ylim(-.65,2.45);ax.set_yticks([-.5,0,.5,1,1.5,2]);ax.grid(axis='y',alpha=.2)
    ax.set_xticks(range(4),labs,fontsize=11);ax.set_ylabel('Coefficient of the stated common factor')
    for i,(v,label) in enumerate(zip(vals,[r'$2$',r'$-1/3$',r'$1/6$',r'$11/6$'])):ax.text(i,v+(.1 if v>=0 else -.19),label,ha='center',fontsize=17)
    fig.text(.08,.16,r'$A_B=\dfrac{11N}{96\pi^2}J(B)=\dfrac{b_0}{2}J(B),\qquad b_0=\dfrac{11N}{48\pi^2},\qquad \beta^{(1)}(g)=-b_0g^3.$',fontsize=17)
    fig.text(.08,.055,'Proof: RG.10–RG.12, RG.20 and RG.23–RG.26. No division by J(B) is needed for the displayed identity.',fontsize=11)
    save(fig,'f13-coefficient')
    t=np.linspace(0,25,501);runs={}
    fig,ax=plt.subplots(figsize=(11.4,7.5));fig.subplots_adjust(left=.1,right=.94,bottom=.28,top=.78)
    fig.suptitle('The exact one-loop flow at increasing scale',fontsize=19,y=.96,weight='bold')
    fig.text(.09,.86,r'$g(\mu)=g_0/[1+2b_0g_0^2\log(\mu/\mu_0)]^{1/2}$; $b_0=11N/(48\pi^2)$; illustrative $g_0=1$.',fontsize=13)
    for n,color in [(2,BLUE),(3,TEAL)]:
        vals=1/np.sqrt(1+2*11*n/(48*np.pi**2)*t);runs[str(n)]=vals.tolist()
        ax.plot(t,vals,color=color,lw=2.5,label='SU('+str(n)+')')
    ax.set_xlim(0,25);ax.set_ylim(.3,1.07);ax.set_xlabel(r'$t=\log(\mu/\mu_0)$',loc='center');ax.set_ylabel(r'$g(\mu)$',loc='center');ax.legend();ax.grid(alpha=.2)
    fig.text(.08,.16,r'Full domain: $\mu>\Lambda_{\rm tr}=\mu_0\exp[-1/(2b_0g_0^2)]$. The graph shows only $\mu\geq\mu_0$.',fontsize=13)
    fig.text(.08,.10,r'Physical energy: $Q=\hbar c\mu$; $Q/Q_0=\mu/\mu_0$. The negative branch is the exact negative of this graph.',fontsize=12)
    fig.text(.08,.045,'Proof: RG.26–RG.29 and F13.4. A one-loop flow; no higher-loop or infrared spectral conclusion is plotted.',fontsize=11)
    save(fig,'f13-running')
    x=np.linspace(2,12,501);h=lambda z:np.log1p(z)+z/(1+z)
    limit=-np.log(4);error=h(4/x**2)-h(1/x**2);values=limit+error;bound=6/x**2
    fig,ax=plt.subplots(figsize=(11.4,7.5));fig.subplots_adjust(left=.1,right=.94,bottom=.29,top=.78)
    fig.suptitle('A finite subtraction with a proved cutoff-error bound',fontsize=18,y=.96,weight='bold')
    fig.text(.09,.86,r'Exact choice $M=2\mu$, $\mu>0$. Full difference $D_\Lambda=I_\Lambda(M)-I_\Lambda(\mu)$.',fontsize=13)
    ax.fill_between(x,limit-bound,limit+bound,color=TEAL,alpha=.09,label='Proved error interval')
    ax.plot(x,limit+bound,color=TEAL,ls='--',lw=1.3);ax.plot(x,limit-bound,color=TEAL,ls='--',lw=1.3)
    ax.plot(x,values,color=BLUE,lw=2.5,label='Exact finite-cutoff value')
    ax.axhline(limit,color=OCHRE,lw=1.8,label=r'Exact limit $-\log4$')
    ax.set_xlim(2,12);ax.set_ylim(-3.05,.3);ax.set_xlabel(r'$\Lambda/\mu$',loc='center');ax.set_ylabel(r'$16\pi^2 D_\Lambda$',loc='center');ax.legend(loc='lower right',fontsize=10);ax.grid(alpha=.2)
    fig.text(.08,.17,r'$16\pi^2D_\Lambda=-\log4+h(4\mu^2/\Lambda^2)-h(\mu^2/\Lambda^2),\quad h(z)=\log(1+z)+z/(1+z).$',fontsize=13)
    fig.text(.08,.105,r'$0<16\pi^2(D_\Lambda-D_\infty)\leq6\mu^2/\Lambda^2$; the exact error decreases with $\Lambda$.',fontsize=13)
    fig.text(.08,.045,'Proof: RG.35–RG.38, F13.5 and F13.13. The shaded region is a proved bound, not a statistical interval.',fontsize=11)
    save(fig,'f13-subtraction')
    (OUT/'f13-figure-data.json').write_text(json.dumps({'coefficient':{'exact_values':['2','-1/3','1/6','11/6'],'common_factor':'N J(B)/(16 pi²)'},
      'running':{'display_x':'t=log(mu/mu0)','g0':1,'t':t.tolist(),'g':runs,'formula':'g0/sqrt(1+2 b0 g0² t), b0=11N/(48pi²)'},
      'subtraction':{'M_over_mu':2,'Lambda_over_mu':x.tolist(),'display_values':values.tolist(),'display_limit':float(limit),'display_error_bound':bound.tolist(),'vertical_multiplier':'16pi²'}},separators=(',',':'))+'\n',encoding='utf8')
if __name__=='__main__':build()
