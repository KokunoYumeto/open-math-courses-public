"""Original radial enclosures and both complete weighted transfer branches."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,(ax,bx)=plt.subplots(1,2,figsize=(15,8),layout='constrained',
                       gridspec_kw={'width_ratios':[1.1,1]})
A=1;M=128;B=100*M*A
rows=[
 ('Proved regular shell (inner enclosure)',141*A/32,B/2-77*A/32,'#dde6e9'),
 ('Earlier velocity region (13.3)',19*A/4,3*B/10+A/4,'#bfd9cf'),
 ('Earlier vorticity region (12.9)',5*A,3*B/10,'#bdd2df'),
 ('Smaller vorticity region (14.1)',(1-1/math.sqrt(32))*10*A,(1+1/math.sqrt(32))*B/10,'#7ea9c0'),
 ('Weighted annulus',10*A,B/10,'#b5bddb'),
 ('Weighted target',100*A,B/20,'#d8c78e'),
 ('Actual outward-mass subannulus',100*A,300*A,'#e2ac79')]
for j,(label,lo,hi,color) in enumerate(rows):
 y=6-j
 ax.plot([lo,hi],[y,y],color=color,lw=18,solid_capstyle='butt')
 ax.scatter([lo,hi],[y,y],color='#3e4f56',s=16,zorder=4)
 left=r'$10(1-1/\sqrt{32})$' if j==3 else f'{lo:.8f}'.rstrip('0').rstrip('.')
 right=r'$1280(1+1/\sqrt{32})$' if j==3 else f'{hi:.8f}'.rstrip('0').rstrip('.')
 ax.text(lo,y+.21,left,fontsize=8,ha='left')
 ax.text(hi,y+.21,right,fontsize=8,ha='right')
ax.set_xscale('log')
ax.set_yticks(list(range(6,-1,-1)),[r[0] for r in rows])
ax.set(xlim=(3.5,8000),ylim=(-.8,6.6),xlabel='Original radius |x − x₀| (logarithmic axis)',
       title='Every receiving region remains in the same annulus')
ax.grid(axis='x',alpha=.15)
ax.text(4,-.62,'Illustrative geometry: A = 1, M = 128, B = 12800.\nActual M is selected by 9.4 and may be larger; no fluid is sampled.',fontsize=9)
bx.set(xlim=(0,1),ylim=(0,1));bx.axis('off')
def box(x,y,w,h,label,color):
 bx.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',
               fc=color,ec='#73838b',lw=1))
 bx.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=10)
def arrow(x1,y1,x2,y2):
 bx.annotate('',xy=(x2,y2),xytext=(x1,y1),
    arrowprops=dict(arrowstyle='->',color='#536872',lw=1.4))
box(.17,.84,.66,.10,'Original outward annular mass\nand the finite annular estimate (10.2–10.3)','#e2ac79')
box(.02,.62,.43,.12,'Initial weighted term ≥ Z₀ / 2\nFinal-time mass directly (10.4)','#b5bddb')
box(.55,.62,.43,.12,'Cylinder term ≥ Z₀ / 2\nActual radial shell (11.1–11.3)','#b5bddb')
arrow(.42,.84,.25,.75);arrow(.59,.84,.76,.75)
box(.55,.43,.43,.13,'Remove the near-zero strip\nusing its full bound; select an\nactual slab and ball (11.4–11.7)','#dde6e9')
arrow(.76,.62,.76,.565)
box(.55,.24,.43,.13,'Full Gaussian cylinder inside '+r'$\mathcal{K}$'+'\nProved first-error absorption\n(12.1–12.7)','#dde6e9')
arrow(.76,.43,.76,.375)
box(.15,.09,.70,.10,'Same original final-time mass (12.9)\nBoth support margins retained','#7ea9c0')
arrow(.23,.62,.23,.195);arrow(.76,.24,.72,.195)
bx.text(.5,.025,'Smaller shell and full curl map → stronger velocity bound (14.1–14.4)',
        ha='center',fontsize=9,color='#315d4f')
fig.suptitle('A complete transfer to the original final time',fontsize=16)
fig.savefig(ROOT/'final-time-annular-transfer.png',dpi=170)
fig.savefig(ROOT/'final-time-annular-transfer.svg')
print('Saved original receiving regions and both complete transfer branches.')
