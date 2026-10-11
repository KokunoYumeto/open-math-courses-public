"""Illustrate the full physical K2 transport and exact singular-square domains."""
from pathlib import Path
import hashlib,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
HERE=Path(__file__).resolve().parent
a,c,H,B=1.3,.7,2.4,6.2
A=min(B,H);s=2.6;L=1.3
def K(u,t):return (u*u-t*t)/(2*(u*u+t*t)**2)
def delta(t):return K(s+a,t)-K(s-a,t)
def partner(t):
    def P(v):return t*v*(v*v+t*v+t*t+2*s*s+2*a*a)-(s*s-a*a)**2
    lo,hi=0.,1.
    while P(hi)<0:hi*=2
    for _ in range(80):
        mid=(lo+hi)/2
        if P(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2
sigma=np.sqrt((-(s*s+a*a)+2*np.sqrt(s**4-s*s*a*a+a**4))/3)
m=partner(A)
plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':11})
fig,axes=plt.subplots(2,2,figsize=(14,11))
fig.patch.set_facecolor('#f8fafc')
ax=axes[0,0]
ax.add_patch(Rectangle((c-a-B,0),2*(B+a),H+B,facecolor='#edf3f9',edgecolor='#47789f',lw=1.3))
for px,color in [(c+a,'#a6423b'),(c-a,'#47789f')]:
    ax.add_patch(Rectangle((px-B,H-B),2*B,2*B,fill=False,edgecolor=color,ls='--',lw=1))
ax.axhline(0,color='#24374e',lw=1.5)
ax.axhline(H,color='#a1b0c1',lw=.8)
ax.scatter([c-a,c+a],[H,H],color=['#47789f','#a6423b'],s=32,zorder=4)
ax.annotate('z = (-0.6, 2.4)',(c-a,H),xytext=(-95,15),textcoords='offset points',fontsize=10)
ax.annotate('x = (2, 2.4)',(c+a,H),xytext=(5,15),textcoords='offset points',fontsize=10)
t=2.;T=partner(t)
ax.annotate('',xy=(c+s,H-T),xytext=(c+s,H-t),arrowprops={'arrowstyle':'->','color':'#1c7b6d','lw':2})
ax.scatter([c+s,c+s],[H-t,H-T],color='#1c7b6d',s=18)
ax.text(c+s+.35,.4,r'$H-t\ \longmapsto\ H-T_s(t)$',fontsize=10,rotation=0)
ax.text(-5.8,7.3,'Original upper data rectangle\nBoth cutoff squares retained',fontsize=10)
ax.set(xlim=(-7.5,8.8),ylim=(-4.3,9.2),xlabel='physical first coordinate',ylabel='physical height',title='A. Original pair, boundary and cutoff squares')
ax.set_aspect('equal',adjustable='box')

bx=axes[0,1];tt=np.linspace(0,A,700);dd=delta(tt)
bx.plot(tt,dd,color='#31445d',lw=1.6)
bx.fill_between(tt,dd,0,where=tt>=sigma,color='#66aaa0',alpha=.5,label='matched positive mass')
bx.fill_between(tt,dd,0,where=(tt>=m)&(tt<=sigma),color='#93b4d7',alpha=.6,label='matched negative mass')
bx.fill_between(tt,dd,0,where=tt<=m,color='#dab16a',alpha=.5,label='residual negative mass')
for val,label in [(m,r'$T_s(A)$'),(sigma,r'$\sigma(s)$'),(A,r'$A$')]:
    bx.axvline(val,color='#667891',lw=.8,ls=':');bx.text(val,.105 if val==A else -.295,label,ha='center',fontsize=11)
for h,y in [(1.5,.027),(1.95,.06),(2.35,.093)]:
    bx.annotate('',xy=(partner(h),y),xytext=(h,y),arrowprops={'arrowstyle':'->','color':'#256d63','lw':1.4})
bx.set(xlim=(0,2.5),ylim=(-.33,.12),xlabel=r'physical vertical displacement $t$',ylabel=r'$\Delta_{a,B}(s,t)$',title='B. The exact upper branch sends mass to its partner')
bx.axhline(0,color='#8a97a6',lw=.6);bx.legend(fontsize=9,loc='lower right')
bx.text(.08,.108,'a = 1.3, s = 2.6, A = 2.4',fontsize=10)

cx=axes[1,0];u=np.linspace(0,L,600)
cx.fill_between(u,u,L,color='#76aba7',alpha=.6,label=r'$C_{\rm up}(L)$: $u\leq t\leq L$')
cx.fill_between(u,0,u*u/L,color='#ddb971',alpha=.6,label=r'$C_{\rm low}(L)$: $0\leq t\leq u^2/L$')
cx.fill_between(u,u*u/L,u,color='#c3d4e7',alpha=.55,label='matched lower mass')
cx.plot(u,u,color='#285a78',lw=1.3);cx.plot(u,u*u/L,color='#886020',lw=1.3)
uu=.65;top=1.08;bottom=uu*uu/top
cx.annotate('',xy=(uu,bottom),xytext=(uu,top),arrowprops={'arrowstyle':'->','color':'#243c61','lw':2})
cx.text(.69,.90,r'$t\mapsto u^2/t$',fontsize=11)
cx.set(xlim=(0,L),ylim=(0,L),xlabel=r'original local displacement $u$',ylabel=r'original local displacement $t$',title='C. Both exact singular-square contributions, L = 1.3')
cx.set_aspect('equal',adjustable='box');cx.legend(fontsize=9,loc='lower right')

dx=axes[1,1];dx.axis('off');dx.set_title('D. Principal-value signs and exact source constants',pad=14)
dx.text(.02,.94,r'$\delta\omega=\omega(x)-\omega(z)$; operator difference is $z-x$',transform=dx.transAxes,fontsize=12)
tab=dx.table(cellText=[[r'$v_x$',r'$+\delta\omega/2$',r'$+\delta\omega/2$',r'$\delta\omega$'],
                      [r'$u_y$',r'$+\delta\omega/2$',r'$-\delta\omega/2$',r'$0$']],
            colLabels=['operator','PV correction','explicit term','total'],cellLoc='center',bbox=[0,.56,1,.29],colWidths=[.15,.30,.30,.25])
tab.auto_set_font_size(False);tab.set_fontsize(12)
for (rr,cc),cell in tab.get_celld().items():
    cell.set_edgecolor('#c9d3de');cell.set_facecolor('#e4edf5' if rr==0 else '#f8fafc')
dx.text(.03,.41,r'$C_{\rm up}(L)=\sqrt{L}\left(\frac{\pi}{2}-\frac{\pi}{2\sqrt{2}}\right)$',transform=dx.transAxes,fontsize=17)
dx.text(.03,.25,r'$C_{\rm low}(L)=\frac{\sqrt{L}}{2}\left(\log 2-2f_s(1)\right)$',transform=dx.transAxes,fontsize=17)
dx.text(.03,.07,r'$C_{K_2}=0.56290143533559718800\ldots$',transform=dx.transAxes,fontsize=13)
fig.suptitle('Original K2 transport: physical geometry, matched mass and every local contribution',fontsize=17,y=.99)
fig.text(.5,.022,'Proof: PV1–PV43. Chen–Hou Parts I and II, exact source versions identified in the note. Curves are drawing samples of proved formulas.',ha='center',fontsize=10)
fig.subplots_adjust(left=.07,right=.97,top=.93,bottom=.09,hspace=.36,wspace=.30)
for ext in ('png','svg'):fig.savefig(HERE/('chen-hou-k2-physical-transport.'+ext),dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
meta={'proof':'CHEN_HOU_K2_PHYSICAL_WORK_20261011.md','locators':'PV1–PV43','kind':'Drawing samples of exact physical domains and maps; exact local-term table',
      'parameters':{'a':'13/10','c':'7/10','H':'12/5','B':'31/5','s':'13/5','L':'13/10'},
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'visual_inspection':'pending'}
(HERE/'chen-hou-k2-physical-transport.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':str(HERE/'chen-hou-k2-physical-transport.png')}))
