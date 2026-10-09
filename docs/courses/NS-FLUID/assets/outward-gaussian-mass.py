"""Original containing annulus and the two proved logarithmic error bounds."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14,6),layout='constrained',gridspec_kw={'width_ratios':[1.15,1]})
ax.add_patch(Circle((0,0),3,fc='#e5edf1',ec='#667f8b',lw=1.5))
ax.add_patch(Circle((0,0),1,fc='white',ec='#667f8b',lw=1.5))
ax.add_patch(Circle((0,0),1,fc='#f3ddb8',ec='#b58b45',alpha=.65,lw=2))
ax.add_patch(Circle((2,0),1,fc='#aecfdb',ec='#386f89',lw=2))
ax.scatter([0,2],[0,0],color=['#b58b45','#386f89'],s=32)
ax.annotate(r'$x_0=(0,0,0)$',(0,0),xytext=(-45,-25),textcoords='offset points')
ax.annotate(r'$x_c=(2,0,0)$',(2,0),xytext=(-26,-25),textcoords='offset points')
ax.text(-2.85,2.5,r'$D/2<|x-x_0|<3D/2$',fontsize=12)
ax.text(-2.85,-2.6,'Original section x₃ = 0; D = 2 and L₀ = 1.\nThe much larger Gaussian ball has radius kD ≥ 128\nand lies beyond this view.',fontsize=9)
ax.annotate('original mass ball',(-.55,.65),xytext=(-2.9,1.6),arrowprops={'arrowstyle':'->','color':'#a17a39'},color='#8c6226',fontsize=10)
ax.annotate('proved outward mass',(2.25,.5),xytext=(.9,1.75),arrowprops={'arrowstyle':'->','color':'#386f89'},color='#386f89',fontsize=10)
ax.set(xlim=(-3.2,3.3),ylim=(-3.15,3.15),aspect='equal',xlabel='Original coordinate x₁',ylabel='Original coordinate x₂',title='The full containing annulus')
ax.grid(alpha=.12)
a=np.linspace(1,3,401)
bx.axhline(0,color='#963d34',lw=2,label='error equals half its receiving lower bound')
bx.plot(a,.5-a,color='#386f89',lw=2.5,label=r'proved upper envelope $1/2-a_D$')
bx.fill_between(a,-2.7,.5-a,color='#dcecf3')
bx.set(xlim=(1,3),ylim=(-2.7,.35),xlabel=r'original ratio $a_D=D^2/(\nu\mathcal{T})$',ylabel='logarithmic error ratio, divided by its stated power of k',title='Both error terms are below their budgets')
bx.text(1.08,-1.7,r'Illustrative scalar inputs: $k=64$,'+'\n'+r'$\log F_1=k^2/2,\quad\log F_2=k^4/2$.'+'\nFirst bound divided by k²; second by k⁴.\nThese are proved bounds, not flow samples.',fontsize=10)
bx.legend(loc='upper right',fontsize=8)
bx.grid(alpha=.15)
fig.suptitle('Original vorticity mass moves outward after two complete Gaussian absorptions',fontsize=14)
fig.savefig(ROOT/'outward-gaussian-mass.png',dpi=170)
fig.savefig(ROOT/'outward-gaussian-mass.svg')
print('Saved original annulus section and both error-bound envelopes.')
