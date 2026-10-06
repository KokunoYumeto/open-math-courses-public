"""Original CC0 teaching figure. GPT-6.1 Sol, Codex, Ultra, October 2026."""
from pathlib import Path
import hashlib
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 60
eta = d = mp.mpf('0.01')
sigma = mp.mpf('0.75')

def exponent(center):
    center = mp.mpf(center)
    return mp.log((center-sigma)/(center-1-eta))/mp.log((center-mp.mpf('0.5')-d)/(center-1-eta))

samples = [{'center': str(a), 'lambda': str(exponent(a))} for a in (3, 10, 100, 1000)]
centers = np.geomspace(3, 1000, 300)
values = np.log((centers-.75)/(centers-1.01))/np.log((centers-.51)/(centers-1.01))
check = max(abs(float(exponent(a))-v) for a, v in zip(centers[::30], values[::30]))
assert check < 1e-11
plt.rcParams.update({'font.size': 14, 'axes.titlesize': 18, 'axes.labelsize': 15})
fig, ax = plt.subplots(1, 2, figsize=(14.4, 6.8), gridspec_kw={'width_ratios': [1.05, 1]})
left, right = ax
center = 3
for radius, color, label, fill, style in [
    (2.49, '#d7e8f5', r'$r_2=2.49$: $|\log\zeta|\ll\log t$', True, '-'),
    (1.99, '#cde9da', r'$r_1=1.99$: $|\log\zeta|\ll1$', True, '-'),
    (2.25, '#894cb2', r'$r=2.25$: target $\sigma=3/4$', False, '--'),
]:
    left.add_patch(Circle((center, 0), radius, facecolor=color if fill else 'none',
                          edgecolor='#346887' if fill and radius==2.49 else '#39734f' if fill else color,
                          linewidth=2.2, linestyle=style, label=label))
left.plot([center], [0], 'o', color='#202934')
left.annotate(r'center $3+it$', (center, 0), xytext=(3.14, .2))
left.plot([.75], [0], 'o', color='#894cb2', markersize=8)
left.annotate(r'$3/4+it$', (.75, 0), xytext=(.83, -.52),
              arrowprops={'arrowstyle': '-', 'color': '#894cb2'}, color='#66348b')
left.axvline(.5, color='#6d7580', linestyle=':', linewidth=1.3)
left.axhline(0, color='#6d7580', linewidth=.8)
left.set_xlim(.28, 5.7)
left.set_ylim(-2.65, 2.65)
left.set_aspect('equal')
left.set_xlabel('Real part of s')
left.set_ylabel('Imaginary part of s minus t')
left.set_title('The three disks, with center 3')
left.legend(loc='upper center', bbox_to_anchor=(.5, -.18), fontsize=12, frameon=False)
right.plot(centers, values, color='#894cb2', linewidth=2.6)
right.axhline(.52, color='#39734f', linestyle='--', linewidth=1.7,
              label=r'limiting exponent $0.52$ for $\eta=d=0.01$')
for a in (3, 10, 100, 1000):
    right.plot(a, float(exponent(a)), 'o', color='#894cb2')
right.annotate(r'$\lambda(100)=0.5206287\ldots$', (100, float(exponent(100))),
               xytext=(18, .539), arrowprops={'arrowstyle':'->', 'color':'#66348b'}, fontsize=13)
right.set_xscale('log')
right.set_ylim(.516, .553)
right.set_xlim(2.8, 1100)
right.set_xlabel('Real part A of the disk center')
right.set_ylabel(r'Three-circles exponent $\lambda(A)$')
right.set_title('Moving the center improves the exponent')
right.grid(alpha=.25)
right.legend(loc='upper center', bbox_to_anchor=(.5, -.18), fontsize=12, frameon=False)
fig.subplots_adjust(left=.065, right=.985, top=.9, bottom=.27, wspace=.28)
out = ROOT/'three_circles.png'
fig.savefig(out, dpi=150, facecolor='white')
plt.close(fig)
receipt = {
    'authorship': 'Original CC0 figure and calculation, GPT-6.1 Sol in Codex, Ultra',
    'parameters': {'eta':'0.01', 'd':'0.01', 'sigma':'0.75'},
    'left_geometry': {'center':3, 'r1':1.99, 'r':2.25, 'r2':2.49},
    'samples': samples,
    'limit':str((1+eta-sigma)/(mp.mpf('0.5')+eta-d)),
    'floating_sample_difference_from_60_digits':check,
    'note':'Numerical formula values illustrate the exact proved interpolation exponent; no zeta zero computation or proof by numerical sampling is claimed.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'figure_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'versions':{'numpy':np.__version__, 'mpmath':mp.__version__, 'matplotlib':matplotlib.__version__},
}
(ROOT/'three_circles_calculation.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'samples':samples,'max_difference':check,'figure_sha256':receipt['figure_sha256']},indent=2))
