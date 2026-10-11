"""Draw original residual weights, cutoff band and exact height comparisons."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent;a=1.3;A=2.4;B=5.2
def g(s,h=A):return h/(s*s+h*h)
def weight(s):return np.where((s<a/9)|(s>9*a),np.sqrt(2*s),2*np.sqrt(abs(s-a))-np.sqrt(2*a))
fig,axs=plt.subplots(2,2,figsize=(14,10.8),layout='constrained')
fig.set_facecolor('#f6f8fb');blue='#315570';green='#168477';red='#bd503b'
for ax in axs.flat:
 ax.set_facecolor('#f6f8fb');ax.grid(alpha=.16)
s=np.unique(np.r_[np.linspace(0,13,1100),a/9,a,9*a]);w=weight(s);w0=np.sqrt(2*s)
ax=axs[0,0];ax.plot(s,w0,color=blue,label=r'$\sqrt{2s}$');ax.plot(s,w,color=red,label=r'$w_a(s)$')
ax.fill_between(s,w,w0,where=(s>=a/9)&(s<=9*a),alpha=.18,color=green,label='retained comparison gap')
ax.axhline(0,color='gray',lw=.7)
for x,label in [(a/9,r'$a/9$'),(a,r'$a$'),(9*a,r'$9a$')]:ax.axvline(x,lw=.6,ls=':',color=blue);ax.text(x+.07,(-.25 if x==9*a else -1.25),label)
ax.set(xlabel='original horizontal displacement s',ylabel='original transport cost',title='A. The negative middle weight remains (XR2, XR12)');ax.legend(loc='lower right')
s=np.linspace(0,B+a+.8,1200);di=g(s-a)-g(s+a)
db=g(s-a)*(abs(s-a)<=B)-g(s+a)*(abs(s+a)<=B)
ax=axs[0,1];ax.plot(s,di,color=blue,label=r'$d_\infty(s)$');ax.plot(s,db,color=red,label=r'$d_B(s)$')
ax.axvspan(B-a,B+a,alpha=.12,color=green,label='original boundary band')
ax.set(xlabel='original horizontal displacement s',ylabel='full residual density',title='B. Compare integrals with the boundary band retained (XR7)');ax.legend()
h=np.linspace(.001,12,600);kap=np.sqrt(a/(h+np.sqrt(a*a+h*h)))
ax=axs[1,0];ax.plot(h,kap,color=blue,label=r'$\kappa(a,A)$')
ax.scatter([A],[np.sqrt(a/(A+np.sqrt(a*a+A*A)))],color=red,zorder=5)
ax.set(xlabel='physical height parameter A',ylabel=r'$X_{uy}(a,A,\infty)/(\pi\sqrt{2a})$',title='C. Exact receiving coefficient; all physical factors kept (XR6)')
ax.text(3,.75,r'$a=13/10$'+'\n'+r'$\kappa=\sqrt{a/(A+\sqrt{a^2+A^2})}$',fontsize=12);ax.legend()
h=np.linspace(a/4,a/3,240);integral=3*np.arctan(a/h)-np.arctan(3*a/h)
ax=axs[1,1];ax.plot(h,integral,color=red)
ax.scatter([h[0],h[-1]],[integral[0],integral[-1]],color=blue,zorder=5)
ax.set(xlabel='original height parameter A',ylabel=r'$\int_0^{2a} d_\infty(s;a,A)\,ds$',title='D. Crossing the singular coordinate reverses the estimate (XR18)')
ax.text(.06,.08,r'$[l,u]=[0,2a]$'+'\n'+r'$I^\prime(A)<0$'+'\n'+'endpoint test passes; actual distance is zero',fontsize=10,transform=ax.transAxes)
fig.suptitle('Original Chen–Hou horizontal residuals: exact coefficients and source corrections\n'+r'$a=13/10,\quad A=12/5,\quad B=26/5$'+' in panels A–B; a remains 13/10 throughout',fontsize=16)
fig.supxlabel('Proof XR1–XR18. Chen–Hou Part II v3, exact locators in the note. Curves are drawing samples, not certificates.',fontsize=10)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-horizontal-residual.'+ext),dpi=180)
plt.close(fig)
record=dict(physical_parameters=dict(a='13/10',A='12/5',B='26/5'),proof_locators='XR1–XR18',sampling='Illustration only; all results proved in the accompanying note',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'chen-hou-horizontal-residual.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
