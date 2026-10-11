"""Original finite outer-kernel bands and the complete proved height envelope."""
from pathlib import Path
import hashlib,json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent;a=1.3;B=4*a;t0=.7
def J(t):
    rr=np.hypot(a,t);cuts=[0.,B-a]
    for z in [rr*rr-2*t*rr,rr*rr+2*t*rr]:
        if z>0 and 0<np.sqrt(z)<B-a:cuts.append(np.sqrt(z))
    cuts=sorted(set(cuts));us=sorted(set([B-2*a,B]+([t] if B-2*a<t<B else [])))
    P=lambda u:u/(2*(u*u+t*t))
    F=lambda s:P(s-a)-P(s+a)
    return sum(abs(F(y)-F(x)) for x,y in zip(cuts,cuts[1:]))+sum(abs(P(y)-P(x)) for x,y in zip(us,us[1:]))
blue='#365b78';green='#228c7b';red='#b44c3c'
fig,axs=plt.subplots(1,3,figsize=(16.4,5.8),layout='constrained');fig.set_facecolor('#f6f8fb')
for ax in axs:ax.set_facecolor('#f6f8fb');ax.grid(alpha=.17)
ax=axs[0];ss=np.linspace(0,B+a+.25,2400)
K=lambda u:(u*u-t0*t0)/(2*(u*u+t0*t0)**2)
DD=K(ss+a)*(np.abs(ss+a)<=B)-K(ss-a)*(np.abs(ss-a)<=B)
ax.plot(ss,DD,color=blue,lw=1.7,label=r'$D_B(s,7/10)$')
ax.axhline(0,color='gray',lw=.7);ax.axvspan(B-a,B+a,color=green,alpha=.12,label='retained truncation edge')
rr=np.hypot(a,t0)
for z,name in [(rr*rr-2*t0*rr,r'$s_-$'),(rr*rr+2*t0*rr,r'$s_+$')]:
    x=np.sqrt(z);ax.scatter([x],[0],color=red,s=18);ax.annotate(name,(x,0),xytext=(0,12),textcoords='offset points',ha='center')
ax.axvline(B-a,color=green,lw=.8,ls='--');ax.axvline(B+a,color=green,lw=.8,ls='--')
ax.set(xlabel='physical horizontal displacement s',ylabel='original difference kernel',title='A. Every sign interval and both cutoff edges');ax.legend(loc='upper right',fontsize=8.5)
ax=axs[1];ts=np.geomspace(.035,10,450);jj=np.array([J(t) for t in ts]);bounds=np.minimum(1/ts,2*a/ts**2)
assert np.all(jj<=bounds+1e-12)
ax.loglog(ts,jj,color=blue,label='samples of exact finite integral (KO5)')
ax.loglog(ts,bounds,color=green,ls='--',label=r'proved bound $\min(1/t,2a/t^2)$')
ax.axvline(2*a,color=red,ls=':',label=r'$t=2a$')
ax.set(xlabel='physical vertical displacement t',ylabel=r'$J_B(t)$ and its upper bound',title='B. Full horizontal integral, no omitted band');ax.legend(fontsize=8.2)
ax=axs[2];hh=np.linspace(.00005,8*a,800)
finite=np.zeros_like(hh);ix=hh<2*a
finite[ix]=2/np.pi*np.sqrt(hh[ix]/a)*(np.log(2*a/hh[ix])+1-2*a/B)
ix=(hh>=2*a)&(hh<B);finite[ix]=2/np.pi*np.sqrt(hh[ix]/a)*2*a*(1/hh[ix]-1/B)
infinite=np.where(hh<=2*a,2/np.pi*np.sqrt(hh/a)*(np.log(2*a/hh)+1),4/np.pi*np.sqrt(a/hh))
peak=2*a*np.exp(-1-2*a/B);peakval=4/np.pi*np.sqrt(2*np.exp(-1-2*a/B))
ax.plot(hh,finite,color=blue,label='finite-cutoff upper envelope (KO12)');ax.plot(hh,infinite,color=green,ls='--',label='uniform in all larger cutoffs')
ax.scatter([peak],[peakval],color=red,s=22);ax.annotate(r'$H_*=2a e^{-1-2a/B}$',(peak,peakval),xytext=(2.4,.99),arrowprops=dict(arrowstyle='->',color=red),fontsize=9)
ax.axvline(B,color='gray',ls=':',label=r'$H=B$: outer cost is zero')
ax.set(xlabel='original observation height H',ylabel=r'upper bound for $Y_{\rm out}/(\pi\sqrt{2a})$',title='C. Every physical factor and both height limits');ax.legend(loc='upper right',fontsize=8)
fig.suptitle('Original outer K2 cost: exact horizontal integration and complete height bounds\n'+r'$a=13/10,\ B=26/5$'+', with t=7/10 in panel A',fontsize=14)
fig.supxlabel('KO1–KO15. Curves sample exact expressions or proved upper envelopes; they do not certify the remaining interior costs.\nHuman source: Chen–Hou Part II v3, numerical supplement1626–1800; complete source identity in the note.',fontsize=9)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-outer-k2.'+ext),dpi=180)
plt.close(fig)
(R/'chen-hou-outer-k2.json').write_text(json.dumps(dict(parameters=dict(a='13/10',B='26/5',t='7/10'),locators='KO1–KO15',plot_status='Floating rendering of exact expressions and proved bounds; no numerical integral certification',source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2)+'\n',encoding='utf-8',newline='\n')
