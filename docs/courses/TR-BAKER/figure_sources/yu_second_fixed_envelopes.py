"""Exact comparisons for the second-scale fixed-order continuation.

GPT-6 Astra (OpenAI), Ultra. CC0. TR-BAKER-10, results 213--217 give
the arithmetic reductions, the unbounded-rank proof and the actual induction.
This program uses exact fractions for every mathematical comparison.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from yu_second_fractional_profile import case_data

LAM=F(59,58)
XI=F(101,100)
ZETA=F(99,100)

def lower_decimal(x):
    n=(x*10**6).__floor__()
    if F(n,10**6)==x:n-=1
    result=F(n,10**6)
    assert result<x
    return str(result)

def parameters(row,r):
    name,c1,c3,c4,av,q,zeta,amin,dmin,w,nu,chi,*_=row
    c2=F(av,q*q)/zeta;c=F(27,50) if q==2 else F(4,5)
    a=r+1;eta=1-c/a;h=eta**a;Q=q*h
    P0=max(F(1),amin)
    fac=F(r**r*a**r,factorial(r)**2)
    L=F(2)*F(27,10)*c4*q*a/58*(c2*q)**r*fac*P0**(r-1)*max(F(1),5*(amin+F(3,5))/r)
    m=0;v=c*L/a
    assert v>=1
    while v*h>=1:m+=1;v*=h
    mu=F(q**r)/Q**m;j=0
    while mu>q**j:j+=1
    v=(Q-1)/(Q+1)
    logQ=2*sum(v**(2*k+1)/F(2*k+1) for k in range(5))
    ell=F(7,50) if q==2 else F(11,50)
    sm=c3*q*dmin*a*a;br=1500*12**(r-3)
    W=w/(2*c2)*(1+1/(2*sm))+F(1,a*a)/(c2*c3*q)
    W+=(1+w/2)*c1*F(8*r+15,9*a*br)+(1+w)*c1*(F(1,79)+F(1,71928*br))
    return dict(name=name,c1=c1,c2=c2,c3=c3,c4=c4,q=q,c=c,a=a,r=r,
                eta=eta,h=h,Q=Q,amin=amin,dmin=dmin,w=w,nu=nu,chi=chi,
                P0=P0,L=L,m=m,mu=mu,j=j,logQ=logQ,ell=ell,sm=sm,W=W)

def comparisons(d,z,tail=False):
    c1,c2,c3,c4,q,c,a,r=(d[k] for k in ['c1','c2','c3','c4','q','c','a','r'])
    amin,w,nu,chi,L,m,mu,j,ell=(d[k] for k in ['amin','w','nu','chi','L','m','mu','j','ell'])
    ratio=F(1) if z is None else z/(1+z)
    inv=F(0) if z is None else 1/(1+z)
    C=LAM*nu/c4;sigma=q*a/(d['sm']*L)
    mean=F(1) if tail else 1-F(483,824*a)
    def K(extra):
        return d['W']+XI*(LAM*(1+w+F(q,q-1)*ell+(j+extra)*ell)*ratio/c4
               +((F(107,103)+F(3,8*a))*a/(c*L)+w*mean)*inv/c3)
    def pair(torus_factor):
        depth=XI*ratio*3*LAM*(5*ell)/(c4*d['logQ'])
        if tail:return torus_factor*mu/c2+depth
        first=torus_factor*mu/c2+XI*ratio*LAM*(5*ell)/c4*min(F(m,5),3/d['logQ'])
        last=torus_factor*min(F(q**r,32768),mu)/c2+depth
        return max(first,last)
    small=K(0)+pair(1)
    large=K(1)+pair(q)
    # Full-node interpolation retains the Q_D cost at both integer boosts.
    P1=2*c*q*q*d['eta']-2*q*sigma-C-small
    P2=ZETA*chi*c1*q**r-2*sigma-C-large
    P3=ZETA*chi*c1*q-(C+2*sigma)/q**r-small
    # A deleted-node full closure at multiplicity one loses B once.
    Bcost=F(103,100)*XI*c/(c3*(1+amin)*a)
    P4=2*c*q*(q-1)*d['eta']-2*(q-1)*sigma-C-Bcost-small
    I4=c1*chi*q**(r+1)-XI/(c3*(1+amin)*L)-Bcost-small
    reserve=(1-ZETA)*c1*chi*q**(r+1)-XI/(c3*(1+amin)*L)
    radius=1-ZETA*chi*c1/(2*c*q*d['h'])
    return dict(small_integer=P1,large_integer=P2,fractional=P3,
                integer_closure=P4,closure_input=I4,original_coefficient_reserve=reserve,
                radius_factor_below_one=radius)

def calculate():
    rows=[];failures=[];count=0
    for row in case_data():
        name=row[0];q=row[5];r0=3 if q==2 else 4
        minima={};checked=[]
        for r in range(r0,34):
            d=parameters(row,r)
            assert d['j']<=1 and d['Q']>1 and d['m']>=1
            for endpoint,z in [('minimum',d['amin']),('rank',F(r))]:
                values=comparisons(d,z)
                for key,gap in values.items():
                    if gap<=0:failures.append({'case':name,'rank':r,'endpoint':endpoint,'comparison':key,'gap':lower_decimal(gap)})
                    minima[key]=min(minima.get(key,gap),gap)
                checked.append({'rank':r,'endpoint':endpoint,'m':d['m'],'j':d['j'],
                                'strict_gap_lower_bounds':{k:lower_decimal(v) for k,v in values.items()}})
                count+=len(values)
        tail_proofs=[]
        for r in [32,33]:
            d=parameters(row,r);d0=10 if q==2 else 9
            assert d['j']<=1 and d['Q']>1 and d['m']>=1
            growth=(d['c2']*q*d['P0'])**2*F(13,2)**2*F(r,r+2)
            assert growth*d['h']**d0>1 and d['Q']**d0>q*q
            for endpoint,z in [('minimum',d['amin']),('infinity',None)]:
                values=comparisons(d,z,True)
                for key,gap in values.items():
                    if gap<=0:failures.append({'case':name,'rank':f'parity >= {r}','endpoint':endpoint,'comparison':key,'gap':lower_decimal(gap)})
                    minima[key]=min(minima.get(key,gap),gap)
                checked.append({'rank':f'parity >= {r}','endpoint':endpoint,'m':d['m'],'j':d['j'],
                                'strict_gap_lower_bounds':{k:lower_decimal(v) for k,v in values.items()}})
                count+=len(values)
            tail_proofs.append({'first_rank':r,'depth_increment':d0,
                'growth_times_h_power_minus_one':lower_decimal(growth*d['h']**d0-1),
                'Q_power_minus_q_squared':lower_decimal(d['Q']**d0-q*q)})
        rows.append({'case':name,'strict_minimum_gaps':{k:lower_decimal(v) for k,v in minima.items()},
                     'rows':checked,'parity_certificates':tail_proofs})
    d=parameters(case_data()[3],3)
    assert d['L']==F(11202105600000000,262099267823)
    assert d['m']==14 and d['j']==1
    assert F(17,10)<d['c']*d['L']*d['h']**14/4<F(43,25)
    assert F(95,100)<d['c']*d['L']*d['h']**15/4<F(97,100)
    assert F(164,100)<d['mu']<F(165,100)
    u=F(201,2);rs=((u/2-1)/2).__floor__();rl=((u-1)/2).__floor__()
    assert (rs,rl,2*rs+1,2*rl+1)==(24,49,49,99)
    assert 2*rs<=rl and u/2-2<2*rs+1<=u/2 and u-2<2*rl+1<=u
    deleted=[s for s in range(-40,41) if s%2]
    assert len(deleted)==40 and 5**2<=80<5**3
    return {'state':'exact_fixed_order_comparisons_passed' if not failures else 'comparisons_failed',
            'checked_inequalities':count,'failures':failures,'cases':rows,
            'parity_growth_inequalities':28,'exercise86_checked':True,
            'scope':'Rational comparisons for results213--217, including two-rank tail growth. The accompanying written proof derives every envelope and constructs the fixed-order family induction.'}

def render(destination):
    import math
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    d=parameters(case_data()[3],3);B=10
    alpha=-math.log(float(d['h']));lq=math.log(2);lQ=math.log(float(d['Q']))
    m=d['m'];end=3*B/lQ
    vertices=[(m,m),(m,(3*B+alpha*m)/lq),(end,end)]
    fig,axs=plt.subplots(1,2,figsize=(12,6.5),layout='constrained',gridspec_kw={'width_ratios':[1.1,1]})
    a=axs[0];a.add_patch(Polygon(vertices,facecolor='#dbeff1',edgecolor='#176b87',lw=1.5))
    a.plot([0,end],[0,end],color='#85999f',ls='--',lw=.8)
    a.scatter(*zip(vertices[0],vertices[2]),color='#20745d',s=55,zorder=3)
    a.scatter(*vertices[1],color='#82939a',s=40,zorder=3)
    a.annotate(r'$(m_r,m_r)$',vertices[0],xytext=(18,-12),textcoords='offset points',fontsize=11)
    a.annotate('Upper left vertex\nis dominated by C',vertices[1],xytext=(17,27),textcoords='offset points',fontsize=10,arrowprops={'arrowstyle':'->','color':'#82939a'})
    a.annotate(r'$C=(3B/\log Q,3B/\log Q)$',vertices[2],xytext=(-7,18),textcoords='offset points',ha='right',fontsize=10)
    a.set(xlim=(0,end*1.10),ylim=(0,end*1.14),xlabel=r'Starting depth $x=I_1$',ylabel=r'Current depth $z=I$',title='Coupled depth domain: case III.1, r = 3, B = 10')
    a.text(.04,.79,r'$m_r=14,\quad Q=2(173/200)^4$'+'\n'+r'$x\leq z\leq(3B+\alpha x)/\log 2$'+'\n'+r'$\alpha=-\log((173/200)^4)$',transform=a.transAxes,fontsize=10,va='top')
    a.text(.40,.12,'Convex cost: only the green\nvertices need comparison.',transform=a.transAxes,fontsize=10)
    a.grid(alpha=.15)
    b=axs[1];b.axis('off');b.set_title(r'Zero sets: every prepared order stays $\leq O$')
    entries=[('Full integer interval R',r'Depth $I$: hypothesis'),('Small integer interval '+r'$R_{\rm s}$',r'$P_1,P_5>0$'),('Large integer interval '+r'$R_{\rm l}$',r'$P_2>0$'),('Fractional interval '+r'$R/q$',r'$P_3>0$; full field degree'),('q-deleted integer interval R','Phase extraction; depth '+r'$I+1$'),('Full integer interval R',r'$P_4,P_5>0$; depth $I+1$')]
    for i,(label,detail) in enumerate(entries):
        y=.90-i*.158
        b.text(.5,y,label+'\n'+detail,ha='center',va='center',transform=b.transAxes,fontsize=10,bbox={'boxstyle':'round,pad=.4','fc':'#edf5f6','ec':'#176b87'})
        if i<5:b.annotate('',xy=(.5,y-.112),xytext=(.5,y-.046),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.2,'color':'#176b87'})
    fig.savefig(destination,dpi=160);plt.close(fig)

if __name__=='__main__':
    result=calculate();Path(__file__).with_name('second-fixed-envelopes-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
    for row in result['cases']:print(row['case'],row['strict_minimum_gaps'])
    import sys
    if '--figure' in sys.argv:render(Path(__file__).with_name('yu-second-fixed-order.png'))
