"""Outward rational first-stage comparisons and Figure 10.19 (CC0)."""
from fractions import Fraction
from math import factorial
from pathlib import Path
import json


def compute():
    from initial_scalar_budget import I, B, biglog, log, scalar_data, fineoptimum, ceildiv
    base=scalar_data()
    vals=base['values'];k,L=base['integers']['degree_factors'];Da=k*L
    c1,c2,c3,c4=[I(Fraction(v)) for v in ['1.4494','1.75','1.3852','20.8']]
    theta=I(Fraction(3,2))/(1+I(Fraction(1,4*10**26)))
    Z=base['Z'];eta=Fraction(1231,1500)
    W=log(6)/(log(2)*log(3))
    h=vals['g0']
    # Positive exponential series, with a geometric upper bound on the tail.
    term=I(1);total=I(1)
    for j in range(1,513):
        term=term*h/j;total=total+term
    next_term=term*h/513
    assert (h/514).hi<B
    exp_h=I(bounds=(total.lo,total.hi+(next_term/(1-h/514)).hi))
    Omega_bound=vals['D']/(c1*c2*3)*W*exp_h
    Omega=ceildiv(Omega_bound.hi,B)
    beta_bound=(h+biglog(W)-biglog(1/log(2)))/log(3)
    beta=beta_bound.floor();assert beta==46
    # Uniform10.235; its coefficient budget uses the whole allowed Rmax family.
    g91=1+(1+biglog(W))/h
    g2=vals['S']
    hc=base['g8']/2+I(Fraction(20,37))*(base['g8']/2+(1+1/vals['g5'])/(c1*c4)
             +g91/(c1*c3*theta)+(1+1/(2*g2))/(2*c1*c2))
    logC=hc+base['g8']/2
    vp_fact=0;power=3
    while power<=k:
        vp_fact+=k//power;power*=3
    vp_lcm=3
    G0=Da*theta+L*vp_fact
    assert (8*Z/log(3)-beta-theta-I(Fraction(1,2))).lo>0
    Rs=[(2**j*vals['S']).floor() for j in range(4)]
    Ts=[(I(eta)**j*vals['T']).floor() for j in range(4)]
    output=[]
    for j in range(3):
        n=2*Rs[j]+1;mu=Ts[j]-Ts[j+1]+1
        sep=0;power=3
        while power<=2*Rs[j]:sep+=1;power*=3
        M0=max(sep,vp_lcm,beta)
        required=(n*mu*theta+mu*M0)/Z
        available=8/log(3)+G0/Z
        gain=((n*mu-Da)*theta-L*vp_fact)/Z
        R=Rs[j+1]+2*k-1
        clearing=3**k
        u=fineoptimum(Omega,clearing,Ts[j+1],Da,R)
        H=Ts[j+1]-u
        def xlogx(x):
            return I(0) if x==0 else x*biglog(x)
        entropy=xlogx(Da)-xlogx(u)-xlogx(Da-u)
        euler=I(0) if H==0 else H*(1+biglog(1+I(Omega)/H))
        logscalar=(Da-u)*biglog(R)-L*biglog(factorial(k))+entropy+u*k*log(3)+euler
        scalar=logscalar/Z
        torus=I(Rs[j+1])/(c1*c2*vals['S'])
        arithmetic=(logC+scalar+torus)/log(3)
        slack=gain-arithmetic
        assert available.lo>required.hi
        assert slack.lo>0
        output.append({'stage':j+1,'input_R':Rs[j],'output_R':Rs[j+1],
            'input_T':Ts[j],'output_T':Ts[j+1],'mu':mu,'nodes':n,
            'B':sep,'M0':M0,'peak_additive_order':u,'peak_euler_order':H,
            'intervals':{name:v.outer_decimal(12) for name,v in {
                'input_available':available,'input_required':required,'analytic_gain':gain,
                'scalar_log_over_Z':scalar,'arithmetic_upper':arithmetic,'strict_gap':slack,
                'coefficient_log_part':logC/log(3),'scalar_part':scalar/log(3),
                'torus_part':torus/log(3)}.items()}})
    return {'state':'passed','family':'K=Q,p3,r2,original2,5; all nonzero b1,b2 with vp(b2)<=vp(b1) and Rmax<=W exp(g0)',
            'Omega_integer_upper':Omega,'beta_integer_upper':beta,'coarse_clearing':3**k,
            'vp_k_factorial':vp_fact,'vp_lcm':vp_lcm,'k':k,'L':L,'Da':Da,
            'eta':str(eta),'R':Rs,'T':Ts,'stages':output,
            'uniform_initial_height':hc.outer_decimal(12),
            'scope':'Complete numerical first three integer steps under the original contradiction precision and an initial kernel of the proved uniform height. Does not verify every degree/rank/prime, fractional descent or final multiplicity contradiction.'}


def draw(data,output=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.size':11.5,'mathtext.fontset':'dejavusans'})
    fig,(ax,bx)=plt.subplots(2,1,figsize=(10.5,8.6))
    fig.subplots_adjust(left=.11,right=.96,bottom=.09,top=.93,hspace=.52)
    x=np.arange(3)
    required=[float(s['intervals']['input_required'][1]) for s in data['stages']]
    available=[float(s['intervals']['input_available'][0]) for s in data['stages']]
    ax.bar(x-.18,required,width=.34,color='#b45931',label='Required: upper bound')
    ax.bar(x+.18,available,width=.34,color='#376797',label='Available: lower bound')
    for a,b,c in zip(x,required,available):
        ax.text(a-.18,b+.12,f'{b:.4f}',ha='center',fontsize=10)
        ax.text(a+.18,c+.12,f'{c:.4f}',ha='center',fontsize=10)
    ax.set(ylim=(0,9.3),xticks=x,xticklabels=['Step 1','Step 2','Step 3'],
           ylabel='Input budget divided by Z',title='The input precision suffices for each complete output jet range')
    ax.legend(loc='upper center',ncol=2,fontsize=10);ax.grid(axis='y',alpha=.18)
    total=np.zeros(3)
    for key,color,label in [('coefficient_log_part','#75849b','Coefficient and logN'),
                            ('scalar_part','#dfaa48','Pointwise scalar: proved lcm < 3^50'),
                            ('torus_part','#298787','Original full-width torus cost')]:
        values=np.array([float(s['intervals'][key][1]) for s in data['stages']])
        bx.bar(x,values,bottom=total,width=.56,color=color,label=label);total+=values
    gain=[float(s['intervals']['analytic_gain'][0]) for s in data['stages']]
    bx.scatter(x,gain,s=75,marker='_',linewidths=3,color='#172638',zorder=4,label='Analytic gain: lower bound')
    for a,b,c,s in zip(x,total,gain,data['stages']):
        bx.annotate('',xy=(a,c),xytext=(a,b),arrowprops={'arrowstyle':'-','linewidth':2,'color':'#172638'})
        bx.text(a,c+.12,'gap > '+s['intervals']['strict_gap'][0][:6],fontsize=10,ha='center')
    bx.set(ylim=(0,4.4),xticks=x,xticklabels=['Step 1','Step 2','Step 3'],
           ylabel='Valuation excess divided by Z',title='A nonzero value would lie below the arithmetic stack and above the analytic bound')
    bx.grid(axis='y',alpha=.18)
    bx.legend(loc='upper left',fontsize=9)
    target=Path(output) if output else Path(__file__).with_name('pointwise-precision-budget.png')
    fig.savefig(target,dpi=175,facecolor='white');plt.close(fig)
    return target


if __name__=='__main__':
    data=compute();print(json.dumps(data,indent=2));print(draw(data))
