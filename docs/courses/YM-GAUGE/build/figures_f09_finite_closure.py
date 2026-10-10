from pathlib import Path
import math,json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def build():
    F=Path(__file__).resolve().parents[1]/'figures';F.mkdir(exist_ok=True)
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','svg.hashsalt':'ym-f09-m-closure'})
    fig,ax=plt.subplots(1,3,figsize=(16,4.7),layout='constrained')
    kappa=2/math.sqrt(math.pi);alpha=2+math.pi*kappa;beta=1+2*kappa;K=2*(1+kappa)
    q=3;B=.1;C=.1;N=max(1,q,math.ceil(8*alpha**2*B**2),math.ceil(2*beta*C))
    target=2.;h=target/(2*N);r=np.arange(N+1)*h+target/2
    orders=np.maximum(0,np.arange(N+1)-(N-q))
    L=K**np.arange(N+1)*(2*N)**(orders/2)
    ax[0].plot(r,L,'o-',color='#126d82');ax[0].set_yscale('log')
    for a,b,o in zip(r,L,orders):ax[0].annotate('order '+str(o),(a,b),xytext=(0,9),textcoords='offset points',ha='center')
    ax[0].set(xlabel='Heat time r (m²)',ylabel='Proved multiplier on the initial norm',title='Three successive derivative gains',ylim=(.65,max(L)*2.4))
    ax[0].text(.03,.91,'q = 3; target s = 2 m²\nB* = C₂ = 0.1; N₃ = '+str(N),transform=ax[0].transAxes,va='top',fontsize=10)
    S=4.;heat=np.geomspace(1e-5,S,350)
    for ell,col in zip((1,2,3),('#126d82','#aa4c13','#71589f')):
     a=ell/2-.25;val=np.sqrt((1-(heat/S)**(2*a))/(2*a))
     ax[1].plot(heat,val,color=col,label='ℓ = '+str(ell)+', α = '+str(a))
    ax[1].set(xscale='log',xlabel='Original heat time s (m²)',ylabel='Exact L² norm of the backward kernel',title='Finite backward integration; S = 4 m²')
    ax[1].legend(loc='lower left',fontsize=10)
    aa=1.;dd=.5;cc=2.;ff=3.;RR=2*(aa+dd);tau=((RR-aa)/(4*cc*ff))**2
    time=np.linspace(0,tau,200);bound=aa+2*cc*np.sqrt(time)*ff
    ax[2].plot(time,bound,color='#126d82',label='I + 2c√t Ψ(R)')
    ax[2].axhline(RR,color='#ac3347',ls='--',label='Radius R = 3 m⁻¹ᐟ²')
    ax[2].scatter([tau],[(RR+aa)/2],color='#126d82')
    ax[2].annotate('(R + I)/2 = 2 m⁻¹ᐟ²',(tau,(RR+aa)/2),xytext=(-5,-23),textcoords='offset points',ha='right',fontsize=10)
    ax[2].set(xlabel='Physical elapsed time t (s)',ylabel='Wave-norm upper bound (m⁻¹ᐟ²)',title='Strict improvement at the chosen time',ylim=(0,3.45))
    ax[2].legend(loc='upper left',fontsize=9)
    fig.suptitle('Exact scalar mechanisms in the heat and wave estimates',fontsize=15)
    for ext in ('svg','png'):fig.savefig(F/('f09-finite-closure.'+ext),dpi=160,metadata={'Date':None} if ext=='svg' else {'Software':'YM-GAUGE reproducible figures'})
    meta={'scope':'Illustrative numerical choices of proof coefficients, not sampled Yang–Mills solutions. The original heat and physical-time coordinates are plotted.','left':{'target_s_m2':target,'q':q,'B_star':B,'C_m_star':C,'N':N,'heat_times_m2':r.tolist(),'derivative_orders':orders.tolist(),'multipliers':L.tolist(),'slab_absorption_coefficient':alpha*B/math.sqrt(2*N)+beta*C/(2*N)},'middle':{'S_m2':S,'formula':'sqrt((1-(s/S)^(2 alpha))/(2 alpha)), alpha=ell/2-1/4','ell':[1,2,3]},'right':{'initial_A':aa,'d':dd,'c_m_per_s':cc,'Phi':ff,'R':RR,'tau_seconds':tau,'strict_bound':(RR+aa)/2},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert meta['left']['slab_absorption_coefficient']<=.5
    (F/'f09-finite-closure-data.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8')
    
    plt.close(fig)

if __name__=='__main__':build()
