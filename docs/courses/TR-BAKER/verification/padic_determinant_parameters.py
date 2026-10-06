"""Finite independent arithmetic checks for the Lesson 10 proof. CC0.

These checks do not replace the general proofs in the lesson. They test exact
small determinants (including common p-parts), the centering endpoint, and
parameter inequalities in varied degree and height regimes.
"""
from fractions import Fraction
from math import comb
import json
import mpmath as mp
import sympy as sp


def valuation(value, p):
    value = abs(int(value))
    if value == 0:
        raise ValueError('Valuation sample must be nonzero')
    result = 0
    while value % p == 0:
        result += 1
        value //= p
    return result


def determinant_checks():
    checks = []
    columns = [(r, s) for r in range(3) for s in range(2)]
    for p in [2, 3, 5, 7]:
        t = 1 if p == 2 else 0
        c = p**t
        precision = 12 if p == 2 else 6
        a, b = 1+p, 1+p+p**precision
        for u in [0, 1, 2]:
            exponent = p**u
            rows = [[comb(exponent*(r+s), k) *
                     a**(p**t*l*r)*b**(p**t*l*s)
                     for r, s in columns]
                    for l in range(2) for k in range(3)]
            det = sp.Matrix(rows).det()
            exact = valuation(det, p)
            difference = valuation(a**exponent-b**exponent, p)
            assert difference >= c*Fraction(11, 2)+u
            bound = c*9 - 6*mp.log(6)/mp.log(p)
            assert mp.mpf(exact) >= bound
            checks.append({'p':p, 'u':u, 'difference_valuation':difference,
                           'determinant_valuation':exact,
                           'proved_lower_bound':str(bound)})
    return checks


def centering_checks():
    count = 0
    for K in range(1, 6):
        for L in range(1, 14):
            weights = [Fraction(l) - Fraction(L-1, 2)
                       for l in range(L) for _ in range(K)]
            assert sum(weights) == 0
            for R in [1, 2, 3, 8, 17]:
                extremum = (R-1)*sum(w for w in weights if w > 0)
                exact = Fraction(K*(R-1)*(L*L//4), 2)
                assert extremum == exact <= Fraction(K*L*L*(R-1), 8)
                count += 1
    return count


def parameter_checks():
    count = 0
    # The two lowest budgets, unequal heights, and large simultaneous heights.
    for p in [2, 3, 5, 11, 31, 101]:
        lp = mp.log(p)
        for d in [1, 2, 3, 7, 20, 40]:
            for factors in [(1,1), (1,10), (100,1), (1000,1000)]:
                a1, a2 = [mp.mpf(v)/lp for v in factors]
                G = mp.mpf(p)**d-1
                z = G*a1*a2
                assert z >= d*d
                for b1,b2 in [(1,1), (5,17), (10**12,3)]:
                    X = b1/a2+b2/a1
                    B = max(mp.mpf(10), d*mp.log(X)/lp)
                    L = int(mp.floor(2*B))+2
                    K = int(mp.floor(256*z*L))+1
                    R1 = int(mp.floor(mp.sqrt(G*L*a2/a1)))+1
                    S1 = int(mp.floor(mp.sqrt(G*L*a1/a2)))+1
                    R2 = int(mp.floor(mp.sqrt(G*(K-1)*L*a2/a1)))+1
                    S2 = int(mp.floor(mp.sqrt(G*(K-1)*L*a1/a2)))+1
                    R,S,N = R1+R2-1,S1+S2-1,K*L
                    assert R1*S1 > G*L
                    assert R2*S2 > G*(K-1)*L
                    beta_upper = ((R-1)*b2+(S-1)*b1)*mp.e**2/(2*(K-1))
                    assert beta_upper < X
                    assert K*(L-1) > 3*d*mp.log(N)/lp+(K-1)*B+L*((R-1)*a1+(S-1)*a2)
                    u = min(valuation(b1,p) if b1 % p == 0 else 0,
                            valuation(b2,p) if b2 % p == 0 else 0)
                    assert 2*N+u < 2500*z*B*B
                    count += 1
    return count


def deep_unit_checks():
    determinants = []
    columns = [(r, s) for r in range(3) for s in range(2)]
    for p in [2, 3, 5, 11]:
        for E in [mp.mpf('1.5'), mp.mpf(2), mp.mpf(4)]:
            depth, precision = int(mp.ceil(E)), int(mp.ceil(6*E))
            a, b = 1+p**depth, 1+p**depth+p**precision
            for u in [0, 1]:
                exponent = p**u
                rows = [[comb(exponent*(r+s), k)*a**(l*r)*b**(l*s)
                         for r, s in columns] for l in range(2) for k in range(3)]
                exact = valuation(sp.Matrix(rows).det(), p)
                difference = valuation(a**exponent-b**exponent, p)
                bound = 9*E-6*mp.log(6)/mp.log(p)
                assert difference >= E*mp.mpf('5.5')+u
                assert exact >= bound
                determinants.append({'p':p,'E':str(E),'u':u,
                                     'determinant_valuation':exact,
                                     'proved_lower_bound':str(bound)})
    parameter_count = 0
    for p in [2, 3, 5, 11, 31, 101]:
        G, lp = mp.mpf(p-1), mp.log(p)
        for E in [1/G+mp.mpf('.001'), mp.mpf(2), mp.mpf(10), mp.mpf(100)]:
            for a1,a2 in [(1,1),(1,10),(100,1),(1000,1000)]:
                z=G*a1*a2
                for b1,b2 in [(1,1),(p,p),(p**3,p**2),(10**12+1,3)]:
                    u=min(valuation(b1,p) if b1 % p == 0 else 0,
                          valuation(b2,p) if b2 % p == 0 else 0)
                    if (b2//p**u) % p == 0:
                        continue
                    X=mp.mpf(b1)/a2+mp.mpf(b2)/a1
                    B=max(mp.mpf(10),mp.log(X)/(E*lp))
                    L=int(mp.floor(2*B))+2
                    K=int(mp.floor(256*z*L))+1
                    R1=int(mp.floor(mp.sqrt(G*L*a2/a1)))+1
                    S1=int(mp.floor(mp.sqrt(G*L*a1/a2)))+1
                    R2=int(mp.floor(mp.sqrt(G*(K-1)*L*a2/a1)))+1
                    S2=int(mp.floor(mp.sqrt(G*(K-1)*L*a1/a2)))+1
                    R,S,N=R1+R2-1,S1+S2-1,K*L
                    assert R1*S1>G*L and R2*S2>G*(K-1)*L
                    assert K*(L-1)>3*mp.log(N)/(E*lp)+(K-1)*B+L*((R-1)*a1+(S-1)*a2)
                    assert E*N+u<1300*E*z*B**2
                    assert mp.log(z)/(E*z*lp)<1
                    parameter_count+=1
    family=[]
    for m in range(1,13):
        a,b=1+5**m,1+2*5**m
        assert valuation(a-b,5)==m
        U=mp.log(a)*mp.log(b)/mp.log(5)**2
        family.append({'m':m,'valuation':m,'height_product':str(U),
                       'precision_budget':str(U/m)})
    return {'determinants':determinants,'parameter_cases':parameter_count,
            'near_one_family':family}


def main():
    mp.mp.dps = 120
    result = {'determinants':determinant_checks(),
              'centering_cases':centering_checks(),
              'parameter_cases':parameter_checks(),
              'deep_unit_refinement':deep_unit_checks()}
    # Check the counterexample to the unrestricted y = 1 statement exactly.
    x = 3**10+1
    assert valuation(x*x-1, 3) == 10
    result['y_equals_one_counterexample'] = {'p':3,'x':x,'y':1,'valuation':10,'claimed_bound':4}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
