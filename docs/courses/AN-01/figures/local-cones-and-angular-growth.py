from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'svg.fonttype':'none'})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
a=ax[0]
a.add_patch(Wedge((0,0),.33,0,90,color='#e9eff8',label='Approach quadrant'))
a.add_patch(Wedge((0,0),.33,15,75,color='#b8d8e7',label='Strict sector'))
for angle in [0,15,75,90]:
 t=np.deg2rad(angle);a.plot([0,.33*np.cos(t)],[0,.33*np.sin(t)],'--',color='#395475',lw=1.1)
theta=np.linspace(0,np.pi/2,601)
a.plot(.25*np.cos(theta),.25*np.sin(theta),color='#9a3e21',lw=2,label='Radius 1/4')
a.text(.08,.24,'V: 15° < θ < 75°',rotation=-28)
a.text(.205,.055,r'$\Gamma$',fontsize=17)
a.set(xlim=(-.015,.35),ylim=(-.015,.35),xlabel=r'$y_1$',ylabel=r'$y_2$',title='Strict angular neighborhoods')
a.set_aspect('equal');a.legend(loc='upper right',fontsize=8,framealpha=.95)
b=ax[1]
deg=np.linspace(0,89.9,1501);factor=1/np.cos(np.deg2rad(deg))
b.axvspan(15,75,color='#b8d8e7')
b.semilogy(deg,factor,color='#9a3e21',lw=2)
for angle in [15,75]:b.axvline(angle,color='#395475',ls='--',lw=1.1)
b.set(xlim=(0,90),ylim=(.9,800),xlabel='Imaginary direction θ (degrees)',ylabel=r'$|y|\,|f(iy)|=1/\cos\theta$',title='Exact angular factor for a linear pole')
b.grid(alpha=.25,which='both')
b.text(27,90,'Bounded on each strict sector')
b.text(49,14,'Unbounded as θ → 90°')
for ext in ['png','svg']:fig.savefig(out/('local-cones-and-angular-growth.'+ext),dpi=180)
svg=out/'local-cones-and-angular-growth.svg'
svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
plt.close(fig)
