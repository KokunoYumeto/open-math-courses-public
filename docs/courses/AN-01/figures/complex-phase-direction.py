"""Original figure for AN01-U135, D9-D15. CC0; GPT-6 Astra (OpenAI)."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams['svg.hashsalt']='AN01-U135-direction'
out=Path(__file__).resolve().parent
fig,axes=plt.subplots(1,3,figsize=(13.5,4.4),layout='constrained')
grid=np.linspace(-1,1,501)
x,y=np.meshgrid(grid,grid)
den=np.hypot(y*y,x)
values=np.ma.masked_where(den==0,-np.log10(np.maximum(den,1e-300)))
im=axes[0].pcolormesh(x,y,values,shading='auto',cmap='magma',vmin=-.2,vmax=5,rasterized=True)
axes[0].plot(0,0,'wo',ms=5,mec='black')
axes[0].set(xlabel=r'$x$',ylabel=r'$y$',title=r'$\log_{10}|U(x,y)|$; origin omitted',aspect='equal')
fig.colorbar(im,ax=axes[0],shrink=.85)
ax=axes[1]
ax.axhline(0,color='0.7',lw=.8);ax.axvline(0,color='0.7',lw=.8)
ax.annotate('',xy=(1.8,0),xytext=(.06,0),arrowprops=dict(arrowstyle='->',color='#175b91',lw=3))
ax.annotate('',xy=(-1.8,0),xytext=(-.06,0),arrowprops=dict(arrowstyle='->',color='#b54e1b',lw=2,linestyle='--'))
ax.plot(0,0,'o',mfc='white',mec='black',ms=7,zorder=5)
ax.text(.8,.35,r'$U:\ \lambda>0$',ha='center',color='#175b91')
ax.text(-.9,-.55,r'$\mathrm{Re}\,U:$ both rays',ha='center',color='#b54e1b')
ax.set(xlim=(-2,2),ylim=(-1.2,1.2),xlabel=r'$\xi_x$',ylabel=r'$\xi_y$',title='Singular covectors over (0,0)',aspect='equal')
ys=np.linspace(-1,1,1001)
for eps in [.2,.05,.01]:
 axes[2].plot(ys,1/(eps+ys*ys),label=rf'$\varepsilon={eps:g}$')
axes[2].set(xlabel=r'$y$',ylabel=r'$U_\varepsilon(0,y)$',title='Smooth damped traces',yscale='log')
axes[2].grid(alpha=.2);axes[2].legend()
fig.savefig(out/'complex-phase-direction.png',dpi=160)
fig.savefig(out/'complex-phase-direction.svg',metadata={'Date':None})
p=out/'complex-phase-direction.svg';p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
