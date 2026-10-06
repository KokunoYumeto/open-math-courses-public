"""Exact sampled figures for the compact-kernel punctured-cone converse.

The renderer's assertions are checks on its encoded samples, not mathematical
proofs of graph convergence or a theorem's general zero-free hypothesis.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import rc_context

OUT = Path(__file__).resolve().parent / 'figures'
OUT.mkdir(exist_ok=True)
COL = {'low': '#245fa5', 'high': '#984aa0', 'mid': '#608265', 'red': '#ad3737'}

with rc_context({'font.family': 'DejaVu Sans', 'font.size': 10,
                 'svg.hashsalt': 'AN02-converse-035', 'axes.titlesize': 12}):
    xi = np.linspace(-7, 7, 1001)
    h = np.log(2 + xi * xi)
    for scale in (12, 14, 16):
        assert np.all(scale * h > 2 * np.log(np.abs(xi + 1j * scale * h) + 2))
    fig, (ax, aj) = plt.subplots(1, 2, figsize=(13, 5.7),
                                gridspec_kw={'width_ratios': [1.22, 1]})
    for lo, hi in ((-6, -3), (3, 6)):
        mask = (xi >= lo) & (xi <= hi)
        ax.fill_between(xi, 12*h, 16*h, where=mask, color='#f4d994', alpha=.65)
        ax.axvspan(lo, hi, color='#f7e9c7', alpha=.32)
    for scale, color, style in ((12, COL['low'], '-'), (14, COL['mid'], '--'),
                                (16, COL['high'], '-')):
        ax.plot(xi, scale*h, color=color, ls=style, lw=1.8,
                label=f'L = {scale}')
    ax.plot([0], [0], 'o', color=COL['red'], ms=6)
    ax.annotate('only pole: z = 0', (0, 0), xytext=(-6.6, 8),
                arrowprops={'arrowstyle': '->', 'color': COL['red']},
                color=COL['red'], fontsize=9)
    ax.text(.035, .95, 'z = ξ + i L log(2 + ξ²)\nCutoff derivative: 3 ≤ |ξ| ≤ 6',
            transform=ax.transAxes, va='top', fontsize=9,
            bbox={'facecolor': 'white', 'alpha': .9, 'edgecolor': 'none'})
    ax.annotate('', (4, 16*np.log(18)), (4, 12*np.log(18)),
                arrowprops={'arrowstyle': '->', 'lw': 1.5, 'color': '#755c21'})
    ax.text(4.22, 14*np.log(18), 'raise L', fontsize=9, color='#755c21')
    ax.set(xlim=(-7, 7), ylim=(-3, 69), xlabel='real frequency ξ',
           ylabel='imaginary frequency Im z', title='A finite safe graph homotopy')
    ax.legend(loc='lower right', frameon=True, fontsize=9)
    exact_im = 24*xi/(2+xi*xi)
    aj.plot(xi, np.ones_like(xi), color='#222', lw=1.5, label='Re J = 1')
    aj.plot(xi, exact_im, color=COL['low'], lw=2,
            label='Im J = 24 ξ / (2 + ξ²)')
    aj.axhline(0, color='#aaa', lw=.7)
    aj.axvline(0, color='#aaa', lw=.7)
    aj.set(xlim=(-7, 7), ylim=(-10, 10), xlabel='real frequency ξ',
           ylabel='complex determinant components',
           title='Exact pullback coefficient, L = 12')
    aj.legend(loc='upper left', frameon=False, fontsize=9)
    fig.text(.57, .035, 'J = 1 + i L ∂ξh. The graph integral uses J, including its phase.',
             fontsize=9)
    fig.suptitle('Logarithmic graphs: cutoff side term and rank-one Jacobian', fontsize=14)
    fig.subplots_adjust(left=.075, right=.975, bottom=.17, top=.82, wspace=.27)
    fig.savefig(OUT/'logarithmic-cutoff-and-jacobian.png', dpi=180,
                metadata={'Software': 'AN02 original renderer'})
    fig.savefig(OUT/'logarithmic-cutoff-and-jacobian.svg', metadata={'Date': None})
    plt.close(fig)

    grid = np.linspace(-3, 3, 65)
    X, Y = np.meshgrid(grid, grid)
    T = 2 + X*X + Y*Y
    lam = 4*np.log(T)
    jim = (8*X+4*Y)/T
    # |u dot gradient h| <= |u| / sqrt(2), u=(4,2).
    assert np.max(np.abs(jim)) <= np.sqrt(20)/np.sqrt(2) + 1e-12
    fig = plt.figure(figsize=(13.2, 6))
    ax = fig.add_subplot(121, projection='3d')
    norm = plt.Normalize(vmin=-3.2, vmax=3.2)
    cmap = plt.get_cmap('coolwarm')
    ax.plot_surface(X, Y, lam, facecolors=cmap(norm(jim)),
                    rcount=65, ccount=65, linewidth=0, antialiased=True,
                    shade=False, alpha=.93)
    ax.set(xlabel='ξ₁', ylabel='ξ₂', zlabel='λ')
    ax.view_init(elev=27, azim=-58)
    fig.text(.25, .835, 'Exact graph in a 3D representation', ha='center', fontsize=12)
    fig.text(.075, .785, 'Im z₁ = λ,  Im z₂ = λ / 2,  λ = 4 log(2 + |ξ|²)', fontsize=9)
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    cb = fig.colorbar(sm, ax=ax, shrink=.5, pad=.08, fraction=.035,
                      orientation='horizontal', aspect=28)
    cb.set_label('Im J = (8ξ₁ + 4ξ₂) / (2 + |ξ|²)', fontsize=9)
    ag = fig.add_subplot(122)
    vx = np.linspace(0, 3.1, 100)
    ag.fill_between(vx, -vx, vx, color='#e6f0fb', alpha=.85)
    ag.plot(vx, vx, '--', color='#7293bc', lw=1)
    ag.plot(vx, -vx, '--', color='#7293bc', lw=1)
    ag.axhline(0, color='#aaa', lw=.7)
    ag.axvline(0, color='#aaa', lw=.7)
    ag.plot([0], [0], 'o', mfc='white', mec=COL['red'], ms=6, zorder=5)
    ag.annotate('zero excluded', (0, 0), xytext=(.16, -.6),
                arrowprops={'arrowstyle': '->', 'color': COL['red']},
                color=COL['red'], fontsize=9)
    ag.plot([1, 1], [0, .5], color=COL['high'], lw=3)
    ag.plot([1, 1], [0, .5], 'o', color=COL['high'], ms=5)
    ag.annotate('θ₀ = (1, 0)', (1, 0), xytext=(1.13, -.26), fontsize=9)
    ag.annotate('θ₁ = (1, 1/2)', (1, .5), xytext=(1.1, .76), fontsize=9)
    ag.plot([0, 2.1], [0, 0], color=COL['low'], alpha=.6, lw=1.2)
    ag.plot([0, 2.1], [0, 1.05], color=COL['low'], alpha=.6, lw=1.2)
    for ray_y in [0, 1.175]:
        ag.annotate('', (2.35, ray_y), (2.05, ray_y*(2.05/2.35)),
                    arrowprops={'arrowstyle':'->','color':COL['low'],'lw':1.2,'alpha':.6})
    ag.text(.10, .93, 'Γ = {θ₁ > |θ₂|}\nθ(s) = (1, s/2),  |θ(s)| ≥ 1',
            transform=ag.transAxes, fontsize=10)
    ag.set(xlim=(-.2, 2.4), ylim=(-1.7, 1.7), xlabel='direction coordinate θ₁',
           ylabel='direction coordinate θ₂', title='A compact interior direction path')
    ag.set_aspect('equal')
    fig.suptitle('The actual Fourier graph map and its cone homotopy', fontsize=14)
    fig.subplots_adjust(left=.045, right=.97, bottom=.12, top=.80, wspace=.25)
    fig.savefig(OUT/'two-variable-graph-and-directions.png', dpi=180,
                metadata={'Software': 'AN02 original renderer'})
    fig.savefig(OUT/'two-variable-graph-and-directions.svg', metadata={'Date': None})
    plt.close(fig)

    # Actual half-space model mu=partial_x1 delta0, theta=(1,0), A=0.
    # E=-H(-x1) tensor delta0(x2) has negative first-axis support.
    from matplotlib.patches import Circle
    fig, (ap, ad) = plt.subplots(1, 2, figsize=(13, 5.7),
                                gridspec_kw={'width_ratios': [1, 1.22]})
    ap.axvspan(-3, 0, color='#e8eef7')
    ap.axvline(0, color='#667a98', lw=1.3)
    ap.axhline(0, color='#aaa', lw=.7)
    ap.plot([-2.7, 0], [0, 0], color=COL['low'], lw=5)
    ap.annotate('', (-2.9, 0), (-2.1, 0),
                arrowprops={'arrowstyle': '->', 'color': COL['low'], 'lw': 2})
    ap.plot([0], [0], 'o', color=COL['low'], ms=6)
    ap.add_patch(Circle((2, 0), .5, facecolor='#b8e3d8',
                       edgecolor='#26836e', alpha=.9, lw=1.5))
    ap.plot([2], [0], 'o', color='#26836e', ms=4)
    ap.axvline(1.5, color='#26836e', lw=1, ls='--')
    ap.annotate('', (1.5, -.9), (0, -.9),
                arrowprops={'arrowstyle': '<->', 'color': '#5a4d21'})
    ap.text(.23, -1.15, 'gap d = 3/2', fontsize=10, color='#5a4d21')
    ap.annotate('', (1, 1.1), (0, 1.1),
                arrowprops={'arrowstyle': '->', 'color': '#222', 'lw': 1.5})
    ap.text(.02, 1.32, 'θ = (1, 0)', fontsize=10)
    ap.text(-2.9, .38, 'exact inverse support\nnegative x₁-axis',
            color=COL['low'], fontsize=9)
    ap.text(-2.9, -1.35, 'permitted half-space: x₁ ≤ 0', fontsize=9)
    ap.text(1.68, .73, 'compact test support B\ncenter (2, 0), radius 1/2',
            fontsize=9, color='#176854', ha='center')
    ap.set(xlim=(-3, 3), ylim=(-1.6, 1.65), xlabel='spatial coordinate x₁',
           ylabel='spatial coordinate x₂', title='The support plane and a strict test gap')
    ap.set_aspect('equal')
    radial = np.linspace(0, 6, 701)
    tt = 2 + radial*radial
    hh = np.log(tt)
    cc = 3*np.log(2)/4
    K0 = (7/cc)**7*np.exp(-7+cc)
    K = K0*(6/np.e)**6
    envelope = tt**-2
    ad.semilogy(radial, envelope, color='#222', lw=2,
                label='retained integrable envelope: (2 + r²)⁻²')
    for scale, color in ((12, COL['low']), (16, COL['mid']), (20, COL['high'])):
        bound = tt**-3*hh**6*(1+scale)**7*np.exp(-1.5*scale*hh)
        assert np.all(bound/K <= envelope*(1+1e-12))
        ad.semilogy(radial, bound/K, lw=1.8, color=color,
                    label=f'g_L(r) / K,  L = {scale}')
    ad.set(xlim=(0, 6), ylim=(1e-58, 1), xlabel='real frequency radius r = |ξ|',
           ylabel='normalized absolute upper-bound functions',
           title='One majorant works for every increasing scale')
    ad.legend(loc='lower left', fontsize=8.5, frameon=False)
    ad.text(.40, .94, 'e⁻ᵈᴸʰ defeats the scale powers; d = 3/2\np = 0, N = 3, n = 2',
            transform=ad.transAxes, fontsize=9, va='top')
    fig.suptitle('Why the inverse vanishes beyond the supporting plane', fontsize=14)
    fig.subplots_adjust(left=.075, right=.975, bottom=.16, top=.82, wspace=.30)
    fig.text(.55, .025, 'g_L = t⁻³ (log t)⁶ (1 + L)⁷ exp(−3 L log(t) / 2),  t = 2 + r²', fontsize=9)
    fig.savefig(OUT/'support-plane-and-uniform-decay.png', dpi=180,
                metadata={'Software': 'AN02 original renderer'})
    fig.savefig(OUT/'support-plane-and-uniform-decay.svg', metadata={'Date': None})
    plt.close(fig)

geometry = {
    'schema': 'AN02-compact-kernel-converse-figures/v1',
    'figure1': {
        'exact_graph': 'z_L(xi)=xi+i L log(2+xi^2)',
        'scales': [12, 14, 16], 'kernel': 'mu=delta_prime_0',
        'reciprocal': 'q(z)=1/(i z)', 'pole_set': ['0'],
        'threshold': 'Im z>2log(|z|+2)',
        'proof_locator': 'manuscript Figure1 and learner Problem2',
        'exact_jacobian': 'J=1+24i xi/(2+xi^2) at L12',
        'cutoff_R': 3, 'cutoff_derivative_support': '3<=|xi|<=6',
        'real_samples': 1001, 'real_interval': [-7, 7],
        'side_bound_locator': 'manuscript5.8-5.11',
        'shading': 'frequency projection of actual cutoff-derivative annuli; strip between endpoint graphs'
    },
    'figure2': {
        'exact_map': 'z=(xi1+4i h,xi2+2i h), h=log(2+xi1^2+xi2^2)',
        'representation': '(xi1,xi2,lambda) with lambda=4h; Im z2=lambda/2 exactly',
        'exact_jacobian': 'J=1+i(8xi1+4xi2)/(2+xi1^2+xi2^2)',
        'grid_samples_per_axis': 65, 'real_axis_intervals': [[-3,3],[-3,3]],
        'color': 'Im J, not surface area or reciprocal estimate',
        'cone': 'Gamma={theta1>|theta2|}',
        'exact_direction_path': 'theta(s)=(1,s/2),0<=s<=1',
        'minimum_path_norm': 1, 'maximum_path_norm': 'sqrt(5)/2',
        'source_locator': 'manuscript9.4-9.5 and Section5',
        'kernel_threshold_claimed': False
    },
    'figure3': {
        'model':'mu=partial_x1 delta0 in R2',
        'exact_inverse':'E=-H(-x1) tensor delta0(x2)',
        'exact_support':'negative x1-axis',
        'direction':[1,0], 'A':0, 'p':0, 'N':3, 'n':2,
        'supporting_halfspace':'x1<=0',
        'test_support':'closed disk center(2,0),radius1/2',
        'test_bump':'exp(-1/(1/4-|x-(2,0)|^2)) inside disk; zero outside',
        'exact_gap':'d=3/2', 'combined_decay':'exp(-3 L h/2)',
        'upper_bound_function':'g_L=t^-3(log t)^6(1+L)^7exp(-3 L log(t)/2)',
        'normalization':'K=((7/c)^7 exp(-7+c))(6/e)^6,c=3log2/4',
        'retained_uniform_majorant':'g_L/K<=t^-2 for L>=0; t=2+|xi|^2',
        'plotted_safe_scales':[12,16,20], 'radial_samples':701,'radial_interval':[0,6],
        'integrand_measurements_claimed':False,
        'proof_locators':['manuscript Section8 and Figure3','learner Problems2,6,9']
    },
    'sample_checks_are_proofs': False,
    'reproducible_source': 'make_figures.py',
    'generated_artifacts': ['logarithmic-cutoff-and-jacobian.png',
                            'logarithmic-cutoff-and-jacobian.svg',
                            'two-variable-graph-and-directions.png',
                            'two-variable-graph-and-directions.svg',
                            'support-plane-and-uniform-decay.png',
                            'support-plane-and-uniform-decay.svg']
}
(OUT/'geometry.json').write_text(json.dumps(geometry, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'figures': 3, 'raster_and_vector': True,
                  'one_dimensional_graph_sample_checks': 3003,
                  'two_variable_jacobian_sample_checks': 4225,
                  'uniform_decay_envelope_sample_checks':2103}))
