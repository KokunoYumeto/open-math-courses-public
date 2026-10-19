"""Exact integer certificate for the finite completion of class number one.

All real enclosures use outward-rounded integer intervals. No floating-point
value is used to accept a continued-fraction coefficient or exclude a field.
"""
from pathlib import Path
from fractions import Fraction
from math import isqrt, gcd, factorial
from collections import Counter
import json, hashlib

HERE = Path(__file__).resolve().parent
S = 10**100

def ceildiv(a, b):
    return -((-a)//b)

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def sub(a, b):
    return a[0]-b[1], a[1]-b[0]

def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products)//S, ceildiv(max(products), S)

def div(a, b):
    assert a[0] >= 0 and b[0] > 0
    return a[0]*S//b[1], ceildiv(a[1]*S, b[0])

def scale(a, n):
    assert n >= 0
    return a[0]*n, a[1]*n

def integer(n):
    return n*S, n*S

def sqrt(n):
    v = isqrt(n*S*S)
    return v, v if v*v == n*S*S else v+1

def log_between_one_and_two(x):
    assert S <= x[0] <= x[1] <= 2*S
    t = div(sub(x, integer(1)), add(x, integer(1)))
    t2 = mul(t, t)
    power, total = t, integer(0)
    N = 120
    for j in range(N):
        total = add(total, div(scale(power, 2), integer(2*j+1)))
        power = mul(power, t2)
    # The remaining positive series is at most
    # 2*t^(2N+1)/((2N+1)*(1-t^2)).
    tail = div(scale(power, 2), scale(sub(integer(1), t2), 2*N+1))
    return total[0], total[1]+tail[1]

ln2 = log_between_one_and_two(integer(2))

def log(x):
    assert x[0] >= S
    m = 0
    while x[0] >= 2*S:
        x = div(x, integer(2))
        m += 1
    assert x[1] <= 2*S
    return add(scale(ln2, m), log_between_one_and_two(x))

def decimal(n):
    sign = '-' if n < 0 else ''
    n = abs(n)
    return sign+str(n//S)+'.'+str(n % S).zfill(100)

def display(a):
    return [decimal(a[0]), decimal(a[1])]

def atan_reciprocal(n):
    total = sum((Fraction((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(80)),Fraction(0))
    return total, total+Fraction(1,161*n**161)

a5, a239 = atan_reciprocal(5), atan_reciprocal(239)
pi_rational = (16*a5[0]-4*a239[1],16*a5[1]-4*a239[0])
pi = (int(pi_rational[0]*S),ceildiv(pi_rational[1].numerator*S,pi_rational[1].denominator))
assert pi[0] > 3*S and 7*pi[1] < 22*S

def exp_negative(x):
    assert 0 <= x[0] <= x[1] < 4*S
    term = total = integer(1)
    for n in range(1,121):
        term = div(mul(term,x),integer(n))
        total = add(total,term)
    next_term = div(mul(term,x),integer(121))
    tail = div(next_term,sub(integer(1),div(x,integer(122))))
    return div(integer(1),(total[0],total[1]+tail[1]))

eps = div(add(integer(5), sqrt(21)), integer(2))
eta = add(integer(23), scale(sqrt(33), 4))
l_eps, l_eta = log(eps), log(eta)
assert l_eps[0]*2 > 3*S and l_eps[1] < 2*S
assert l_eta[0] > 3*S and l_eta[1] < 4*S
assert log(integer(3000))[1] < 9*S
assert 100*log(integer(3000))[1] < 801*S
assert log(integer(52500000000000))[1] < 32*S
theta = div(l_eta, l_eps)
lo, hi = Fraction(theta[0], S), Fraction(theta[1], S)
p0, p1, q0, q1 = 0, 1, 1, 0
rows = []
coefficient_bound = 140*10**12
for j in range(100):
    a = lo.numerator//lo.denominator
    assert a == hi.numerator//hi.denominator
    p, q = a*p1+p0, a*q1+q0
    rows.append({'j':j, 'a':a, 'p':p, 'q':q})
    if q > coefficient_bound:
        break
    assert lo > a
    lo, hi = 1/(hi-a), 1/(lo-a)
    p0, p1, q0, q1 = p1, p, q1, q
else:
    raise AssertionError('No denominator crossing')
previous = rows[-2]
p, q = previous['p'], previous['q']
error = sub(scale(theta, q), integer(p))
assert error[0]*error[1] > 0
error_lower = min(abs(error[0]), abs(error[1]))
assert error_lower > S//10**18
assert sum(Fraction(5**j, factorial(j)) for j in range(11)) > 145
assert 145**10 > 3000*10**18
assert 600 > 11*50
assert 10**12 > 11*11059201*32**2

def primes_to(n):
    sieve = bytearray(b'\1')*(n+1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\0'*((n-p*p)//p+1)
    return [i for i in range(2,n+1) if sieve[i]]

def split(D, p):
    if p == 2:
        return D % 8 == 1
    return D % p in {r*r % p for r in range(1,p)}

limit = 600**2
primes = primes_to(limit)
survivors, histogram, witnesses = [], Counter(), []
for d in primes:
    if d <= 8 or d % 4 != 3:
        continue
    witness = None
    for ell in primes:
        if 4*ell >= d:
            break
        if split(-d, ell):
            witness = ell
            break
    if witness is None:
        survivors.append(d)
    else:
        assert 4*witness < d and split(-d,witness)
        histogram[witness] += 1
        witnesses.append([d,witness])
assert survivors == [11,19,43,67,163]

def forms(d):
    found = []
    for a in range(1,isqrt(d//3)+1):
        for b in range(-a,a+1):
            if (b*b+d) % (4*a):
                continue
            c = (b*b+d)//(4*a)
            if c < a or gcd(gcd(a,abs(b)),c) != 1:
                continue
            if (abs(b)==a or a==c) and b < 0:
                continue
            found.append([a,b,c])
    return found

known_discriminants = [3,4,7,8,11,19,43,67,163]
known_forms = {str(d):forms(d) for d in known_discriminants}
assert all(len(v)==1 for v in known_forms.values())
unit_candidates = {}
for k, last in [(21,1),(33,8)]:
    found=[]
    for y in range(1,last+1):
        for norm in [-1,1]:
            n=k*y*y+4*norm
            x=isqrt(n)
            if x*x==n and (x-y)%2==0:
                found.append([x,y,norm])
    unit_candidates[str(k)] = found
assert unit_candidates == {'21':[[5,1,1]],'33':[[46,8,1]]}
examples = {str(k):{'h_negative':len(forms(163*k)),
                    'forms':forms(163*k)} for k in [21,33]}
for k, coefficient, logarithm in [(21,Fraction(32,21),l_eps),(33,Fraction(80,33),l_eta)]:
    exponent = div(mul(pi,sqrt(163)),integer(k))
    qk = exp_negative(exponent)
    one_minus = sub(integer(1),qk)
    bound = div(scale(qk,2*k),mul(one_minus,one_minus))
    main = div(scale(mul(pi,sqrt(163)),coefficient.numerator),integer(coefficient.denominator))
    residual = sub(scale(logarithm,examples[str(k)]['h_negative']),main)
    assert max(map(abs,residual)) < bound[0]
    examples[str(k)].update(residual=display(residual),proved_bound=display(bound),q=display(qk))
record={'state':'passed_exact_integer_certificate','scale':str(S),
        'source_sha256':hashlib.sha256((HERE.parent/'src/TR-BAKER-18.md').read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'log_series_terms':120,'log_epsilon':display(l_eps),'log_eta':display(l_eta),
        'theta':display(theta),'continued_fraction':rows,
        'coefficient_bound':coefficient_bound,'best_error_interval':display(error),
        'best_error_greater_than':'1e-18','finite_discriminant_bound':limit,
        'tested_prime_discriminants':len(witnesses)+len(survivors),
        'excluded_prime_discriminants':len(witnesses),
        'split_prime_histogram':dict(sorted(histogram.items())),
        'all_split_prime_witnesses':witnesses,'surviving_prime_discriminants':survivors,
        'all_class_one_reduced_forms':known_forms,'fundamental_unit_candidates':unit_candidates,
        'example_d163':examples,
        'limits':'Uses the written logarithmic bound to reach d<10^24, proved continued-fraction best approximation to reach d<360000, and the written split-prime obstruction. The finite sieve and all accepted rounding steps are exact integer operations.'}
(HERE/'class-number-one-check.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:record[k] for k in ['state','source_sha256','checker_sha256',
      'best_error_greater_than','finite_discriminant_bound','tested_prime_discriminants',
      'excluded_prime_discriminants','surviving_prime_discriminants']}))
