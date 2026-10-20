"""Finish the exact two-variable character constant term.

The first-variable trace is factored over Q[t,y]. Each inside pole has a
monic factor in Q(t)[y] and multiplicity at most two. Residues are traced
in the corresponding finite quotient. All arithmetic is rational; there
is no coefficient truncation or floating-point root selection.
"""
from pathlib import Path
import json,time
from flint import fmpq_poly,fmpq_mpoly_ctx
from quartic_hilbert import ctx,residue,weights,serialize,root

class Rat:
    def __init__(self,n=0,d=1):
        n=n if isinstance(n,fmpq_poly) else fmpq_poly([n])
        d=d if isinstance(d,fmpq_poly) else fmpq_poly([d])
        assert d
        if not n:self.n,self.d=fmpq_poly([]),fmpq_poly([1]);return
        g=n.gcd(d);n=n//g;d=d//g;c=d.leading_coefficient()
        self.n,self.d=n/c,d/c
    def __bool__(self):return bool(self.n)
    def __add__(self,q):
        q=q if isinstance(q,Rat) else Rat(q)
        return Rat(self.n*q.d+q.n*self.d,self.d*q.d)
    def __neg__(self):return Rat(-self.n,self.d)
    def __sub__(self,q):return self+-q
    def __mul__(self,q):
        q=q if isinstance(q,Rat) else Rat(q)
        return Rat(self.n*q.n,self.d*q.d)
    def __truediv__(self,q):
        q=q if isinstance(q,Rat) else Rat(q)
        assert q.n
        return Rat(self.n*q.d,self.d*q.n)
    def __pow__(self,n):
        return Rat(self.n**n,self.d**n) if n>=0 else Rat(self.d**(-n),self.n**(-n))
    def serial(self):return {'numerator':[str(c) for c in self.n.coeffs()],'denominator':[str(c) for c in self.d.coeffs()]}

zero=Rat(0);one=Rat(1)
def trim(p):
    while p and not p[-1]:p.pop()
    return p
def add(p,q):
    return trim([(p[i] if i<len(p) else zero)+(q[i] if i<len(q) else zero) for i in range(max(len(p),len(q)))])
def neg(p):return [-a for a in p]
def mul(p,q):
    if not p or not q:return []
    out=[zero]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        if not a:continue
        for j,b in enumerate(q):
            if b:out[i+j]=out[i+j]+a*b
    return trim(out)
def divrem(p,q):
    assert q
    p=p.copy();out=[zero]*max(0,len(p)-len(q)+1)
    while len(p)>=len(q):
        j=len(p)-len(q);c=p[-1]/q[-1];out[j]=c
        for i,a in enumerate(q):p[i+j]=p[i+j]-c*a
        trim(p)
    return trim(out),p
def rem(p,q):return divrem(p,q)[1]
def inverse(p,q):
    a,b=q,rem(p,q);u,v=[],[one]
    while b:
        h,r=divrem(a,b);a,b=b,r;u,v=v,add(u,neg(mul(h,v)))
    assert len(a)==1
    return rem([c/a[0] for c in u],q)
def derivative(p):return [c*i for i,c in enumerate(p)][1:]
def trace(p,q):
    answer=zero
    for i in range(len(q)-1):
        r=rem([zero]*i+p,q)
        if i<len(r):answer=answer+r[i]
    return answer
def convert(p):
    coeff={}
    for (t,y),c in p.to_dict().items():
        coeff.setdefault(int(y),{})[int(t)]=c
    if not coeff:return []
    out=[]
    for y in range(max(coeff)+1):
        d=coeff.get(y,{})
        out.append(Rat(fmpq_poly([d.get(t,0) for t in range(max(d,default=-1)+1)])))
    return trim(out)

def inside(p):
    terms=p.to_dict();positive=[(int(t),int(y)) for (t,y),c in terms.items()]
    r=max(y for t,y in positive)
    if r==0:return False
    # Factors here are t^a-y^b or homogeneous cyclotomic polynomials
    # in t^a,y^b. A positive Newton slope means every root tends to0.
    t0=min(t for t,y in positive if y==0)
    tr=min(t for t,y in positive if y==r)
    assert t0!=tr and all(t*r+(t0-tr)*y==t0*r for t,y in positive)
    return t0>tr

def full_first():
    N,D=ctx.constant(0),ctx.constant(1)
    for i,(a,b) in enumerate(weights):
        if a>=0:continue
        n,d=residue(i);g=D.gcd(d)
        N=N*(d//g)+n*(D//g);D=D*(d//g)
        h=N.gcd(D);N=N//h;D=D//h
    return N,D

def calculate():
    start=time.monotonic();N,D=full_first();n,d=convert(N),convert(D)
    assert d and d[0]
    answer=(n[0] if n else zero)/d[0]
    rows=[]
    constant,factors=D.factor()
    for factor,multiplicity in factors:
        if not inside(factor):continue
        q=convert(factor);q=[v/q[-1] for v in q];r=len(q)-1
        assert multiplicity in (1,2)
        qm=ctx.constant(1)
        # Use the monic version in the original bivariate polynomial ring.
        leading=next(c for (t,y),c in factor.to_dict().items() if y==r and t==0)
        monic=factor/leading
        H=D//(monic**multiplicity);h=convert(H)
        yH=[zero]+h
        v=inverse(yH,q);phi=rem(mul(n,v),q)
        prime=derivative(q);invprime=inverse(prime,q)
        if multiplicity==1:
            value=rem(mul(phi,invprime),q)
        else:
            # phi'=N'/(yH)-N(yH)'/(yH)^2 before reduction.
            phi_prime=rem(add(mul(derivative(n),v),neg(mul(mul(mul(n,derivative(yH)),v),v))),q)
            value=rem(add(mul(mul(phi_prime,invprime),invprime),
                          neg(mul(mul(mul(phi,derivative(prime)),invprime),mul(invprime,invprime)))),q)
        traced=trace(value,q);answer=answer+traced
        rows.append({'factor':serialize(monic),'multiplicity':int(multiplicity),'trace':traced.serial()})
        print('Inside factor degree',r,'multiplicity',multiplicity,'trace degrees',traced.n.degree(),traced.d.degree(),flush=True)
    t=fmpq_poly([0,1])
    expectedN=fmpq_poly([0]*76)
    coefficients={0:1,9:1,12:1,15:1,18:2,21:3,24:2,27:3,30:4,33:3,36:4,39:4,42:3,45:4,48:3,51:2,54:3,57:2,60:1,63:1,66:1,75:1}
    for degree,c in coefficients.items():expectedN[degree]=c
    expectedD=fmpq_poly([1])
    for degree in (3,6,9,12,15,18,27):expectedD*=1-t**degree
    assert answer.n*expectedD==answer.d*expectedN
    result={'first_numerator':serialize(N),'first_denominator':serialize(D),
            'inside_residue_traces':rows,'hilbert_series':answer.serial(),
            'expected_numerator_coefficients':coefficients,'expected_denominator_degrees':[3,6,9,12,15,18,27],
            'exact_rational_identity':True,'elapsed_seconds':time.monotonic()-start}
    print('All-degree Hilbert identity verified; elapsed',time.monotonic()-start,flush=True)
    return result

if __name__=='__main__':
    result=calculate()
    (root/'hilbert-series.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
