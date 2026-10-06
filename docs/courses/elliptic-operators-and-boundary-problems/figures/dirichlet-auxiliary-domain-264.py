"""Sample the original auxiliary domain and the explicit DSP-AUX1 cutoff."""
from pathlib import Path
import argparse
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
args=parser.parse_args()
args.output_dir.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'text.usetex':False,'svg.hashsalt':'AN03-U026-DSP-AUX1-264','font.family':'DejaVu Sans','font.size':13})
c=1.0;d=1.0;s_edge=4.0
def bump(w):return np.exp(-1.0/w) if w>0 else 0.0
I_edge=quad(bump,0,s_edge-d*d,epsabs=1e-12,epsrel=1e-12)[0]
L=2/I_edge
def psi(s):return L*quad(bump,0,s-d*d,epsabs=1e-12,epsrel=1e-12)[0] if s>d*d else 0.0
s_star=brentq(lambda s:psi(s)-c*c,d*d,s_edge,xtol=1e-13)
z_star=np.sqrt(s_star)
z=np.linspace(-z_star,z_star,1001)
psi_z=np.array([psi(q*q) for q in z])
gap=np.sqrt(np.maximum(c*c-psi_z,0.0))
lower=c-gap;upper=c+gap
fig,(ax,notes)=plt.subplots(1,2,figsize=(12,6),gridspec_kw={'width_ratios':[1.45,1]},facecolor='#fffdf8')
fig.subplots_adjust(left=.08,right=.97,bottom=.30,top=.78,wspace=.24)
ax.set_facecolor('#fffdf8');notes.set_facecolor('#fffdf8')
ax.fill_between(z,lower,upper,color='#e4efe8')
ax.plot(z,upper,color='#ab5732',lw=2.5,label='artificial boundary')
for sign in (-1,1):
 window=z*sign>=d
 ax.plot(z[window],lower[window],color='#ab5732',lw=2.5)
ax.plot([-d,d],[0,0],color='#225e7b',lw=3,label='physical flat boundary')
ax.plot([-.65,.65,.65,-.65,-.65],[0,0,.7,.7,0],ls='--',color='#615b86',lw=1.6,label='cutoff-support window')
ax.plot([z_star],[c],'o',color='#173750',ms=5)
ax.annotate(r'$\nabla F=(2\sqrt{s_*}\,\psi^\prime(s_*),0)\ne0$',xy=(z_star,c),xytext=(z_star+.18,c+.25),fontsize=11,arrowprops={'arrowstyle':'->','color':'#173750'})
ax.axhline(c,color='#9cabb3',lw=.8,ls=':')
ax.set_xticks([-z_star,-d,0,d,z_star],[r'$-\sqrt{s_*}$',r'$-d$',r'$0$',r'$d$',r'$\sqrt{s_*}$'])
ax.set_yticks([0,c,2*c],[r'$0$',r'$c$',r'$2c$'])
ax.set_xlim(-z_star-.15,z_star+.9);ax.set_ylim(-.2,2.25)
ax.set_xlabel(r'original tangential coordinate $z$');ax.set_ylabel(r'original normal coordinate $t$')
ax.spines[['top','right']].set_visible(False)
fig.legend(*ax.get_legend_handles_labels(),loc='upper center',bbox_to_anchor=(.5,.195),ncol=3,fontsize=10,frameon=False)
notes.axis('off')
entries=[(.98,'Same defining function',17),(.88,r'$F(z,t)=t^2-2ct+\psi(z^2)$',15),(.73,r'$c=d=1,\quad s_{\rm e}=4$',14),(.62,r'$L=2/I_{\rm e},\quad \psi(4)=2>c^2$',13),(.48,r'$\psi^\prime(s)>0\quad\mathrm{for}\ s>d^2$',14),(.34,r'$\psi(s_*)=c^2,\quad d^2<s_*<4$',13),(.19,'At t = c the tangential gradient\nproves smoothness of the level set.',12)]
for y,label,size in entries:notes.text(0,y,label,transform=notes.transAxes,va='top',fontsize=size,color='#173750',linespacing=1.5)
fig.text(.5,.94,'A smooth auxiliary domain with its physical boundary retained',ha='center',fontsize=20,weight='bold',color='#173750')
fig.text(.5,.86,r'$\Omega_{\rm flat}=\{(z,t):t^2-2ct+\psi(z^2)<0\}$',ha='center',fontsize=17,color='#315f78')
fig.text(.5,.10,'DSP-AUX1: a two-dimensional section; the full construction and all original constants are proved in the lesson.',ha='center',fontsize=10.7,color='#405163')
fig.text(.5,.055,'Curves are numerical samples. The dashed window indicates a permitted support; it does not prescribe the cutoff function.',ha='center',fontsize=10.3,color='#405163')
for suffix in ('png','svg'):
 metadata={'Date':None} if suffix=='svg' else {'Software':'AN03-U026-DSP-AUX1-264'}
 fig.savefig(args.output_dir/f'dirichlet-auxiliary-domain-264.{suffix}',dpi=200,facecolor=fig.get_facecolor(),metadata=metadata)
plt.close(fig)
print(f'Rendered DSP-AUX1 section; s_star={s_star:.12f}, L={L:.12f}.')
