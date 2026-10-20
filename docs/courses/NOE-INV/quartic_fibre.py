"""Exact finite-field fibre for the fifty quartic secondary monomials.

First eliminate over F_p(A), retaining a linear B remainder. Then verify
all original equations in a reduced finite algebra; remove every factor
on which a denominator, a Jacobian, or the node discriminant vanishes.
No assertion about unretained roots is needed for the independence test.
"""
from pathlib import Path
import json,time
import sympy as s
from flint import nmod_poly,nmod_mpoly_ctx

P=101
ZERO_INVARIANT='I18'
N1,N2='I12','I15'
E1,E2=4,5
C1,C2=1,1
root=Path(__file__).resolve().parent
outroot=root/'quartic-generator-certificates'
outroot.mkdir(exist_ok=True)
def poly(v):return v if isinstance(v,nmod_poly) else nmod_poly([int(v)%P],P)
def unit(v):return pow(int(v)%P,-1,P)

class Rat:
    def __init__(self,n=0,d=1):
        n,d=poly(n),poly(d);assert d
        if not n:self.n,self.d=poly(0),poly(1);return
        g=n.gcd(d);n=n//g;d=d//g;u=unit(d.leading_coefficient())
        self.n,self.d=n*u,d*u
    def __bool__(self):return bool(self.n)
    def __add__(self,q):
        q=coerce(q)
        g=self.d.gcd(q.d)
        return Rat(self.n*(q.d//g)+q.n*(self.d//g),self.d*(q.d//g))
    __radd__=__add__
    def __neg__(self):return Rat(-self.n,self.d)
    def __sub__(self,q):return self+-coerce(q)
    def __rsub__(self,q):return coerce(q)+-self
    def __mul__(self,q):
        q=coerce(q)
        if not self or not q:return Rat()
        a=self.n.gcd(q.d);b=q.n.gcd(self.d)
        return Rat((self.n//a)*(q.n//b),(self.d//b)*(q.d//a))
    __rmul__=__mul__
    def __truediv__(self,q):
        q=coerce(q);assert q
        return self*Rat(q.d,q.n)
    def __rtruediv__(self,q):return coerce(q)/self
    def __pow__(self,n):
        return Rat(self.n**n,self.d**n) if n>=0 else Rat(self.d**(-n),self.n**(-n))
    def serial(self):return {'numerator':[int(c) for c in self.n.coeffs()], 'denominator':[int(c) for c in self.d.coeffs()]}
def coerce(q):return q if isinstance(q,Rat) else Rat(q)
zero,one=Rat(),Rat(1)
av=Rat(nmod_poly([0,1],P))
def trim(p):
    while p and not p[-1]:p.pop()
    return p
def add(p,q):return trim([(p[i] if i<len(p) else zero)+(q[i] if i<len(q) else zero) for i in range(max(len(p),len(q)))])
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
def det(m):
    m=[row.copy() for row in m];answer=one
    for j in range(len(m)):
        i=next((i for i in range(j,len(m)) if m[i][j]),None)
        if i is None:return zero
        if i!=j:m[i],m[j]=m[j],m[i];answer=-answer
        pivot=m[j][j];answer=answer*pivot
        for i in range(j+1,len(m)):
            if not m[i][j]:continue
            ratio=m[i][j]/pivot
            for k in range(j+1,len(m)):m[i][k]=m[i][k]-ratio*m[j][k]
    return answer

curve=[]
class Cur:
    def __init__(self,v=0):
        self.v=rem(v if isinstance(v,list) else [coerce(v)],curve)
    def __bool__(self):return bool(self.v)
    def __add__(self,q):return Cur(add(self.v,cur(q).v))
    __radd__=__add__
    def __neg__(self):return Cur(neg(self.v))
    def __sub__(self,q):return self+-cur(q)
    def __rsub__(self,q):return cur(q)+-self
    def __mul__(self,q):return Cur(mul(self.v,cur(q).v))
    __rmul__=__mul__
    def __truediv__(self,q):return self*Cur(inverse(cur(q).v,curve))
    def __rtruediv__(self,q):return cur(q)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        a,b=Cur(1),self
        while n:
            if n%2:a=a*b
            b=b*b;n//=2
        return a
def cur(q):return q if isinstance(q,Cur) else Cur(q)

A,B,D,E=s.symbols('A B D E')
local={str(t):t for t in (A,B,D,E)}
data=json.loads((root/'quartic-certificates/case-2.1.json').read_text())
values={n:s.cancel(s.sympify(v,locals=local).subs(E,s.Rational(9,4)/A)) for n,v in data['values'].items()}
p0,p1=(s.fraction(values[n])[0] for n in ('I9',ZERO_INVARIANT))
def symrat(expr,aa,bb,dd):
    n,d=s.fraction(s.cancel(expr))
    def evaluate(p):
        ans=aa*0
        for (i,j,k),c in s.Poly(p,A,B,D).terms():
            coeff=int(c.p)*unit(int(c.q))
            ans=ans+coeff*(aa**i)*(bb**j)*(dd**k)
        return ans
    return evaluate(n)/evaluate(d)
def sym_to_B(expr):
    ans=[]
    for j in range(s.degree(expr,B)+1):
        p=s.Poly(s.expand(expr).coeff(B,j),A)
        ans.append(Rat(nmod_poly([int(p.nth(i))%P for i in range(p.degree()+1)],P)))
    return trim(ans)

def elimination():
    global curve
    start=time.monotonic()
    R=s.Poly(s.resultant(p0,p1,D),A,B).primitive()[1].as_expr()
    R=s.cancel(R/A**2) # A is a unit on the normalized curve.
    curve=sym_to_B(R);curve=[c/curve[-1] for c in curve]
    remainder=s.fraction(s.cancel(s.rem(p1,p0,D)))[0]
    L=s.expand(remainder).coeff(D,1);M=s.expand(remainder).coeff(D,0)
    aa,bb=Cur(av),Cur([zero,one])
    dd=-symrat(M,aa,bb,Cur(0))/symrat(L,aa,bb,Cur(0))
    assert not symrat(p0,aa,bb,dd) and not symrat(p1,aa,bb,dd)
    v1=symrat(values[N1],aa,bb,dd);v2=symrat(values[N2],aa,bb,dd)
    h=C2**E1*v1**E2-C1**E2*v2**E1
    print('Curve degree',len(curve)-1,'H coefficient degrees',[(c.n.degree(),c.d.degree()) for c in h.v],flush=True)
    n=len(curve)-1
    matrix=[]
    for i in range(n):
        col=rem([zero]*i+h.v,curve);matrix.append(col+[zero]*(n-len(col)))
    norm=det([[matrix[j][i] for j in range(n)] for i in range(n)])
    print('Norm degrees',norm.n.degree(),norm.d.degree(),'elapsed',time.monotonic()-start,flush=True)
    a,b=curve,h.v;linear=None;steps=[]
    while b:
        steps.append(len(b)-1)
        if len(b)==2:linear=b.copy()
        _,r=divrem(a,b);a,b=b,r
    assert len(a)==1 and linear is not None
    shape=-linear[0]/linear[1]
    result={'prime':P,'zero_invariant':ZERO_INVARIANT,'normalizing_invariants':[N1,N2],
            'target_values':[C1,C2], 'curve':[c.serial() for c in curve], 'L':str(L),'M':str(M),
            'norm':norm.serial(),'B_shape':shape.serial(),'Euclidean_remainder_degrees':steps,
            'elapsed_seconds':time.monotonic()-start}
    (outroot/'fibre-elimination.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
    print('Saved linear shape, numerator degree',shape.n.degree(),'denominator',shape.d.degree(),flush=True)
    return result

modulus=poly(1)
class Alg:
    def __init__(self,v=0):self.v=poly(v)%modulus
    def __bool__(self):return bool(self.v)
    def __add__(self,q):return Alg(self.v+alg(q).v)
    __radd__=__add__
    def __neg__(self):return Alg(-self.v)
    def __sub__(self,q):return self+-alg(q)
    def __rsub__(self,q):return alg(q)+-self
    def __mul__(self,q):return Alg(self.v*alg(q).v)
    __rmul__=__mul__
    def __truediv__(self,q):
        g,u,_=alg(q).v.xgcd(modulus);assert g.degree()==0
        return Alg(self.v*u*unit(g[0]))
    def __rtruediv__(self,q):return alg(q)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        return Alg(self.v.pow_mod(n,modulus))
    def serial(self):return [int(c) for c in self.v.coeffs()]
def alg(q):return q if isinstance(q,Alg) else Alg(q)
def unrat(row):return Rat(nmod_poly(row['numerator'],P),nmod_poly(row['denominator'],P))
def retain_units(polynomials,reason,log):
    global modulus
    old=modulus.degree()
    for p in polynomials:
        g=modulus.gcd(poly(p));modulus=modulus//g
    modulus*=unit(modulus.leading_coefficient())
    log.append({'condition':reason,'before':old,'after':modulus.degree()})
    print(reason,old,'->',modulus.degree(),flush=True)
def shape_points(shape):
    aa=Alg(nmod_poly([0,1],P));bb=Alg(shape.n)/Alg(shape.d)
    L=s.expand(s.fraction(s.cancel(s.rem(p1,p0,D)))[0]).coeff(D,1)
    M=s.expand(s.fraction(s.cancel(s.rem(p1,p0,D)))[0]).coeff(D,0)
    dd=-symrat(M,aa,bb,Alg(0))/symrat(L,aa,bb,Alg(0))
    return aa,bb,dd
def coefficient_rank(columns,nrows):
    # Eliminate the transpose. Pivot columns identify a square minor of
    # the original coefficient matrix; its determinant is checked separately.
    m=[[int(c[i]) for i in range(nrows)] for c in columns]
    pivots=[];r=0
    for j in range(nrows):
        i=next((i for i in range(r,len(m)) if m[i][j]),None)
        if i is None:continue
        m[r],m[i]=m[i],m[r];u=unit(m[r][j]);m[r]=[(v*u)%P for v in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][j]:
                c=m[i][j];m[i]=[(a-c*b)%P for a,b in zip(m[i],m[r])]
        pivots.append(j);r+=1
        if r==len(m):break
    return r,pivots
def scalar_det(m):
    m=[r.copy() for r in m];value=1
    for j in range(len(m)):
        i=next((i for i in range(j,len(m)) if m[i][j]%P),None)
        if i is None:return 0
        if i!=j:m[i],m[j]=m[j],m[i];value=-value
        c=m[j][j]%P;value=value*c%P;u=unit(c)
        for i in range(j+1,len(m)):
            q=m[i][j]*u%P
            for k in range(j+1,len(m)):m[i][k]=(m[i][k]-q*m[j][k])%P
    return value%P
def certify(elim):
    global modulus
    from quartic_generators import invariants,secondary_powers,secondary_names,secondary_degrees
    start=time.monotonic();log=[]
    norm=unrat(elim['norm']);shape=unrat(elim['B_shape'])
    G=norm.n//norm.n.gcd(norm.n.derivative())
    modulus=G*unit(G.leading_coefficient())
    retain_units([nmod_poly([0,1],P),norm.d,shape.d], 'A and elimination denominators are units',log)
    # Test the linear-D coefficient without division before retaining it.
    aa=Alg(nmod_poly([0,1],P));bb=Alg(shape.n)/Alg(shape.d)
    L=s.sympify(elim['L'],locals=local)
    retain_units([symrat(L,aa,bb,Alg(0)).v], 'linear-D coefficient is a unit',log)
    aa,bb,dd=shape_points(shape)
    q1=symrat(values[N1],aa,bb,dd);q2=symrat(values[N2],aa,bb,dd)
    residuals=[symrat(p0,aa,bb,dd).v,symrat(p1,aa,bb,dd).v,(C2**E1*q1**E2-C1**E2*q2**E1).v]
    old=modulus.degree()
    for r in residuals:modulus=modulus.gcd(r)
    log.append({'condition':'all three original equations hold','before':old,'after':modulus.degree()})
    print('Original-equation common roots',old,'->',modulus.degree(),flush=True)
    aa,bb,dd=shape_points(shape)
    q1=symrat(values[N1],aa,bb,dd);q2=symrat(values[N2],aa,bb,dd)
    retain_units([q1.v,q2.v], 'the two normalizing invariants are units',log)
    aa,bb,dd=shape_points(shape)
    q1=symrat(values[N1],aa,bb,dd);q2=symrat(values[N2],aa,bb,dd)
    rows=[]
    for expr in (p0,p1):rows.append([symrat(s.diff(expr,v),aa,bb,dd) for v in (A,B,D)])
    rows.append([C2**E1*E2*q1**(E2-1)*symrat(s.diff(values[N1],v),aa,bb,dd)-C1**E2*E1*q2**(E1-1)*symrat(s.diff(values[N2],v),aa,bb,dd) for v in (A,B,D)])
    from itertools import permutations
    jac=Alg(0)
    for p in permutations(range(3)):
        term=Alg((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))
        for i,j in enumerate(p):term=term*rows[i][j]
        jac=jac+term
    retain_units([jac.v], 'three-equation Jacobian is a unit',log)
    U=s.symbols('U');h=A*U**6-9*U**5-4*A*D*U**4+20*A*U**3-4*A*B*U**2-4*A**2*U+A
    mc=nmod_mpoly_ctx.get(('U','A','B','D'),P,'lex')
    hp=mc.from_dict({e:int(c)%P for e,c in s.Poly(h,U,A,B,D).terms()})
    disc=hp.resultant(hp.derivative('U'),'U')
    aa,bb,dd=shape_points(shape);node=Alg(0)
    for (u,a,b,d),c in disc.to_dict().items():
        assert not u
        node=node+int(c)*aa**a*bb**b*dd**d
    retain_units([node.v], 'binary sextic is squarefree: unique ordinary node',log)
    aa,bb,dd=shape_points(shape);ee=9/(4*aa)
    f={(1,1,2):Alg(1),(3,0,1):Alg(1),(0,3,1):Alg(1),(0,4,0):aa,
       (1,3,0):bb,(2,2,0):-Alg(9)/2,(3,1,0):dd,(4,0,0):ee}
    inv=invariants(f,include_I6=False)
    assert not inv['I3'] and not inv['I9'] and not inv[ZERO_INVARIANT]
    q1=symrat(values[N1],aa,bb,dd);q2=symrat(values[N2],aa,bb,dd)
    assert not inv[N1]-q1 and not inv[N2]-q2
    assert not C2**E1*q1**E2-C1**E2*q2**E1
    a=C2*q1/(C1*q2)
    columns=[];degrees=[]
    for powers in secondary_powers:
        degree=sum(i*d for i,d in zip(powers,secondary_degrees));value=a**(degree//3)
        for n,e in zip(secondary_names,powers):value=value*inv[n]**e
        columns.append(value.v);degrees.append(degree)
    rank,pivots=coefficient_rank(columns,modulus.degree())
    print('Secondary rank',rank,'in reduced algebra dimension',modulus.degree(),flush=True)
    minor=[[int(c[i]) for c in columns] for i in pivots]
    minor_det=scalar_det(minor) if rank==50 else None
    checks={'A':aa,'linear_D_coefficient':symrat(L,aa,bb,Alg(0)),
            N1:q1,N2:q2,'three_equation_Jacobian':Alg(jac.v),'node_sextic_resultant':Alg(node.v),
            'modulus_derivative':Alg(modulus.derivative())}
    unit_witnesses={name:{'value':v.serial(),'inverse':(1/v).serial()} for name,v in checks.items()}
    assert modulus.gcd(modulus.derivative()).degree()==0
    result={'prime':P,'zero_invariant':ZERO_INVARIANT,'normalizing_invariants':[N1,N2],
            'target_primary_values':[0,0,0,1,1,0,0],
            'modulus':[int(c) for c in modulus.coeffs()], 'dimension':modulus.degree(),
            'B':[int(c) for c in bb.v.coeffs()],'D':[int(c) for c in dd.v.coeffs()],
            'filters':log,'unit_witnesses':unit_witnesses,
            'invariant_values':{n:alg(v).serial() for n,v in inv.items()},
            'normalizing_cube':a.serial(),'secondary_names':secondary_names,
            'secondary_powers':secondary_powers,'secondary_degrees':degrees,
            'secondary_columns':[[int(c) for c in v.coeffs()] for v in columns],
            'rank':rank,'minor_rows':pivots,'minor_determinant':minor_det,
            'elapsed_seconds':time.monotonic()-start}
    (outroot/'fibre-secondary-rank.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
    assert rank==50 and minor_det
    return result

if __name__=='__main__':certify(elimination())
