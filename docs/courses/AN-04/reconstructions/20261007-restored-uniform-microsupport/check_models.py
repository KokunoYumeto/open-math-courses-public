"""Finite sign and Fourier-order checks supporting the full written proofs."""
from pathlib import Path
import hashlib,json
import numpy as np
r=Path(__file__).resolve().parent;source=r/'uniform-microsupport-and-dual-sources.md'
rng=np.random.default_rng(5803);groups=[]
def complex_array(shape):return rng.normal(size=shape)+1j*rng.normal(size=shape)
errors=[]
for i in range(24):
    A=complex_array((5,5));L=complex_array((5,5))+5*np.eye(5)
    Lp=np.linalg.inv(L)+.03*complex_array((5,5));E=L@Lp-np.eye(5)
    f=complex_array(5);u=complex_array(5)
    left=np.vdot(A@u,A@f)
    right=np.vdot(L.conj().T@A@u,Lp@A@f)-np.vdot(A.conj().T@E.conj().T@A@u,f)
    errors.append(abs(left-right)/max(1,abs(left)))
assert max(errors)<1e-11
groups.append({'name':'Linear-first dual pairing, actual adjoints and negative parametrix defect in UM17','samples':24,'max_relative_error':max(errors),'passed':True})
n=np.arange(-256,257);weight=np.sqrt(1+n*n);rows=[]
def cutoff(t):
    x=np.abs(t-1);a=np.maximum(x-.1,0);b=np.maximum(.5-x,0)
    fa=np.zeros_like(a);fb=np.zeros_like(b);ia=np.zeros_like(a);ib=np.zeros_like(b)
    np.divide(-1,a,where=a>0,out=ia);np.divide(-1,b,where=b>0,out=ib)
    np.exp(ia,where=a>0,out=fa);np.exp(ib,where=b>0,out=fb)
    return np.divide(fb,fa+fb,out=np.zeros_like(fb),where=fa+fb>0)
for s in [-1,0,.5,1,2.5]:
    for N in [16,64,128]:
        f=complex_array(len(n));u=complex_array(len(n));a=weight**s*cutoff(n/N)
        S=abs(np.vdot(a*u,a*f))
        Yhalf=np.linalg.norm(weight**(s-.5)*f);Xhalf=np.linalg.norm(weight**(s+.5)*u)
        Ys=np.linalg.norm(weight**(s-1)*f);Au=np.linalg.norm(weight*a*u)
        assert S<=Yhalf*Xhalf*(1+1e-12) and S<=Ys*Au*(1+1e-12)
        for epsilon in [.01,.1,1,10]:assert S<=epsilon*Au**2+Ys**2/(4*epsilon)+1e-9*max(1,S)
        rows.append({'s':s,'N':N,'half_order_bound':True,'source_order_s_absorption':True})
groups.append({'name':'UM23 and UM24 weighted Fourier orders and all epsilon constants','samples':rows,'passed':True})
rows=[]
for m in [2,16,256,4096]:
    w=np.sqrt(1+m*m);s=1;f=w**(1-s);u=w**(-s-.5)
    assert abs(w**(s-1)*f-1)<1e-12 and abs(w**(s+.5)*u-1)<1e-12
    pairing=w**(2*s)*f*u;assert abs(pairing/w**.5-1)<1e-12
    rows.append({'m':m,'two_proposed_weighted_norms':1,'pairing':float(pairing),'required_ratio_grows_as':'<m>^(1/2)'})
groups.append({'name':'UM25 exact one-mode obstruction with bare norms bounded at s=1','samples':rows,'passed':True})
record={'schema':'an04-uniform-microsupport-finite-model-checks/v1','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'passed':True,'groups':groups,'general_theorem_certificate':False,'scope':'Finite algebra/order checks supplement the complete written proof; no general symbol-family or boundary-propagation proof is certified numerically.'}
out=r/'model-check.json'
if out.exists():assert json.loads(out.read_text(encoding='utf8'))['source_sha256']==record['source_sha256']
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':len(groups),'full_written_proof_required':True})
