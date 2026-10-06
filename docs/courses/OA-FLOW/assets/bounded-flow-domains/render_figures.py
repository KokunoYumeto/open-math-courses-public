"""Bounded perturbations and flow domains: three revised OA-FLOW figures.

Original renderer: OA-FLOW course project contributors, 2026 (MIT).
Figures and diagnostic annotations: GFDL-1.2-or-later. See ASSET_TERMS.md. Run with Python; no TeX, browser, or source image.

Every output is confined to the explicit --output directory. Matplotlib MathText is internal,
not a TeX subprocess. Fixed SVG IDs and omitted dates make output reproducible.
"""
from pathlib import Path
import os
import json
import hashlib
import math
import argparse
import re

parser = argparse.ArgumentParser(description='Reproduce three original derivation-domain figures; requires matplotlib 3.10.9 and numpy 2.4.4 for the recorded bytes.')
parser.add_argument('--output', type=Path, required=True, help='Dedicated output directory; do not use the distributed assets directory.')
args = parser.parse_args()
HERE = args.output.resolve()
HERE.mkdir(parents=True, exist_ok=True)
os.environ['MPLCONFIGDIR'] = str(HERE / 'runtime-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.text import Text
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 15,
    'mathtext.fontset': 'dejavusans', 'text.usetex': False,
    'svg.fonttype': 'path', 'svg.hashsalt': 'OA-FLOW-BP-20261006-v1',
    'axes.spines.top': False, 'axes.spines.right': False,
})
INK = '#162b3c'
BLUE = '#155e96'
GREEN = '#087a64'
RED = '#a73535'
GRAY = '#4b5b67'
PALE = '#f1f5f8'
LINE = '#c5d0d8'
ARTIFACTS = []
LAYOUT = []


def page(title, subtitle, size=(14, 13.8)):
    fig = plt.figure(figsize=size, dpi=160, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')
    put(ax, .055, .965, title, 25, weight='bold')
    put(ax, .055, .932, subtitle, 14, color=GRAY)
    return fig, ax


def put(ax, x, y, text, size=17, color=INK, weight='normal', ha='left', va='center', **kw):
    return ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
                   ha=ha, va=va, transform=ax.transAxes, **kw)


def line(ax, x0, y0, x1, y1, color=LINE, lw=1.2, **kw):
    ax.plot([x0, x1], [y0, y1], color=color, lw=lw, transform=ax.transAxes, **kw)


def arrow(ax, x0, y0, x1, y1, color=BLUE, style='-|>', mutation=18, **kw):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), transform=ax.transAxes,
        arrowstyle=style, mutation_scale=mutation, linewidth=1.8, color=color, **kw))


def box(ax, x, y, w, h, edge=LINE, face=PALE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, transform=ax.transAxes,
         boxstyle='round,pad=0.008,rounding_size=0.008', facecolor=face,
         edgecolor=edge, linewidth=1.1))


def band(ax, y, label):
    put(ax, .055, y, label, 17, weight='bold', color=BLUE)


def footer(ax, lines):
    line(ax, .055, .103, .945, .103)
    for j, s in enumerate(lines):
        put(ax, .055, .082 - j * .023, s, 11.7, color=GRAY)


def finish(fig, stem):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    text_checks = []
    for txt in fig.findobj(Text):
        if not txt.get_visible() or not txt.get_text():
            continue
        bounds = txt.get_window_extent(renderer).bounds
        x, y, w, h = bounds
        inside = x >= 0 and y >= 0 and x+w <= fig.bbox.width and y+h <= fig.bbox.height
        text_checks.append({'text': txt.get_text(), 'bbox_px': [round(v, 3) for v in bounds], 'inside_canvas': bool(inside)})
    assert all(x['inside_canvas'] for x in text_checks), [x for x in text_checks if not x['inside_canvas']]
    for ext in ('svg', 'png'):
        p = HERE / (stem + '.' + ext)
        kwargs = {'metadata': {'Date': None, 'Creator': 'OA-FLOW original mathematical illustration'}} if ext == 'svg' else {'metadata': {'Software': 'OA-FLOW original mathematical illustration'}}
        fig.savefig(p, format=ext, dpi=160, facecolor='white', **kwargs)
        if ext == 'svg':
            p.write_bytes(re.sub(br'<!DOCTYPE svg PUBLIC[^>]*>\r?\n', b'', p.read_bytes(), count=1))
        ARTIFACTS.append({'path': p.name, 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    LAYOUT.append({'figure': stem, 'canvas_px': list(fig.canvas.get_width_height()), 'text_checks': text_checks})
    plt.close(fig)


# Figure 1. Arrows represent the maps proved in Sections 2 and 3.
fig, ax = page('A bounded velocity changes the first derivative by a commutator',
              'Real time; arbitrary von Neumann algebra M; point-ultraweakly continuous action alpha.')
band(ax, .889, '1   Solve the equation with the velocity on the right')
put(ax, .065, .846, r'$a^*=-a,\quad a\in M;\qquad c(t)=\alpha_t(a),\qquad u_t\in\mathcal{U}(M)$', 20)
put(ax, .065, .798, r"$u'_t=u_t\alpha_t(a),\qquad u_0=1,\qquad \|u_t-u_s\|\leq\|a\|\,|t-s|$", 21, color=BLUE)
put(ax, .065, .754, r'$V_0(t)=1,\qquad V_n(t)=\int_0^t V_{n-1}(s)c(s)\,ds,\qquad u_t=\sum_{n\geq0}V_n(t)$', 18)
put(ax, .065, .709, r'$t>0:\quad 0\leq t_3\leq t_2\leq t_1\leq t\qquad\longmapsto\qquad c(t_3)c(t_2)c(t_1)$', 19)
put(ax, .065, .676, 'Positive-time ordering: the earliest coefficient is the leftmost factor.', 14)
put(ax, .065, .646, r'For $t<0$, keep the oriented integrals.  Bound: $\|V_n(t)\|\leq\|a\|^n|t|^n/n!$.', 14)
line(ax, .055, .617, .945, .617)

band(ax, .586, '2   Uniqueness of the shifted equation gives the cocycle')
put(ax, .065, .545, r'$u_{s+t}=u_s\alpha_s(u_t)\qquad(s,t\in\mathbb{R})$', 23, color=GREEN)
put(ax, .20, .470, r'$x\in M$', 22, ha='center')
put(ax, .72, .491, r'$\alpha_t(x)\in M$', 22, ha='center')
put(ax, .72, .393, r'$\beta_t(x)\in M$', 22, ha='center')
arrow(ax, .295, .479, .593, .491)
put(ax, .438, .508, r'$\alpha_t:M\to M$', 15, ha='center', color=BLUE)
arrow(ax, .286, .452, .593, .393, color=GREEN)
put(ax, .436, .393, r'$\beta_t:M\to M$', 15, ha='center', color=GREEN)
arrow(ax, .72, .463, .72, .422, color=GRAY)
put(ax, .773, .444, r'$y\mapsto u_tyu_t^*$', 16, color=GRAY)
put(ax, .065, .346, r'$\beta_t=\operatorname{Ad}(u_t)\circ\alpha_t,\qquad \alpha_t(x)=u_t^*\beta_t(x)u_t$', 19)
line(ax, .055, .316, .945, .316)

band(ax, .286, '3   Differentiate at zero, in the sigma-strong-star topology')
put(ax, .065, .244, r'$u_t\alpha_t(x)u_t^*\quad\longmapsto\quad ax+\delta_\alpha x-xa$', 22)
box(ax, .057, .151, .882, .058, edge=GREEN, face='#edf7f3')
put(ax, .50, .181, r'$D_\beta=D_\alpha,\qquad \delta_\beta x=\delta_\alpha x+[a,x]\quad(x\in D_\alpha)$', 22, color=GREEN, ha='center')
put(ax, .065, .124, r'Extra hypothesis for every derivative: $a\in M_\alpha^\infty\ \Longrightarrow\ M_\beta^\infty=M_\alpha^\infty$.', 15)
footer(ax, [
    'Proof: OA-FLOW-BP, Sections 2–3: oa-flow.bp.evolution and oa-flow.bp.perturbation.',
    'Antecedent: M. Takesaki, Theory of Operator Algebras II, Chapter XI, §3. Original diagram.',
    'The triangle arrows are maps M to M. All-time smoothness uses the additional hypothesis in Section 4.',
])
finish(fig, '34-cocycle-and-common-domain')


# Figure 2. The matrix corner fixes the sign and normalization unambiguously.
fig, ax = page('The first derivative exists; a second derivative is obstructed',
              r'Exact counterexample on $B(\ell^2(\mathbb{N}_0))$. These are domain statements, not numerical tests.')
band(ax, .888, '1   Couple a fixed vector to a vector outside the generator domain')
put(ax, .065, .846, r'$He_n=ne_n,\quad D(H)=\{\xi:\sum_{n\geq0}n^2|\xi_n|^2<\infty\},\quad v=\sum_{n\geq1}n^{-5/4}e_n$', 18)
put(ax, .065, .797, r'$v\in\ell^2\setminus D(H),\qquad b=|v\rangle\langle e_0|+|e_0\rangle\langle v|,\qquad a=ib$', 20)
put(ax, .065, .755, r'$b=b^*\in B(\ell^2),\quad L=H+b,\quad D(L)=D(H),\quad p=|e_0\rangle\langle e_0|$', 18)
put(ax, .065, .710, r'$\alpha_t=\operatorname{Ad}(e^{itH}),\quad\beta_t=\operatorname{Ad}(e^{itL}),\quad u_t=e^{itL}e^{-itH}$', 20)
put(ax, .065, .667, r"$u'_t=i e^{itL}b e^{-itH}=u_t\alpha_t(ib)$", 20, color=BLUE)
line(ax, .055, .634, .945, .634)

band(ax, .605, '2   The fixed projection acquires an explicit bounded first derivative')
put(ax, .065, .564, r'$\alpha_t(p)=p\quad\Longrightarrow\quad p\in M_\alpha^\infty\subseteq D_\alpha=D_\beta$', 20)
put(ax, .065, .518, r'$T=\delta_\beta p=i[b,p]=i(|v\rangle\langle e_0|-|e_0\rangle\langle v|)$', 20, color=GREEN)
box(ax, .058, .407, .884, .078)
put(ax, .078, .457, r'On $\operatorname{span}\{e_0,v\}$, use the orthonormal basis $(e_0,w)$ with $w=v/m$, $m=\|v\|>0$:', 14)
put(ax, .078, .426, r'$be_0=mw,\quad bw=me_0;\qquad Te_0=imw=iv,\quad Tw=-im e_0.$', 18)
put(ax, .065, .382, r'Both $b$ and $T$ vanish on $\operatorname{span}\{e_0,w\}^{\perp}$; $\|b\|=\|T\|=m$.', 14)
line(ax, .055, .356, .945, .356)

band(ax, .326, '3   A second derivative would force preservation of D(L)')
put(ax, .065, .286, r'$T\in D_\beta\quad\Longrightarrow\quad T(D(L))\subseteq D(L)$', 21)
put(ax, .065, .251, r'Reason: $e^{itL}T\xi=\beta_t(T)e^{itL}\xi$ is differentiable for $\xi\in D(L)$.', 15)
put(ax, .202, .204, r'$e_0\in D(L)$', 22, ha='center', color=GREEN)
arrow(ax, .351, .204, .581, .204, color=RED)
put(ax, .465, .230, r'$T$', 17, ha='center', color=RED)
put(ax, .768, .204, r'$iv\notin D(L)$', 22, ha='center', color=RED)
put(ax, .50, .146, r'$T\notin D_\beta\quad\Longrightarrow\quad p\notin D(\delta_\beta^2),\qquad p\in M_\alpha^\infty\setminus M_\beta^\infty$', 21, color=RED, ha='center')
footer(ax, [
    'Proof: OA-FLOW-BP, Section 7 (X1–X10), oa-flow.bp.counterexample.',
    'Antecedent: M. Takesaki, Theory of Operator Algebras II, Chapter XI, §3. Original example and diagram.',
    'Section 6 constructs the selfadjoint sum on its full domain; (X8)–(X9) prove domain preservation.',
])
finish(fig, '34-lost-second-derivative')


# Figure 3. Two separate y scales prevent the convergent sum being visually lost.
NMAX = 10000
n = np.arange(1, NMAX + 1, dtype=np.float64)
s = np.cumsum(n ** -2.5)
q = np.cumsum(n ** -0.5)
sample_N = np.unique(np.rint(np.geomspace(1, NMAX, 145)).astype(int))
fig, ax = page('Why the coupling vector exists but its H-image does not',
              'At exponent r = 5/4, the two squared-coordinate sums lie on opposite sides of summability.',
              size=(14, 13.8))
put(ax, .065, .884, r'$v_n=n^{-5/4}:\qquad |v_n|^2=n^{-5/2},\qquad n^2|v_n|^2=n^{-1/2}$', 23)
left = fig.add_axes([.125, .516, .330, .278])
right = fig.add_axes([.609, .516, .330, .278])
left.plot(sample_N, s[sample_N - 1], color=GREEN, marker='o', markersize=3, lw=1.8)
left.set(xscale='log', xlim=(1, NMAX), ylim=(.98, 1.37), xlabel=r'$N$', ylabel=r'$S_N=\sum_{n=1}^{N}n^{-5/2}$')
left.set_title('Finite partial sums: bounded', fontsize=16, loc='left', color=GREEN, pad=13)
left.set_xticks([1, 10, 100, 1000, 10000])
left.grid(True, which='major', alpha=.22)
right.plot(sample_N, q[sample_N - 1], color=RED, marker='o', markersize=3, lw=1.8, label=r'$Q_N$ samples')
right.plot(sample_N, 2*(np.sqrt(sample_N+1)-1), color=BLUE, ls='--', lw=1.5, label='proved lower bound')
right.set(xscale='log', xlim=(1, NMAX), ylim=(0, 211), xlabel=r'$N$', ylabel=r'$Q_N=\sum_{n=1}^{N}n^{-1/2}$')
right.set_title('Finite partial sums: growing', fontsize=16, loc='left', color=RED, pad=13)
right.set_xticks([1, 10, 100, 1000, 10000])
right.grid(True, which='major', alpha=.22)
right.legend(loc='upper left', fontsize=11, frameon=False)
put(ax, .065, .464, 'Dots are finite numerical samples (1 <= N <= 10,000). Connecting lines only guide the eye.', 13, color=GRAY)
put(ax, .065, .433, 'Convergence and divergence follow from the exact inequalities below, not from these plots.', 14, weight='bold')
box(ax, .058, .271, .884, .129)
put(ax, .078, .372, r'$S_N\leq 1+\int_1^\infty x^{-5/2}\,dx=5/3\qquad\Longrightarrow\qquad v\in\ell^2$', 20, color=GREEN)
put(ax, .078, .323, r'$Q_N\geq\int_1^{N+1}x^{-1/2}\,dx=2(\sqrt{N+1}-1)\longrightarrow\infty$', 20, color=RED)
put(ax, .078, .288, r'Therefore $v\notin D(H)$.  The expression $Hv$ is not an element of the Hilbert space.', 14)
put(ax, .065, .233, r'Exact parameter window for $v_n=n^{-r}$:', 17, weight='bold')
put(ax, .065, .191, r'$v\in\ell^2\Longleftrightarrow r>1/2;\qquad v\in D(H)\Longleftrightarrow r>3/2.$', 22)
put(ax, .065, .148, r'Hence $1/2<r\leq3/2$ gives the lost-second-derivative construction (including both $r=1$ and $r=5/4$).', 15)
footer(ax, [
    'Proof: OA-FLOW-BP, Section 7: (X3) and (X11–X13), oa-flow.bp.counterexample.',
    'Antecedent: M. Takesaki, Theory of Operator Algebras II, Chapter XI, §3. Original coordinate plots.',
    'Integral comparison proves the bounds. For r > 3/2 this particular obstruction vanishes; smoothness is not asserted.',
])
finish(fig, '34-summability-and-domain-window')


# Numerical sanity checks support the drawing; the exact reasoning is in captions.
checks = []
def check(name, value):
    assert bool(value), name
    checks.append({'check': name, 'pass': True})
check('all S_N below the exact 5/3 upper bound', np.all(s <= 5/3))
check('all Q_N above exact integral lower bound', np.all(q + 1e-10 >= 2*(np.sqrt(n+1)-1)))
check('all Q_N below exact integral upper bound', np.all(q <= 2*np.sqrt(n)-1 + 1e-10))
for N in (1, 7, 29):
    v = np.arange(1, N+1, dtype=float) ** -1.25
    b = np.zeros((N+1, N+1), complex)
    b[1:, 0] = v
    b[0, 1:] = v
    p = np.zeros_like(b); p[0, 0] = 1
    T = 1j * (b @ p - p @ b)
    check(f'finite algebra diagnostic N={N}: b selfadjoint', np.allclose(b, b.conj().T))
    check(f'finite algebra diagnostic N={N}: T selfadjoint', np.allclose(T, T.conj().T))
    check(f'finite algebra diagnostic N={N}: T e0 = i v with positive sign', np.allclose(T[1:,0], 1j*v))
    check(f'finite algebra diagnostic N={N}: T w = -i norm(v) e0', np.allclose(T @ np.r_[0, v/np.linalg.norm(v)], -1j*np.linalg.norm(v)*np.eye(N+1)[:,0]))

samples = []
for N in (1, 10, 100, 1000, 10000):
    samples.append({'N': N, 'S_N_sample': float(s[N-1]), 'Q_N_sample': float(q[N-1]),
                    'Q_N_proved_lower_bound_evaluated': 2*(math.sqrt(N+1)-1)})
def write_json(name, value):
    (HERE/name).write_bytes((json.dumps(value, indent=2, ensure_ascii=False)+'\n').encode('utf-8'))

write_json('34-derivation-domain-data.json', {
    'schema': 'oa-flow-xi3-figure-samples/v1',
    'meaning': 'Float64 partial-sum and finite-matrix diagnostics; none is an infinite-dimensional proof.',
    'range': [1, NMAX], 'plotted_sample_N': [int(x) for x in sample_N],
    'samples': samples, 'checks': checks,
})
write_json('LAYOUT_CHECKS.json', {'schema': 'oa-flow-xi3-figure-layout/v1', 'figures': LAYOUT,
    'scope': 'Text extents inside the canvas; visual inspection is recorded separately.'})
write_json('BUILD_RECEIPT.json', {
    'schema': 'oa-flow-xi3-original-figure-build/v1',
    'status': 'render complete; visual inspection recorded separately',
    'runtime': {'matplotlib': matplotlib.__version__, 'numpy': np.__version__, 'tex_used': False},
    'outputs': ARTIFACTS,
    'source': {'path': Path(__file__).name, 'bytes': Path(__file__).stat().st_size,
               'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
})
print(json.dumps({'figures': len(LAYOUT), 'artifacts': len(ARTIFACTS), 'numerical_diagnostics': len(checks), 'all_text_inside_canvas': True}))
