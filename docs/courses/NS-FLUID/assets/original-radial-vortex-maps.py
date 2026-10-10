"""Original vortex figure sources; quadrature is illustration, not proof."""
from pathlib import Path
import math
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
B=4096.;alpha=.5;delta=B**-.5;kappa=1/16
eps=1/(16*math.e*B);cap=1/(8*math.e);slope=1/(4*math.e)
L=math.log(2);d=(L-.5)/2
def th(x):return math.exp(-1/x) if x>0 else 0.
def H(x):
    if x<=0:return 0.
    if x>=1:return 1.
    return th(x)/(th(x)+th(1-x))
def bump(t):return th(t+1)*th(-.5-t)
Q=quad(lambda t:math.exp(2*t)*bump(t),-1,-.5,epsabs=1e-16)[0]
def pre(t):
    c=1-H((t+9*delta/8)/(delta/8))
    return -kappa*math.exp(2*t)*c+B*t*(1-c)
J=kappa*math.exp(-4)/4+quad(lambda t:-math.exp(2*t)*pre(t),-1,0,
    points=[-9*delta/8,-delta],epsabs=1e-12)[0]
def A(t):
    if t<=0:return pre(t)-(1-J)*bump(t)/Q
    h=H((t-eps)/eps);p=(1-h)*B*t+h*cap
    h=H(8*(t-.25));rr=(1-h)*p+h*slope*(.5-t)
    w=H((t-.5-d)/d)
    return (1-w)*rr-w*alpha*math.exp(-alpha*t)
breaks=sorted(set([-1,-.5,-9*delta/8,-delta,0,eps,2*eps,.25,.375,.5,.5+d,L]))
def integral(fn,a,b):
    if b<=a:return 0.
    cuts=[a]+[x for x in breaks if a<x<b]+[b]
    return sum(quad(fn,x,y,epsabs=2e-11,epsrel=2e-10)[0] for x,y in zip(cuts,cuts[1:]))
def profile(t):
    if t<=-1:
        weighted=-kappa*math.exp(4*t)/4
    else:
        weighted=-kappa*math.exp(-4)/4+integral(lambda s:math.exp(2*s)*A(s),-1,t)
    D=math.exp(-2*t)*weighted
    if t>=L:G=math.exp(-alpha*t)
    elif t>=-1:G=math.exp(-alpha*L)-integral(A,t,L)
    else:G=math.exp(-alpha*L)-integral(A,-1,L)+kappa*(math.exp(-2)-math.exp(2*t))/2
    return D,(G-D)/2,G
Xi0=profile(0)[1]
def potential(t):
    if abs(t)<1e-11:return -B
    return A(t)/(profile(t)[1]-Xi0)
def annular_psi(r):
    if r<=1:return -r*r*math.log(2)/4
    if r<=2:return -((r*r-r**-2)/4+r*r*math.log(2/r))/4
    return -15/(16*r*r)
def main():
    plt.rcParams.update({'font.size':11,'axes.titlesize':13,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(1,3,figsize=(17,5.5),layout='constrained')
    rs=np.geomspace(.08,16,650)
    for radius in [1,2,4]:
        ax[0].plot(rs,[radius*annular_psi(r/radius) for r in rs],label=f'R = {radius}')
        ax[1].plot(rs,[radius*annular_psi(r/radius)/r for r in rs],label=f'R = {radius}')
    ax[0].set(title='The unweighted stream function grows',xlabel='Original radius r',ylabel=r'$\psi_R(r)$',xscale='log')
    ax[1].set(title='The weighted receiver stays bounded',xlabel='Original radius r',ylabel=r'$\psi_R(r)/r$',xscale='log')
    ax[1].axhline(-.25,c='black',ls='--',lw=1,label='proved bound −1/4')
    s=np.geomspace(.08,12,800)
    ax[2].plot(s,np.where(s<1,s**2,s**-2),label='stream-function equality input')
    ax[2].plot(s,np.where(s<1,0,s**-2),label='velocity equality input',ls='--')
    ax[2].set(title='Two distinct sharp equality inputs',xlabel='Original input radius s',ylabel=r'$\gamma(s)$',xscale='log')
    for a in ax:a.grid(alpha=.2);a.legend(fontsize=9)
    fig.suptitle('Original radial maps: m = 2, physical angular factor 2π',fontsize=17)
    for ext in ['png','svg']:fig.savefig(OUT/f'original-radial-green-receivers.{ext}',dpi=160)
    plt.close(fig)
    fig,ax=plt.subplots(1,3,figsize=(17,5.8),layout='constrained')
    t=np.unique(np.r_[np.linspace(-1.15,.9,700),np.linspace(-9*delta/8,delta,180),np.linspace(0,2*eps,50)])
    av=np.array([A(x) for x in t])
    ax[0].plot(t,av,c='#036c89');ax[0].axhline(0,c='black',lw=.6)
    ax[0].scatter([0,.5],[0,0],c='black',s=20,zorder=4)
    ax[0].set(title='Complete signed profile A(t)',xlabel='t = log r',ylabel='A(t); symmetric logarithmic scale',yscale='symlog')
    ax[0].set_yscale('symlog',linthresh=.02);ax[0].grid(alpha=.2)
    rr=np.unique(np.r_[np.linspace(.02,2.6,260),np.exp(np.linspace(-2*delta,2*delta,80))])
    gg=np.array([profile(math.log(r))[2] for r in rr])
    ax[1].plot(rr,gg,c='#036c89',label='constructed g(r)')
    outer=np.linspace(2,2.6,50);ax[1].plot(outer,outer**-alpha,'--',c='#b14424',label=r'exact tail $r^{-1/2}$')
    ax[1].set(title='Actual positive radial vorticity',xlabel='Original radius r',ylabel='g(r)');ax[1].legend(fontsize=9);ax[1].grid(alpha=.2)
    tt=np.unique(np.r_[np.linspace(-2*delta,2*delta,500),np.linspace(-eps,2*eps,80),0])
    vv=np.array([potential(x) for x in tt])
    ax[2].plot(tt,vv,c='#65449b',label=r'$A(t)/(\Xi(t)-\Xi(0))$')
    ax[2].axvspan(-delta,0,color='#c9c0dd',alpha=.45)
    ax[2].plot([-delta,0],[-B*math.exp(-2*delta)]*2,'--',c='black',label=r'proved upper bound $-B e^{-2\delta}$')
    ax[2].set(title='The full removable spectral well',xlabel='Original t = log r',ylabel=r'$V_a(t)$')
    ax[2].legend(fontsize=9);ax[2].grid(alpha=.2)
    fig.suptitle('Explicit source-class vortex: B = 4096, ᾱ = 1/2, δ = 1/64',fontsize=17)
    for ext in ['png','svg']:fig.savefig(OUT/f'original-vortex-and-spectral-well.{ext}',dpi=160)
    plt.close(fig)
    print({'figures':2,'J':J,'Q':Q,'weighted_moment':profile(0)[0],'positive_vorticity_sample_min':float(gg.min()),'purpose':'Numerical samples of exact VA12–VA26 formulas; no numerical eigenvalue claim.'})
if __name__=='__main__':main()

