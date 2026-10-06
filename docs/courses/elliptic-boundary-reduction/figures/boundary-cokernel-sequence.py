"""Exact quotient maps proved in the boundary Fredholm lesson, BF51--BF53."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(15, 5.5), dpi=160)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 15)
ax.set_ylim(0, 5.5)
ax.axis('off')
ax.text(7.5, 5.03, 'The equation, combined data and boundary cokernels',
        ha='center', va='center', fontsize=21, color='#172b4d')
rows = [
    (1.1, r'$C_P=\mathsf{F}/\mathrm{ran}\,P_B$', 'Homogeneous boundary domain'),
    (5.4, r'$C_A=(\mathsf{F}\oplus\mathsf{G})/\mathrm{ran}\,A_m$', 'Equation and boundary data'),
    (9.7, r'$C_B=\mathsf{G}/\mathrm{ran}\,B$', 'Boundary data alone'),
]
for x, formula, label in rows:
    ax.add_patch(FancyBboxPatch((x, 2.5), 3.65, 1.45,
        boxstyle='round,pad=0.04,rounding_size=0.1',
        facecolor='#edf4ff', edgecolor='#275dad', linewidth=1.6))
    ax.text(x+1.825, 3.46, formula, ha='center', va='center', fontsize=16)
    ax.text(x+1.825, 2.88, label, ha='center', va='center', fontsize=12, color='#344563')
arrows=[(0.45, 1.0), (4.83, 5.3), (9.13, 9.6), (13.45, 14.23)]
for start, end in arrows:
    ax.annotate('', xy=(end, 3.22), xytext=(start, 3.22),
        arrowprops=dict(arrowstyle='->', lw=1.7, color='#172b4d'))
ax.text(0.2, 3.22, r'$0$', ha='center', va='center', fontsize=20)
ax.text(14.5, 3.22, r'$0$', ha='center', va='center', fontsize=20)
ax.text(5.075, 4.18, r'$j([f])=[(f,0)]$', ha='center', fontsize=16)
ax.text(9.375, 4.18, r'$\pi([(f,g)])=[g]$', ha='center', fontsize=16)
ax.text(7.5, 1.79, r'$\ker\pi=\mathrm{ran}\,j$', ha='center', fontsize=19, color='#172b4d')
ax.text(7.5, 1.06, r'$\mathrm{ind}\,P_B=\mathrm{ind}\,A_m+\dim C_B$',
        ha='center', fontsize=21, color='#172b4d')
ax.text(7.5, 0.39, 'Original targets retained; all maps and exactness proved in BF51–BF53.',
        ha='center', fontsize=13, color='#344563')
fig.tight_layout(pad=0.2)
fig.savefig(root/'boundary-cokernel-sequence.svg', facecolor='white')
fig.savefig(root/'boundary-cokernel-sequence.png', facecolor='white')
plt.close(fig)
