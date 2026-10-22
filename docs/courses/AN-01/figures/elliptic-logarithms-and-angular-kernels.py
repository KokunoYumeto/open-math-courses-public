"""Exact angular functions for two elliptic point-source kernels; CC0.
GPT-6 Astra (OpenAI). AN01-U137 Exercises 5-6, E19-E22.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U188-20261022/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-elliptic-logarithms-and-angular-kernels'})
theta=np.linspace(0,2*np.pi,801)
fig,axes=plt.subplots(1,2,figsize=(12,5.8),layout='constrained')
e0=-np.log(np.cos(theta)**2+np.sin(theta)**2/4)/(8*np.pi)
axes[0].plot(theta,e0,color='#196b98',lw=2.4)
axes[0].set(title=r'$P(\xi)=\xi_1^2+4\xi_2^2,\quad Q_P=1/(4\pi)$',ylabel=r'$E_0(\cos\theta,\sin\theta)$',ylim=(-.008,.068))
axes[0].set_yticks([0,np.log(2)/(4*np.pi)],['0',r'$\log 2/(4\pi)$'])
axes[1].plot(theta,-np.cos(2*theta)/(4*np.pi),color='#196b98',lw=2.4,label=r'$\operatorname{Re}E$')
axes[1].plot(theta,np.sin(2*theta)/(4*np.pi),color='#a44425',lw=2.4,ls='--',label=r'$\operatorname{Im}E$')
axes[1].set(title=r'$P(\xi)=(\xi_1+i\xi_2)^2,\quad Q_P=0$',ylabel=r'$E(\cos\theta,\sin\theta)$',ylim=(-.1,.1))
axes[1].set_yticks([-1/(4*np.pi),0,1/(4*np.pi)],[r'$-1/(4\pi)$','0',r'$1/(4\pi)$'])
axes[1].legend(loc='upper right',fontsize=11)
for ax in axes:
    ax.set(xlim=(0,2*np.pi),xlabel=r'$\theta$')
    ax.set_xticks(np.arange(5)*np.pi/2,['0',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$'])
    ax.grid(alpha=.2)
fig.suptitle('The angular residue decides whether a logarithm is required',fontsize=16)
fig.supxlabel(r'Left: $E=E_0-\log|x|/(4\pi)$.   Right: $E=-\overline{z}/(4\pi z)$ is homogeneous of degree zero.',fontsize=12)
for ext in ['png','svg']:
    p=out/('elliptic-logarithms-and-angular-kernels.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'elliptic-logarithms-and-angular-kernels.py').write_bytes(Path(__file__).read_bytes())
