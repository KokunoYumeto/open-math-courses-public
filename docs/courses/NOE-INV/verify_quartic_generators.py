"""Independently reconstruct and check the finite secondary certificate.

The elimination is a construction aid only. This verifier starts with the
retained monic modulus and coordinates, recomputes the original equations,
unit conditions, contractions, fifty columns and their displayed minor.
"""
from pathlib import Path
import json
import sympy as s
from flint import nmod_poly,nmod_mpoly_ctx
import quartic_fibre as f
from quartic_generators import invariants,secondary_names,secondary_degrees,secondary_powers

root=Path(__file__).resolve().parent
def verify():
    data=json.loads((root/'quartic-generator-certificates/fibre-secondary-rank.json').read_text())
    assert data['prime']==f.P==101 and data['target_primary_values']==[0,0,0,1,1,0,0]
    f.modulus=nmod_poly(data['modulus'],101);G=f.modulus
    assert G.degree()==300 and int(G.leading_coefficient())==1
    assert G.gcd(G.derivative()).degree()==0
    aa=f.Alg(nmod_poly([0,1],101));bb=f.Alg(nmod_poly(data['B'],101));dd=f.Alg(nmod_poly(data['D'],101))
    ev=lambda expr:f.symrat(expr,aa,bb,dd)
    q12,q15=ev(f.values['I12']),ev(f.values['I15'])
    assert not ev(f.p0) and not ev(f.p1) and not q12**5-q15**4
    rows=[[ev(s.diff(expr,v)) for v in (f.A,f.B,f.D)] for expr in (f.p0,f.p1)]
    rows.append([5*q12**4*ev(s.diff(f.values['I12'],v))-4*q15**3*ev(s.diff(f.values['I15'],v)) for v in (f.A,f.B,f.D)])
    jac=(rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
         -rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
         +rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]))
    U=s.symbols('U');A,B,D=f.A,f.B,f.D
    h=A*U**6-9*U**5-4*A*D*U**4+20*A*U**3-4*A*B*U**2-4*A**2*U+A
    ctx=nmod_mpoly_ctx.get(('U','A','B','D'),101,'lex')
    hp=ctx.from_dict({e:int(c)%101 for e,c in s.Poly(h,U,A,B,D).terms()})
    disc=hp.resultant(hp.derivative('U'),'U');node=f.Alg(0)
    for (u,a,b,d),c in disc.to_dict().items():
        assert not u
        node=node+int(c)*aa**a*bb**b*dd**d
    L=s.expand(s.fraction(s.cancel(s.rem(f.p1,f.p0,D)))[0]).coeff(D,1)
    checks={'A':aa,'linear_D_coefficient':ev(L),'I12':q12,'I15':q15,
            'three_equation_Jacobian':jac,'node_sextic_resultant':node,
            'modulus_derivative':f.Alg(G.derivative())}
    assert set(data['unit_witnesses'])==set(checks)
    for name,value in checks.items():
        witness=data['unit_witnesses'][name]
        assert value.serial()==witness['value']
        assert not value*f.Alg(nmod_poly(witness['inverse'],101))-1
    form={(1,1,2):f.Alg(1),(3,0,1):f.Alg(1),(0,3,1):f.Alg(1),(0,4,0):aa,
          (1,3,0):bb,(2,2,0):-f.Alg(9)/2,(3,1,0):dd,(4,0,0):9/(4*aa)}
    inv=invariants(form,include_I6=True)
    assert not inv['I3'] and not inv['I6'] and not inv['I9'] and not inv['I18']
    assert not inv['I12']-q12 and not inv['I15']-q15
    for name,row in data['invariant_values'].items():assert f.alg(inv[name]).serial()==row
    assert list(secondary_names)==data['secondary_names'] and list(map(list,secondary_powers))==data['secondary_powers']
    a=q12/q15;assert a.serial()==data['normalizing_cube']
    assert not a**4*q12-1 and not a**5*q15-1
    cols=[]
    for powers in secondary_powers:
        degree=sum(p*d for p,d in zip(powers,secondary_degrees));v=a**(degree//3)
        for name,p in zip(secondary_names,powers):v=v*inv[name]**p
        cols.append(v.v)
    assert [[int(c) for c in v.coeffs()] for v in cols]==data['secondary_columns']
    minor=[[int(c[i]) for c in cols] for i in range(0,150,3)]
    assert data['minor_rows']==list(range(0,150,3))
    assert f.scalar_det(minor)==data['minor_determinant']==70
    assert f.coefficient_rank(cols,300)[0]==50
    print('Original equations, seven unit witnesses, all twelve contractions, and50-by50 determinant70 modulo101 verified.')
    return True
def verify_hilbert():
    from quartic_hilbert_second import calculate
    from quartic_hilbert import weights,residue,serialize
    fresh=json.loads(json.dumps(calculate()));stored=json.loads((root/'quartic-generator-certificates/hilbert-series.json').read_text())
    for d in (fresh,stored):d.pop('elapsed_seconds',None)
    assert fresh==stored
    first=json.loads((root/'quartic-generator-certificates/first-variable-residues.json').read_text())
    rows=[]
    for i,(a,b) in enumerate(weights):
        if a>=0:continue
        n,d=residue(i);rows.append({'weight':[a,b],'numerator':serialize(n),'denominator':serialize(d)})
    assert rows==first['residues'] and list(map(list,weights))==first['weights']
    from collections import Counter
    degrees=Counter(sum(p*d for p,d in zip(v,secondary_degrees)) for v in secondary_powers)
    assert degrees=={int(k):v for k,v in fresh['expected_numerator_coefficients'].items()}
    print('All six first residues, nine second traces, all-degree rational identity and50 secondary degrees verified.')
if __name__=='__main__':verify_hilbert();verify()
