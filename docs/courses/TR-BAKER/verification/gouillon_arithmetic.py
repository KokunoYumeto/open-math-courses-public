"""Exact finite checks for the derivative arithmetic in the two-logarithm lesson.

Uses only the Python standard library. These checks supplement the full proofs;
they do not prove the general multiplicity estimate or the final numerical bounds.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, lcm
import json


def product_poly(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


@lru_cache(None)
def binomial_poly(n):
    p = [F(1)]
    for i in range(n):
        p = product_poly(p, [F(-i), F(1)])
    return tuple(x / factorial(n) for x in p)


@lru_cache(None)
def delta(b, t):
    q, r = divmod(t, b)
    p = list(binomial_poly(r))
    for _ in range(q):
        p = product_poly(p, binomial_poly(b))
    return tuple(p)


def divided_derivative(p, x, k):
    return sum((p[j] * comb(j, k) * x ** (j - k)
                for j in range(k, len(p))), F(0))


def log_unit(x, terms=45):
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    lo = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    hi = lo + 2 * z ** (2*terms+1) / ((2*terms+1) * (1-z*z))
    return lo, hi


LOG2 = log_unit(F(2))


@lru_cache(None)
def log_integer(n):
    exponent = n.bit_length() - 1
    lo, hi = log_unit(F(n, 2 ** exponent))
    return lo + exponent*LOG2[0], hi + exponent*LOG2[1]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        d = a[pivot][col]
        a[pivot] = [x/d for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            d = a[i][col]
            if d:
                a[i] = [x-d*y for x,y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def main():
    counts = {}
    n_integral = n_growth = 0
    for b in range(1, 6):
        multiplier = lcm(*range(1, b+1))
        for t in range(16):
            p = delta(b, t)
            for x in range(-4, 9):
                for k in range(min(t, 6)+1):
                    value = multiplier**k * divided_derivative(p, x, k)
                    assert value.denominator == 1
                    n_integral += 1
            for x in range(9):
                for k in range(t+1):
                    value = abs(divided_derivative(p, x, k))
                    h = max(8, b-1)
                    bound = F(comb(t, k)*h**(t-k), b**t) * F(271, 100)**(t+b)
                    assert value <= bound
                    n_growth += 1
    counts['integral_divided_derivatives'] = n_integral
    counts['derivative_growth_checks'] = n_growth

    n_mixture = 0
    for kmax in range(1, 81):
        c = F((kmax+1)*(kmax+2), 2)
        s = kmax*c/3
        lhs = sum(((kmax+1-k)*sum((log_integer(j)[0] for j in range(1,k+1)),F(0))
                   for k in range(1,kmax+1)), F(0))
        rhs = s*(log_integer(kmax)[1]-F(11,6))
        assert lhs >= rhs
        for k in range(1, kmax+1):
            mass = F(6*comb(kmax-1,k-1)*factorial(k)*factorial(kmax+1-k),
                     factorial(kmax+2))
            assert mass == F(k*(kmax+1-k), s)
            n_mixture += 1
        if kmax <= 40:
            for u in (F(1,7), F(1,2), F(6,7)):
                reciprocal = sum((F(kmax,j+1)*comb(kmax-1,j)*u**j*(1-u)**(kmax-1-j)
                                  for j in range(kmax)), F(0))
                assert reciprocal == (1-(1-u)**kmax)/u <= 1/u
    counts['triangular_factorial_checks'] = 80
    counts['beta_mixture_identities'] = n_mixture
    counts['reciprocal_mean_identities'] = 120

    n_occupancy = 0
    for q in range(1, 13):
        for tmax in range(17):
            for n in range(1, q*(tmax+1)+1):
                m, r = divmod(n, q)
                exact = n*tmax - q*m*(m-1)//2-r*m
                upper = n*tmax-F(n*n,2*q)+F(n,2)
                omega = 1-F(n,2*q*(tmax+1))
                omega0 = F(2*q*(tmax+1),n)
                assert exact <= upper <= n*(omega*tmax+omega0)
                n_occupancy += 1
    counts['occupancy_checks_including_zero_order'] = n_occupancy

    kmax, lmax, tmax, b = 2, 2, 3, 2
    rows = [(k0,k1,l) for k0 in range(kmax+1)
            for k1 in range(kmax+1-k0) for l in range(lmax+1)]
    cols = [(r,s,t) for r in range(4) for s in range(3) for t in range(tmax+1)]
    pos = {row:i for i,row in enumerate(rows)}
    original = [[F((2*r+3*s)**k1*comb(t,k0)*l**(t-k0)*2**(r*l)*3**(s*l))
                 if t >= k0 else F(0) for r,s,t in cols] for k0,k1,l in rows]
    changed = [[divided_derivative(binomial_poly(k1),2*r+3*s,0)
                *2**k0*divided_derivative(delta(b,t),l,k0)*2**(r*l)*3**(s*l)
                for r,s,t in cols] for k0,k1,l in rows]
    for i,(k0,k1,l) in enumerate(rows):
        for j,(r,s,t) in enumerate(cols):
            predicted = F(0)
            for low,c0 in enumerate(binomial_poly(k1)):
                for v,cv in enumerate(delta(b,t)):
                    predicted += 2**k0*c0*cv*original[pos[k0,low,l]][j-t+v]
            assert predicted == changed[i][j]
            assert changed[i][j].denominator == 1
    rank_original, rank_changed = rank(original), rank(changed)
    assert rank_original == rank_changed == len(rows)
    counts['basis_transformation_entries'] = len(rows)*len(cols)
    counts['example_ranks'] = [rank_original, rank_changed]

    n_spaces = 0
    for k in range(1,7):
        for d in range(13):
            space = []
            for k0 in range(k+1):
                for k1 in range(k+1-k0):
                    e = d-k0-k1
                    if e < 0:
                        continue
                    vector = [F(0)]*(d+1)
                    for j in range(e+1):
                        vector[k0+j] = F(comb(e,j)*2**(e-j))
                    space.append(vector)
            assert rank(space) == min(d+1,k+1)
            n_spaces += 1
    counts['homogeneous_Taylor_space_checks'] = n_spaces
    n_orders = 0
    for k in range(1,21):
        c = k+1
        for m in range(201):
            exact = sum(j//c for j in range(m))
            coarse = F(m*m,2*c)-F(m,2)
            claimed = F(m,2)*(F(m+1,c)-F(k,2)-1)
            assert exact >= coarse >= claimed
            n_orders += 1
    counts['Taylor_degree_capacity_checks'] = n_orders
    n_quadratics = 0
    for k in range(1,21):
        for l in range(1,61):
            a0 = F(k+2,4)
            # v=a0*l+a0*sqrt(l*l-1); check both radical coefficients.
            vp, vq, rad = a0*l, a0, l*l-1
            nc = F((k+2)*(l+1),2)
            assert vp*vp+vq*vq*rad+(2*a0-nc)*vp+a0*a0 == 0
            assert 2*vp*vq+(2*a0-nc)*vq == 0
            n_quadratics += 1
    counts['perturbation_threshold_quadratic_identities'] = n_quadratics
    print(json.dumps({'scope':'Two-logarithm lesson, derivative arithmetic and analytic comparison (7.37–7.48)',
                      'checks':counts,
                      'limits':'Finite exact checks supplement the analytic proofs. No geometric multiplicity estimate, full-rank theorem in general, final Gouillon theorem or 78500 radius bound certified here.'}))


if __name__ == '__main__':
    main()
