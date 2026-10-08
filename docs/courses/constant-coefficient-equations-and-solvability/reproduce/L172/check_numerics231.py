"""Supplementary exact geometry, complex transpose and scaled-jet checks."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import mpmath as mp

OWN = Path(__file__).resolve().parent
mp.mp.dps = 65
counts = {}
maximum = mp.mpf(0)


def test(kind, condition):
    assert condition, kind
    counts[kind] = counts.get(kind, 0)+1


def equal(kind, left, right):
    global maximum
    error = abs(left-right)
    maximum = max(maximum, error)
    test(kind, error < mp.mpf("1e-61"))


test("singular_sampling_interval",
     (F(-2,3)-F(1,3), F(4,3)-F(1,3)) == (-1,1))
test("remote_tail_sampling_band",
     (0-F(13,4), 0-F(11,4)) == (F(-13,4), F(-11,4)))
test("tail_disjoint_from_solution_domain", -F(11,4)<-1)
test("cutoff_tail_translation", F(3)-F(1,3)==F(8,3))
test("cutoff_singular_distances",
     min(F(-1,3)+F(4,3), F(2,3)+F(1,3)) == 1)
test("complex_point_solution_location", F(3,5)+F(2,5)==1)
test("two_atom_distance_identity",
     min(F(0)+F(1,2), 1-F(1,2))
     == min(-F(1,4)+F(3,4), F(3,4)-F(1,4)) == F(1,2))
test("nonconvex_hull_trim", F(-2)-(-3)==(-1)-F(-2)==1
     and F(2)-1==3-F(2)==1)
for j in range(1, 129):
    gap = F(1, 2**j)
    x = 1-gap
    test("escaping_point_distances",
         min(x+1,1-x)==gap and min(x+2,2-x)==1+gap)
    test("locally_finite_monotone_points", F(1,2)<=x<1)
    epsilon = gap/8
    test("isolated_test_support",
         x-epsilon>0 and x+epsilon<1 and epsilon<gap/2)
for j in range(1, 65):
    x = 2-F(1,3**j)
    test("second_increasing_order_family", F(5,3)<=x<2 and 2*j>=2)
for m in range(1, 25):
    for n in [0, m//2, m-1]:
        eps = F(1, 2**(m+3))
        test("scaled_jet_exponents",
             eps**(m-n) > 0 and m-n>0 and eps**(m+1)<eps**(m-n))
    eta = lambda t:t**m/mp.factorial(m)
    for eps in [mp.mpf(".1"), mp.mpf(".01")]:
        equal("exact_top_order_scaled_jet",
              mp.diff(lambda t:eps**m*eta(t/eps), 0, m), 1)
for k in range(-8, 9):
    x = mp.mpf(k)/7
    a = mp.mpf(-2)/5
    for degree in range(1, 7):
        theta = lambda t:(1+mp.mpc(".2",".4")*t)**degree
        kernel = [(F(-2,5), mp.mpc(0,1)), (F(1,3), mp.mpc(2,-1))]
        datum_atoms = [(F(k,7), mp.mpc(1,-1)),
                       (F(k,7)+F(3,10), mp.mpf("-.5"))]
        number = lambda q:mp.mpf(q.numerator)/q.denominator
        forward = sum(weight*sum(coefficient*theta(number(point-offset))
                                for offset,coefficient in kernel)
                      for point,weight in datum_atoms)
        reflected_image = {}
        for point,weight in datum_atoms:
            for offset,coefficient in kernel:
                location=point-offset
                reflected_image[location]=reflected_image.get(location,0)+weight*coefficient
        backward = sum(weight*theta(number(point))
                       for point,weight in reflected_image.items())
        equal("bilinear_complex_transpose", forward, backward)
        wrong = sum(weight*sum(mp.conj(coefficient)*theta(number(point-offset))
                              for offset,coefficient in kernel)
                    for point,weight in datum_atoms)
        test("conjugated_transpose_is_different", abs(forward-wrong)>mp.mpf("1e-20"))
        datum = lambda t:mp.exp(mp.mpc(".3",".8")*t)
        u = lambda y:datum(y+a)/1j
        equal("complex_translated_solution", 1j*u(x-a), datum(x))
for s in [mp.mpf(k)/16 for k in range(16)]:
    image=s-mp.mpf(1)/4
    test("swept_compact_boundary_gap",
         -mp.mpf(1)/4<=image<mp.mpf(3)/4
         and min(image+mp.mpf(3)/2,mp.mpf(3)/2-image)>=mp.mpf(3)/4)

report = {"status": "PASS", "probe_count": sum(counts.values()),
          "probe_kinds": counts, "decimal_precision": 65,
          "largest_numerical_identity_error": str(maximum),
          "exact_rational_geometry_and_scaling": True,
          "proof_replacement": False,
          "source_code_sha256": hashlib.sha256(
              Path(__file__).read_bytes()).hexdigest().upper()}
(OWN / "supplementary-example-probes231.json").write_text(
    json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps(report))
