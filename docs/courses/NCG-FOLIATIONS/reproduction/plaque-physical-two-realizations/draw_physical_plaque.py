"""Original CC0 diagram of the physical two-realization plaque estimate.

Run from any working directory. The PNG and SVG go into ../../figures.
Bundled unmodified DejaVu fonts and software keep their own notice terms.
"""
from pathlib import Path
import argparse, tempfile, os
HERE = Path(__file__).resolve().parent
CACHE = tempfile.TemporaryDirectory(prefix='plaque-figure-')
os.environ['MPLCONFIGDIR'] = CACHE.name
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.ticker import NullFormatter
import numpy as np

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=HERE.parents[1] / 'figures')
OUT = parser.parse_args().output
OUT.mkdir(parents=True, exist_ok=True)
REGULAR = HERE / 'fonts' / 'DejaVuSans.ttf'
BOLD = HERE / 'fonts' / 'DejaVuSans-Bold.ttf'
FP = FontProperties(fname=str(REGULAR))
FB = FontProperties(fname=str(BOLD))
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'svg.fonttype': 'path', 'svg.hashsalt': 'physical-plaque-v1',
                     'axes.unicode_minus': False, 'savefig.facecolor': '#ffffff'})
BLUE, TEAL, ORANGE, INK = '#2457a7', '#087f8c', '#c04e19', '#183046'

def txt(ax, x, y, value, *, size=13, color=INK, bold=False, ha='left', va='center'):
    return ax.text(x, y, value, fontsize=size, color=color,
                   fontproperties=FB if bold else FP, ha=ha, va=va)

def box(ax, x, y, w, h, title, subtitle, color):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle='round,pad=0.012,rounding_size=0.012',
                 linewidth=1.5, edgecolor=color, facecolor='#f4f8fb'))
    txt(ax, x+w/2, y+h*.65, title, size=16, color=color, bold=True, ha='center')
    txt(ax, x+w/2, y+h*.28, subtitle, size=11.5, ha='center')

fig = plt.figure(figsize=(14, 9.3))
gs = fig.add_gridspec(2, 2, height_ratios=[1.04, 1],
                      left=.052, right=.97, bottom=.09, top=.90,
                      hspace=.24, wspace=.25)
a = fig.add_subplot(gs[0, :]); a.set_axis_off(); a.set_xlim(0,1); a.set_ylim(0,1)
txt(a, 0, 1.04, 'A  The same actual kernel, with correctly typed local boundaries',
    size=15, bold=True)
positions=[.015,.285,.555,.825]
titles=['J^r on the cover','direct sum I^r','direct sum O^r′','J^r′ on the cover']
subs=['physical global input','all lifted plaque inputs','all lifted plaque outputs','physical global output']
colors=[BLUE,TEAL,TEAL,BLUE]
for x,title,sub,color in zip(positions,titles,subs,colors):
    box(a,x,.70,.16,.23,title,sub,color)
for n,label,bound in [(0,'restriction R_r','norm ≤ 1'),
                      (1,'block sum of P_u','norm ≤ M'),
                      (2,'extension E_r′','norm ≤ 1')]:
    left=positions[n]+.173; right=positions[n+1]-.015
    a.add_patch(FancyArrowPatch((left,.81),(right,.81),arrowstyle='-|>',
                               mutation_scale=17,color=INK,linewidth=1.6))
    txt(a,(left+right)/2,.62,label,size=11.5,ha='center')
    txt(a,(left+right)/2,.55,bound,size=11.5,ha='center')
txt(a,.045,.42,'Order',bold=True,size=13)
txt(a,.20,.42,'Input I^r',bold=True,size=13)
txt(a,.51,.42,'Output O^r',bold=True,size=13)
txt(a,.045,.29,'r ≥ 0',size=13)
txt(a,.20,.29,'M^r: maximal physical jets / interpolation',size=12)
txt(a,.51,.29,'S^r: compact-test closure / interpolation',size=12)
txt(a,.045,.17,'r = −s < 0',size=13)
txt(a,.20,.17,'(S^s)×: dual of the minimal space',size=12)
txt(a,.51,.17,'(M^s)×: dual retaining boundary modes',size=12)
a.plot([.035,.965],[.36,.36],color='#b3c5d0',linewidth=1)
txt(a,.045,.035,'Spectral conversion only:  ‖P′‖_(W^r,W^r′) ≤ b_r′ a_r M',
    size=13,color=BLUE,bold=True)

b = fig.add_subplot(gs[1,0]); b.set_xlim(-.06,1.03); b.set_ylim(-.32,1.10)
b.set_axis_off()
txt(b,-.055,1.08,'B  A boundary mode survives the output extension',size=14,bold=True)
txt(b,-.015,.91,'Fixed ordinary physical plaque I = (0, 1)',size=12)
b.plot([0,1],[.03,.03],color=INK,linewidth=2)
for x,label in [(0,'0'),(1,'1')]:
    b.plot(x,.03,'o',markerfacecolor='white',markeredgecolor=INK,markersize=7)
    txt(b,x,-.07,label,size=12,ha='center')
epsilons=[.12,.065,.025]
for e,y,c in zip(epsilons,[.65,.46,.27],[BLUE,TEAL,ORANGE]):
    z=np.linspace(0,1,401)
    profile=np.zeros_like(z)
    keep=(z>0)&(z<1)
    profile[keep]=np.exp(4-1/(z[keep]*(1-z[keep])))
    xx=e*(1+z)
    b.fill_between(xx,y,y+.13*profile,color=c,alpha=.23)
    b.plot(xx,y+.13*profile,color=c,linewidth=1.7)
    b.plot([e,2*e],[y,y],color=c,linewidth=2)
    txt(b,.36,y+.045,f'ε = {e:g}: support (ε, 2ε)',size=11.5,color=c)
txt(b,.0,-.20,'h_ε → b₀ in (H¹(I))×;    b₀ ≠ 0,    b₀|H₀¹ = 0',size=11.5,color=ORANGE)
txt(b,.0,-.30,'E₋₁ b₀ = point functional at 0 on the circle',size=11.5,color=TEAL)

c = fig.add_subplot(gs[1,1])
eps=np.geomspace(1e-4,1/6,400)
c.plot(eps,np.sqrt(2*eps),color=BLUE,linewidth=2.6,label='local bound after both constants (product = 1)')
c.axhline(.5,color=ORANGE,linewidth=2.2,label='proved global norm lower bound: 1/2')
c.axvline(1/8,color='#879aa7',linewidth=1,linestyle='--')
c.scatter([1/8],[.5],color=INK,s=22,zorder=4)
c.set_xscale('log'); c.set_xlim(1e-4,1/6); c.set_ylim(0,.63)
c.set_xticks([1e-4,1e-3,1e-2,1e-1])
c.set_xticklabels(['10⁻⁴','10⁻³','10⁻²','10⁻¹'],fontproperties=FP)
c.xaxis.set_minor_formatter(NullFormatter())
c.set_xlabel('ε  (logarithmic axis)',fontproperties=FP,fontsize=12)
c.set_ylabel('operator norm bound',fontproperties=FP,fontsize=12)
c.grid(True,alpha=.19)
c.set_title('C  Compact-core contradiction',loc='left',fontproperties=FB,fontsize=14,pad=14,color=INK)
c.legend(loc='upper left',prop=FontProperties(fname=str(REGULAR),size=9.5),framealpha=.95)
c.annotate('ε = 1/8',xy=(1/8,.5),xytext=(.009,.40),
           fontproperties=FP,fontsize=11,color=INK,
           arrowprops={'arrowstyle':'->','color':INK})
for label in [*c.get_xticklabels(),*c.get_yticklabels()]:label.set_fontproperties(FP)
fig.text(.052,.97,'Physical plaque norms: unrestricted lifting and the unavoidable boundary choice',
         fontproperties=FB,fontsize=18,color=INK,va='top')
fig.text(.052,.023,'PJ.1–PJ.13 and NC.1–NC.5. Profiles indicate supports only; curves are proved bounds, not spectra.',
         fontproperties=FP,fontsize=11.5,color=INK)
base=OUT/'plaque-physical-two-realizations'
fig.savefig(base.with_suffix('.png'),dpi=210,metadata={'Software':'Original CC0 physical plaque diagram'})
fig.savefig(base.with_suffix('.svg'),metadata={'Date':None,'Creator':'Original CC0 physical plaque diagram'})
plt.close(fig)
print('Rendered plaque-physical-two-realizations.png and plaque-physical-two-realizations.svg')
CACHE.cleanup()
