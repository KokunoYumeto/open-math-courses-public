"""Twelve classical quartic invariants over a characteristic-zero scalar ring.

The same arithmetic works modulo primes greater than3 when the displayed
denominators are units. The degree27 discriminant is defined separately by
the cubic Koszul determinant. Definitions follow the contractions credited
to Salmon, Dixmier and Ohno; implementation and certificates are independent.
"""
from math import factorial,comb
from itertools import permutations

def indices(n):
    return [(i,j,n-i-j) for i in range(n,-1,-1) for j in range(n-i,-1,-1)]
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items():out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def multiply(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            g=tuple(x+y for x,y in zip(e,f));out[g]=out.get(g,0)+c*d
    return {e:c for e,c in out.items() if c}
def contract(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            if any(x>y for x,y in zip(e,f)):continue
            g=tuple(y-x for x,y in zip(e,f))
            factor=1
            for x,y in zip(e,f):factor*=factorial(y)//factorial(y-x)
            out[g]=out.get(g,0)+c*d*factor
    return {e:c for e,c in out.items() if c}
def divide(p,c):return {e:v/c for e,v in p.items() if v}
def quotient(c,n):return c/n if c else 0
def transfer(f):
    c=[{} for _ in range(5)]
    for (i,j,k),a in f.items():
        for q in range(i+1):
            e=(j+k,q,i-q)
            c[q+j][e]=c[q+j].get(e,0)+a*((-1)**i*comb(i,q))
    e,d,h,b,a=c
    i2=add(scale(multiply(a,e),12),scale(multiply(b,d),-3),multiply(h,h))
    i3=add(scale(multiply(multiply(a,h),e),72),scale(multiply(a,multiply(d,d)),-27),
           scale(multiply(multiply(b,b),e),-27),scale(multiply(multiply(b,h),d),9),
           scale(multiply(multiply(h,h),h),-2))
    assert all(e[0]>=4 for e in i2) and all(e[0]>=6 for e in i3)
    return ({(i-4,j,k):v/12 for (i,j,k),v in i2.items()},
            {(i-6,j,k):v/432 for (i,j,k),v in i3.items()})
def differentiate(p,i):
    return {tuple(e[j]-(i==j) for j in range(3)):c*e[i] for e,c in p.items() if e[i]}
def form_determinant(m):
    out={}
    for p in permutations(range(3)):
        sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        out=add(out,scale(multiply(multiply(m[0][p[0]],m[1][p[1]]),m[2][p[2]]),sign))
    return out
def quadratic(p):
    return [[p.get((2,0,0),0),quotient(p.get((1,1,0),0),2),quotient(p.get((1,0,1),0),2)],
            [quotient(p.get((1,1,0),0),2),p.get((0,2,0),0),quotient(p.get((0,1,1),0),2)],
            [quotient(p.get((1,0,1),0),2),quotient(p.get((0,1,1),0),2),p.get((0,0,2),0)]]
def determinant(m):
    n=len(m);out=0
    for p in permutations(range(n)):
        term=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i,j in enumerate(p):term=term*m[i][j]
        out=out+term
    return out
def adjugate(m):
    return [[(-1)**(i+j)*determinant([[m[r][c] for c in range(3) if c!=i]
                                     for r in range(3) if r!=j])
             for j in range(3)] for i in range(3)]
def pairing(a,b):return sum((a[i][j]*b[j][i] for i in range(3) for j in range(3)),0)

def invariants(f,include_I6=True):
    sigma,psi=transfer(f)
    he=divide(form_determinant([[differentiate(differentiate(f,i),j) for j in range(3)] for i in range(3)]),1728)
    rho=divide(contract(f,psi),144)
    tau=divide(contract(rho,f),12)
    xi=divide(contract(sigma,he),72)
    pi=divide(contract(rho,he),2)
    eta=divide(contract(xi,sigma),12)
    nu=divide(contract(eta,pi),4)
    r,t,c,e,n=(quadratic(p) for p in (rho,tau,xi,eta,nu))
    result={'I3':quotient(contract(f,sigma).get((0,0,0),0),72),
            'I9':pairing(t,r),'J9':pairing(c,r),
            'I12':determinant(r),'J12':pairing(t,e),
            'I15':determinant(t),'J15':determinant(c),
            'I18':pairing(adjugate(t),adjugate(r)),
            'J18':pairing(adjugate(c),adjugate(r)),
            'J21a':determinant(e),'J21b':pairing(n,e)}
    if include_I6:
        normalized={e:v*factorial(e[0])*factorial(e[1])*factorial(e[2])/24 for e,v in f.items()}
        basis=indices(2)
        result['I6']=determinant([[normalized.get(tuple(x+y for x,y in zip(a,b)),0) for b in basis] for a in basis])
    return result

# Fifty candidate secondaries, in the six-generator order below.
secondary_names=('J9','J12','J15','J18','J21a','J21b')
secondary_degrees=(9,12,15,18,21,21)
secondary_powers=[
(0,0,0,0,0,0),(1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0),
(2,0,0,0,0,0),(0,0,0,1,0,0),(1,1,0,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1),
(1,0,1,0,0,0),(0,2,0,0,0,0),(3,0,0,0,0,0),(1,0,0,1,0,0),
(0,1,1,0,0,0),(2,1,0,0,0,0),(1,0,0,0,1,0),(1,0,0,0,0,1),
(0,1,0,1,0,0),(2,0,1,0,0,0),(1,2,0,0,0,0),(0,0,1,1,0,0),
(2,0,0,1,0,0),(1,1,1,0,0,0),(0,0,1,0,1,0),(0,0,1,0,0,1),
(3,1,0,0,0,0),(2,0,0,0,1,0),(2,0,0,0,0,1),(0,0,0,1,0,1),
(1,0,1,1,0,0),(0,2,0,1,0,0),(0,0,0,0,1,1),(2,1,1,0,0,0),
(1,0,1,0,1,0),(1,0,1,0,0,1),(0,1,1,1,0,0),(3,0,0,0,1,0),
(3,0,0,0,0,1),(1,0,0,1,0,1),(2,0,1,1,0,0),(1,0,0,0,1,1),
(2,0,1,0,1,0),(2,0,1,0,0,1),(0,0,1,1,0,1),(2,0,0,1,0,1),
(0,0,1,0,1,1),(2,0,0,0,1,1),(1,0,1,1,0,1),(1,0,1,0,1,1),
(2,0,1,0,1,1)]
assert len(secondary_powers)==50 and len(set(secondary_powers))==50
