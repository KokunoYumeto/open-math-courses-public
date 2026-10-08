"""Supplemental finite algebra checks; the written proof supplies the theorem."""
from pathlib import Path
import hashlib,json
import numpy as np

r=Path(__file__).resolve().parent;p=r
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
rng=np.random.default_rng(5903)
def mat():return rng.normal(size=(5,5))+1j*rng.normal(size=(5,5))
def adj(a):return a.conj().T
def pair(u,v):return np.vdot(v,u) # linear first argument
errors=[]
for _ in range(40):
    A=mat();Ds=[mat(),mat()];g=[[mat(),mat()],[mat(),mat()]]
    ell=[mat(),mat()];m=[mat(),mat()];c=mat();u=mat()[:,0];v=A@u
    def q(x,y):
        return sum(pair(g[i][j]@Ds[j]@x,Ds[i]@y) for i in range(2) for j in range(2))+sum(pair(ell[j]@Ds[j]@x,y) for j in range(2))+sum(pair(m[i]@x,Ds[i]@y) for i in range(2))+pair(c@x,y)
    K=lambda h:h@A-A@h
    C=lambda i:Ds[i]@A-A@Ds[i]
    Ct=lambda i:Ds[i]@adj(A)-adj(A)@Ds[i]
    exact=q(v,v)-q(u,adj(A)@v)
    defect=sum(pair(K(g[i][j])@Ds[j]@u,Ds[i]@v)+pair(g[i][j]@C(j)@u,Ds[i]@v)-pair(g[i][j]@Ds[j]@u,Ct(i)@v) for i in range(2) for j in range(2))
    defect+=sum(pair(K(ell[j])@Ds[j]@u,v)+pair(ell[j]@C(j)@u,v) for j in range(2))
    defect+=sum(pair(K(m[i])@u,Ds[i]@v)-pair(m[i]@u,Ct(i)@v) for i in range(2))+pair(K(c)@u,v)
    errors.append(abs(exact-defect)/max(1,abs(exact),abs(defect)))
assert max(errors)<2e-12
balances=[];adjoints=[]
for _ in range(40):
    L=mat()+8*np.eye(5);E=mat()/10;Lp=np.linalg.solve(L,np.eye(5)+E)
    Bs=[mat(),mat()];Ds=[mat(),mat()];C0=mat();H=mat();u=mat()[:,0]
    F=sum(B@D for B,D in zip(Bs,Ds))+C0
    lhs=pair(F@u,H@u)
    rhs=pair(Lp@F@u,adj(L)@H@u)-pair(F@u,adj(E)@H@u)
    balances.append(abs(lhs-rhs)/max(1,abs(lhs),abs(rhs)))
    correction=sum(pair(D@u,adj(B)@adj(E)@H@u) for B,D in zip(Bs,Ds))+pair(u,adj(C0)@adj(E)@H@u)
    adjoints.append(abs(correction-pair(F@u,adj(E)@H@u))/max(1,abs(correction)))
assert max(balances+adjoints)<2e-12
G=np.diag([1.,2.]);swap=np.array([[0.,1.],[1.,0.]]);e1=np.array([1.,0.])
samples=[]
for N in [1,4,16,64,256,1024]:
    w=np.sqrt(1+N*N);A=w*swap
    defect=pair(G@(N*A@e1),N*A@e1)-pair(G@(N*e1),N*adj(A)@A@e1)
    assert abs(defect-N*N*w*w)<1e-6*max(1,abs(defect))
    ratio=abs(defect)/(w+w**1.5)**2
    samples.append({'N':N,'defect':float(defect),'ratio':float(ratio)})
assert all(b['ratio']>a['ratio'] for a,b in zip(samples,samples[1:]))
record={'schema':'an04-sharp-form-models/v1','source_sha256':sha(p/'sharp-boundary-form-defect.md'),'script_sha256':sha(Path(__file__)), 'passed':True,'general_theorem_certificate':False,
 'groups':[{'name':'Complete complex full-form defect algebra, all principal and lower terms','cases':40,'maximum_relative_error':max(errors)},
 {'name':'Negative right-parametrix correction and coefficient-only adjoint moves','cases':40,'maximum_relative_error':max(balances+adjoints)},
 {'name':'Noncommuting principal matrix one-mode obstruction','samples':samples}],
 'scope':'Finite algebra supports signs, multiplication order and the explicit exercise. It certifies no b-calculus, boundary estimate or limiting argument.'}
(p/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':3,'general_theorem_certificate':False})
