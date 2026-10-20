"""Exact planar carriers in AN01-U095, P17-P18. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(1,2,figsize=(11.8,5.8),constrained_layout=True)
blue='#195f9a';orange='#bd5912';green='#167848'
t=np.linspace(0,1,801)
x=(1-np.cos(np.pi*t))/2;y=np.sin(np.pi*t)/2
ax[0].plot(x,y,color=blue,lw=3,label=r'$A_+$')
ax[0].plot(x,-y,color=orange,lw=3,label=r'$A_-$')
for sign,col in [(1,blue),(-1,orange)]:
 a=.40;b=.46
 p=lambda s:((1-np.cos(np.pi*s))/2,sign*np.sin(np.pi*s)/2)
 ax[0].add_patch(FancyArrowPatch(p(a),p(b),arrowstyle='-|>',mutation_scale=15,color=col,lw=2))
ax[0].scatter([0,1],[0,0],s=45,color='#202d3d',zorder=5)
ax[0].annotate('0',(0,0),xytext=(-13,-19),textcoords='offset points')
ax[0].annotate('1',(1,0),xytext=(7,-19),textcoords='offset points')
ax[0].text(.50,.66,'Each semicircle is a minimal carrier',ha='center',weight='bold')
ax[0].text(.50,-.72,r'$A_+\cap A_-=\{0,1\}$ is not a carrier',ha='center')
ax[0].set_title('Same functional, two minimal carriers',pad=16)
ax[0].legend(loc='center',frameon=False,ncol=2)
ax[0].set_xlim(-.23,1.23);ax[0].set_ylim(-.84,.83)

s=np.linspace(0,2*np.pi,1001)
z=1j*(1-np.exp(1j*s))
ax[1].plot(z.real,z.imag,color=blue,lw=2.8,label='Circular part of the path')
ax[1].plot([0,1],[0,0],color=green,lw=3.5,label='Segment carrier')
for a,b in [(np.pi/2-.10,np.pi/2+.10),(3*np.pi/2-.10,3*np.pi/2+.10)]:
 p=lambda v: (np.sin(v),1-np.cos(v))
 ax[1].add_patch(FancyArrowPatch(p(a),p(b),arrowstyle='-|>',mutation_scale=15,color=blue,lw=2))
ax[1].add_patch(FancyArrowPatch((.35,0),(.57,0),arrowstyle='-|>',mutation_scale=16,color=green,lw=2))
ax[1].scatter([0,1,0],[0,0,1],s=[45,45,22],color='#202d3d',zorder=5)
ax[1].annotate('0',(0,0),xytext=(-13,-19),textcoords='offset points')
ax[1].annotate('1',(1,0),xytext=(7,-19),textcoords='offset points')
ax[1].annotate(r'$i$',(0,1),xytext=(8,1),textcoords='offset points')
ax[1].plot([0,1],[1,1],color='#667789',lw=1,ls='--')
ax[1].text(.44,1.07,'radius 1',fontsize=10)
ax[1].text(0,2.22,'The circular integral is zero',ha='center',weight='bold')
ax[1].text(.10,-.39,r'$[0,1]$ already carries $U_{0,1}$',ha='center')
ax[1].set_title(r'A regular $C^1$ path need not be simple',pad=16)
ax[1].set_xlim(-1.3,1.3);ax[1].set_ylim(-.55,2.42)
for a in ax:
 a.set_aspect('equal')
 a.axhline(0,color='#d3dce4',lw=.8,zorder=0)
 a.axvline(0,color='#d3dce4',lw=.8,zorder=0)
 a.set_xlabel(r'$\operatorname{Re}z$')
 a.set_ylabel(r'$\operatorname{Im}z$')
 a.spines[['top','right']].set_visible(False)
fig.suptitle(r'$U_{0,1}(f)=\int_0^1 f(z)\,dz$ for entire tests $f$',fontsize=16)
fig.savefig(out/'simple-arcs-and-complex-carriers.png',dpi=170)
fig.savefig(out/'simple-arcs-and-complex-carriers.svg')
svg_path=out/'simple-arcs-and-complex-carriers.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
assert np.allclose(x[[0,-1]],[0,1]) and np.allclose(y[[0,-1]],[0,0])
assert np.max(np.abs(np.abs(z-1j)-1))<1e-12
print('Exact semicircles and the regular loop-plus-segment path rendered.')
