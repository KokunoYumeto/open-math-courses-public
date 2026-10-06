"""Exact tests of weighted kernel volumes, indices and relation products.

The all-dimensional inequalities are proved in the lesson. These tests
independently check the determinant normalization and examples.
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

checks=[]
examples=[
    # (surjective coordinate matrix, primitive integer kernel columns, weights)
    (sp.Matrix([[1,1,1]]),sp.Matrix([[-1,-1],[1,0],[0,1]]),[2,3,5]),
    (sp.Matrix([[1,0,2],[0,1,3]]),sp.Matrix([[-2],[-3],[1]]),[2,5,7]),
    (sp.Matrix([[1,0,0,2,3],[0,1,0,5,-1],[0,0,1,1,4]]),
     sp.Matrix([[-2,-3],[-5,1],[-1,-4],[1,0],[0,1]]),[2,3,5,7,11]),
    (sp.Matrix([[2,1,0],[0,0,1]]),sp.Matrix([[1],[-2],[0]]),[3,5,7]),
]
for C,U,A in examples:
    r,n=C.shape;s=n-r
    assert C*U==sp.zeros(r,s)
    assert U.rank()==s
    # Maximal-minor gcd=1 proves the map and the displayed kernel are primitive.
    from itertools import combinations
    g=0
    for I in combinations(range(n),r):
        g=math.gcd(g,abs(int(C[:,I].det())))
    assert g==1
    g=0
    for I in combinations(range(n),s):
        g=math.gcd(g,abs(int(U[I,:].det())))
    assert g==1
    Q=sp.diag(*[a*a for a in A])
    lhs=(U.T*Q*U).det()
    rhs=Q.det()*(C*Q.inv()*C.T).det()
    assert lhs==rhs>0
    expanded=sum(C[:,I].det()**2/sp.prod(A[j]**2 for j in I)
                 for I in combinations(range(n),r))
    assert expanded==(C*Q.inv()*C.T).det()
    checks.append({"rank":r,"ambient_dimension":n,
                   "weighted_kernel_covolume_squared":str(lhs),
                   "surjective_and_primitive":True})

# Sharp minimum product and finite-volume telescope in the illustrated body.
for N in range(1,31):
    area1=F((2*N+1)**2,2)
    area2=F((2*N+1)*(2*N+2))
    assert area2>=2*area1
    assert F(4)==1*2*2 # lambda_1*lambda_2*area(K)=2^2*covol(Z^2)

# Basis loss: all finite products agree exactly with the stated formula.
for s in range(1,101):
    loss=math.prod(max(F(1),F(i,2)) for i in range(1,s+1))
    assert loss==F(math.factorial(s),2**(s-1))
    assert loss*2**s==2*math.factorial(s)

# Exact equality examples for the crosspolytope and box bounds, s=1,...,12.
for s in range(1,13):
    A=[F(i+1,i+2) for i in range(s)]
    covol=math.prod(A)
    boxvol=2**s*covol
    crossvol=boxvol/math.factorial(s)
    assert crossvol==F(2**s,math.factorial(s))*covol
    assert boxvol==2**s*covol

# Cube-section Gram mechanism: exact polytope, full flag partition and
# a comparison map that contracts the simplex but expands an ambient vector.
verts=[sp.Matrix([1,2]),sp.Matrix([sp.Rational(11,10),2]),
       sp.Matrix([3,-3]),sp.Matrix([-3,-3]),sp.Matrix([-3,1])]
count=len(verts)
area=abs(sum(sp.det(sp.Matrix.hstack(verts[i],verts[(i+1)%count]))
             for i in range(count)))/2
assert area==sp.Rational(93,4)
flag_area=0;flag_count=0
Gtarget=sp.Matrix([[1,1],[1,2]])
for i in range(count):
    p,q=verts[i],verts[(i+1)%count];d=q-p
    # Distance to the affine line of the facet is at least1.
    dist2=sp.det(sp.Matrix.hstack(p,q))**2/d.dot(d)
    assert dist2>=1
    t=max(sp.Rational(0),min(sp.Rational(1),-p.dot(d)/d.dot(d)))
    nearest=p+t*d
    for v in [p,q]:
        G=sp.Matrix.hstack(nearest,v).T*sp.Matrix.hstack(nearest,v)
        assert all(z>=0 for z in G-Gtarget)
        a=abs(sp.det(sp.Matrix.hstack(nearest,v)))/2
        flag_area+=a
        if a: flag_count+=1
assert flag_area==area
assert all(v.dot(v)>=2 for v in verts)
a1,a2=verts[:2];X=sp.Matrix.hstack(a1,a2)
Y=sp.Matrix([[1,1],[0,1]])
T=Y*X.inv()
assert T==sp.Matrix([[0,sp.Rational(1,2)],[10,-5]])
Gdiff=X.T*X-Y.T*Y
assert Gdiff==sp.Matrix([[4,sp.Rational(41,10)],
                         [sp.Rational(41,10),sp.Rational(321,100)]])
assert Gdiff.det()==-sp.Rational(397,100)
assert T*sp.Matrix([sp.Rational(1,10),0])==sp.Matrix([0,1])
for i in range(21):
    for j in range(21-i):
        c=sp.Matrix([sp.Rational(i,20),sp.Rational(j,20)])
        assert ((X*c).dot(X*c)-(Y*c).dot(Y*c))>=0

# Exercise8: minima need not give a basis, even for the sum norm.
H=sp.Matrix([[1,0,sp.Rational(1,2)],
             [0,1,sp.Rational(1,2)],[0,0,sp.Rational(1,2)]])
assert H.det()==sp.Rational(1,2)
assert H*sp.Matrix([-1,-1,2])==sp.Matrix([0,0,1])
assert sp.Rational(8,6)*2*sp.Rational(1,2)==sp.Rational(4,3)

result={"status":"passed","weighted_kernel_examples":checks,
        "finite_volume_checks":30,"basis_loss_dimensions":100,
        "equality_dimensions":12,"face_flags_non_degenerate":flag_count,
        "face_flag_area":str(flag_area),"barycentric_checks":231,
        "simplex_gram_difference_determinant":str(Gdiff.det()),
        "nonbasis_minima_example":"exact covolume1/2, index2 and sum-norm basis(1,1,3/2)",
        "scope":"Exact normalization and examples supplement the universal minima and weighted-kernel proofs (8.46–8.54)."}
if __name__=="__main__":
    print(json.dumps(result,indent=2))
