"""Original edge transport domain, height-dependent bound and full parameter cell."""
from pathlib import Path
import hashlib,json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent;a=1.3;B=4*a;A=3*a
fig,axs=plt.subplots(1,3,figsize=(16.4,5.7),layout='constrained');fig.set_facecolor('#f6f8fb')
blue='#365b78';green='#228c7b';red='#b44c3c'
for ax in axs:ax.set_facecolor('#f6f8fb');ax.grid(alpha=.16)
ax=axs[0];s=np.linspace(B-a,B+a,500);ax.fill_between(s,np.minimum(s-a,A),A,color=green,alpha=.27)
ax.plot(s,s-a,color=blue,label=r'$t=s-a$');ax.axhline(A,color=red,label=r'$A=3a$')
ss=4.3;tt=3.5;partner=(ss-a)**2/tt
ax.annotate('',xy=(ss,partner),xytext=(ss,tt),arrowprops=dict(arrowstyle='->',color=green,lw=2));ax.scatter([ss,ss],[tt,partner],color=green,s=14)
ax.text(ss+.12,2.65,r'$t\mapsto(s-a)^2/t$',fontsize=10)
ax.set(xlim=(B-a-.15,B+a+.15),ylim=(0,5.5),xlabel='original horizontal displacement s',ylabel='original vertical displacement t',title='A. The original edge and its paired mass');ax.legend(loc='upper left',fontsize=10)
ax=axs[1];h=np.linspace(0,B,600);bound=a**1.5*np.maximum(h-B+2*a,0)**2/(2*(B-2*a)**3);coarse=2*a**3.5/(B-2*a)**3
ax.plot(h,bound,color=green,label='bound retaining actual height');ax.axhline(coarse,color=red,ls='--',label='full-height upper bound')
ax.scatter([A],[np.sqrt(a)/16],color=blue);ax.annotate('one quarter of the full-height bound',xy=(A,np.sqrt(a)/16),xytext=(.15,.14),fontsize=9,arrowprops=dict(arrowstyle='->',color=blue))
ax.set(xlabel='physical height parameter A',ylabel='proved upper bound for E(a,A,B)',title='B. The full area improves the bound (KE5)');ax.legend(loc='upper left',fontsize=9)
ax=axs[2];bb=np.linspace(4*a,6*a,500);ax.fill_between(bb,0,3*a,color=blue,alpha=.1,label='complete parameter cell')
ax.fill_between(bb,np.minimum(bb-2*a,3*a),3*a,color=green,alpha=.35,label='edge can contribute')
ax.plot(bb,bb-2*a,color=blue,label=r'$A=B-2a$')
ax.text(5.15*a,1.4*a,r'$E=0$',fontsize=16);ax.set(xlim=(4*a,6*a),ylim=(0,3.2*a),xlabel='physical cutoff B',ylabel='physical height parameter A',title='C. Exact zero region in the cell (KE6)');ax.legend(loc='lower left',fontsize=9)
fig.suptitle('Original K2 paired edge: both half factors and the complete support\n'+r'$a=13/10$'+', with B=26/5 in panels A–B and A=39/10 in panel A',fontsize=15)
fig.supxlabel('Proof KE1–KE6. Chen–Hou Part II v3, original numerical supplement1505–1528; exact source version in the note.',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-k2-edge.'+ext),dpi=180)
plt.close(fig)
(R/'chen-hou-k2-edge.json').write_text(json.dumps(dict(physical_parameters=dict(a='13/10',A='39/10',B='26/5'),proof_locators='KE1–KE6',plot_status='Exact geometric supports and sampled proved upper bounds; no numerical integral certificate',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n',encoding='utf-8',newline='\n')
