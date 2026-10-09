"""Exact comparison envelope and relative time inclusions, QR17–QR18 and QR43–QR44."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13.5,5.2),layout='constrained')
x=np.linspace(0,1,501)
ax.axhline(1,color='#983f34',lw=2,label=r'first possible crossing: $E_*$')
ax.plot(x,.5+.25*x,color='#286c8e',lw=2.5,label=r'$E_*/2+Q_*(t-s_{\rm start})\leq E_*(1/2+\sigma/4)$')
ax.fill_between(x,0,.5+.25*x,color='#dcecf3')
ax.annotate(r'gap $\geq E_*/4$',(1,.875),xytext=(.48,.84),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set(xlim=(0,1.02),ylim=(0,1.14),xlabel=r'$\sigma=(t-s_{\rm start})/\delta$',ylabel=r'comparison value divided by $E_*$',title='The first crossing is impossible')
ax.legend(loc='lower left',fontsize=9,framealpha=.95)
ax.grid(alpha=.15)
bx.plot([0,1],[2,2],lw=10,color='#b8c7cf',solid_capstyle='butt')
bx.plot([9/16,1],[1,1],lw=10,color='#43849b',solid_capstyle='butt')
bx.plot([25/32,1],[0,0],lw=10,color='#c89948',solid_capstyle='butt')
for xx in (0,9/16,25/32,1):bx.axvline(xx,color='#809099',alpha=.5,lw=.8,ls=':')
bx.set(xlim=(-.03,1.05),ylim=(-.6,2.65),yticks=[0,1,2],yticklabels=['guaranteed region for I′','regularity interval','energy interval J'],
 xticks=[0,9/16,25/32,1],xticklabels=['0','9/16','25/32','1'],
 xlabel=r'$(t-s_{\rm start})/\delta$',title='Every receiving time stays in the original interval')
bx.text(.025,2.35,r'$J\subset I=[a,a+\ell]$',fontsize=11)
bx.text(.05,-.42,r'$T^\prime\leq7\delta/32$: actual $I^\prime$ may be shorter.',fontsize=10)
fig.suptitle('Quantitative regularity: energy margin and exact time domains',fontsize=15)
fig.savefig(ROOT/'quantitative-regularity-interval.png',dpi=170)
fig.savefig(ROOT/'quantitative-regularity-interval.svg')
print('Saved exact comparison envelope and time inclusion figure.')
