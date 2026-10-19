"""Exact parabola and cotangent coordinates for AN01-U101; CC0."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size':12,'svg.hashsalt':'AN01-U101-substitution-parabola','text.usetex':False})
D=Path(__file__).resolve().parent
blue='#17659b';orange='#c16a08';green='#177b56';dark='#24354a'
fig,axs=plt.subplots(1,2,figsize=(12.4,6.7))
s=np.linspace(-1.5,1.5,501)
ax=axs[0]
ax.axhline(0,color=blue,lw=1.5,label=r'$y_2=0$')
ax.axvline(0,color='#b9c1cb',lw=.8)
ax.plot(s,s*s-1,color=dark,lw=2.4,label=r'$F(s)=(s,s^2-1)$')
for root in [-1.,1.]:
 assert root*root-1==0 and 2*root in [-2,2]
 ax.scatter([root],[0],color=dark,s=36,zorder=5)
 ax.annotate('',xy=(root,1.),xytext=(root,0),arrowprops=dict(arrowstyle='->',color=orange,lw=2.2))
 ax.text(root,1.10,r'$(0,1)$',ha='center',color=orange)
ax.text(-1.04,-.19,r'$s=-1$',ha='right',color=dark)
ax.text(1.04,-.19,r'$s=1$',ha='left',color=dark)
ax.set(xlim=(-1.75,1.75),ylim=(-1.3,1.5),xlabel=r'$y_1$',ylabel=r'$y_2$')
ax.set_title('Target coordinates and selected covectors',fontweight='bold',fontsize=13,pad=12)
ax.legend(loc='upper center',frameon=True,facecolor='white',edgecolor='#d3dae3',framealpha=.96)
ax.text(.5,-.17,r'$DF(s)^{T}(0,\eta)=2s\eta$',transform=ax.transAxes,ha='center',fontsize=14)
ax=axs[1]
ax.axhline(0,color='#7d8a9b',lw=1);ax.axvline(0,color='#b9c1cb',lw=.8)
for root in [-1.,1.]:
 ax.plot([root,root],[-2.55,2.55],color=green,lw=2,ls='--',alpha=.55)
 ax.scatter([root],[0],facecolor='white',edgecolor=green,s=38,zorder=6)
 ax.annotate('',xy=(root,2*root),xytext=(root,0),arrowprops=dict(arrowstyle='->',color=orange,lw=2.4))
 ax.scatter([root],[2*root],color=orange,s=30,zorder=5)
ax.text(-1.12,-2.12,r'$(-1,-2)$',ha='right',va='top',color=orange)
ax.text(1.12,2.12,r'$(1,2)$',ha='left',va='bottom',color=orange)
ax.set(xlim=(-2.,2.),ylim=(-2.85,2.85),xlabel=r'$s$',ylabel=r'$\xi$')
ax.set_xticks([-1,0,1]);ax.set_yticks([-2,0,2])
ax.set_title('Source cotangent coordinates',fontweight='bold',fontsize=13,pad=12)
ax.text(.5,-.17,r'$F^*\delta(y_2)=\frac{1}{2}\delta_{-1}+\frac{1}{2}\delta_1$',transform=ax.transAxes,ha='center',fontsize=14)
ax.text(.5,-.27,'Dashed fibers: every nonzero covector',transform=ax.transAxes,ha='center',color=green)
for ax in axs:
 ax.spines[['top','right']].set_visible(False)
 ax.spines[['left','bottom']].set_color('#b9c1cb')
fig.suptitle('Transverse crossings retain both singular points and their positive weights',fontsize=15,y=.98)
fig.subplots_adjust(left=.07,right=.97,top=.86,bottom=.27,wspace=.30)
fig.savefig(D/'analytic-substitution-parabola.png',dpi=150,facecolor='white',metadata={'Software':'GPT-6 Astra (OpenAI); reproducible CC0 figure'})
fig.savefig(D/'analytic-substitution-parabola.svg',facecolor='white',metadata={'Date':None,'Creator':'GPT-6 Astra (OpenAI); CC0'})
p=D/'analytic-substitution-parabola.svg';p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
plt.close(fig)
