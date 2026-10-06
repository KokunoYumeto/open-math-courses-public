"""Exact finite checks supplementing the degree-capacity and parameter proofs."""
from fractions import Fraction as F
from math import comb
import json


def constants(m):
    if m == 1:
        n = 48
        c = F(4*49**2, 3)
    else:
        n = 4*(m+1)**3
        c = F(60*m*(m+1)*(n+1)**(m+1), 3**m)
    return n, c


def weight_groups(d, q, k):
    # The multiplicity of total transverse degree h is stars and bars.
    for h in range(q+1):
        number = 1 if d == 1 and h == 0 else (
            0 if d == 1 else comb(h+d-2, d-2))
        for _ in range(number):
            yield h, k*(q-h+1)


def check():
    from laurent_constant import Interval, E
    assert Interval(3).log().lo > F(109,100)
    assert Interval(3).log().hi < F(11,10)
    assert Interval(60).log().hi < F(41,10)
    assert Interval(F(109,27)).log().hi < F(14,10)
    assert Interval(29).log().hi < F(34,10)
    assert Interval(337).log().hi < 7
    assert (E**3).hi < 21
    assert Interval(2).sqrt().lo > F(14,10)
    # The exceptional one-logarithm size margin.
    n1,c1 = constants(1)
    exceptional_size = (2*Interval(c1).log()
                        +Interval(F(200,n1)).log()-2+6)
    assert exceptional_size.hi < 22
    parameter_examples = 0
    for m in [1,4,9]:
        root = {1:1,4:2,9:3}[m]
        n,c = constants(m)
        for degree,radius_log in [(1,1),(2,1),(19,1),(2,14)]:
            y = F(degree,radius_log)
            eq = max(F(1),1/y,y)
            for r in [F(1),F(5)]:
                eb = max(eq,r)
                b1 = 37*m*root*eb
                b2 = 10*root*eq
                prod = r**m
                u = c*degree*y*b1*b2*prod
                x = u/(degree*b1)
                t0 = (x/2).__floor__()
                t1 = (n*y*b1).__floor__()
                s0 = (u/(degree*b2)).__floor__()
                h = (b1/(6*m)).__floor__()
                a = F(radius_log,degree)*r
                sj = (u/(degree*(t1+1)*a)).__floor__()
                assert min(t0,t1,s0,h,sj) > 0
                assert 4*sj < t0 and s0+1 >= 2*t0
                sstar = 2*(m+1)*m*sj
                assert (Interval(t0*sstar).log()+h*Interval(3).log()).hi < b1
                assert (2+Interval(1+F(t1,h)).log()).hi < b2
                lm = comb(t0+m,m)*(2*t1+1)
                budget = (4*degree*t0*b1+2*(m+1)*degree*s0*b2
                          +degree*h+(m+1)*u
                          +2*(m+1)*degree*(t1+1)*m*sj*a)
                assert (budget+degree*Interval(2*lm).log()).hi <= F(t0*(2*t1+1)*radius_log,m+2)
                parameter_examples += 1
    capacity_checks = 0
    for d in range(1, 7):
        for q in range(1, 9):
            groups = list(weight_groups(d, q, 3))
            rs = [c//3 for _,c in groups]
            n = comb(q+d,d)
            assert sum(rs) == n
            assert F(sum(r*r for r in rs),n) == 1+F(2*q,d+1)
            assert F(sum(r**3 for r in rs),n) == 1+F(6*q*(q+d+1),(d+1)*(d+2))
            for k in [3,5,9,17]:
                weights = sorted(w for h,c in weight_groups(d,q,k)
                                 for w in range(h,h+c))
                size = k*n
                assert len(weights) == size
                cut = F(k*(q+1),2)
                cut2 = k*(q+1)
                trimmed2 = sum(min(2*w,cut2) for w in weights)
                assert F(trimmed2,2) > F(size*k*q,d+2)
                # Exact minimization of every possible number of analytic columns.
                prefix = 0
                minimum2 = size*cut2
                for ell in range(size+1):
                    if ell:
                        prefix += weights[ell-1]
                    minimum2 = min(minimum2,2*prefix+(size-ell)*cut2)
                assert minimum2 == trimmed2
                capacity_checks += 1
    constant_checks = []
    for m in range(1,101):
        n,c = constants(m)
        cost = F(370*m*m*(2*n+1),4)*(c+2)+1
        target = 2**(m+25)*m**(3*m+9)
        assert cost < target
        assert c >= 100*(m+1)
        assert 10*c >= 4*n+2
        # Uniform budget, after replacing the two lower-order terms by U.
        assert F(49*(2*n-1),100*(m+2)) > 2*m*m+5*m+6
        if m <= 12:
            constant_checks.append({"m":m,"ratio":float(cost/target),
                                    "exact_ratio":str(cost/target)})
    # The infinite-tail majorant uses only rational arithmetic here.
    tail = F(546,100000)*21*F(5,4)**7*4*F(27,40)**4
    assert tail < F(46,100)
    example_weights = sorted(w for h,c in weight_groups(2,3,5)
                             for w in range(h,h+c))
    example_trimmed = sum(min(F(w),F(10)) for w in example_weights)
    return {
        "status":"passed",
        "capacity_instances":capacity_checks,
        "moment_scope":"d1..6,q1..8",
        "trim_scope":"k3,5,9,17; every analytic-column count",
        "constant_prefix_scope":"m1..100; independent analytic tail in lesson",
        "rational_interval_margins":"128-bit outward rational intervals, including all stated elementary logarithm/exp margins",
        "parameter_examples":parameter_examples,
        "parameter_example_scope":"m1,4,9; D,v=(1,1),(2,1),(19,1),(2,14); rj=1 or5; exact rounding and complete finite budget",
        "constant_ratios":constant_checks,
        "tail_majorant":str(tail),
        "figure_example":{"d":2,"T0":3,"k":5,"rows":len(example_weights),
                          "threshold":10,"trimmed_sum":str(example_trimmed),
                          "trimmed_mean":str(example_trimmed/len(example_weights)),
                          "proved_lower_mean":"15/4"},
        "limits":"Finite checks supplement the full general capacity, concentration and infinite parameter proofs; no homogeneous/dependent or Matveev completion claim.",
    }


if __name__ == "__main__":
    print(json.dumps(check(),indent=2))
