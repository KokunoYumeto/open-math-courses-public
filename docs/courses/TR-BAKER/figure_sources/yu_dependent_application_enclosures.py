"""Exact endpoints for TR-BAKER-10 Lemma10.155. CC0."""
from fractions import Fraction as F
from pathlib import Path
import json

def certificate():
    lam=F(2099,2100)
    coefficient_upper=F(64*58**2,27*200*7**2)/lam
    assert coefficient_upper<1
    threshold_lower=lam*F(200,58)*105/F(11,4)**5
    assert threshold_lower>2
    assert F(200*5*162,58)>2100
    assert F(104,51)-F(1,672)>2
    records=[]
    for n in range(2,16):
        value=F((n+1)**(n+2),(n-1)**(n-1)*n*n)*F(n+4,n+5)**(n-2)/(n+5)
        assert value>F(11,4)
        records.append({'n':n,'J_over_nplus5':str(value),'gap_above_euler_upper':str(value-F(11,4))})
    assert F(5,2)-F(119,3*16)==F(1,48)
    assert F(4,3)>F(9,8)**2
    assert 256>243 # (n+1)^2/n^(3/2)>3 at the continuous minimum n=3.
    return {'state':'passed_exact_endpoints_with_written_uniform_proof',
        'coefficient_normalized_upper':str(coefficient_upper),
        'threshold_prefactor_lower':str(threshold_lower),
        'J_finite_rows':records,
        'J_infinite':'For n>=16, ln(J_n/(n+5)) >=1+y*(5/2-119*y/3+125*y*y/3)>1+y/48, y=1/n.',
        'scope':'Greedy-basis dependent-list main estimate156; exact coefficient, threshold and scalar-rank envelopes. The written proof supplies the universal quantifiers.'}

if __name__=='__main__':
    data=certificate();(Path(__file__).resolve().parent/'yu-dependent-application-endpoints.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:data[k] for k in ['state','coefficient_normalized_upper','threshold_prefactor_lower']}))
