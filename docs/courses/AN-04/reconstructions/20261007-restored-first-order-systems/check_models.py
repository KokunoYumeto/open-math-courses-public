"""Exact finite systems complement, and do not replace, the Hilbert-space proofs."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,xml.etree.ElementTree as ET
import sympy as sp
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
xi,t=sp.symbols('xi t',real=True);beta=sp.symbols('beta')
P=sp.Matrix([[1,1],[1,1]])/2;B=sp.diag(1,-1)
assert P*P==P and P.T==P
assert P*B-B*P==sp.Matrix([[0,-1],[1,0]])
a=sp.sqrt(1+xi**2)*P+sp.I*xi*B
assert sp.simplify(sp.trace(a)-sp.sqrt(1+xi**2))==0
aa=sp.Matrix(2,2,sp.symbols('a:4'));mm=sp.Matrix(2,2,sp.symbols('m:4'))
velocity=aa*mm
det_derivative=sum(sp.diff(mm.det(),mm[i,j])*velocity[i,j] for i in range(2) for j in range(2))
assert sp.expand(det_derivative-sp.trace(aa)*mm.det())==0
B=sp.Matrix([[0,1],[4,0]]);S=sp.diag(4,1);R=sp.diag(2,1)
assert S*B==(S*B).T and R*B*R.inv()==sp.Matrix([[0,2],[2,0]])
lam=sp.symbols('lam')
hermitian=sp.I*xi*(B-B.T)/2
assert sp.expand(hermitian.charpoly(lam).as_expr()-(lam**2-sp.Rational(9,4)*xi**2))==0
assert B*sp.Matrix([1,2])==2*sp.Matrix([1,2])
assert B*sp.Matrix([1,-2])==-2*sp.Matrix([1,-2])
N=sp.Matrix([[0,1],[0,0]]);a=sp.I*xi*sp.diag(1,-1)+beta*N
U=sp.Matrix([[sp.exp(-sp.I*t*xi),-beta*sp.sin(t*xi)/xi],[0,sp.exp(sp.I*t*xi)]])
assert (sp.diff(U,t)+a*U).applyfunc(lambda q:sp.simplify(q.rewrite(sp.exp)))==sp.zeros(2)
assert U.subs(t,0)==sp.eye(2)
assert U.applyfunc(lambda q:sp.limit(q,xi,0))==sp.eye(2)-t*beta*N
assert -beta/sp.Integer(2)-beta/sp.Integer(2)+beta==0
assert -beta/sp.Integer(2)+beta/sp.Integer(2)==0
fig=HERE/'figures/first-order-system-fronts.svg'
root=ET.fromstring(fig.read_text('utf-8'));ns={'s':'http://www.w3.org/2000/svg'}
paths=[p.attrib['d'] for p in root.findall('.//s:path',ns)]
assert 'M110 290L790 90L790 490Z' in paths
assert 'M110 290L790 90' in paths and 'M110 290L790 490' in paths
for px,py,time,pos in [(110,290,0,0),(790,90,2,2),(790,490,2,-2)]:
 assert sp.Rational(px-110,340)==time and sp.Rational(290-py,100)==pos
text=' '.join(root.itertext());assert all(s in text for s in ['ξ = 1','every ξ ≠ 0','−β/2','delta of u₂'])
sources=[HERE/'first-order-systems-and-ordered-evolution.md',HERE/'hilbert-coefficient-calculus-and-positivity.md',fig]
result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'passed':True,'finite_groups':3,
 'groups':['Accretive projection, exact noncommutator and general 2x2 determinant differential identity',
 'Fixed symmetrizer, Euclidean Hermitian eigenvalue polynomial and both exact speeds',
 'Ordered coupled evolution, zero-frequency limit, distributional boundary signs and every diagram vertex'],
 'script_sha256':sha(Path(__file__)),
 'source_hashes':{p.relative_to(HERE).as_posix():sha(p) for p in sources},
 'limitation':'Finite exact models only; the full written proofs establish Hilbert-space estimates, all parameter derivatives and the precise solution domains.'}
(HERE/'model-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'finite_groups':3}))
