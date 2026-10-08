"""Exact component spans, four principal-root valuations and norm. CC0."""
from pathlib import Path
from fractions import Fraction
import json

def rank2(vectors):
    nonzero = {v for v in vectors if v != (0, 0)}
    return 0 if not nonzero else (1 if len(nonzero) == 1 else 2)

def certificate():
    examples = [
        {'value': 'U1 U2', 'vectors': [(1, 1)]},
        {'value': '1 + U1', 'vectors': [(0, 0), (1, 0)]},
        {'value': '2 - U1 - U2', 'vectors': [(0, 0), (1, 0), (0, 1)]},
    ]
    for example in examples:
        example['rank'] = rank2(example['vectors'])
        example['degree'] = 2 ** example['rank']
    p = 73; modulus = p * p; roots = [2702, 74]
    assert [x % p for x in roots] == [1, 1]
    assert [x*x % modulus for x in roots] == [74, 147]
    valuations=[]; values=[]
    for signs in [(1,1),(-1,1),(1,-1),(-1,-1)]:
        value=(2-signs[0]*roots[0]-signs[1]*roots[1]) % modulus
        assert value != 0
        valuation=1 if value % p == 0 else 0
        values.append(value);valuations.append(valuation)
    assert valuations == [1,0,0,0]
    # (X^2 - 4X - 217)^2 - 4*74*147, exact convolution.
    square=[0]*5;quad=[-217,-4,1]
    for i,a in enumerate(quad):
        for j,b in enumerate(quad):square[i+j]+=a*b
    square[0]-=4*74*147
    assert square == [3577,1736,-418,-8,1] and square[0]==49*p
    return {'state':'passed','examples':examples,'prime':p,'root_modulus':modulus,
            'principal_roots_mod_p_squared':roots,'conjugate_values_mod_p_squared':values,
            'valuations':valuations,'minimal_polynomial_coefficients_ascending':square,
            'norm':3577,'norm_valuation':1,
            'scope':'Exact illustration of the proved component-field mechanism; no second-induction integer-zero family asserted.'}

if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
    data=certificate()
    if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data))
