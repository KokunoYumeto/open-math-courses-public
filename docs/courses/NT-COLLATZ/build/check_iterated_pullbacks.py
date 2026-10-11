"""Bounded exact regressions for iterated pullbacks, not infinite proofs."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from decimal import Decimal as D, localcontext, ROUND_CEILING
from math import isqrt
import json, random

ROOT = Path(__file__).resolve().parents[1]
counts = defaultdict(int)
diagnostics = defaultdict(int)

def step(n):
    return (3*n+1)//2 if n % 2 else n//2

def envelope(n, p=1, d=16):
    x = n
    for k in range(n.bit_length()):
        v = (x*(1 << k))**(2*d)
        if not 3**(k*d)*n**(2*(d-p)) <= v <= 3**(k*d)*n**(2*(d+p)):
            return False
        x = step(x)
    return True

# Enumerate complete source shells, not sampled parity words.
for M in range(2, 12):
    for q in range(1, M):
        Y = 1 << q
        if M > Y:
            continue
        fibres, odds = defaultdict(list), defaultdict(set)
        for n in range(1 << M, 1 << (M+1)):
            x, a, product = n, 0, F(1)
            for h in range(1, M+1):
                old = x
                x = step(x)
                if old % 2:
                    a += 1
                    product *= F(3*old, 3*old+1)
                if x <= Y:
                    assert old % 2 == 0 and Y//2 < x <= Y
                    assert a <= h-1
                    eps = F(h-1, 3*Y+4)
                    assert 1-product <= eps < F(1, 3)
                    assert F((1 << h)*x, 3**a)*product == n
                    fibres[h, x].append(n)
                    odds[h, x].add(a)
                    counts['exact_passages'] += 1
                    break
            counts['enumerated_sources'] += 1
        bounds = [1+(h-1)*((1 << (M+1))-1)//(3*Y+4) for h in range(1, M+1)]
        for (h, y), values in fibres.items():
            assert len(odds[h, y]) == 1
            assert len(values) <= bounds[h-1]
            counts['integer_fibres'] += 1
        band = list(range(Y//2+1, Y+1))
        if Y <= 16:
            targets = [{v for j, v in enumerate(band) if mask >> j & 1}
                       for mask in range(1 << len(band))]
        else:
            targets = [set(), set(band), set(band[::2]), {Y}]
        for target in targets:
            actual = sum(len(v) for (h, y), v in fibres.items() if y in target)
            assert actual <= len(target)*sum(bounds)
            # Restricting the source to odd starts never enlarges a fibre.
            restricted = sum(sum(n % 2 for n in v) for (h, y), v in fibres.items() if y in target)
            assert restricted <= actual
            counts['arbitrary_target_counts'] += 1

for M in range(2, 41):
    for q in range(1, M):
        Y = 1 << q
        if M > Y:
            continue
        integer = sum(1+(h-1)*((1 << (M+1))-1)//(3*Y+4) for h in range(1, M+1))
        precise = M+F((1 << M)*M*(M-1), 3*Y+4)
        uniform = F(5, 12)*M*M*F(1 << M, Y)
        assert integer <= precise <= uniform
        counts['time_sum_coefficients'] += 1
example = [1+(h-1)*127//52 for h in range(1, 7)]
assert example == [1, 3, 5, 8, 10, 13]
assert sum(example) == 40 and 6*max(example) == 78
assert F(5, 12)*36*4 == 60

# Exhaust all admissible checkpoint sets for a finite total stopped map.
mapping = {1:1, 2:2, 3:8, 4:6, 5:4, 6:2, 7:5, 8:1}
universe = set(mapping)
for mask in range(64):
    W = {1, 2} | {i+3 for i in range(6) if mask >> i & 1}
    S = W.copy()
    for R in range(6):
        direct = set()
        for n in universe:
            x, retained = n, True
            for i in range(R+1):
                retained &= x in W
                x = mapping[x]
            if retained:
                direct.add(n)
        assert direct == S and {1, 2} <= S
        next_S = W & {n for n in universe if mapping[n] in S}
        assert next_S <= S
        S = next_S
        counts['finite_set_recursions'] += 1

for n in [*range(1, 1025), 65536]:
    x = n
    for R in range(1, 6):
        x = isqrt(x) if x >= 16 else x
        assert x < 16 or x**(2**R) <= n
        counts['absorbing_power_checks'] += 1
x, example_path = 65536, [65536]
for _ in range(4):
    x = isqrt(x) if x >= 16 else x
    example_path.append(x)
assert example_path == [65536, 256, 16, 4, 4]
assert 4**16 > 65536

r, eta, M0 = F(15, 16), F(1, 16), 28
K = 1 << M0
assert 3**5 < 2**8  # a0 < 4/5, giving an exact startup certificate.
assert (r-F(4, 5)-eta)*M0 >= 2+eta and r*M0 >= 2
assert 2**(15*M0-16) >= M0**16
rng = random.Random(3711)
with localcontext() as ctx:
    ctx.prec = 90
    ell, ln3 = D(2).ln(), D(3).ln()
    lam, rr, et = ln3/ell, D(15)/16, D(1)/16
    a0, g = lam/2, 1-lam/2
    a, cr = (1+et-rr)/g, (1+rr)/g+1
    samples = [1, 3, 17, K-1]
    for M in [64, 128, 192, 256, 384, 512]:
        samples += [(1 << M)+rng.getrandbits(M) for _ in range(12)]
    for n in samples:
        x, path, checkpoints = n, [n], [n]
        h, odd, G = 0, 0, D(0)
        for R in range(1, 5):
            if x >= K and not envelope(x):
                break
            z = x
            if z >= K:
                m, q = z.bit_length()-1, 15*(z.bit_length()-1)//16
                Y = 1 << q
                block, block_odd = [z], 0
                while x > Y:
                    old = x
                    x = step(x)
                    block.append(x)
                    block_odd += old % 2
                    assert len(block)-1 <= m
                length = len(block)-1
                assert x**16 <= z**15
                assert max(block)**16 <= z**17
                assert 3**(32*block_odd) <= 3**(16*length)*z**2
                H = int(((D(17)/16*(D(z).ln()/ell)-q)/g).to_integral_value(rounding=ROUND_CEILING))
                # The logarithm proposes H; integer comparisons certify its meaning.
                assert 1 <= length <= H <= m
                assert 3**(16*H)*z**34 <= 2**(32*(H+q))
                assert 3**(16*(H-1))*z**34 > 2**(32*(H-1+q))
                path += block[1:]
                h += length
                odd += block_odd
                G += rr**(R-1)
                counts['controlled_blocks'] += 1
                counts['exact_shortened_horizons'] += 1
            else:
                assert x == z
                counts['zero_time_blocks'] += 1
            checkpoints.append(x)
            assert all(checkpoints[i+1] <= checkpoints[i] for i in range(len(checkpoints)-1))
            assert len(path)-1 == h
            assert 3**odd*n <= 2**h*x
            assert max(path)**16 <= n**17
            ordinary = [n]
            for old, new in zip(path, path[1:]):
                if old % 2:
                    ordinary.append(3*old+1)
                ordinary.append(new)
            assert len(ordinary)-1 == h+odd
            assert max(ordinary)**16 <= 2**16*n**17
            nu = next((i for i in range(R) if checkpoints[i] < K), R)
            logn, logx = D(n).ln(), D(x).ln()
            assert D(h) <= G*logn/ell + D('1e-70')
            assert D(h) <= a*G*logn/ell+nu*cr+D('1e-70')
            assert D(odd) <= D(h)/2+et*G*logn/ln3+D('1e-70')
            assert D(odd) <= (D(h)+(logx-logn)/ell)/lam+D('1e-70')
            assert x < K or logx <= rr**R*logn+D('1e-70')
            diagnostics['global_clock_and_power_comparisons'] += 1
            if n % 2:
                y = n
                for _ in range(odd):
                    y = 3*y+1
                    while y % 2 == 0:
                        y //= 2
                odd_part = x
                while odd_part % 2 == 0:
                    odd_part //= 2
                assert y == odd_part
                counts['exact_odd_return_endpoints'] += 1
            if x < K or envelope(x):
                counts['retained_prefixes'] += 1
            counts['actual_prefixes'] += 1

    # Check the explicit constant recursion independently of sampled paths.
    t = et/lam
    b = (D('0.5')+t)*(1+2*t).ln()+(D('0.5')-t)*(1-2*t).ln()
    DD, v, Cstar, kap = b/ell, ell*rr/2, D(100), D(5)/12
    A0 = Cstar*(1+ell).sqrt()/(1-b.exp()/2)**2
    Q = 1/(1+(-(1-rr*DD)*ell).exp()*(-1))
    F0 = kap*(DD*ell).exp()/v.sqrt()
    Lstar = 1+Q*(Cstar+F0)
    AA = A0
    for R in range(11):
        power = D(2*R)-D('0.5')
        assert AA+1 <= (A0+1)*Lstar**R*ell**(-D(R*R)-D(R)/2)+D('1e-60')
        dd = DD*rr**R
        ZZ = v**min(power,D(0))
        AA = ell**(-power-2)*(Cstar+kap*(dd*ell).exp()*ZZ*AA)/(1+(-(1-rr*dd)*ell).exp()*(-1))
        diagnostics['depth_constant_majorants'] += 1
    for M in range(M0, 201):
        Y = 2**(15*M//16)
        value = 1+D(Y).ln()
        assert v*(1+M) <= value <= 1+M
        for p in [D('-.5'),D('1.5'),D('5.5')]:
            assert value**p <= v**min(p,D(0))*D(1+M)**p
            diagnostics['logarithmic_power_comparisons'] += 1

assert counts['controlled_blocks'] > 0 and counts['retained_prefixes'] > 0
out = dict(passed=True, counts=dict(counts),
    scopes=dict(exhaustive_source_shell_ranks=[2,11],uniform_coefficient_ranks=[2,40],
                finite_total_map_points=8,all_admissible_checkpoint_sets=64,
                actual_orbits="72 seeded inputs of ranks64–512 plus four startup inputs; at most four blocks each"),
    exact_scope="Integer and rational first-passage fibres, product defects, arbitrary-target counts, time-summed coefficients, finite-set recursion, absorbing branches, integer-power envelopes, shortened horizons and exact clock expansion. Bounded checks, not infinite proofs.",
    diagnostics=dict(precision_digits=90,counts=dict(diagnostics),scope="Logarithmic global bounds and recurrence magnitudes are numerical diagnostics, not formal certificates."),
    exercise_values=dict(time_bounds=example,time_sum=40,longest_bound_repeated=78,uniform_bound=60,absorbing_path=example_path),
    formal_status="No Lean replay or independent certificate.")
(ROOT/'checks/iterated_pullbacks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
