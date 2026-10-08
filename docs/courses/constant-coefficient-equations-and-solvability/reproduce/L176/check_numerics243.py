"""Supplementary finite checks of the exact examples; none replace a proof."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import argparse, hashlib, json
import mpmath as mp

mp.mp.dps = 65
counts = Counter()
maximum = mp.mpf(0)

def check(group, left, right, tolerance=mp.mpf("1e-55")):
    global maximum
    error = abs(left-right)/(1+abs(left)+abs(right))
    maximum = max(maximum, error)
    assert error < tolerance, (group, str(left), str(right), str(error))
    counts[group] += 1

def require(group, assertion):
    assert assertion, group
    counts[group] += 1

def cutoff(x, plateau=mp.mpf(1)):
    """C-infinity cutoff and two exact derivatives; transition ends at radius 2."""
    x = mp.mpf(x)
    radius = abs(x)
    if radius <= plateau:
        return mp.mpf(1), mp.mpf(0), mp.mpf(0)
    if radius >= 2:
        return mp.mpf(0), mp.mpf(0), mp.mpf(0)
    width = 2-plateau
    s = (radius-plateau)/width
    odds = -1/s+1/(1-s)
    c = 1/(1+mp.exp(odds))
    first = 1/s**2+1/(1-s)**2
    second = -2/s**3+2/(1-s)**3
    cs = -c*(1-c)*first
    css = c*(1-c)*((1-2*c)*first**2-second)
    return c, mp.sign(x)*cs/width, css/width**2

def green(x):
    return mp.exp(-abs(x))/2

def pv_transform(frequency):
    """Independent finite principal-value integral, after removing its pole."""
    frequency = abs(mp.mpf(frequency))
    center = mp.cos(frequency)
    def regular(x):
        if x == 1:
            return frequency*mp.sin(frequency)/2
        c = cutoff(x, mp.mpf("1.5"))[0]
        return (c*mp.cos(frequency*x)-center)/(1-x*x)
    return 2*mp.quad(regular, [0, mp.mpf(".5"), 1, mp.mpf("1.5"),
                               mp.mpf("1.75"), 2])+center*mp.log(3)

def removed_tail_transform(frequency):
    """Separate smooth-tail integral, with its infinite tail evaluated by Ci/Si."""
    frequency = abs(mp.mpf(frequency))
    transition = mp.quad(
        lambda x: (1-cutoff(x, mp.mpf("1.5"))[0])*mp.cos(frequency*x)/(1-x*x),
        [mp.mpf("1.5"), mp.mpf("1.75"), 2])
    if frequency == 0:
        tail = -mp.log(3)/2
    else:
        def shifted_tail(a):
            return (-mp.cos(frequency*a)*mp.ci(frequency*(2-a))
                    -mp.sin(frequency*a)*(mp.pi/2-mp.si(frequency*(2-a))))
        tail = (-shifted_tail(1)+shifted_tail(-1))/2
    return 2*(transition+tail)

def run():
    for j in range(-100, 101):
        z = (2*j+1)*mp.pi-mp.j*mp.log(2)
        transform = mp.exp(mp.j*z/2)+2*mp.exp(-mp.j*z/2)
        check("exact_escaping_complex_zeros", transform, 0)
        coefficient = Fraction(-2)**(j+1)+2*Fraction(-2)**j
        require("bilateral_comb_exact_fraction_cancellation", coefficient == 0)
    for j in range(100):
        radius = mp.sqrt(((2*j+1)*mp.pi)**2+mp.log(2)**2)
        next_radius = mp.sqrt(((2*j+3)*mp.pi)**2+mp.log(2)**2)
        require("sampled_fixed_height_ratio_decreases",
                mp.log(2)/mp.log(next_radius) < mp.log(2)/mp.log(radius))
    for t in range(1, 61):
        z1 = mp.mpf(t)
        z2 = mp.j*mp.sqrt(1+t*t)
        check("exact_elliptic_zero_branch", 1+z1*z1+z2*z2, 0)
        check("exact_elliptic_branch_norm", abs(z1)**2+abs(z2)**2, 1+2*t*t)
    for real in ("-3", "-1", "0", "1", "3"):
        for imaginary in ("-.4", "0", ".4"):
            z = mp.mpc(real, imaginary)
            # Worst decay rate is0.6; the omitted300-to-infinity tail is<1e-77.
            # Finite ten-unit intervals prevent inaccurate infinite oscillatory quadrature.
            intervals = list(range(0, 301, 10))
            integral = mp.quad(lambda x: mp.exp(-(1+mp.j*z)*x)/2, intervals)
            integral += mp.quad(lambda x: mp.exp(-(1-mp.j*z)*x)/2, intervals)
            check("green_function_independent_half_line_integrals",
                  integral, 1/(1+z*z))
            a = mp.mpf(3)/5
            symbol = mp.j*(1+z*z)*mp.exp(-mp.j*a*z)
            inverse = -mp.j*mp.exp(mp.j*a*z)*integral
            check("complex_bilinear_translated_inverse", symbol*inverse, 1)
            require("wrong_conjugation_sign_rejected", abs(-symbol*inverse-1)>1)
    for alpha in (mp.mpf(".5"), mp.mpf(1), mp.mpf(2)):
        for beta in (mp.mpf(-2), mp.mpf(0), mp.mpf(3)):
            def phi(x):
                return mp.exp(-alpha*x*x+mp.j*beta*x)
            def second_phi(x):
                return ((-2*alpha*x+mp.j*beta)**2-2*alpha)*phi(x)
            left = mp.quad(lambda x: cutoff(x)[0]*green(x)*(phi(x)-second_phi(x)),
                           [-2, -1, 0, 1, 2])
            def residual(x):
                c, cp, cpp = cutoff(x)
                return (-cpp+2*mp.sign(x)*cp)*green(x)*phi(x)
            right = phi(0)+mp.quad(residual, [-2, -1, 0, 1, 2])
            check("compact_parametrix_distributional_test_identity", left, right)
    for f in ("0", ".25", ".75", "1", "2", "3", "5", "8", "12", "20"):
        frequency = mp.mpf(f)
        principal = pv_transform(frequency)
        tail = removed_tail_transform(frequency)
        check("principal_value_and_independent_smooth_tail",
              principal+tail, mp.pi*mp.sin(frequency))
        minus = principal+mp.j*mp.pi*mp.cos(frequency)
        plus = principal-mp.j*mp.pi*mp.cos(frequency)
        check("two_point_compact_parametrix_exact_product",
              minus*plus/mp.pi**2,
              1+(tail**2-2*mp.pi*tail*mp.sin(frequency))/mp.pi**2)
        check("boundary_value_translation_and_delta_sign",
              minus+tail, mp.j*mp.pi*mp.exp(-mp.j*frequency))
    for dimension in (1, 2, 3):
        for index in range(1, 41):
            xi = [mp.mpf(index-j)/7 for j in range(dimension)]
            theta = [mp.mpf(j+1) for j in range(dimension)]
            norm = mp.sqrt(sum(v*v for v in theta))
            theta = [v/norm for v in theta]
            t = mp.mpf(index)/13
            gradient = [2*v/(2+sum(w*w for w in xi)) for v in xi]
            matrix = mp.matrix(dimension)
            for a in range(dimension):
                for b in range(dimension):
                    matrix[a,b] = int(a==b)+mp.j*t*theta[a]*gradient[b]
            expected = 1+mp.j*t*sum(theta[j]*gradient[j] for j in range(dimension))
            check("complex_rank_one_graph_jacobian", mp.det(matrix), expected)
            require("graph_jacobian_uniform_bound", abs(expected)<=1+t)
    for index in range(1, 61):
        radius = mp.mpf(index)/122
        for angle in (mp.mpf(0), mp.pi/3, mp.pi):
            kernel_ratio = (1-radius**2)/abs(mp.exp(mp.j*angle)-radius)**2
            require("poisson_center_comparison_kernel",
                    kernel_ratio >= mp.mpf(1)/4**2)
    for radius in (mp.mpf(0), mp.mpf(".25"), mp.mpf(".5")):
        total = mp.quad(lambda angle:
            (1-radius**2)/abs(mp.exp(mp.j*angle)-radius)**2/(2*mp.pi),
            [0, mp.pi, 2*mp.pi])
        check("poisson_kernel_normalization", total, 1)
    require("strict_derivative_budget", mp.mpf(4)/5*16 > 4+5+3)
    for j in range(1, 61):
        c = mp.exp(mp.mpf(j+5)/3)
        m = mp.mpf(7)
        z = c-mp.j*m*mp.log(c)/2
        inverse_modulus = abs(mp.exp(2*mp.j*z))
        check("reflected_translation_exponential", inverse_modulus, c**m)
        require("actual_translation_point_inside_logarithmic_strip",
                abs(z.imag) < m*mp.log(abs(z)))
    return dict(
        status="PASS", precision_decimal_digits=mp.mp.dps,
        total_checks=sum(counts.values()), grouped_checks=dict(counts),
        maximum_scaled_identity_error=str(maximum),
        identity_tolerance="1e-55",
        numerical_checks_are_proofs=False,
        scope="Finite exact Fraction cancellations, independent distributional and Fourier integrals, complex zeros, reciprocal signs, contour determinants and harmonic kernel checks.",
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    if args.output:
        assert args.output.resolve().parent == Path(__file__).resolve().parent
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result), flush=True)
