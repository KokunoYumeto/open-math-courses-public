"""Finite checks of signs, matrix algebra and exercise constants, not a theorem certificate."""
from pathlib import Path
from fractions import Fraction
import datetime,hashlib,json,math
r=Path(__file__).resolve().parent;p=r
groups=[]
for a in [Fraction(1,3),Fraction(7,2)]:
    for t in [Fraction(-3,2),Fraction(0),Fraction(1,4),Fraction(2)]:
        assert a*(1+t)**2-a*t-a*t-a*t*t==a
groups.append({'name':'QR8 exact three negative scalar tails','cases':8,'passed':True})
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(a,b,scale=1):return [[a[i][j]+scale*b[i][j] for j in range(2)] for i in range(2)]
def adj(a):return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]
ident=[[1+0j,0j],[0j,1+0j]];f=[[1+0j,1j],[2+0j,1+0j]]
ff=mul(adj(f),f);z=[[q/100 for q in row] for row in ff]
assert max(sum(abs(q) for q in row) for row in z)<.25
power=ident;c=[[0j,0j],[0j,0j]];co=Fraction(1)
for j in range(45):
    if j:co=co*(Fraction(1,2)-j+1)/j;power=mul(power,z)
    c=add(c,power,10*float(co)*(-1)**j)
error=max(abs(q) for row in add(add(mul(adj(c),c),ff),ident,-100) for q in row)
assert error<2e-13
groups.append({'name':'QR9–QR11 nonnormal matrix square-root algebra','matrix_is_nonnormal':mul(adj(f),f)!=mul(f,adj(f)),'maximum_absolute_error':error,'passed':True})
checks=0
for L in [1,3,7]:
    for rr in [1.,1e-2,1e-6,1e-12]:
        for x in [1.,2.,10.,1000.,1e6,1e10]:
            a=rr*x*x;m=(1+a)**(-L/2)
            assert abs(m-1)/x<=max(1,L/2)*math.sqrt(rr)*(1+1e-10)
            checks+=1
groups.append({'name':'QR18 sampled order-one difference bound','cases':checks,'passed':True,'all_derivative_proof_in_lesson':True})
assert Fraction(7,3)-3==Fraction(-2,3)
for rr in [1e-1,1e-5]:
    assert abs((1+rr*(1+10**16))**(-1.5)-1)>.9999
groups.append({'name':'exercise 2 individual order and operator-norm obstruction','passed':True})
for L in [1,2,4]:
    rr=.01
    for n in [1,2,10,1000]:
        term=(1+n*n)/(n*n)*(1+rr*(1+n*n))**(-L)
        assert term<=2*rr**(-L)*n**(-2*L)
for J in [10,100]:
    partial=sum((1+n*n)/(n*n)*(1+1e-12*(1+n*n))**(-1) for n in range(1,J+1))
    assert partial>.999*J
groups.append({'name':'exercise 3 summable fixed-r H1 tail and divergent limit partial sums','passed':True})
source=p/'quadratic-normal-errors-and-regularization.md'
out={'schema':'an04-quadratic-normal-regularizer-models/v1','checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'groups':groups,'general_theorem_certificate':False}
(p/'model-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'general_theorem_certificate':False})
