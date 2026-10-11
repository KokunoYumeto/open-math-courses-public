# GG_FIGURE_SOURCE
import io, base64, hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.fonttype']='none'
matplotlib.rcParams['svg.hashsalt']='ncg-global-curved-graph-20261010'
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def pack(fig, key):
    out = io.BytesIO()
    fig.savefig(out, format='png', dpi=145, facecolor='white', bbox_inches='tight')
    name={'FIGURE1':'global-curved-rank-example','FIGURE2':'global-curved-graph-carrier'}[key]
    fig.savefig(Path(__file__).resolve().parents[2]/'figures'/(name+'.svg'),format='svg',facecolor='white',bbox_inches='tight',metadata={'Date':None})
    plt.close(fig)
    raw = out.getvalue()
    return {'key': key, 'mime': 'image/png', 'sha256': hashlib.sha256(raw).hexdigest(),
            'data': base64.b64encode(raw).decode('ascii')}

rendered_figures = []
r = np.linspace(-.999, .999, 2001)
s = np.maximum(np.abs(r)-.25, 0.)
f = np.zeros_like(r)
active = s > 0
f[active] = np.exp(-1/s[active]**2)
a = np.exp(f)
alpha = (1-r*r)/100
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.1))
ax = axes[0]
ax.plot(r, a, color='#216f9c', lw=2.2, label=r'$a(r)=\exp f(r)$')
ax.axvspan(-.25, .25, color='#d9eedd', zorder=0)
for seam in [-.25, .25]:
    ax.axvline(seam, color='#52636b', ls='--', lw=1)
ax.set(xlim=(-1,1), ylim=(.960,1.215), xlabel='Original radial coordinate r', ylabel='Angular metric factor a(r)',
       title=r'$g=dr^2+a(r)^2d\theta^2$, $\theta\in\mathbb{R}/2\pi\mathbb{Z}$')
ax.text(0, 1.14, 'Full local Killing rank 3\nonly for |r| < 1/4', ha='center', va='center', fontsize=10)
ax.text(-.67, 1.055, 'Rank 1', ha='center', fontsize=10)
ax.text(.67, 1.055, 'Rank 1', ha='center', fontsize=10)
ax.text(0, .975, 'Both seams have rank 1', ha='center', fontsize=9)
ax.legend(loc='upper center', fontsize=9)
ax.grid(alpha=.18)
ax = axes[1]
ax.plot(r, alpha, color='#b76a28', lw=2.2)
ax.axvline(-1, color='#9b4242', ls=':', lw=1.5)
ax.axvline(1, color='#9b4242', ls=':', lw=1.5)
ax.plot([-1,1], [0,0], 'o', mfc='white', mec='#9b4242', ms=7, clip_on=False)
ax.set(xlim=(-1,1), ylim=(0,.0115), xlabel='Original r; endpoints omitted', ylabel='Positive speed on T',
       title=r'$\alpha(r)=(1-r^2)/100$')
ax.text(0, .0062, r'$\rho=1-|r|,\quad 0<\alpha\leq\rho/50$', ha='center', fontsize=11)
ax.text(0, .0039, r'$\int_0^r\alpha(t)^{-1}dt=100\,\operatorname{artanh}(r)$', ha='center', fontsize=11)
ax.text(0, .0017, 'Complete speed realization\non the same original incomplete metric', ha='center', fontsize=10)
ax.grid(alpha=.18)
fig.tight_layout()
rendered_figures.append(pack(fig, 'FIGURE1'))

fig, ax = plt.subplots(figsize=(11.6, 5.0))
ax.set(xlim=(0,12), ylim=(0,5.4))
ax.axis('off')
boxes = [
 (.2, 3.45, 3.25, 1.45, 'Original global action', r'$G=\Gamma\ltimes(T,g)$'+'\n'+r'$S_{\rm inv}$, degree $q$, original disk $b_U$'),
 (4.1, 3.45, 3.55, 1.45, 'Actual reduced multiplication', r'$H_0=H_\kappa\otimes L^2(T,S_{\rm inv})$'+'\n'+r'$\mathcal{D}=D_\kappa+\Gamma_\kappa N_\alpha$'),
 (8.3, 3.45, 3.45, 1.45, 'Entire physical graph', r'$H_{\rm graph}=E_Z\otimes_{A_r}H_0$'+'\n'+r'$F_{\rm graph}=P(1\otimes F_0)P$'),
]
for x,y,w,h,title,body in boxes:
    ax.text(x+w/2, y+h/2, title+'\n\n'+body, ha='center', va='center', fontsize=11,
            bbox=dict(boxstyle='round,pad=.65', facecolor='#eef5f8', edgecolor='#41677a'))
for x1,x2 in [(3.45,4.1),(7.65,8.3)]:
    ax.add_patch(FancyArrowPatch((x1,4.18),(x2,4.18),arrowstyle='->',mutation_scale=16,lw=1.7,color='#41677a'))
ax.text(3.85, 3.04, 'GG.17–GG.21\nActual coaction norm', ha='center', fontsize=9)
ax.text(8., 3.04, 'GG.33–GG.36\nFull module frame', ha='center', fontsize=9)
ax.text(5.95, 1.95, r'$\operatorname{Dom}\mathcal{D}=\operatorname{Dom}(D_\kappa\otimes1)\cap\operatorname{Dom}(1\otimes N_\alpha)$',
        ha='center', fontsize=13, bbox=dict(boxstyle='round,pad=.55',fc='#f4efe5',ec='#987545'))
ax.text(5.95, .92, r'$F_{\rm graph}T_\xi e^{itf}v\sim T_\xi e^{itf}\Gamma_\kappa\,iC(df)/|df|_g$', ha='center', fontsize=13)
ax.text(5.95, .36, 'GG.39: norm difference tends to zero on every actual compact physical column.  Original disk pairing: +1.',
        ha='center', fontsize=10)
rendered_figures.append(pack(fig, 'FIGURE2'))
from pathlib import Path
output=Path(__file__).resolve().parents[2]/'figures'
for slug,figure in zip(['global-curved-rank-example','global-curved-graph-carrier'],rendered_figures):
    (output/(slug+'.png')).write_bytes(base64.b64decode(figure['data']))
