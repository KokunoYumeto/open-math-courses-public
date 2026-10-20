"""Original illustration of exact monomial point-mass coefficients.
GPT-6 Astra (OpenAI), 2026. CC0. Numerical coordinates illustrate formula M12.
"""
from pathlib import Path
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'svg.hashsalt':'AN01-U167-monomial-coefficients','font.size':12})
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(9,5.4),layout='constrained')
for k in range(2,8):
    scale=2*math.gamma(1/k)/k
    if k%2:
        x=scale*math.cos(math.pi/(2*k))
        ax.scatter([x],[0],color='#267346',marker='D',s=70,zorder=5)
        ax.annotate(f'k = {k}',(x,0),xytext={3:(1.3,.20),5:(1.55,-.23),7:(2.12,.20)}[k],
                    fontsize=11,va='center',color='#267346',
                    arrowprops={'arrowstyle':'-','color':'#267346','lw':.8})
    else:
        x=scale*math.cos(math.pi/(2*k));y=scale*math.sin(math.pi/(2*k))
        ax.plot([x,x],[-y,y],color='#9aa6ae',ls=':',lw=1)
        for sign,color in [(1,'#176b91'),(-1,'#b04a34')]:
            ax.scatter([x],[sign*y],color=color,s=65,zorder=5)
            ax.annotate(f'k = {k}',(x,sign*y),xytext=(8,2*sign),textcoords='offset points')
ax.scatter([],[],color='#176b91',label='Even degree, positive frequency')
ax.scatter([],[],color='#b04a34',label='Even degree, negative frequency')
ax.scatter([],[],color='#267346',marker='D',label='Odd degree, either frequency sign')
ax.axhline(0,color='#7b858c',lw=.8);ax.axvline(0,color='#7b858c',lw=.8)
ax.set(xlabel=r'Re $C_{k,\sigma}$',ylabel=r'Im $C_{k,\sigma}$',
       title='The coefficient of the limiting point mass',xlim=(0,2.6),ylim=(-1.55,1.55))
ax.grid(alpha=.18);ax.legend(loc='upper left',fontsize=10)
fig.savefig(out/'monomial-concentration-coefficients.png',dpi=180)
fig.savefig(out/'monomial-concentration-coefficients.svg',metadata={'Date':None})
svg=out/'monomial-concentration-coefficients.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
