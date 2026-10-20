"""An exact seven-by-seven Jacobian witness for the quartic parameters.

The discriminant is the determinant quotient of the cubic Koszul complex.
Matrices, point, derivatives and a nonzero minor are retained as a certificate.
"""
from pathlib import Path
import json,random,time
import sympy as s
from flint import fmpq,fmpq_mat,nmod_mat
from quartic_algebra import indices,parameters,cubic_koszul_matrices

root=Path(__file__).resolve().parent/'quartic-certificates'
quartics=indices(4)
def trace_product(a,b):
    return sum((a[i,j]*b[j][i] for i in range(a.nrows()) for j in range(a.ncols())),fmpq(0))

start=time.monotonic()
rng=random.Random(20261002)
f={e:rng.choice([i for i in range(-9,10) if i]) for e in quartics}
m,n,selected,complement=cubic_koszul_matrices(f)
fm,fn=fmpq_mat(m),fmpq_mat(n)
assert fm.det()!=0 and fn.det()!=0
fermat={(4,0,0):1,(0,4,0):1,(0,0,4):1}
mf,kf,_,_=cubic_koszul_matrices(fermat)
normalizer=fmpq_mat(mf).det()/fmpq_mat(kf).det()
assert abs(normalizer)==4**27
delta=fm.det()/fn.det()/normalizer
mi,ni=fm.inv(),fn.inv()
rows=[[] for _ in range(7)]
t=s.Symbol('t')
for j,e in enumerate(quartics):
    perturb=f.copy();perturb[e]+=t
    p=parameters(perturb)
    for i,name in enumerate(('I3','I6','I9','I12','I15','I18')):
        rows[i].append(str(s.expand(p[name]).coeff(t,1)))
    dm,dn,_,_=cubic_koszul_matrices({e:1})
    rows[6].append(str(delta*(trace_product(mi,dm)-trace_product(ni,dn))))
    print('Derivative',j+1,'of15',flush=True)
jac=s.Matrix([[s.Rational(v) for v in row] for row in rows])
_,pivots=jac.rref()
assert len(pivots)==7
witness=jac[:,list(pivots)].det()
assert witness!=0
prime=101
modular=[]
for row in rows:
    q=[s.Rational(row[j]) for j in pivots]
    assert all(int(v.q)%prime!=0 for v in q)
    modular.append([int(v.p)%prime*pow(int(v.q),-1,prime)%prime for v in q])
modular_determinant=int(nmod_mat(modular,prime).det())
assert modular_determinant!=0
out={'coefficient_order':[list(e) for e in quartics],'point':[f[e] for e in quartics],
     'parameter_order':['I3','I6','I9','I12','I15','I18','I27'],
     'gradient_cubic_matrix':m,'selected_domain_indices':selected,
     'complement_domain_indices':complement,'koszul_complement_matrix':n,
     'normalizer':str(normalizer),
     'discriminant_value':str(delta),'jacobian':rows,'minor_columns':list(pivots),
     'minor_determinant':str(witness),'elapsed_seconds':time.monotonic()-start,
     'modular_minor':{'prime':prime,'matrix':modular,'determinant':modular_determinant},
     'normalization':'I27 is the cubic Koszul determinant quotient, divided by its value at F=x^4+y^4+z^4.'}
(root/'parameter-independence.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8',newline='\n')
print('Nonzero minor columns',pivots,'elapsed',out['elapsed_seconds'],flush=True)
