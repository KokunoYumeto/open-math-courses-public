"""Exact finite certificate for the mixed-generator lemma in the draft.

Independent root lists and matrix calculation, using Fraction only.
This checks every based root system of rank at most three, including products.
The draft explains why that finite set covers the lemma in arbitrary rank.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial
from pathlib import Path
import json, hashlib

def negate(v): return tuple(-x for x in v)
def add(v,w): return tuple(x+y for x,y in zip(v,w))
def scale(c,v): return tuple(c*x for x in v)
def dot(v,w,G): return sum(v[i]*G[i][j]*w[j] for i in range(len(v)) for j in range(len(v)))
def signed(positive): return sorted(set(positive)|{negate(v) for v in positive})
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def zero(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def mul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def minus(A,B): return [[x-y for x,y in zip(row,col)] for row,col in zip(A,B)]
def times(c,A): return [[c*x for x in row] for row in A]
def plus(A,B): return [[x+y for x,y in zip(row,col)] for row,col in zip(A,B)]
def comm(A,B): return minus(mul(A,B),mul(B,A))
def norm(A): return max((abs(x) for row in A for x in row),default=F(0))
def exp_nil(A):
    n=len(A); result=eye(n); power=eye(n)
    for k in range(1,n+1):
        power=mul(power,A)
        if not norm(power): return result
        result=plus(result,times(F(1,factorial(k)),power))
    raise AssertionError("operator not nilpotent")

def direct(left,right):
    R,G=left; S,H=right; a=len(G); b=len(H)
    roots=[tuple(r)+(0,)*b for r in R]+[(0,)*a+tuple(s) for s in S]
    gram=[list(row)+[0]*b for row in G]+[[0]*a+list(row) for row in H]
    return sorted(roots),gram

A1=(signed([(1,)]),[[2]])
A2=(signed([(1,0),(0,1),(1,1)]),[[2,-1],[-1,2]])
B2=(signed([(1,0),(0,1),(1,1),(1,2)]),[[2,-1],[-1,1]])
G2=(signed([(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]),[[2,-3],[-3,6]])
A3=(signed([tuple(int(i<=k<=j) for k in range(3)) for i in range(3) for j in range(i,3)]),[[2,-1,0],[-1,2,-1],[0,-1,2]])
def classical(kind):
    e=[tuple(F(int(k>=i),2 if k==2 and kind=='C' else 1) for k in range(3)) for i in range(3)]
    roots=[]
    for v in e: roots += [scale(1 if kind=='B' else 2,v),scale(-1 if kind=='B' else -2,v)]
    for i,j in combinations(range(3),2):
        for s,t in product([-1,1],repeat=2): roots.append(add(scale(s,e[i]),scale(t,e[j])))
    assert all(x.denominator==1 for v in roots for x in v)
    gram=[[2,-1,0],[-1,2,-1],[0,-1,1]] if kind=='B' else [[2,-1,0],[-1,2,-2],[0,-2,4]]
    return sorted(set(tuple(int(x) for x in v) for v in roots)),gram
systems={'A1':A1,'A1+A1':direct(A1,A1),'A2':A2,'B2':B2,'G2':G2,
 'A1+A1+A1':direct(direct(A1,A1),A1),'A2+A1':direct(A2,A1),
 'B2+A1':direct(B2,A1),'G2+A1':direct(G2,A1),
 'A3':A3,'B3':classical('B'),'C3':classical('C')}

results=[]
for name,(roots,G) in systems.items():
    rank=len(G); rootset=set(roots); count=rank+len(roots)
    simple=[tuple(int(i==j) for j in range(rank)) for i in range(rank)]
    ix={root:rank+k for k,root in enumerate(roots)}
    def cartan(a,i): return F(2)*dot(a,simple[i],G)/G[i][i]
    def length(a,i,direction):
        k=0
        while add(a,scale(direction*(k+1),simple[i])) in rootset: k+=1
        return k
    E=[]; D=[]; H=[]
    for i in range(rank):
        e=zero(count); f=zero(count); h=zero(count)
        for j in range(rank):
            c=abs(cartan(simple[i],j)); e[ix[simple[i]]][j]=c; f[ix[negate(simple[i])]][j]=c
        for a in roots:
            col=ix[a]; h[col][col]=cartan(a,i)
            if a==negate(simple[i]): e[i][col]=1
            elif add(a,simple[i]) in rootset: e[ix[add(a,simple[i])]][col]=length(a,i,-1)+1
            if a==simple[i]: f[i][col]=1
            elif add(a,negate(simple[i])) in rootset: f[ix[add(a,negate(simple[i]))]][col]=length(a,i,1)+1
        E.append(e);D.append(f);H.append(h)
    residuals=[]; serre_residuals=[]; reflection_residuals=[]
    for i in range(rank):
        residuals.append(norm(minus(comm(E[i],D[i]),H[i])))
        for j in range(rank):
            residuals += [norm(comm(H[i],H[j])),norm(minus(comm(H[i],E[j]),times(cartan(simple[j],i),E[j]))),norm(plus(comm(H[i],D[j]),times(cartan(simple[j],i),D[j])))]
            if i!=j:
                residuals.append(norm(comm(E[i],D[j])))
                n=1-int(cartan(simple[j],i)); X=E[j];Y=D[j]
                for _ in range(n): X=comm(E[i],X);Y=comm(D[i],Y)
                serre_residuals += [norm(X),norm(Y)]
        N=mul(mul(exp_nil(E[i]),exp_nil(times(-1,D[i]))),exp_nil(E[i]))
        expected=zero(count)
        for j in range(rank):
            expected[j][j]=1;expected[i][j]-=abs(cartan(simple[i],j))
        for a in roots:
            reflected=add(a,scale(-cartan(a,i),simple[i]))
            sign=1 if a in [simple[i],negate(simple[i])] else (-1)**length(a,i,-1)
            expected[ix[reflected]][ix[a]]=sign
        reflection_residuals.append(norm(minus(N,expected)))
    coroot_coordinates=[tuple(F(a[i]*G[i][i],dot(a,a,G)) for i in range(rank)) for a in roots]
    assert all(c.denominator==1 for v in coroot_coordinates for c in v)
    assert not max(residuals+serre_residuals+reflection_residuals,default=0),name
    results.append({'type':name,'rank':rank,'roots':len(roots),'module_dimension':count,
        'mixed_commutator_basis_cases':rank*(rank-1)*count,'max_generator_residual':str(max(residuals,default=0)),
        'max_Serre_residual':str(max(serre_residuals,default=0)),'max_reflection_residual':str(max(reflection_residuals,default=0)),
        'all_coroot_coordinates_integral':True})

out={'arithmetic':'exact fractions; no floating point','systems':results,
     'mixed_commutator_basis_cases':sum(x['mixed_commutator_basis_cases'] for x in results),
     'all_checks_pass':True,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps(out,indent=2))
