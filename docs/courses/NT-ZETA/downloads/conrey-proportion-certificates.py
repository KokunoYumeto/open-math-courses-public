from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
from datetime import datetime, timezone
import json
import mpmath as mp

mp.mp.dps = 70
root = Path(__file__).resolve().parent

def approx(x):
    return mp.mpf(x.numerator)/x.denominator

def exponential_bounds(x, n=100):
    lower = sum((x**j/F(factorial(j)) for j in range(n+1)), F(0))
    next_term = x**(n+1)/F(factorial(n+1))
    ratio = x/F(n+2)
    assert 0 <= ratio < 1
    return lower, lower+next_term/(1-ratio)

def mul(p, q):
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out

def integral(p):
    return sum((c/F(j+1) for j,c in enumerate(p)), F(0))

def exp_integral_pair(p, lam):
    # Integral_0^1 exp(lam*v)*v^j dv = a_j*exp(lam)+b_j.
    moments = [(1/lam, -1/lam)]
    for j in range(1, len(p)):
        a,b = moments[-1]
        moments.append((1/lam-F(j)*a/lam, -F(j)*b/lam))
    return tuple(sum((p[j]*moments[j][h] for j in range(len(p))), F(0))
                 for h in range(2))

def interval(pair, lo, hi):
    a,b = pair
    return (a*lo+b, a*hi+b) if a >= 0 else (a*hi+b, a*lo+b)

def reflected(p):
    out = [F(0)]*len(p)
    for j,c in enumerate(p):
        for k in range(j+1):
            out[k] += c*F(comb(j,k))*(-1)**k
    return out

def ceiling_bound(x, scale=10**9):
    return F((x.numerator*scale+x.denominator-1)//x.denominator,scale)

full_q = [F(0)]*8
full_q[0] = F(492,1000)
for degree, coeff in [(1,F(602,1000)),(3,-F(8,100)),
                      (5,-F(6,100)),(7,F(46,1000))]:
    for j in range(degree+1):
        full_q[j] += coeff*comb(degree,j)*(-2)**j

theta = F(28571,50000)
assert theta < F(4,7)
cases = []
for name, q, R, target, fixed_alpha in [
        ('critical_line', full_q, F(32,25), F(4077,10000), None),
        ('simple_critical_line', [F(1),-F(51,50)],
         F(6,5), F(401,1000), F(26,25))]:
    assert q[0] == 1
    qref = reflected(q)
    sym = [x+y for x,y in zip(q,qref)]
    assert all(x==0 for x in sym[1:]) and sym[0] != 0
    lo,hi = exponential_bounds(2*R)
    iq_pair = exp_integral_pair(mul(q,q), 2*R)
    d = [R*x for x in q]
    for j in range(1,len(q)):
        d[j-1] += j*q[j]
    id_pair = exp_integral_pair(mul(d,d), 2*R)
    iq = interval(iq_pair,lo,hi)
    idv = interval(id_pair,lo,hi)
    assert iq[0]>0 and idv[0]>0
    if fixed_alpha is None:
        opt = approx(theta)*mp.sqrt(approx((idv[0]+idv[1])/(iq[0]+iq[1])))
        alpha = F(int(mp.nint(opt*10**6)),10**6)
    else:
        alpha = fixed_alpha
    # A fixed degree17 polynomial, normalized to P(1)=1 exactly.
    p = [F(0)]*18
    weights = [alpha**(2*j+1)/F(factorial(2*j+1)) for j in range(9)]
    denominator = sum(weights)
    for j,weight in enumerate(weights):
        p[2*j+1] = weight/denominator
    assert p[0]==0 and sum(p)==1
    dp = [(j+1)*p[j+1] for j in range(len(p)-1)]
    I0, I1 = integral(mul(p,p)), integral(mul(dp,dp))
    qone = sum(q)
    cup = (q[0]**2+hi*qone*qone)/2 + I1*iq[1]/theta + theta*I0*idv[1]
    target_exp_lo,target_exp_hi = exponential_bounds(R*(1-target))
    assert cup < target_exp_lo, name
    compact = {
        'exp_2R': ceiling_bound(hi, 1000),
        'I0': ceiling_bound(I0), 'I1': ceiling_bound(I1),
        'IQ': ceiling_bound(iq[1]), 'ID': ceiling_bound(idv[1])
    }
    compact_c = ((1+compact['exp_2R']*qone*qone)/2+
                 compact['I1']*compact['IQ']/theta+
                 theta*compact['I0']*compact['ID'])
    rational_c = F(533,250) if name=='critical_line' else F(20513,10000)
    target_arg = R*(1-target)
    target_six = sum((target_arg**j/F(factorial(j)) for j in range(7)),F(0))
    assert cup <= compact_c < rational_c < target_six
    simple = len(q)==2
    if simple:
        assert -q[1] not in (0,2)
    cases.append({
        'claim': name, 'theta': str(theta), 'R': str(R),
        'target_strict_proportion': str(target),
        'Q_coefficients_ascending': [str(x) for x in q],
        'Q_at_one': str(qone), 'Q_symmetry_constant': str(sym[0]),
        'alpha_for_polynomial': str(alpha),
        'P_coefficients_ascending': [str(x) for x in p],
        'P_degree':17, 'I0_exact':str(I0), 'I1_exact':str(I1),
        'exp_2R_lower':str(lo), 'exp_2R_upper':str(hi),
        'IQ_linear_exp_pair':[str(x) for x in iq_pair],
        'ID_linear_exp_pair':[str(x) for x in id_pair],
        'c_upper_exact':str(cup),
        'target_exponential_lower_exact':str(target_exp_lo),
        'positive_exact_margin':str(target_exp_lo-cup),
        'compact_upper_bounds':{k:str(x) for k,x in compact.items()},
        'compact_c_upper_exact':str(compact_c),
        'intermediate_c_upper':str(rational_c),
        'compact_c_to_intermediate_margin':str(rational_c-compact_c),
        'target_degree_six_lower':str(target_six),
        'target_six_to_intermediate_margin':str(target_six-rational_c),
        'c_upper_descriptive':mp.nstr(approx(cup),25),
        'proportion_descriptive':mp.nstr(1-mp.log(approx(cup))/approx(R),25),
        'all_hypotheses_checked':True,
        'all_certificate_bounds_exact_rational':True
    })

record = {
    'recorded_utc':datetime.now(timezone.utc).isoformat(),
    'nature':'Exact Fraction arithmetic certificates. Both exponential bounds use a positive degree100 Taylor sum and a geometric upper bound for its tail. mpmath only chooses a rational polynomial parameter and prints descriptive decimals; it supplies no certificate inequality.',
    'cases':cases, 'all_assertions_passed':True
}
(root/'conrey_proportion_certificates.json').write_text(
    json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_assertions_passed':True,
                  'claims':[{k:c[k] for k in ('claim','alpha_for_polynomial',
                       'c_upper_descriptive','proportion_descriptive',
                       'compact_upper_bounds','intermediate_c_upper',
                       'compact_c_to_intermediate_margin',
                       'target_six_to_intermediate_margin')}
                            for c in cases]}))
