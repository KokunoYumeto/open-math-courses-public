"""Exact formulas and explicit display maps for the free quantum lesson."""
from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermval
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'figures'
INK='#173f4a';TEAL='#187c78';BLUE='#445fa6';OCHRE='#a75c18';RED='#a24363'
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None},facecolor=fig.get_facecolor())
    fig.savefig(OUT/(name+'.png'),dpi=145,metadata={'Software':'YM-GAUGE reproducible figure'},facecolor=fig.get_facecolor())
    plt.close(fig)
def build():
    OUT.mkdir(exist_ok=True)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'text.color':INK,
      'axes.labelcolor':INK,'axes.edgecolor':INK,'xtick.color':INK,'ytick.color':INK,
      'svg.hashsalt':'YM-F11-20261010','figure.facecolor':'#fffef9','axes.facecolor':'#fffef9'})
    hbar=6.62607015e-34/(2*np.pi);M=2e-26;Omega=3e13;beta=M*Omega/hbar
    q=np.linspace(-4/np.sqrt(beta),4/np.sqrt(beta),1001)
    fig,axs=plt.subplots(1,2,figsize=(11.4,7.2))
    fig.subplots_adjust(left=.15,right=.96,bottom=.28,top=.79,wspace=.36)
    fig.suptitle('The oscillator: exact states and absolute energies',fontsize=19,y=.97,weight='bold')
    fig.text(.07,.90,r'$M=2\times10^{-26}\,\mathrm{kg}$; $\Omega=3\times10^{13}\,\mathrm{s}^{-1}$; $\hbar=(6.62607015\times10^{-34}/2\pi)\,\mathrm{J\,s}$.',fontsize=12)
    states=[]
    for n,color in enumerate([TEAL,BLUE,OCHRE,RED]):
        coef=[0]*n+[1]
        psi=(beta/np.pi)**.25/np.sqrt(2**n*math.factorial(n))*hermval(np.sqrt(beta)*q,coef)*np.exp(-beta*q*q/2)
        axs[0].plot(q/1e-12,psi,color=color,lw=2,label=r'$n='+str(n)+'$')
        energy=hbar*Omega*(n+.5)
        axs[1].axhline(energy,color=color,lw=2,label=r'$E_'+str(n)+'$')
        states.append({'n':n,'psi_m_to_minus_half':psi.tolist(),'energy_J':energy})
    axs[0].set_xlabel(r'$q$ (pm; $1\,\mathrm{pm}=10^{-12}\,\mathrm{m}$)')
    axs[0].set_ylabel(r'$\psi_n(q)$ ($\mathrm{m}^{-1/2}$)')
    axs[1].plot(q/1e-12,M*Omega**2*q*q/2,color=INK,ls='--',lw=1.6,label=r'$M\Omega^2q^2/2$')
    axs[1].set_xlabel(r'$q$ (pm)');axs[1].set_ylabel('Energy (J)')
    axs[1].set_ylim(0,4.6*hbar*Omega)
    for ax in axs:ax.grid(alpha=.2);ax.legend(frameon=False,fontsize=10)
    fig.text(.07,.16,r'$\psi_n(q)=(\beta/\pi)^{1/4}H_n(\sqrt{\beta}q)e^{-\beta q^2/2}/\sqrt{2^n n!}$,  $\beta=M\Omega/\hbar$.',fontsize=13)
    fig.text(.07,.10,r'$E_n=\hbar\Omega(n+1/2)$. The zero-point energy is retained; the energy spacing is $\hbar\Omega$.',fontsize=12)
    fig.text(.07,.045,'Numerical plots of the full formulas. Proof: QF.4–QF.11; variances: Solution 1.',fontsize=11)
    save(fig,'f11-oscillator')
    fig=plt.figure(figsize=(11.4,8.2));ax=fig.add_axes((.095,.57,.83,.25))
    fig.suptitle('Real field coordinates and independent particle modes',fontsize=18,y=.97,weight='bold')
    fig.text(.07,.90,r'$L_1=3\,\mathrm{m}$, $L_2=2\,\mathrm{m}$, $L_3=5\,\mathrm{m}$; $V=30\,\mathrm{m}^3$; $n=(1,0,0)$.',fontsize=13)
    x=np.linspace(0,3,601);V=30
    ax.plot(x,np.sqrt(2/V)*np.cos(2*np.pi*x/3),color=TEAL,lw=2,label=r'$u_{n,c}=\sqrt{2/V}\cos(2\pi x_1/L_1)$')
    ax.plot(x,np.sqrt(2/V)*np.sin(2*np.pi*x/3),color=BLUE,lw=2,label=r'$u_{n,s}=\sqrt{2/V}\sin(2\pi x_1/L_1)$')
    ax.axhline(1/np.sqrt(V),color=OCHRE,ls='--',label=r'$u_0=1/\sqrt{V}$')
    ax.set_xlabel(r'$x_1$ (m)');ax.set_ylabel(r'Basis amplitude ($\mathrm{m}^{-3/2}$)')
    ax.set_xlim(0,3);ax.grid(alpha=.2);ax.legend(frameon=False,fontsize=10,loc='lower left',ncol=1)
    fig.text(.07,.455,'Position and momentum Fourier coefficients',fontsize=14,weight='bold')
    fig.text(.08,.397,r'$\phi_{\pm n}=(q_c\mp i q_s)/\sqrt{2V}$,    $\Pi_{\pm n}=(p_c\mp i p_s)/\sqrt{2V}$',fontsize=16)
    fig.text(.08,.34,r'$\phi_n^*=\phi_{-n}$;   $[\phi_n,\Pi_{-n}]=i\hbar/V$;   $[\phi_n,\Pi_n]=0$.',fontsize=14)
    fig.text(.07,.255,'Annihilation operators: a different, unitary map',fontsize=14,weight='bold')
    fig.text(.08,.20,r'$a_n=(b_c-i b_s)/\sqrt{2}$,    $a_{-n}=(b_c+i b_s)/\sqrt{2}$',fontsize=16)
    fig.text(.08,.145,r'$[a_n,a_{-n}^*]=0$;   $[a_n,a_n^*]=[a_{-n},a_{-n}^*]=I$;   $a_{-n}\ne a_n^*$.',fontsize=14)
    fig.text(.07,.055,'Exact mode maps: QF.13 and QF.18–QF.21. Projection kernel with every volume factor: Solution 2.',fontsize=11)
    save(fig,'f11-real-complex-modes')
    fig=plt.figure(figsize=(11.4,8.6));ax=fig.add_axes((0,0,1,1));ax.axis('off')
    ax.text(.04,.95,'Which spectral set belongs to which Hamiltonian?',fontsize=19,weight='bold')
    ax.text(.04,.897,'Exact sets; each row has its own explicitly labelled energy axis.',fontsize=13)
    left=.35;right=.91
    rows=[(.77,'Oscillator','absolute energy',r'$E/(\hbar\Omega)$'),
          (.58,'Massive continuum','relative energy; m > 0',r'$E/(mc^2)$'),
          (.39,'Massless continuum','relative energy',r'$E/E_\star$'),
          (.20,'Massless periodic field','relative energy; zero retained',r'$E/E_\star$')]
    for y,title,sub,xlabel in rows:
        ax.text(.04,y+.025,title,fontsize=13,weight='bold');ax.text(.04,y-.02,sub,fontsize=10)
        ax.annotate('',xy=(right+.035,y),xytext=(left-.015,y),arrowprops={'arrowstyle':'->','color':INK,'lw':1})
        ax.text(right+.035,y-.055,xlabel,ha='right',fontsize=12)
    y=.77
    for n in range(4):
        xx=left+(n+.5)/4*(right-left);ax.plot(xx,y,'o',color=BLUE,ms=7);ax.text(xx,y-.045,str(n)+r'$+\frac{1}{2}$',ha='center',fontsize=10)
    ax.text(left,y+.055,r'$\{\hbar\Omega(n+1/2):n\in\mathbb{N}_0\}$; every point is an eigenvalue.',fontsize=12)
    ax.text(right+.04,y+.006,'…',fontsize=17)
    y=.58;threshold=left+(right-left)/4
    ax.plot(left,y,'o',color=TEAL,ms=8);ax.plot([threshold,right],[y,y],color=BLUE,lw=6,solid_capstyle='butt')
    ax.annotate('',xy=(right+.025,y),xytext=(right-.03,y),arrowprops={'arrowstyle':'->','color':BLUE,'lw':4})
    ax.plot(threshold,y,'o',mfc='#fffef9',mec=BLUE,ms=8,mew=2)
    ax.text(left,y-.045,'0',ha='center');ax.text(threshold,y-.045,'1',ha='center')
    ax.text(left,y+.055,r'$\{0\}\cup[mc^2,\infty)$; vacuum eigenvector, continuous threshold.',fontsize=12)
    for y,vac in [(.39,True),(.20,False)]:
        ax.plot([left,right],[y,y],color=BLUE,lw=6,solid_capstyle='butt')
        ax.annotate('',xy=(right+.025,y),xytext=(right-.03,y),arrowprops={'arrowstyle':'->','color':BLUE,'lw':4})
        ax.plot(left,y,'o',mfc=TEAL if vac else '#fffef9',mec=TEAL if vac else BLUE,ms=8,mew=2)
        ax.text(left,y-.045,'0',ha='center')
        ax.text(left,y+.055,r'$[0,\infty)$; '+('a vacuum vector exists at the nonisolated endpoint.' if vac else 'no normalizable ground vector.'),fontsize=12)
    ax.text(.04,.087,r'$E_\star>0$ is any retained display energy; it does not alter either massless Hamiltonian.',fontsize=12)
    ax.text(.04,.044,'Endpoint circles mark eigenvector status, not set inclusion: every displayed endpoint belongs to the spectrum.',fontsize=10.5)
    ax.set_xlim(0,1);ax.set_ylim(0,1)
    save(fig,'f11-spectral-sets')
    (OUT/'f11-figure-data.json').write_text(json.dumps({'proof_locators':['QF.4–QF.11','QF.13','QF.18–QF.21','QF.26','QF.34','QF.36'],
      'oscillator':{'M_kg':M,'Omega_per_second':Omega,'hbar_J_second':hbar,'q_m':q.tolist(),'states':states},
      'mode_example':{'L_m':[3,2,5],'V_m3':30,'n':[1,0,0],'x1_m':x.tolist()},
      'spectral_display':'Each row explicitly retains its own energy scale. E_star>0 arbitrary; endpoint markers classify eigenvectors, not spectral membership.'},separators=(',',':'))+'\n',encoding='utf8')
if __name__=='__main__':build()
