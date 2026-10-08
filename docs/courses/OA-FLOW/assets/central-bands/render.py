"""Exact central-band coordinates and the normal fixed-carrier inverse."""
from pathlib import Path
from fractions import Fraction
import argparse, json, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=HERE.parent / 'typeiii-zero-decomposition')
args = parser.parse_args()
for name in ['DejaVuSans.ttf', 'DejaVuSans-Bold.ttf']:
    fontManager.addfont(str(args.font_dir / name))
font = FontProperties(fname=str(args.font_dir / 'DejaVuSans.ttf'))
plt.rcParams.update({'font.family': font.get_name(), 'font.size': 10,
                     'svg.hashsalt': 'oa-flow-central-bands-v1', 'svg.fonttype': 'path'})
data = json.loads((HERE / 'data.json').read_text())

def exponent(value):
    q = Fraction(value)
    n, d = q.numerator, q.denominator
    assert n & (n - 1) == 0 and d & (d - 1) == 0
    return (n.bit_length() - 1) - (d.bit_length() - 1)

rho = {int(n): [Fraction(x) for x in pair] for n, pair in data['rho_n'].items()}
for n in range(-2, 4):
    assert rho[n][0] == Fraction(1, 2) * rho[n-1][1]
    assert rho[n][1] == Fraction(1, 4) * rho[n-1][0]

fig = plt.figure(figsize=(12, 7.4), facecolor='#fbfcff')
grid = fig.add_gridspec(2, 1, height_ratios=[1.15, 1], hspace=.55,
                       left=.20, right=.96, bottom=.10, top=.88)
ax = fig.add_subplot(grid[0])
colors = ['#5277b8', '#548e8b', '#9389bb', '#da9a37', '#c56d6d', '#687c9c']
for coordinate, y in [(0, 1), (1, 0)]:
    for n, color in zip(data['indices'], colors):
        left = exponent(rho[n][coordinate])
        right = exponent(rho[n-1][coordinate])
        ax.plot([left, right], [y, y], lw=12, color=color, solid_capstyle='butt')
        ax.plot(left, y-.045, 'o', color=color, markersize=6, mec='#243146', mew=.6)
        ax.plot(right, y+.045, 'o', color='white', markersize=5, mec='#243146', mew=.6)
        ax.text((left+right)/2, y+.18, f'n={n}', ha='center', fontsize=9)
    sample = math.log2(3/8)
    ax.scatter(sample, y, marker='D', s=45, facecolor='#111827', zorder=5)
ax.set(yticks=[0, 1], yticklabels=['center 1: ρ = 1/4', 'center 0: ρ = 1/2'],
       ylim=(-.5, 1.6), xlim=(-5.5, 5.5), xticks=list(range(-5, 6)),
       xlabel='log₂(density): filled lower endpoint, open upper endpoint')
ax.grid(axis='x', alpha=.17)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.tick_params(axis='y', length=0, pad=12)
ax.set_title('Exact joint bands [ρₙ, ρₙ₋₁): one h, two band indices',
             loc='left', fontweight='bold', pad=20, fontsize=12)
ax.text(.98, .08, '◆ h = 3/8\nCB14–19, CB34', transform=ax.transAxes,
        ha='right', va='bottom', fontsize=9,
        bbox={'facecolor':'#fbfcff', 'edgecolor':'none', 'alpha':.95})

bx = fig.add_subplot(grid[1]); bx.set(xlim=(0, 12), ylim=(0, 4.2)); bx.axis('off')
bx.set_title('One band determines every fixed element', loc='left',
             fontweight='bold', fontsize=12, pad=14)

def box(x,y,w,h,label,color='#eaf0f9'):
    bx.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04,rounding_size=.10',
                              linewidth=1,edgecolor='#61748e',facecolor=color))
    bx.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10)

def arrow(start,end,label=None,dy=0):
    bx.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=12,
                                color='#50627d',linewidth=1.2))
    if label: bx.text((start[0]+end[0])/2,(start[1]+end[1])/2+dy,label,
                      ha='center',va='center',fontsize=9)

for x,n in [(0.4,0),(4.3,1),(8.2,2)]:
    box(x,2.6,2.5,.9,f'band c{n}\ncoordinate a c{n}', '#f7edd8' if n==1 else '#eaf0f9')
    arrow((x+1.25,2.55),(5.55,1.22))
arrow((4.25,3.12),(2.98,3.12),r'$\bar\theta: n\mapsto n-1$',dy=.43)
arrow((8.14,3.12),(6.88,3.12),r'$\bar\theta: n\mapsto n-1$',dy=.43)
box(4.05,.32,3,.88,'the full carrier Aₘ', '#e4f0e9')
bx.text(.2,.72,'I(cₙ) = 1 for every n\nI collapses distinct bands',fontsize=10,va='center')
bx.text(8.0,.72,'fixed inverse:\n'+r'$R(b)c_n=\bar\theta^{1-n}(b)$',fontsize=10,va='center')
bx.text(5.55,1.70,'I on projections; Jₙ on each band',ha='center',fontsize=9,
        bbox={'facecolor':'#fbfcff','edgecolor':'none','pad':2})
fig.suptitle('Central bands and the global carrier', x=.09, ha='left',
             fontsize=19, fontweight='bold', color='#1e304a')
fig.text(.09,.027,'Finite window of exact coefficient bands. Lower diagram: the proved maps, not a finite model of the carrier.  CB24–25, CB30–31.',
         fontsize=8.7,color='#43536a')
fig.savefig(HERE/'central-bands.svg',metadata={'Date':None,'Creator':'OA-FLOW course project'})
fig.savefig(HERE/'central-bands.png',dpi=180,metadata={'Software':'OA-FLOW course project'})
plt.close(fig)
