"""Verify the finite identities used in the seven-parameter proof."""
from pathlib import Path
import json
import sympy as s
from flint import fmpq,fmpq_mpoly_ctx,fmpq_mat,nmod_mat
from quartic_algebra import from_expr,parameters,cubic_koszul_matrices

root=Path(__file__).resolve().parent/'quartic-certificates'
symbols=s.symbols('A B C D E L M N x y z')
local={str(t):t for t in symbols};x,y,z=(local[n] for n in ('x','y','z'))
load=lambda name:json.loads((root/name).read_text())
def unpack(entries,ctx):
    return ctx.from_dict({tuple(t['exponents']):fmpq(t['coefficient']) for t in entries})

for case in ('1.1','1.2','2.1','2.2','2.3'):
    r=load('case-'+case+'.json')
    form=s.sympify(r['normal_form'],locals=local)
    computed=parameters(from_expr(form,(x,y,z)))
    assert all(s.expand(computed[n]-s.sympify(v,locals=local))==0 for n,v in r['values'].items())
print('All five contraction tables verified.',flush=True)
r=load('case-2.1-resultants.json');ctx=fmpq_mpoly_ctx.get(('D','B','A'),'lex')
p=[unpack(a,ctx) for a in r['inputs']]
table=load('case-2.1.json')
for polynomial,name in zip(p,('I9','I12','I15','I18')):
    expr=s.fraction(s.cancel(s.sympify(table['values'][name],locals=local).subs(local['E'],s.Rational(9,4)/local['A'])))[0]
    q=ctx.from_dict({e:fmpq(int(c.p),int(c.q)) for e,c in s.Poly(expr,local['D'],local['B'],local['A']).terms()})
    assert q==polynomial
rd=[p[0].resultant(p[i],'D') for i in (1,2,3)]
assert all(q==unpack(v,ctx) for q,v in zip(rd,r['D_resultants']))
rb=[rd[i].resultant(rd[j],'B') for i,j in ((0,1),(0,2),(1,2))]
assert all(q==unpack(v,ctx) for q,v in zip(rb,r['B_resultants']))
g=ctx.constant(0)
for q in rb:g=g.gcd(q)
_,_,A=ctx.gens()
assert g==unpack(r['gcd'],ctx)==A**66*(2*A+3)**8*(4*A*A-6*A+9)**8/16777216
print('Both stages of resultants and exact gcd verified.',flush=True)
for branch,r in load('branch-identities.json').items():
    if not isinstance(r,dict):continue
    ctx=fmpq_mpoly_ctx.get(tuple(r['variables']),'lex')
    inputs=[unpack(a,ctx) for a in r['inputs']]
    A,B,D,E=(local[n] for n in ('A','B','D','E'))
    source=[s.fraction(s.sympify(table['values'][n],locals=local))[0]
            for n in ('I9','I12','I15','I18')]
    if branch=='first':
        expected=[s.expand(q.subs({A:-s.Rational(3,2),E:-s.Rational(3,2)})) for q in source]
        targets=[B+D+s.Rational(15,2),(B+s.Rational(15,4))**2]
    else:
        assert branch=='second'
        expected=[s.expand(q.subs(E,s.Rational(3,2)-A)) for q in source]+[4*A*A-6*A+9]
        targets=[2*A*B/3-5*A-B+D,(B-s.Rational(15,4)+5*A/2)**2]
    def convert(expr):
        return ctx.from_dict({e:fmpq(int(c.p),int(c.q))
                              for e,c in s.Poly(expr,*[local[n] for n in r['variables']]).terms()})
    assert inputs==[convert(q) for q in expected]
    for identity,target in zip(r['identities'],targets):
        coefficients=[unpack(a,ctx) for a in identity['coefficients']]
        assert sum((a*b for a,b in zip(inputs,coefficients)),ctx.constant(0))==unpack(identity['target'],ctx)==convert(target)
print('All four branch ideal-membership identities verified by multiplication.',flush=True)
r=load('parameter-independence.json')
point={tuple(e):c for e,c in zip(r['coefficient_order'],r['point'])}
mm,kk,selected,complement=cubic_koszul_matrices(point)
assert mm==r['gradient_cubic_matrix'] and kk==r['koszul_complement_matrix']
assert selected==r['selected_domain_indices'] and complement==r['complement_domain_indices']
m,k=fmpq_mat(r['gradient_cubic_matrix']),fmpq_mat(r['koszul_complement_matrix'])
assert m.det()/k.det()/fmpq(r['normalizer'])==fmpq(r['discriminant_value'])
mf,kf,_,_=cubic_koszul_matrices({(4,0,0):1,(0,4,0):1,(0,0,4):1})
assert fmpq_mat(mf).det()/fmpq_mat(kf).det()==fmpq(r['normalizer'])
mi,ki=m.inv(),k.inv();t=s.Symbol('t')
def trace(a,b):
    return sum((a[i,j]*b[j][i] for i in range(a.nrows()) for j in range(a.ncols())),fmpq(0))
for j,e in enumerate(point):
    perturb=point.copy();perturb[e]+=t
    result=parameters(perturb)
    assert all(s.expand(result[n]).coeff(t,1)==s.Rational(r['jacobian'][i][j])
               for i,n in enumerate(('I3','I6','I9','I12','I15','I18')))
    dm,dk,_,_=cubic_koszul_matrices({e:1})
    assert fmpq(r['discriminant_value'])*(trace(mi,dm)-trace(ki,dk))==fmpq(r['jacobian'][6][j])
jac=s.Matrix([[s.Rational(v) for v in row] for row in r['jacobian']])
assert jac[:,r['minor_columns']].det()==s.Rational(r['minor_determinant'])!=0
q=r['modular_minor'];prime=q['prime']
reduced=[[int(v.p)%prime*pow(int(v.q),-1,prime)%prime for v in jac[i,r['minor_columns']]] for i in range(7)]
assert reduced==q['matrix'] and int(nmod_mat(reduced,prime).det())==q['determinant']==47
print('Rational determinant quotient and modular nonzero Jacobian minor verified.',flush=True)
