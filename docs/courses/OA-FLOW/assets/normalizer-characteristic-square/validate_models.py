"""Reproducible sign, period, link and finite-model checks; not proof substitutes."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import math
import re
import numpy as np

HERE=Path(__file__).resolve().parent
checks={}
# Normalize P to one for these exact rational group-coordinate checks.
def principal(a): return a-a.numerator//a.denominator
def carry(a,b): return a+b-principal(a+b)
grid=[F(n,12) for n in range(12)]
for a in grid:
    for b in grid:
        for c in grid:
            assert carry(a,b)+carry(principal(a+b),c)==carry(b,c)+carry(a,principal(b+c))
checks['integer_cocycle_exact_rational_triples']=len(grid)**3
for q in grid:
    for s in [F(n,7) for n in range(-15,16)]:
        qs=principal(q-s); n=qs-(q-s)
        assert n.denominator==1 and qs-n==q-s
        for t in [F(-2,3),F(5,4)]:
            qst=principal(qs-t); nt=qst-(qs-t)
            assert n+nt==qst-(q-s-t)
checks['flow_cell_sign_and_action_exact']=True
for n in range(2,13):
    for j in range(-10,11):
        # A lift of -P/n is (-1/n+j)P. Its nth power gives gamma_(1-nj).
        assert -n*(F(-1,n)+j)==1-n*j
        assert 1-n*j != 0
checks['torsion_obstruction_exact_n2_through12']=True

P=2.; T=math.pi
def xi(x):
    if abs(x)>=2*T: return 0j
    return (1+.2*x)+1j*(.3-.1*x*x)
def floquet(q,r,f):
    return math.sqrt(T)*np.exp(1j*q*r)*sum(np.exp(1j*k*T*q)*f(r+k*T) for k in range(-8,9))
err=0.
for q in [.07,.31,1.18,1.91]:
    for r in [.1,.7,1.9,3.01]:
        for t in [-1.1*T,-.3*T,.4*T,T]:
            left=floquet(q,r,lambda x:xi(x-t))
            right=np.exp(1j*q*t)*floquet(q,(r-t)%T,xi)
            err=max(err,abs(left-right))
assert err<1e-11
checks['floquet_translation_finite_support_max_abs_error']=err
# Finite Fourier vectors test the exact normalization independently of translations.
cells=np.arange(-3,4); QN=32
vectors=np.array([complex(k*k+1,2-k) for k in cells])
out=np.array([math.sqrt(T)*sum(np.exp(1j*k*T*(P*j/QN))*v for k,v in zip(cells,vectors)) for j in range(QN)])
relative=abs(np.mean(abs(out)**2)-T*sum(abs(vectors)**2))/(T*sum(abs(vectors)**2))
assert relative<1e-13
checks['floquet_parseval_normalization_relative_error']=relative

links=[]
for doc in [HERE.parent.parent/'src/OA-FLOW-NSQ.md',HERE.parent.parent/'src/OA-FLOW-PSQ.md']:
    text=doc.read_text(encoding='utf-8-sig')
    assert text.count(r'\[')==text.count(r'\]')
    assert text.count(r'\(')==text.count(r'\)')
    tags=re.findall(r'\\tag\{([^}]+)\}',text)
    assert len(tags)==len(set(tags)),f'duplicate tag in {doc.name}'
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' in target: continue
        if not any(ext in target for ext in ('.md','.png','.svg','.html')) and not target.startswith('#'): continue
        name,_,anchor=target.partition('#')
        path=(doc.parent/name).resolve() if name else doc
        assert path.exists(),str(path)
        if anchor:
            source=path.read_text(encoding='utf-8-sig')
            if f'id="{anchor}"' not in source and path.name.startswith('OA-FLOW-') and path.suffix=='.md':
                path=HERE.parent.parent/(path.stem+'.html')
                source=path.read_text(encoding='utf-8-sig')
            assert f'id="{anchor}"' in source, (str(path),anchor)
        links.append({'document':doc.name,'target':target})
checks['verified_local_links_and_anchors']=len(links)
checks['balanced_display_inline_math_and_unique_tags']=True
hashes=json.loads((HERE/'HASHES.json').read_text())['files']
for name,digest in hashes.items():
    assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
checks['manifest_files_verified']=len(hashes)
(HERE/'VALIDATION.json').write_text(json.dumps({'checks':checks,'limits':'Finite-model numerical checks supplement the complete written proofs; they do not validate infinite-dimensional theorems by simulation.'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(checks,indent=2))
