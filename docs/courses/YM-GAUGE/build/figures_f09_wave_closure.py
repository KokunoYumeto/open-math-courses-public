"""Reproducible exact coefficient and kernel figures for PW, ST and TB."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parents[1]/'figures'
COL=['#126b75','#ad5d23','#6b4a9b']
def save(fig,name):
    fig.savefig(OUT/(name+'.svg'),metadata={'Date':None})
    fig.savefig(OUT/(name+'.png'),dpi=150,metadata={'Software':'YM-GAUGE reproducible exact figure'})
    plt.close(fig)
def build():
    OUT.mkdir(exist_ok=True)
    plt.rcParams.update({'svg.hashsalt':'YM-F09-PW-ST-TB-20261009',
      'font.family':'DejaVu Sans','font.size':11,'axes.labelsize':12,'axes.titlesize':13})
    fig,axes=plt.subplots(1,2,figsize=(12.8,6.1))
    fig.subplots_adjust(left=.08,right=.96,bottom=.25,top=.8,wspace=.29)
    L=2.;S=2.;s=np.linspace(0,S,601)
    xi=np.array([2.,-1.,2.])/L;v=np.array([1.,2.,-1.])
    cf=xi*np.dot(xi,v)/np.dot(xi,xi);df=v-cf
    decay=np.exp(-np.dot(xi,xi)*s)
    full=cf[:,None]+df[:,None]*decay
    for i in range(3):
        axes[0].plot(s,full[i],lw=2.2,color=COL[i],label=f'Component {i+1}')
    axes[0].set(xlabel='Original heat time s (m²)',ylabel='Fourier coefficient (m²)',
                title='Every original component (PW.22)',xlim=(0,S))
    ncf=np.linalg.norm(cf);ndf=np.linalg.norm(df)*decay
    axes[1].plot(s,np.full_like(s,ncf),color=COL[0],lw=2.2,label='Longitudinal length')
    axes[1].plot(s,ndf,color=COL[1],lw=2.2,label='Transverse length')
    axes[1].plot(s,np.sqrt(ncf**2+ndf**2),color=COL[2],lw=2.2,label='Full coefficient length')
    axes[1].set(xlabel='Original heat time s (m²)',ylabel='Euclidean coefficient length (m²)',
                title='Zero and decaying parts of the symbol',xlim=(0,S))
    for ax in axes:ax.grid(alpha=.2);ax.legend(frameon=False,fontsize=10)
    fig.suptitle('The longitudinal coefficient is retained by the potential heat equation',fontsize=16,y=.96)
    fig.text(.5,.065,
      'ξ = (2, −1, 2)/L, L = 2 m; initial coefficient (1, 2, −1) m². Transverse factor exp(−9s/L²).\n'
      'Exact linear Fourier-symbol comparison, not a monochromatic L² Yang–Mills field.',ha='center',va='bottom',fontsize=10)
    save(fig,'f09-potential-wave')

    fig,axes=plt.subplots(1,3,figsize=(14,5.9))
    fig.subplots_adjust(left=.075,right=.97,bottom=.25,top=.78,wspace=.36)
    S=4.;s=np.geomspace(1e-4,S,1601)
    for ax,q,beta,col,unit in zip(axes,[0,1,2],[.125,.25,.75],COL,['m','m¹/⁴','m¹/⁴']):
        gamma=q/2-3/8
        vals=s**beta*(s**(-gamma)-S**(-gamma))/gamma
        star=S*((beta-gamma)/beta)**(1/gamma)
        peak=S**(beta-gamma)/beta*((beta-gamma)/beta)**((beta-gamma)/gamma)
        ax.semilogx(s,vals,color=col,lw=2.4)
        ax.plot([star],[peak],'o',color='#344957',ms=6)
        ax.annotate('Exact maximum',xy=(star,peak),xytext=(.0015,peak*1.19),
          arrowprops={'arrowstyle':'->','color':'#344957'},fontsize=10)
        ax.set(xlabel='Original heat time s (m²)',ylabel=f'Weighted kernel ({unit})',
          title=f'q = {q}, β = {beta:g}',xlim=(1e-4,S),ylim=(0,1.38*peak))
        ax.grid(alpha=.2)
    fig.suptitle('The finite temporal kernels and their attained weighted maxima (ST.5–ST.7)',fontsize=16,y=.96)
    fig.text(.5,.06,
      'S = 4 m². Every curve retains both terms of (s⁻ᵞ − S⁻ᵞ)/γ, with γ = q/2 − 3/8.\n'
      'The lower plotted heat time is a viewing limit. Distinct units remain on separate panels.',ha='center',va='bottom',fontsize=10)
    save(fig,'f09-spacetime-tension')

    fig,axes=plt.subplots(1,2,figsize=(12.8,6.1))
    fig.subplots_adjust(left=.08,right=.96,bottom=.26,top=.8,wspace=.29)
    L=1.;S=1.;kappa=1.;x=np.linspace(-3.5,3.5,1001)
    phi=np.exp(-x*x/(2*L*L));lap=(x*x/L**4-3/L**2)*phi
    endpoint=-kappa*S*phi
    forcing=kappa*S*phi-.5*kappa*S*S*lap
    actual=-.5*kappa*S*S*lap;wrong=actual+2*kappa*S*phi
    axes[0].plot(x,endpoint,color=COL[0],lw=2,label='Negative endpoint −W(S)')
    axes[0].plot(x,forcing,color=COL[1],lw=2,label='Complete forcing integral')
    axes[0].plot(x,actual,color=COL[2],lw=2.3,label='Their sum = Δaₜ(0)')
    axes[1].plot(x,actual,color=COL[2],lw=2.3,label='Correct identity')
    axes[1].plot(x,wrong,color=COL[1],lw=2,ls='--',label='Positive endpoint sign')
    axes[1].plot(x,2*kappa*S*phi,color=COL[0],lw=2,label='Exact defect 2W(S)')
    for ax in axes:
        ax.set(xlabel='Original spatial coordinate x₁ (m)',ylabel='Coefficient of T (s⁻¹ m⁻²)',
               xlim=(-3.5,3.5))
        ax.grid(alpha=.2);ax.legend(frameon=False,fontsize=10,loc='upper right')
    axes[0].set_title('Keep both original contributions')
    axes[1].set_title('Changing the sign has an exact defect')
    axes[0].set_ylim(-1.2,3.6)
    axes[1].set_ylim(-.25,4.8)
    fig.suptitle('A full three-dimensional Gaussian test of the endpoint identity (TB.17)',fontsize=16,y=.96)
    fig.text(.5,.065,
      'W(s,x) = κs exp(−|x|²/(2L²))T; L = 1 m, S = 1 m², κ = 1 s⁻¹ m⁻⁴; slice x₂ = x₃ = 0.\n'
      'Smooth zero-initial diagnostic history; not asserted to solve the Yang–Mills system.',ha='center',va='bottom',fontsize=10)
    save(fig,'f09-temporal-boundary')
if __name__=='__main__':build()

