"""Exact traces in AN01-U014, Proposition 1.4. Original figure: CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(2,1,figsize=(9,8),layout='constrained')
x=np.r_[np.linspace(-.45,-1e-5,1000),0,np.linspace(1e-5,.45,1000)]
q=np.zeros_like(x);nz=x!=0;q[nz]=x[nz]*(np.log(abs(x[nz]))-1)
ax=axes[0]
ax.plot(x,q,color='#136f8a',lw=2.5,label=r'$\mathrm{Re}\,h^\pm(x)=x(\log|x|-1)$')
ax.axhline(0,color='#8996a3',lw=.8);ax.axvline(0,color='#8996a3',lw=.8)
ax.scatter([0],[0],s=35,color='#136f8a')
ax.set(xlabel='$x$',ylabel='Real trace',title='Continuous at zero; no Lipschitz bound there')
ax.text(.52,.78,r'$|h^\pm(x)|/x=|\log x-1|\to\infty$'+'\n'+r'for $x\downarrow0$',transform=ax.transAxes,fontsize=12)
ax.legend(loc='lower left',frameon=False)
ax=axes[1];jump=np.where(x<0,x,0)
ax.plot(x,jump,color='#b65035',lw=2.5,label=r'$\mathrm{Im}(h^+-h^-)/(2\pi)$')
ax.axhline(0,color='#8996a3',lw=.8);ax.axvline(0,color='#8996a3',lw=.8)
ax.scatter([0],[0],s=35,color='#b65035')
ax.text(.51,.30,r'$q(x)=x\,1_{\{x<0\}}$'+'\n'+r"$q'=1_{\{x<0\}},\quad q''=-\delta_0$",transform=ax.transAxes,fontsize=14)
ax.set(xlabel='$x$',ylabel='Normalized imaginary jump',title='The upper and lower traces retain the side of approach')
ax.legend(loc='upper left',frameon=False)
fig.savefig(out/'logarithmic-boundary-trace.png',dpi=160)
fig.savefig(out/'logarithmic-boundary-trace.svg')
p=out/'logarithmic-boundary-trace.svg'
p.write_text('\n'.join(s.rstrip() for s in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
