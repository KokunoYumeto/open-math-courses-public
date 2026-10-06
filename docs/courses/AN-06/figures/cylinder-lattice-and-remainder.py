"""Reproducible CC0 illustration of AN06-U051 Theorem 6.1.

The lattice and sampled counts use the explicit fixed lengths a=pi, L=2pi.
Quarter-integer radii are counted with integer inequalities, including ties.
The samples illustrate the exact formula; the asymptotic bound is proved in text.
Requires Python 3, NumPy and Matplotlib; run to reproduce PNG and SVG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT=Path(__file__).resolve().parent
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'AN06-cylinder-lattice-v1'})
fig=plt.figure(figsize=(11,12),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1.2,1],hspace=.45,wspace=.4)
ax=fig.add_subplot(gs[0,0])
mi,li=np.meshgrid(np.arange(-4,5),np.arange(-4,5))
inside=mi*mi+li*li<=16
S=int(inside.sum());row=int((inside & (mi==0)).sum());N=int((inside & (mi>0)).sum())
assert (S,row,N)==(49,9,20) and N==(S-row)//2
for condition,color,label in [(mi<0,'#9aa5af','reflected partners'),(mi==0,'#c36b11','excluded normal-zero row'),(mi>0,'#176996','Dirichlet modes')]:
    mask=inside & condition
    ax.scatter(mi[mask],li[mask],s=36,color=color,label=label,zorder=3)
ax.add_patch(Circle((0,0),4,fill=False,color='#176996',lw=1.5))
ax.axvline(0,color='#c36b11',alpha=.3);ax.axhline(0,color='#758391',alpha=.25)
ax.set(xlim=(-4.7,4.7),ylim=(-4.7,4.7),aspect='equal',xlabel=r'$\pi m/a=m$',ylabel=r'$2\pi\ell/L=\ell$',title=r'Closed frequency disk: $k=4$')
ax.set_xticks(np.arange(-4,5,2));ax.set_yticks(np.arange(-4,5,2));ax.grid(alpha=.12)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),fontsize=10,frameon=False)
info=fig.add_subplot(gs[0,1]);info.axis('off')
info.text(0,1,'Exact coordinates and multiplicities',weight='bold',va='top',fontsize=14)
lines=[r'$D=\mathrm{diag}(\pi/a,2\pi/L)$',r'$\det D=2\pi^2/(aL)$',r'$2\pi D^{-T}(r,t)=(2ar,Lt)$','',r'$R_0(k)=2\lfloor Lk/(2\pi)\rfloor+1$',r'$N_P(k^2)=(S_{a,L}(k)-R_0(k))/2$','',r'Shown: $a=\pi,\ L=2\pi,\ D=I$',r'$S(4)=49,\ R_0(4)=9,\ N_P(16)=20$','Every integer pair is counted.','The disk includes its boundary.']
for i,line in enumerate(lines):info.text(0,.86-.075*i,line,va='top',fontsize=12)
q=np.arange(4,161);ks=q/4
m,l=np.meshgrid(np.arange(-40,41),np.arange(-40,41));square=16*(m*m+l*l)
full=np.array([np.count_nonzero(square<=int(v)*int(v)) for v in q])
direct=np.array([np.count_nonzero((square<=int(v)*int(v)) & (m>0)) for v in q])
rows=2*(q//4)+1
assert np.array_equal(2*direct,full-rows)
E=full-np.pi*ks*ks
residual=direct-(np.pi*ks*ks/2-ks)
assert np.allclose(residual,(ks-np.floor(ks))-.5+E/2,atol=1e-12)
plot=fig.add_subplot(gs[1,0])
plot.plot(ks,residual/ks**(2/3),color='#176996',lw=1,marker='.',markersize=2)
plot.axhline(0,color='#758391',lw=.8)
plot.set(xlabel=r'Spectral radius $k$',ylabel=r'$[N_P(k^2)-(\pi k^2/2-k)]/k^{2/3}$',title='Exact count samples, same fixed lengths')
plot.grid(alpha=.16)
balance=fig.add_subplot(gs[1,1]);balance.axis('off')
balance.text(0,1,'Proved smoothing balance',weight='bold',va='top',fontsize=14)
for y,txt in [(.84,r'$|E(k)|\leq C_{a,L,\rho}$'),(.73,r'$\quad\cdot(k\delta+\delta^2+k^{1/2}\delta^{-1/2})$'),(.55,r'$\delta=k^{-1/3}$'),(.43,r'$k\delta=k^{2/3}$'),(.31,r'$k^{1/2}\delta^{-1/2}=k^{2/3}$'),(.19,r'$\delta^2=k^{-2/3}$'),(.05,r'$E(k)=O_{a,L}(k^{2/3})$')]:balance.text(0,y,txt,va='top',fontsize=12)
fig.suptitle('The flat cylinder: its exact row subtraction and lattice remainder',fontsize=16,y=.98)
fig.text(.5,.045,'AN06-U051 Theorem 6.1; original cylinder in Exercise/Solution 7.5. CC0.',ha='center',fontsize=10)
fig.text(.5,.026,'The plotted samples illustrate the formula; the disk decay and Poisson argument prove the bound.',ha='center',fontsize=10)
fig.subplots_adjust(top=.91,bottom=.12,left=.09,right=.96)
fig.savefig(OUT/'cylinder-lattice-and-remainder.png',dpi=170,metadata={'Software':'Matplotlib; original CC0 figure'})
fig.savefig(OUT/'cylinder-lattice-and-remainder.svg',metadata={'Date':None,'Creator':'Original CC0 figure; GPT-6.1 Sol (OpenAI), Ultra'})
plt.close(fig)
print('Generated exact cylinder lattice and fixed-radius count samples; all integer checks passed.')
