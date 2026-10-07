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
        return [f'{lo//scale}.{lo%scale:0{places}d}',
                f'{hi//scale}.{hi%scale:0{places}d}']


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



if __name__=='__main__':
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from pathlib import Path
    from math import comb
    values,integers=compute()
    k,L=integers['degree_factors']
    s,t,m=integers['node_floor'],integers['jet_floor'],integers['box_volume_floor']
    N=k*L*(m+1)
    M=(2*s+1)*comb(t+2,2)
    Jrep=comb(t+2,2)-comb(t-k*L+1,2)
    Mrep=(2*s+1)*Jrep
    ratio=Fraction(N,M)
    assert 20*N>57*M
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
    fig,(ax,zoom)=plt.subplots(1,2,figsize=(11.2,5.5),gridspec_kw={'width_ratios':[1.4,1]})
    fig.patch.set_facecolor('#f6f8fc')
    labels=[r'$M_*$',r'$M_{\rm full}$',r'$(57/20)M_{\rm full}$',r'$N$']
    xs=[float(Fraction(Mrep,M)),1,2.85,float(ratio)]
    colors=['#637c9d','#b9c7d8','#e59b32','#177e89']
    ax.barh(range(4),xs,color=colors,height=.58)
    ax.set_yticks(range(4),labels)
    ax.invert_yaxis()
    ax.set_xlim(0,3.35)
    for i,x in enumerate(xs):
        ax.text(x+.035,i,f'{x:.6f}',va='center',fontsize=10)
    ax.set_xlabel(r'Count divided by $M_{\rm full}$')
    ax.set_title('All rounded rows fit beneath the columns',fontsize=12)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
    zoom.hlines([0,1],2.849,float(ratio)+.0004,color=['#e59b32','#177e89'],lw=3)
    zoom.scatter([2.85,float(ratio)],[0,1],s=75,color=['#e59b32','#177e89'],zorder=3)
    zoom.set_yticks([0,1],[r'$57/20$',r'$N/M_{\rm full}$'])
    zoom.set_xlim(2.849,float(ratio)+.0006);zoom.set_ylim(-.4,1.5)
    zoom.set_title('The strict surplus survives both floors',fontsize=12)
    zoom.ticklabel_format(axis='x',style='plain',useOffset=False)
    zoom.spines[['top','right']].set_visible(False)
    zoom.grid(axis='x',alpha=.2)
    fig.text(.06,.115,
        f'Nodes: 2 floor(S) + 1 = {2*s+1:,}     |     jet floor: {t:,}     |     additive degree cap: {k*L:,}',
        fontsize=10,color='#24354a')
    fig.text(.06,.068,
        f'Exact witness: 20 N - 57 M_full = {20*N-57*M:,} > 0',
        fontsize=10,color='#24354a')
    fig.text(.06,.023,
        'Q, p = 3; bases 2 and 5; phase count H = 1. Theorem 10.71 and Solution 34.',
        fontsize=9,color='#52657a')
    fig.subplots_adjust(left=.09,right=.98,top=.89,bottom=.27,wspace=.45)
    target=Path(__file__).with_name('initial-parameter-counts.png')
    fig.savefig(target,dpi=160,facecolor=fig.get_facecolor())
    plt.close(fig)
