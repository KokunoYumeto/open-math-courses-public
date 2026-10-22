"""Oriented semicircle normalization of Fourier inversion; CC0.
GPT-6 Astra (OpenAI). AN01-U040 Proposition0.6, I1-I4.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U185-20261022/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-fourier-semicircle-signs'})
fig,axes=plt.subplots(1,2,figsize=(12.8,5.7),layout='constrained')
for ax,sgn,col,lab in zip(axes,[-1,1],['#196b98','#a44425'],[r'$H_+$: positive half-line',r'$H_-$: negative half-line']):
    t=np.linspace(0,sgn*np.pi,401)
    ax.plot(np.cos(t),np.sin(t),color=col,lw=2.4)
    ax.plot([-1,1],[0,0],color='#353535',lw=2)
    ax.annotate('',xy=(.24,0),xytext=(-.24,0),arrowprops=dict(arrowstyle='->',color='#353535',lw=2))
    for a in [.27,.7]:
        start=sgn*np.pi*a;end=sgn*np.pi*(a+.08)
        ax.annotate('',xy=(np.cos(end),np.sin(end)),xytext=(np.cos(start),np.sin(start)),arrowprops=dict(arrowstyle='->',color=col,lw=2))
    for x,txt in [(-1,r'$-R$'),(1,r'$R$')]:
        ax.scatter([x],[0],s=22,color=col,zorder=3)
        ax.text(x, -.12*sgn,txt,ha='center',va='bottom' if sgn<0 else 'top')
    ax.text(0,-.32*sgn,r'real segment: $-R\ \longrightarrow\ R$',ha='center',fontsize=11)
    ax.text(0,.44*sgn,r'$\Delta\theta=-\pi$' if sgn<0 else r'$\Delta\theta=\pi$',ha='center',fontsize=14,color=col)
    ax.text(0,.7*sgn,r'$H_+(z)\sim f(0)/(iz)$' if sgn<0 else r'$H_-(z)\sim-f(0)/(iz)$',ha='center',fontsize=12,color=col)
    ax.text(0,-1.44,r'arc integral $\longrightarrow -\pi f(0)$',ha='center',fontsize=13)
    ax.text(0,-1.68,r'real integral $\longrightarrow \pi f(0)$',ha='center',fontsize=13)
    ax.set(xlim=(-1.3,1.3),ylim=(-1.83,1.3),aspect='equal',title=lab)
    ax.axis('off')
fig.suptitle('Fourier inversion: two orientations, equal contributions',fontsize=17)
for ext in ['png','svg']:
    p=out/('fourier-semicircle-signs.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'fourier-semicircle-signs.py').write_bytes(Path(__file__).read_bytes())
