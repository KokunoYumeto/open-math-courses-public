"""Original CC0 numerical illustration for the explicit-formula lesson.

The zeros and b were recomputed with mpmath at 32 digits in the accompanying
writer check; the decimal constants here permit a small reproducible figure.
The direct curve is the right-continuous psi, not its half-weight at jumps.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

dest=Path(__file__).resolve().parent.parent
zeros=np.array([6.0209489046975966549,10.2437703041665545521,
12.9880980123124225075,16.3426071045872221950,18.2919931961235348385,
21.4506113439834604972,23.2783765204595315318,25.7287564250887275673,
28.3596343430253277857,29.6563840145931527218])
b=0.78318878541373
def character(n):return 0 if n%2==0 else (1 if n%4==1 else -1)
def von_mangoldt(n):
    p=next((p for p in range(2,math.isqrt(n)+1) if n%p==0),n)
    m=n
    while m%p==0:m//=p
    return math.log(p) if m==1 else 0
integers=np.arange(2,101)
direct=np.cumsum([character(int(n))*von_mangoldt(int(n)) for n in integers])
x=np.linspace(2,100,4000);rho=.5+1j*zeros
approx=-2*np.real(np.exp(np.log(x[:,None])*rho)/rho).sum(axis=1)-b+np.arctanh(1/x)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'path'})
fig,ax=plt.subplots(figsize=(11,5.7),layout='constrained')
fig.patch.set_facecolor('#faf9f4');ax.set_facecolor('#faf9f4')
ax.step(integers,direct,where='post',color='#173f4f',lw=1.65,label=r'Direct $\psi(x,\chi_{-4})$')
ax.plot(x,approx,color='#b65437',lw=1.6,label='Ten zero pairs, with constant and trivial-zero terms')
ax.axhline(0,color='#60737a',lw=.7,alpha=.7)
ax.set(xlim=(2,100),xlabel=r'$x$',ylabel='Character-weighted prime-power sum')
ax.set_title('A finite explicit formula for the character modulo 4',loc='left',pad=14,fontweight='bold')
ax.grid(axis='y',alpha=.15);ax.legend(loc='lower left',frameon=True,fontsize=11)
ax.spines[['top','right']].set_visible(False)
fig.savefig(dest/'beta-explicit-formula.png',dpi=170)
fig.savefig(dest/'beta-explicit-formula.svg')
print('Saved original CC0 explicit-formula diagram.')
