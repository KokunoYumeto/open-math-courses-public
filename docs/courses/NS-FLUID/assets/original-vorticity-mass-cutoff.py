"""VM5–VM11: original physical cutoff, signed derivative and full support."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,(ax,bx,cx)=plt.subplots(1,3,figsize=(15,6),layout='constrained',gridspec_kw={'width_ratios':[1.12,1,1]})
N=4.;R=2.;core=R/N;outer=2*R/N
ax.add_patch(Circle((0,0),2,facecolor='#edf2f4',edgecolor='#738893',lw=1.5))
ax.add_patch(Circle((1,0),outer,facecolor='#ead1a9',edgecolor='#a77133',lw=2))
ax.add_patch(Circle((1,0),core,facecolor='#bdd7e4',edgecolor='#386f89',lw=2))
ax.scatter([0,1],[0,0],c=['#536b76','#263d49'],s=25,zorder=4)
ax.annotate(r'$x_0=(0,0,0)$',(0,0),xytext=(-40,-26),textcoords='offset points',fontsize=9)
ax.annotate(r'$x_*=(1,0,0)$',(1,0),xytext=(4,-26),textcoords='offset points',fontsize=9)
ax.annotate(r'$\chi=1$',(1,.24),ha='center',color='#24536a',fontsize=12)
ax.annotate(r'$\nabla\chi$ support',(1.25,.7),xytext=(-.8,1.42),arrowprops={'arrowstyle':'->','color':'#8b561c'},color='#8b561c')
ax.text(-1.9,-1.75,'Section x₃ = 0 of original 3D balls.\nThe receiving radius keeps the full center displacement.',fontsize=9)
ax.set(xlim=(-2.15,2.2),ylim=(-2.1,2.1),aspect='equal',xlabel='Original coordinate x₁',ylabel='Original coordinate x₂',title='Core, derivative annulus and receiving ball')
ax.grid(alpha=.12)
def bump(s):
 result=np.zeros_like(s);mask=s>0;result[mask]=np.exp(-1/s[mask]);return result
def bump_prime(s):
 result=np.zeros_like(s);mask=s>0;result[mask]=np.exp(-1/s[mask])/s[mask]**2;return result
r=np.linspace(0,1.3,1801);s=(N*r/(2*R))**2
a=bump(1-s);b=bump(s-.25)
ap=-bump_prime(1-s);bp=bump_prime(s-.25)
chi=a/(a+b);derivative=(ap*b-a*bp)/(a+b)**2*2*(N/(2*R))**2*r
for panel in (bx,cx):
 panel.axvspan(core,outer,color='#ead1a9',alpha=.6)
 panel.axvline(core,color='#738893',ls=':',lw=1);panel.axvline(outer,color='#738893',ls=':',lw=1)
 panel.set(xlim=(0,1.3),xlabel=r'Original radius $r=|y-x_*|$')
 panel.grid(alpha=.15)
bx.plot(r,chi,color='#386f89',lw=2.3)
bx.set(ylim=(-.08,1.15),ylabel=r'$\phi(Nr/(2R))$',title='The exact original radial cutoff')
bx.text(.08,1.05,r'$R/N=1/2$',fontsize=10)
bx.text(.83,.12,r'$2R/N=1$',fontsize=10)
cx.plot(r,derivative,color='#a77133',lw=2.3)
cx.axhline(0,color='#738893',lw=.8)
cx.set(ylabel=r'$d[\phi(Nr/(2R))]/dr$',title='The full signed cutoff derivative')
fig.suptitle('Local original vorticity and the retained exterior velocity contribution',fontsize=15)
fig.savefig(ROOT/'original-vorticity-mass-cutoff.png',dpi=170)
fig.savefig(ROOT/'original-vorticity-mass-cutoff.svg')
print('Saved exact physical cutoff and derivative figure.')
