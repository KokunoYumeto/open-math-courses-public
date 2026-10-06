"""Exact four-point normalization and Bochner measure; no numerical theorem proof."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='oa-flow-scalar-plancherel-v1'
import matplotlib.pyplot as plt

D=Path(__file__).resolve().parent
(D/'figures').mkdir(exist_ok=True)
# Integer Gaussian entries, with no floating Fourier approximation.
F=np.array([[1,1,1,1],[1,-1j,-1,1j],[1,-1,1,-1],[1,1j,-1,-1j]],complex)
f=np.array([1,1j,-1,0],complex)
hat=F@f
assert np.array_equal(hat,np.array([1j,3,-1j,1]))
assert np.array_equal(F.conj().T@F,4*np.eye(4))
mass=np.abs(hat)**2/4
p=F.conj().T@mass
assert np.array_equal(p,np.array([3,2j,-2,-2j]))
assert np.sum(np.abs(f)**2)==np.sum(mass)==3

fig,axs=plt.subplots(1,3,figsize=(14,5.5),layout='constrained')
fig.suptitle('The dual Haar factor makes energy and the coefficient measure agree',fontsize=16,fontweight='bold')
x=np.arange(4)
ax=axs[0]
ax.bar(x-.17,f.real,.34,label='Real part',color='#247e8d')
ax.bar(x+.17,f.imag,.34,label='Imaginary part',color='#775aa6')
ax.set_xticks(x);ax.set_xlabel(r'$j\in\mathbb{Z}/4\mathbb{Z}$')
ax.set_ylabel(r'$f(j)$');ax.set_ylim(-1.3,1.6);ax.axhline(0,color='#667',lw=.6)
ax.set_title(r'$f=(1,i,-1,0),\quad \sum_j |f(j)|^2=3$',fontsize=12)
ax.legend(loc='upper right',fontsize=10);ax.grid(axis='y',alpha=.2)
ax=axs[1]
ax.bar(x,mass,color='#247e8d',width=.58)
for j,v in enumerate(mass):ax.text(j,v+.06,['1/4','9/4','1/4','1/4'][j],ha='center',fontsize=13)
ax.set_xticks(x);ax.set_xlabel(r'$k\in\widehat{\mathbb{Z}/4\mathbb{Z}}$')
ax.set_ylabel(r'$\nu_p(\{k\})=|\widehat f(k)|^2/4$')
ax.set_ylim(0,2.75);ax.grid(axis='y',alpha=.2)
ax.set_title(r'$\widehat f=(i,3,-i,1),\quad \lambda(\{k\})=1/4$',fontsize=12)
ax.text(.97,.85,r'$\sum_k\nu_p(\{k\})=3$',transform=ax.transAxes,fontsize=13,ha='right',bbox={'facecolor':'white','edgecolor':'#dde3e9','alpha':.97})
ax=axs[2]
colors=['#247e8d','#775aa6','#c17628','#775aa6']
for j,z in enumerate(p):
    ax.annotate('',xy=(z.real,z.imag),xytext=(0,0),arrowprops={'arrowstyle':'->','color':colors[j],'lw':2})
    dx=-.06 if j==0 else (.08 if j in (1,3) else .06)
    dy=.15 if z.imag>=0 else -.3
    ax.text(z.real+dx,z.imag+dy,[r'$p(0)=3$',r'$p(1)=2i$',r'$p(2)=-2$',r'$p(3)=-2i$'][j],ha='right' if j==0 else 'left',fontsize=12)
ax.set_xlim(-3.55,4.25);ax.set_ylim(-2.85,2.85);ax.set_aspect('equal')
ax.axhline(0,color='#778',lw=.6);ax.axvline(0,color='#778',lw=.6)
ax.set_xlabel('Real part');ax.set_ylabel('Imaginary part');ax.grid(alpha=.2)
ax.set_title(r'$p(j)=\sum_k \nu_p(\{k\}) e^{2\pi i k j/4}$',fontsize=12)
fig.savefig(D/'figures/plancherel-normalization.png',dpi=180)
fig.savefig(D/'figures/plancherel-normalization.svg',metadata={'Date':None})
svg=D/'figures/plancherel-normalization.svg'
svg.write_text('\n'.join(s.rstrip() for s in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8',newline='\n')
(D/'figures/plancherel-data.json').write_text(json.dumps({'group':'Z/4Z','primal_Haar_atom':1,'dual_Haar_atom':'1/4','f':['1','i','-1','0'],'negative_transform':['i','3','-i','1'],'Bochner_atoms':['1/4','9/4','1/4','1/4'],'p':['3','2i','-2','-2i'],'energy':3,'identities':'Exact Gaussian integer matrix multiplication, not rounded evidence for an infinite-dimensional theorem.'},indent=2)+'\n',encoding='utf-8',newline='\n')
