"""Reproduce BG, BA and BN figures in their original coordinates."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':13})
def save(fig,name):
 for suffix in ['png','svg']:fig.savefig(R/(name+'.'+suffix),dpi=170,bbox_inches='tight')
 plt.close(fig)
s=np.linspace(-1,1,4001)
fig,ax=plt.subplots(1,2,figsize=(12.2,4.5),constrained_layout=True)
for q,color in [(2,'#296b98'),(2.5,'#ad5522'),(4,'#478a60')]:
 yy=s+s*np.abs(s)**q
 ax[0].plot(yy,-s,color=color,lw=2,label=rf'$\lambda={1/q:g}$')
ax[0].scatter([-2,0,2],[1,0,-1],c='black',s=22,zorder=5)
ax[0].set(xlabel='Original coordinate $y$',ylabel='Original profile $U(y)$',title='The same exact anchor at every exponent',xlim=(-2.15,2.15))
ax[0].legend();ax[0].grid(alpha=.18)
ss=np.linspace(-.22,.22,4001);h=1+3.5*np.abs(ss)**2.5
hp=8.75*np.sign(ss)*np.abs(ss)**1.5;hpp=(105/8)*np.abs(ss)**.5
yy=ss+ss*np.abs(ss)**2.5;u3=hpp/h**4-3*hp**2/h**5
ax[1].plot(yy,u3,color='#ad5522',lw=2.1)
ax[1].scatter([0],[0],c='black',s=22,zorder=4)
ax[1].set(xlabel='Original coordinate $y$',ylabel=r'Exact $U^{(3)}(y)$',title=r'$\lambda=2/5$: the exact third-derivative cusp',xlim=(-.22,.22),ylim=(-.15,4.8))
ax[1].text(.5,.94,r'$U^{(3)}(y)/|y|^{1/2}\to105/8$',transform=ax[1].transAxes,ha='center')
ax[1].grid(alpha=.18)
fig.suptitle('BG3–BG14: implicit fields are plotted through their exact inverse map',fontsize=14)
save(fig,'burgers-real-branch')
def values(ss,delta):
 c=(1+delta*delta)**(-1.25);r=ss*ss+delta*delta
 H=ss+c*ss*r**1.25
 h=1+c*(r**1.25+2.5*ss*ss*r**.25)
 hp=c*(7.5*ss*r**.25+1.25*ss**3*r**(-.75))
 hpp=c*(15/8)*(-ss**4*r**(-1.75)+4*ss*ss*r**(-.75)+4*r**.25)
 hppp=c*(15/16)*ss*r**(-.75)*(7*ss**4/r**2-20*ss*ss/r+20)
 return H,hpp/h**4-3*hp**2/h**5,hppp/h**5-10*hp*hpp/h**6+15*hp**3/h**7
fig,ax=plt.subplots(1,3,figsize=(15.4,4.6),constrained_layout=True)
ss=np.linspace(-.13,.13,4001);h=1+3.5*np.abs(ss)**2.5;hp=8.75*np.sign(ss)*np.abs(ss)**1.5;hpp=(105/8)*np.abs(ss)**.5
ax[0].plot(ss+ss*np.abs(ss)**2.5,hpp/h**4-3*hp**2/h**5,color='black',lw=2,label='Exact limiting profile')
for delta,color in [(.08,'#97bfcf'),(.02,'#367fa8'),(.005,'#ae5725')]:
 yy,u3,_=values(ss,delta);ax[0].plot(yy,u3,color=color,lw=1.8,label=rf'$\delta={delta:g}$')
ax[0].set(xlabel='Original coordinate $y$',ylabel=r'$U_\delta^{(3)}(y)$',title='Smooth profiles approach the cusp',xlim=(-.12,.12),ylim=(-.1,4.7));ax[0].legend(fontsize=9,loc='lower left')
delta=np.geomspace(1e-5,.08,400);c=(1+delta*delta)**(-1.25);h0=1+c*delta**2.5
f3=-1.5*c*delta**.5/h0**4+30*c*c*delta**3/h0**5
ax[1].loglog(delta,np.abs(f3),color='#286b96',lw=2,label='Exact value from BA8')
ax[1].loglog(delta,1.5*np.sqrt(delta),'--',color='#888888',label=r'Leading term $(3/2)\sqrt{\delta}$')
ax[1].set(xlabel=r'Original parameter $\delta$',ylabel=r'$|\partial_y^3 f_\delta(0)|$',title='The tested derivative tends to zero');ax[1].legend(fontsize=9)
yy,u3,u4=values(delta,delta);limit=705/(64*2**.75)
ax[2].loglog(delta,u4,color='#ae5725',lw=2,label='Exact value from BA23')
ax[2].loglog(delta,limit/np.sqrt(delta),'--',color='#888888',label=r'$[705/(64\,2^{3/4})]\delta^{-1/2}$')
ax[2].set(xlabel=r'Original parameter $\delta$',ylabel=r'$U_\delta^{(4)}(H_\delta(\delta))$',title='The profile derivative diverges');ax[2].legend(fontsize=9)
for a in ax:a.grid(alpha=.18)
fig.suptitle(r'BA1–BA25: $\lambda=2/5$; oddness and $U_\delta(-2)=1$ hold exactly',fontsize=14)
save(fig,'burgers-anchored-residuals')
fig,ax=plt.subplots(1,2,figsize=(13,4.8),constrained_layout=True)
ax[0].set(xlim=(0,1),ylim=(0,1));ax[0].axis('off')
labels=['$y$','20 tanh','20 tanh','20 tanh','$N(y)$']
centers=np.linspace(.09,.91,5)
for i,(xx,label) in enumerate(zip(centers,labels)):
 ax[0].add_patch(FancyBboxPatch((xx-.065,.62),.13,.12,boxstyle='round,pad=.012',facecolor='#e4edf4',edgecolor='#32617c'))
 ax[0].text(xx,.68,label,ha='center',va='center',fontsize=10)
 if i<4:ax[0].annotate('',(centers[i+1]-.08,.68),(xx+.08,.68),arrowprops={'arrowstyle':'->','color':'#32617c'})
ax[0].text(.49,.88,'Actual layer sizes; schematic connections',ha='center',fontsize=13)
ax[0].text(.49,.47,r'$U_N(y)=[N(y)-N(-y)]/2$',ha='center',fontsize=14)
ax[0].text(.49,.29,'BN2–BN4: supplied weights and biases\ngive every derivative bound $Q_n$.',ha='center',linespacing=1.6)
ax[0].text(.49,.1,r'BN7: node error $+\;\Delta R_{j+1}/2$',ha='center',fontsize=13)
M=np.geomspace(.1,1000,600);Y0=(29/28)*28**(-.4);c0=(105/16)*(8/9)**5*np.sqrt(28/29)
ym=np.minimum(Y0,c0*c0/(4*M*M));eps=(c0*np.sqrt(ym)-M*ym)/2;threshold=c0/(2*np.sqrt(Y0))
ax[1].loglog(M,eps,lw=2.4,color='#8a3b75');ax[1].axvline(threshold,color='#555555',ls=':')
ax[1].text(.06,.17,r'$\epsilon\geq(c_0\sqrt{y_M}-My_M)/2$'+'\n'+r'$y_M=\min\{Y_0,c_0^2/(4M^2)\}$',transform=ax[1].transAxes)
ax[1].set(xlabel=r'Proved fourth-derivative bound $M$',ylabel=r'Lower bound on $\|V^{(3)}-U_0^{(3)}\|_\infty$',title='BN9–BN13: approximation on the original interval')
ax[1].grid(alpha=.18);fig.suptitle('Finite-network control and a quantitative regularity barrier',fontsize=14)
save(fig,'burgers-network-regularity')
print({'figures':['burgers-real-branch','burgers-anchored-residuals','burgers-network-regularity'],'Y0':Y0,'c0':c0,'fourth_derivative_limit':limit})
