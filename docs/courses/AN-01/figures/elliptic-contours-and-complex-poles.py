"""Contour geometry and exact complex zeros; original figure, CC0.
GPT-6 Astra (OpenAI). AN01-U137 A4-A6 and Exercises11-12.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U189-20261022/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-elliptic-contours-and-complex-poles'})
fig,axes=plt.subplots(1,2,figsize=(12,6),layout='constrained')
u=np.linspace(-6,6,1601);r=np.abs(u)
def flat(t):
    a=np.zeros_like(t);mask=t>0;a[mask]=np.exp(-1/t[mask]);return a
v=flat(r-3);w=flat(4-r);beta=v/(v+w)
curve=.25*r*beta
axes[0].plot(u,curve,lw=2.4,color='#196b98',label=r'$e=e_1$')
axes[0].plot(u,-curve,lw=2.4,color='#a44425',ls='--',label=r'$e=-e_1$')
axes[0].axhline(0,lw=.7,color='black')
for a in [-4,-3,3,4]:axes[0].axvline(a,lw=.8,color='gray',alpha=.4)
axes[0].set(xlabel=r'$\xi_1$ on the real frequency slice',ylabel=r'$\operatorname{Im}\zeta_1$',
            title=r'Fixed direction, $\varepsilon=1/4,\ R=1$',xlim=(-6,6),ylim=(-1.8,1.8))
axes[0].set_xticks([-6,-4,-3,0,3,4,6]);axes[0].legend(loc='upper center')
axes[0].text(0,-.55,r'$\beta=0$ for $|\xi|\leq3$',ha='center')
axes[0].text(0,-1.45,'The spatial half-space determines the sign.',ha='center',fontsize=11)
a=np.linspace(0,2*np.pi,801)
axes[1].add_patch(Circle((0,0),.5,facecolor='#cce7f2',edgecolor='#196b98',lw=1.8))
axes[1].plot(.5*np.cos(a),np.sin(a),color='#a44425',lw=2,ls='--',label=r'$\operatorname{Re}q=0$')
axes[1].scatter([-.5,.5],[0,0],color='#822a22',s=55,zorder=5,label=r'$q=0$')
axes[1].axhline(0,lw=.6,color='gray');axes[1].axvline(0,lw=.6,color='gray')
axes[1].set(xlabel=r'$y_1$',ylabel=r'$y_2$',title=r'$x=(0,1),\quad q(z)=z_1^2+z_2^2/4$',
            xlim=(-.95,.95),ylim=(-1.15,1.15),aspect='equal')
axes[1].set_xticks([-.5,0,.5],[r'$-1/2$','0',r'$1/2$'])
axes[1].text(0,.16,r'$|y|<1/2$',ha='center',fontsize=12)
axes[1].legend(loc='lower center',fontsize=10)
for ax in axes:ax.grid(alpha=.16)
fig.suptitle('Exponential contour decay and the limit imposed by complex poles',fontsize=15)
for ext in ['png','svg']:
    p=out/('elliptic-contours-and-complex-poles.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'elliptic-contours-and-complex-poles.py').write_bytes(Path(__file__).read_bytes())
