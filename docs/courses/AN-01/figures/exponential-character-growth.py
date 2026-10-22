"""Exponential characters and exact modulus, CC0.
GPT-6 Astra (OpenAI). AN01-U040 Theorem 0.2 and Solution 9.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U184-20261020/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-exponential-character-growth'})
fig,axes=plt.subplots(1,2,figsize=(12.7,5.3),layout='constrained')
t=np.linspace(-4,4,801)
for a,col,lab in [(0,'#185c9d',r'$e^{it}$'),(.25,'#ac4b28',r'$e^{(1/4+i)t}$')]:
    z=np.exp((a+1j)*t)
    axes[0].plot(z.real,z.imag,lw=2.2,color=col,label=lab)
    axes[1].plot(t,np.exp(a*t),lw=2.2,color=col,label=rf'$|h(t)|=e^{{{a:g}t}}$' if a else r'$|h(t)|=1$')
    for v in [-4,0,4]:
        w=np.exp((a+1j)*v)
        axes[0].scatter([w.real],[w.imag],color=col,s=26,zorder=4)
axes[0].annotate(r'$t=-4$',xy=(np.exp(-1-4j).real,np.exp(-1-4j).imag),xytext=(-1.5,.8),arrowprops={'arrowstyle':'->'},fontsize=11)
axes[0].annotate(r'$t=4$',xy=(np.exp(1+4j).real,np.exp(1+4j).imag),xytext=(-.8,-1.85),arrowprops={'arrowstyle':'->'},fontsize=11)
axes[0].annotate(r'$h(0)=1$',xy=(1,0),xytext=(1.1,-.6),arrowprops={'arrowstyle':'->'},fontsize=11)
axes[0].set(xlabel='Real part',ylabel='Imaginary part',title=r'Characters in the complex plane',aspect='equal')
axes[0].legend(loc='upper left',fontsize=10)
axes[1].set(xlabel=r'$t$',ylabel=r'$|h(t)|$',title=r'Modulus on both sides of zero',xlim=(-4,4),ylim=(0,3))
axes[1].legend(loc='upper left',fontsize=11)
for ax in axes:
    ax.grid(alpha=.22);ax.axhline(0,color='#444444',lw=.7);ax.axvline(0,color='#444444',lw=.7)
fig.suptitle(r'$h(t+s)=h(t)h(s)$; continuous characters are exponential',fontsize=16)
for ext in ['png','svg']:
    p=out/('exponential-character-growth.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'exponential-character-growth.py').write_bytes(Path(__file__).read_bytes())
