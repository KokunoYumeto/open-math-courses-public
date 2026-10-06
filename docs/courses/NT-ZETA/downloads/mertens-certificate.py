"""CC0. Certify a finite zero sum in the 1985 Mertens disproof.

The two exact decimal evaluation points are numerical facts from Table 3
of Odlyzko and te Riele, J. reine angew. Math. 357 (1985), p. 155.
This independently computes the zeros, derivatives, weights and sums with
python-flint / FLINT ball arithmetic. It computes no value of M(exp(y)).
Run: python mertens_certificate.py [output-directory]
"""
from pathlib import Path
import sys, json, time, hashlib
import flint
from flint import arb, acb, acb_series, ctx

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name('certificates') / 'Mertens'
out.mkdir(parents=True, exist_ok=True)
ctx.dps = 120
ctx.cap = 2
T = arb(2515)
points = {
    'positive': '-14045289680592998046790361630399781127400591999789738039965960762.521505',
    'negative': '32097025772922655869740000186211307099797144540349062682805321651.697419',
}
started = time.monotonic()
zeros = acb.zeta_zeros(1, 2000)
assert len(zeros) == 2000
assert zeros[1998].imag < T < zeros[1999].imag
ys = {key: arb(value) for key, value in points.items()}
sums = {key: arb(0) for key in points}
rows = []
previous = arb(0)
for j, rho in enumerate(zeros, 1):
    assert rho.real == arb('0.5') and rho.imag > previous
    previous = rho.imag
    derivative = acb_series([rho, acb(1)], 2).zeta()[1]
    assert derivative.abs_lower() > 0
    row = {
        'index': j,
        'ordinate': rho.imag.str(125),
        'zeta_derivative_real': derivative.real.str(125),
        'zeta_derivative_imag': derivative.imag.str(125),
    }
    if j < 2000:
        v = rho.imag / T
        weight = (1 - v) * v.cos_pi() + v.sin_pi() / arb.pi()
        assert weight >= 0
        coefficient = 1 / (rho * derivative)
        for key, y in ys.items():
            sums[key] += 2 * weight * (acb(0, rho.imag * y).exp() * coefficient).real
        row['weight'] = weight.str(125)
    rows.append(row)

assert sums['positive'] > arb('1.06')
assert sums['negative'] < arb('-1.009')
data = out / 'zero-balls.json'
data.write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')
receipt = {
    'license': 'CC0-1.0',
    'python_flint_version': flint.__version__,
    'decimal_precision': 120,
    'series_truncation': 2,
    'cutoff_exact': 2515,
    'positive_zeros_in_sum': 1999,
    'next_zero_index': 2000,
    'zero_enclosures_sorted_disjoint': True,
    'all_derivative_enclosures_exclude_zero': True,
    'points_exact_decimal': points,
    'sums_enclosed': {key: value.str(100) for key, value in sums.items()},
    'assertions': {'positive_exceeds_1_06': True, 'negative_below_minus_1_009': True},
    'zero_data_sha256': hashlib.sha256(data.read_bytes()).hexdigest(),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'elapsed_seconds': time.monotonic() - started,
    'scope': 'Finite ball-arithmetic spectral certificate; no direct M(x) counterexample is evaluated.',
}
(out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: receipt[k] for k in ['python_flint_version', 'cutoff_exact', 'positive_zeros_in_sum', 'sums_enclosed', 'assertions', 'elapsed_seconds']}, indent=2))
