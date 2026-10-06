"""Reproduce the exact quadratic averaging geometry. Original work CC0."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np

def render(output):
    output.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({
        'font.family': 'DejaVu Sans', 'font.size': 12,
        'svg.hashsalt': 'AN02-polynomial-averaging036',
        'axes.spines.top': False, 'axes.spines.right': False,
    })
    fig, axes = plt.subplots(1, 2, figsize=(13.6, 6.4), dpi=150)
    left, right = axes
    blue, green, red = '#215e9b', '#217653', '#ad343c'
    theta = np.linspace(0, 2*np.pi, 1001)
    left.add_patch(Circle((0, 0), 1, fill=False, edgecolor='#8894a0',
                          linestyle='--', linewidth=1.3))
    left.add_patch(Wedge((0, 0), 5/12, 0, 360, width=5/12-1/3,
                         facecolor='#bee3d2', alpha=.85, edgecolor=green))
    left.plot((3/8)*np.cos(theta), (3/8)*np.sin(theta), color=blue, lw=2)
    left.scatter([-1/4, 1/4], [0, 0], marker='x', s=75, color=red, zorder=5)
    left.scatter([0], [0], s=18, color='#25313a', zorder=5)
    left.annotate(r'zeros $\pm1/4$', xy=(1/4, 0), xytext=(.43, -.25),
                  arrowprops={'arrowstyle':'->','color':red}, color=red)
    left.annotate(r'$|z|=3/8$', xy=(-3/8, 0), xytext=(-1.02, .17),
                  arrowprops={'arrowstyle':'->','color':blue}, color=blue)
    left.annotate('available density support\ninside the annulus',
                  xy=(0, -5/12), xytext=(-.88, -.80),
                  arrowprops={'arrowstyle':'->','color':green}, color=green)
    left.text(.08, .97, r'$\rho=1$', ha='left', va='bottom', color='#536271')
    left.set(xlim=(-1.12, 1.12), ylim=(-1.1, 1.15), xlabel=r'$\operatorname{Re}z$',
             ylabel=r'$\operatorname{Im}z$', title='A full circle separated from both roots')
    left.text(0, -1.02, r'$1/3\leq |z|\leq5/12$', ha='center', color=green)

    center, radius = -1/16, 9/64
    # This is the entire exact image circle, not a numerical zero test.
    right.plot(center+radius*np.cos(theta), radius*np.sin(theta), color=blue, lw=2.4)
    right.scatter([0, center], [0, 0], s=[28, 25], color=['#25313a', blue], zorder=5)
    right.text(-.004, -.018, '0', ha='right', va='top')
    right.annotate(r'centre $-1/16$', xy=(center, 0), xytext=(-.19, -.13),
                   arrowprops={'arrowstyle':'->','color':blue}, color=blue)
    right.annotate('', xy=(center, radius), xytext=(center, 0),
                   arrowprops={'arrowstyle':'<->','color':blue})
    right.text(center-.008, radius/2, r'$9/64$', rotation=90, va='center', ha='right', color=blue)
    right.annotate('', xy=(5/64, 0), xytext=(0, 0),
                   arrowprops={'arrowstyle':'<->','color':green,'lw':1.7})
    right.text(5/128, .018, r'$5/64$', ha='center', color=green)
    right.annotate('nearest image point', xy=(5/64, 0), xytext=(.10, -.075),
                   arrowprops={'arrowstyle':'->','color':green}, color=green, ha='center')
    right.text(-.06, .178, r'$q((3/8)e^{it})=-1/16+(9/64)e^{2it}$', ha='center')
    right.text(-.06, -.18, 'The phase circle traverses this image twice.\nEvery image point stays away from zero.',
               ha='center', va='top', fontsize=11)
    right.set(xlim=(-.24, .20), ylim=(-.22, .22), xlabel=r'$\operatorname{Re}q$',
              ylabel=r'$\operatorname{Im}q$', title='The quadratic image and its positive distance')
    for ax in axes:
        ax.set_aspect('equal', adjustable='box')
        ax.axhline(0, color='#cad0d5', lw=.7, zorder=0)
        ax.axvline(0, color='#cad0d5', lw=.7, zorder=0)
        ax.tick_params(labelsize=10)
    fig.suptitle(r'Averaging away from the zeros of $q(z)=z^2-1/16$', fontsize=17)
    fig.tight_layout(rect=(0, 0, 1, .94))
    fig.savefig(output/'polynomial-averaging-annulus.png',
                metadata={'Software':'AN02 CC0 reproducible geometry'})
    fig.savefig(output/'polynomial-averaging-annulus.svg',
                metadata={'Date':None,'Creator':'AN02 CC0 reproducible geometry'})
    plt.close(fig)
    geometry = {
        'schema':'AN02-polynomial-averaging036-geometry/v1',
        'license':'CC0-1.0', 'polynomial':'z^2-1/16',
        'rho':'1', 'roots':['-1/4','1/4'],
        'available_closed_annulus':{'inner':'1/3','outer':'5/12'},
        'actual_density_support':'any normalized smooth radial bump compactly inside the open annulus',
        'phase_circle_radius':'3/8', 'image_center':'-1/16',
        'image_radius':'9/64', 'image_traversals':2,
        'exact_annulus_lower_bound':'7/144',
        'exact_phase_circle_lower_bound':'5/64',
        'coefficient_norm':'sqrt(1025)/16',
        'normalized_annulus_bound':'7/(9*sqrt(1025))',
        'proof_locators':['PA036-3','PA036-4','learner section 5, first example','learner exercise 4'],
        'illustration_is_not_a_numerical_proof':True,
    }
    (output/'polynomial-averaging.geometry.json').write_text(
        json.dumps(geometry, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent/'figures')
    render(parser.parse_args().output)
