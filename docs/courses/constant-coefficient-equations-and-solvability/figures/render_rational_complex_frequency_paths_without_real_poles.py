"""Reproducible exact-model figure for rational selection and real-pole removal."""
import argparse, hashlib, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
STEM = 'rational-frequency-path-and-real-pole-removal-025'

def run(output_dir=None):
    dest = Path(output_dir) if output_dir else Path(__file__).resolve().parent
    dest.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 20, 'svg.hashsalt': STEM, 'axes.titlesize': 24, 'axes.labelsize': 22, 'legend.fontsize': 19})
    fig = plt.figure(figsize=(24, 12), dpi=100, facecolor='#fbfaf6')
    fig.text(0.045, 0.955, 'Rational frequency paths and removal of real poles', fontsize=31, weight='bold', color='#132a38')
    fig.text(0.045, 0.913, 'Two exact algebraic models; no physical-space solution is sampled.', fontsize=21, color='#41505a')
    left = fig.add_axes([0.075, 0.345, 0.4, 0.475], facecolor='white')
    right = fig.add_axes([0.56, 0.345, 0.39, 0.475], facecolor='white')
    u = np.geomspace(1 / 128, 1 / 4, 257)
    left.loglog(u, u, color='#167194', lw=4, label='$K/T=T/\\lambda=\\lambda/(TK)=u$')
    left.loglog(u, u ** 2, color='#ba5237', lw=4, label='$\\|cP-1\\|_{\\rm c}=u^2$')
    left.loglog(u, u ** 4, color='#7954a1', lw=4, label='$|b/c|=u^4$')
    left.set_xlabel('Positive parameter $u$')
    left.set_ylabel('Exact error or scale ratio')
    left.set_title('Frequency path: $(\\kappa,\\tau,\\Lambda)=(2,3,4)$', pad=22)
    left.set_xlim(1 / 128, 1 / 4)
    left.set_ylim(1e-09, 0.5)
    left.grid(True, which='both', color='#d7dedf', alpha=0.65)
    left.legend(loc='lower right', framealpha=0.96)
    s = np.linspace(-5 / 4, 5 / 4, 501)
    right.plot(s, s ** 3, color='#167194', lw=4, label='$z(u)=u+iu^3$')
    right.axhline(0, color='#858a8e', lw=1.5, ls='--')
    right.axvline(0, color='#d7dedf', lw=1.2)
    right.scatter([0], [0], s=120, color='#132a38', zorder=5)
    right.scatter([1], [0], s=230, marker='x', lw=4, color='#ba5237', zorder=5)
    right.scatter([1], [1], s=100, color='#167194', zorder=5)
    right.annotate('Root 0: met at u = 0;\nratio cancels it', xy=(0, 0), xytext=(-1.4, 0.57), fontsize=18, arrowprops={'arrowstyle': '->', 'color': '#132a38'}, color='#132a38')
    right.annotate('Root 1: never met', xy=(1, 0), xytext=(0.43, -0.7), fontsize=18, arrowprops={'arrowstyle': '->', 'color': '#ba5237'}, color='#ba5237')
    right.annotate('$z(1)=1+i$', xy=(1, 1), xytext=(0.17, 1.55), fontsize=20, arrowprops={'arrowstyle': '->', 'color': '#167194'}, color='#167194')
    right.set_xlim(-1.55, 1.55)
    right.set_ylim(-2.2, 2.2)
    right.set_xlabel('$\\operatorname{Re}z$')
    right.set_ylabel('$\\operatorname{Im}z$')
    right.set_title('Denominator zeros of $C(z)=z(1-z)$', pad=22)
    right.grid(True, color='#d7dedf', alpha=0.65)
    right.legend(loc='lower left', framealpha=0.95)
    fig.text(0.06, 0.222, '$P=(\\xi_1-i\\xi_2)^6-\\xi_1^5,\\quad Q=\\xi_1^6,\\quad N=e_2$', fontsize=22, color='#132a38')
    fig.text(0.06, 0.17, '$\\zeta=(u^{-4},-iu^{-4}),\\ T=u^{-3},\\ K=u^{-2}$', fontsize=22, color='#132a38')
    fig.text(0.06, 0.118, '$c=-u^{20},\\ b=u^{24},\\quad K(cP-bQ)=z^6$', fontsize=22, color='#132a38')
    fig.text(0.545, 0.222, '$c_0=u(1-u),\\quad b_0=u^2$', fontsize=22, color='#132a38')
    fig.text(0.545, 0.17, '$c_1=(u+iu^3)(1-u-iu^3)$', fontsize=22, color='#132a38')
    fig.text(0.545, 0.118, '$b_0/c_1=\\dfrac{u}{(1+iu^2)(1-u-iu^3)}$', fontsize=22, color='#132a38')
    fig.text(0.045, 0.045, 'Equations (14)–(22), (25)–(28). Exact algebraic models; no physical solution is sampled.', fontsize=15, color='#41505a')
    fig.savefig(dest / f'{STEM}.png', dpi=100, metadata={'Software': 'Original scientific figure; GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    fig.savefig(dest / f'{STEM}.svg', metadata={'Date': None, 'Creator': 'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
    plt.close(fig)
    data = {'schema': 'exact-rational-frequency-and-pole-removal-model-figure/v1', 'dimensions': [2400, 1200], 'lesson_equations': ['(14)-(22)', '(25)-(28)'], 'frequency_model': {'dimension': 2, 'N': [0, 1], 'P': '(xi1-i*xi2)^6-xi1^5', 'Q': 'xi1^6', 'zeta': ['u^-4', '-i*u^-4'], 'T': 'u^-3', 'K': 'u^-2', 'lambda': 'u^-4', 'c': '-u^20', 'b': 'u^24', 'r': 'z^6', 'exponents': {'kappa': 2, 'tau': 3, 'Lambda': 4}, 'u_domain': ['1/128', '1/4'], 'logarithmic_sample_count': 257, 'exact_ratios': {'K/T': 'u', 'T/lambda': 'u', 'lambda/(T*K)': 'u'}, 'normalized_P_error': 'u^2', 'coefficient_ratio_modulus': 'u^4'}, 'pole_model': {'c0': 'u*(1-u)', 'b0': 'u^2', 'z_h': 'u+i*u^3', 'h': 1, 'v': 3, 'C_roots': [[0, 0], [1, 0]], 'parameter_domain': ['-5/4', '5/4'], 'linear_sample_count': 501, 'root0_met_only_at_parameter0': True, 'root0_cancelled_in_ratio': True, 'root1_never_met_at_real_parameter': True, 'z_at_parameter1': [1, 1], 'ratio': 'u/((1+i*u^2)*(1-u-i*u^3))', 'distinct_from_frequency_model': True}, 'plots_are_numerical_evaluations_of_stated_exact_models': True, 'physical_space_solution_sampled': False, 'periodic_seed_constructed': False, 'source_comparison': 'H2 Lemma13.6.13', 'author': 'GPT-6.1 Sol (OpenAI)', 'license': 'CC0-1.0'}
    (dest / f'{STEM}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'destination': str(dest), 'dimensions': [2400, 1200]}))
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir')
    run(parser.parse_args().output_dir)
