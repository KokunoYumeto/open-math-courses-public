"""Exact basis data and outward rational intervals for Figure 10.18 (CC0)."""
from fractions import Fraction
from math import factorial
from pathlib import Path
import json


def intervals():
    # This accompanying CC0 module proves and implements the rational series
    # explained in Solution 34. It is included in the same source package.
    from initial_scalar_budget import I, log, biglog, explowerupper
    c0,c1,c2,c3,c4=[I(Fraction(v)) for v in ['1.9','1.4494','1.75','1.3852','20.8']]
    r,d,e,f,p,q,u,nu,rho,P,delta,wK=2,2,1,2,3,2,1,1,58,3,2,2
    t=f*log(p)
    a0=2+log(14);a1=I(Fraction('4.79'))
    g0=3*(2*a0+a1+log(2*a0+a1)+log(d))
    h=g0;g1=4+log(6);A=g1;x=log(2)
    theta=I(Fraction(3,2))/(1+I(Fraction(1,4*10**26)))
    g2=c3*q*3*g0/log(p)
    g3=I(Fraction(2,rho))*c0*c1*c4*7**2*2**2*3**2/factorial(2)**2*g1*t
    g4=q*3*g3/(c1*I(Fraction(3,2))*t*g1)
    g5=c3*q*3*g3/(c1*c4*g1*t)
    eps1=(1+I(3)/(2*g4))**2
    gamma=2*h*A/((h+x)*(A+x))
    S=c3*q*3*d*(h+x)/t
    first=I(9)/(delta*t**2)
    second=explowerupper(2)/4*t
    assert second.lo>first.hi
    D=gamma/4*eps1*(2+1/g2)*c0*c1*c4*(c2*q*P*2*3/theta)**2/2*second*d**3*log(5)*log(7)*(A+x)
    Z=S*D/d
    D1=D/(c1*c2*2*P*d*log(5))
    D2=D/(c1*c2*2*P*d*log(7))
    T=q*3*D/(c1*theta*e*t)
    k=(h+x).floor()
    D0=Z/(c1*c4*k*(A+x));L=D0.floor()+1
    g61=2*c0/c1*c4*(I(2)/I(Fraction(3,2)))**2*9*explowerupper(2)/8*t*I(Fraction(1,2))*g1*(g3/g1)
    g6=rho*(1+1/g5)*(1+1/g61)*2*explowerupper(2)/(c1**3*c4*c2**2*P**2*wK*2**4)
    g7=c3*q*3*g0*g3/t
    assert (g6*d/(explowerupper(4)*6)).hi<10**60
    g8=(biglog(g7)+g1)/g7+I(2)/(c3*q*9)*biglog(g3)/g3
    g11=I(Fraction(4*q,rho))*explowerupper(1)*c0*c1*c3*c4*7**2*I(Fraction(27,4))*g0*g1
    g12=g1/(2*g7)+1/g11
    g91=1+(1+3*log(log(6)))/g0
    c01=c0*I(Fraction(9,8))
    whole=g12+g8/2+1/(c01-1)*(g8/2+(1+1/g5)/(c1*c4)+g91/(c1*c3*theta)+(1+1/(2*g2))/(2*c1*c2))
    actual_field=log(5)/(4*Z)
    tower_field=(log(2)+log(5))/(2*Z)
    centered_field=(log(2)/2+log(7))/Z
    assert actual_field.hi<tower_field.lo<centered_field.lo<g12.lo
    assert (2*Z/(2*d*log(5))).lo>=g11.hi
    assert (2*Z/(2*d*log(7))).lo>=g11.hi
    # Select exactly floor(volume)+1 grid points, then a largest phase class.
    m=(2*D1*D2).floor()+1
    width=(2*D1).floor()+1;height=D2.floor()+1
    assert width*height>=m
    rows,rest=divmod(m,width)
    even=rows*((width+1)//2)+(rest+1)//2
    odd=m-even
    support=max(even,odd)
    s0,t0=S.floor(),T.floor()
    from math import comb
    N=k*L*support;Mfull=(2*s0+1)*comb(t0+2,2)
    assert 80*N-171*Mfull>0
    vals=dict(g0=g0,g11=g11,g12=g12,g7=g7,g8=g8,g91=g91,Z=Z,
              exact_discriminant_cost=actual_field,tower_discriminant_bound=tower_field,
              centered_discriminant_bound=centered_field,uniform_initial_height=whole)
    ints=dict(node_floor=s0,jet_floor=t0,k=k,L=L,selected_points_before_phase=m,
              retained_support=support,N=N,Mfull=Mfull,strict_surplus=80*N-171*Mfull,
              phase_counts=[even,odd],grid_sides=[width,height])
    return vals,ints


def draw(output=None):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams.update({'font.size':12,'axes.titlesize':13,'mathtext.fontset':'dejavusans'})
    fig,(ax,bars)=plt.subplots(2,1,figsize=(10.4,8.7),gridspec_kw={'height_ratios':[1.2,1]})
    fig.subplots_adjust(left=.23,right=.96,top=.94,bottom=.09,hspace=.65)
    for b in range(4):
        for a in range(5):
            ax.scatter(a/2,b,s=55,color='#2459a6' if a%2==0 else '#ac551b')
            ax.annotate(f'({a},{b})',(a/2,b),xytext=(0,8),textcoords='offset points',ha='center',fontsize=9)
    ax.set(xlim=(-.3,2.3),ylim=(-.35,3.55),xlabel=r'Original coordinate $\mu_1=\lambda^\prime_1/2$',
           ylabel=r'Original coordinate $\mu_2=\lambda^\prime_2$',
           title=r'$B^\prime=BU=\operatorname{diag}(1/2,1)$: labels are the new integer coordinates')
    ax.set_xticks([0,.5,1,1.5,2]);ax.set_yticks(range(4));ax.grid(alpha=.2)
    ax.text(.5,-.28,r'$U\lambda^\prime=(\lambda^\prime_1-10\lambda^\prime_2,\lambda^\prime_2)$;  '
            r'$\theta^{U\lambda^\prime}=(\sqrt{5})^{\lambda^\prime_1}7^{\lambda^\prime_2}$',
            transform=ax.transAxes,ha='center',fontsize=11)
    vals=[.5*np.log(5),5*np.log(5)+np.log(7),.5*np.log(5),np.log(7)]
    labels=[r'Old $\theta_1=\sqrt{5}$',r'Old $\theta_2=5^5\cdot7$',
            r'Centered $\theta^\prime_1=\sqrt{5}$',r'Centered $\theta^\prime_2=7$']
    bars.barh(range(4),vals,color=['#8295b3','#8295b3','#2459a6','#2459a6'],height=.62)
    bars.set_yticks(range(4),labels);bars.invert_yaxis()
    exact=[r'$\frac{1}{2}\ln5$',r'$5\ln5+\ln7$',r'$\frac{1}{2}\ln5$',r'$\ln7$']
    for i,(v,label) in enumerate(zip(vals,exact)):bars.text(v+.12,i,label,va='center',fontsize=12)
    bars.axvline(np.log(7),color='#9b4a13',ls='--',lw=1.5)
    bars.set(xlim=(0,13),xlabel='Absolute logarithmic height',
             title=r'The same field $E=\mathbb{Q}(\sqrt{5})$, $\Delta_E=5$, with smaller displayed generators')
    bars.grid(axis='x',alpha=.18)
    out=Path(output) if output else Path(__file__).with_name('initial-field-budget.png')
    fig.savefig(out,dpi=175,facecolor='white');plt.close(fig)
    return out


if __name__=='__main__':
    values,integers=intervals()
    print(json.dumps({'intervals':{n:v.outer_decimal(12) for n,v in values.items()},'integers':integers},indent=2))
    print(draw())
