"""Full residual tail and exact velocity differences, exercises3–4."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
P=Path(__file__).resolve();a=13/10;d=13/100
plt.rcParams.update({'font.size':12})
fig,axs=plt.subplots(1,2,figsize=(13,5),layout='constrained')
h=np.linspace(.001,1.5,1000)
tail=np.pi/4-np.arctan(h/d)/2+np.arctan(h/(2*a+d))/2-np.arctan(h/(2*a))/2
axs[0].plot(h,tail,color='#216b95',label='Complete residual mass above h',lw=2)
axs[0].plot(h,np.minimum(np.pi/4,d/(2*h)),color='#ac563b',ls='--',label=r'Proved bound: $\min(\pi/4,d/(2h))$')
axs[0].scatter([0],[np.pi/4],color='#216b95',s=35)
axs[0].set(xlabel='Actual height h',ylabel='Mass',title='All three original terms retained  ·  EX8–EX9',xlim=(0,1.5),ylim=(0,.87))
axs[0].legend(fontsize=10);axs[0].grid(alpha=.2)
M=np.linspace(a,a+4,800);Du=np.sqrt(M+a)-np.sqrt(M-a)
axs[1].plot(M,Du,color='#21785c',lw=2,label=r'$\mathscr{D}_u=\sqrt{M+a}-\sqrt{M-a}$')
axs[1].plot(M,np.zeros_like(M),color='#7353a6',lw=2,label=r'$\mathscr{D}_v=0$')
axs[1].axhline(np.sqrt(2*a),color='#555555',ls=':',label=r'Proved upper value $\sqrt{2a}$')
axs[1].scatter([a],[np.sqrt(2*a)],facecolors='white',edgecolors='#21785c',s=65,zorder=5)
axs[1].set(xlabel='Actual midpoint height M > a',ylabel='Original velocity-derivative difference',
           title=r'Explicit data $\omega(p,h)=\sqrt{h}$  ·  EX11–EX15',xlim=(a-.1,a+4),ylim=(-.13,1.8))
axs[1].legend(fontsize=10);axs[1].grid(alpha=.2)
fig.suptitle('Original physical shift a = 13/10; middle width d = 13/100',fontsize=15)
for ext in ['png','svg']:fig.savefig(P.with_suffix('.'+ext),dpi=160)
plt.close(fig)
P.with_suffix('.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),
 source_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),parameters=dict(a=a,d=d),
 locators='EX7–EX15; KX11–KX14; RV6–RV9',
 scope='Sampled exact density primitives, proved tail bound and exact velocity differences. No numerical integral certificate.',
 human_sources=['Chen–Hou Parts I v4 and II v3; exact original source locators in the lesson'],
 visual_inspection='pending'),indent=2)+'\n',encoding='utf-8',newline='\n')
print(str(P.with_suffix('.png')))
