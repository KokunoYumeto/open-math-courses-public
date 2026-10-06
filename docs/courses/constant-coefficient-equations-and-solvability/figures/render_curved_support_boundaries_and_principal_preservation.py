"""Exact wave cylinder and adapted support coordinates; no model solution is sampled."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
STEM = 'curved-wave-cylinder-and-adapted-support-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 18, 'svg.hashsalt': STEM, 'axes.titlesize': 22, 'axes.labelsize': 20})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'A curved support boundary with straight characteristic generators', fontsize=29, weight='bold', color='#132a38')
    fig.text(0.045, 0.911, 'Wave $q=\\xi_1^2+\\xi_2^2-\\xi_3^2$; orthonormal $r=(x_1+x_3)/\\sqrt{2}$, $z=x_2$, $w=(x_1-x_3)/\\sqrt{2}$.', fontsize=20.5, color='#41505a')
    left = fig.add_axes([0.025, 0.335, 0.46, 0.495], projection='3d', computed_zorder=False)
    right = fig.add_axes([0.57, 0.35, 0.37, 0.45], facecolor='white')
    rr = np.linspace(-1.25, 1.25, 51)
    ww = np.linspace(-1.25, 1.25, 31)
    R, W = np.meshgrid(rr, ww)
    Z = -R * R / 2
    left.plot_surface(R, W, np.zeros_like(R), color='#a7b2ba', alpha=0.1, linewidth=0, zorder=0)
    generator_grid, height_grid = np.meshgrid(np.linspace(-1.25, 1.25, 11), np.linspace(-1.15, 1.1, 11))
    left.plot_surface(np.zeros_like(generator_grid), generator_grid, height_grid, color='#d58940', alpha=0.13, linewidth=0, zorder=0)
    left.plot_surface(R, W, Z, color='#2a938f', alpha=0.52, edgecolor='none', zorder=1)
    for rv in np.linspace(-1, 1, 5):
        left.plot([rv, rv], [-1.25, 1.25], [-rv * rv / 2, -rv * rv / 2], color='#167194', lw=2.3, zorder=3)
    left.plot(rr, np.zeros_like(rr), -rr * rr / 2, color='#116763', lw=3, zorder=4)
    left.scatter([0], [0], [0], s=50, color='#132a38', depthshade=False, zorder=5)
    for vector, color in (((1, 0, 0), '#bd6d2c'), ((0, 1, 0), '#167194'), ((0, 0, 1), '#176b63')):
        left.quiver(0, 0, 0, *vector, length=1, normalize=False, color=color, arrow_length_ratio=0.13, lw=2.8, zorder=6)
    left.text(1.08, -0.02, 0.03, '$\\eta=e_r$', fontsize=17, color='#9e5420', zorder=8)
    left.text(-0.08, 1.03, 0.09, '$v=e_w$', fontsize=17, color='#135c7b', zorder=8)
    left.text(0.03, 0.05, 1.07, '$n(0)=e_z$', fontsize=16.5, color='#176b63', zorder=8)
    left.set_xlim(-1.4, 1.4)
    left.set_ylim(-1.4, 1.4)
    left.set_zlim(-1.7, 1.2)
    left.set_box_aspect([2.8, 2.8, 2.9])
    left.set_proj_type('ortho')
    left.view_init(elev=23, azim=-56)
    left.set_xlabel('$r$', labelpad=8)
    left.set_ylabel('$w$', labelpad=8)
    left.set_zlabel('$z$', labelpad=7)
    left.set_xticks([-1, 0, 1])
    left.set_yticks([-1, 0, 1])
    left.set_zticks([-1, 0, 1])
    left.set_title('Exact cylinder, characteristic plane and tangent plane', pad=5)
    left.set_facecolor('#fbfaf6')
    curve = np.linspace(-1.35, 1.35, 501)
    boundary = -curve * curve / 2
    right.fill_between(curve, -2.05, boundary, color='#d5e9e3', alpha=0.9)
    for value in (0.4, 0.8, 1.2):
        right.plot(curve, boundary - value, color='#167194', lw=2, ls='--', alpha=0.82)
        rv = -0.8
        right.text(rv, -rv * rv / 2 - value + 0.04, f'$y_2={value}$', fontsize=17, color='#135c7b', bbox={'facecolor': '#d5e9e3', 'edgecolor': 'none', 'pad': 1})
    right.plot(curve, boundary, color='#116763', lw=4)
    right.axvline(0, color='#bd6d2c', ls=':', lw=2)
    right.scatter([0], [0], s=55, color='#132a38', zorder=6)
    right.text(0.3, -0.09, '$\\phi=0,\\ y_2=0$', fontsize=18, color='#116763')
    right.text(-1.05, 0.35, '$\\phi>0$', fontsize=18, color='#41505a')
    right.text(0.12, -1.88, 'Support side: $\\phi\\leq0$', fontsize=18, color='#176b63')
    right.annotate('', xy=(0.99, -1.72), xytext=(0.99, -0.92), arrowprops={'arrowstyle': '->', 'lw': 2.5, 'color': '#135c7b'})
    right.text(0.12, -1.03, '$y_2$ increases', fontsize=17, color='#135c7b')
    right.set_xlim(-1.35, 1.35)
    right.set_ylim(-2.05, 0.65)
    right.set_aspect('equal', adjustable='box')
    right.set_xlabel('$r=y_1=\\psi$')
    right.set_ylabel('$z$ in the section $w=0$')
    right.set_title('Exact support side and translated coordinate levels', pad=22)
    right.grid(color='#cfdad8', alpha=0.55)
    for ypos, color, style, label in [(0.258, '#116763', '-', 'Boundary: $\\phi=z+r^2/2=0$'), (0.203, '#bd6d2c', ':', 'Characteristic plane: $r=0$'), (0.148, '#a7b2ba', '-', 'Tangent plane at the origin: $z=0$')]:
        fig.add_artist(Line2D([0.045, 0.077], [ypos + 0.004, ypos + 0.004], transform=fig.transFigure, color=color, lw=3.5, ls=style))
        fig.text(0.088, ypos, label, fontsize=20, color='#132a38')
    fig.text(0.045, 0.089, 'Straight generator: $v=e_w$; Hamilton vector: $2e_w$.', fontsize=19, color='#41505a')
    fig.text(0.535, 0.258, '$F(r,z,w)=(r,-z-r^2/2,w)$; level curves are translated downward.', fontsize=19, color='#132a38')
    fig.text(0.535, 0.203, '$\\widetilde q=\\eta_2^2+2(\\eta_1-y_1\\eta_2)\\eta_3$.', fontsize=22, color='#132a38')
    fig.text(0.535, 0.148, 'The exact correction is first order, so the wave principal part stays fixed.', fontsize=18.5, color='#41505a')
    fig.text(0.535, 0.089, 'Transverse curvature $1/(1+r^2)^{3/2}>0$; generator curvature $0$.', fontsize=19, color='#41505a')
    fig.text(0.045, 0.035, 'Equations (22)–(31); Exercises 5–6. Exact cylinder geometry; the solution is not sampled.', fontsize=14.5, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    meta = {'schema': 'exact-curved-wave-cylinder-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(22)-(31)', 'Exercises 5-6'], 'kappa': 1, 'symbol': 'xi1^2+xi2^2-xi3^2', 'orthonormal_coordinates': {'r': '(x1+x3)/sqrt2', 'z': 'x2', 'w': '(x1-x3)/sqrt2'}, 'surface': 'z=-r^2/2', 'surface_r_and_w_range': [-1.25, 1.25], 'characteristic_plane': 'r=0', 'boundary_tangent_plane_at_origin': 'z=0', 'left_projection': 'orthographic', 'left_plot_axis_order': ['r', 'w', 'z'], 'left_data_ranges': [[-1.4, 1.4], [-1.4, 1.4], [-1.7, 1.2]], 'left_box_aspect': [2.8, 2.8, 2.9], 'left_equal_physical_unit_scale_before_projection': True, 'arrows_in_plot_r_w_z_order': {'characteristic_normal': [1, 0, 0], 'generator': [0, 1, 0], 'boundary_normal_at_origin': [0, 0, 1]}, 'Hamilton_vector': '2*e_w', 'right_section': 'w=0', 'right_r_range': [-1.35, 1.35], 'right_z_range': [-2.05, 0.65], 'right_equal_euclidean_axes': True, 'adapted_map': '(r,-z-r^2/2,w)', 'full_original_coordinate_Jacobian_determinant': 1, 'adapted_map_determinant_in_r_z_w_coordinates': -1, 'coordinate_levels': [0, 0.4, 0.8, 1.2], 'support_side': 'z+r^2/2<=0', 'transformed_symbol': 'eta2^2+2*(eta1-y1*eta2)*eta3', 'transverse_curvature': '1/(1+r^2)^(3/2)', 'generator_curvature': 0, 'curvature_convention': 'II(tau,tau)=<D_tau(n_phi),tau>; n_phi=grad(phi)/|grad(phi)|', 'coordinate_arrow_tail_r_z': [0.99, -0.92], 'coordinate_arrow_head_r_z': [0.99, -1.72], 'coordinate_arrow_is_normal_distance_curve': False, 'geometry_window_is_finite_crop': True, 'constructed_solution_or_coefficient_sampled': False, 'finite_picture_replaces_general_proof': False, 'Blender_available_on_PATH_at_checkpoint': False, 'renderer': 'Matplotlib exact scientific geometry', 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)
