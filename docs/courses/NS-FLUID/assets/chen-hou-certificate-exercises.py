"""Original physical residual domain and the enlarged actual-exponent cell."""
from pathlib import Path
import hashlib,json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve();mp.mp.dps=50
fig,axs=plt.subplots(1,2,figsize=(13,5.8),layout='constrained')
fig.suptitle('Complete middle residual and a larger weighted cell\n'
 'Editorial consequences of the Chen–Hou source comparison · EX5–EX11 and EX21–EX23',fontsize=13)
a=1.3;M=2.6
ss=np.linspace(a,M,400)
B0=M*M+ss*ss+2*a*a;C0=(ss*ss-a*a)*(M*M-a*a)
bb=np.sqrt(2*C0/(B0+np.sqrt(B0*B0+12*C0)))
sigma=(ss-a)*(ss+a)/np.sqrt(ss*ss+a*a+2*np.sqrt(ss**4-a*a*ss*ss+a**4))
ax=axs[0]
ax.fill_between(ss,bb,2.2,color='#bedce4',alpha=.8,label='Residual: all t above b(s), to infinity')
ax.plot(ss,bb,color='#226d83',lw=2,label='Exact residual boundary b(s), EX5')
ax.plot(ss,sigma,color='#bc7331',ls='--',lw=1.8,label='Original sign threshold σₐ(s)')
ax.annotate('Every height above the boundary remains',xy=(1.8,2.05),xytext=(1.47,1.65),
 arrowprops=dict(arrowstyle='->',color='#226d83'),fontsize=9)
ax.text(1.44,.88,'a = 13/10, M = 13/5\nFull residual mass = π/4\nBoth shifted primitive terms retained',fontsize=10,
 bbox=dict(facecolor='white',alpha=.85,edgecolor='none'))
ax.set(xlim=(a,M),ylim=(0,2.2),xlabel='Original coordinate s',ylabel='Original height t',
 title='Full residual domain · displayed finite height window')
ax.legend(fontsize=8,loc='upper left');ax.grid(alpha=.15)
def regular(B):
 d=2+4*B+4*B*B
 return ((mp.log(2)-mp.log(d)+2*mp.log(1+2*B))/B
 +2/B*(mp.pi/4-mp.atan(1+2*B)+mp.atan(2*B))
 -2*mp.log(d)+2*mp.log(1+4*B*B)+4*mp.log(1+2*B)-4*mp.log(2))/4
h=mp.mpf(3)/5
xx=np.linspace(0,float(h/6),300)
yy=[0 if x==0 else float(mp.sqrt(mp.mpf(str(x)))*(regular(mp.mpf(str(x))/h)-mp.log(mp.mpf(str(x))/h))) for x in xx]
ax=axs[1];old=float(h*mp.exp(-2));new=float(h/6)
ax.axvspan(0,old,color='#d5e5ee',label='Source cell: 0 ≤ x ≤ h exp(−2)')
ax.axvspan(old,new,color='#d9e9c9',label='Additional proved range to h/6')
ax.plot(xx,yy,color='#226d83',lw=2,label='Full x¹ᐟ² J₂(x/h), numerical illustration')
ax.axvline(old,color='#778899',ls='--');ax.axvline(new,color='#55813c',ls=':')
ax.text(.033,.32,'Original mesh h = 3/5\nNew right endpoint h/6 = 1/10\nDerivative > 0 on the entire cell\nExact proof uses log(9/2) > 3/2',fontsize=10,
 bbox=dict(facecolor='white',alpha=.9,edgecolor='none'))
ax.set(xlim=(0,.105),ylim=(0,max(yy)*1.22),xlabel='Original physical coordinate x',
 ylabel='Complete weighted integral',title='Actual source exponent α = 1/2 · EX21–EX23')
ax.legend(fontsize=8,loc='upper left');ax.grid(alpha=.15)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=150)
P.with_suffix('.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),
 proof='Lesson54 EX5–EX11 and EX21–EX23',physical_parameters=dict(a='13/10',M='13/5',h='3/5'),
 status='Numerical illustrations of proved full formulas; no sampled certification',human_source='Jiajie Chen and Thomas Y. Hou, Part II v3, original author TeX; exact locators in the lesson'),indent=2)+'\n',encoding='utf-8')
print(P.with_suffix('.png'))
