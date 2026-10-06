"""Exact sections of the homogenized moving oscillator; original source, CC0.

Each circle is a level set in phase space, not a spatial wavefunction.
Matplotlib's mathtext draws labels; no TeX compiler is used.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig, axes = plt.subplots(1, 3, figsize=(11, 4.3), layout='constrained')
angle = np.linspace(0, 2*np.pi, 600)
for ax, t in zip(axes, [0, 1, 2]):
    center = np.array([-t, -t/2])
    ax.plot(center[0]+np.cos(angle), center[1]+np.sin(angle),
            color='#13745b', lw=2)
    ax.scatter(*center, color='#103b51', s=35, zorder=4)
    ax.annotate(f'center ({center[0]:g}, {center[1]:g})', xy=center,
                xytext=(-3.1, 1.3), fontsize=10,
                arrowprops={'arrowstyle':'->','color':'#103b51'})
    ax.set(xlim=(-3.3,1.5), ylim=(-2.3,1.8), xlabel=r'$y$', ylabel=r'$\eta$')
    ax.set_title(r'$t='+str(t)+r'$: $(y+t)^2+(\eta+t/2)^2=1$')
    ax.set_aspect('equal')
    ax.axhline(0, color='#87909a', lw=.7)
    ax.axvline(0, color='#87909a', lw=.7)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.13)
fig.suptitle(r'Exact phase-space slices of $\mathcal{Q}=(y+t)^2+(\eta+t/2)^2$, independent of $\tau$', fontsize=14)
fig.savefig(Path(__file__).with_name('homogeneous-slices.png'), dpi=170,
            metadata={'Software':'Matplotlib; original course figure, CC0'})
plt.close(fig)
