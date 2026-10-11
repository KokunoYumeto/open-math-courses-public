"""Original-coordinate residual edge region and full physical coefficients."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.titlesize':15,'axes.labelsize':12})
a=1.3; B=7.8; A=6.5; L=B-2*a; U=min(B,8*a); t0=min(A,L*L/A);t1=min(A,U*U/A)
def fs(b):
    b=np.asarray(b);r=np.sqrt(2)
    return (-2*np.arctan(1-r*b)+2*np.arctan(1+r*b)+np.log(1-r*b+b*b)-np.log(1+r*b+b*b))/(4*r)
def residual(a,A,B):
    if B>=10*a:return 0.
    L=B-2*a;U=min(B,8*a);t0=min(A,L*L/A);t1=min(A,U*U/A)
    first=np.sqrt(L)*fs(np.sqrt(t0/L)) if L>0 else 0.
    return first-np.sqrt(U)*fs(np.sqrt(t1/U))+np.sqrt(A)/2*np.log((A+t1)/(A+t0))
fig=plt.figure(figsize=(14,11),layout='constrained');gs=fig.add_gridspec(2,2,height_ratios=[1,1.05])
ax=fig.add_subplot(gs[0,0]);bx=fig.add_subplot(gs[0,1]);cx=fig.add_subplot(gs[1,:])
u=np.linspace(L,U,500);m=np.minimum(A,u*u/A)
for plot in [ax,bx]:
    plot.set_xlim(L-.6,U+.45);plot.set_ylim(0,A+1.1)
    plot.set_xlabel(r'Original horizontal coordinate $u=s-a$');plot.set_ylabel(r'Original height $t$')
    plot.grid(alpha=.2);plot.axvline(L,color='#66788a',linestyle=':',linewidth=1.2);plot.axvline(U,color='#66788a',linestyle=':',linewidth=1.2)
    plot.set_xticks([L,A,U],[r'$L=26/5$',r'$A=13/2$',r'$U=39/5$'])
ax.fill_between(u,0,m,color='#73b7d3',alpha=.5)
ax.plot(u,u*u/A,color='#28628c',label=r'$t=u^2/A$');ax.plot(u,np.full_like(u,A),color='#bb6744',label=r'$t=A$')
ax.plot(u,m,color='#142f48',linewidth=2.4,label=r'$m(u,A)=\min(A,u^2/A)$')
ax.set_title('Original residual fibers · KR1–KR4')
ax.text(L+.1,1.25,r'$K_2(u,t)\sqrt{t}\geq 0$',fontsize=14)
ax.legend(loc='upper left',fontsize=10,framealpha=.95)
bx.fill_between(u,0,np.minimum(t0,m),color='#9aca8f',alpha=.65,label=r'$0<t<t_0$: lower boundary $L$')
bx.fill_between(u,t0,m,where=m>=t0,color='#b798d5',alpha=.55,label=r'$t_0<t<t_1$: lower boundary $\sqrt{At}$')
bx.plot(u,m,color='#142f48',linewidth=2.4)
bx.axhline(t0,color='#7a5d96',linestyle='--');bx.axhline(t1,color='#66788a',linestyle=':')
for tt in [2.3,5.5]:bx.annotate('',xy=(U,tt),xytext=(max(L,np.sqrt(A*tt)),tt),arrowprops=dict(arrowstyle='<->',color='#273953',lw=2))
bx.text(L-.55,t0+.08,r'$t_0$',fontsize=12);bx.text(U+.12,t1+.08,r'$t_1$',fontsize=12)
bx.set_title('Same region after changing order · KR5–KR8')
bx.legend(loc='upper left',fontsize=10,framealpha=.95)
colors=['#24638d','#9b5540']
for cutoff,color in zip([4*a,6*a],colors):
    hs=np.linspace(.004,cutoff,700);rs=np.array([residual(a,h,cutoff) for h in hs])
    coeff=4*rs/(np.pi*np.sqrt(2*a));l=cutoff-2*a;u0=min(cutoff,8*a)
    bound=4/(np.pi*np.sqrt(2*a))*(.5-fs(1))*(np.sqrt(u0)-np.sqrt(l))
    cx.plot(hs,coeff,color=color,lw=2.3,label=fr'Exact KR6 coefficient, $B={cutoff:g}$')
    cx.hlines(bound,0,cutoff,color=color,linestyle='--',lw=1.5,label=fr'KR9 envelope, $B={cutoff:g}$')
small=np.linspace(0,2*a,240)
cx.plot(small,(small/a)**1.5/(3*np.pi*np.sqrt(2)),color='#386b48',linestyle='-.',lw=1.7,label=r'KR11 bound, only $0\leq A\leq2a$')
cx.set_xlabel(r'Actual inner height $A=\min(B,H)$');cx.set_ylabel(r'Full coefficient $4R/(\pi\sqrt{2a})$')
cx.set_xlim(0,6*a+.12);cx.set_ylim(0,.235);cx.grid(alpha=.2)
cx.set_title(r'Original physical contribution · KR9–KR14 · multiply by $H_y(\omega)$')
cx.legend(loc='upper right',fontsize=10,ncol=2)
fig.suptitle('Exact residual at the original K2 cutoff edge\nActual shift $a=13/10$; upper panels $B=39/5$, $A=13/2$',fontsize=17)
for ext in ['png','svg']:fig.savefig(R/('chen-hou-k2-residual-edge.'+ext),dpi=180)
(R/'chen-hou-k2-residual-edge.json').write_text(json.dumps(dict(parameters={'a':'13/10','B':'39/5','A':'13/2','L':'26/5','U':'39/5'},proof='KR1–KR15',status='Numerical rendering of exact original-coordinate formulas and proved bounds',visual_inspection='pending'),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(figure='chen-hou-k2-residual-edge.png',parameters='original a=13/10, B=39/5, A=13/2')))
