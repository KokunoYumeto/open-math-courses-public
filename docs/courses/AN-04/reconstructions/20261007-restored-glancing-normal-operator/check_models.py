"""Finite supplementary checks; not an analytic theorem certificate."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import numpy as np
r=Path(__file__).resolve().parent;p=r
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
rng=np.random.default_rng(6003);errors=[]
for _ in range(40):
    F=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    F/=max(1,np.linalg.norm(F,2));alpha=2.
    eig,U=np.linalg.eigh(alpha**2*np.eye(4)-F.conj().T@F)
    assert eig.min()>0
    C=(U*np.sqrt(eig))@U.conj().T
    err=np.linalg.norm(F.conj().T@F+C.conj().T@C-alpha**2*np.eye(4))
    assert err<1e-12;errors.append(float(err))
samples=0
for lam in [0,1,10,100]:
    for eta in [0,.125,.25]:
        h=min(.25,1/(4*max(lam,1)))
        for x in np.linspace(0,h,7):
            for y in np.linspace(-.25,.25,11):
                G=np.array([[1,lam*x],[lam*x,1+x+eta*np.sin(y)]])
                assert np.linalg.eigvalsh(G).min()>=.5-1e-12
                for ratio in np.linspace(.75,1.25,9):
                    d=abs(1-(1+eta*np.sin(y))*ratio**2)
                    assert d<=169/64*.25+1e-12
                    samples+=1
absorbed=Fraction(8,64)+Fraction(4,4096)+Fraction(16,16384)
assert absorbed==Fraction(65,512)<Fraction(1,2)
groups=[{'name':'Actual-adjoint norm factorization algebra with complex matrices','cases':40,'max_absolute_error':max(errors)},
 {'name':'Variable spatial positivity and exact exercise symbol bound','samples':samples,'finite_sampling_only':True},
 {'name':'Exact fixed-ratio absorption arithmetic','leading_sum':str(absorbed),'epsilon_upper_bound':'1/4'}]
record={'schema':'an04-glancing-normal-operator-models/v1','source_sha256':sha(p/'glancing-normal-energy-and-operator-errors.md'),'script_sha256':sha(Path(__file__)),'passed':True,'groups':groups,'general_theorem_certificate':False,'scope':'Finite algebra, exercise samples and exact rational arithmetic; the complete written proof supplies all analytic statements.'}
(p/'model-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
print({'passed':True,'groups':3,'general_theorem_certificate':False})
