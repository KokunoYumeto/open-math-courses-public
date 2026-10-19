"""Independent finite L-values versus the proved Fourier limit, with interval tails."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import hashlib, json, math
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
iv = mp.iv
iv.dps = 55

def chi(D, n):
    return int(sp.kronecker_symbol(D, int(n)))

def forms(d):
    result = []
    for a in range(1, math.isqrt(d // 3) + 1):
        for b in range(-a, a + 1):
            if (b*b+d) % (4*a):
                continue
            c = (b*b+d)//(4*a)
            if c < a or math.gcd(math.gcd(a, abs(b)), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            result.append((a, b, c))
    return result

def endpoint(t, rounding):
    sign, man, exponent, _ = t
    man, exponent, sign = int(man), int(exponent), int(sign)
    if exponent < 0:
        exact = Decimal((sign, tuple(map(int, str(man*5**(-exponent)))), exponent))
    else:
        exact = Decimal((-1)**sign*(man << exponent))
    with localcontext() as ctx:
        ctx.prec = 45
        ctx.rounding = rounding
        return str(+exact)

def bounds(x):
    return [endpoint(x._mpi_[0], ROUND_FLOOR),
            endpoint(x._mpi_[1], ROUND_CEILING)]

def l_one(D):
    q = abs(D)
    if D < 0:
        moment = sum(j*chi(D, j) for j in range(1, q))
        return -iv.pi * moment / (q*iv.sqrt(q))
    return -sum((chi(D, j)*iv.ln(2*iv.sin(iv.pi*j/q))
                 for j in range(1, q)), iv.mpf(0))/iv.sqrt(q)

def fourier(d, k, R, selected=()):
    fs = forms(d)
    primes = list(sp.factorint(k))
    leading = iv.pi**2/6
    for p in primes:
        leading *= 1-iv.mpf(1)/int(p)**2
    leading *= sum((iv.mpf(chi(k, a))/a for a,b,c in fs), iv.mpf(0))
    zero = iv.mpf(0)
    if len(primes) == 1:
        zero = -2*iv.pi/(k*iv.sqrt(d))*iv.ln(int(primes[0]))*sum(chi(k,a) for a,b,c in fs)
    value = leading + zero
    character = [chi(k, j) for j in range(k)]
    snapshots = {}
    magnitudes = []
    for r in range(1, R+1):
        combined = iv.mpf(0)
        for a,b,c in fs:
            q = iv.exp(-iv.pi*iv.sqrt(d)/(k*a))
            inner = iv.mpf(0)
            for y0 in sp.divisors(r):
                y = int(y0)
                finite = sum((character[(a*j*j+b*j*y+c*y*y)%k]
                              *iv.cos(2*iv.pi*r*j/(k*y)+iv.pi*r*b/(k*a))
                              for j in range(k)), iv.mpf(0))
                inner += finite/y
            combined += 4*iv.pi/(k*iv.sqrt(d))*q**r*inner
        value += combined
        magnitudes.append(bounds(abs(combined)))
        if r in selected:
            tail = remainder(d,k,r,fs)
            snapshots[str(r)] = {'partial_sum':bounds(value), 'tail_bound':bounds(tail)[1],
                                  'enclosure':bounds(value+iv.mpf([-1,1])*tail)}
    tail = remainder(d,k,R,fs)
    return {'leading':leading, 'zero':zero, 'partial':value, 'tail':tail,
            'enclosure':value+iv.mpf([-1,1])*tail, 'snapshots':snapshots,
            'terms':magnitudes, 'forms':fs}

def remainder(d,k,R,fs):
    total = iv.mpf(0)
    for a,b,c in fs:
        q = iv.exp(-iv.pi*iv.sqrt(d)/(k*a))
        total += q**(R+1)*((R+1)-R*q)/(1-q)**2
    return 4*iv.pi/iv.sqrt(d)*total

records=[]
for d,k,R in [(11,21,80),(11,5,35),(7,33,220),(23,5,80),(84,5,100)]:
    assert math.gcd(d,k)==1
    left=l_one(k)*l_one(-d*k)
    right=fourier(d,k,R,selected=(5,10,20,40,80))
    assert right['partial'].b-right['partial'].a < iv.mpf('1e-50')
    difference=left-right['partial']
    assert abs(difference) <= right['tail'], (d,k,bounds(difference),bounds(right['tail']))
    records.append({'d':d,'k':k,'R':R,'forms':right['forms'],
                    'L_positive':bounds(l_one(k)), 'L_negative':bounds(l_one(-d*k)),
                    'product':bounds(left), 'leading':bounds(right['leading']),
                    'zero_coefficient_sum':bounds(right['zero']),
                    'fourier_partial':bounds(right['partial']),
                    'tail_bound':bounds(right['tail'])[1],
                    'fourier_enclosure':bounds(right['enclosure']),
                    'product_minus_partial':bounds(difference),
                    'snapshots':right['snapshots'],
                    'nonzero_frequency_pair_absolute_values':right['terms']})
assert forms(11)==[(1,1,3)]
assert sum(j*chi(-231,j) for j in range(1,231)) == -2772
assert [sum(j*chi(-231,j) for j in range(21*m+1,21*(m+1)+1))
        for m in range(11)] == [81,98,123,116,-82,21,149,-346,-339,-595,-1998]
assert all(chi(21,n)*chi(-11,n)==chi(-231,n) for n in range(462))
record={'utc':datetime.now(timezone.utc).isoformat(),
        'state':'passed_interval_comparisons', 'mpmath_version':mp.__version__,
        'interval_decimal_precision':iv.dps, 'cases':records,
        'sources':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in [HERE.parent/'src/TR-BAKER-17.md']},
        'limits':'Interval evaluations check the displayed finite L-value and Fourier formulas against one another. The infinite tail is bounded by the written proof of (17.31); finite tests alone do not prove the general identity.'}
(HERE/'class-number-fourier-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'state':record['state'],'cases':[{k:r[k] for k in ['d','k','R','product','fourier_partial','tail_bound']} for r in records]}))
