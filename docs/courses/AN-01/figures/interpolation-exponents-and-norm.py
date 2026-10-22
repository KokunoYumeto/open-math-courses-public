"""Reciprocal exponents and an exactly computed rank-one norm; CC0.
GPT-6 Astra (OpenAI). AN01-U033 Theorem 7.3 and Solution 14.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parent
if out.name=='work':out=out/'advanced-U186-20261022/new'
out.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-interpolation-exponents-and-norm'})
fig,axes=plt.subplots(1,2,figsize=(12,5.6),layout='constrained')
t=np.linspace(0,1,301)
ax=axes[0]
ax.plot(1-t/2,t/2,color='#196b98',lw=2.5)
for theta,label,offset in [(0,r'$\theta=0:\ (p,q)=(1,\infty)$',(-210,15)),(.5,r'$\theta=1/2:\ (p,q)=(4/3,4)$',(-80,25)),(1,r'$\theta=1:\ (p,q)=(2,2)$',(10,15))]:
    xy=(1-theta/2,theta/2)
    ax.scatter(*xy,color='#196b98',s=40,zorder=3)
    ax.annotate(label,xy=xy,xytext=offset,textcoords='offset points',fontsize=11)
ax.set(xlim=(.4,1.08),ylim=(-.07,.68),xlabel=r'$1/p$',ylabel=r'$1/q$',title='A straight segment of reciprocal exponents')
ax.grid(alpha=.22)
ax=axes[1]
ax.plot(t,4**t,color='#a44425',lw=2.5)
for theta in [0,.5,1]:
    ax.scatter(theta,4**theta,color='#a44425',s=40,zorder=3)
    ax.annotate(str(int(4**theta)),(theta,4**theta),xytext=(10,0),textcoords='offset points')
ax.set(xlim=(-.05,1.12),ylim=(.5,4.7),xlabel=r'$\theta$',ylabel=r'$\|T\|_{L^p\to L^q}$',title=r'Exact norm: $2^{1/p^\prime}8^{1/q}=4^\theta$')
ax.grid(alpha=.22)
fig.suptitle(r'$Tf=1_{[0,8]}\int_0^2 f(x)\,dx$: equality along the whole segment',fontsize=16)
for ext in ['png','svg']:
    p=out/('interpolation-exponents-and-norm.'+ext)
    fig.savefig(p,dpi=160,metadata={'Date':None} if ext=='svg' else {})
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
if out.name=='new':(out/'interpolation-exponents-and-norm.py').write_bytes(Path(__file__).read_bytes())
