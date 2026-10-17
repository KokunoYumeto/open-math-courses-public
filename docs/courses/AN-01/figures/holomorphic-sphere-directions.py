"""Exact multipliers and boundary orientation for AN01-U077.

Written by GPT-6 Astra (OpenAI), Ultra. CC0.
Requires NumPy and Matplotlib. Run this file to reproduce both figures.
The sampled curves illustrate the exact identity in equation (26).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
plt.rcParams.update({'font.size': 12, 'svg.fonttype': 'none'})
fig, (ax, plane) = plt.subplots(1, 2, figsize=(12, 5.3), layout='constrained')
xi = np.linspace(-4, 4, 1001)
plus = 1 / (1 + np.exp(2 * xi))
minus = 1 / (1 + np.exp(-2 * xi))
ax.plot(xi, plus, lw=2.6, color='#1367a8', label=r'$m_{+1}(\xi)=1/(1+e^{2\xi})$')
ax.plot(xi, minus, lw=2.6, color='#c45428', label=r'$m_{-1}(\xi)=1/(1+e^{-2\xi})$')
ax.axhline(1, color='#555555', ls=':', lw=1.4, label=r'$m_{+1}+m_{-1}=1$')
ax.set(xlabel=r'Frequency $\xi$', ylabel='Multiplier value', xlim=(-4, 4), ylim=(-.04, 1.12), title='Two boundary multipliers in dimension one')
ax.grid(alpha=.18)
ax.text(-3.8, .76, r'$m_{+1}=1/(1+e^{2\xi})$', color='#1367a8', fontsize=12)
ax.text(.55, .23, r'$m_{-1}=1/(1+e^{-2\xi})$', color='#a73e19', fontsize=12)
ax.text(-1.6, 1.04, r'$m_{+1}+m_{-1}=1$', color='#444444', fontsize=12)
theta = np.linspace(0, 2*np.pi, 721)
plane.plot(np.cos(theta), np.sin(theta), color='#526579', lw=2)
plane.fill(np.cos(theta), np.sin(theta), color='#e8f0f7', alpha=.7)
plane.axhline(0, color='#aab4bf', lw=.8)
plane.axvline(0, color='#aab4bf', lw=.8)
omega = np.array([3/5, 4/5])
plane.annotate('', xy=omega, xytext=(0, 0), arrowprops={'arrowstyle': '->', 'color': '#1367a8', 'lw': 2.5})
plane.scatter(*omega, color='#1367a8', s=45, zorder=4)
plane.annotate(r'$\omega=(3/5,4/5)$', xy=omega, xytext=(-.12, 1.19), fontsize=12, arrowprops={'arrowstyle': '-', 'color': '#526579'})
plane.annotate('', xy=-1.17*omega, xytext=(0, 0), arrowprops={'arrowstyle': '->', 'color': '#c45428', 'lw': 2.5, 'linestyle': '--'})
plane.text(-1.3, -1.18, r'Covector ray $-t\omega$, $t>0$', color='#9b3b17', fontsize=12)
plane.text(.20, -.20, 'Imaginary unit ball', fontsize=11)
plane.set(xlabel='First coordinate', ylabel='Second coordinate', xlim=(-1.38, 1.38), ylim=(-1.35, 1.38), aspect='equal', title='Boundary point and opposite covector')
plane.set_xticks([-1, 0, 1]); plane.set_yticks([-1, 0, 1])
fig.savefig(out/'holomorphic-sphere-directions.png', dpi=170, metadata={'Software': 'Matplotlib; original AN01-U077 illustration; CC0'})
svg = out/'holomorphic-sphere-directions.svg'
fig.savefig(svg, metadata={'Creator': 'GPT-6 Astra (OpenAI), Ultra; CC0', 'Date': None})
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8', newline='\n')
plt.close(fig)
