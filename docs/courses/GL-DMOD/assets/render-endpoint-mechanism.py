"""Render the exact proof dependencies and signs of E.2--E.5.

This is a mechanism diagram for arbitrary rank, not a geometric drawing of a
particular flag or a numerical approximation. Run with the local Python runtime.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

out = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(15, 9), dpi=180)
fig.patch.set_facecolor('#f8fafc')
ax.set_xlim(0, 15)
ax.set_ylim(0, 9)
ax.axis('off')

def box(x, y, w, h, title, lines, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
        facecolor='white', edgecolor=color, linewidth=2))
    ax.text(x + w/2, y + h - 0.27, title, ha='center', va='center',
        fontsize=14, fontweight='bold', color=color)
    for k, line in enumerate(lines):
        ax.text(x + w/2, y + h - 0.72 - 0.40*k, line,
            ha='center', va='center', fontsize=12, color='#172033')

def arrow(start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>',
        mutation_scale=18, color='#64748b', linewidth=1.8))

ax.text(7.5, 8.65, 'Both translation endpoints for arbitrary complex parameters',
    ha='center', fontsize=19, fontweight='bold', color='#172033')
ax.text(7.5, 8.20,
    r'$Q=\mathbb{Z}\Phi,\quad Q_+=\sum_i\mathbb{Z}_{\geq0}\alpha_i,'
    r'\quad \tau(h_\alpha)\notin\mathbb{Z}_{>0}\ (\alpha\in\Phi^+)$',
    ha='center', fontsize=13, color='#334155')

box(0.35, 5.9, 6.55, 1.8, 'E.2  Complex affine stabilizer', [
    r'$\tau=x+iy\in\mathfrak{h}^*_{\mathbb{C}}$',
    r'$w\tau-\tau\in Q\ \Longleftrightarrow\ w\in W_{\tau,\mathbb{Z}}$',
    r'$W_{\tau,\mathbb{Z}}=\langle s_\alpha:\tau(h_\alpha)\in\mathbb{Z}\rangle$'], '#315aa6')
box(8.05, 5.9, 6.55, 1.8, 'E.3  Integral-root orbit order', [
    r'$w\tau-\tau=-\sum_j\tau(h_{\delta_j})\beta_j\in Q_+$',
    r'$w\in W_{\tau,\mathbb{Z}},\quad\delta_j,\beta_j\in\Phi^+_{\tau,\mathbb{Z}}$',
    r'$\tau(h_\alpha)\ne0\ \forall\alpha:\quad w\ne1\Rightarrow w\tau\ne\tau$'], '#315aa6')
arrow((6.99, 6.8), (7.93, 6.8))

box(0.35, 2.25, 6.55, 2.55, r'E.4  Highest weight of $F_\mu$', [
    r'$\tau-\mu+\nu=w\tau$',
    r'$w\tau-\tau=\nu-\mu\in -Q_+$',
    r'$w\tau-\tau\in Q_+\cap(-Q_+)=\{0\}$',
    r'$\nu=\mu\quad(\dim F_{\mu,\mu}=1)$'], '#166c4f')
box(8.05, 2.25, 6.55, 2.55, r'E.5  Lowest weight of $F_{-w_0\mu}$', [
    r'$\tau+\nu^{\prime}=w(\tau-\mu)$',
    r'$w^{-1}\nu^{\prime}+\mu=\tau-w^{-1}\tau\in Q_+\cap(-Q_+)$',
    r'$\tau(h_\alpha)\ne0\ \forall\alpha\Rightarrow w=1$',
    r'$\nu^{\prime}=-\mu\quad(\dim F^{\prime}_{-\mu}=1)$'], '#166c4f')
arrow((3.6, 5.80), (3.6, 4.94))
arrow((11.3, 5.80), (11.3, 4.94))

ax.text(7.5, 1.56,
    r'$\mu=N\,2\rho\in X^*(T),\quad N\geq1,\quad \mu(h_i)=2N>0$',
    ha='center', fontsize=14, color='#172033')
ax.text(7.5, 1.07,
    'Both endpoint panels use E.2 and E.3. Every nonintegral root pairing may be complex.',
    ha='center', fontsize=12, color='#334155')
ax.text(7.5, 0.58,
    'Exact proof locators: BB §5A.8, E.2–E.5.  Earlier weight proof: BB H.5.',
    ha='center', fontsize=11, color='#475569')
ax.text(7.5, 0.22,
    'Free comparison: Miličić, Localization and Representation Theory of Reductive Lie Groups, Chapter 2 §2.',
    ha='center', fontsize=10, color='#475569')
fig.savefig(out / 'endpoint-orbit-mechanism.png', bbox_inches='tight', pad_inches=0.2)
fig.savefig(out / 'endpoint-orbit-mechanism.svg', bbox_inches='tight', pad_inches=0.2)
plt.close(fig)
