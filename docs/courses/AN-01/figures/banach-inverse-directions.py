"""Sections, retractions and a norm error bound for local inversion.
Original figure: GPT-6 Astra (OpenAI), 2026. CC0.
Run with numpy and matplotlib; writes PNG and SVG beside this source.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,(left,right)=plt.subplots(1,2,figsize=(12.8,5.4))
s=np.linspace(-1.15,1.15,300)
left.plot(s,s*s,color='#155699',lw=2.5,label=r'$i(s)=(s,s^2)$')
left.axhline(0,color='#64748b',lw=1)
left.axvline(0,color='#64748b',lw=1)
a=.7;t=1.25
left.scatter([a,a],[t,a*a],color=['#b45309','#155699'],zorder=4)
left.annotate('',xy=(a,a*a+.03),xytext=(a,t-.03),arrowprops=dict(arrowstyle='->',color='#b45309',lw=2))
left.text(a+.08,t,r'$(s,t)$',color='#b45309')
left.text(a+.08,a*a,r'$(s,s^2)$',color='#155699')
labelbox=dict(facecolor='white',edgecolor='none',alpha=.95,pad=2)
left.text(-1.12,1.4,r'$p(s,t)=s$',fontsize=12,bbox=labelbox)
left.text(-1.12,1.15,r'$p\circ i=\mathrm{id}_{\mathbb{R}}$',fontsize=12,bbox=labelbox)
left.text(-1.12,.9,r'$i\circ p(s,t)=(s,s^2)$',fontsize=12,bbox=labelbox)
left.set(xlim=(-1.25,1.25),ylim=(-.15,1.65),xlabel='First coordinate s',ylabel='Second coordinate t')
left.set_title('A section and its retraction',pad=16)
N=np.arange(0,9)
q=.5
bound=q**N/(1-q)
right.plot(N,bound,'o-',color='#168787',lw=2.3)
right.set_yscale('log',base=2)
right.set(xlabel='Iteration number j',ylabel=r'Upper bound for $\|u-u_j\|/\|z\|$',xticks=N,
          yticks=[2,1,.5,.25,.125,.0625,.03125,.015625,.0078125])
right.set_yticklabels(['2','1','1/2','1/4','1/8','1/16','1/32','1/64','1/128'])
right.grid(axis='y',alpha=.2)
right.set_title(r'$q=1/2:\quad q^j/(1-q)=2^{1-j}$',pad=16)
fig.suptitle('Local inverses: which identity holds, and how fast the iteration converges',fontsize=14,y=.98)
fig.text(.5,.015,'Corollary 5 and estimate (B14). The right panel is a proved norm bound, not a measured trajectory.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.065,1,.92),w_pad=3)
for ext in ['png','svg']:
    p=root/('banach-inverse-directions.'+ext)
    fig.savefig(p,dpi=190,facecolor='white')
    if ext=='svg':p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
