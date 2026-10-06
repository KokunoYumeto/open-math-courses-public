"""Exact implication diagram and logarithmic spectral-band schematic for TS1–3."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'oa-flow-iii1-direct-spectral-20261004'})
fig=plt.figure(figsize=(13,7.5),facecolor='#f6f8fb')
ax=fig.add_axes([.045,.56,.91,.29]);ax.axis('off')
boxes=[(.015,'Corner isomorphism',r'$S(pMp)=S(M)=[0,\infty)$','PC8 + full n.s.f. graph transport'),(.355,'One included corner weight',r'$S(pMp)\subseteq\mathrm{Sp}(\Delta_\psi)$',r'$\psi=\varphi|_{pMp}$ is faithful and finite'),(.695,'The same corner action',r'$\mathrm{Sp}(\sigma^\varphi|_{pMp})=\mathbb{R}$','CZ26 + TS1/TS2')]
for x,title,eq,sub in boxes:
 rect=FancyBboxPatch((x,.15),.285,.76,boxstyle='round,pad=.015',facecolor='white',edgecolor='#719ab8',linewidth=1.6,transform=ax.transAxes);ax.add_patch(rect)
 ax.text(x+.1425,.74,title,ha='center',va='center',transform=ax.transAxes,fontsize=12,color='#20354f')
 ax.text(x+.1425,.51,eq,ha='center',va='center',transform=ax.transAxes,fontsize=12)
 ax.text(x+.1425,.28,sub,ha='center',va='center',transform=ax.transAxes,fontsize=9.3,color='#546178')
for x in [.32,.66]:ax.annotate('',xy=(x+.025,.53),xytext=(x-.025,.53),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.8,'color':'#526985'})
ax=fig.add_axes([.115,.15,.77,.25]);ax.set_xlim(-.3,2.3);ax.set_ylim(-.25,.9);ax.set_yticks([])
ax.spines[['left','right','top']].set_visible(False);ax.spines['bottom'].set_position(('data',0));ax.set_xticks([0,.8,1,1.2,2],['0','0.8','1','1.2','2']);ax.set_xlabel(r'Additive variable $r=\log\lambda$',labelpad=10)
ax.plot([.8,1.2],[.3,.3],lw=14,color='#65b6ce',alpha=.35,solid_capstyle='butt');ax.scatter([.8,1.2],[.3,.3],s=85,facecolors='white',edgecolors='#147b9c',linewidths=2,zorder=4)
ax.annotate(r'$1_{(0.8,1.2)}(\log\Delta_\psi)\ne0$',xy=(1,.3),xytext=(1.52,.68),arrowprops={'arrowstyle':'->','color':'#147b9c'},fontsize=12,color='#147b9c')
def log_positive(values):
 # Matplotlib probes zero outside the displayed strictly positive axis range.
 with np.errstate(divide='ignore',invalid='ignore'):return np.log(values)
sec=ax.secondary_xaxis('top',functions=(np.exp,log_positive));sec.set_xticks([np.exp(.8),np.e,np.exp(1.2)],[r'$e^{0.8}$',r'$e$',r'$e^{1.2}$']);sec.set_xlabel(r'Positive variable $\lambda$; the same projection is $1_{(e^{0.8},e^{1.2})}(\Delta_\psi)$',labelpad=12)
fig.suptitle('Full invariant-corner spectrum directly from the III₁ intersection',fontsize=19,color='#20354f',y=.962)
fig.text(.05,.89,r'$M$ is a separable-predual III₁ factor; $0\ne p\in M^{\sigma^\varphi}$; $\varphi$ is faithful, finite and normal.',fontsize=12,color='#546178')
fig.text(.115,.055,r'Density: some $x\Omega$ has a nonzero component in this band. AL20 and AL15 detect the same action spectrum.',fontsize=11,color='#20354f')
fig.text(.115,.018,'The interval is illustrative; every open real interval has nonzero projection. This is not an eigenspace-dimension plot.',fontsize=10,color='#546178')
fig.savefig(HERE/'assets/iii1-direct-spectrum.png',dpi=160,facecolor=fig.get_facecolor())
fig.savefig(HERE/'assets/iii1-direct-spectrum.svg',facecolor=fig.get_facecolor(),metadata={'Date':None})
f=HERE/'assets/iii1-direct-spectrum.svg';f.write_text(f.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
