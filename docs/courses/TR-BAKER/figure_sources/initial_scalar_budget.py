"""Outward fixed-denominator rational intervals for the worked parameter example."""
from fractions import Fraction
from math import factorial

B = 10**60


def ceildiv(a, b):
    return -((-a)//b)


class I:
    def __init__(self, value=0, bounds=None):
        if bounds is not None:
            self.lo, self.hi = bounds
        else:
            v = Fraction(value)
            self.lo = v.numerator*B//v.denominator
            self.hi = ceildiv(v.numerator*B,v.denominator)

    def __add__(self, other):
        other = other if isinstance(other,I) else I(other)
        return I(bounds=(self.lo+other.lo,self.hi+other.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(bounds=(-self.hi,-self.lo))

    def __sub__(self, other):
        return self+-I(other) if not isinstance(other,I) else self+-other

    def __rsub__(self, other):
        return I(other)+-self

    def __mul__(self, other):
        other = other if isinstance(other,I) else I(other)
        products=[a*b for a in [self.lo,self.hi] for b in [other.lo,other.hi]]
        return I(bounds=(min(products)//B,ceildiv(max(products),B)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other,I) else I(other)
        assert other.lo>0
        values=[Fraction(a*B,b) for a in [self.lo,self.hi] for b in [other.lo,other.hi]]
        lower,upper=min(values),max(values)
        return I(bounds=(lower.numerator//lower.denominator,ceildiv(upper.numerator,upper.denominator)))

    def __rtruediv__(self, other):
        return I(other)/self

    def __pow__(self, power):
        assert isinstance(power,int) and power>=0
        result=I(1)
        while power:
            if power%2:
                result=result*self
            self=self*self
            power//=2
        return result

    def floor(self):
        assert self.lo//B==self.hi//B
        return self.lo//B

    def outer_decimal(self, places=6):
        scale=10**places
        lo=self.lo*scale//B
        hi=ceildiv(self.hi*scale,B)
        def fmt(value):
            sign='-' if value<0 else ''
            value=abs(value)
            return f'{sign}{value//scale}.{value%scale:0{places}d}'
        return [fmt(lo),fmt(hi)]


def log(value):
    x=value if isinstance(value,I) else I(value)
    assert x.lo>=B
    z=(x-1)/(x+1)
    z2=z*z
    power=z
    total=I(0)
    for j in range(512):
        total=total+power/(2*j+1)
        power=power*z2
    # At iteration512 power encloses z^1025. All series terms are nonnegative.
    tail=2*power/(1025*(1-z2))
    return I(bounds=(2*total.lo,2*total.hi+tail.hi))


def compute():
    c0,c1,c2,c3,c4=[I(Fraction(v)) for v in ['1.9','1.4494','1.75','1.3852','20.8']]
    r,p,q,u,rho,P=2,3,2,1,17,3
    t=log(p)
    a0=2+log(14);a1=I(Fraction('4.79'))
    h=3*(2*a0+a1+log(2*a0+a1))
    A=4+log(3)
    theta=I(Fraction(3,2))/(1+I(Fraction(1,4*10**26)))
    g2=c3*q*3*h/t
    g3=I(Fraction(2,rho))*c0*c1*c4*7**2*2**2*3**2/factorial(2)**2*A*t
    g4=q*3*g3/(c1*I(Fraction(3,2))*t)
    g5=c3*q*3*g3/(c1*c4*A*t)
    eps1=(1+I(3)/(2*g4))**2
    S=c3*q*3*h/t
    first=I(3)/t**2
    # exp(2) is bounded by its positive Taylor series and a geometric tail.
    expsum=sum(Fraction(2**j,factorial(j)) for j in range(65))
    exptail=Fraction(2**65,factorial(65))/(1-Fraction(2,66))
    exp2=I(bounds=(I(expsum).lo,I(expsum+exptail).hi))
    second=exp2/4*t
    assert first.lo>second.hi
    D=I(Fraction(1,2))*eps1*(2+1/g2)*c0*c1*c4*(c2*q*P*2*3/theta)**2/factorial(2)*first*log(2)*log(5)*A
    T=q*3*D/(c1*theta*t)
    k=h.floor()
    D0=S*D/(c1*c4*k*A)
    L=D0.floor()+1
    D1=D/(c1*c2*2*P*log(2))
    D2=D/(c1*c2*2*P*log(5))
    volume=D1*D2
    values=dict(g0=h,S=S,D=D,T=T,D0_tilde=D0,D1=D1,D2=D2,volume=volume,g3=g3,g4=g4,g5=g5)
    integers=dict(node_floor=S.floor(),jet_floor=T.floor(),degree_factors=[k,L],
                  box_volume_floor=volume.floor(),grid_sides=[D1.floor()+1,D2.floor()+1])
    return values,integers



def explowerupper(n):
    total=sum(Fraction(n**j,factorial(j)) for j in range(65))
    tail=Fraction(n**65,factorial(65))/(1-Fraction(n,66))
    return I(bounds=(I(total).lo,I(total+tail).hi))


def biglog(value):
    value=value if isinstance(value,I) else I(value)
    assert value.lo>=B
    exponent=max(0,(value.lo//B).bit_length()-1)
    return exponent*log(2)+log(value/(1<<exponent))


def optimum(m,v,t,U):
    if v==1:return 0
    return min(U,max(0,t-ceildiv(m,v-1)+1))


def fineoptimum(m,v,t,D,R):
    lo,hi=0,min(t,D)
    while lo<hi:
        mid=(lo+hi)//2
        if v*(D-mid)*(t-mid)>=R*(mid+1)*(m+t-mid):
            lo=mid+1
        else:
            hi=mid
    return lo


def scalar_data():
    from math import lcm,comb
    values,integers=compute()
    k,L=integers['degree_factors'];s,t,mvol=integers['node_floor'],integers['jet_floor'],integers['box_volume_floor']
    Dadd=k*L
    N=Dadd*(mvol+1)
    Mfull=(2*s+1)*comb(t+2,2)
    Mrep=(2*s+1)*(comb(t+2,2)-comb(t-Dadd+1,2))
    Omega=integers['grid_sides'][0]-1
    clearing=lcm(*range(1,k+1))
    coarse=3**k
    U=min(Dadd,t)
    ua,uc=optimum(Omega,clearing,t,U),optimum(Omega,coarse,t,U)
    assert ua==uc==Dadd
    euler=comb(Omega+t-ua,t-ua)
    e1,e2=explowerupper(1),explowerupper(2)
    c0,c1,c2,c3,c4=[I(Fraction(v)) for v in ['1.9','1.4494','1.75','1.3852','20.8']]
    theta_hat=I(Fraction(3,2));tt=log(3);g1=4+log(3)
    g61=2*c0/c1*c4*(2/theta_hat)**2*3**2*e2/(factorial(2)*2**2)*tt*I(Fraction(1,2))*g1*values['g3']
    g6=17*(1+1/values['g5'])*(1+1/g61)*factorial(2)*e2/(c1**3*c4*c2**2*3**2*2*2**4)
    g7=c3*2*3*values['g0']*values['g3']/tt
    # g6*d/exp(g1)<1, hence the positive part in g8 vanishes here.
    assert g6.hi < B and g1.lo > 5*B
    g8=(biglog(g7)+g1)/g7+2/(c3*2*3**2)*biglog(values['g3'])/values['g3']
    Z=values['S']*values['D']
    ratio=I(Fraction(Mrep,N-Mrep))
    additive=Dadd*biglog(2*e1*(I(s)/k+2))/Z
    eulerpart=biglog(euler)/Z
    mean=I(Fraction(s*(s+1),2*s+1))/(c1*c2*values['S'])
    logpart=biglog(N)/(2*Z)
    costs={}
    for label,v,u in [('actual',clearing,ua),('coarse',coarse,uc)]:
        parts={'additive':ratio*additive,'lcm':ratio*u*biglog(v)/Z,
               'euler':ratio*eulerpart,'torus':ratio*mean,
               'log':(1+ratio)*logpart}
        costs[label]=parts|{'total':sum(parts.values(),I(0))}
    R=s+2*k
    umean=Fraction((t+1)*Dadd*(Dadd+1)//2-Dadd*(Dadd+1)*(2*Dadd+1)//6,
                   (Dadd+1)*(t+1)-Dadd*(Dadd+1)//2)
    hmean=(t-umean)/2
    entropy=Dadd*biglog(Dadd)-I(umean)*biglog(I(umean))-I(Dadd-umean)*biglog(I(Dadd-umean))
    amean=(Dadd-I(umean))*biglog(R)-L*biglog(factorial(k))+entropy
    emean=I(hmean)*(1+biglog(1+I(Omega)/I(hmean)))
    for label,v in [('actual',clearing),('coarse',coarse)]:
        uf=fineoptimum(Omega,v,t,Dadd,R)
        assert uf==Dadd
        afine=biglog(comb(Dadd,uf))+(Dadd-uf)*biglog(R)-L*biglog(factorial(k))
        for mode,a,u,ee in [('fine',afine,I(uf),biglog(euler)),('mean',amean,I(umean),emean)]:
            parts={'additive':ratio*a/Z,'lcm':ratio*u*biglog(v)/Z,
                   'euler':ratio*ee/Z,'torus':ratio*mean,'log':(1+ratio)*logpart}
            costs[mode+'_'+label]=parts|{'total':sum(parts.values(),I(0))}
    up=fineoptimum(Omega,1,t,Dadd,R)
    projective_euler=comb(Omega+t-up,t-up)
    ap=biglog(comb(Dadd,up))+(Dadd-up)*biglog(R)
    for mode,a,ee in [('proj_peak',ap,biglog(projective_euler)),('proj_mean',amean+L*biglog(factorial(k)),emean)]:
        parts={'additive':ratio*a/Z,'lcm':I(0),'euler':ratio*ee/Z,
               'torus':ratio*mean,'log':(1+ratio)*logpart}
        costs[mode]=parts|{'total':sum(parts.values(),I(0))}
    assert values['volume'].lo >= g61.hi
    assert N*B <= (g6*values['S']*values['D']**3).lo
    assert Z.lo >= g7.hi
    assert biglog(N).hi <= (g8*Z).lo
    assert additive.hi <= ((1+1/values['g5'])/(c1*c4)).lo
    return dict(values=values,integers=integers,N=N,Mfull=Mfull,Mrep=Mrep,Dadd=Dadd,Omega=Omega,
                clearing=clearing,coarse_clearing=coarse,U=U,actual_optimum=ua,coarse_optimum=uc,
                euler=euler,costs=costs,g61=g61,g6=g6,g7=g7,g8=g8,Z=Z,
                mean_additive_order=umean,mean_euler_order=hmean,R=R,projective_peak_order=up)


if __name__=='__main__':
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from pathlib import Path
    data=scalar_data()
    keys=['additive','lcm','euler','torus','log']
    colors=['#547a9c','#dc8837','#8861a9','#157e83','#aab5c6']
    names=['Additive / factorial term','lcm clearing','Euler allocation','Mean torus','Logarithmic terms']
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,ax=plt.subplots(figsize=(11.5,8))
    fig.patch.set_facecolor('#f6f8fc')
    labels=['Peak: actual lcm','Peak: proved 3^50','Row mean: actual lcm','Row mean: proved 3^50','Alternative rows: peak','Alternative rows: mean']
    for row,label in enumerate(['fine_actual','fine_coarse','mean_actual','mean_coarse','proj_peak','proj_mean']):
        positive=negative=0
        for key,color,name in zip(keys,colors,names):
            value=data['costs'][label][key]
            width=(value.lo+value.hi)/(2*B)
            left=negative if width<0 else positive
            ax.barh(row,width,left=left,color=color,height=.46,label=name if row==0 else None)
            if width<0:negative+=width
            else:positive+=width
        net=positive+negative
        ax.scatter([net],[row],marker='D',s=24,color='#172839',zorder=4)
        ax.text(positive+.006,row,f"net < {data['costs'][label]['total'].outer_decimal(6)[1]}",va='center',fontsize=10)
    ax.set_yticks(range(6),labels);ax.invert_yaxis();ax.set_xlim(-.025,.39)
    ax.axvline(0,color='#546477',lw=.8)
    ax.set_xlabel(r'Proved bound for $h_2(c)/Z$; $Z=S\mathcal{D}$')
    ax.set_title('The initial coefficient height retains every scalar cost',fontsize=14,pad=18)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
    ax.legend(loc='upper left',bbox_to_anchor=(0,-.24),ncol=3,frameon=False,fontsize=10)
    fig.text(.06,.085,
        f"Peak additive order: {data['actual_optimum']:,}; mean additive order: {float(data['mean_additive_order']):,.3f}. Diamonds = signed sums.",
        fontsize=10,color='#24354a')
    fig.text(.06,.04,
        'Rational bases 2,5 at p=3; Lemma10.76 and Corollaries10.79–10.80. Every row retains its equations and field.',
        fontsize=9,color='#52657a')
    fig.subplots_adjust(left=.23,right=.97,top=.86,bottom=.32)
    fig.savefig(Path(__file__).with_name('initial-scalar-budget.png'),dpi=160,facecolor=fig.get_facecolor())
    plt.close(fig)
