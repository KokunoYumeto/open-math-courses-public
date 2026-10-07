"""Reproduce the exact local-cutoff and Newtonian-potential figures (CC0)."""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Patch
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none',
                     'svg.hashsalt': 'AN02-L131-local-potentials',
                     'axes.spines.top': False, 'axes.spines.right': False})
BLUE, ORANGE, GREEN = '#2166ac', '#df7c24', '#188557'
ATOMS = [(-1.2, .3, 1), (.8, -.7, 2), (2.5, .8, 1), (-2.8, -1.5, 1)]

def cutoff(radius):
    t = (np.asarray(radius, dtype=float) - 2.2) / .8
    result = np.zeros_like(t)
    result[t <= 0] = 1.
    interior = (t > 0) & (t < 1)
    u = t[interior]
    b0, b1 = np.exp(-1/u), np.exp(-1/(1-u))
    result[interior] = b1 / (b0 + b1)
    return result

def kernel(n, r):
    r = np.asarray(r, dtype=float)
    if n == 2:
        return np.log(r)/(2*np.pi)
    s = 2*np.pi**(n/2)/math.gamma(n/2)
    return -r**(2-n)/((n-2)*s)

def ball_potential(n, r, a=1.):
    r = np.asarray(r, dtype=float)
    if n == 2:
        inside = np.log(a)/(2*np.pi)+(r*r-a*a)/(4*np.pi*a*a)
    else:
        s = 2*np.pi**(n/2)/math.gamma(n/2)
        inside = (r*r-n*a*a/(n-2))/(2*s*a**n)
    result = inside.copy()
    exterior = r >= a
    result[exterior] = kernel(n, r[exterior])
    return result

weights = [float(cutoff(math.hypot(x,y))) for x,y,m in ATOMS]
geometry = {
    'dimension': 2, 'X_radius': 3.6, 'Y_radius': 2.,
    'cutoff_one_radius': 2.2, 'cutoff_zero_radius': 3.,
    'cutoff_formula': 'S((r-2.2)/0.8), S(t)=b(1-t)/(b(t)+b(1-t)); b(t)=exp(-1/t) for t>0, zero otherwise',
    'atoms': [{'label': chr(65+i), 'xy': [x,y], 'mass': m,
               'radius_squared_exact_decimal': str(round(x*x+y*y,2)),
               'retained_fraction': w, 'retained_mass': m*w,
               'remainder_mass': m*(1-w)} for i,((x,y,m),w) in enumerate(zip(ATOMS,weights))],
    'bubble_area_rule': 'outer area=pi*(0.19)^2*mass; blue inner area=pi*(0.19)^2*retained_mass; orange annulus area=pi*(0.19)^2*remainder_mass',
    'kernel_convention': 'Delta E_n=delta_0; E_2=log(r)/(2*pi); E_n=-r^(2-n)/((n-2)*s_n), n>2',
    'ball_average_radius': 1,
    'integrability_panel': {'dimension':3,'p':[2,3,4], 'epsilon_range':[1e-4,.9],
                            'J2':'1-epsilon','J3':'log(1/epsilon)','J4':'1/epsilon-1',
                            'kernel_integral_multiplier':'(4*pi)^(1-p)'},
    'proof_locators': ['NP4', 'NP6', 'NP7', 'NP10 Examples 1-3']
}
(OUT/'geometry.json').write_text(json.dumps(geometry, indent=2)+'\n',encoding='utf-8')

fig = plt.figure(figsize=(13.5,7.6), layout='constrained')
grid = fig.add_gridspec(2,3,width_ratios=[1,1,.9],height_ratios=[1,1])
ax = fig.add_subplot(grid[:, :2]); profile=fig.add_subplot(grid[0,2]); mass=fig.add_subplot(grid[1,2])
ax.set_aspect('equal'); ax.set_xlim(-4.1,4.1); ax.set_ylim(-3.95,4.2)
ax.add_patch(Circle((0,0),2.2,facecolor='#edf4fa',edgecolor='none'))
for radius,color,style,width in [(3.6,'#333333','-',1.8),(3.,'#777777','--',1.3),
                                  (2.2,BLUE,':',1.5),(2.,GREEN,'-',2.)]:
    ax.add_patch(Circle((0,0),radius,fill=False,edgecolor=color,linestyle=style,linewidth=width))
offsets=[(-.2,.68),(.58,-.38),(-.8,.62),(-.34,-.77)]
for i,((x,y,m),w,(dx,dy)) in enumerate(zip(ATOMS,weights,offsets)):
    outer=.19*np.sqrt(m); inner=.19*np.sqrt(m*w)
    if w < 1:
        ax.add_patch(Circle((x,y),outer,facecolor=ORANGE,edgecolor='#555555',linewidth=.6,zorder=4))
    if w > 0:
        ax.add_patch(Circle((x,y),inner,facecolor=BLUE,edgecolor='#555555',linewidth=.6,zorder=5))
    ax.annotate(f'{chr(65+i)}: ({x:g}, {y:g})\nmass {m}',xy=(x,y),xytext=(x+dx,y+dy),
                ha='center',va='center',fontsize=10,
                arrowprops={'arrowstyle':'-','color':'#555555','linewidth':.8},
                bbox={'facecolor':'white','edgecolor':'none','alpha':.86,'pad':2},zorder=6)
ax.text(0,3.75,r'$X=B(0,3.6)$',ha='center',fontsize=12)
ax.text(.1,-1.7,r'$Y=B(0,2)$',color=GREEN,ha='center',fontsize=11,
        bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
ax.text(-2.3,2.46,r'$\chi=0$ for $r\geq3$',color='#555555',ha='center',fontsize=10,
        bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
ax.text(-1.02,-1.05,r'$\chi=1$ for $r\leq2.2$',color=BLUE,ha='center',fontsize=10)
ax.text(0,-3.8,'The remainder potential is harmonic on Y.',ha='center',fontsize=12,color=GREEN)
ax.set_xlabel('$x_1$');ax.set_ylabel('$x_2$')
ax.set_title('Local cutoff: mass near Y + mass outside Y',fontsize=15,pad=16)
ax.grid(alpha=.1)
r=np.linspace(0,3.6,600)
profile.plot(r,cutoff(r),color=BLUE,linewidth=2.3)
profile.axvline(2.,color=GREEN,linewidth=1.6);profile.axvline(2.2,color=BLUE,linestyle=':')
profile.axvline(3.,color='#777777',linestyle='--')
profile.set_xlim(0,3.6);profile.set_ylim(-.06,1.18)
profile.set_xticks([0,2.2,3,3.6]);profile.tick_params(axis='x',labelsize=9)
profile.set_yticks([0,.5,1]);profile.set_xlabel('radius r');profile.set_ylabel(r'$\chi(r)$')
profile.set_title('Exact smooth cutoff',fontsize=13);profile.grid(alpha=.15)
profile.annotate('0.2 buffer',xy=(2.1,1.07),xytext=(.6,.68),color=GREEN,fontsize=10,
                 arrowprops={'arrowstyle':'->','color':GREEN})
retained=np.array([m*w for (x,y,m),w in zip(ATOMS,weights)])
remainder=np.array([m for x,y,m in ATOMS])-retained
mass.bar(np.arange(4),retained,color=BLUE,label=r'$\chi\mu$')
mass.bar(np.arange(4),remainder,bottom=retained,color=ORANGE,label=r'$(1-\chi)\mu$')
mass.set_xticks(range(4),list('ABCD'));mass.set_ylabel('mass');mass.set_ylim(0,2.52)
mass.set_title('Retained and remaining mass',fontsize=13)
mass.legend(loc='upper right',fontsize=10,frameon=False)
mass.grid(axis='y',alpha=.15)
for i in range(4):
    mass.text(i,retained[i]+remainder[i]+.06,f'{retained[i]+remainder[i]:g}',ha='center',fontsize=10)
for ext in ['png','svg']:
    fig.savefig(OUT/f'local-cutoff.{ext}',dpi=165,metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0-1.0', **({'Date':None} if ext=='svg' else {})})
plt.close(fig)

fig,axes=plt.subplots(1,3,figsize=(15,5.3),layout='constrained')
r=np.linspace(.015,2.3,850); r0=np.linspace(0,2.3,850)
for ax,n in zip(axes[:2],[2,3]):
    ax.axvspan(0,1,color='#edf4fa',zorder=0)
    ax.plot(r,kernel(n,r),color='#555555',linewidth=2,label=rf'$E_{n}(r)$')
    ax.plot(r0,ball_potential(n,r0),color=BLUE,linewidth=2.5,label=rf'$E_{n}*q_1$')
    ax.axvline(1,color='#888888',linestyle=':',linewidth=1)
    ax.set_xlim(0,2.3);ax.set_ylim((-.62,.17) if n==2 else (-.65,.045))
    ax.set_xlabel('radius r');ax.set_ylabel('potential')
    ax.set_title(f'Dimension {n}: unit-ball average',fontsize=13)
    ax.legend(loc='upper right',frameon=False,fontsize=11);ax.grid(alpha=.16)
    ax.annotate(r'$E_n(r)\to-\infty$',xy=(.028, -.54),xytext=(.30,-.40),fontsize=10,
                arrowprops={'arrowstyle':'->','color':'#555555'})
    ax.text(.34, .94, 'averaging ball: r ≤ 1',transform=ax.transAxes,color=BLUE,ha='center',fontsize=10)
eps=np.geomspace(1e-4,.9,800);ax=axes[2]
for p,value,color in [(2,1-eps,GREEN),(3,np.log(1/eps),ORANGE),(4,1/eps-1,'#8a3a9b')]:
    ax.plot(eps,value,color=color,linewidth=2.2,label=rf'$p={p}$')
ax.set_xscale('log');ax.set_yscale('log');ax.invert_xaxis()
ax.set_xlabel(r'inner radius $\varepsilon$ (decreasing →)')
ax.set_ylabel(r'$J_p(\varepsilon)=\int_{\varepsilon}^{1}r^{2-p}\,dr$')
ax.set_title('Dimension 3: sharp endpoint',fontsize=13)
ax.legend(loc='upper left',frameon=False);ax.grid(which='both',alpha=.15)
ax.text(.50,.05,r'$p=3$ is the logarithmic divergence',transform=ax.transAxes,ha='center',fontsize=10)
for ext in ['png','svg']:
    fig.savefig(OUT/f'kernel-integrability.{ext}',dpi=165,metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0-1.0', **({'Date':None} if ext=='svg' else {})})
plt.close(fig)
print(json.dumps({'figures': ['local-cutoff.png','local-cutoff.svg','kernel-integrability.png','kernel-integrability.svg'],
                  'cutoff_weights': weights},indent=2))
